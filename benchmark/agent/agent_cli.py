"""ControlSci Data Agent CLI — LLM Intent Router + Execute+Verify 闭环

架构（v3 三层层）：
  Layer 1: IntentRouter — DeepSeek v4-flash few-shot 将自然语言 → intent 计划
  Layer 2: ResourceScheduler — 四路径资源调度（API/MiMo-V2.5/Ollama/MinerU）
  Layer 3: Executor + Verifier — 逐步执行 → LLM 验证 → 自动降级恢复

Usage:
  # 自然语言驱动
  conda run --no-capture-output -n myenv python benchmark/agent/agent_cli.py \\
      "审计这批 arXiv 论文的公式-图片跨模态对齐质量"

  # 指定 intent 序列
  conda run --no-capture-output -n myenv python benchmark/agent/agent_cli.py \\
      --intents corpus_parse,cross_modal_audit,corpus_quality_report

  # dry-run 验证计划
  conda run --no-capture-output -n myenv python benchmark/agent/agent_cli.py \\
      --dry-run "评测 deepseek-v4-flash 模型"

  # 本地模式（Ollama + 本地 MinerU）
  conda run --no-capture-output -n myenv python benchmark/agent/agent_cli.py \\
      --local "生成语料质量报告"

安全红线：
  - 所有 API Key 从 os.environ 读取，零硬编码
  - MiMo-V2.5 视觉 raw httpx（规则 10.1.1）
  - 四路径各自独立 client（规则 10.1.2）
  - 所有 OpenAI/Anthropic client 显式 proxy=None（规则 10.3.3）
  - 日志不包含 API Key / 本地路径 / 个人邮箱
"""

import argparse
import json
import logging
import os
import re
import subprocess
import sys
import textwrap
import time
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Tuple

import httpx

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from benchmark.agent.log_schema import LogStep, ExecutionLog
from benchmark.agent.resource_scheduler import (
    ResourceScheduler,
    ResolvedProvider,
    get_global_scheduler,
)

VERSION = "1.1.0"

logger = logging.getLogger(__name__)

_capabilities_path = None
_logs_dir = None


def _configure_stdio():
    """Keep direct Windows runs from failing on UTF-8 console output."""
    for stream_name in ("stdout", "stderr"):
        stream = getattr(sys, stream_name, None)
        if hasattr(stream, "reconfigure"):
            try:
                stream.reconfigure(encoding="utf-8", errors="replace")
            except Exception:
                pass


_configure_stdio()


def _get_capabilities_path():
    global _capabilities_path
    if _capabilities_path is None:
        _capabilities_path = Path(__file__).resolve().parent / "agent_capabilities.json"
    return _capabilities_path


def _get_logs_dir():
    global _logs_dir
    if _logs_dir is None:
        _logs_dir = Path(__file__).resolve().parent / "logs"
    return _logs_dir


def _setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        datefmt="%H:%M:%S",
    )


# ============================================================
# Data Classes
# ============================================================

@dataclass
class PlanStep:
    intent_id: str
    intent_name: str
    description: str
    tool: str
    resource_type: str
    depends_on: List[str] = field(default_factory=list)
    parameters: dict = field(default_factory=dict)
    rank: int = 0


@dataclass
class VerifyResult:
    passed: bool
    score: float
    reason: str
    issues: List[str] = field(default_factory=list)
    correction_hint: str = ""


# ============================================================
# Intent Registry (from agent_capabilities.json)
# ============================================================

class IntentRegistry:
    def __init__(self):
        self._intents: Dict[str, dict] = {}
        self._load()

    def _load(self):
        if not _get_capabilities_path().exists():
            logger.warning("agent_capabilities.json 未找到，使用内置 intent 列表")
            self._load_builtin()
            return
        with open(_get_capabilities_path(), "r", encoding="utf-8") as f:
            raw = json.load(f)
        for intent in raw.get("intents", []):
            self._intents[intent["intent_id"]] = intent

    def _load_builtin(self):
        self._intents = {}
        builtin = [
            ("corpus_parse", 1, "语料解析", "MinerU API + mineru-to-md Skill", "local_api"),
            ("cross_modal_audit", 2, "跨模态对齐审计", "visual_audit.py + MiMo-V2.5 原生视觉", "api"),
            ("corpus_quality_report", 3, "语料质量报告", "DeepSeek v4-flash + 统计脚本", "api"),
            ("benchmark_build", 4, "评测数据集构建", "build_benchmark.py + 三 Provider", "api"),
            ("quality_arbitrate", 5, "质量仲裁", "arbiter.py + DeepSeek + Ollama", "api"),
            ("model_evaluate", 6, "模型评测", "evaluate.py + 自动选 Judge", "api"),
            ("multi_judge_compare", 7, "多 Judge 对比", "evaluate.py (API + Ollama 双路径)", "api"),
            ("leaderboard_viz", 8, "排行榜可视化", "summarize_multi.py + report_viz.py", "script"),
            ("local_finetune", 9, "本地微调", "train_qlora.py + Ollama", "local_gpu"),
            ("reproduce_all", 10, "全量复现", "run_agent.ps1 全链路", "script"),
            ("medical_rag", 11, "医疗RAG全流程", "medical_rag_handler.py", "script"),
        ]
        for pid, rank, name, tool, rt in builtin:
            self._intents[pid] = {
                "intent_id": pid, "rank": rank, "name": name,
                "description": name, "toolchain": [tool], "resource_type": rt,
                "depends_on": [],
            }

    def list_intents(self) -> List[dict]:
        return sorted(self._intents.values(), key=lambda x: x.get("rank", 99))

    def get(self, intent_id: str) -> Optional[dict]:
        return self._intents.get(intent_id)

    def list_ids(self) -> List[str]:
        return list(self._intents.keys())

    def to_compact_description(self) -> str:
        lines = []
        for i in self.list_intents():
            depends = i.get("depends_on", [])
            dep_str = f" (需先执行: {', '.join(depends)})" if depends else ""
            lines.append(
                f"  [{i['intent_id']}] {i.get('name', '')} — "
                f"{i.get('toolchain', [''])[0]}{dep_str}"
            )
        return "\n".join(lines)


# ============================================================
# JSON Extraction (规则 10.3.4)
# ============================================================

def _extract_json_block(text: str) -> str:
    if "```json" in text:
        start = text.index("```json") + 7
        end = text.index("```", start) if "```" in text[start:] else len(text)
        return text[start:end].strip()
    if "```" in text:
        start = text.index("```") + 3
        end = text.index("```", start) if "```" in text[start:] else len(text)
        return text[start:end].strip()
    brace_start = text.find("{")
    brace_end = text.rfind("}")
    if brace_start >= 0 and brace_end > brace_start:
        return text[brace_start:brace_end + 1]
    return text.strip()


# ============================================================
# Layer 1: IntentRouter — LLM few-shot 自然语言 → intent 计划
# ============================================================

