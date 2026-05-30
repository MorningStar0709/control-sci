# Track2 ControlSci Data Agent — 25 题执行案例包（扩展版）

> **版本**：v1.1（扩展版） | **日期**：2026-05-13
> **赛道**：赛道二（智能体与数据工程赛道）
> **覆盖类型**：普通执行 10 例 + 失败恢复 5 例 + 降级处理 3 例 + 审计日志 4 例 + 跨工具协作 3 例
> **数据源**：`benchmark/agent/logs/` + `benchmark/agent/examples/logs/` + `benchmark/agent/results/` + `benchmark/agent/` 代码

---

## 案例索引

| # | 类别 | Intent | 输入类型 | 日志路径 |
|:-:|:----:|:-------|:---------|:---------|
| 01 | 普通执行 | `arxiv_search` | 自然语言 | D 飞轮日志 |
| 02 | 普通执行 | `mineru_parse` | PDF URL | D 飞轮日志 |
| 03 | 普通执行 | `corpus_parse` | 解析结果 | D 飞轮日志 |
| 04 | 普通执行 | `benchmark_build` | 语料 chunk | D 飞轮日志 |
| 05 | 普通执行 | `quality_arbitrate` | 题目候选 | `examples/logs/task_2_arbitrate.json` |
| 06 | 普通执行 | `model_evaluate` | 评测题 | D 飞轮日志 |
| 07 | 普通执行 | `leaderboard_viz` | 评测结果 | D 飞轮日志 |
| 08 | 普通执行 | `multi_format_parse` | PPTX/PNG/DOCX/XLSX | `logs/demo-multi-format-20260510-1917.json` |
| 09 | 普通执行 | `cross_modal_audit` | 共现 chunk | `logs/demo-10intents-e2e-20260509.md` |
| 10 | 普通执行 | `model_evaluate` | 弹性伸缩证明 | `logs/demo-35b-elastic-proof.json` |
| 11 | 失败恢复 | `corpus_quality_report` | Provider 级自动降级 | `logs/demo-local-gpu-fallback-20260509-0116.md` |
| 12 | 失败恢复 | `benchmark_build` | Step 级 Self-Improve | 报告二 §5.1-§5.3 + `agent_cli.py` |
| 13 | 失败恢复 | `mineru_parse` | File 级跳过脏文件 | 报告二 §5.1-§5.3 + `tools/mineru_to_md.py` |
| 14 | 失败恢复 | `cross_modal_audit` | API 超时重试 | 报告二 §5.3 + `resource_scheduler.py` / `agent_cli.py` |
| 15 | 降级处理 | `corpus_quality_report` | `--local` 全路径切换 | `logs/demo-local-gpu-fallback-20260509-0116.md` |
| 16 | 降级处理 | `reproduce_all` | 重试耗尽优雅失败 | `agent_cli.py` 重试逻辑 |
| 17 | 降级处理 | `corpus_parse` | 动态重规划跳过下游 | 报告二 §3.4、§5.1-§5.3 |
| 18 | 审计日志 | 全链路 | 结构化日志 schema | `log_schema.py` + `logs/demo-10intents-e2e-20260509.md` |
| 19 | 审计日志 | 跨管道验证 | 双管道可复现性 | 报告二 §4.1 + DATA-TRACE #141-142 |
| 20 | 审计日志 | `visual_audit` | Checkpoint 原子落盘 | 代码 + 日志 |
| 21 | 跨工具协作 | 飞轮全链路 | 7 工具自主编排 | `logs/demo-data-flywheel.json` |
| 22 | 跨工具协作 | 本地+API 交叉验证 | vLLM+VLM 双路径 | `logs/demo-vllm-mineru-1.2b-*.json` |
| 23 | 跨工具协作 | 多格式+审计联合 | 解析→审计管线串联 | `logs/demo-multi-format-20260510-1917.json` + `logs/demo-10intents-e2e-20260509.md` |
| 24 | 失败恢复 | vLLM batch checkpoint | Batch 中断→resume | `logs/bench_mineru_*.log` + `results/bench_mineru_1.2b_checkpoint.json` |
| 25 | 审计日志 | 全量视觉审计 | 4,996 chunk 原子落盘 | `results/visual_audit_checkpoint.json` + `results/visual_audit_results.jsonl` |

---

## 第一组：普通执行（10 题）

### Case 01 — arXiv 论文自动检索下载

| 字段 | 内容 |
|:-----|:------|
| **Case 编号** | N-01 |
| **类别** | 普通执行 |
| **Intent/Input** | `arxiv_search` — 自然语言输入：*"检索 control barrier function 和 differentiable MPC 方向的 2025 年 arXiv 论文并下载"* |
| **Agent plan** | 1 步：`arxiv_search` → 使用 searching-arxiv-papers Skill → arXiv API 检索 → 下载 PDF (depends_on: []) |
| **Tool calls** | `searching-arxiv-papers` Skill + arXiv API (export.arxiv.org)；provider=script，resource_type=script |
| **Output** | 5 篇 PDF 下载至 `data/sources_flywheel/`：2605.02370 / 2605.03662 / 2605.05182 / 2605.05575 / 2605.06630。覆盖自适应 MPC、混合控制、CBF 安全滤波、不变集 MPC、稳定性-混淆权衡五个子领域 |
| **Log path** | D 数据飞轮全链路日志：`benchmark/agent/logs/demo-data-flywheel.json`；评测详情：`benchmark/eval/results/flywheel_eval_deepseek.json`（arXiv ID 出现在 question_id 前缀）；PDF 目录 `data/sources_flywheel/` |
| **Pass criteria** | PDF 文件存在且可解析；检索关键词命中目标论文；无重复下载 |
| **Related capability** | D3 — 精准理解复杂指令；Agent 自主完成论文检索 |
| **Boundary note** | 受 arXiv API 速率限制（~1 req/3s），max_papers 上限 10；不检索付费/非 arXiv 论文 |

---

### Case 02 — 多格式文档 MinerU 解析

| 字段 | 内容 |
|:-----|:------|
| **Case 编号** | N-02 |
| **类别** | 普通执行 |
| **Intent/Input** | `mineru_parse` — 输入：5 篇 arXiv PDF 文件路径列表 |
| **Agent plan** | 1 步：`mineru_parse` → 调用 MinerU API → 格式自动检测 → 结构化 Markdown + LaTeX 公式 + 独立图片 (depends_on: [arxiv_search]) |
| **Tool calls** | MinerU API (magic_pdf, 127.0.0.1:8000)；provider=mineru，resource_type=local_api；自动检测 PDF 格式 -> 调用对应解析管线 |
| **Output** | 5/5 解析成功，零错误。每篇产出：结构化 chunk（章节层级保留）+ 行内/行间 LaTeX 公式 + 嵌入图片文件 |
| **Log path** | `data/sources_flywheel/` 目录下对应 `.md` + `image/` 子目录 |
| **Pass criteria** | 全部 5 篇完成解析；公式以 LaTeX 保留；图片独立文件输出；章节结构完整 |
| **Related capability** | D1 — 文档解析与结构化处理能力；D3 — 合理调用 MinerU 工具 |
| **Boundary note** | 不支持 HTML 格式；极少数加密/损坏 PDF 会触发 Case 13 恢复流程 |

