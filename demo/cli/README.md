# ControlMind Demo CLI

三赛道快速验证入口 —— 评委可在 3 分钟内通过 CLI 查看所有赛道的关键样例。

## 快速开始

```bash
# Track1 — 科学数据对齐演示 (5 题)
conda run --no-capture-output -n myenv python demo/cli/controlscidemo track1 --quick

# Track2 — Agent 智能体演示 (5 题)
conda run --no-capture-output -n myenv python demo/cli/controlscidemo track2 --quick

# Track3 — 医疗 RAG 问答演示 (5 题)
conda run --no-capture-output -n myenv python demo/cli/controlscidemo track3 --quick

# 三赛道全跑
conda run --no-capture-output -n myenv python demo/cli/controlscidemo all --quick

# 指定数量
conda run --no-capture-output -n myenv python demo/cli/controlscidemo track1 --sample 10
```

说明：

- `--sample N` 会覆盖 `--quick`。
- Windows 控制台下 CLI 会主动使用 UTF-8 输出；如评委环境无法显示特殊符号，可设置 `CONTROLSCI_ASCII=1` 使用 ASCII 状态标记。

## 依赖

纯 Python 标准库，无需 `pip install`。如需 `requirements.txt` 仅声明 Python ≥ 3.10。

## 输出说明

每道题展示以下字段：

| 字段 | Track1 | Track2 | Track3 |
|------|--------|--------|--------|
| 编号 | Case 编号 | Case 编号 | Case 编号 |
| 类型 | 覆盖类型 (text/formula/table/chart) | 执行类别 (普通/失败恢复/降级/审计) | 回答类别 (证据/拒答/视觉增强) |
| 输入 | Input | Intent/Input | Question |
| 预期 | Expected behavior | Agent plan | System answer |
| 输出 | System output | Tool calls + Output | Confidence |
| 证据 | Evidence path (并检查存在性) | Log path (并检查存在性) | Retrieved evidence |
| 通过标准 | Pass criteria | Pass criteria | Pass criteria |
| 评分项 | Related score item | Related score item | Related score item |
| 边界 | Boundary note | Boundary note | Boundary note + Endpoint≠Conclusion |

## 验收标准

- [x] `controlscidemo track1 --quick` 在 30 秒内完成 ✅
- [x] 每条命令输出结果路径 + 评分项映射 ✅
- [x] 失败时给出清晰错误说明（非 Python traceback 裸抛） ✅
- [x] Windows UTF-8 控制台兼容 + ASCII fallback ✅
- [x] `--sample` 覆盖 `--quick` ✅
- [x] CLI 不依赖完整产品安装，纯标准库 ✅
- [x] Track2 采用日志重放模式，不启动真实 Agent 管道 ✅

## 数据源

- Track1: `docs/submissions/track1_sci_align_20_cases.md` → `benchmark/dataset/core.json` + `corpus/processed/`
- Track2: `docs/submissions/track2_agent_20_cases.md` → `benchmark/agent/logs/` + `benchmark/agent/examples/logs/`
- Track3: `docs/submissions/track3_medical_rag_20_cases.md` → `data/sources_medical/chunks/` + `data/sources_medical/qa/` + `data/sources_medical/vision/`
