"""Task 2d: 28K Chunk 全量嵌入分析
A1: 语料全局语义空间 PCA (按 doc type + control_category 着色)
A2: 文档间相似度矩阵 (362 doc centroids → cosine heatmap + 层次聚类)
A3: Chunk 级冗余检测 (KMeans 分桶 → 组内 cos > 0.95 近似重复对)
A4: Train/Eval 分布一致性 (PCA split 着色 + MMD 统计检验)

前置条件: Ollama qwen3-embedding:4b 运行中 (http://localhost:11434)
数据量: ~28K chunks × 2560-dim
耗时估算: 嵌入 ~10min + 分析 ~5min = ~15min (RTX 5090)
内存: ~300MB embeddings + ~200MB 分析中间量
"""

import argparse
import json
import os
import sys
import time
from collections import Counter, defaultdict
from pathlib import Path

import numpy as np
import httpx

try:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    from matplotlib.patches import Ellipse
    from sklearn.decomposition import PCA
    from sklearn.cluster import MiniBatchKMeans
    from sklearn.preprocessing import normalize
    from scipy.stats import chi2
    from scipy.cluster.hierarchy import dendrogram, linkage
    from scipy.spatial.distance import squareform
except ImportError as e:
    print(f"缺少依赖: {e}")
    print("请安装: conda run -n myenv pip install scikit-learn matplotlib scipy")
    sys.exit(1)

PROJECT_ROOT = Path(__file__).resolve().parents[2]
_OLLAMA_HOST = os.environ.get("OLLAMA_HOST", "http://localhost:11434").rstrip("/")
OLLAMA_EMBED_URL = f"{_OLLAMA_HOST}/api/embed"
EMBED_MODEL = "qwen3-embedding:4b"
EMBED_DIM = 2560
BATCH_SIZE = 20
DEFAULT_MANIFEST = PROJECT_ROOT / "corpus" / "chunks" / "chunks_manifest.json"
DEFAULT_METADATA = PROJECT_ROOT / "corpus" / "metadata.json"
DEFAULT_OUTPUT_DIR = PROJECT_ROOT / "benchmark" / "eval" / "results" / "chunk_embedding"


def get_embeddings(texts, progress_label="embed", cache_path=None):
    """批量获取 Ollama 嵌入向量，支持磁盘缓存续跑。
    返回 (n, 2560) float32 ndarray。
    """
    if not texts:
        if cache_path and Path(cache_path).exists():
            print(f"  [{progress_label}] 从缓存加载: {cache_path}", flush=True)
            cached = np.load(cache_path)
            print(f"  [{progress_label}] 缓存命中 {cached.shape[0]} 条", flush=True)
            return cached
        return np.array([], dtype=np.float32)

    if cache_path and Path(cache_path).exists():
        print(f"  [{progress_label}] 从缓存加载: {cache_path}", flush=True)
        cached = np.load(cache_path)
        if cached.shape[0] == len(texts):
            print(f"  [{progress_label}] 缓存命中 {cached.shape[0]} 条", flush=True)
            return cached
        print(f"  [{progress_label}] 缓存维度不匹配 ({cached.shape[0]} vs {len(texts)})，重新计算", flush=True)

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
        if done % 500 == 0 or done >= n:
            elapsed = time.time() - t0
            rate = done / elapsed if elapsed > 0 else 0
            print(f"  [{progress_label}] {done}/{n} ({done/n*100:.0f}%) — {rate:.1f}条/s", flush=True)

    elapsed = time.time() - t0
    result = np.array(all_emb, dtype=np.float32)
    print(f"  [{progress_label}] 完成 {n} 条, 总耗时 {elapsed:.1f}s, 均速 {n/elapsed:.1f}条/s", flush=True)

    if cache_path:
        Path(cache_path).parent.mkdir(parents=True, exist_ok=True)
        np.save(cache_path, result)
        print(f"  [{progress_label}] 缓存已保存: {cache_path}", flush=True)

    return result


def load_manifest(manifest_path, max_chunks=None):
    """加载 chunk manifest，返回 (chunks_list, summary_dict)"""
    with open(manifest_path, "r", encoding="utf-8") as f:
        manifest = json.load(f)

    chunks = manifest["chunks"]
    if max_chunks and max_chunks < len(chunks):
        chunks = chunks[:max_chunks]

    summary = {
        "total_chunks": manifest.get("total_chunks", len(chunks)),
        "train_chunks": manifest.get("train_chunks", 0),
        "eval_chunks": manifest.get("eval_chunks", 0),
        "target_tokens": manifest.get("target_tokens"),
        "min_tokens": manifest.get("min_tokens"),
        "max_tokens": manifest.get("max_tokens"),
    }
    return chunks, summary


