# ControlMind 三赛道来源与证据矩阵

> 本文件定位：把三赛道的核心问题、方法论、实验数据和云端展示统一到同一张来源矩阵中。矩阵用于连接主报告、案例包、DATA-TRACE、云端 Demo 与本地复现入口。

| 赛道 | 核心问题 | 方法论 | 实验数据与来源 | 云端展示对应关系 |
|:---|:---|:---|:---|:---|
| 赛道一：Sci-Align | 控制科学论文、教材和公式密集 PDF 难以直接进入大模型评测；传统 QA 数据集缺少来源、公式、图片和推理步骤的统一追溯。 | 以 MinerU 解析为结构化入口，构建 A/B/C/D 四维认知评测；每题绑定来源、参考答案、评分规则和模型回答，使用多模型 Judge 与自修正 trace 校验评测稳定性。 | `benchmark/dataset/core.json`、`benchmark/eval/results/leaderboard_complete.json`、`benchmark/eval/reports/cross_judge_kappa.json`、`docs/submissions/shared/DATA-TRACE.md`、赛道一报告附录 A。 | `/track1` 对公开 PDF 上传、MinerU 官方 API 解析、DeepSeek 云端出题和 DeepSeek 云端评分提供实时闭环；全量评测和训练实验不在云端重跑，通过 CLI、样例包和 DATA-TRACE 核验。 |
| 赛道二：Data Agent | 科学语料生产不是单脚本问题，而是多步骤、多资源、多失败模式的长链路；缺少可恢复、可审计、可迁移的执行协议。 | 将任务拆成 intent、DAG、资源策略、工具调用、日志 schema 和产物索引；用统一 Agent 协议连接解析、审计、飞轮、微调和验收。 | `benchmark/agent/logs/`、`benchmark/agent/capabilities/agent_capabilities.json`、`docs/submissions/shared/track2_agent_20_cases.md`、`docs/submissions/shared/DATA-TRACE.md`、赛道二报告附录 A/C。 | `/track2` 展示公开任务规划、DAG 和来源产物回放；云端不执行私有长任务，但保留与完整系统一致的能力注册、日志结构和核验入口。 |
| 赛道三：医学 RAG | 医学文献问答容易变成模型凭记忆回答；检索上下文、引用覆盖、安全拒答和中英文桥接缺少可复现实验。 | 构建章节感知 chunk、混合检索、多索引对照、source-structured answer、claim check 和安全分流；中文问题桥接英文文献，回答只组织本次检索来源。 | `benchmark/eval/results/medical_rag_eval*.json`、`benchmark/eval/results/medical_rag_zh_ask*_traces.jsonl`、`data/sources_medical/`、`docs/submissions/shared/DATA-TRACE.md`、赛道三报告附录 A。 | `/track3` 只开放已验证医学 RAG 案例回放，展示来源卡片、claim 状态、机制解释和安全边界；患者资料、私有索引和真实问诊不进入云端 Demo。 |

## 矩阵结论

三个赛道不是彼此孤立的样例。MinerU 负责把复杂科学文档变成可消费结构，Agent 负责把复杂工作拆成可审计流程，评测和 RAG 负责把模型输出绑定到来源和边界。云端 Demo 展示可公开体验的切面，完整系统保留重资产能力和私有部署路径。