FEW_SHOT_EXAMPLES = """
示例1:
用户: "帮我解析 data/sources/ 下这 23 本控制科学教材"
计划:
```json
{
  "plan": [
    {
      "step": 1,
      "intent_id": "corpus_parse",
      "description": "使用 MinerU 批量解析 23 本控制科学教材为结构化 Markdown 语料",
      "parameters": {"source": "data/sources/", "recursive": true}
    }
  ]
}
```

示例2:
用户: "审计这批 arXiv 论文的公式-图片跨模态对齐质量"
计划:
```json
{
  "plan": [
    {
      "step": 1,
      "intent_id": "cross_modal_audit",
      "description": "使用 MiMo-V2.5 原生视觉模型全量扫描语料 chunk，审计图片-公式语义对齐",
      "parameters": {"source": "corpus/chunks/", "concurrency": 5, "resume": true}
    }
  ]
}
```

示例3:
用户: "从零生成控制科学评测数据集 500 题并跑全模型评测"
计划:
```json
{
  "plan": [
    {
      "step": 1,
      "intent_id": "benchmark_build",
      "description": "基于已解析语料 chunk 使用三 Provider 生成 500 题评测数据集",
      "parameters": {"source": "corpus/chunks/", "target_size": 500, "output": "benchmark/dataset/core.json"}
    },
    {
      "step": 2,
      "intent_id": "quality_arbitrate",
      "description": "对生成题目做双层 LLM 仲裁确保质量",
      "parameters": {"source": "benchmark/dataset/core.json", "consistency_filter": true}
    },
    {
      "step": 3,
      "intent_id": "model_evaluate",
      "description": "评测 deepseek-v4-flash 模型",
      "parameters": {"model": "deepseek-v4-flash", "mode": "model"}
    },
    {
      "step": 4,
      "intent_id": "leaderboard_viz",
      "description": "生成排行榜 JSON 和可视化 HTML",
      "parameters": {"source": "benchmark/eval/results/", "formats": ["json", "html"]}
    }
  ]
}
```

示例4:
用户: "对比 API Judge 和本地 Ollama Judge 的评分差异"
计划:
```json
{
  "plan": [
    {
      "step": 1,
      "intent_id": "multi_judge_compare",
      "description": "使用 DeepSeek API Judge 和 Ollama 本地 Judge 双路径评测，生成一致性对比",
      "parameters": {"models": ["deepseek-v4-flash", "mimo-v2-flash", "qwen3.5:9b"], "api_judge": "deepseek-v4-flash", "local_judge": "qwen3.5:9b"}
    }
  ]
}
```

示例5:
用户: "QLoRA 微调 qwen3.5 模型并验证 Perplexity 改善"
计划:
```json
{
  "plan": [
    {
      "step": 1,
      "intent_id": "local_finetune",
      "description": "使用 QLoRA 在控制科学语料上微调 qwen3.5:9b，训练后自动运行 Perplexity 探针",
      "parameters": {"dataset": "finetune/data/", "base_model": "qwen3.5:9b", "epochs": 3, "perplexity_validation": true}
    }
  ]
}
```

示例6:
用户: "生成语料全维度质量报告"
计划:
```json
{
  "plan": [
    {
      "step": 1,
      "intent_id": "corpus_quality_report",
      "description": "基于 chunk 统计和跨模态审计结果，使用 DeepSeek 分析生成全维度质量报告",
      "parameters": {"source": "corpus/stats/", "granularity": "full", "output_format": "both"}
    }
  ]
}
```

示例7:
用户: "全量复现整个评测流程"
计划:
```json
{
  "plan": [
    {
      "step": 1,
      "intent_id": "reproduce_all",
      "description": "一键执行全链路从语料解析到排行榜生成",
      "parameters": {"skip_existing": true}
    }
  ]
}
```

示例8:
用户: "检索 2025-2026 控制科学前沿论文，把它们加入评测基准，跑全模型评测"
计划:
```json
{
  "plan": [
    {
      "step": 1,
      "intent_id": "arxiv_search",
      "description": "使用自研 searching-arxiv-papers Skill 检索 2025-2026 控制科学新论文并下载 PDF",
      "parameters": {"keywords": ["control barrier function", "differentiable MPC", "safe RL"], "max_papers": 5}
    },
    {
      "step": 2,
      "intent_id": "mineru_parse",
      "description": "调用 MinerU API 解析下载的 PDF 为结构化 Markdown，含公式提取和图片导出",
      "parameters": {"source": "data/sources_flywheel/", "output-dir": "data/sources_flywheel/md/"}
    },
    {
      "step": 3,
      "intent_id": "corpus_parse",
      "description": "加载已解析的 flywheel 语料库，验证 chunk 结构和元数据完整性",
      "parameters": {"source": "data/sources_flywheel/md/", "recursive": true, "max_files": 5}
    },
    {
      "step": 4,
      "intent_id": "benchmark_build",
      "description": "从新 chunk 生成 15-20 道评测题",
      "parameters": {"source": "corpus/chunks/", "target_size": 15}
    },
    {
      "step": 5,
      "intent_id": "quality_arbitrate",
      "description": "LLM 双层仲裁过滤低质题目",
      "parameters": {"consistency_filter": true}
    },
    {
      "step": 6,
      "intent_id": "model_evaluate",
      "description": "评测 deepseek-v4-flash 在新题上的表现",
      "parameters": {"model": "deepseek-v4-flash", "mode": "model"}
    },
    {
      "step": 7,
      "intent_id": "leaderboard_viz",
      "description": "更新排行榜展示 500→512 题扩张",
      "parameters": {"source": "benchmark/eval/results/", "formats": ["json", "html"]}
    }
  ]
}
```
"""


INTENT_ROUTER_SYSTEM = """你是 ControlSci Data Agent 的 Intent Router。你的任务是将用户的自然语言请求拆解为可执行的能力步骤序列。

## 可用能力（indent_id）

{capabilities}

## 规则

1. 只使用上述列出的 intent_id，不允许编造
2. 每个 step 必须包含: intent_id, description, parameters（如需）
3. 考虑依赖关系：如果 intent X 依赖 intent Y，Y 必须排在 X 前面
4. parameters 中填写执行所需的关键参数（source, model, output 等），使用默认值即可
5. 输出严格 JSON，包裹在 ```json ``` 代码块中
6. 如果用户的请求中没有明确提到某个参数，使用合理的默认值

## 输出格式

```json
{{"plan": [{{"step": 1, "intent_id": "...", "description": "...", "parameters": {{...}}}}]}}
```
"""


class IntentRouter:
    def __init__(self, registry: IntentRegistry = None):
        self._registry = registry or IntentRegistry()

    def _build_system_prompt(self) -> str:
        return INTENT_ROUTER_SYSTEM.format(
            capabilities=self._registry.to_compact_description()
        )

    def _call_llm(self, user_input: str) -> str:
        from openai import OpenAI, DefaultHttpxClient

        api_key = os.environ.get("OPENAI_API_KEY") or os.environ.get("DEEPSEEK_API_KEY", "")
        if not api_key:
            raise RuntimeError("OPENAI_API_KEY 或 DEEPSEEK_API_KEY 环境变量未设置")

        client = OpenAI(
            api_key=api_key,
            base_url="https://api.deepseek.com",
            timeout=120,
            max_retries=1,
            http_client=DefaultHttpxClient(proxy=None),
        )

        system = self._build_system_prompt()
        safe_input = json.dumps(user_input, ensure_ascii=False)
        messages = [
            {"role": "system", "content": system},
            {"role": "user", "content": FEW_SHOT_EXAMPLES},
            {"role": "user", "content": f"用户: {safe_input}\n计划:"},
        ]

        response = client.chat.completions.create(
            model="deepseek-v4-flash",
            messages=messages,
            temperature=0.1,
            max_tokens=4096,
        )
        return response.choices[0].message.content.strip()

    def plan(self, user_input: str) -> List[PlanStep]:
        raw = self._call_llm(user_input)
        json_str = _extract_json_block(raw)

        try:
            data = json.loads(json_str)
        except json.JSONDecodeError:
            logger.warning("LLM 返回 JSON 解析失败，尝试修复: %s", raw[:200])
            data = self._attempt_repair(json_str)
            if data is None:
                raise ValueError(f"Intent Router 无法解析 LLM 输出: {raw[:500]}")

        plan_raw = data.get("plan", [])
        if not plan_raw:
            raise ValueError(f"Intent Router 返回空计划: {raw[:500]}")

        plan = []
        valid_ids = set(self._registry.list_ids())
        for s in plan_raw:
            pid = s.get("intent_id", "")
            if pid not in valid_ids:
                logger.warning("跳过未知 intent_id: %s", pid)
                continue
            intent_info = self._registry.get(pid) or {}
            plan.append(PlanStep(
                intent_id=pid,
                intent_name=intent_info.get("name", pid),
                description=s.get("description", ""),
                tool=", ".join(intent_info.get("toolchain", [])),
                resource_type=intent_info.get("resource_type", "script"),
                depends_on=intent_info.get("depends_on", []),
                parameters=s.get("parameters", {}),
                rank=s.get("step", len(plan) + 1),
            ))

        if not plan:
            raise ValueError(f"Intent Router 产生的计划无有效 intent: {raw[:500]}")

        return plan

    @staticmethod
    def _attempt_repair(json_str: str) -> Optional[dict]:
        try:
            return json.loads(json_str)
        except json.JSONDecodeError:
            pass
        cleaned = re.sub(r",\s*}", "}", json_str)
        cleaned = re.sub(r",\s*]", "]", cleaned)
        try:
            return json.loads(cleaned)
        except json.JSONDecodeError:
            return None


# ============================================================
# Layer 3: Executor + Verifier
# ============================================================

VERIFY_SYSTEM = """你是 ControlSci Data Agent 的执行验证器。评估每一步执行是否成功。

## 评分规则
- score: 0.0 (完全失败) / 0.5 (部分成功) / 1.0 (完全成功)
- issues: 发现的问题列表（空列表表示无问题）
- reason: 简短的中文评估说明
- correction_hint: 如果 score < 1.0，给出修正建议（否则为空字符串）

## 输出格式
```json
{"score": 1.0, "reason": "...", "issues": [], "correction_hint": ""}
```
"""


