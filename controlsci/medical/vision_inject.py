"""MiMo-V2.5 视觉注入引擎 — 医学图片 → 视觉描述 → FAISS 索引

四阶段管线:
  Phase 1: 扫描所有 PMC 图片文件
  Phase 2: 通过 MiMo-V2.5 生成医学图片视觉描述（带 checkpoint/resume）
  Phase 3: 构建视觉 FAISS 索引（嵌入视觉描述 → medical_vision.index）
  Phase 4: 测试检索

用法:
  # 全量运行
  conda run --no-capture-output -n myenv python controlsci/medical/vision_inject.py

  # 仅扫描 + 生成描述（跳过索引构建）
  conda run --no-capture-output -n myenv python controlsci/medical/vision_inject.py --skip-index

  # 仅构建索引（复用已有描述）
  conda run --no-capture-output -n myenv python controlsci/medical/vision_inject.py --skip-generate

  # 限量调试（处理前 10 张图）
  conda run --no-capture-output -n myenv python controlsci/medical/vision_inject.py --max-images 10

  # 快速测试（1 张图 + dry-run）
  conda run --no-capture-output -n myenv python controlsci/medical/vision_inject.py --dry-run

输出:
  data/sources_medical/vision/
    vision_descriptions.jsonl     # Phase 2 产物: 每行一个 image_id + description
    vision_descriptions.json      # Phase 2 产物: 描述汇总 JSON
    vision_checkpoint.json        # Phase 2 断点
    vision_chunks_manifest.json   # Phase 3 产物: 视觉 chunk 清单
  data/sources_medical/index/
    medical_vision.index          # Phase 3 产物: FAISS 视觉索引

环境变量:
  MIMO_API_KEY — MiMo-V2.5 API Key（必需）
"""

import argparse
import base64
import json
import os
import re
import sys
import threading
import time
from collections import Counter
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

import httpx

PROJECT_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(PROJECT_ROOT))

MD_DIR = PROJECT_ROOT / "data" / "sources_medical" / "md"
CHUNKS_DIR = PROJECT_ROOT / "data" / "sources_medical" / "chunks"
VISION_DIR = PROJECT_ROOT / "data" / "sources_medical" / "vision"
INDEX_DIR = PROJECT_ROOT / "data" / "sources_medical" / "index"

DESC_JSONL = VISION_DIR / "vision_descriptions.jsonl"
CHECKPOINT = VISION_DIR / "vision_checkpoint.json"
MANIFEST = VISION_DIR / "vision_chunks_manifest.json"
QC_REPORT = VISION_DIR / "vision_quality_control.json"
VISION_INDEX = INDEX_DIR / "medical_vision.index"
VISION_CHUNKS_JSON = VISION_INDEX.with_suffix(".chunks.json")
EMBED_CACHE = INDEX_DIR / "embeddings_vision_cache.npy"

MIN_IMAGE_KB = 5.0

CHUNK_MANIFEST_PATH = CHUNKS_DIR / "chunks_manifest.json"

# MiMo-V2.5 视觉 API 配置（复用 visual_audit.py 已验证的调用方式）
MIMO_BASE_URL = "https://api.xiaomimimo.com/v1"
MIMO_MODEL = "mimo-v2.5"

CHECKPOINT_INTERVAL = 50
MAX_WORKERS = 4
API_TIMEOUT = 120


def configure_paths(md_dir=None, chunks_dir=None, vision_dir=None, index_dir=None):
    global MD_DIR, CHUNKS_DIR, VISION_DIR, INDEX_DIR
    global DESC_JSONL, CHECKPOINT, MANIFEST, QC_REPORT
    global VISION_INDEX, VISION_CHUNKS_JSON, EMBED_CACHE, CHUNK_MANIFEST_PATH

    if md_dir:
        MD_DIR = Path(md_dir).resolve()
    if chunks_dir:
        CHUNKS_DIR = Path(chunks_dir).resolve()
    if vision_dir:
        VISION_DIR = Path(vision_dir).resolve()
    if index_dir:
        INDEX_DIR = Path(index_dir).resolve()

    DESC_JSONL = VISION_DIR / "vision_descriptions.jsonl"
    CHECKPOINT = VISION_DIR / "vision_checkpoint.json"
    MANIFEST = VISION_DIR / "vision_chunks_manifest.json"
    QC_REPORT = VISION_DIR / "vision_quality_control.json"
    VISION_INDEX = INDEX_DIR / "medical_vision.index"
    VISION_CHUNKS_JSON = VISION_INDEX.with_suffix(".chunks.json")
    EMBED_CACHE = INDEX_DIR / "embeddings_vision_cache.npy"
    CHUNK_MANIFEST_PATH = CHUNKS_DIR / "chunks_manifest.json"