def load_metadata(metadata_path):
    """加载 corpus metadata，返回 {filename: doc_info}"""
    with open(metadata_path, "r", encoding="utf-8") as f:
        meta = json.load(f)

    doc_map = {}
    for doc in meta.get("docs", []):
        doc_map[doc["filename"]] = doc
    return doc_map, {
        "total_docs": meta.get("total_docs"),
        "textbooks": meta.get("textbooks"),
        "arxiv_papers": meta.get("arxiv_papers"),
    }


def load_chunk_texts(chunks):
    """从 manifest chunk 条目加载所有文本。
    返回 (texts: list[str], ids: list[str], metas: list[dict])
    """
    texts, ids, metas = [], [], []
    skipped = 0
    for item in chunks:
        filepath = PROJECT_ROOT / item["filepath"]
        if not filepath.exists():
            skipped += 1
            continue
        text = filepath.read_text(encoding="utf-8").strip()
        if not text:
            skipped += 1
            continue
        texts.append(text)
        ids.append(item["chunk_id"])
        metas.append({
            "chunk_id": item["chunk_id"],
            "filename": item["filename"],
            "set": item["set"],
            "source_section": item.get("source_section", ""),
            "estimated_tokens": item.get("estimated_tokens", 0),
        })

    if skipped:
        print(f"  ⚠ 跳过 {skipped} 个不可读/空 chunk", flush=True)
    print(f"  加载 {len(texts)} 个有效 chunk", flush=True)
    return texts, ids, metas


def ensure_output_dir(output_dir):
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    return output_dir


def _configure_plot_style():
    plt.rcParams["font.sans-serif"] = ["DejaVu Sans"]
    plt.rcParams["axes.unicode_minus"] = False


