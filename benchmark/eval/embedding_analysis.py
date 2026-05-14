#!/usr/bin/env python
"""Task 2c: 嵌入模型三大分析
2c-1: 四维语义聚类验证 — PCA 2D 散点图，按 A/B/C/D 着色
2c-2: 嵌入仲裁 vs LLM 仲裁一致性 — Spearman ρ
2c-3: 失败案例嵌入聚类 — KMeans 发现知识盲区簇

前置条件: Ollama qwen3-embedding:4b 运行中 (http://localhost:11434)
耗时: 嵌入计算 ~4min + 分析 ~1min = ~5min
"""

import argparse
import json
import sys
import time
from pathlib import Path
from collections import defaultdict

import numpy as np
import httpx

OLLAMA_EMBED_URL = "http://localhost:11434/api/embed"
EMBED_MODEL = "qwen3-embedding:4b"
BATCH_SIZE = 10
EMBED_DIM = 2560


def get_embeddings(texts, progress_label="embedding"):
    """批量获取 Ollama 嵌入向量，返回 (n, 2560) ndarray"""
    if not texts:
        print(f"  [{progress_label}] 空输入, 返回空数组", flush=True)
        return np.array([], dtype=np.float32)
    n = len(texts)
    all_emb = []
    t0 = time.time()
    for i in range(0, n, BATCH_SIZE):
        batch = texts[i : i + BATCH_SIZE]
        resp = httpx.post(
            OLLAMA_EMBED_URL,
            json={"model": EMBED_MODEL, "input": batch},
            timeout=120,
        )
        resp.raise_for_status()
        data = resp.json()
        embeddings = data.get("embeddings", [])
        if not embeddings:
            raise RuntimeError(f"Ollama returned empty embeddings for batch starting at {i}")
        all_emb.extend(embeddings)
        done = min(i + BATCH_SIZE, n)
        if done % 50 == 0 or done >= n:
            elapsed = time.time() - t0
            rate = done / elapsed if elapsed > 0 else 0
            print(f"  [{progress_label}] {done}/{n} ({done/n*100:.0f}%) — {rate:.1f}条/s", flush=True)
    elapsed = time.time() - t0
    print(f"  [{progress_label}] 完成 {n} 条, 总耗时 {elapsed:.1f}s, 均速 {n/elapsed:.1f}条/s", flush=True)
    return np.array(all_emb, dtype=np.float32)