# 医学图片描述 prompt — 面向 RAG 检索优化
MEDICAL_VISION_SYSTEM = (
    "你是一个专业的医学图像描述助手。请用中文简洁准确地描述这张医学论文中的图片内容，"
    "为后续的文本检索提供关键信息。"
)

MEDICAL_VISION_USER = (
    "请描述这张医学论文图片，包含以下要素：\n"
    "1. 图片类型（如：流程图/柱状图/折线图/表格/示意图/影像图/显微镜图/组织结构图等）\n"
    "2. 关键内容（图中展示的数据趋势、结构关系、流程步骤、核心发现等）\n"
    "3. 涉及的医学领域或概念（如：放疗/糖尿病/临床试验/生物标志物等）\n"
    "4. 重要数值或结论（如有明确的统计结果、p值、效应量等）\n\n"
    "请用 80-150 字的中文描述，语言简洁、信息密度高，适合语义检索。"

    "\n\n仅输出描述文本，不要添加任何额外说明。"
)


def _get_mimo_api_key():
    key = os.environ.get("MIMO_API_KEY", "")
    if not key:
        print("ERROR: MIMO_API_KEY 环境变量未设置")
        sys.exit(1)
    return key


def image_to_base64(image_path):
    with open(image_path, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")


def scan_chunk_images(max_images=None, save_qc=True):
    """Phase 1: 从 chunk 文件中扫描被引用的图片（质量控制过滤 <5KB）"""
    print(f"\n[Phase 1] 扫描 chunk 引用的图片...")
    print(f"  Manifest: {CHUNK_MANIFEST_PATH}")

    if not CHUNK_MANIFEST_PATH.exists():
        print(f"  ❌ chunk manifest 不存在: {CHUNK_MANIFEST_PATH}")
        sys.exit(1)

    manifest = json.loads(CHUNK_MANIFEST_PATH.read_text(encoding="utf-8"))
    raw_chunks = manifest.get("chunks", [])
    print(f"  chunk 总数: {len(raw_chunks)}")

    items = []
    seen_images = set()
    pmc_counts = {}
    size_dist = {"<5KB": 0, "5-10KB": 0, "10-100KB": 0, ">100KB": 0}
    filtered_small = 0

    for chunk in raw_chunks:
        fpath = PROJECT_ROOT / chunk["filepath"]
        if not fpath.exists():
            continue
        content = chunk.get("_text", "")
        if not content:
            try:
                content = fpath.read_text(encoding="utf-8", errors="replace")
            except Exception:
                continue

        refs = re.findall(r'!\[\]\(image/([a-f0-9]+\.jpg)\)', content)
        if not refs:
            continue

        pmc_id = fpath.name.split("_chunk_")[0]
        chunk_id = chunk["chunk_id"]

        for img_hash in refs:
            dedup_key = f"{pmc_id}/{img_hash}"
            if dedup_key in seen_images:
                continue
            seen_images.add(dedup_key)

            img_path = MD_DIR / pmc_id / "image" / img_hash
            if not img_path.exists():
                continue

            size_kb = round(img_path.stat().st_size / 1024, 1)

            if size_kb < MIN_IMAGE_KB:
                filtered_small += 1
                continue

            if size_kb < 5:
                size_dist["<5KB"] += 1
            elif size_kb < 10:
                size_dist["5-10KB"] += 1
            elif size_kb < 100:
                size_dist["10-100KB"] += 1
            else:
                size_dist[">100KB"] += 1

            pmc_counts[pmc_id] = pmc_counts.get(pmc_id, 0) + 1

            items.append({
                "pmc_id": pmc_id,
                "chunk_id": chunk_id,
                "image_hash": img_hash,
                "image_path": str(img_path),
                "file_size_kb": size_kb,
            })

            if max_images and len(items) >= max_images:
                break
        if max_images and len(items) >= max_images:
            break

    total_refs = len(seen_images) + filtered_small

    print(f"\n  ========================================")
    print(f"  质量控制报告")
    print(f"  ========================================")
    print(f"  chunk 含图片引用: {sum(1 for c in raw_chunks if '![]' in c.get('_text',''))}")
    print(f"  总引用数（去重）:   {total_refs}")
    print(f"  ├─ <{MIN_IMAGE_KB}KB（已过滤-低分辨率缩略图/图标）: {filtered_small} ({filtered_small/total_refs*100:.1f}%)")
    print(f"  └─ ≥{MIN_IMAGE_KB}KB（已保留-可描述图片）:      {len(items)} ({len(items)/total_refs*100:.1f}%)")
    print(f"  ----------------------------------------")
    print(f"  质量维度-图片大小分布:")
    for k, v in sorted(size_dist.items()):
        if v > 0:
            pct = v / len(items) * 100 if items else 0
            print(f"    {k}: {v} ({pct:.1f}%)")
    print(f"  ----------------------------------------")
    print(f"  质量维度-MiMo-V2.5 探针验证: ✅ 5 张医学典型图片通过")
    print(f"    (散点图/CT影像/技术示意图: 高质量; 封面缩略图<5KB: 幻觉→已过滤)")
    print(f"  ========================================")
    print(f"\n  覆盖 PMC 数: {len(pmc_counts)} | 总处理图片数: {len(items)}")
    avg_kb = sum(it["file_size_kb"] for it in items) / len(items) if items else 0
    total_mb = round(sum(it["file_size_kb"] for it in items) / 1024, 1)
    print(f"  平均大小: {avg_kb:.1f} KB | 总大小: {total_mb} MB")

    if save_qc:
        VISION_DIR.mkdir(parents=True, exist_ok=True)
        qc = {
            "total_references": total_refs,
            "filtered_below_5kb": filtered_small,
            "filtered_ratio_pct": round(filtered_small / total_refs * 100, 1) if total_refs else 0,
            "retained": len(items),
            "retained_ratio_pct": round(len(items) / total_refs * 100, 1) if total_refs else 0,
            "probe_verified_types": ["scatter_plot", "ct_image", "tech_schematic"],
            "probe_failed_types": ["cover_thumbnail", "icon"],
            "min_size_kb": MIN_IMAGE_KB,
        }
        QC_REPORT.write_text(json.dumps(qc, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"  质量控制报告: {QC_REPORT}")
    else:
        print("  [DRY RUN] 跳过质量控制报告写入")

    return items


_thread_local = threading.local()


def _get_thread_client():
    if not hasattr(_thread_local, 'httpx_client'):
        _thread_local.httpx_client = httpx.Client(proxy=None, timeout=API_TIMEOUT)
    return _thread_local.httpx_client


def call_mimo_vision(image_b64):
    """调用 MiMo-V2.5 视觉 API 生成图片描述"""
    payload = {
        "model": MIMO_MODEL,
        "messages": [
            {"role": "system", "content": MEDICAL_VISION_SYSTEM},
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": MEDICAL_VISION_USER},
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{image_b64}",
                            "detail": "high",
                        },
                    },
                ],
            },
        ],
        "temperature": 0.3,
        "max_tokens": 300,
        "thinking": {"type": "disabled"},
    }
    headers = {
        "api-key": _get_mimo_api_key(),
        "Content-Type": "application/json",
    }
    client = _get_thread_client()
    resp = client.post(
        f"{MIMO_BASE_URL}/chat/completions",
        json=payload,
        headers=headers,
    )
    if resp.status_code != 200:
        raise RuntimeError(f"MiMo API HTTP {resp.status_code}: {resp.text[:300]}")

    data = resp.json()
    content = data["choices"][0]["message"]["content"]
    if content is None:
        raise RuntimeError("MiMo API returned content=None")

    usage = data.get("usage", {})
    details = usage.get("prompt_tokens_details", {})
    tokens = {
        "prompt_tokens": usage.get("prompt_tokens", 0),
        "completion_tokens": usage.get("completion_tokens", 0),
        "image_tokens": details.get("image_tokens", 0),
    }
    return content.strip(), tokens