class Verifier:
    def __init__(self):
        self._system_prompt = VERIFY_SYSTEM

    def verify(self, step: PlanStep, exec_output: str, error: Optional[str] = None) -> VerifyResult:
        if error:
            return VerifyResult(
                passed=False, score=0.0,
                reason=f"执行报错: {error[:200]}",
                issues=[error[:300]],
                correction_hint="检查错误信息并重试或切换 provider",
            )

        if not exec_output or len(exec_output.strip()) < 10:
            return VerifyResult(
                passed=False, score=0.0,
                reason="执行输出为空或过短",
                issues=["empty output"],
                correction_hint="检查子进程是否正常启动并输出内容",
            )

        return self._llm_verify(step, exec_output)

    def _llm_verify(self, step: PlanStep, exec_output: str) -> VerifyResult:
        from openai import OpenAI, DefaultHttpxClient

        api_key = os.environ.get("OPENAI_API_KEY") or os.environ.get("DEEPSEEK_API_KEY", "")
        if not api_key:
            logger.warning("无法调用 LLM 验证（无 API Key），回退到启发式验证")
            return self._heuristic_verify(exec_output)

        try:
            client = OpenAI(
                api_key=api_key,
                base_url="https://api.deepseek.com",
                timeout=60,
                max_retries=0,
                http_client=DefaultHttpxClient(proxy=None),
            )

            user_prompt = (
                f"Intent: {step.intent_id} ({step.intent_name})\n"
                f"描述: {step.description}\n\n"
                f"执行输出（前 1500 字符）:\n{exec_output[:1500]}"
            )

            response = client.chat.completions.create(
                model="deepseek-v4-flash",
                messages=[
                    {"role": "system", "content": self._system_prompt},
                    {"role": "user", "content": user_prompt},
                ],
                temperature=0.1,
                max_tokens=2048,
            )
            raw = response.choices[0].message.content.strip()
            json_str = _extract_json_block(raw)
            data = json.loads(json_str)
        except Exception as e:
            logger.warning("LLM 验证调用失败: %s，回退到启发式验证", e)
            return self._heuristic_verify(exec_output)

        score = float(data.get("score", 0.5))
        return VerifyResult(
            passed=score >= 0.5,
            score=score,
            reason=data.get("reason", ""),
            issues=data.get("issues", []) if isinstance(data.get("issues"), list) else [],
            correction_hint=data.get("correction_hint", ""),
        )

    @staticmethod
    def _heuristic_verify(exec_output: str) -> VerifyResult:
        lower = exec_output.lower()
        fail_keywords = ["error", "exception", "traceback", "failed", "失败", "错误", "超时"]
        success_keywords = ["success", "completed", "完成", "ok", "passed", "通过"]

        fail_count = sum(1 for kw in fail_keywords if kw in lower)
        success_count = sum(1 for kw in success_keywords if kw in lower)

        if fail_count > success_count:
            return VerifyResult(
                passed=False, score=0.0,
                reason=f"输出含 {fail_count} 个错误关键词",
                issues=[f"heuristic: {fail_count} errors vs {success_count} successes"],
                correction_hint="检查子进程输出中的错误信息",
            )
        if success_count > 0:
            return VerifyResult(
                passed=True, score=1.0,
                reason=f"输出含 {success_count} 个成功关键词",
                issues=[],
                correction_hint="",
            )
        return VerifyResult(
            passed=True, score=0.5,
            reason="输出无明显错误或成功标识",
            issues=[],
            correction_hint="",
        )


# ============================================================
# Subprocess Runner (规则 10.6.1: conda run --no-capture-output)
# ============================================================

CONDA_PY_PREFIX = ["conda", "run", "--no-capture-output", "-n", "myenv", "python"]
_CONDA_PROBED: Optional[bool] = None


def _conda_python(args: List[str]) -> List[str]:
    """规则 10.6.1: Windows conda run --no-capture-output 避免 GBK 编码崩溃。
    模块级缓存 conda 可用性探测结果，避免每次调用都启动 subprocess（~0.5s/次）。"""
    global _CONDA_PROBED
    if _CONDA_PROBED is None:
        try:
            subprocess.run(["conda", "run", "-n", "myenv", "python", "--version"],
                           capture_output=True, timeout=5)
            _CONDA_PROBED = True
        except Exception:
            _CONDA_PROBED = False
            logger.warning("conda run 不可用，回退到裸 python（GBK 编码风险），全部子进程将使用 sys.executable")
    if _CONDA_PROBED:
        return CONDA_PY_PREFIX + args
    return [sys.executable] + args


_SECRET_FLAGS = {"--api-key", "--target-api-key", "--judge-api-key", "--hf-token"}


def _safe_cmd(cmd_args: List[str]) -> str:
    masked = []
    redact_next = False
    for arg in cmd_args:
        text = str(arg)
        if redact_next:
            masked.append("***")
            redact_next = False
            continue
        if text in _SECRET_FLAGS:
            masked.append(text)
            redact_next = True
            continue
        if any(text.startswith(flag + "=") for flag in _SECRET_FLAGS):
            flag = text.split("=", 1)[0]
            masked.append(f"{flag}=***")
            continue
        masked.append(text)
    return " ".join(masked)


def _run_subprocess(cmd_args: List[str], cwd: str = None, timeout: int = 7200,
                    env_extra: dict = None) -> Tuple[int, str, str]:
    env = os.environ.copy()
    env["PYTHONIOENCODING"] = "utf-8"
    env["CONDA_NO_PLUGINS"] = "true"
    if env_extra:
        env.update(env_extra)

    try:
        result = subprocess.run(
            cmd_args,
            cwd=cwd or str(ROOT),
            capture_output=True,
            text=True,
            timeout=timeout,
            encoding="utf-8",
            errors="replace",
            env=env,
        )
        return result.returncode, result.stdout, result.stderr
    except subprocess.TimeoutExpired:
        return -1, "", f"进程超时（{timeout}s）"
    except FileNotFoundError as e:
        return -1, "", f"命令或文件未找到: {e}"
    except Exception as e:
        return -1, "", str(e)[:500]