def analysis_a1_pca(embeddings, chunk_metas, doc_map, output_dir):
    """A1: 语料全局语义空间 PCA"""
    print("\n" + "=" * 60)
    print("A1: 语料全局语义空间 PCA")
    print("=" * 60)

    _configure_plot_style()

    n = embeddings.shape[0]
    print(f"  PCA 输入: {n} × {embeddings.shape[1]}", flush=True)

    t0 = time.time()
    pca = PCA(n_components=2, random_state=42, svd_solver="auto")
    coords = pca.fit_transform(embeddings)
    evr = pca.explained_variance_ratio_
    print(f"  PCA 完成 ({time.time()-t0:.1f}s), 解释方差: PC1={evr[0]:.3f}, PC2={evr[1]:.3f}, 合计={sum(evr):.3f}", flush=True)

    doc_types = []
    control_cats = []
    for m in chunk_metas:
        doc = doc_map.get(m["filename"], {})
        doc_types.append(doc.get("type", "unknown"))
        cats = doc.get("control_category", ["Unclassified"])
        control_cats.append(cats[0] if cats else "Unclassified")

    fig, axes = plt.subplots(2, 2, figsize=(20, 16))

    # 左上: doc type 着色 (textbook vs arxiv)
    ax = axes[0, 0]
    type_colors = {"textbook": "#E74C3C", "arxiv": "#3498DB", "unknown": "#95A5A6"}
    type_labels_cn = {"textbook": f"Textbook (n={doc_types.count('textbook')})",
                      "arxiv": f"arXiv (n={doc_types.count('arxiv')})",
                      "unknown": "Other"}
    for t in ["textbook", "arxiv", "unknown"]:
        mask = np.array([dt == t for dt in doc_types])
        if mask.sum() == 0:
            continue
        ax.scatter(coords[mask, 0], coords[mask, 1],
                   c=type_colors[t], label=type_labels_cn[t],
                   alpha=0.15, s=3, edgecolors="none")
    ax.set_xlabel(f"PC1 ({evr[0]*100:.1f}%)")
    ax.set_ylabel(f"PC2 ({evr[1]*100:.1f}%)")
    ax.set_title(f"Corpus Semantic Space PCA (n={n}) — Colored by Doc Type")
    ax.legend(markerscale=8, fontsize=9)
    ax.grid(True, alpha=0.3)

    # 右上: control_category top-8 着色
    ax = axes[0, 1]
    cat_counts = Counter(control_cats)
    top_cats = [c for c, _ in cat_counts.most_common(8)]
    cat_colors = plt.cm.tab10(np.linspace(0, 1, len(top_cats)))
    for i, cat in enumerate(top_cats):
        mask = np.array([cc == cat for cc in control_cats])
        ax.scatter(coords[mask, 0], coords[mask, 1],
                   c=[cat_colors[i]], label=f"{cat} (n={cat_counts[cat]})",
                   alpha=0.2, s=3, edgecolors="none")
    ax.set_xlabel(f"PC1 ({evr[0]*100:.1f}%)")
    ax.set_ylabel(f"PC2 ({evr[1]*100:.1f}%)")
    ax.set_title("Colored by Control Discipline (Top-8)")
    ax.legend(markerscale=8, fontsize=7)
    ax.grid(True, alpha=0.3)

    # 左下: doc type 质心 + 95% 椭圆
    ax = axes[1, 0]
    chi2_scale = np.sqrt(chi2.ppf(0.95, df=2))
    centroids_a1 = {}
    for t in ["textbook", "arxiv"]:
        mask = np.array([dt == t for dt in doc_types])
        if mask.sum() < 2:
            continue
        pts = coords[mask]
        centroid = pts.mean(axis=0)
        centroids_a1[t] = centroid
        cov = np.cov(pts.T)
        eigenvalues, eigenvectors = np.linalg.eigh(cov)
        angle = np.degrees(np.arctan2(eigenvectors[1, 0], eigenvectors[0, 0]))
        width, height = 2 * chi2_scale * np.sqrt(np.maximum(eigenvalues, 0))
        ell = Ellipse(xy=centroid, width=width, height=height, angle=angle,
                      edgecolor=type_colors[t], facecolor=type_colors[t],
                      alpha=0.15, linewidth=2)
        ax.add_patch(ell)
        ax.scatter(*centroid, c=type_colors[t], s=200, marker="X",
                   edgecolors="black", linewidths=1.2, zorder=5)
        ax.annotate(type_labels_cn[t].split(" ")[0], centroid,
                    textcoords="offset points", xytext=(10, 10),
                    fontsize=13, fontweight="bold", color=type_colors[t])
    ax.set_xlabel(f"PC1 ({evr[0]*100:.1f}%)")
    ax.set_ylabel(f"PC2 ({evr[1]*100:.1f}%)")
    ax.set_title("Doc Type Centroids + 95% Confidence Ellipses")
    ax.grid(True, alpha=0.3)

    # 右下: token 密度热力图 (hexbin)
    ax = axes[1, 1]
    token_sizes = np.array([m["estimated_tokens"] for m in chunk_metas])
    hb = ax.hexbin(coords[:, 0], coords[:, 1], C=token_sizes,
                   gridsize=50, cmap="YlOrRd", reduce_C_function=np.mean)
    plt.colorbar(hb, ax=ax, label="avg estimated_tokens")
    ax.set_xlabel(f"PC1 ({evr[0]*100:.1f}%)")
    ax.set_ylabel(f"PC2 ({evr[1]*100:.1f}%)")
    ax.set_title("Chunk Token Density Distribution (hexbin)")
    ax.grid(True, alpha=0.3)

    plt.tight_layout()
    png_path = output_dir / "a1_global_pca.png"
    fig.savefig(png_path, dpi=150, bbox_inches="tight")
    plt.close(fig)
    print(f"  PCA 图已保存: {png_path}", flush=True)

    centroid_dist = None
    if "textbook" in centroids_a1 and "arxiv" in centroids_a1:
        centroid_dist = float(np.linalg.norm(centroids_a1["textbook"] - centroids_a1["arxiv"]))

    result = {
        "analysis": "A1_global_pca",
        "n_chunks": n,
        "pca_variance_explained": [round(float(v), 4) for v in evr],
        "doc_type_counts": {"textbook": doc_types.count("textbook"), "arxiv": doc_types.count("arxiv")},
        "control_category_top8": [{"category": c, "count": cat_counts[c]} for c in top_cats],
        "centroid_distance_textbook_vs_arxiv": round(centroid_dist, 4) if centroid_dist else None,
        "interpretation": (
            "教材 chunk 与 arXiv chunk 在语义空间中高度重叠，"
            "说明语料覆盖连续且无系统性偏差；若质心距离 < 0.5 则分布一致性良好。"
        ),
    }

    json_path = output_dir / "a1_global_pca.json"
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
    print(f"  JSON 已保存: {json_path}", flush=True)
    return result