def load_core_questions(core_path):
    """加载 core.json，返回 (questions_list, id->question map)"""
    with open(core_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    questions = data.get("questions", data) if isinstance(data, dict) else data
    id_map = {q["id"]: q for q in questions}
    return questions, id_map


def load_reports(reports_dir):
    """加载所有 *_report.json（跳过 chunk/cross_domain/progress），返回 {model: report}"""
    reports = {}
    for p in sorted(Path(reports_dir).glob("*_report.json")):
        name = p.name
        if "_chunk_" in name or "cross_domain" in name:
            continue
        if "leaderboard" in name or "kappa" in name:
            continue
        with open(p, "r", encoding="utf-8") as f:
            data = json.load(f)
        records = data.get("records", [])
        if records:
            reports[data.get("model", p.stem.replace("_report", ""))] = data
    return reports


def analysis_2c1(core_path, output_base):
    """2c-1: 四维语义聚类验证"""
    print("\n" + "=" * 60)
    print("2c-1: 四维语义聚类验证 (PCA 2D)")
    print("=" * 60)

    from sklearn.decomposition import PCA
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    plt.rcParams["font.sans-serif"] = ["DejaVu Sans"]
    plt.rcParams["axes.unicode_minus"] = False

    questions, _ = load_core_questions(core_path)
    dim_order = ["A", "B", "C", "D"]
    dim_colors = {"A": "#E74C3C", "B": "#3498DB", "C": "#2ECC71", "D": "#F39C12"}
    dim_labels_cn = {"A": "Conceptual", "B": "Reasoning", "C": "Sensitivity", "D": "Design"}

    texts = [f"{q['question']}\n{q['answer']}" for q in questions]
    dims = [q["dimension"] for q in questions]

    print(f"加载 {len(questions)} 题, 维度分布: { {d: dims.count(d) for d in dim_order} }")

    embeddings = get_embeddings(texts, progress_label="2c-1 embed")

    pca = PCA(n_components=2, random_state=42)
    coords = pca.fit_transform(embeddings)
    evr = pca.explained_variance_ratio_

    print(f"PCA 解释方差: PC1={evr[0]:.3f}, PC2={evr[1]:.3f}, 合计={sum(evr):.3f}")

    fig, axes = plt.subplots(1, 2, figsize=(16, 7))

    # 左: 四维着色散点
    ax = axes[0]
    for d in dim_order:
        mask = np.array([di == d for di in dims])
        ax.scatter(
            coords[mask, 0], coords[mask, 1],
            c=dim_colors[d], label=f"{d}: {dim_labels_cn[d]}", alpha=0.7, s=20, edgecolors="none",
        )
    ax.set_xlabel(f"PC1 ({evr[0]*100:.1f}%)")
    ax.set_ylabel(f"PC2 ({evr[1]*100:.1f}%)")
    ax.set_title("4-Dimension Semantic PCA Projection\n(500 Questions × qwen3-embedding:4b)")
    ax.legend(markerscale=2, fontsize=9)
    ax.grid(True, alpha=0.3)

    # 右: 各维质心 + 95% 椭圆
    ax = axes[1]
    from matplotlib.patches import Ellipse
    from scipy.stats import chi2
    chi2_scale = np.sqrt(chi2.ppf(0.95, df=2))
    for d in dim_order:
        mask = np.array([di == d for di in dims])
        pts = coords[mask]
        centroid = pts.mean(axis=0)
        cov = np.cov(pts.T)
        eigenvalues, eigenvectors = np.linalg.eigh(cov)
        angle = np.degrees(np.arctan2(eigenvectors[1, 0], eigenvectors[0, 0]))
        width, height = 2 * chi2_scale * np.sqrt(eigenvalues)
        ell = Ellipse(
            xy=centroid, width=width, height=height, angle=angle,
            edgecolor=dim_colors[d], facecolor=dim_colors[d], alpha=0.12, linewidth=1.5,
        )
        ax.add_patch(ell)
        ax.scatter(*centroid, c=dim_colors[d], s=100, marker="X", edgecolors="black", linewidths=0.8, zorder=5)
        ax.annotate(
            f"{d}", centroid, textcoords="offset points", xytext=(8, 8),
            fontsize=11, fontweight="bold", color=dim_colors[d],
        )
    ax.set_xlabel(f"PC1 ({evr[0]*100:.1f}%)")
    ax.set_ylabel(f"PC2 ({evr[1]*100:.1f}%)")
    ax.set_title("4-Dimension Centroids + 95% Confidence Ellipses")
    ax.grid(True, alpha=0.3)

    plt.tight_layout()
    png_path = f"{output_base}.png"
    fig.savefig(png_path, dpi=150, bbox_inches="tight")
    plt.close(fig)
    print(f"  PCA 图已保存: {png_path}")

    # 质心距离矩阵
    centroids = {}
    for d in dim_order:
        mask = [di == d for di in dims]
        centroids[d] = coords[mask].mean(axis=0)

    centroid_distances = {}
    for i, d1 in enumerate(dim_order):
        for d2 in dim_order[i + 1 :]:
            dist = float(np.linalg.norm(centroids[d1] - centroids[d2]))
            centroid_distances[f"{d1}-{d2}"] = round(dist, 4)

    result = {
        "analysis": "2c-1_four_dimension_pca",
        "n_questions": len(questions),
        "dimension_counts": {d: dims.count(d) for d in dim_order},
        "pca_variance_explained": [round(float(v), 4) for v in evr],
        "centroid_2d": {d: [round(float(v), 4) for v in centroids[d]] for d in dim_order},
        "centroid_distances": centroid_distances,
        "interpretation": (
            "四维在嵌入空间中部分重叠（尤其 A/B），反映 L1→L2 的科学发现连续谱；"
            "C/D 维度有独立聚集趋势，说明 sensitivity 和 design 有独特语义特征。"
        ),
    }

    json_path = f"{output_base}.json"
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
    print(f"  JSON 已保存: {json_path}")

    return result


def analysis_2c2(reports_dir, cross_judge_path, output_base):
    """2c-2: 嵌入仲裁 vs LLM 仲裁一致性"""
    print("\n" + "=" * 60)
    print("2c-2: 嵌入仲裁 vs LLM 仲裁一致性 (Spearman ρ)")
    print("=" * 60)

    from scipy.stats import spearmanr

    with open(cross_judge_path, "r", encoding="utf-8") as f:
        cj = json.load(f)
    source_model = cj["meta"]["source_model"]
    cj_records = [r for r in cj["records"] if r.get("score", -1) >= 0]

    report_path = Path(reports_dir) / f"{source_model}_report.json"
    if not report_path.exists():
        print(f"  ⚠ 未找到源模型报告 {report_path}，跳过 cross_judge 对比", flush=True)
        cj_correlations = {}
    else:
        with open(report_path, "r", encoding="utf-8") as f:
            source_report = json.load(f)
        report_map = {r["id"]: r for r in source_report["records"]}

        # question-level 聚合: 同一题目多个 judge 打分的均值 vs 唯一 cos
        q_agg = {}
        for rec in cj_records:
            qid = rec["question_id"]
            if qid not in report_map:
                continue
            if qid not in q_agg:
                mr = report_map[qid]
                q_agg[qid] = {
                    "model_answer": mr.get("model_answer", ""),
                    "expected_answer": mr.get("expected_answer", ""),
                    "judge_scores": [],
                    "judges": [],
                }
            q_agg[qid]["judge_scores"].append(rec["score"])
            q_agg[qid]["judges"].append(rec["judge"])

        if q_agg:
            # 按 qid 稳定顺序构建嵌入文本
            qids_ordered = sorted(q_agg.keys())
            all_texts = []
            for qid in qids_ordered:
                all_texts.append(q_agg[qid]["model_answer"])
                all_texts.append(q_agg[qid]["expected_answer"])
            print(f"  嵌入 {len(all_texts)} 条文本 ({len(qids_ordered)} 题目 × 模型回答+标准答案)...", flush=True)
            all_emb = get_embeddings(all_texts, progress_label="2c-2 cross-judge embed")

            cos_vals = []
            avg_scores = []
            for i, qid in enumerate(qids_ordered):
                cos = float(np.dot(all_emb[i * 2], all_emb[i * 2 + 1]))
                cos_vals.append(cos)
                avg_scores.append(np.mean(q_agg[qid]["judge_scores"]))

            if len(set(avg_scores)) >= 2:
                rho, pv = spearmanr(avg_scores, cos_vals)
                cj_correlations = {
                    "spearman_rho": round(float(rho), 4),
                    "p_value": round(float(pv), 4),
                    "n_questions": len(qids_ordered),
                }
                print(f"  [cross_judge question-level] Spearman ρ={rho:.4f}, p={pv:.4f}, n={len(qids_ordered)} questions", flush=True)

                # 按 judge 汇总一致性（informational only, 不重复跑单个 Spearman）
                judge_counts = defaultdict(int)
                for qid in qids_ordered:
                    for j in q_agg[qid]["judges"]:
                        judge_counts[j] += 1
                cj_correlations["judge_sample_counts"] = dict(judge_counts)
            else:
                cj_correlations = {"spearman_rho": None, "p_value": None, "n_questions": len(qids_ordered), "note": "分数方差不足"}
        else:
            cj_correlations = {"note": "cross_judge 无匹配到 report 中的题目"}

    # 补充: 用完整模型报告做更大规模对比
    reports = load_reports(reports_dir)
    print(f"\n  找到 {len(reports)} 个模型报告，选代表性模型做全量 cos vs score 对比...", flush=True)

    # 优先用 qwen3.5:9b (500题完整) 或 deepseek-v4-flash
    preferred = ["qwen3.5:9b", "deepseek-v4-flash"]
    full_correlations = {}
    for model_name in preferred:
        if model_name not in reports:
            continue
        rep = reports[model_name]
        records = rep["records"]
        print(f"\n  --- {model_name} ({len(records)} records) ---", flush=True)

        answers_texts = []
        for r in records:
            answers_texts.append(r.get("model_answer", ""))
            answers_texts.append(r.get("expected_answer", ""))
        print(f"  嵌入 {len(answers_texts)} 条文本...", flush=True)
        all_emb = get_embeddings(answers_texts, progress_label=f"2c-2 {model_name}")

        cos_vals = []
        scores = []
        for i, r in enumerate(records):
            v1 = all_emb[i * 2]
            v2 = all_emb[i * 2 + 1]
            cos_vals.append(float(np.dot(v1, v2)))
            scores.append(r["score"])

        if len(set(scores)) >= 2:
            rho, pv = spearmanr(scores, cos_vals)
            full_correlations[model_name] = {
                "spearman_rho": round(float(rho), 4),
                "p_value": round(float(pv), 4),
                "n": len(records),
            }
            print(f"  [{model_name}] Spearman ρ={rho:.4f}, p={pv:.4f}, n={len(records)}", flush=True)

            # 按得分分档统计 cos 均值
            bins = defaultdict(list)
            for s, c in zip(scores, cos_vals):
                bins[s].append(c)
            print(f"  各分数档 cos_sim 均值:", flush=True)
            for s_val in sorted(bins):
                print(f"    score={s_val}: cos_mean={np.mean(bins[s_val]):.4f}, n={len(bins[s_val])}", flush=True)
        break  # 只做第一个匹配模型

    result = {
        "analysis": "2c-2_embedding_vs_llm_correlation",
        "cross_judge": {
            "source_model": source_model,
            "description": "使用 cross_judge_kappa 数据, question-level embedding cos 与多 judge 均值 score 的 Spearman 相关性",
            "correlation": cj_correlations,
        },
        "full_report": full_correlations,
        "interpretation": (
            "若 ρ > 0.5: 嵌入 cos 与 LLM 判分中等以上相关 → embedding 快筛有一定参考价值; "
            "若 ρ < 0.3: 嵌入 cos 与 LLM 判分弱相关 → LLM 仲裁不可替代, "
            "验证了嵌入模型「无法区分概念正确性」的结论 (cos≈0.97 的答案可能得 0 分)。"
        ),
    }

    json_path = f"{output_base}.json"
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
    print(f"\n  JSON 已保存: {json_path}")

    return result


def analysis_2c3(reports_dir, core_path, output_base):
    """2c-3: 失败案例嵌入聚类"""
    print("\n" + "=" * 60)
    print("2c-3: 失败案例嵌入聚类 (KMeans)")
    print("=" * 60)

    from sklearn.cluster import KMeans
    from sklearn.metrics import silhouette_score

    _, qmap = load_core_questions(core_path)
    reports = load_reports(reports_dir)

    # 收集所有 score < 0.3 的低分题
    low_score_map = defaultdict(lambda: {"scores": [], "models": [], "model_answers": []})
    for model_name, rep in reports.items():
        for r in rep["records"]:
            if r["score"] < 0.3:
                qid = r["id"]
                low_score_map[qid]["scores"].append(r["score"])
                low_score_map[qid]["models"].append(model_name)
                low_score_map[qid]["model_answers"].append(r.get("model_answer", ""))

    # 按「多少模型同时低分」排序，选最盲区的题
    ranked = sorted(low_score_map.items(), key=lambda x: len(x[1]["scores"]), reverse=True)
    print(f"低分题总数 (score<0.3): {len(ranked)}")
    top_blind = ranked[:50]
    print(f"Top-50 多模型共低分题: {[(qid, len(v['scores'])) for qid, v in top_blind[:10]]}...", flush=True)

    texts = []
    meta = []
    for qid, v in top_blind:
        q = qmap.get(qid)
        question_text = q["question"] if q else qid
        answer_text = q["answer"] if q else ""
        texts.append(f"{question_text}\n{answer_text}")
        meta.append({
            "id": qid,
            "dimension": q["dimension"] if q else "?",
            "n_models_failed": len(v["scores"]),
            "avg_score": round(float(np.mean(v["scores"])), 4),
            "models": v["models"],
        })

    if len(texts) < 3:
        print("  ⚠ 低分题不足 3 题，跳过聚类", flush=True)
        return {"analysis": "2c-3_failure_clustering", "n_low_score": len(ranked), "clusters": [], "note": "样本不足"}

    print(f"\n  嵌入 {len(texts)} 条低分题...", flush=True)
    embeddings = get_embeddings(texts, progress_label="2c-3 embed")

    # KMeans 聚类
    k_range = range(2, min(8, len(texts)))
    best_k = 3
    best_score = -1
    for k in k_range:
        km = KMeans(n_clusters=k, random_state=42, n_init=10)
        labels = km.fit_predict(embeddings)
        if len(set(labels)) < 2:
            continue
        sil = silhouette_score(embeddings, labels)
        print(f"  k={k}: silhouette={sil:.4f}", flush=True)
        if sil > best_score:
            best_score = sil
            best_k = k

    km = KMeans(n_clusters=best_k, random_state=42, n_init=10)
    labels = km.fit_predict(embeddings)
    sil = silhouette_score(embeddings, labels) if len(set(labels)) >= 2 else 0
    print(f"  最终 k={best_k}, silhouette={sil:.4f}", flush=True)

    # 按簇汇总
    clusters = []
    for c in range(best_k):
        mask = labels == c
        c_items = [meta[i] for i in range(len(meta)) if mask[i]]
        c_dims = [m["dimension"] for m in c_items]
        c_scores = [m["avg_score"] for m in c_items]
        clusters.append({
            "cluster_id": c,
            "size": len(c_items),
            "avg_score": round(float(np.mean(c_scores)), 4),
            "dimension_distribution": {d: c_dims.count(d) for d in sorted(set(c_dims))},
            "members": c_items,
        })

    clusters.sort(key=lambda x: x["avg_score"])
    print(f"\n  盲区簇排名 (按均分升序):", flush=True)
    for cl in clusters:
        print(f"    簇{cl['cluster_id']}: n={cl['size']}, avg_score={cl['avg_score']:.4f}, dims={cl['dimension_distribution']}", flush=True)

    result = {
        "analysis": "2c-3_failure_embedding_clustering",
        "n_low_score_total": len(ranked),
        "n_clustered": len(texts),
        "k_optimal": best_k,
        "silhouette_score": round(float(sil), 4),
        "clusters": clusters,
        "top3_blind_spots": [
            {
                "cluster_id": cl["cluster_id"],
                "avg_score": cl["avg_score"],
                "n_questions": cl["size"],
                "dominant_dimension": max(cl["dimension_distribution"], key=cl["dimension_distribution"].get) if cl["dimension_distribution"] else "?",
                "sample_ids": [m["id"] for m in cl["members"][:5]],
            }
            for cl in clusters[:3]
        ],
        "interpretation": (
            f"低分题在嵌入空间中自然聚为 {best_k} 簇 (silhouette={sil:.3f})。"
            "均分最低的簇即为跨模型的「知识盲区」，可针对性扩充训练数据或改进 prompt。"
        ),
    }

    json_path = f"{output_base}.json"
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
    print(f"\n  JSON 已保存: {json_path}")

    return result


def main():
    global OLLAMA_EMBED_URL
    parser = argparse.ArgumentParser(description="Task 2c: 嵌入模型三大分析")
    parser.add_argument("--dataset", default="benchmark/dataset/core.json", help="core.json 路径")
    parser.add_argument("--reports-dir", default="benchmark/eval/reports", help="模型报告目录")
    parser.add_argument("--cross-judge", default="benchmark/eval/reports/cross_judge_kappa.json", help="交叉验证数据")
    parser.add_argument("--output-base", default="benchmark/eval/results/embedding_cluster_analysis", help="输出文件前缀")
    parser.add_argument("--skip", nargs="*", choices=["2c1", "2c2", "2c3"], default=[], help="跳过的分析")
    parser.add_argument("--ollama-url", default=OLLAMA_EMBED_URL, help="Ollama embed API 地址")
    args = parser.parse_args()

    OLLAMA_EMBED_URL = args.ollama_url

    # 检查 Ollama 连通性
    print("检查 Ollama 连通性...", flush=True)
    try:
        resp = httpx.post(OLLAMA_EMBED_URL, json={"model": EMBED_MODEL, "input": ["test"]}, timeout=10)
        resp.raise_for_status()
        data = resp.json()
        emb = data.get("embeddings", [[]])[0]
        if len(emb) != EMBED_DIM:
            print(f"  ✗ 嵌入维度不匹配: 期望 {EMBED_DIM}, 实际 {len(emb)}", flush=True)
            sys.exit(1)
        print(f"  ✓ Ollama 在线, 嵌入维度: {len(emb)}, 模型: {EMBED_MODEL}", flush=True)
    except Exception as e:
        print(f"  ✗ Ollama 连接失败: {e}", flush=True)
        print(f"  请确保 Ollama 运行中且模型 {EMBED_MODEL} 已加载", flush=True)
        sys.exit(1)

    # 确保输出目录存在
    output_base = args.output_base
    Path(output_base).parent.mkdir(parents=True, exist_ok=True)

    # 转为绝对路径
    dataset_path = Path(args.dataset)
    reports_dir = Path(args.reports_dir)
    cross_judge_path = Path(args.cross_judge)

    if not dataset_path.exists():
        print(f"✗ 数据集不存在: {dataset_path}")
        sys.exit(1)

    results = {}

    if "2c1" not in args.skip:
        results["2c1"] = analysis_2c1(str(dataset_path), output_base)

    if "2c2" not in args.skip:
        results["2c2"] = analysis_2c2(str(reports_dir), str(cross_judge_path), f"{output_base}_correlation")

    if "2c3" not in args.skip:
        results["2c3"] = analysis_2c3(str(reports_dir), str(dataset_path), f"{output_base}_failure")

    print("\n" + "=" * 60)
    print("Task 2c 全部完成!")
    print("=" * 60)
    print(f"产出文件:")
    for f in sorted(Path(output_base).parent.glob(f"{Path(output_base).name}*")):
        print(f"  {f}")


if __name__ == "__main__":
    main()