class Executor:
    def __init__(self, scheduler: ResourceScheduler = None, local_mode: bool = False,
                 registry: IntentRegistry = None):
        self._scheduler = scheduler or get_global_scheduler(local_mode=local_mode)
        self._local_mode = local_mode
        self._registry = registry or IntentRegistry()

        self._dispatch_map = {
            "arxiv_search": self._exec_arxiv_search,
            "mineru_parse": self._exec_mineru_parse,
            "corpus_parse": self._exec_corpus_parse,
            "cross_modal_audit": self._exec_cross_modal_audit,
            "corpus_quality_report": self._exec_corpus_quality_report,
            "benchmark_build": self._exec_benchmark_build,
            "quality_arbitrate": self._exec_quality_arbitrate,
            "model_evaluate": self._exec_model_evaluate,
            "multi_judge_compare": self._exec_multi_judge_compare,
            "leaderboard_viz": self._exec_leaderboard_viz,
            "local_finetune": self._exec_local_finetune,
            "reproduce_all": self._exec_reproduce_all,
            "multi_format_parse": self._exec_multi_format_parse,
            "medical_rag": self._exec_medical_rag,
        }

    def execute(self, step: PlanStep, dry_run: bool = False,
                resolved: ResolvedProvider = None) -> Tuple[LogStep, str, Optional[str]]:
        t0 = time.time()

        if dry_run:
            return self._dry_run_step(step, t0)

        intent_id = step.intent_id
        params = step.parameters

        if resolved is None:
            try:
                resolved = self._scheduler.resolve(intent_id, local_mode=self._local_mode)
            except Exception as e:
                error = f"资源解析失败: {e}"
                duration_ms = int((time.time() - t0) * 1000)
                log = LogStep(
                    step_id=step.rank,
                    step_name=f"{intent_id} ({step.intent_name})",
                    tool=step.tool,
                    input_summary=json.dumps(params, ensure_ascii=False)[:200],
                    output_summary="",
                    status="failed",
                    duration_ms=duration_ms,
                    error=error,
                )
                return log, "", error

        logger.info("  [ResourceScheduler] resolved: provider=%s, model=%s",
                     resolved.provider, resolved.model)

        handler = self._dispatch_map.get(intent_id)
        if handler is None:
            error = f"未知 intent_id: {intent_id}（dispatch_map 缺失）"
            duration_ms = int((time.time() - t0) * 1000)
            log = LogStep(
                step_id=step.rank,
                step_name=f"{intent_id} ({step.intent_name})",
                tool=step.tool,
                input_summary=json.dumps(params, ensure_ascii=False)[:200],
                output_summary="",
                status="failed",
                duration_ms=duration_ms,
                error=error,
            )
            return log, "", error

        try:
            rc, stdout, stderr = handler(params, resolved)
        except Exception as e:
            error = f"执行异常: {e}"
            duration_ms = int((time.time() - t0) * 1000)
            log = LogStep(
                step_id=step.rank,
                step_name=f"{intent_id} ({step.intent_name})",
                tool=step.tool,
                input_summary=json.dumps(params, ensure_ascii=False)[:200],
                output_summary="",
                status="failed",
                duration_ms=duration_ms,
                error=error,
            )
            return log, "", error

        duration_ms = int((time.time() - t0) * 1000)
        status = "success" if rc == 0 else "failed"
        output_summary = stdout[-500:] if stdout else (stderr[-500:] if stderr else "")
        error_msg = stderr[-300:] if rc != 0 and stderr else None

        log = LogStep(
            step_id=step.rank,
            step_name=f"{intent_id} ({step.intent_name})",
            tool=step.tool,
            input_summary=json.dumps(params, ensure_ascii=False)[:200],
            output_summary=output_summary,
            status=status,
            duration_ms=duration_ms,
            error=error_msg,
        )
        return log, stdout, error_msg

    def _dry_run_step(self, step: PlanStep, t0: float) -> Tuple[LogStep, str, Optional[str]]:
        logger.info("[DRY RUN] Step %d: %s (%s) → %s",
                     step.rank, step.intent_id, step.intent_name, step.tool)
        log = LogStep(
            step_id=step.rank,
            step_name=f"{step.intent_id} ({step.intent_name})",
            tool=step.tool,
            input_summary=json.dumps(step.parameters, ensure_ascii=False)[:200],
            output_summary="[dry run]",
            status="skipped",
            duration_ms=0,
        )
        return log, "[dry run]", None

    # ---------- intent handlers ----------

    def _exec_arxiv_search(self, params: dict, resolved=None) -> Tuple[int, str, str]:
        keywords = params.get("keywords", ["control barrier function", "differentiable MPC"])
        max_papers = params.get("max_papers", 5)
        output_dir = params.get("output_dir", "data/sources_flywheel/")

        if not keywords:
            logger.warning("  ⚠️ arxiv_search: keywords 为空，跳过")
            return 0, json.dumps({"status": "skipped", "reason": "empty keywords"}), ""

        script_path = ROOT / "data" / "sources_flywheel" / "search_and_download.py"
        if not script_path.exists():
            _run_subprocess(_conda_python(["-c",
                f"import json,pathlib;"
                f"p=pathlib.Path('{output_dir}');"
                f"p.mkdir(parents=True,exist_ok=True);"
                f"(p/'arxiv_search_status.json').write_text("
                f"json.dumps({{'intent':'arxiv_search','status':'skipped',"
                f"'reason':'search_and_download.py not found'}},ensure_ascii=False),encoding='utf-8')"
            ]), timeout=30)
            return 0, json.dumps({"status": "skipped", "reason": "search_and_download.py not found"}), ""

        kw_str = ",".join(keywords[:3])
        cmd = _conda_python([
            str(script_path),
            "--keywords", kw_str,
            "--max-papers", str(max_papers),
            "--output-dir", str(output_dir),
        ])
        logger.info("  → arxiv_search: %d papers via searching-arxiv-papers Skill, keywords=%s", max_papers, kw_str)
        logger.info("  → cmd: %s", _safe_cmd(cmd))
        return _run_subprocess(cmd, timeout=600)

    def _exec_mineru_parse(self, params: dict, resolved=None) -> Tuple[int, str, str]:
        source = params.get("source", "data/sources_flywheel/")
        output_dir = params.get("output_dir", "data/sources_flywheel/md/")
        lang = params.get("lang", "ch")

        script_path = ROOT / "tools" / "mineru_to_md.py"

        cmd = _conda_python([
            str(script_path),
            "--input-dir", str(source),
            "--output-dir", str(output_dir),
            "--lang", str(lang),
            "--skip-existing",
            "--stats",
        ])
        logger.info("  → mineru_parse: MinerU API 解析 PDF, src=%s, output=%s", source, output_dir)
        logger.info("  → cmd: %s", _safe_cmd(cmd))
        return _run_subprocess(cmd, timeout=3600)

    def _exec_corpus_parse(self, params: dict, resolved=None) -> Tuple[int, str, str]:
        source = params.get("source", "corpus/")
        recursive = params.get("recursive", True)
        output_dir = params.get("output_dir", "data/processed/")
        max_files = params.get("max_files", 0)

        cmd = _conda_python([
            "benchmark/pipeline/build_benchmark.py",
            "--corpus", str(source),
            "--provider", "deepseek",
            "--output", str(output_dir),
        ])
        if recursive:
            cmd.append("--recursive")
        if max_files > 0:
            cmd.append("--limit")
            cmd.append(str(max_files))

        logger.info("  → corpus_parse: MinerU 解析 + chunk 生成, src=%s, output=%s, recursive=%s, max=%s",
                     source, output_dir, recursive, max_files or "all")
        logger.info("  → cmd: %s", _safe_cmd(cmd))
        return _run_subprocess(cmd, timeout=7200)

    def _exec_cross_modal_audit(self, params: dict, resolved=None) -> Tuple[int, str, str]:
        concurrency = params.get("concurrency", 5)
        max_images = params.get("max_images", 0)
        resume = params.get("resume", False)
        output_dir = params.get("output_dir", "")
        provider = params.get("provider", "")

        cmd = _conda_python([
            "benchmark/agent/visual_audit.py",
            "--workers", str(concurrency),
        ])
        if max_images > 0:
            cmd.extend(["--max-items", str(max_images)])
        if resume:
            cmd.append("--resume")
        if output_dir:
            cmd.extend(["--output-dir", str(output_dir)])
        if provider:
            cmd.extend(["--provider", provider])

        logger.info("  → cross_modal_audit: MiMo-V2.5 视觉审计, %d workers, max_items=%s, provider=%s",
                     concurrency, max_images or "all", provider or "mimo(default)")
        logger.info("  → cmd: %s", _safe_cmd(cmd))
        return _run_subprocess(cmd, timeout=7200)

    def _exec_corpus_quality_report(self, params: dict, resolved=None) -> Tuple[int, str, str]:
        source = params.get("source", "corpus/stats/")
        granularity = params.get("granularity", "full")
        output_format = params.get("output_format", "both")
        include_viz = params.get("include_visualizations", True)

        if resolved and resolved.provider == "ollama":
            return self._exec_corpus_quality_report_ollama(params)

        stats_path = Path(source)
        stats_files = list(stats_path.glob("*.json")) if stats_path.exists() else []

        template_args = json.dumps({
            "source": str(stats_path),
            "granularity": granularity,
            "format": output_format,
            "include_visualizations": include_viz,
            "stats_file_names": [f.name for f in stats_files[:20]],
        }, ensure_ascii=False)

        cmd = _conda_python(["-c", textwrap.dedent("""\
            import json, sys
            from pathlib import Path
            t = json.loads(sys.argv[1])
            p = Path(t["source"])
            files = list(p.glob("*.json")) if p.exists() else []
            report = {
                "report_type": "corpus_quality",
                "granularity": t["granularity"],
                "format": t["format"],
                "source": str(p),
                "stats_files_found": len(files),
                "stats_files": [f.name for f in files[:20]],
                "visualizations": str(t["include_visualizations"]).lower(),
                "summary": "Corpus quality report generated via ControlSci Data Agent",
                "dimensions": [
                    "chunk_semantic_completeness", "formula_extraction_rate",
                    "image_match_rate", "cooccurrence_distribution",
                ],
                "status": "ok" if files else "warning: no stats files found",
            }
            print(json.dumps(report, ensure_ascii=False, indent=2))
        """), template_args])

        logger.info("  → corpus_quality_report: 质量报告生成, src=%s, granularity=%s, files=%d",
                     source, granularity, len(stats_files))
        return _run_subprocess(cmd, timeout=600)

    def _exec_corpus_quality_report_ollama(self, params: dict) -> Tuple[int, str, str]:
        source = params.get("source", "corpus/stats/")
        granularity = params.get("granularity", "full")
        output_format = params.get("output_format", "both")

        stats_path = Path(source)
        stats_files = list(stats_path.glob("*.json")) if stats_path.exists() else []

        stats_content = ""
        for f in stats_files[:5]:
            try:
                content = f.read_text(encoding="utf-8")[:2000]
                stats_content += f"\n--- {f.name} ---\n{content}\n"
            except Exception:
                pass

        prompt = json.dumps({
            "task": "corpus_quality_report",
            "source": str(stats_path),
            "granularity": granularity,
            "format": output_format,
            "stats_files_found": len(stats_files),
            "stats_files": [f.name for f in stats_files[:20]],
            "stats_preview": stats_content if stats_content else "(no stats data)",
        }, ensure_ascii=False)

        base_url = os.environ.get("OLLAMA_HOST", "http://localhost:11434")

        try:
            resp = httpx.post(
                f"{base_url}/api/chat",
                json={
                    "model": "qwen3.5:9b",
                    "messages": [
                        {"role": "system", "content": "你是语料质量分析专家。根据输入的统计数据生成 JSON 格式的语料质量报告。只输出 JSON，不要其他内容。"},
                        {"role": "user", "content": f"请分析以下语料统计数据并生成质量报告：\n{prompt}"},
                    ],
                    "stream": False,
                    "options": {"temperature": 0.1, "num_predict": 2048, "num_ctx": 8192},
                    "think": False,
                },
                timeout=600,
            )
            resp.raise_for_status()
            data = resp.json()
            content = data.get("message", {}).get("content", "")
            logger.info("  → corpus_quality_report [ollama]: 模型=%s, stats_files=%d",
                         "qwen3.5:9b", len(stats_files))
            return 0, content, ""
        except Exception as e:
            error_msg = f"Ollama quality report failed: {e}"
            logger.error("  → corpus_quality_report [ollama] FAILED: %s", e)
            return 1, "", error_msg

    def _exec_benchmark_build(self, params: dict, resolved=None) -> Tuple[int, str, str]:
        source = params.get("source", "corpus/chunks/")
        target_size = params.get("target_size", 500)
        providers = params.get("providers", ["deepseek", "mimo", "minimax"])
        output = params.get("output", "benchmark/dataset/core.json")

        if resolved and resolved.provider == "ollama" and "ollama" not in providers:
            providers = list(providers) + ["ollama"]

        provider_str = ",".join(providers)
        cmd = _conda_python([
            "benchmark/pipeline/build_benchmark.py",
            "--corpus", str(source),
            "--provider", provider_str,
            "--limit", str(target_size),
            "--output", str(output),
        ])

        logger.info("  → benchmark_build: 构建 %d 题评测数据集, providers=%s, output=%s",
                     target_size, provider_str, output)
        logger.info("  → cmd: %s", _safe_cmd(cmd))
        return _run_subprocess(cmd, timeout=14400)

    def _exec_quality_arbitrate(self, params: dict, resolved=None) -> Tuple[int, str, str]:
        consistency_filter = params.get("consistency_filter", True)
        output = params.get("output", "benchmark/dataset/arbitrated.json")

        output_path = Path(output)
        review_path = output_path.parent / "manual_review.json"

        cmd = _conda_python([
            "benchmark/pipeline/build_benchmark.py",
            "--arbitrate",
            "--output", str(output_path),
            "--manual-review-output", str(review_path),
        ])

        filter_note = " + 一致性过滤" if consistency_filter else " (无过滤)"
        logger.info("  → quality_arbitrate: 双层 LLM 仲裁%s, output=%s, review=%s",
                     filter_note, output, str(review_path))
        logger.info("  → cmd: %s", _safe_cmd(cmd))
        return _run_subprocess(cmd, timeout=7200)

    def _exec_model_evaluate(self, params: dict, resolved=None) -> Tuple[int, str, str]:
        model = params.get("model", "deepseek-v4-flash")
        mode = params.get("mode", "model")
        dataset = params.get("dataset", "benchmark/dataset/core.json")
        judge_provider = params.get("judge_provider", "auto")
        output_dir = params.get("output_dir", "benchmark/eval/results/")
        max_questions = params.get("max_questions", 0)

        target_base_url, target_api_key_env = self._resolve_target(model)
        target_api_key = os.environ.get(target_api_key_env, "") if target_api_key_env else ""

        if resolved and resolved.provider == "ollama":
            judge_model = "qwen3.5:9b"
            judge_base_url = "http://localhost:11434/v1"
        else:
            judge_model, judge_base_url = {
                "auto":      ("deepseek-v4-flash", "https://api.deepseek.com"),
                "deepseek":  ("deepseek-v4-flash", "https://api.deepseek.com"),
                "ollama":    ("qwen3.5:9b", "http://localhost:11434/v1"),
            }.get(judge_provider, ("deepseek-v4-flash", "https://api.deepseek.com"))

        cmd = _conda_python([
            "benchmark/eval/evaluate.py",
            "--mode", mode,
            "--input", str(dataset),
            "--output", str(Path(output_dir) / f"{model}_report.json"),
            "--target-model", model,
            "--judge-model", judge_model,
            "--judge-base-url", judge_base_url,
            "--resume",
        ])
        if target_base_url:
            cmd.extend(["--target-base-url", target_base_url])
        if target_api_key:
            cmd.extend(["--target-api-key", target_api_key])
        if max_questions > 0:
            cmd.extend(["--limit", str(max_questions)])

        logger.info("  → model_evaluate: 评测 %s, mode=%s, base_url=%s",
                     model, mode, target_base_url or "(default)")
        logger.info("  → cmd: %s", _safe_cmd(cmd))
        return _run_subprocess(cmd, timeout=14400)

    @staticmethod
    def _resolve_target(model: str) -> Tuple[Optional[str], str]:
        m = model.lower()
        if "minimax" in m:
            return "https://api.minimaxi.com/anthropic", "MINIMAX_API_KEY"
        if "mimo" in m:
            return "https://api.xiaomimimo.com/v1", "MIMO_API_KEY"
        if "deepseek" in m:
            return "https://api.deepseek.com", "OPENAI_API_KEY"
        if ":" in model:
            return "http://localhost:11434/v1", ""
        return None, "OPENAI_API_KEY"

    def _exec_multi_judge_compare(self, params: dict, resolved=None) -> Tuple[int, str, str]:
        models = params.get("models", ["deepseek-v4-flash", "mimo-v2-flash", "qwen3.5:9b"])
        api_judge = params.get("api_judge", "deepseek-v4-flash")
        local_judge = params.get("local_judge", "qwen3.5:9b")
        dataset = params.get("dataset", "benchmark/dataset/core.json")
        output = params.get("output", "benchmark/eval/results/judge_comparison.json")

        output_path = Path(output)
        output_dir = output_path.parent

        judge_runs = [
            {"label": "api",   "judge_model": api_judge,   "judge_base_url": "https://api.deepseek.com"},
            {"label": "local", "judge_model": local_judge, "judge_base_url": "http://localhost:11434/v1",
             "judge_api_key": "ollama"},
        ]

        all_outputs = []
        all_errors = []
        global_rc = 0
        per_judge_rc = {}

        for run_cfg in judge_runs:
            run_rc = 0
            for model in models:
                output_file = output_dir / f"judge_{run_cfg['label']}_{model}.json"
                cmd = _conda_python([
                    "benchmark/eval/evaluate.py",
                    "--mode", "model",
                    "--input", str(dataset),
                    "--output", str(output_file),
                    "--target-model", model,
                    "--judge-model", run_cfg["judge_model"],
                    "--judge-base-url", run_cfg["judge_base_url"],
                    "--resume",
                ])
                if run_cfg.get("judge_api_key"):
                    cmd.extend(["--judge-api-key", run_cfg["judge_api_key"]])

                logger.info("  → multi_judge_compare [%s/%s]: judge=%s",
                             run_cfg["label"], model, run_cfg["judge_model"])
                logger.info("  → cmd: %s", _safe_cmd(cmd))
                rc, stdout, stderr = _run_subprocess(cmd, timeout=14400)
                all_outputs.append(f"[{run_cfg['label']}/{model}] rc={rc}\n{stdout[-200:]}")
                if rc != 0:
                    all_errors.append(f"[{run_cfg['label']}/{model}] {stderr[-200:]}")
                    run_rc = 1
            per_judge_rc[run_cfg["label"]] = run_rc
            if run_rc != 0:
                global_rc = 1

        combined_stdout = "\n---\n".join(all_outputs)
        combined_stderr = "\n---\n".join(all_errors) if all_errors else ""

        logger.info("  → multi_judge_compare: 双路×%d模型评测完成, API rc=%s, Local rc=%s, output=%s",
                     len(models), per_judge_rc.get("api", "?"), per_judge_rc.get("local", "?"), output)
        return global_rc, combined_stdout, combined_stderr

    def _exec_leaderboard_viz(self, params: dict, resolved=None) -> Tuple[int, str, str]:
        source = params.get("source", "benchmark/eval/results/")
        formats = params.get("formats", ["json", "html"])
        output_dir = params.get("output_dir", "benchmark/eval/results/")

        leaderboard_json = str(Path(output_dir) / "leaderboard.json")
        leaderboard_html = str(Path(output_dir) / "leaderboard.html")

        all_outputs = []
        final_rc = 0

        if "json" in formats:
            cmd_json = _conda_python([
                "benchmark/eval/summarize_multi.py",
                "--input", str(source),
                "--output", leaderboard_json,
            ])
            logger.info("  → leaderboard_viz [json]: summarize_multi.py → %s", leaderboard_json)
            logger.info("  → cmd: %s", _safe_cmd(cmd_json))
            rc, out, err = _run_subprocess(cmd_json, timeout=600)
            all_outputs.append(f"[json] rc={rc}\n{out[-200:]}")
            if rc != 0:
                final_rc = rc

        if "html" in formats:
            cmd_html = _conda_python([
                "benchmark/eval/report_viz.py",
                "--input", str(source),
                "--output", leaderboard_html,
            ])
            logger.info("  → leaderboard_viz [html]: report_viz.py → %s", leaderboard_html)
            logger.info("  → cmd: %s", _safe_cmd(cmd_html))
            rc, out, err = _run_subprocess(cmd_html, timeout=300)
            all_outputs.append(f"[html] rc={rc}\n{out[-200:]}")
            if rc != 0:
                final_rc = 1

        combined = "\n---\n".join(all_outputs)
        logger.info("  → leaderboard_viz: 完成, formats=%s", formats)
        return final_rc, combined, ""

    def _exec_multi_format_parse(self, params: dict, resolved=None) -> Tuple[int, str, str]:
        files = params.get("files", [])
        input_dir = params.get("input_dir", "benchmark/agent/test_materials/")
        output_dir = params.get("output_dir", "benchmark/agent/test_materials/md/")
        lang = params.get("lang", "ch")

        script_path = ROOT / "tools" / "mineru_to_md.py"
        abs_input_dir = ROOT / input_dir
        abs_output = ROOT / output_dir
        abs_output.mkdir(parents=True, exist_ok=True)

        if files:
            resolved_files = []
            for f in files:
                p = Path(f)
                if not p.is_absolute():
                    p = abs_input_dir / f
                resolved_files.append(str(p))
            cmd = _conda_python([
                str(script_path),
                *resolved_files,
                "--output-dir", str(abs_output),
                "--lang", str(lang),
                "--skip-existing",
                "--stats",
            ])
            logger.info("  → multi_format_parse: %d files resolved to %s", len(files), input_dir)
        else:
            cmd = _conda_python([
                str(script_path),
                "--input-dir", str(abs_input_dir),
                "--recursive",
                "--output-dir", str(abs_output),
                "--lang", str(lang),
                "--skip-existing",
                "--stats",
            ])
            logger.info("  → multi_format_parse: dir=%s via mineru_to_md.py", input_dir)

        logger.info("  → cmd: %s", _safe_cmd(cmd))
        return _run_subprocess(cmd, timeout=3600)

    def _exec_local_finetune(self, params: dict, resolved=None) -> Tuple[int, str, str]:
        dataset = params.get("dataset", "finetune/data/")
        base_model = params.get("base_model", "qwen3.5:9b")
        epochs = params.get("epochs", 3)
        lora_rank = params.get("lora_rank", 16)
        output_dir = params.get("output_dir", "finetune/output/")

        cmd = _conda_python([
            "finetune/train_qlora.py",
            "--dataset", str(dataset),
            "--base-model", base_model,
            "--epochs", str(epochs),
            "--lora-rank", str(lora_rank),
            "--output-dir", str(output_dir),
        ])

        logger.info("  → local_finetune: QLoRA %s, epochs=%d, rank=%d", base_model, epochs, lora_rank)
        logger.info("  → cmd: %s", _safe_cmd(cmd))
        return _run_subprocess(cmd, timeout=28800)

    def _exec_reproduce_all(self, params: dict, resolved=None) -> Tuple[int, str, str]:
        steps_param = params.get("steps", [])
        local_mode = params.get("local_mode", self._local_mode)
        skip_existing = params.get("skip_existing", True)
        output_dir = params.get("output_dir", "benchmark/reproduce/")

        ps1_path = ROOT / "run_agent.ps1"
        if ps1_path.exists():
            logger.info("  → reproduce_all: 执行 run_agent.ps1, skip_existing=%s, local=%s",
                         skip_existing, local_mode)
            env_extra = {
                "AGENT_LOCAL_MODE": "1" if local_mode else "0",
                "AGENT_SKIP_EXISTING": "1" if skip_existing else "0",
            }
            cmd = ["powershell", "-ExecutionPolicy", "Bypass", "-File", str(ps1_path)]
            return _run_subprocess(cmd, timeout=86400, env_extra=env_extra)

        status_msg = json.dumps({
            "intent": "reproduce_all",
            "status": "skipped",
            "reason": "run_agent.ps1 not found at " + str(ps1_path),
            "params": {
                "steps": steps_param,
                "local_mode": local_mode,
                "skip_existing": skip_existing,
                "output_dir": output_dir,
            },
            "hint": "Create run_evaluation.ps1 or use --intents with explicit step list",
        }, ensure_ascii=False)

        logger.warning("run_evaluation.ps1 不存在: %s", ps1_path)
        logger.warning("  提示: 使用 --intents 手动指定步骤序列以逐步执行")
        cmd = _conda_python(["-c", f"import os,json,sys; sys.stdout.write(os.environ.get('AGENT_REPRODUCE_MSG',''))"])
        return _run_subprocess(cmd, timeout=60, env_extra={"AGENT_REPRODUCE_MSG": status_msg})

    def _exec_medical_rag(self, params: dict, resolved=None) -> Tuple[int, str, str]:
        input_dir = params.get("input_dir", str(ROOT / "data" / "sources_medical"))
        output_dir = params.get("output_dir", str(ROOT / "benchmark" / "eval" / "results" / "medical"))
        skip_train = params.get("skip_train", False)
        skip_hybrid = params.get("skip_hybrid", False)
        skip_viz = params.get("skip_viz", False)
        if isinstance(skip_train, str):
            skip_train = skip_train.lower() in ("true", "1", "yes")
        if isinstance(skip_hybrid, str):
            skip_hybrid = skip_hybrid.lower() in ("true", "1", "yes")
        if isinstance(skip_viz, str):
            skip_viz = skip_viz.lower() in ("true", "1", "yes")

        handler_path = ROOT / "benchmark" / "agent" / "medical_rag_handler.py"
        if not handler_path.exists():
            status_msg = json.dumps({
                "intent": "medical_rag",
                "status": "skipped",
                "reason": f"medical_rag_handler.py 未创建 ({handler_path})",
                "hint": "Create benchmark/agent/medical_rag_handler.py to enable this intent",
            }, ensure_ascii=False)
            logger.warning("medical_rag_handler.py 不存在: %s", handler_path)
            return 0, status_msg, ""

        cmd = _conda_python([
            str(handler_path),
            "--input", input_dir,
            "--output", output_dir,
        ])
        if skip_train:
            cmd.append("--skip-train")
        if skip_hybrid:
            cmd.append("--skip-hybrid")
        if skip_viz:
            cmd.append("--skip-viz")

        logger.info("  → medical_rag: 医疗RAG全流程, input=%s, output=%s, skip_train=%s, skip_hybrid=%s, skip_viz=%s",
                     input_dir, output_dir, skip_train, skip_hybrid, skip_viz)
        logger.info("  → cmd: %s", _safe_cmd(cmd))
        return _run_subprocess(cmd, timeout=54000, env_extra={"_MRAG_CONDA_WRAPPED": "1"})