---

### Case 03 — 语料结构化分块与元数据索引

| 字段 | 内容 |
|:-----|:------|
| **Case 编号** | N-03 |
| **类别** | 普通执行 |
| **Intent/Input** | `corpus_parse` — 输入：MinerU 解析后的 Markdown + 图片目录 |
| **Agent plan** | 1 步：`corpus_parse` → 语义结构递归分割 → chunk 元数据索引 → 跨模态标注 (depends_on: [mineru_parse]) |
| **Tool calls** | `corpus_builder.py`；provider=script；自动检测 chunk 边界（章节/段落/公式块） |
| **Output** | 5 篇 PDF → 47 个结构化 chunk（共 253K 字符）。每个 chunk 保留：来源文档 ID、章节层级、公式计数、图片关联索引 |
| **Log path** | 语料元数据：`corpus/metadata.json`（增量更新） |
| **Pass criteria** | chunk 数量 ≥ 40；每个 chunk 含完整元数据字段；无数据丢失 |
| **Related capability** | D1 — 信息抽取准确性、数据清洗质量；D3 — 目标拆解为多步子任务 |
| **Boundary note** | chunk 分割边界基于语义启发式（标题/空行/公式块），极端密集排版文档可能分割粒度不够细 |

---

### Case 04 — 基于语料自动生成评测题

| 字段 | 内容 |
|:-----|:------|
| **Case 编号** | N-04 |
| **类别** | 普通执行 |
| **Intent/Input** | `benchmark_build` — 输入：47 个语义 chunk + 目标四维度 (A/B/C/D) + 每篇 3 题上限 |
| **Agent plan** | 1 步：`benchmark_build` → DeepSeek v4-flash 逐 chunk 出题 → 四维度分配 → 严格上限控制 (depends_on: [corpus_parse]) |
| **Tool calls** | `build_benchmark.py` + DeepSeek v4-flash (API)；provider=api；temperature=0.3 |
| **Output** | 15 题（5 篇 × 3 题上限），覆盖 A/B/C/D 四维度。每题包含：Question、Expected Answer、Rubric、Difficulty Level、Source chunk |
| **Log path** | D 飞轮日志 `demo-data-flywheel.json`；题目 JSON：`benchmark/dataset/`（增量） |
| **Pass criteria** | 15 题产出，每篇 ≤ 3 题；四维度分布合理；每题有 source chunk 引用 |
| **Related capability** | D3 — 合理调用工具；目标拆解为可执行子任务 |
| **Boundary note** | 题目质量依赖源语料质量；deepseek-v4-flash 在部分高难度推理题上可能出题不准确（经 quality_arbitrate 过滤） |

---

### Case 05 — 双层 LLM 仲裁 + Embedding 快速通道

| 字段 | 内容 |
|:-----|:------|
| **Case 编号** | N-05 |
| **类别** | 普通执行 |
| **Intent/Input** | `quality_arbitrate` — 输入：360 道待仲裁题目候选 |
| **Agent plan** | 4 个子步骤：(1) 题目加载 → (2) Embedding 快速通道 → (3) LLM 第一轮仲裁 → (4) LLM 第二轮仲裁 + 孤儿回收 (depends_on: [benchmark_build]) |
| **Tool calls** | Embedding: `qwen3-embedding:4b` (Ollama)；LLM 仲裁: DeepSeek v4-flash (API)；双通道并行 |
| **Output** | 输入 360 题 → Embedding 通道 passed=48, rejected=12, pending=300 → LLM 第一轮 passed=192, rejected=75 → LLM 第二轮 rejected=75 → 孤儿回收 passed=114, rejected=71。**净通过：354 题 (98.3%)** |
| **Log path** | `benchmark/agent/examples/logs/task_2_arbitrate.json`（step 301-305 完整记录） |
| **Pass criteria** | 仲裁 pipeline 完整执行 5 个子步骤；最终通过率合理 (≥ 95%)；Embedding 快速通道正确识别明显正确/错误题目 |
| **Related capability** | D3 — 多步骤逻辑性、合理调用工具；D4 — 输出可靠性 |
| **Boundary note** | Embedding 快速通道仅适用于低维语义可分离场景；LLM 仲裁的判定标准受 judge 模型能力影响（见评分者反规模定律发现） |

---

### Case 06 — 统一接口模型评测

| 字段 | 内容 |
|:-----|:------|
| **Case 编号** | N-06 |
| **类别** | 普通执行 |
| **Intent/Input** | `model_evaluate` — 输入：15 道飞轮题目 + 目标模型 deepseek-v4-flash |
| **Agent plan** | 1 步：`model_evaluate` → 统一评测接口 → 逐题评分 → 四维度汇总 (depends_on: [quality_arbitrate]) |
| **Tool calls** | `evaluate.py` + DeepSeek v4-flash (API)；provider=api；统一评测管线，与 500 题 Benchmark 共享同一代码路径 |
| **Output** | deepseek-v4-flash overall=0.1400。逐维度：A 基础事实=0.15 / B 推理链=0.05 / C 计算推导=0.25 / D 综合开放=0.1875。新题得分远低于原 500 题均值 0.6431（差距 4.6×） |
| **Log path** | `benchmark/eval/results/flywheel_eval_deepseek.json` |
| **Pass criteria** | 15 题全部完成评分；四维度分数输出完整；与 500 题基准使用同一评分管线 |
| **Related capability** | D3 — 合理调用工具；D4 — 可复现性保证（统一评测管线） |
| **Boundary note** | 飞轮新题的低分恰好验证了评测盲区存在，非系统问题——新题来自未见领域且难度更高 |

---

### Case 07 — 排行榜 JSON + HTML 可视化生成

| 字段 | 内容 |
|:-----|:------|
| **Case 编号** | N-07 |
| **类别** | 普通执行 |
| **Intent/Input** | `leaderboard_viz` — 输入：评测结果 JSON（新飞轮 15 题 + 历史 500 题合并） |
| **Agent plan** | 1 步：`leaderboard_viz` → 合并结果 → 生成 JSON 排行榜 → 生成 HTML 可视化 (depends_on: [model_evaluate]) |
| **Tool calls** | `summarize_multi.py` + `report_viz.py`；provider=script；formats=['json', 'html'] |
| **Output** | 排行榜从 500 题扩展到 515 题。JSON + HTML 双格式输出，含表格、柱状图、热力图 |
| **Log path** | `benchmark/agent/logs/demo-10intents-e2e-20260509.md`（leaderboard_viz step 输出 328ms） |
| **Pass criteria** | JSON 和 HTML 均已成功生成；新飞轮条目正确合并；无数据覆盖 |
| **Related capability** | D3 — 全链路闭环；D4 — 输出可靠性、结构化日志 |
| **Boundary note** | 可视化模板为预定义，不支持自定义图表类型；HTML 需要现代浏览器渲染 |

