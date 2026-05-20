"""
build_data_trace_bundle.py — 从 DATA-TRACE 引用的源文件中构建集中导航包

策略：复制（不移动）所有 DATA-TRACE 引用的数据源文件到
      docs/submissions/data_trace_bundle/，
      按报告章节分组，生成 SHA-256 校验清单和 README。

注意：报告、脚本等已 git tracked 的文件不重复复制。
      data_trace_bundle 是集中导航层，不是数据替代。

排除：
  - 已 git tracked 的报告 / 脚本（不重复）
  - 非文件源（git log, 管线日志）
  - 已删除条目

用法：
  conda run --no-capture-output -n myenv python scripts/build_data_trace_bundle.py
  conda run --no-capture-output -n myenv python scripts/build_data_trace_bundle.py --full-public
"""
import hashlib
import json
import shutil
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BUNDLE_DIR = ROOT / "docs" / "submissions" / "data_trace_bundle"

# ============================================================
# 文件清单 — 按 DATA-TRACE 章节分组，仅数据文件
# 格式: (subdir, relative_source_path)
# ============================================================

FILES = [
    # --- 01 语料规模 (DATA-TRACE #1-16) ---
    ("01_corpus_scale", "corpus/metadata.json"),
    ("01_corpus_scale", "corpus/stats/corpus_stats.json"),
    ("01_corpus_scale", "benchmark/eval/results/multimodal_chunks.json"),
    ("01_corpus_scale", "benchmark/eval/results/image_formula_cooccurrence.json"),
    ("01_corpus_scale", "benchmark/eval/results/chunk_embedding/a1_global_pca.json"),
    ("01_corpus_scale", "benchmark/eval/results/chunk_embedding/a2_doc_similarity.json"),
    ("01_corpus_scale", "benchmark/eval/results/chunk_embedding/a3_redundancy.json"),
    ("01_corpus_scale", "benchmark/eval/results/chunk_embedding/a4_train_eval.json"),

    # --- 02 Benchmark 设计 (DATA-TRACE #17-23) ---
    ("02_benchmark", "benchmark/dataset/core.json"),
    ("02_benchmark", "benchmark/dataset/multimodal_index.json"),
    ("02_benchmark", "benchmark/dataset/flywheel_filtered.json"),

    # --- 03 排行榜 & 评测 (DATA-TRACE #38-42, #61-63, #106-108) ---
    ("03_leaderboard", "benchmark/eval/results/leaderboard.json"),
    ("03_leaderboard", "benchmark/eval/results/qwen3.5_9b_target_eval.json"),
    ("03_leaderboard", "benchmark/eval/results/qwen3.5_9b_answers.jsonl"),
    ("03_leaderboard", "benchmark/eval/results/errata_v1.1.json"),

    # --- 04 QLoRA & PPL (DATA-TRACE #47-54) ---
    ("04_qlora_ppl", "finetune/output/eval_finetuned_report.json"),
    ("04_qlora_ppl", "finetune/output/eval_baseline_4b_report.json"),
    ("04_qlora_ppl", "finetune/output/perplexity_delta.json"),
    ("04_qlora_ppl", "finetune/output/perplexity_delta_9b.json"),
    ("04_qlora_ppl", "finetune/output/qlora-qwen4b-cross/training.status.json"),

    # --- 05 跨模态对齐审计 (DATA-TRACE #55-58) ---
    ("05_cross_modal", "benchmark/eval/results/cross_modal_audit_summary.json"),

    # --- 06 视觉审计 (DATA-TRACE #71) ---
    ("06_visual_audit", "benchmark/agent/results/visual_audit_results.jsonl"),

    # --- 07 数据飞轮 (DATA-TRACE #22, #59-64) ---
    ("07_flywheel", "benchmark/agent/agent_capabilities.json"),
    ("07_flywheel", "benchmark/agent/logs/demo-data-flywheel.json"),
    ("07_flywheel", "benchmark/eval/results/flywheel_eval_deepseek.json"),
    ("07_flywheel", "benchmark/eval/results/flywheel_progress_deepseek.jsonl"),
    ("07_flywheel", "data/sources_flywheel/2605.02370_Robust Adaptive Predictive Control for Hook-Based Aerial Tra.pdf"),
    ("07_flywheel", "data/sources_flywheel/2605.03662_Feasibility-aware Hybrid Control for Motion Planning under S.pdf"),
    ("07_flywheel", "data/sources_flywheel/2605.05182_A Closed-Form Dual-Barrier CBF Safety Filter for Holonomic R.pdf"),
    ("07_flywheel", "data/sources_flywheel/2605.05575_Maximal Controlled Invariant-MPC - Enhancing Feasibility and.pdf"),
    ("07_flywheel", "data/sources_flywheel/2605.06630_Quantifying Trade-Offs Between Stability and Goal-Obfuscatio.pdf"),

    # --- 08 Think 对照实验 (DATA-TRACE #75) ---
    ("08_think_probe", "benchmark/eval/results/think_probe_35b_10queries.json"),

    # --- 09 赛道三 Medical RAG (DATA-TRACE #88-105, #117-120) ---
    ("09_medical_rag", "data/sources_medical/qa/qa_output.json"),
    ("09_medical_rag", "data/sources_medical/vision/vision_chunks_manifest.json"),
    ("09_medical_rag", "data/sources_medical/vision/vision_quality_control.json"),
    ("09_medical_rag", "data/sources_medical/vision/vision_descriptions.jsonl"),
    ("09_medical_rag", "data/sources_medical/vision/vision_descriptions_qwen35.jsonl"),
    ("09_medical_rag", "benchmark/eval/results/medical/vision_ab_comparison.json"),
    ("09_medical_rag", "data/sources_medical/medbench/medbench_35b_speed_probe.json"),
    ("09_medical_rag", "benchmark/eval/results/medical_rag_eval.json"),
    ("09_medical_rag", "benchmark/eval/results/medical_rag_eval.md"),
    ("09_medical_rag", "benchmark/eval/results/medical_rag_eval_zh_ask.json"),
    ("09_medical_rag", "benchmark/eval/results/medical_rag_eval_zh_ask.md"),
    ("09_medical_rag", "benchmark/eval/results/medical_rag_zh_ask_traces.jsonl"),
    ("09_medical_rag", "benchmark/eval/results/medical_rag_eval_synthesis_smoke.json"),
    ("09_medical_rag_large", "data/sources_medical/index/medical.index"),
    ("09_medical_rag_large", "data/sources_medical/index/embeddings_cache.npy"),
    ("09_medical_rag_large", "data/sources_medical/index/bm25.pkl"),

    # --- 10 嵌入分析 PNG 图表 (DATA-TRACE #79-86) ---
    ("10_charts", "benchmark/eval/results/chunk_embedding/a1_global_pca.png"),
    ("10_charts", "benchmark/eval/results/chunk_embedding/a2_doc_similarity.png"),
    ("10_charts", "benchmark/eval/results/chunk_embedding/a2_doc_similarity_full.png"),
    ("10_charts", "benchmark/eval/results/chunk_embedding/a4_train_eval.png"),
    ("10_charts", "build/submission_experiment_figures/manifest.json"),
    ("10_charts_large", "benchmark/eval/results/chunk_embedding/embeddings_cache.npy"),

    # --- 11 本地吞吐与 HF embedding 短测 (DATA-TRACE #145-146) ---
    ("11_throughput", "docs/assets/medical/gpu_throughput.json"),
    ("11_throughput", "docs/assets/medical/hf_embedding_throughput.json"),
    ("11_throughput", "docs/assets/medical/hf_embedding_throughput_raw.json"),
]