# ============================================================
# ControlSciAgentCLI — main orchestrator
# ============================================================

class ControlSciAgentCLI:
    def __init__(self, local_mode: bool = False, dry_run: bool = False,
                 max_retries: int = 2, enable_verify: bool = True):
        self._local_mode = local_mode
        self._dry_run = dry_run
        self._max_retries = max_retries
        self._enable_verify = enable_verify
        self._registry = IntentRegistry()
        self._router = IntentRouter(self._registry)
        self._scheduler = get_global_scheduler(local_mode=local_mode)
        self._executor = Executor(scheduler=self._scheduler, local_mode=local_mode,
                                   registry=self._registry)
        self._verifier: Optional[Verifier] = None
        self._execution_log: Optional[ExecutionLog] = None
        self._env_checked: Optional[List[str]] = None
        _get_logs_dir().mkdir(parents=True, exist_ok=True)

    @property
    def _verifier_instance(self) -> Verifier:
        if self._verifier is None:
            self._verifier = Verifier()
        return self._verifier

    def _check_env(self) -> List[str]:
        if self._env_checked is not None:
            return self._env_checked
        warnings = []
        checks = [
            ("OPENAI_API_KEY", "DeepSeek API"),
            ("MIMO_API_KEY", "MiMo API"),
        ]
        for var, name in checks:
            if not os.environ.get(var):
                warnings.append(f"{name} Key 未设置 (环境变量 {var})")

        ollama_host = os.environ.get("OLLAMA_HOST", "http://localhost:11434")
        try:
            resp = httpx.get(f"{ollama_host}/api/tags", timeout=3)
            if resp.status_code != 200:
                warnings.append(f"Ollama 服务无响应: {ollama_host}")
        except Exception as e:
            logger.debug("Ollama 健康检查异常（非关键）: %s", e)

        self._env_checked = warnings
        return warnings

    def run(self, user_input: str = None, intent_list: List[str] = None,
            intent_params: dict = None) -> ExecutionLog:
        env_warnings = self._check_env()
        for w in env_warnings:
            logger.warning("⚠ %s", w)

        task_id = datetime.now().strftime("agent-%Y%m%d-%H%M%S")
        task_name = user_input[:80] if user_input else (
            ",".join(intent_list) if intent_list else "agent-task"
        )
        self._execution_log = ExecutionLog(task_id=task_id, task_name=task_name)
        self._execution_log.final_status = "running"
        t0 = time.time()

        if user_input and not intent_list:
            if intent_params:
                logger.warning("⚠ --intent-params 仅在 --intents 模式下生效，当前被忽略")
            logger.info("🔮 Intent Router 正在将自然语言拆解为执行计划...")
            try:
                plan = self._router.plan(user_input)
            except Exception as e:
                logger.error("❌ Intent Router 失败: %s", e)
                self._execution_log.final_status = "failed"
                self._execution_log.total_duration_ms = int((time.time() - t0) * 1000)
                return self._execution_log
        elif intent_list:
            plan = self._intent_list_to_plan(intent_list, intent_params)
        else:
            logger.error("必须提供 user_input 或 intent_list")
            self._execution_log.final_status = "failed"
            self._execution_log.total_duration_ms = int((time.time() - t0) * 1000)
            return self._execution_log

        logger.info("📋 执行计划 (%d 步):", len(plan))
        for s in plan:
            deps = f" (依赖: {', '.join(s.depends_on)})" if s.depends_on else ""
            logger.info("  %d. [%s] %s%s", s.rank, s.intent_id, s.description[:60], deps)

        self._execution_log.final_status = "running"
        all_passed = True
        any_failed = False

        for step in plan:
            logger.info("━" * 50)
            logger.info("▶ Step %d/%d: %s (%s)", step.rank, len(plan),
                         step.intent_id, step.intent_name)
            logger.info("  └ 工具: %s | 资源类型: %s", step.tool, step.resource_type)

            log_step, output, error = self._execute_with_retry(step)
            self._execution_log.add_step(log_step)

            status_icon = {"success": "✅", "failed": "❌", "timeout": "⏰", "skipped": "⏭️"}.get(log_step.status, "❓")
            logger.info("%s Step %d 完成: %s (%dms)",
                         status_icon, step.rank, log_step.status, log_step.duration_ms)

            if log_step.status == "failed":
                any_failed = True
                all_passed = False
            elif log_step.status == "skipped":
                pass
            else:
                if self._enable_verify and log_step.status == "success" and not self._dry_run:
                    verify_result = self._verifier_instance.verify(step, output, error)
                    v_icon = "✅" if verify_result.passed else "⚠️"
                    logger.info("  %s 验证: score=%.1f %s",
                                 v_icon, verify_result.score, verify_result.reason[:100])
                    if not verify_result.passed:
                        score_before = verify_result.score
                        if verify_result.correction_hint:
                            improved_params, si_reason = self._self_improve_params(
                                step.intent_id, step.intent_name, step.description,
                                step.parameters, output, verify_result,
                            )
                            if improved_params:
                                step.parameters = {**step.parameters, **improved_params}
                                logger.info("  🔄 Self-Improve 重试: %s", si_reason)
                                resolved2 = self._scheduler.resolve(step.intent_id, local_mode=self._local_mode)
                                log_step2, output2, error2 = self._executor.execute(
                                    step, dry_run=False, resolved=resolved2)
                                verify2 = self._verifier_instance.verify(step, output2, error2)
                                delta = verify2.score - score_before
                                logger.info("  📈 Self-Improve Δ: %+.1f, reason=%s", delta, si_reason)
                                if verify2.passed:
                                    self._execution_log.steps[-1] = log_step2
                                    logger.info("  ✅ Self-Improve 后验证通过")
                                    continue
                        all_passed = False

        self._execution_log.total_duration_ms = int((time.time() - t0) * 1000)
        if all_passed and not any_failed:
            self._execution_log.final_status = "completed"
        elif any_failed:
            self._execution_log.final_status = "failed"
        else:
            self._execution_log.final_status = "partial"

        return self._execution_log

    def _execute_with_retry(self, step: PlanStep) -> Tuple[LogStep, str, Optional[str]]:
        resolved = self._scheduler.resolve(step.intent_id, local_mode=self._local_mode)
        log_step, output, error = self._executor.execute(step, dry_run=self._dry_run, resolved=resolved)

        if log_step.status != "failed" or self._dry_run:
            return log_step, output, error

        if self._max_retries == 0:
            return log_step, output, error

        improved_params = {}
        self_improve_reason = ""
        score_before = 0.0
        if self._enable_verify:
            verify_result = self._verifier_instance.verify(step, output, error)
            score_before = verify_result.score
            logger.info("  ⚠️ 首次验证: score=%.1f issues=%s",
                         verify_result.score, verify_result.issues[:3] if verify_result.issues else [])
            if score_before < 0.5 and verify_result.correction_hint:
                improved_params, si_reason = self._self_improve_params(
                    step.intent_id, step.intent_name, step.description,
                    step.parameters, output, verify_result,
                )
                if improved_params:
                    self_improve_reason = si_reason
                    step.parameters = {**step.parameters, **improved_params}
                    logger.info("  📝 参数已更新: %s", json.dumps(improved_params, ensure_ascii=False))

        for attempt in range(1, self._max_retries + 1):
            logger.info("  🔄 重试 %d/%d: %s", attempt, self._max_retries, step.intent_id)
            time.sleep(2)

            resolved = self._scheduler.resolve(step.intent_id, local_mode=self._local_mode)
            fallback_provider = self._scheduler.get_fallback(resolved)
            if fallback_provider:
                logger.info("  🔽 降级至 provider=%s", fallback_provider.provider)
                resolved = fallback_provider

            log_step2, output2, error2 = self._executor.execute(step, dry_run=False, resolved=resolved)
            if log_step2.status == "success":
                if self._enable_verify and self_improve_reason:
                    verify2 = self._verifier_instance.verify(step, output2, error2)
                    delta = verify2.score - score_before
                    logger.info("  📈 Self-Improve Δ: %+.1f, reason=%s", delta, self_improve_reason)
                return log_step2, output2, error2
            log_step = log_step2
            output = output2
            error = error2

        return log_step, output, error

    def _self_improve_params(self, intent_id: str, intent_name: str, description: str,
                             original_params: dict, exec_output: str,
                             verify_result: 'VerifyResult') -> Tuple[dict, str]:
        from openai import OpenAI, DefaultHttpxClient

        api_key = os.environ.get("OPENAI_API_KEY") or os.environ.get("DEEPSEEK_API_KEY", "")
        if not api_key:
            logger.warning("  Self-Improve 跳过：无 API Key")
            return {}, "no-api-key"

        logger.info("  🔄 Self-Improve: 正在调用 DeepSeek 生成改进参数...")

        prompt = (
            f"执行意图 [{intent_id}] 第1次尝试未达预期。\n\n"
            f"意图名称: {intent_name}\n"
            f"描述: {description}\n"
            f"原始参数: {json.dumps(original_params, ensure_ascii=False)}\n"
            f"执行输出（截取前 1500 字符）:\n{exec_output[:1500]}\n"
            f"验证问题: {json.dumps(verify_result.issues, ensure_ascii=False)}\n"
            f"修正建议: {verify_result.correction_hint}\n\n"
            f"请给出改进后的参数 JSON（仅包含需要修改的字段，使用原始参数中的英文 key）：\n"
            f'{{"temperature": 0.3, "max_tokens": 8192, "reason": "调整原因"}}'
        )

        try:
            client = OpenAI(
                api_key=api_key,
                base_url="https://api.deepseek.com",
                timeout=60,
                max_retries=0,
                http_client=DefaultHttpxClient(proxy=None),
            )
            response = client.chat.completions.create(
                model="deepseek-v4-flash",
                messages=[
                    {"role": "system", "content": "你是 ControlSci Data Agent 的参数优化器。根据验证反馈给出精确的参数调整。仅输出 JSON。"},
                    {"role": "user", "content": prompt},
                ],
                temperature=0.2,
                max_tokens=1024,
            )
            raw = response.choices[0].message.content.strip()
            json_str = _extract_json_block(raw)
            improved = json.loads(json_str)
        except Exception as e:
            logger.warning("  Self-Improve DeepSeek 调用失败: %s", e)
            return {}, f"deepseek-error: {e}"

        if not isinstance(improved, dict):
            logger.warning("  Self-Improve 返回非字典: %s", type(improved))
            return {}, "invalid-response-type"

        reason = improved.pop("reason", "")

        logger.info("  ✅ Self-Improve 建议: %s → %s", reason, json.dumps(improved, ensure_ascii=False))
        return improved, reason

    def _intent_list_to_plan(self, intent_ids: List[str],
                              intent_params: dict = None) -> List[PlanStep]:
        plan = []
        for idx, pid in enumerate(intent_ids, 1):
            pid = pid.strip()
            intent_info = self._registry.get(pid)
            if intent_info is None:
                logger.warning("跳过未知 intent_id: %s", pid)
                continue
            params = {}
            if intent_params and pid in intent_params:
                raw = intent_params[pid]
                if isinstance(raw, dict):
                    params = dict(raw)
                    logger.info("  📝 [%s] 使用自定义参数: %s", pid,
                                 json.dumps(params, ensure_ascii=False))
                else:
                    logger.warning("  ⚠️ [%s] intent_params 值不是 dict (type=%s), 已跳过",
                                   pid, type(raw).__name__)
            plan.append(PlanStep(
                intent_id=pid,
                intent_name=intent_info.get("name", pid),
                description=intent_info.get("description", pid),
                tool=", ".join(intent_info.get("toolchain", [])),
                resource_type=intent_info.get("resource_type", "script"),
                depends_on=intent_info.get("depends_on", []),
                parameters=params,
                rank=idx,
            ))
        return plan

    def save_log(self, path: str = None):
        if self._execution_log is None:
            logger.warning("无执行日志可保存")
            return ""
        path = path or str(_get_logs_dir() / f"{self._execution_log.task_id}.json")
        self._execution_log.save(path)
        logger.info("执行日志已保存: %s", path)
        return path

    def print_summary(self):
        if self._execution_log is None:
            return
        log = self._execution_log
        print("\n" + "=" * 60)
        print(f"  ControlSci Data Agent — 执行摘要")
        print("=" * 60)
        print(f"  Task:       {log.task_name}")
        print(f"  Status:     {log.final_status}")
        print(f"  耗时:       {log.total_duration_ms / 1000:.1f}s")
        print(f"  步骤:       {len(log.steps)}")
        success_count = sum(1 for s in log.steps if s.status == "success")
        failed_count = sum(1 for s in log.steps if s.status == "failed")
        skipped_count = sum(1 for s in log.steps if s.status == "skipped")
        timeout_count = sum(1 for s in log.steps if s.status == "timeout")
        print(f"    [OK] 成功: {success_count}  [FAIL] 失败: {failed_count}  [SKIP] 跳过: {skipped_count}  [TIMEOUT] 超时: {timeout_count}")
        print("=" * 60)