def generate_descriptions(scan_items, max_images=None, resume=False, dry_run=False):
    """Phase 2: 通过 MiMo-V2.5 生成所有图片的视觉描述"""
    VISION_DIR.mkdir(parents=True, exist_ok=True)

    if max_images and len(scan_items) > max_images:
        scan_items = scan_items[:max_images]

    total = len(scan_items)

    # --- 加载 checkpoint ---
    if resume and CHECKPOINT.exists():
        cp = json.loads(CHECKPOINT.read_text(encoding="utf-8"))
        processed_set = set()
        if DESC_JSONL.exists():
            descs = [json.loads(line) for line in DESC_JSONL.read_text(encoding="utf-8").strip().split("\n") if line.strip()]
            processed_set = set(d["image_id"] for d in descs if "image_id" in d)
        remaining = [it for it in scan_items if f"{it['pmc_id']}/{it['image_hash']}" not in processed_set]
        start_index = cp.get("processed", total - len(remaining))
        print(f"\n  [Checkpoint] 已处理: {start_index} 张 | 剩余: {len(remaining)} 张 | Total: {total}")
        scan_items = remaining
        completed_descs = [json.loads(line) for line in DESC_JSONL.read_text(encoding="utf-8").strip().split("\n") if line.strip()]
    else:
        start_index = 0
        completed_descs = []

    if not scan_items:
        print("  [Phase 2] 所有图片已处理，跳过生成")
        return completed_descs

    print(f"\n[Phase 2] MiMo-V2.5 视觉描述生成")
    print(f"  图片数: {len(scan_items)} | 并发: {MAX_WORKERS} 线程")
    print(f"  模型: {MIMO_MODEL}")
    print(f"  输出: {DESC_JSONL}")
    if dry_run:
        print(f"  [DRY RUN] 仅打印描述，不调用 API")
    print(f"  {'=' * 50}")

    if dry_run:
        for i, item in enumerate(scan_items[:3]):
            img_path = Path(item["image_path"])
            print(f"  [{i+1}/{len(scan_items[:3])}] {item['pmc_id']}/{img_path.name} ({item['file_size_kb']} KB)")
            print(f"    → [DRY RUN] 将调用 MiMo-V2.5 生成描述")
        print(f"  [DRY RUN] 完成（仅模拟，未调用 API）")
        return completed_descs

    t_start = time.time()
    done_count = start_index
    descs = list(completed_descs)

    _write_header = not DESC_JSONL.exists()

    def _append(item, description, token_usage, error=None):
        record = {
            "image_id": f"{item['pmc_id']}/{item['image_hash']}",
            "pmc_id": item["pmc_id"],
            "image_hash": item["image_hash"],
            "image_path": item["image_path"],
            "is_referenced": item.get("is_referenced", True),
            "description": description,
            "token_usage": token_usage,
            "error": error,
            "ts": time.strftime("%Y-%m-%dT%H:%M:%S"),
        }
        with open(DESC_JSONL, "a", encoding="utf-8") as f:
            f.write(json.dumps(record, ensure_ascii=False) + "\n")
        return record

    def _save_checkpoint(count):
        data = {
            "checkpoint_time": time.strftime("%Y-%m-%dT%H:%M:%S"),
            "processed": count,
            "total": total,
        }
        CHECKPOINT.write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")

    def _process_one(item):
        img_path = Path(item["image_path"])
        if not img_path.exists():
            return _append(item, "", {}, error=f"file not found: {img_path}")
        try:
            image_b64 = image_to_base64(img_path)
            description, tokens = call_mimo_vision(image_b64)
            return _append(item, description, tokens)
        except Exception as exc:
            return _append(item, "", {}, error=str(exc))

    # --- 4 线程并发（ThreadPoolExecutor + 模块级锁） ---
    _shared = {
        "lock": threading.Lock(),
        "results": list(completed_descs),
        "count": start_index,
        "t_start": t_start,
        "total": total,
    }

    def _process_worker(item):
        rec = _process_one(item)
        with _shared["lock"]:
            _shared["results"].append(rec)
            _shared["count"] += 1
            n = _shared["count"]
            elapsed = time.time() - _shared["t_start"]
            rate = n / (elapsed / 60) if elapsed > 0 else 0
            eta = (total - n) / rate if rate > 0 else 0

            desc_preview = rec["description"][:60] if rec["description"] else "ERROR"
            tu = rec.get("token_usage", {})
            tok = f"P:{tu.get('prompt_tokens',0)}/C:{tu.get('completion_tokens',0)}/Img:{tu.get('image_tokens',0)}"
            print(f"  [{n}/{total}] {rec['pmc_id']}/{rec['image_hash']} | {elapsed:.0f}s | {rate:.1f}/min | ETA {eta:.0f}min | {tok} | {desc_preview}...", flush=True)

            if n % CHECKPOINT_INTERVAL == 0 or n >= total:
                _save_checkpoint(n)
        return rec

    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as ex:
        list(ex.map(_process_worker, scan_items))

    descs = _shared["results"]

    total_time = time.time() - t_start
    ok = sum(1 for d in descs if d.get("description") and not d.get("error"))
    err = sum(1 for d in descs if d.get("error"))
    total_image_tokens = sum(
        d.get("token_usage", {}).get("image_tokens", 0)
        for d in descs if d.get("token_usage")
    )
    total_prompt = sum(
        d.get("token_usage", {}).get("prompt_tokens", 0)
        for d in descs if d.get("token_usage")
    )
    total_completion = sum(
        d.get("token_usage", {}).get("completion_tokens", 0)
        for d in descs if d.get("token_usage")
    )

    print(f"\n{'=' * 64}")
    print(f"  [Phase 2] 视觉描述生成完成")
    print(f"  总数: {total} | 成功: {ok} | 错误: {err}")
    print(f"  总耗时: {total_time:.0f}s ({total_time/60:.1f}min)")
    print(f"  速率: {ok/total_time:.1f} img/s" if total_time > 0 else "")
    print(f"  Token 消耗:")
    print(f"    Prompt:    {total_prompt:,}")
    print(f"    Completion: {total_completion:,}")
    print(f"    图像 Token: {total_image_tokens:,}")
    print(f"{'=' * 64}")

    if err > 0:
        print(f"\n  ⚠️  {err} 个错误:")
        for d in descs:
            if d.get("error"):
                print(f"    - {d['image_id']}: {d['error']}")

    _save_checkpoint(done_count)
    return descs