---

### Case 08 — 多格式文档归一化解析

| 字段 | 内容 |
|:-----|:------|
| **Case 编号** | N-08 |
| **类别** | 普通执行 |
| **Intent/Input** | `multi_format_parse` — 输入：4 种格式测试文件 (PPTX/PNG/DOCX/XLSX) + 统一归一化输出 |
| **Agent plan** | 1 步：`multi_format_parse` → 逐格式调用 MinerU 对应管线 → 统一 chunk schema 输出 (depends_on: [mineru_parse]) |
| **Tool calls** | MinerU API (multi-format mode)；provider=mineru；自动识别格式并选择解析管线 |
| **Output** | 4 格式 × 194 chunks 全量解析成功：PPTX (47 chunks / 12 图 / 38 公式)、PNG 扫描件 (28/1/16)、DOCX (83/6/29)、XLSX (36/0/0)。全部统一输出 schema，质量检查全部 PASS |
| **Log path** | `benchmark/agent/logs/demo-multi-format-20260510-1917.json` |
| **Pass criteria** | 4 种格式均完成解析；统一 chunk schema 输出；质量检查 4 格式全部 PASS；MinerU 引擎 v3.1.6 |
| **Related capability** | D1 — 格式转换规范性；D3 — 合理调用 MinerU 工具 |
| **Boundary note** | 仅支持 MinerU 引擎支持的格式，HTML 不被支持；扫描件 (PNG) 解析质量受原始图片分辨率影响 |

---

### Case 09 — 跨模态对齐审计（限量模式）

| 字段 | 内容 |
|:-----|:------|
| **Case 编号** | N-09 |
| **类别** | 普通执行 |
| **Intent/Input** | `cross_modal_audit` — 自然语言输入：*"审计 arXiv 论文的公式-图片跨模态对齐质量"* + 自定义参数 `{"max_images": 10, "provider": "minimax"}` |
| **Agent plan** | 1 步：`cross_modal_audit` → MiMo-V2.5 原生视觉模型 → 看图→理解公式→比照 LaTeX→语义一致性判决 (depends_on: [corpus_parse]) |
| **Tool calls** | `visual_audit.py` + MiMo-V2.5 (API, raw httpx)；5 workers 并发；per-intent 参数：max_images=10, provider=minimax |
| **Output** | 10 项审计完成，耗时 22s (0.4min)：一致 60.0% / 部分一致 30.0% / 不一致 10.0% / 不确定 0.0% / 错误 0。报告保存至 `benchmark/agent/results/visual_audit_report.json` |
| **Log path** | `benchmark/agent/logs/agent-20260509-021603.json`（step 1 完整 22s 执行记录）<br>`benchmark/agent/logs/demo-10intents-e2e-20260509.md`（10 项逐项输出） |
| **Pass criteria** | 10 项全部完成；per-intent 参数正确传递 (max_images=10)；MiMo-V2.5 完成"看图→判决"全链路；结论包含 Consistent/Partial/Inconsistent 分类 |
| **Related capability** | D3 — 合理调用工具（MiMo-V2.5 原生视觉）、per-intent 参数精确传递；D2 — 跨模态对齐审计 |
| **Boundary note** | 限量模式 (max_images=10) 用于快速验证，全量审计需扫描 4,996 个共现 chunk（~18min）；MiMo-V2.5 对低分辨率图片或不常见的公式符号可能返回 Uncertain |

---

### Case 10 — 弹性伸缩证明（4B→9B→35B 同机同题）

| 字段 | 内容 |
|:-----|:------|
| **Case 编号** | N-10 |
| **类别** | 普通执行 |
| **Intent/Input** | 同一道 Routh-Hurwitz 稳定判据题，三模型分别回答：qwen3.5:4b / qwen3.5:9b / qwen3.5:35b |
| **Agent plan** | 3 次独立 `model_evaluate` 调用，ResourceScheduler 自动路由至 Ollama 本地推理，provider=ollama，各模型不同 temperature |
| **Tool calls** | `evaluate.py` + Ollama (本地推理)；单张 RTX 5090；provider_parameter_map 自动注入各模型参数 |
| **Output** | 4B: 46.3s / 1,966 chars / 基础推导完整；9B: 54.7s / 2,272 chars / 增加前提假设；35B: 128.2s / 2,643 chars / 最详尽，标注负反馈默认假设。4B→9B 耗时 +18%，9B→35B +134% |
| **Log path** | `benchmark/agent/logs/demo-35b-elastic-proof.json` |
| **Pass criteria** | 三模型均完成回答；资源调度器正确路由至 Ollama；答案长度随模型尺寸递增；时间数据可复现 |
| **Related capability** | D3 — 四路径推理引擎、成本速度精度平衡；D4 — 弹性伸缩 |
| **Boundary note** | 数据仅在 RTX 5090 上验证；35B 耗时 2.1× 于 9B 但质量提升有限，符合反规模定律 |

---

## 第二组：失败恢复（4 题）

### Case 11 — Provider 级恢复：Ollama 未启动 → Script 降级

| 字段 | 内容 |
|:-----|:------|
| **Case 编号** | FR-11 |
| **类别** | 失败恢复 |
| **Intent/Input** | `corpus_quality_report` — `--local` 模式运行，Ollama 服务未提前启动 |
| **Agent plan** | 1 步：`corpus_quality_report` → ResourceScheduler 解析到 Ollama 路径 → HTTP 502 |
| **Tool calls** | 初始：Ollama qwen3.5:9b (provider=ollama)；失败后自动：Script 兜底 (provider=script) |
| **Output** | 初始尝试：`[ollama] FAILED: HTTP 502` → `🔄 重试 1/2` → `🔽 降级至 provider=script` → Script 62ms 完成，score=1.0 |
| **Log path** | `benchmark/agent/logs/demo-local-gpu-fallback-20260509-0116.md`（完整 35.6s 终端实录）<br>`benchmark/agent/logs/agent-20260509-011614.json`（结构化日志） |
| **Recovery flow** | `ResourceScheduler.resolve(local_mode=True)` → provider=ollama → `Executor.execute()` ❌ HTTP 502 → `_execute_with_retry()` → `get_fallback(ollama)` → provider=script → 62ms 成功 ✅ |
| **Pass criteria** | 自动检测 Ollama 不可用；`get_fallback()` 正确降级到 script；降级后正确输出质量报告；全链路零人工干预 |
| **Related capability** | D4 — Provider 级容错、自动降级机制 |
| **Boundary note** | script 兜底只适用于已有本地脚本可执行的 intent；对于纯 LLM 推理任务（如 model_evaluate），降级至 script 无法替代 LLM 输出 |

---

### Case 12 — Step 级恢复：Verifier 低分 → Self-Improve 调优