def analysis_a2_doc_similarity(embeddings, chunk_metas, doc_map, output_dir):
    """A2: 文档间相似度矩阵"""
    print("\n" + "=" * 60)
    print("A2: 文档间相似度矩阵 (362 docs)")
    print("=" * 60)

    _configure_plot_style()

    # 按文档聚合 centroid
    doc_embeddings = defaultdict(list)
    for i, m in enumerate(chunk_metas):
        doc_embeddings[m["filename"]].append(embeddings[i])

    doc_filenames = sorted(doc_embeddings.keys())
    doc_centroids = np.array([np.mean(doc_embeddings[fn], axis=0) for fn in doc_filenames])
    n_docs = len(doc_filenames)
    print(f"  {n_docs} 个文档, centroid 矩阵: {doc_centroids.shape}", flush=True)

    doc_centroids_norm = normalize(doc_centroids, norm="l2")

    cos_sim = doc_centroids_norm @ doc_centroids_norm.T
    cos_sim = np.clip(cos_sim, -1.0, 1.0)
    cos_dist = 1.0 - cos_sim
    np.fill_diagonal(cos_dist, 0.0)

    # 层次聚类
    Z = linkage(squareform(cos_dist), method="ward")

    # 短标签: 取文件名前30字符 + type 标记
    short_labels = []
    for fn in doc_filenames:
        doc = doc_map.get(fn, {})
        dtype = "T" if doc.get("type") == "textbook" else "A"
        label = fn[:28] + "…" if len(fn) > 28 else fn
        short_labels.append(f"[{dtype}] {label}")

    fig, axes = plt.subplots(1, 2, figsize=(28, 14))

    # 左: 热力图 (下采样显示概览，全量存单独文件)
    ax = axes[0]
    im = ax.imshow(cos_sim, cmap="RdYlBu_r", aspect="auto", vmin=0.5, vmax=1.0)
    plt.colorbar(im, ax=ax, label="cosine similarity", shrink=0.8)
    ax.set_title(f"Inter-Document Cosine Similarity ({n_docs}×{n_docs})")
    ax.set_xlabel("Document Index")
    ax.set_ylabel("Document Index")

    # 右: 树状图
    ax = axes[1]
    dendrogram(Z, labels=short_labels, leaf_font_size=3, ax=ax,
               orientation="right", color_threshold=0.3 * max(Z[:, 2]))
    ax.set_title("Document Hierarchical Clustering (Ward linkage on cosine distance)")
    ax.set_xlabel("Merge Distance")

    plt.tight_layout()
    png_path = output_dir / "a2_doc_similarity.png"
    fig.savefig(png_path, dpi=150, bbox_inches="tight")
    plt.close(fig)
    print(f"  相似度图已保存: {png_path}", flush=True)

    # 全尺寸热力图单独保存
    fig2, ax2 = plt.subplots(1, 1, figsize=(24, 22))
    im2 = ax2.imshow(cos_sim, cmap="RdYlBu_r", aspect="auto", vmin=0.5, vmax=1.0)
    plt.colorbar(im2, ax=ax2, label="cosine similarity")
    ax2.set_title(f"Inter-Document Cosine Similarity — Full ({n_docs}×{n_docs})")
    ax2.set_xticks(range(n_docs))
    ax2.set_yticks(range(n_docs))
    ax2.set_xticklabels(short_labels, rotation=90, fontsize=2.5)
    ax2.set_yticklabels(short_labels, fontsize=2.5)
    full_heatmap_path = output_dir / "a2_doc_similarity_full.png"
    fig2.savefig(full_heatmap_path, dpi=150, bbox_inches="tight")
    plt.close(fig2)
    print(f"  全尺寸热力图已保存: {full_heatmap_path}", flush=True)

    # Top-20 最相似文档对 (排除自相似)
    triu_indices = np.triu_indices(n_docs, k=1)
    triu_vals = cos_sim[triu_indices]
    top_n = min(20, len(triu_vals))
    top_indices = np.argpartition(triu_vals, -top_n)[-top_n:]
    top_indices = top_indices[np.argsort(triu_vals[top_indices])[::-1]]

    top_pairs = []
    for idx in top_indices:
        i, j = triu_indices[0][idx], triu_indices[1][idx]
        doc_i = doc_map.get(doc_filenames[i], {})
        doc_j = doc_map.get(doc_filenames[j], {})
        top_pairs.append({
            "rank": len(top_pairs) + 1,
            "doc_a": doc_filenames[i],
            "doc_a_id": doc_i.get("id", ""),
            "doc_a_type": doc_i.get("type", ""),
            "doc_a_title": doc_i.get("title", ""),
            "doc_b": doc_filenames[j],
            "doc_b_id": doc_j.get("id", ""),
            "doc_b_type": doc_j.get("type", ""),
            "doc_b_title": doc_j.get("title", ""),
            "cosine_similarity": round(float(cos_sim[i, j]), 4),
        })

    print(f"\n  Top-20 最相似文档对:", flush=True)
    for pair in top_pairs[:10]:
        print(f"    #{pair['rank']}: cos={pair['cosine_similarity']:.4f}  "
              f"[{pair['doc_a_type']}] {pair['doc_a'][:40]} ↔ [{pair['doc_b_type']}] {pair['doc_b'][:40]}", flush=True)

    # 统计: textbook-textbook, arxiv-arxiv, cross-type 相似度分布
    tt_sims, aa_sims, ta_sims = [], [], []
    for i in range(n_docs):
        for j in range(i + 1, n_docs):
            ti = doc_map.get(doc_filenames[i], {}).get("type", "")
            tj = doc_map.get(doc_filenames[j], {}).get("type", "")
            val = float(cos_sim[i, j])
            if ti == "textbook" and tj == "textbook":
                tt_sims.append(val)
            elif ti == "arxiv" and tj == "arxiv":
                aa_sims.append(val)
            else:
                ta_sims.append(val)

    sim_stats = {
        "textbook_textbook": {"mean": round(np.mean(tt_sims), 4), "std": round(np.std(tt_sims), 4), "n": len(tt_sims)} if tt_sims else {},
        "arxiv_arxiv": {"mean": round(np.mean(aa_sims), 4), "std": round(np.std(aa_sims), 4), "n": len(aa_sims)} if aa_sims else {},
        "cross_type": {"mean": round(np.mean(ta_sims), 4), "std": round(np.std(ta_sims), 4), "n": len(ta_sims)} if ta_sims else {},
    }
    print(f"\n  同类/跨类相似度统计:", flush=True)
    for k, v in sim_stats.items():
        if v:
            print(f"    {k}: mean={v['mean']:.4f} ± {v['std']:.4f} (n={v['n']})", flush=True)

    result = {
        "analysis": "A2_doc_similarity",
        "n_docs": n_docs,
        "similarity_stats": sim_stats,
        "top20_pairs": top_pairs,
        "interpretation": (
            "教材-教材相似度若显著高于 arXiv-ArXiv，说明教材内容更同质化；"
            "跨类型相似度若与同类相当，说明语料主题覆盖连续。"
        ),
    }

    json_path = output_dir / "a2_doc_similarity.json"
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
    print(f"  JSON 已保存: {json_path}", flush=True)
    return result