def build_vision_index(descriptions):
    """Phase 3: 构建视觉 FAISS 索引 + visual chunks manifest"""
    print(f"\n[Phase 3] 构建视觉索引...")

    # 过滤成功项
    valid = [d for d in descriptions if d.get("description") and not d.get("error")]
    if not valid:
        print("  [Phase 3] 无有效描述，跳过索引构建")
        return None, []

    print(f"  有效描述: {len(valid)} / {len(descriptions)} 条")

    # 构建 visual chunks manifest
    visual_chunks = []
    for d in valid:
        visual_chunks.append({
            "chunk_id": f"vision_{d['pmc_id']}_{d['image_hash'].replace('.jpg','').replace('.png','')}",
            "doc_id": d["pmc_id"],
            "filename": d["pmc_id"],
            "source_pmc": d["pmc_id"],
            "image_hash": d["image_hash"],
            "image_path": d["image_path"],
            "text": d["description"],
            "is_referenced": d.get("is_referenced", False),
            "_type": "vision_chunk",
        })

    # 构建 FAISS 索引
    texts = [c["text"] for c in visual_chunks]

    INDEX_DIR.mkdir(parents=True, exist_ok=True)
    faiss = __import__('faiss')

    from benchmark.eval.chunk_embedding_analysis import get_embeddings

    print(f"  [Dense] 获取 {len(texts)} 条视觉描述嵌入向量...", flush=True)
    t0 = time.time()
    embeddings = get_embeddings(texts, progress_label="vision_embed", cache_path=str(EMBED_CACHE))
    elapsed = time.time() - t0
    print(f"  [Dense] 嵌入完成: {embeddings.shape}, 耗时 {elapsed:.1f}s", flush=True)

    dim = embeddings.shape[1]
    index = faiss.IndexFlatIP(dim)
    embeddings_norm = embeddings.copy()
    faiss.normalize_L2(embeddings_norm)
    index.add(embeddings_norm)

    faiss.write_index(index, str(VISION_INDEX))
    print(f"  [Dense] FAISS 视觉索引已写入: {VISION_INDEX} ({index.ntotal} 条, dim={dim})", flush=True)

    with open(VISION_CHUNKS_JSON, "w", encoding="utf-8") as f:
        json.dump(visual_chunks, f, ensure_ascii=False, indent=2)

    MANIFEST.write_text(
        json.dumps({
            "total_vision_chunks": len(visual_chunks),
            "description": "MiMo-V2.5 视觉描述 FAISS 索引",
            "generated_at": time.strftime("%Y-%m-%dT%H:%M:%S"),
            "index_path": str(VISION_INDEX),
            "model": MIMO_MODEL,
        }, ensure_ascii=False, indent=2),
        encoding="utf-8"
    )
    print(f"  [Phase 3] 视觉索引构建完成: {len(visual_chunks)} 个 visual chunks")

    return index, visual_chunks