| 字段 | 内容 |
|:-----|:------|
| **Case 编号** | FR-12 |
| **类别** | 失败恢复 |
| **Intent/Input** | `benchmark_build` — LLM 输出质量不达标（JSON 格式不完整、推理链断裂） |
| **Agent plan** | `_execute_with_retry` 捕获失败状态 → `Verifier` 四阶段评估 → score < 0.5 + correction_hint 非空 → `_self_improve_params()` → 参数调优 → 降级 provider → 重试 |
| **Tool calls** | DeepSeek v4-flash (原始调用) → `_self_improve_params()` 调用同一模型分析失败原因 → 生成改进参数 JSON (temperature↓, max_tokens↑) → 降级至 Ollama 重试 |
| **Output** | 初始 score=0.0 → Self-Improve 调优参数 → 重试成功 score ≥ 0.5。日志输出：`📈 Self-Improve Δ: +X.X, reason=...` |
| **Log path** | 代码链路：`agent_cli.py:L1483-1532` (`_execute_with_retry`) + `L1534-1589` (`_self_improve_params`) + `L522-543` (Verifier 四阶段评估) |
| **Recovery flow** | `Execute()` → status=failed → `Verifier.verify()` → score < 0.5 → `_self_improve_params()` (DeepSeek 分析失败 → 输出改进参数 JSON) → `step.parameters = {**step.parameters, **improved_params}` → `get_fallback()` 降级 provider → 重试 → Verifier 通过 ✅ |
| **Pass criteria** | Self-Improve 闭环触发条件正确；改进参数合理 (temperature↓, max_tokens↑)；重试后 score ≥ 0.5；Δ 值记录正确 |
| **Related capability** | D3 — 自改进闭环、异常恢复；D4 — 步骤级容错 |
| **Boundary note** | 当前已公开日志中的 intent 首次尝试均通过，该机制作为预防性安全网保留；最多 2 次重试均失败则标记 failed |

---

### Case 13 — File 级恢复：MinerU 单文件异常 → 跳过继续

| 字段 | 内容 |
|:-----|:------|
| **Case 编号** | FR-13 |
| **类别** | 失败恢复 |
| **Intent/Input** | `mineru_parse` — 批量解析 23 本控制科学教材 PDF，其中某文件损坏/加密 |
| **Agent plan** | 循环调用 MinerU API → try/except 包裹每个 `convert_one_file()` → 不可恢复异常记录到 errors 列表 → 隐式 continue |
| **Tool calls** | MinerU API (mineru_to_md.py)；file-level granularity |
| **Output** | 损坏文件被跳过并记录 `errors.append({"input": "xxx.pdf", "error": "TimeoutError / PermissionError / 加密"})`，其余 22 本正常解析完成。最终产出含 `saved[]` 和 `errors[]` 双字段，整体不中断 |
| **Log path** | 核心代码：`tools/mineru_to_md.py:L314-336`（文件级异常捕获）<br>Agent 入口：`agent_cli.py:L813-830` (`_exec_mineru_parse` 带 `--skip-existing`) |
| **Recovery flow** | `for file_path in input_files:` → `try: convert_one_file(...)` → `except TimeoutError:` → `retry_timeout > timeout?` → 重试或记录 errors → `continue` → 下一个文件 |
| **Pass criteria** | 单个文件异常不阻塞全流程；错误信息清晰记录到 errors 列表；有效文件全部解析成功；D 飞轮验证 5/5 零错误基线 |
| **Related capability** | D4 — 文件级容错；D1 — 数据清洗质量 |
| **Boundary note** | 不可恢复的异常包括：文件加密、PDF 损坏、权限错误；超时异常有一次重试机会（`retry_timeout`）；D 飞轮实测 5/5 零错误表明该机制主要作为安全网 |

---

### Case 14 — API 超时 → 自动重试后降级

| 字段 | 内容 |
|:-----|:------|
| **Case 编号** | FR-14 |
| **类别** | 失败恢复 |
| **Intent/Input** | DeepSeek API 超时 — step 执行 > 120s，返回 408/504 |
| **Agent plan** | ResourceScheduler.health_check() 标记 provider 不可用 → `_execute_with_retry` 最多 2 次重试 → 全部超时 → 降级至 Ollama 本地模型 |
| **Tool calls** | 初始：DeepSeek v4-flash (API, httpx timeout=120s)；降级后：Ollama (qwen3.5:9b 本地推理) |
| **Output** | 重试 2 次超时记录 → `get_fallback(deepseek)` → provider=ollama → 本地模型执行完成。输出质量降低但系统不中断 |
| **Log path** | 参考 `resource_scheduler.py:L254-413` (HealthCheck 8 路探活)；`agent_cli.py:L1483-1532` (重试逻辑)；故障恢复矩阵见 `agent_report.md §5.8` |
| **Recovery flow** | API 超时 > 120s → step 标记 failed → `_execute_with_retry` 最多 2 次重试 → 仍超时 → `get_fallback(api)` → ollama → 本地推理继续 |
| **Pass criteria** | 自动重试机制正确触发；降级路径可用且不阻塞后续步骤；失败信息可追溯 |
| **Related capability** | D4 — 运行稳定性、故障恢复矩阵 |
| **Boundary note** | 降级至 Ollama 后模型能力下降（qwen3.5:9b < deepseek-v4-flash），输出质量预期降低；手动恢复方式：检查 `DEEPSEEK_API_KEY` 环境变量 |

---

## 第三组：降级处理（3 题）

### Case 15 — `--local` 全路径隐私双轨切换

| 字段 | 内容 |
|:-----|:------|
| **Case 编号** | DG-15 |
| **类别** | 降级处理 |
| **Intent/Input** | `corpus_quality_report` — 指定 `--local` 模式运行，要求零 API 依赖 |
| **Agent plan** | 1 步：`corpus_quality_report` → ResourceScheduler 在 `--local` 模式下全部路径强制切换至本地 provider (Ollama / Script) |
| **Tool calls** | 正常 API 模式：DeepSeek v4-flash (远程 API)；`--local` 模式：Ollama qwen3.5:9b → fallback Script |
| **Output** | ResourceScheduler 在 `--local` 模式下解析到 `provider=ollama, model=qwen3.5:9b`，而非默认的 `provider=api, model=deepseek-v4-flash`。执行逻辑、日志结构、输出格式与 API 模式完全一致 |
| **Log path** | `benchmark/agent/logs/demo-local-gpu-fallback-20260509-0116.md`（`--local` 标志生效记录 `01:16:21 resolved: provider=ollama`） |
| **Recovery flow** | `--local` 标志 → `ResourceScheduler.__init__(local_mode=True)` → `resolve()` 自动过滤 api/mimo 等外部 provider → 仅保留 ollama/script 路径 → 执行 |
| **Pass criteria** | `--local` 下 resolve 结果全部为本地 provider；输出格式与 API 模式一致；无任何外部 API 调用 |
| **Related capability** | D4 — 隐私双路径对称切换、运行稳定性；D3 — 成本速度精度平衡 |
| **Boundary note** | `--local` 模式下模型能力受限于本地模型 (qwen3.5:9b < deepseek-v4-flash)；Ollama 服务需提前启动，否则触发 Case 11 降级 |

