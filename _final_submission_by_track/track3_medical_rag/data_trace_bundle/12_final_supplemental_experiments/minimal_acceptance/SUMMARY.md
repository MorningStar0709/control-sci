# Minimal Acceptance Checks

## Purpose

验证三个赛道公开入口在零 API Key 或跳过远端健康检查的最小条件下，能够完成基础资产、脚本入口和索引文件的快速验收。

## Result

| Track | Scope | Passed | Skipped | Failed | Runtime |
|---|---|---:|---:|---:|---:|
| Track 1 | Sci-Evo dataset and scoreboard | 5/5 | 0 | 0 | 0.1s |
| Track 2 | Agent capability registry and dry-run | 4/4 | 0 | 0 | 0.3s |
| Track 3 | Medical RAG indexes and API boundary | 6/7 | 1 | 0 | 0s |

## Key Checks

- Track 1: dataset schema validation, `core.json`, `full.json`, leaderboard, local-vs-API baseline scoreboard.
- Track 2: 14-intent capability registry, `reproduce_all` dry-run plan, Agent capability and CLI files.
- Track 3: text FAISS, BM25 sparse index, MiMo vision FAISS, qwen3.5 local vision FAISS, 730 local vision descriptions; API health check intentionally skipped.

## Evidence

- `track1_acceptance_demo.log`
- `track2_acceptance_demo.log`
- `track3_acceptance_demo_skip_api.log`

## Notes

本组检查用于确认公开入口和核心资产可被快速识别，不替代完整实验复现。