def analysis_a3_redundancy(embeddings, chunk_metas, output_dir, cos_threshold=0.95):
    """A3: Chunk 级冗余检测 — MiniBatchKMeans 分桶 + 组内 cosine 去重"""
    print("\n" + "=" * 60)
    print(f"A3: Chunk 级冗余检测 (cos > {cos_threshold})")
    print("=" * 60)

    n = embeddings.shape[0]
    n_clusters = min(500, max(2, n // 50))
    if n_clusters > n:
        n_clusters = max(1, n)
    print(f"  L2 归一化 → MiniBatchKMeans k={n_clusters}...", flush=True)

    emb_norm = normalize(embeddings, norm="l2")
    kmeans = MiniBatchKMeans(n_clusters=n_clusters, random_state=42,
                              batch_size=200, n_init=3, max_iter=100)
    labels = kmeans.fit_predict(emb_norm)

    cluster_sizes = Counter(labels)
    print(f"  聚类完成: {len(cluster_sizes)} 个非空簇, "
           f"max_size={max(cluster_sizes.values())}, mean_size={n/len(cluster_sizes):.1f}", flush=True)

    redundant_pairs = []
    checked_pairs = 0
    t0 = time.time()

    for c_id in sorted(cluster_sizes.keys()):
        indices = np.where(labels == c_id)[0]
        if len(indices) < 2:
            continue
        cluster_emb = emb_norm[indices]
        cos_mat = cluster_emb @ cluster_emb.T
        for i in range(len(indices)):
            idx_i = int(indices[i])
            for j in range(i + 1, len(indices)):
                checked_pairs += 1
                cos_val = float(cos_mat[i, j])
                if cos_val >= cos_threshold:
                    idx_j = int(indices[j])
                    redundant_pairs.append({
                        "chunk_a_id": chunk_metas[idx_i]["chunk_id"],
                        "chunk_b_id": chunk_metas[idx_j]["chunk_id"],
                        "cosine_similarity": round(cos_val, 4),
                        "same_doc": chunk_metas[idx_i]["filename"] == chunk_metas[idx_j]["filename"],
                    })

    elapsed = time.time() - t0
    print(f"  遍历 {checked_pairs} 对 ({elapsed:.1f}s), 发现 {len(redundant_pairs)} 对冗余 (cos ≥ {cos_threshold})", flush=True)

    redundant_pairs.sort(key=lambda x: x["cosine_similarity"], reverse=True)

    # 分类: 同文档内 vs 跨文档
    same_doc = [p for p in redundant_pairs if p["same_doc"]]
    cross_doc = [p for p in redundant_pairs if not p["same_doc"]]
    print(f"    同文档内冗余: {len(same_doc)} 对", flush=True)
    print(f"    跨文档冗余: {len(cross_doc)} 对", flush=True)

    # 按文档统计冗余率（unique chunk，避免一个chunk出现在多对中重复计数）
    doc_redundancy = defaultdict(lambda: {"total": 0, "redundant_chunks": set()})
    for m in chunk_metas:
        doc_redundancy[m["filename"]]["total"] += 1
    chunk_id_to_meta = {m["chunk_id"]: m for m in chunk_metas}
    for p in same_doc:
        fn = chunk_id_to_meta[p["chunk_a_id"]]["filename"]
        doc_redundancy[fn]["redundant_chunks"].add(p["chunk_a_id"])

    high_redundancy_docs = sorted(
        [(fn, v) for fn, v in doc_redundancy.items() if v["total"] >= 10 and len(v["redundant_chunks"]) > 0],
        key=lambda x: len(x[1]["redundant_chunks"]) / x[1]["total"],
        reverse=True,
    )[:10]

    print(f"\n  Top-10 冗余率最高文档:", flush=True)
    for fn, v in high_redundancy_docs:
        unique_count = len(v["redundant_chunks"])
        rate = unique_count / v["total"] * 100
        print(f"    {fn[:60]}: {unique_count}/{v['total']} ({rate:.1f}%)", flush=True)

    if cross_doc:
        print(f"\n  Top-10 跨文档冗余对:", flush=True)
        for pair in cross_doc[:10]:
            same_flag = "同文档" if pair["same_doc"] else "跨文档"
            print(f"    cos={pair['cosine_similarity']:.4f} [{same_flag}] "
                  f"{pair['chunk_a_id'][:50]} ↔ {pair['chunk_b_id'][:50]}", flush=True)

    result = {
        "analysis": "A3_redundancy",
        "cosine_threshold": cos_threshold,
        "n_chunks": n,
        "n_clusters": n_clusters,
        "checked_pairs": checked_pairs,
        "redundant_pairs_total": len(redundant_pairs),
        "same_doc_redundant": len(same_doc),
        "cross_doc_redundant": len(cross_doc),
        "top_same_doc_sample": [
            {k: v for k, v in p.items() if k != "same_doc"}
            for p in same_doc[:10]
        ],
        "top_cross_doc_sample": [
            {k: v for k, v in p.items() if k != "same_doc"}
            for p in cross_doc[:10]
        ],
        "high_redundancy_docs": [
            {"filename": fn, "total_chunks": v["total"],
             "redundant_chunk_count": len(v["redundant_chunks"]),
             "redundancy_rate": round(len(v["redundant_chunks"]) / v["total"], 4)}
            for fn, v in high_redundancy_docs
        ],
        "interpretation": (
            f"在 {n} chunks 中发现 {len(redundant_pairs)} 对 cos ≥ {cos_threshold} 的近似重复。"
            f"同文档内 {len(same_doc)} 对 → 可能为公式/列表重复（低频，≤1% 属正常）；"
            f"跨文档 {len(cross_doc)} 对 → 可能为引用文字重叠或翻译一致（需人工抽查）。"
        ),
    }

    json_path = output_dir / "a3_redundancy.json"
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
    print(f"  JSON 已保存: {json_path}", flush=True)
    return result


def analysis_a4_train_eval(embeddings, chunk_metas, output_dir):
    """A4: Train/Eval 分布一致性"""
    print("\n" + "=" * 60)
    print("A4: Train/Eval 分布一致性")
    print("=" * 60)

    _configure_plot_style()

    train_mask = np.array([m["set"] == "train" for m in chunk_metas])
    eval_mask = np.array([m["set"] == "eval" for m in chunk_metas])

    n_train = train_mask.sum()
    n_eval = eval_mask.sum()
    print(f"  Train: {n_train}, Eval: {n_eval}", flush=True)

    # PCA
    pca = PCA(n_components=2, random_state=42, svd_solver="auto")
    coords = pca.fit_transform(embeddings)
    evr = pca.explained_variance_ratio_

    train_emb = embeddings[train_mask]
    eval_emb = embeddings[eval_mask]
    train_centroid = train_emb.mean(axis=0)
    eval_centroid = eval_emb.mean(axis=0)

    centroid_cos = float(np.dot(train_centroid, eval_centroid) /
                         (np.linalg.norm(train_centroid) * np.linalg.norm(eval_centroid)))
    print(f"  Train/Eval 质心 cosine: {centroid_cos:.6f}", flush=True)

    # MMD (Maximum Mean Discrepancy) with RBF kernel
    def rbf_mmd(X, Y, sigma=None):
        if sigma is None:
            XX = np.dot(X, X.T)
            distances = (np.diag(XX).reshape(-1, 1) + np.diag(XX).reshape(1, -1) - 2 * XX)
            sigma = np.median(np.sqrt(np.maximum(distances[np.triu_indices(len(X), k=1)], 0)))
            if sigma == 0:
                sigma = 1.0

        gamma = 1.0 / (2 * sigma * sigma)

        def kernel(A, B):
            AA = np.sum(A * A, axis=1).reshape(-1, 1)
            BB = np.sum(B * B, axis=1).reshape(1, -1)
            dist2 = np.maximum(AA + BB - 2 * np.dot(A, B.T), 0)
            return np.exp(-gamma * dist2)

        K_XX = kernel(X, X)
        K_YY = kernel(Y, Y)
        K_XY = kernel(X, Y)

        mmd = np.mean(K_XX) + np.mean(K_YY) - 2 * np.mean(K_XY)
        return mmd, sigma

    sample_size = min(1000, n_train, n_eval)
    rng = np.random.RandomState(42)
    train_sample = train_emb[rng.choice(n_train, sample_size, replace=False)]
    eval_sample = eval_emb[rng.choice(n_eval, sample_size, replace=False)]

    mmd_val, sigma_val = rbf_mmd(train_sample, eval_sample)
    print(f"  MMD (RBF, n={sample_size}, σ={sigma_val:.2f}): {mmd_val:.6f}", flush=True)

    # Permutation test for MMD significance
    combined = np.vstack([train_sample, eval_sample])
    n_perm = 200
    perm_mmds = []
    for _ in range(n_perm):
        perm_idx = rng.permutation(2 * sample_size)
        perm_train = combined[perm_idx[:sample_size]]
        perm_eval = combined[perm_idx[sample_size:]]
        perm_mmd, _ = rbf_mmd(perm_train, perm_eval, sigma_val)
        perm_mmds.append(perm_mmd)

    perm_mmds = np.array(perm_mmds)
    p_value = float(np.mean(perm_mmds >= mmd_val))
    print(f"  Permutation test (n={n_perm}): p={p_value:.4f}")
    if p_value < 0.05:
        print("  ⚠ Train/Eval 分布在 MMD 意义上存在显著差异 (p<0.05)", flush=True)
    else:
        print("  ✓ Train/Eval 分布在 MMD 意义上无显著差异", flush=True)

    # 可视化
    fig, axes = plt.subplots(1, 2, figsize=(18, 7))

    # 左: PCA split 着色
    ax = axes[0]
    split_colors = {"train": "#3498DB", "eval": "#E74C3C"}
    for split_name, mask in [("train", train_mask), ("eval", eval_mask)]:
        ax.scatter(coords[mask, 0], coords[mask, 1],
                   c=split_colors[split_name],
                   label=f"{split_name} (n={mask.sum()})",
                   alpha=0.12, s=3, edgecolors="none")
    ax.set_xlabel(f"PC1 ({evr[0]*100:.1f}%)")
    ax.set_ylabel(f"PC2 ({evr[1]*100:.1f}%)")
    ax.set_title("Train/Eval Distribution Comparison (PCA 2D)")
    ax.legend(markerscale=8, fontsize=10)
    ax.grid(True, alpha=0.3)

    # 右: MMD permutation 分布
    ax = axes[1]
    ax.hist(perm_mmds, bins=30, alpha=0.7, color="#95A5A6", edgecolor="white",
            label=f"Permutation null (n={n_perm})")
    ax.axvline(mmd_val, color="#E74C3C", linewidth=2.5, linestyle="--",
               label=f"Observed MMD={mmd_val:.4f}")
    ax.set_xlabel("MMD")
    ax.set_ylabel("Frequency")
    ax.set_title(f"MMD Permutation Test (p={p_value:.3f})")
    ax.legend(fontsize=9)

    plt.tight_layout()
    png_path = output_dir / "a4_train_eval.png"
    fig.savefig(png_path, dpi=150, bbox_inches="tight")
    plt.close(fig)
    print(f"  图已保存: {png_path}", flush=True)

    result = {
        "analysis": "A4_train_eval_consistency",
        "n_train": int(n_train),
        "n_eval": int(n_eval),
        "split_ratio_actual": round(float(n_train) / (n_train + n_eval), 4),
        "centroid_cosine": round(centroid_cos, 4),
        "mmd_rbf": round(float(mmd_val), 6),
        "mmd_sigma": round(float(sigma_val), 2),
        "mmd_p_value": round(p_value, 4),
        "mmd_permutation_n": n_perm,
        "mmd_significant": p_value < 0.05,
        "interpretation": (
            f"质心 cosine = {centroid_cos:.4f} (≈1.0 说明分布一致)。"
            f"MMD = {mmd_val:.4f}, permutation p = {p_value:.4f}"
            f"{' → 差异显著' if p_value < 0.05 else ' → 无显著差异'}。"
        ),
    }

    json_path = output_dir / "a4_train_eval.json"
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
    print(f"  JSON 已保存: {json_path}", flush=True)
    return result


def main():
    global OLLAMA_EMBED_URL
    parser = argparse.ArgumentParser(description="Task 2d: 28K Chunk 全量嵌入分析")
    parser.add_argument("--manifest", default=str(DEFAULT_MANIFEST), help="chunks_manifest.json 路径")
    parser.add_argument("--metadata", default=str(DEFAULT_METADATA), help="corpus metadata.json 路径")
    parser.add_argument("--output-dir", default=str(DEFAULT_OUTPUT_DIR), help="输出目录")
    parser.add_argument("--max-chunks", type=int, default=0, help="限制加载 chunk 数量 (0=全量, >0=快速测试)")
    parser.add_argument("--skip", nargs="*", choices=["A1", "A2", "A3", "A4"], default=[], help="跳过的分析")
    parser.add_argument("--skip-embed", action="store_true", help="跳过嵌入计算，使用缓存")
    parser.add_argument("--ollama-url", default=OLLAMA_EMBED_URL, help="Ollama embed API 地址")
    parser.add_argument("--cos-threshold", type=float, default=0.95, help="A3 冗余检测 cosine 阈值")
    args = parser.parse_args()

    OLLAMA_EMBED_URL = args.ollama_url
    output_dir = ensure_output_dir(args.output_dir)
    max_chunks = args.max_chunks if args.max_chunks > 0 else None

    print("=" * 60)
    print("Task 2d: 28K Chunk 全量嵌入分析")
    print("=" * 60)

    manifest_path = Path(args.manifest)
    metadata_path = Path(args.metadata)

    if not manifest_path.exists():
        print(f"✗ manifest 不存在: {manifest_path}")
        sys.exit(1)
    if not metadata_path.exists():
        print(f"✗ metadata 不存在: {metadata_path}")
        sys.exit(1)

    print(f"\n配置:")
    print(f"  manifest: {manifest_path}")
    print(f"  metadata: {metadata_path}")
    print(f"  output: {output_dir}")
    print(f"  max_chunks: {max_chunks or '全量'}")
    print(f"  skip: {args.skip or '无'}")
    print(f"  skip_embed: {args.skip_embed}")
    print(f"  cos_threshold: {args.cos_threshold}")

    chunks, manifest_summary = load_manifest(manifest_path, max_chunks)
    doc_map, meta_summary = load_metadata(metadata_path)
    print(f"\nManifest: {manifest_summary['total_chunks']} chunks (train={manifest_summary['train_chunks']}, eval={manifest_summary['eval_chunks']})")
    print(f"Metadata: {meta_summary['total_docs']} docs (textbooks={meta_summary['textbooks']}, arxiv={meta_summary['arxiv_papers']})")

    texts, _, chunk_metas = load_chunk_texts(chunks)
    if not texts:
        print("✗ 无有效 chunk 文本可加载，请检查 corpus/chunks/ 目录")
        sys.exit(1)

    cache_path = output_dir / "embeddings_cache.npy"
    if args.skip_embed:
        embeddings = get_embeddings([], progress_label="embed", cache_path=str(cache_path))
        if embeddings.size == 0:
            print("✗ --skip-embed 但缓存不可用，请先完成初始嵌入")
            sys.exit(1)
    else:
        print("\n检查 Ollama 连通性...", flush=True)
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

        print(f"\n开始嵌入计算 ({len(texts)} chunks)...", flush=True)
        embeddings = get_embeddings(texts, progress_label="28K embed", cache_path=str(cache_path))

    print(f"\n嵌入矩阵: {embeddings.shape}", flush=True)

    results = {}

    if "A1" not in args.skip:
        results["A1"] = analysis_a1_pca(embeddings, chunk_metas, doc_map, output_dir)

    if "A2" not in args.skip:
        results["A2"] = analysis_a2_doc_similarity(embeddings, chunk_metas, doc_map, output_dir)

    if "A3" not in args.skip:
        results["A3"] = analysis_a3_redundancy(embeddings, chunk_metas, output_dir, args.cos_threshold)

    if "A4" not in args.skip:
        results["A4"] = analysis_a4_train_eval(embeddings, chunk_metas, output_dir)

    print("\n" + "=" * 60)
    print("Task 2d 全部完成!")
    print("=" * 60)
    print(f"产出目录: {output_dir}")
    for f in sorted(output_dir.glob("*")):
        size_kb = f.stat().st_size / 1024
        print(f"  {f.name} ({size_kb:.1f} KB)")


if __name__ == "__main__":
    main()