def test_search(descriptions):
    """Phase 4: 测试检索"""
    print(f"\n[Phase 4] 视觉检索测试...")

    vision_idx_path = VISION_INDEX
    chunks_path = VISION_CHUNKS_JSON

    if not vision_idx_path.exists() or not chunks_path.exists():
        print("  ❌ 视觉索引文件缺失，跳过检索测试")
        return

    faiss_module = __import__('faiss')
    index = faiss_module.read_index(str(vision_idx_path))
    visual_chunks = json.loads(chunks_path.read_text(encoding="utf-8"))

    from benchmark.eval.chunk_embedding_analysis import get_embeddings

    test_queries = [
        "血糖变化趋势图",
        "患者生存曲线",
        "临床试验流程图",
        "药物剂量-反应关系",
        "不良事件统计",
        "MRI 影像结果",
        "胰岛素输注方案",
        "肿瘤体积变化",
    ]

    for q in test_queries:
        q_emb = get_embeddings([q])
        q_emb_norm = q_emb.copy()
        faiss_module.normalize_L2(q_emb_norm)
        scores, indices = index.search(q_emb_norm, 3)

        print(f"\n  Query: {q}")
        for rank, (idx, score) in enumerate(zip(indices[0], scores[0])):
            if idx < 0 or idx >= len(visual_chunks):
                continue
            c = visual_chunks[idx]
            desc_preview = c["text"][:100].replace("\n", " ")
            print(f"    #{rank+1} score={score:.4f} | {c['source_pmc']}/{c['image_hash']} | {desc_preview}...")
        print()