EXCLUDED = []

FULL_PUBLIC_ONLY = {
    "benchmark/dataset/multimodal_index.json",
    "benchmark/eval/results/errata_v1.1.json",
    "benchmark/agent/agent_capabilities.json",
    "benchmark/agent/logs/demo-data-flywheel.json",
    "benchmark/eval/results/medical_rag_eval_synthesis_smoke.json",
    "data/sources_medical/index/medical.index",
    "data/sources_medical/index/embeddings_cache.npy",
    "data/sources_medical/index/bm25.pkl",
    "build/submission_experiment_figures/manifest.json",
    "benchmark/eval/results/chunk_embedding/embeddings_cache.npy",
    "docs/assets/medical/gpu_throughput.json",
    "docs/assets/medical/hf_embedding_throughput.json",
    "docs/assets/medical/hf_embedding_throughput_raw.json",
}

FULL_PUBLIC_EXCLUDED = [
    ("278 MB", "benchmark/eval/results/chunk_embedding/embeddings_cache.npy",
     "conda run --no-capture-output -n myenv python benchmark/eval/chunk_embedding_analysis.py"),
    ("33 MB", "data/sources_medical/index/medical.index",
     "conda run --no-capture-output -n myenv python -m controlsci.medical.indexing"),
    ("33 MB", "data/sources_medical/index/embeddings_cache.npy",
     "conda run --no-capture-output -n myenv python -m controlsci.medical.indexing"),
    ("17 MB", "data/sources_medical/index/bm25.pkl",
     "conda run --no-capture-output -n myenv python -m controlsci.medical.indexing"),
]