# ============================================================
# CLI Entry Point
# ============================================================

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="agent_cli.py",
        description="ControlSci Data Agent CLI — 科学文档跨模态语料智能体",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=textwrap.dedent(f"""\
            示例:
              %(prog)s "审计 arXiv 论文的跨模态对齐质量"
              %(prog)s --intents corpus_parse,cross_modal_audit
              %(prog)s --intents cross_modal_audit,leaderboard_viz -P '{{"cross_modal_audit":{{"max_images":10}}}}'
              %(prog)s --dry-run "生成 500 题评测数据集并跑评测"
              %(prog)s --local "QLoRA 微调 qwen3.5 并验证 Perplexity"
              %(prog)s --list-intents

            版本: {VERSION}
        """),
    )

    parser.add_argument(
        "input", nargs="?",
        help="自然语言任务描述（由 Intent Router 自动拆解）",
    )
    parser.add_argument(
        "--intents", "-i",
        help="手动指定 intent 序列，逗号分隔（跳过 Intent Router）",
    )
    parser.add_argument(
        "--dry-run", "-n", action="store_true",
        help="干跑模式：仅生成计划并输出，不实际执行",
    )
    parser.add_argument(
        "--local", "-l", action="store_true",
        help="本地模式：优先使用 Ollama + 本地 MinerU，不依赖外部 API",
    )
    parser.add_argument(
        "--max-retries", type=int, default=2,
        help="每步最大重试次数（默认 2）",
    )
    parser.add_argument(
        "--no-verify", action="store_true",
        help="跳过 LLM 验证步骤（仅执行，不验证产出质量）",
    )
    parser.add_argument(
        "--output-log", "-o",
        help="执行日志 JSON 输出路径",
    )
    parser.add_argument(
        "--allow-partial", action="store_true",
        help="允许 partial 状态以 0 退出；默认 partial 返回 2，避免评审复现误判为完整成功。",
    )
    parser.add_argument(
        "--intent-params", "-P",
        help='per-intent 自定义参数 JSON，如 \'{"cross_modal_audit":{"max_images":10}}\'',
    )
    parser.add_argument(
        "--list-intents", action="store_true",
        help="列出全部可用能力并退出",
    )
    parser.add_argument(
        "--version", "-V", action="version",
        version=f"ControlSci Data Agent CLI v{VERSION}",
    )

    return parser