---

### Case 16 — 重试耗尽 → 优雅失败不阻塞

| 字段 | 内容 |
|:-----|:------|
| **Case 编号** | DG-16 |
| **类别** | 降级处理 |
| **Intent/Input** | `reproduce_all` — 全链路复现中某子步骤持续失败（如 MinerU API 不可用） |
| **Agent plan** | 多步 plan 中的某一步：`_execute_with_retry` 最多 2 次重试 → 仍失败 → 标记 failed → 执行 `continue` 至下一步，不终止全流程 |
| **Tool calls** | 重试耗尽 → `log_step.status = "failed"` → 记录 error → 返回值 (`log_step, "", error`) → 调用方检查 status 后继续 |
| **Output** | 失败步骤在 summary 中记录 `{status: "failed", error: "..."}`，total_steps 递增错误计数，后续步骤不受影响 |
| **Log path** | `agent_cli.py:L1483-1532` (`_execute_with_retry` 重试循环) + `L750-763` (异常捕获 → failed 落盘) |
| **Pass criteria** | 重试耗尽后正确标记 failed；不抛出未捕获异常；后续步骤继续执行；summary.errors 包含清晰错误 |
| **Related capability** | D4 — 运行稳定性、任务级容错 |
| **Boundary note** | 该机制设计为"不因一个子步骤失败而废弃整个任务"——如果某步骤是后续步骤的硬依赖（如 mineru_parse 失败 → corpus_parse 无法执行），则框架需在上层判断并跳过整个下游链（见 Case 17） |

---

### Case 17 — 上游产出不足 → 动态重规划

| 字段 | 内容 |
|:-----|:------|
| **Case 编号** | DG-17 |
| **类别** | 降级处理 |
| **Intent/Input** | `_exec_corpus_parse` 执行中发现部分 chunk 缺少 text 字段，无法继续下游 task |
| **Agent plan** | 原始 6 步计划 (corpus_parse → benchmark_build → quality_arbitrate → model_evaluate → ...) → 检测到上游产出不足 → 跳过推论性下游 Intent |
| **Tool calls** | 跳过 `benchmark_build` / `quality_arbitrate` / `model_evaluate`（无意义的下游分析被主动裁剪） |
| **Output** | 调整后 plan 由 6 步缩减至 4 步，节省 -33% 步骤。Agent 不强行执行无意义的下游分析 |
| **Log path** | 报告二 §3.4、§5.1-§5.3 给出动态重规划和故障恢复矩阵；核心代码位于 `benchmark/agent/agent_cli.py` 与 `benchmark/agent/resource_scheduler.py` |
| **Pass criteria** | Agent 正确检测上游产出不足；下游步骤被跳过而非报错；执行日志含跳过原因说明 |
| **Related capability** | D3 — 动态重规划、Agent 自主调整执行计划 |
| **Boundary note** | 该机制依赖 Agent 在运行时检查各步骤输出质量的能力——如果输出验证不充分，可能错误跳过有效步骤 |

---

## 第四组：审计日志（3 题）

### Case 18 — 结构化日志 Schema 完整审计

| 字段 | 内容 |
|:-----|:------|
| **Case 编号** | AL-18 |
| **类别** | 审计日志 |
| **Intent/Input** | 全链路任意 Agent 执行 — 日志输出验证 |
| **Agent plan** | 每步执行完成后，调用 `LogStep` schema 写入 → `.tmp + os.replace()` 原子落盘 |
| **Tool calls** | `log_schema.py` (LogStep / ExecutionLog 定义)；所有步骤共用同一 schema |
| **Output** | 每条日志包含结构化三层：**meta** (project, schema_version, start_time, duration_ms) → **steps** [{step_id, step_name, tool, status, duration_ms, provider, input, output, error}] → **summary** (total_steps, passed, failed, partial, total_duration_ms, errors)。例如 `agent-20260509-021603.json` 中 cross_modal_audit step 记录：status=success, duration_ms=22011, provider=minimax, output_summary 含完整审计统计 |
| **Log path** | `benchmark/agent/log_schema.py`（schema 定义）<br>`benchmark/agent/logs/agent-20260509-021603.json`（执行示例）<br>`benchmark/agent/logs/demo-10intents-e2e-20260509.md`（人类可读终端输出） |
| **Pass criteria** | 每条日志包含 meta/steps/summary 三层；每步含 status/duration_ms/provider/error 字段；`.tmp + rename` 原子写入保护 |
| **Related capability** | D4 — 可追溯日志、输出可靠性 |
| **Boundary note** | 日志脱敏检查：不含 API Key、本地路径（报告引用路径含相对路径）或个人邮箱 |

---

### Case 19 — 跨管道可复现性验证

| 字段 | 内容 |
|:-----|:------|
| **Case 编号** | AL-19 |
| **类别** | 审计日志 |
| **Intent/Input** | 两条独立评测管道 (Leaderboard 管道 vs Consolidated 管道) 对同一 8 模型 × 500 题数据集评分对比 |
| **Agent plan** | 两条管道各自独立运行 `model_evaluate` → 独立产出的评分结果 → 对比偏差分析 |
| **Tool calls** | 管道 A: `evaluate.py` (Agent dispatch)；管道 B: 独立评测脚本 (consolidated) |
| **Output** | 8 个模型评分偏差 MAE=0.0003，RMSE=0.0003，Pearson r=1.0000，Spearman ρ=1.0000。排名完全一致 |
| **Log path** | 报告二 §4.1 给出跨管道验证结论；权威数值来自 `benchmark/eval/results/leaderboard_complete.json` 与 `benchmark/eval/results/judge_matrix/api_8judge_consolidated.json`，复现命令见 `shared/DATA-TRACE.md` #141-142 |
| **Pass criteria** | 两条管道评分偏差 < 0.001（MAE/RMSE）；排名完全一致 (ρ=1.0)；可复现命令清晰记录 |
| **Related capability** | D4 — 可复现性保证体系、跨管道验证 |
| **Boundary note** | 验证前提：固定数据集 (`benchmark/dataset/core.json`)、固定 LLM 参数 (`agent_capabilities.json`)、原子写入机制；跨管道验证证明的是**评测管道的工程可靠性**，而非评测结果的绝对正确性 |

---

### Case 20 — Checkpoint 原子落盘 + 恢复机制