NON_FILE_SOURCES = [
    ("DT #23", "benchmark/agent/agent_report.md §3.4 L254 — Markdown 行引用"),
    ("DT #34", "抽样确认 — 人工核查"),
    ("DT #69", "git log — 版本控制元数据"),
    ("DT #70", "evaluate 管线日志 — 分布式运行时日志"),
    ("DT #73", "GPU 嵌入分析 — 已删除，无日志"),
    ("DT #74", "Ollama 评测进度日志 — 运行时日志"),
]


def sha256_file(filepath):
    h = hashlib.sha256()
    with open(filepath, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def main():
    if any(arg in {"-h", "--help"} for arg in sys.argv[1:]):
        print(__doc__.strip())
        return
    full_public = "--full-public" in sys.argv[1:]

    t_start = time.time()

    if BUNDLE_DIR.exists():
        shutil.rmtree(BUNDLE_DIR)
    BUNDLE_DIR.mkdir(parents=True)

    manifest = {
        "generated_at": time.strftime("%Y-%m-%dT%H:%M:%S"),
        "project": "ControlSci — 2026 MinerU Challenge",
        "generator": "scripts/build_data_trace_bundle.py",
        "strategy": "copy (源文件未移动); full_public=" + str(full_public).lower(),
        "description": "DATA-TRACE 配套数据集中导航包。所有数据均可在仓库原始位置找到。",
        "total_size_mb": 0,
        "files": [],
        "excluded": [],
        "non_file_sources": [],
    }

    total_bytes = 0
    copied = 0
    missing = 0

    for subdir, rel_path in FILES:
        if (not full_public) and rel_path in FULL_PUBLIC_ONLY:
            continue
        src = ROOT / rel_path.replace("\\", "/")
        if not src.exists():
            print(f"  MISSING: {rel_path}")
            missing += 1
            continue

        dest_subdir = BUNDLE_DIR / subdir
        dest_subdir.mkdir(parents=True, exist_ok=True)

        dest = dest_subdir / src.name
        if dest.exists():
            stem = src.stem
            for i in range(2, 100):
                dest = dest_subdir / f"{src.stem}_{i}{src.suffix}"
                if not dest.exists():
                    break

        shutil.copy2(src, dest)
        sha = sha256_file(dest)
        size = src.stat().st_size
        total_bytes += size
        copied += 1

        entry = {
            "bundle_path": str(dest.relative_to(BUNDLE_DIR)).replace("\\", "/"),
            "source_path": rel_path,
            "size_bytes": size,
            "size_mb": round(size / 1048576, 2),
            "sha256": sha,
        }
        manifest["files"].append(entry)
        print(f"  OK  {size/1024:>7.1f} KB  [{sha[:12]}]  {entry['bundle_path']}")

    manifest["total_size_mb"] = round(total_bytes / 1048576, 2)

    excluded_items = [] if full_public else FULL_PUBLIC_EXCLUDED
    for size_est, rel_path, regen_cmd in excluded_items:
        manifest["excluded"].append({
            "source_path": rel_path,
            "estimated_size": size_est,
            "reason": "可重新生成（衍生缓存文件）",
            "regeneration_command": regen_cmd,
        })
        print(f"  EXCL {size_est:>7}  {rel_path}")

    for label, note in NON_FILE_SOURCES:
        manifest["non_file_sources"].append({"label": label, "note": note})

    manifest_path = BUNDLE_DIR / "manifest.json"
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")

    write_readme(full_public=full_public)

    elapsed = time.time() - t_start
    print()
    print(f"{'='*60}")
    print(f"Bundle complete: {copied} copied, {missing} missing, {len(excluded_items)} excluded")
    print(f"Total size: {manifest['total_size_mb']:.1f} MB  |  Elapsed: {elapsed:.1f}s")
    print(f"Output: {BUNDLE_DIR}")


def write_readme(*, full_public: bool):
    readme = BUNDLE_DIR / "README.md"
    mode_text = "full-public 最大化公开包" if full_public else "light 核心溯源包"
    optional_rows = """| `09_medical_rag_large/` | 十一 | 医疗 RAG 原始索引与检索缓存 |
| `10_charts_large/` | 十 | 语料嵌入矩阵缓存 |
| `11_throughput/` | 十一 / 附录性能 | GPU 吞吐与 HF embedding 短测 (#145-146) |""" if full_public else ""
    excluded_text = (
        "无。`--full-public` 模式会复制可定位数据源文件，包括大型索引与缓存；报告、脚本、命令、git log 等非数据源不重复复制。"
        if full_public
        else """以下大型衍生文件默认不复制，可用 `--full-public` 生成最大化公开包：

| 文件 | 大小 | 生成命令 |
|:--|:--|:--|
| `benchmark/eval/results/chunk_embedding/embeddings_cache.npy` | 278 MB | `python benchmark/eval/chunk_embedding_analysis.py` |
| `data/sources_medical/index/medical.index` | 33 MB | `python -m controlsci.medical.indexing` |
| `data/sources_medical/index/embeddings_cache.npy` | 33 MB | `python -m controlsci.medical.indexing` |
| `data/sources_medical/index/bm25.pkl` | 17 MB | `python -m controlsci.medical.indexing` |"""
    )
    readme.write_text(f"""# DATA-TRACE Bundle — 可复现溯源资产集中导航

本目录是 [DATA-TRACE.md](../shared/DATA-TRACE.md) 的配套数据包。
所有文件均从项目仓库中以**复制**方式采集（源文件未移动），按报告章节分组。

生成模式：{mode_text}。

## 结构

| 子目录 | DATA-TRACE 章节 | 内容 |
|:--|:--|:--|
| `01_corpus_scale/` | 一 | 语料规模统计 (#1-16) |
| `02_benchmark/` | 二 | Benchmark 数据集与跨模态索引 (#17-23) |
| `03_leaderboard/` | 四 | 排行榜、评测结果与修订清单 (#38-42, #106-108) |
| `04_qlora_ppl/` | 五 | QLoRA 微调 & PPL (#47-54) |
| `05_cross_modal/` | 六 | 跨模态对齐审计 (#55-58) |
| `06_visual_audit/` | 八 | MiMo 全量视觉审计 (#71) |
| `07_flywheel/` | 七 | Agent 能力配置、飞轮日志与原始文献 (#22, #59-64) |
| `08_think_probe/` | 八 | Think 模式对照实验 (#75) |
| `09_medical_rag/` | 十一 | 赛道三 Medical RAG 与合成 smoke (#88-105, #117-120) |
| `10_charts/` | 十 | 嵌入分析 PNG 图表与提交插图 manifest (#79-86) |
{optional_rows}

## 完整清单

所有文件的 SHA-256 校验值见 `manifest.json`。

## 排除文件

{excluded_text}

## 许可

CC-BY-4.0。飞轮 arXiv 论文版权归原作者所有。
""", encoding="utf-8")


if __name__ == "__main__":
    main()