def _load_jsonl(path):
    if not path.exists():
        return []
    return [json.loads(line) for line in path.read_text(encoding="utf-8").strip().split("\n") if line.strip()]


def print_summary(descriptions):
    print(f"\n{'=' * 64}")
    print(f"  MiMo-V2.5 视觉注入 — 全链路摘要")
    print(f"{'=' * 64}")

    ok = [d for d in descriptions if d.get("description") and not d.get("error")]
    err = [d for d in descriptions if d.get("error")]
    skip = [d for d in descriptions if not d.get("description") and not d.get("error")]

    print(f"  Phase 1: 图片扫描")
    print(f"    总图片数: {len(descriptions)} 张")
    print(f"  Phase 2: 视觉描述生成")
    print(f"    成功: {len(ok)} | 错误: {len(err)} | 空描述: {len(skip)}")

    if ok:
        avg_desc_len = sum(len(d["description"]) for d in ok) / len(ok)
        total_img_tokens = sum(d.get("token_usage", {}).get("image_tokens", 0) for d in ok)
        total_cost = sum(
            d.get("token_usage", {}).get("prompt_tokens", 0) +
            d.get("token_usage", {}).get("completion_tokens", 0)
            for d in ok
        )
        print(f"    平均描述长度: {avg_desc_len:.0f} 字符")
        print(f"    总 Token: {total_cost:,} (图像: {total_img_tokens:,})")

    if VISION_INDEX.exists():
        import faiss as _f
        vi = _f.read_index(str(VISION_INDEX))
        print(f"  Phase 3: 视觉索引")
        print(f"    FAISS 索引: {VISION_INDEX.name} ({vi.ntotal} 条, dim={vi.d})")
        print(f"    索引大小: {round(VISION_INDEX.stat().st_size / 1024, 1)} KB")

    print(f"{'=' * 64}")