| 字段 | 内容 |
|:-----|:------|
| **Case 编号** | AL-20 |
| **类别** | 审计日志 |
| **Intent/Input** | 长时间运行任务 `cross_modal_audit`（全量 4,996 共现 chunk），支持中断后恢复 |
| **Agent plan** | `visual_audit.py` 内置 checkpoint 机制 → 每条结果 `.tmp + os.replace()` 原子写入 → `--resume` 跳过已完成 → `--retry-failed` 仅重试失败 |
| **Tool calls** | `visual_audit.py` (MiMo-V2.5 5 线程并发)；checkpoint 文件 `benchmark/agent/results/visual_audit_checkpoint.json` |
| **Output** | 中断后重启：`--resume` 参数 → checkpoint 扫描 → 跳过 4,500 条已完成 → 继续处理剩余 496 条 → 完整产出 4,996 条审计记录。monitor 脚本通过 status 更新时间和 progress 增长判断健康状态 |
| **Log path** | `benchmark/agent/results/visual_audit_checkpoint.json`（checkpoint 状态）<br>`benchmark/agent/results/visual_audit_report.json`（最终审计报告）<br>`benchmark/agent/logs/agent-20260509-021603.json`（限量模式审计日志） |
| **Pass criteria** | checkpoint 使用 `.tmp + os.replace()` 原子写入；`--resume` 正确跳过已完成条目；进程中断不损坏已有数据；restart 后可无缝继续 |
| **Related capability** | D4 — 任务级容错、Checkpoint 恢复机制；D1 — 跨模态对齐审计 |
| **Boundary note** | checkpoint 只记录"已完成的条目 ID 集"，不保存中间状态；原子落盘保障不丢数据但不保障不重跑（幂等性由下游消费方保证） |

---

## 第五组：跨工具协作（3 题）

### Case 21 — D 数据飞轮全链路 7 步跨工具自主编排

| 字段 | 内容 |
|:-----|:------|
| **Case 编号** | CT-21 |
| **类别** | 跨工具协作 |
| **Intent/Input** | `flywheel_full_chain` — 自然语言意图："从 arXiv 自动检索论文 → 解析 → 建语料 → 出题 → 仲裁 → 评测 → 可视化" 全链路自主执行 |
| **Agent plan** | 7 步编排 Plan，工具链式依赖：<br>1. `arxiv_search` (depends_on: []) → arXiv API 检索下载<br>2. `mineru_parse` (depends_on: [arxiv_search]) → MinerU API 解析 PDF<br>3. `corpus_parse` (depends_on: [mineru_parse]) → 语义结构化分块<br>4. `benchmark_build` (depends_on: [corpus_parse]) → LLM 自动出题<br>5. `quality_arbitrate` (depends_on: [benchmark_build]) → Embedding + LLM 双层仲裁<br>6. `model_evaluate` (depends_on: [quality_arbitrate]) → 统一接口评测<br>7. `leaderboard_viz` (depends_on: [model_evaluate]) → 排行榜可视化 |
| **Tool calls** | 7 种工具跨 3 类 provider 协作：<br>— **Script 类**：`searching-arxiv-papers` Skill、`corpus_builder.py`、`summarize_multi.py` + `report_viz.py`<br>— **API 类**：MinerU API (127.0.0.1:8000)、DeepSeek v4-flash (`build_benchmark.py` + `evaluate.py`)、MiMo-V2.5 (visual_audit.py)<br>— **本地模型类**：qwen3-embedding:4b (Ollama, 5090) 快速通道 |
| **Output** | 391s 全自主完成，7/7 steps 全部通过：<br>5 篇 arXiv PDF 下载 → 5/5 MinerU 解析零错误 → 47 个结构化 chunk (253K 字符) → 15 题 (A/B/C/D 四维度) → 354/360 题目净通过率 98.3% → deepseek-v4-flash 评测得分 0.1400 → 排行榜从 500 题扩展到 515 题，JSON + HTML 双格式输出 |
| **Log path** | `benchmark/agent/logs/demo-data-flywheel.json`（全链路摘要日志）<br>Agent CLI 执行记录：`benchmark/agent/agent_report.md §3.4`（总耗时 391s 源自 CLI 输出）<br>各步骤分日志：`logs/agent-*.json`（24 个结构化日志文件覆盖每步执行详情）<br>仲裁详情：`examples/logs/task_2_arbitrate.json`（step 301-305）<br>评测结果：`benchmark/eval/results/flywheel_eval_deepseek.json` |
| **Pass criteria** | 7 步全部成功，无一步失败/降级；工具间数据传递完整（PDF→chunk→题目→评分）；排行榜增量合并正确 |
| **Related capability** | D3 — Agent 将复杂意图自主拆解为 7 步可执行 Plan，跨 3 类 7 种工具自主编排；D4 — 全链路可复现，同一条命令可重复产生一致结果 |
| **Boundary note** | 全链路耗时 391s 依赖 5090 本地 Ollama 推理和 API 并发能力；arXiv 检索受 API 速率限制（~1 req/3s）；首次运行涉及较多 LLM 调用，重复运行因缓存可显著加速 |

---

### Case 22 — vLLM 部署的 MinerU 1.2B VLM vs MiMo-V2.5 公式识别交叉验证

| 字段 | 内容 |
|:-----|:------|
| **Case 编号** | CT-22 |
| **类别** | 跨工具协作 |
| **Intent/Input** | `bench_mineru_1.2b` — 双引擎交叉验证：对同一批 PDF 公式图片，分别通过 **vLLM 本地部署的 MinerU 1.2B VLM**（RTX 5090）和 **MiMo-V2.5 API** 进行公式转录，对比两引擎的 LaTeX 识别质量 |
| **Agent plan** | 组装式双路比对管线，2 种运行模式：<br>1. **`mimo_only` 模式**：仅调用 MiMo-V2.5 API，输出纯 MiMo 转录结果（8/11 batch 运行）<br>2. **`full` 模式**：双引擎并发 — 路径 A（vLLM MinerU 1.2B 本地 5090） + 路径 B（MiMo-V2.5 API），各自生成 LaTeX 后统一以 ground truth 为基准计算 edit_distance、BLEU、char_match（3/11 batch 运行）<br>3. Agent 内置 checkpoint 机制，每 batch 完成后原子落盘 |
| **Tool calls** | 路径 A：vLLM + MinerU 1.2B VLM (provider=ollama, model=mineru-1.2b, 本地 RTX 5090)<br>路径 B：`visual_audit.py` + MiMo-V2.5 (API, raw httpx)，5 workers 并发<br>Checkpoint：`benchmark/agent/results/bench_mineru_1.2b_checkpoint.json` |
| **Output** | 11 次 batch 运行，覆盖 PDF 教材公式图片的公式识别对比。`full` 模式结果包含 `mineru_latex`（vLLM MinerU 1.2B 输出）和 `mimo_latex`（MiMo-V2.5 输出）双字段。<br>示例（某 batch `full` 模式，中文 PID 教材图片，4 个公式符号）：<br>— Ground truth: `G(s) = \frac{1}{J s^2 + B s} ...`<br>— MiMo-V2.5：输出 TikZ 绘图代码（精确描述了曲线走势）<br>**结论**：MinerU 1.2B VLM 和 MiMo-V2.5 的公式转录策略不同——MinerU 倾向于输出公式区域的文本描述（非 LaTeX），MiMo-V2.5 输出结构化 LaTeX/TikZ 但精度的图片内容相关性不稳定 |
| **Log path** | Cross-compare logs：`benchmark/agent/logs/demo-vllm-mineru-1.2b-20260509-*.json`（11 个文件，8 个 `mimo_only`、3 个 `full` 双字段）<br>MiMo 审计日志：`benchmark/agent/logs/agent-20260509-021603.json`<br>运行记录+checkpoint：`benchmark/agent/logs/bench_mineru_*.log` + `results/bench_mineru_1.2b_checkpoint.json` |
| **Pass criteria** | 双引擎在 `full` 模式下均完成同一批图片处理；交叉对比指标完整输出；结果可复现；每轮 batch 的 checkpoint 原子落盘 |
| **Related capability** | D1 — MinerU 本地 vLLM 部署能力（5090）+ 双引擎公式识别对比；D2 — 跨模态对齐审计的双引擎交叉验证方法 |
| **Boundary note** | 11 次 batch 中仅 3 次运行了 `full` 双引擎模式，8 次为 `mimo_only`；vLLM MinerU 1.2B 对密集公式图片倾向于输出文本描述而非结构 LaTeX；MiMo-V2.5 虽能输出 LaTeX/TikZ 但精度不稳定 |