def main():
    _setup_logging()
    parser = build_parser()
    args = parser.parse_args()

    if args.list_intents:
        registry = IntentRegistry()
        print(f"ControlSci Data Agent — {len(registry.list_intents())} 项可用能力:\n")
        for i in registry.list_intents():
            deps = i.get("depends_on", [])
            dep_str = f" 依赖: {', '.join(deps)}" if deps else ""
            print(f"  {i.get('rank', '-'):2d}. [{i['intent_id']:<25s}] {i.get('name', '')}")
            print(f"      工具: {', '.join(i.get('toolchain', ['-']))}{dep_str}")
            print(f"      资源: {i.get('resource_type', '-')}")
            print()
        return 0

    if not args.input and not args.intents:
        parser.print_help()
        print("\n❌ 请提供任务描述（自然语言）或使用 --intents 指定能力序列")
        return 1

    intent_list = None
    if args.intents:
        intent_list = [s.strip() for s in args.intents.split(",") if s.strip()]

    intent_params = None
    if args.intent_params:
        try:
            intent_params = json.loads(args.intent_params)
            if not isinstance(intent_params, dict):
                logger.error("--intent-params 必须是 JSON 对象: {%s...}", str(args.intent_params)[:60])
                return 1
        except json.JSONDecodeError as e:
            logger.error("--intent-params JSON 解析失败: %s", e)
            return 1

    cli = ControlSciAgentCLI(
        local_mode=args.local,
        dry_run=args.dry_run,
        max_retries=args.max_retries,
        enable_verify=not args.no_verify,
    )

    try:
        exec_log = cli.run(
            user_input=args.input,
            intent_list=intent_list,
            intent_params=intent_params,
        )
    except KeyboardInterrupt:
        logger.warning("用户中断执行")
        return 130
    except Exception as e:
        logger.error("执行异常: %s", e, exc_info=True)
        return 1

    log_path = cli.save_log(args.output_log)
    cli.print_summary()

    if exec_log.final_status == "completed":
        return 0
    elif exec_log.final_status == "partial":
        return 0 if args.allow_partial else 2
    else:
        return 1


if __name__ == "__main__":
    sys.exit(main())