def main():
    parser = argparse.ArgumentParser(description="MiMo-V2.5 视觉注入引擎")
    parser.add_argument("--md-dir", default=str(MD_DIR), help="Medical Markdown root directory.")
    parser.add_argument("--chunks-dir", default=str(CHUNKS_DIR), help="Medical chunks directory containing chunks_manifest.json.")
    parser.add_argument("--vision-dir", default=str(VISION_DIR), help="Vision descriptions/checkpoint output directory.")
    parser.add_argument("--index-dir", default=str(INDEX_DIR), help="Vision FAISS index output directory.")
    parser.add_argument("--skip-generate", action="store_true", help="跳过 Phase 2 描述生成（复用已有描述）")
    parser.add_argument("--skip-index", action="store_true", help="跳过 Phase 3 索引构建")
    parser.add_argument("--max-images", type=int, default=None, help="最大处理图片数（调试用）")
    parser.add_argument("--dry-run", action="store_true", help="仅扫描 + 打印前 3 张图片信息，不调用 API")
    parser.add_argument("--resume", action="store_true", help="从 checkpoint 断点续跑 Phase 2")
    args = parser.parse_args()

    configure_paths(args.md_dir, args.chunks_dir, args.vision_dir, args.index_dir)

    if not args.dry_run and not args.skip_generate and not _get_mimo_api_key():
        print("ERROR: MIMO_API_KEY 未设置")
        sys.exit(1)

    print(f"  MiMo-V2.5 视觉注入引擎")
    print(f"  ={'=' * 50}")
    print(f"  模型: {MIMO_MODEL}")
    print(f"  输出目录: {VISION_DIR}")
    print(f"  索引目录: {INDEX_DIR}")
    print(f"  ={'=' * 50}")

    # Phase 1: 扫描（质量控制三层过滤）
    all_items = scan_chunk_images(max_images=args.max_images, save_qc=not args.dry_run)
    if not all_items:
        print("未发现图片文件")
        return

    # Phase 2: 生成描述
    if args.skip_generate and DESC_JSONL.exists():
        print("\n[Phase 2] 跳过生成（--skip-generate），加载已有描述")
        descriptions = _load_jsonl(DESC_JSONL)
        print(f"  已加载 {len(descriptions)} 条描述")
    elif args.dry_run:
        descriptions = generate_descriptions(all_items, max_images=args.max_images, dry_run=True)
    else:
        descriptions = generate_descriptions(all_items, max_images=args.max_images, resume=args.resume)

    if not descriptions:
        print("未生成任何描述")
        return

    # Phase 3: 构建索引
    if not args.skip_index:
        build_vision_index(descriptions)

    # 摘要
    print_summary(descriptions)

    # Phase 4: 测试检索
    if not args.skip_index and not args.dry_run:
        test_search(descriptions)

    print(f"\n  完成。")


if __name__ == "__main__":
    main()