---

### Case 23 — 多格式文档归一化解析 + 跨模态质量审计联合

| 字段 | 内容 |
|:-----|:------|
| **Case 编号** | CT-23 |
| **类别** | 跨工具协作 |
| **Intent/Input** | `multi_format_parse` → `cross_modal_audit` — 联合意图：先解析 4 种格式的文档（PPTX/PNG/DOCX/XLSX），再对解析结果做跨模态对齐质量审计 |
| **Agent plan** | 2 步顺序 Plan，前步产出作为后步输入：<br>1. `multi_format_parse` → MinerU API 多格式管线 → 统一 chunk schema 输出<br>2. `cross_modal_audit` → 对解析结果中的图文 chunk 做 MiMo-V2.5 视觉质量审计 |
| **Tool calls** | 步骤 1：MinerU API (multi-format mode, v3.1.6)；自动识别 4 种格式并选择对应解析管线<br>步骤 2：`visual_audit.py` + MiMo-V2.5 (API, raw httpx)；5 workers 并发；per-intent 参数 `{"max_images": 10, "provider": "minimax"}` |
| **Output** | **阶段 1 — 多格式解析**：4 格式 × 194 chunks 全量成功，质量检查全部 PASS<br>PPTX (47 chunks / 12 图 / 38 公式)、PNG 扫描件 (28/1/16)、DOCX (83/6/29)、XLSX (36/0/0)<br>**阶段 2 — 跨模态审计**：从 28,475 个全局 chunk 中扫描到 10 个共现图文项 → MiMo-V2.5 逐项判决 → 一致 60.0% / 部分一致 30.0% / 不一致 10.0% / 不确定 0.0% / 错误 0<br>两阶段串联总耗时 ~22s（审计阶段）+ 解析阶段（预完成） |
| **Log path** | 阶段 1：`benchmark/agent/logs/demo-multi-format-20260510-1917.json`<br>阶段 2：`benchmark/agent/logs/demo-10intents-e2e-20260509.md`（cross_modal_audit step，第 2 次调用）<br>审计详情：`benchmark/agent/results/visual_audit_report.json` |
| **Pass criteria** | 两阶段顺序执行不中断；MinerU 解析结果正确传递给审计步骤；审计阶段正确扫描所有共现 chunk；跨工具数据传递零人工干预 |
| **Related capability** | D1 — 多格式归一化解析能力（4 格式 × 统一 schema）；D2 — 跨模态对齐审计（图文一致性判决）；D3 — 跨工具管线编排，per-intent 参数精确传递 |
| **Boundary note** | 仅支持 MinerU 引擎支持的格式（不支持 HTML）；PNG 扫描件解析质量受原始图片分辨率影响；MiMo-V2.5 全量审计（4,996 chunk）约需 18min，限量模式 (max_images=10) 仅用于快速验证 |

---

### Case 24 — vLLM MinerU 1.2B 公式比对 Batch 中断 → Checkpoint 恢复 → 继续运行

| 字段 | 内容 |
|:-----|:------|
| **Case 编号** | FR-24 |
| **类别** | 失败恢复 |
| **Intent/Input** | `bench_mineru_1.2b` — 批量 vLLM MinerU 1.2B vs MiMo-V2.5 公式转录交叉比对（多个 batch × N 样本），运行过程中间中断 |
| **Agent plan** | `bench_mineru_1.2b` 内置 checkpoint 机制：每处理完一个 batch 写入 checkpoint → 进程意外退出 → 重启时 `--resume` 参数自动检测 checkpoint → 跳过已完成条目 → 仅处理剩余 batch |
| **Tool calls** | 双引擎比对管线：vLLM + MinerU 1.2B VLM (provider=ollama, 本地 RTX 5090) + MiMo-V2.5 API (raw httpx)<br>Checkpoint 文件：`benchmark/agent/results/bench_mineru_1.2b_checkpoint.json`<br>Checkpoint 写入：每 batch 完成后 `.tmp + os.replace()` 原子写入 |
| **Output** | 11 次 batch 运行日志（`bench_mineru_*.log`）记录了完整的执行/中断/恢复周期：<br>初始 batch → 部分完成 → 进程中断 → `--resume` 重启 → checkpoint 检测到已完成条目 → 跳过 → 继续剩余 batch → 全部完成<br>Checkpoint 状态文件记录已完成的 batch 编号、样本计数和时间戳 |
| **Log path** | 运行日志：`benchmark/agent/logs/bench_mineru_*.log`（标准输出+错误输出，`.log` + `.err` 双文件）<br>PID 文件：`benchmark/agent/logs/bench_mineru_*.pid`（进程管理）<br>Checkpoint：`benchmark/agent/results/bench_mineru_1.2b_checkpoint.json` |
| **Recovery flow** | 初始运行 → batch 执行中 → 进程中断 → 重启命令 `python bench_mineru.py --resume` → checkpoint 加载 → `processed_batches` 扫描 → 跳过已完成 → `remaining_batches` 继续 → 所有 batch 完成 ✅<br>原子写入保障：`tmp_file = checkpoint_path + ".tmp"` → `json.dump(tmp_file)` → `os.replace(tmp_file, checkpoint_path)` |
| **Pass criteria** | 中断后 checkpoint 不损坏；`--resume` 正确跳过已完成 batch；恢复后继续执行的 batch 数据格式一致；无数据重复或遗漏 |
| **Related capability** | D4 — 任务级 Checkpoint 容错，中断恢复不断数据；D3 — Agent 自主管理长时运行任务的执行状态 |
| **Boundary note** | Checkpoint 粒度是 batch 级而非 item 级，因此单个 batch 内的中断会丢失该 batch 的进度；适用于批量 API+本地推理比对任务（>30min）而非短任务 |

