"""
轻量级 metadata.json 重建脚本 (方案B)
输入: data/processed/ (362 dirs) + data/sources/ (source_list.json, arxiv_candidates.json) + build_corpus.py FALLBACK_METADATA
输出: corpus/metadata.json  (不复制文件，纯元数据生成)
"""

import json
import os
import re
from pathlib import Path
from datetime import date

ROOT = Path(__file__).resolve().parents[1]
PROCESSED = ROOT / "data" / "processed"
SOURCE_LIST = ROOT / "data" / "sources" / "source_list.json"
ARXIV_CANDIDATES = ROOT / "data" / "sources" / "arxiv_candidates.json"
OUTPUT = ROOT / "corpus"
METADATA_OUT = OUTPUT / "metadata.json"

FALLBACK_METADATA = {
    "Computer_Controlled_Systems_Astrom": {
        "title": "Computer-Controlled Systems",
        "author": "Karl Johan Åström / Björn Wittenmark",
        "control_category": "数字控制, 现代控制",
        "source": "GitHub: evilsin/control-and-system-book",
        "copyright": "Open Access / Educational",
    },
    "Essentials_of_Robust_Control_Zhou_Doyle": {
        "title": "Essentials of Robust Control",
        "author": "Kemin Zhou / John C. Doyle",
        "control_category": "鲁棒控制, 现代控制",
        "source": "GitHub: GeorgeQLe/Textbooks-and-Papers",
        "copyright": "Open Access / Educational",
    },
    "控制之美": {
        "title": "控制之美",
        "author": "Unknown / To be verified",
        "control_category": "经典控制, 现代控制",
        "source": "中文教材 / Chinese Textbook",
        "copyright": "Educational / Copyright holder to be verified",
    },
    "控制理论导论_郭雷": {
        "title": "控制理论导论",
        "author": "郭雷",
        "control_category": "现代控制, 控制理论",
        "source": "中文教材 / Chinese Textbook",
        "copyright": "Educational / Copyright holder to be verified",
    },
    "最优控制理论与应用": {
        "title": "最优控制理论与应用",
        "author": "Unknown / To be verified",
        "control_category": "最优控制",
        "source": "中文教材 / Chinese Textbook",
        "copyright": "Educational / Copyright holder to be verified",
    },
    "线性系统理论_郑大钟": {
        "title": "线性系统理论",
        "author": "郑大钟",
        "control_category": "现代控制, 线性系统",
        "source": "中文教材 / Chinese Textbook",
        "copyright": "Educational / Copyright holder to be verified",
    },
    "智能控制": {
        "title": "智能控制",
        "author": "Unknown / To be verified",
        "control_category": "智能控制",
        "source": "中文教材 / Chinese Textbook",
        "copyright": "Educational / Copyright holder to be verified",
    },
    "自动控制原理题海与考研指导_胡寿松": {
        "title": "自动控制原理题海与考研指导",
        "author": "胡寿松",
        "control_category": "经典控制",
        "source": "中文教材 / Chinese Textbook",
        "copyright": "Educational / Copyright holder to be verified",
    },
    "自抗扰控制技术": {
        "title": "自抗扰控制技术",
        "author": "韩京清",
        "control_category": "自抗扰控制, 非线性控制",
        "source": "中文教材 / Chinese Textbook",
        "copyright": "Educational / Copyright holder to be verified",
    },
    "动态系统的反馈控制_Franklin": {
        "title": "动态系统的反馈控制",
        "author": "Gene F. Franklin / J. David Powell / Abbas Emami-Naeini",
        "control_category": "经典控制, 现代控制, 数字控制",
        "source": "中文教材 / Chinese Textbook",
        "copyright": "Educational / Copyright holder to be verified",
    },
    "先进PID控制MATLAB仿真": {
        "title": "先进PID控制MATLAB仿真",
        "author": "刘金琨",
        "control_category": "智能控制, PID控制",
        "source": "中文教材 / Chinese Textbook",
        "copyright": "Educational / Copyright holder to be verified",
    },
    "自动控制原理_胡寿松": {
        "title": "自动控制原理",
        "author": "胡寿松",
        "control_category": "经典控制, 现代控制",
        "source": "中文教材 / Chinese Textbook",
        "copyright": "Educational / Copyright holder to be verified",
    },
    "非线性系统_Khalil": {
        "title": "非线性系统（第三版）",
        "author": "Hassan K. Khalil",
        "control_category": "非线性控制",
        "source": "中文教材 / Chinese Textbook",
        "copyright": "Educational / Copyright holder to be verified",
    },
}

CATEGORY_DIFFICULTY_MAP = {
    "经典控制": "L1", "PID控制": "L1", "现代控制": "L2", "线性系统": "L2",
    "数字控制": "L2", "最优控制": "L3", "鲁棒控制": "L3",
    "自适应控制": "L3", "非线性控制": "L3", "智能控制": "L3",
    "估计与定位": "L2", "导航制导与控制": "L3", "自抗扰控制": "L3",
    "模型预测控制": "L3", "控制理论": "L2",
    "multi_agent": "L2", "robust": "L3", "nonlinear": "L3",
    "optimal": "L3", "adaptive": "L3", "intelligent": "L3",
    "classical": "L1", "digital": "L2", "mpc": "L3", "modern": "L2",
}


def main():
    processed_dirs = sorted(d for d in os.listdir(PROCESSED)
                           if os.path.isdir(PROCESSED / d))

    # ── 1. Build lookup tables ──
    # Textbook lookup: from source_list.json
    txt_by_dirname = {}
    if SOURCE_LIST.exists():
        with open(SOURCE_LIST, encoding="utf-8") as f:
            sl = json.load(f)
        for t in sl["categories"]["textbooks"]:
            filename = t["filename"].replace(".pdf", "")
            txt_by_dirname[filename] = {
                "title": t["title"],
                "author": t["author"],
                "source": t.get("source", ""),
                "copyright": t.get("copyright", ""),
                "control_category": t.get("control_category", ""),
                "size_mb": t.get("size_mb"),
            }

    # Fallback textbook lookup
    txt_fallback = {}
    for dirname, info in FALLBACK_METADATA.items():
        txt_fallback[dirname] = info

    # arXiv lookup: from arxiv_candidates.json (all entries)
    arxiv_lookup = {}
    if ARXIV_CANDIDATES.exists():
        with open(ARXIV_CANDIDATES, encoding="utf-8") as f:
            ac = json.load(f)
        for direction in ac:
            dn = direction.get("direction_cn", direction.get("direction", ""))
            for c in direction["candidates"]:
                arxiv_lookup[c["arxiv_id"]] = {
                    "title": c["title"],
                    "author": ", ".join(c.get("authors", [])),
                    "source": f"arXiv: {c['arxiv_id']}",
                    "copyright": "arXiv Open Access",
                    "control_category": dn,
                    "year": c.get("year"),
                    "arxiv_id": c["arxiv_id"],
                    "direction": direction.get("direction", ""),
                }

    # ── 2. Match processed dirs → metadata ──
    docs = []
    textbook_count = 0
    arxiv_matched = 0
    arxiv_fallback = 0

    for i, dirname in enumerate(processed_dirs, 1):
        md_path = PROCESSED / dirname
        md_files = list(md_path.glob("*.md"))
        file_size = sum(f.stat().st_size for f in md_files) if md_files else 0

        doc_id = f"D{i:02d}"
        doc_type = None
        meta = {}

        # Check if it's an arXiv dir (has arXiv ID prefix like "2403.06397_")
        parts = dirname.split("_", 1)
        if parts[0].count(".") >= 1 and any(c.isdigit() for c in parts[0]):
            arxiv_id = parts[0]
            doc_type = "arxiv"
            if arxiv_id in arxiv_lookup:
                m = arxiv_lookup[arxiv_id]
                meta = {
                    "arxiv_id": arxiv_id,
                    "title": m["title"],
                    "author": m["author"],
                    "source": m["source"],
                    "copyright": m["copyright"],
                    "control_category": m["control_category"],
                    "year": m.get("year"),
                }
                arxiv_matched += 1
            else:
                title_part = parts[1] if len(parts) > 1 else dirname
                title_clean = title_part[:100] if title_part else dirname
                meta = {
                    "arxiv_id": arxiv_id,
                    "title": dirname,
                    "author": "Unknown / arXiv",
                    "source": f"arXiv: {arxiv_id}",
                    "copyright": "arXiv Open Access",
                    "control_category": "控制理论",
                    "year": int(arxiv_id[:2]) + 2000 if arxiv_id[:2].isdigit() else None,
                }
                arxiv_fallback += 1
        else:
            doc_type = "textbook"
            # Try source_list first, then fallback
            if dirname in txt_by_dirname:
                meta = txt_by_dirname[dirname]
            elif dirname in txt_fallback:
                meta = txt_fallback[dirname]
            else:
                meta = {
                    "title": dirname,
                    "author": "Unknown / To be verified",
                    "source": "中文教材 / Chinese Textbook",
                    "copyright": "Educational / Copyright holder to be verified",
                    "control_category": "控制理论",
                }
            textbook_count += 1

        # Determine difficulty_level from control_category
        cats = [c.strip() for c in meta.get("control_category", "控制理论").split(",")]
        difficulty_candidates = []
        for cat in cats:
            if cat in CATEGORY_DIFFICULTY_MAP:
                difficulty_candidates.append(CATEGORY_DIFFICULTY_MAP[cat])
            elif cat.lower() in CATEGORY_DIFFICULTY_MAP:
                difficulty_candidates.append(CATEGORY_DIFFICULTY_MAP[cat.lower()])
        difficulty = "L3"
        if difficulty_candidates:
            order = {"L1": 1, "L2": 2, "L3": 3, "L4": 4}
            difficulty = min(difficulty_candidates, key=lambda x: order.get(x, 3))

        doc = {
            "id": doc_id,
            "type": doc_type,
            "filename": dirname,
            "title": meta.get("title", dirname),
            "author": meta.get("author", "Unknown"),
            "source": meta.get("source", ""),
            "copyright": meta.get("copyright", ""),
            "control_category": cats,
            "difficulty_level": difficulty,
            "file_size_bytes": file_size,
        }
        if meta.get("size_mb"):
            doc["size_mb"] = meta["size_mb"]
        if meta.get("arxiv_id"):
            doc["arxiv_id"] = meta["arxiv_id"]
        if meta.get("year"):
            doc["year"] = meta["year"]

        docs.append(doc)

    # ── 3. Write output ──
    OUTPUT.mkdir(parents=True, exist_ok=True)

    metadata = {
        "project": "ControlSci — 控制科学结构化语料库",
        "version": "1.0-light",
        "updated": str(date.today()),
        "total_docs": len(docs),
        "textbooks": textbook_count,
        "arxiv_papers": len(docs) - textbook_count,
        "categories": {
            "textbooks": [],
            "arxiv_papers": [],
        },
        "generation_note": f"方案B轻量重建: {arxiv_matched} arXiv from candidates, "
                          f"{arxiv_fallback} arXiv fallback, {textbook_count} textbooks",
        "docs": docs,
    }

    with open(METADATA_OUT, "w", encoding="utf-8") as f:
        json.dump(metadata, f, ensure_ascii=False, indent=2)

    print(f"[OK] corpus/metadata.json 已生成", flush=True)
    print(f"     {len(docs)} 篇文档", flush=True)
    print(f"     {textbook_count} 教材 + {len(docs) - textbook_count} 论文", flush=True)
    print(f"     arXiv: {arxiv_matched} from candidates + {arxiv_fallback} fallback", flush=True)
    print(f"     输出: {METADATA_OUT}  ({METADATA_OUT.stat().st_size / 1024:.1f} KB)", flush=True)

    # Quick validation
    empty_author = sum(1 for d in docs if not d.get("author") or d["author"] == "Unknown")
    empty_cat = sum(1 for d in docs if not d.get("control_category"))
    print(f"\n[VALIDATION]", flush=True)
    print(f"     author 空/Unknown: {empty_author}/{len(docs)}", flush=True)
    print(f"     control_category 空: {empty_cat}/{len(docs)}", flush=True)


if __name__ == "__main__":
    main()