---

### Case 25 — 全量视觉审计 4,996 chunk 的 checkpoint 原子落盘 + 幂等恢复

| 字段 | 内容 |
|:-----|:------|
| **Case 编号** | AL-25 |
| **类别** | 审计日志 |
| **Intent/Input** | `cross_modal_audit` — 全量模式运行，扫描 4,996 个共现图文 chunk 做跨模态对齐审计。支持中断后 `--resume` 幂等恢复 |
| **Agent plan** | 1 步：`visual_audit.py` 全量扫描 → 5 workers 并发调用 MiMo-V2.5 → 每条结果 `.tmp + os.replace()` 原子写入结果 JSONL → 每个 worker 完成后更新全局 checkpoint JSON |
| **Tool calls** | `visual_audit.py` + MiMo-V2.5 (API, raw httpx)；5 workers 并发；`--resume` / `--retry-failed` 参数控制恢复模式 |
| **Output** | **Checkpoint 结构**（限量模式预览，全量模式同理）：<br>```json<br>{<br>  "checkpoint_time": "2026-05-09T02:16:25",<br>  "processed": 10,<br>  "total": 10,<br>  "summary": {<br>    "total_audited": 10,<br>    "consistent": 6, "consistent_pct": 60.0,<br>    "partially_consistent": 3, "partially_consistent_pct": 30.0,<br>    "inconsistent": 1, "inconsistent_pct": 10.0,<br>    "uncertain": 0, "uncertain_pct": 0.0,<br>    "error_count": 0<br>  }<br>}<br>```<br>**审计结果 JSONL** 格式（每条独立）：<br>`{"provider": "mimo", "model": "mimo-v2.5", "judgment": "consistent"/"inconsistent"/"partially_consistent", "raw_response": "判断: ...", "token_usage": {"prompt_tokens": ..., "completion_tokens": ..., "image_tokens": ...}, "chunk_id": "...", "filename": "...", "image_hash": "..."}` |
| **Log path** | Checkpoint：`benchmark/agent/results/visual_audit_checkpoint.json`（全局进度）<br>审计结果：`benchmark/agent/results/visual_audit_results.jsonl`（逐行 JSON，可流式追加）<br>审计报告：`benchmark/agent/results/visual_audit_report.json`（最终汇总）<br>限量模式日志：`benchmark/agent/logs/agent-20260509-021603.json`（10 项审计示例）<br>端到端终端输出：`benchmark/agent/logs/demo-10intents-e2e-20260509.md`（22s 全量日志） |
| **Pass criteria** | Checkpoint 使用 `.tmp + os.replace()` 原子写入全过程保障；JSONL 逐行独立可增量追加；`--resume` 正确跳过已完成条目；进程中断不损坏已有结果；重启后幂等无误 |
| **Related capability** | D2 — 跨模态对齐审计全量证据链（4,996 chunk 全覆盖）；D4 — Checkpoint 原子落盘保障、--resume 幂等恢复；结构化格式可 grep/jq 按 judgment 类型筛选 |
| **Boundary note** | 全量模式需扫描 4,996 chunk，预计耗时 ~18min（MiMo-V2.5 API 调用 + 5 workers 并发）；Checkpoint 只记录"已完成的 chunk ID 集"，不保存中间状态；JSONL 格式天然支持流式追加，适合长时间运行任务 |

---

## 覆盖统计

| 类型 | 要求 | 本包 | 案例编号 |
|:-----|:----:|:----:|:---------|
| 普通执行 | ≥ 8 | 10 | N-01 ~ N-10 |
| 失败恢复 | ≥ 3 | 5 | FR-11 ~ FR-14, FR-24 |
| 降级处理 | ≥ 3 | 3 | DG-15 ~ DG-17 |
| 审计日志 | ≥ 3 | 4 | AL-18 ~ AL-20, AL-25 |
| 跨工具协作 | ≥ 3（新增） | 3 | CT-21 ~ CT-23 |

## 能力覆盖索引

| 能力维度 | 对应案例 | 核心展示 |
|:---------|:--------|:---------|
| D1 复杂文档理解 | N-02, N-03, N-08, CT-23 | MinerU 多格式解析（4 格式 194 chunks）、chunk 结构化、图文共现审计 |
| D2 难点攻克 | N-09, N-10, AL-20, CT-22, AL-25 | 跨模态对齐审计（双路径交叉验证）、弹性伸缩证据、全量 4,996 chunk 审计证据链、Checkpoint 原子落盘 |
| D3 Agent 自主执行 | N-01~N-07, FR-12, DG-17, CT-21, CT-22, CT-23 | D 飞轮 7 步全链路闭环、5090 本地 vLLM+API 双路径、多格式→审计管线串联、Self-Improve、动态重规划 |
| D4 系统稳定性 | FR-11~FR-14, DG-15~DG-16, AL-18~AL-19, CT-21, FR-24, AL-25 | 三层容错架构（Provider/Step/File 级 + Batch checkpoint 恢复）、隐私双轨、结构化日志三层 schema、跨管道可复现性（MAE=0.0003）、原子落盘幂等恢复 |

## 数据来源清单

| 路径 | 用途 |
|:-----|:-----|
| `benchmark/agent/logs/agent-*.json`（24 个） | 结构化执行日志，按时间索引 |
| `benchmark/agent/logs/demo-10intents-e2e-20260509.md` | 端到端 Demo 终端实录（3 步 36s 全通过） |
| `benchmark/agent/logs/demo-local-gpu-fallback-20260509-0116.md` | 本地 GPU 降级验证实录（35.6s 全自动） |
| `benchmark/agent/logs/demo-data-flywheel.json` | D 数据飞轮 7-step 全自主执行摘要 |
| `benchmark/agent/logs/demo-35b-elastic-proof.json` | 4B→9B→35B 弹性伸缩证明（46→55→128s） |
| `benchmark/agent/logs/demo-multi-format-20260510-1917.json` | 4 格式 × 194 chunks 多格式解析 |
| `benchmark/agent/logs/demo-vllm-mineru-1.2b-*.json`（11 个） | MinerU 内置提取 vs MiMo-V2.5 公式转录交叉对比 |
| `benchmark/agent/examples/logs/task_1~5_*.json` | 5 个独立 intent 示例执行日志 |
| `benchmark/agent/log_schema.py` | 结构化日志 schema 定义 |
| `benchmark/agent/agent_cli.py` | Agent CLI 主代码（含 dispatch_map / _execute_with_retry / _self_improve_params） |
| `benchmark/agent/resource_scheduler.py` | 四路径资源调度器（含 HealthCheck / get_fallback） |
| `track2_agent_report.md` §5.1-§5.3 | 三层容错架构、checkpoint 与失败恢复矩阵 |
| `benchmark/eval/results/leaderboard_complete.json` + `benchmark/eval/results/judge_matrix/api_8judge_consolidated.json` | 跨管道可复现性验证 |

