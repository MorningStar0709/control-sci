"""视觉审计 Top10 最佳/最差画廊

从 visual_audit_results.jsonl (9,227 条记录) 中提取 Top 10 最佳对齐和
Top 10 最差对齐的图片-公式对，生成可视化对比画廊。

用法:
  conda run --no-capture-output -n myenv python tools/submission_figures/viz_alignment_gallery.py

产出:
  - docs/assets/alignment_gallery_best.png   — Top 10 最佳对齐
  - docs/assets/alignment_gallery_worst.png  — Top 10 最差对齐
  - docs/evidence/alignment_gallery_captions.md — 每对的解释文字
"""

import json
import random
import re
from collections import Counter, defaultdict
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.font_manager as fm
import matplotlib.pyplot as plt

_CJK_CANDIDATES = [
    Path("C:/Windows/Fonts/NotoSansSC-VF.ttf"),
    Path("C:/Windows/Fonts/msyh.ttc"),
    Path("/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc"),
    Path("/System/Library/Fonts/NotoSansCJKsc-Regular.otf"),
]
_CJK_FONT_PATH = next((p for p in _CJK_CANDIDATES if p.exists()), None)
if _CJK_FONT_PATH is not None:
    fm.fontManager.addfont(str(_CJK_FONT_PATH))
    _CJK_NAME = fm.FontProperties(fname=str(_CJK_FONT_PATH)).get_name()
    matplotlib.rcParams["font.family"] = "sans-serif"
    matplotlib.rcParams["font.sans-serif"] = [_CJK_NAME, "DejaVu Sans"] + matplotlib.rcParams["font.sans-serif"]
    matplotlib.rcParams["axes.unicode_minus"] = False
else:
    print("  ⚠ 未找到 CJK 字体，中文可能渲染为方框。建议安装 Noto Sans SC")

ROOT = Path(__file__).resolve().parents[2]

RESULTS_LOG = ROOT / "benchmark" / "agent" / "results" / "visual_audit_results.jsonl"
CHUNKS_DIR = ROOT / "corpus" / "chunks"
ASSETS_DIR = ROOT / "docs" / "assets"
EVIDENCE_DIR = ROOT / "docs" / "evidence"

ASSETS_DIR.mkdir(parents=True, exist_ok=True)
EVIDENCE_DIR.mkdir(parents=True, exist_ok=True)

FM_BLOCK = re.compile(r'\$\$(.+?)\$\$', re.DOTALL)
FM_INLINE = re.compile(r'(?<!\$)\$(?!\$)([^$]+?)(?<!\$)\$(?!\$)')

JUDGMENT_LABELS = {
    "consistent": "Consistent",
    "partially_consistent": "Partial",
    "inconsistent": "Inconsistent",
    "uncertain": "Uncertain",
}

JUDGMENT_COLORS = {
    "consistent": "#2ecc71",
    "partially_consistent": "#f39c12",
    "inconsistent": "#e74c3c",
    "uncertain": "#95a5a6",
}


def read_results():
    results = []
    errors = 0
    with open(RESULTS_LOG, "r", encoding="utf-8") as f:
        for line_num, line in enumerate(f, 1):
            line = line.strip()
            if not line:
                continue
            try:
                results.append(json.loads(line))
            except json.JSONDecodeError as e:
                errors += 1
                if errors <= 3:
                    print(f"  ⚠ 跳过第 {line_num} 行: JSON 解析失败 — {e}")
    if errors:
        print(f"  ⚠ 共跳过 {errors} 条损坏记录（{len(results)} 条有效）")
    return results


def find_chunk_file(chunk_id):
    for split in ["train", "eval"]:
        p = CHUNKS_DIR / split / f"{chunk_id}.md"
        if p.exists():
            return p
    return None


def extract_formulas_from_text(text):
    scan = re.sub(r"```.*?```", "", text, flags=re.DOTALL)
    formulas = []
    for m in FM_BLOCK.findall(scan):
        formulas.append(("block", m.strip()))
    for m in FM_INLINE.findall(scan):
        formulas.append(("inline", m.strip()))
    return formulas


def extract_text_context(text, image_hash):
    lines = text.split("\n")
    img_line_idx = None
    for i, line in enumerate(lines):
        if image_hash in line:
            img_line_idx = i
            break
    if img_line_idx is None:
        before = text[:600]
        after = ""
    else:
        before = "\n".join(lines[max(0, img_line_idx - 8):img_line_idx])
        after = "\n".join(lines[img_line_idx + 1:min(len(lines), img_line_idx + 4)])
    return before.strip(), after.strip()


def shorten_formula(formula, max_chars=80):
    if len(formula) <= max_chars:
        return formula
    return formula[:max_chars - 3] + "..."


def pick_diverse(items, n=10):
    seen_chunks = set()
    seen_docs = defaultdict(int)
    selected = []

    for item in items:
        chunk_id = item.get("chunk_id", "")
        doc_id = item.get("doc_id", "")
        if not doc_id:
            doc_id = chunk_id.split("_chunk_")[0] if "_chunk_" in chunk_id else chunk_id[:20]

        if chunk_id in seen_chunks:
            continue
        if seen_docs[doc_id] >= 2:
            continue

        selected.append(item)
        seen_chunks.add(chunk_id)
        seen_docs[doc_id] += 1

        if len(selected) >= n:
            break

    if len(selected) < n:
        for item in items:
            if item not in selected and len(selected) < n:
                selected.append(item)

    return selected


def prepare_gallery_data(results, mode="best"):
    if mode == "best":
        candidates = [r for r in results if r.get("judgment") == "consistent" and "error" not in r]
    else:
        candidates = [r for r in results if r.get("judgment") in ("inconsistent", "uncertain") and "error" not in r]
    random.shuffle(candidates)
    selected = pick_diverse(candidates, n=10)
    gallery = []

    for item in selected:
        chunk_id = item["chunk_id"]
        image_path = Path(item["image_path"])
        image_hash = item["image_hash"]
        judgment = item["judgment"]
        raw_response = item.get("raw_response", "")

        if not image_path.exists():
            print(f"  ⚠ 图片不存在: {image_path}")
            gallery.append({
                "chunk_id": chunk_id,
                "image_hash": image_hash,
                "judgment": judgment,
                "raw_response": raw_response,
                "image_path": image_path,
                "formulas": [],
                "text_before": "",
                "text_after": "",
                "image_loaded": False,
            })
            continue

        chunk_file = find_chunk_file(chunk_id)
        formulas = []
        text_before = ""
        text_after = ""

        if chunk_file:
            content = chunk_file.read_text(encoding="utf-8")
            raw_formulas = extract_formulas_from_text(content)
            for t, f in raw_formulas[:5]:
                formulas.append({"type": t, "latex": shorten_formula(f, 100)})
            tb, ta = extract_text_context(content, image_hash)
            text_before = tb[:200]
            text_after = ta[:200]

        gallery.append({
            "chunk_id": chunk_id,
            "image_hash": image_hash,
            "judgment": judgment,
            "raw_response": raw_response,
            "image_path": image_path,
            "formulas": formulas,
            "text_before": text_before,
            "text_after": text_after,
            "image_loaded": True,
        })

    return gallery


def draw_gallery(gallery, mode="best", output_path=None):
    n = len(gallery)

    fig_width = 20
    row_height = 3.2
    fig_height = max(4, n * row_height + 2)

    fig, axes = plt.subplots(n, 2, figsize=(fig_width, fig_height),
                             gridspec_kw={"width_ratios": [1, 1.5], "hspace": 0.4, "wspace": 0.3})
    if n == 1:
        axes = axes.reshape(1, 2)

    title_color = "#27ae60" if mode == "best" else "#e74c3c"
    title_prefix = "Best Aligned Top 10" if mode == "best" else "Worst Aligned Top 10"
    fig.suptitle(f"Cross-Modal Alignment Gallery — {title_prefix}", fontsize=22, fontweight="bold",
                 color=title_color, y=0.98)

    for i, data in enumerate(gallery):
        ax_img = axes[i, 0]
        ax_text = axes[i, 1]

        image_path = data["image_path"]
        if data["image_loaded"]:
            try:
                img = plt.imread(image_path)
                ax_img.imshow(img)
                ax_img.set_title(f"#{i+1} Image: {data['image_hash'][:16]}...", fontsize=10, pad=4)
            except Exception as e:
                ax_img.text(0.5, 0.5, f"Image load failed\n{str(e)}", ha="center", va="center",
                            transform=ax_img.transAxes, fontsize=9, color="red")
        else:
            ax_img.text(0.5, 0.5, f"Image unavailable\n{data['image_path'].name}", ha="center", va="center",
                        transform=ax_img.transAxes, fontsize=9, color="gray")
        ax_img.set_xticks([])
        ax_img.set_yticks([])
        for spine in ax_img.spines.values():
            spine.set_visible(False)

        chunk_id = data["chunk_id"]
        doc_part = chunk_id.split("_chunk_")[0] if "_chunk_" in chunk_id else chunk_id[:20]

        text_lines = []
        text_lines.append(f"[#{i+1}] Chunk: {chunk_id[:60]}...")
        text_lines.append(f"Doc: {doc_part[:50]}...")
        text_lines.append(f"Judgment: {JUDGMENT_LABELS.get(data['judgment'], data['judgment'])}")

        reason = data.get("raw_response", "")
        reason_clean = reason.replace("判断: ", "").replace("判断:", "").replace("理由: ", "").replace("理由:", "")
        if "判断:" in reason_clean:
            reason_clean = reason_clean.split("判断:")[-1].strip()
        reason_clean = reason_clean.replace("\n", " ").replace("\r", " ").strip()
        if len(reason_clean) > 200:
            reason_clean = reason_clean[:197] + "..."
        text_lines.append(f"MiMo: {reason_clean}")

        if data["formulas"]:
            text_lines.append(f"Formula ({len(data['formulas'])}):")
            for j, fm in enumerate(data["formulas"][:4]):
                fm_disp = fm['latex']
                text_lines.append(f"  [{j+1}] LaTeX: {fm_disp[:100]}")

        if data["text_before"]:
            ctx = data['text_before'][:120]
            text_lines.append(f"Context: {ctx}...")

        text = "\n".join(text_lines)
        text = text.replace("$", "\uff04")
        ax_text.text(0.02, 0.98, text, transform=ax_text.transAxes, fontsize=7.5,
                     fontfamily="sans-serif", va="top", ha="left",
                     bbox=dict(boxstyle="round,pad=0.5", facecolor="#f8f9fa",
                               edgecolor=JUDGMENT_COLORS.get(data["judgment"], "#ccc"),
                               linewidth=1.5))
        ax_text.set_xlim(0, 1)
        ax_text.set_ylim(0, 1)
        ax_text.axis("off")

    if output_path:
        fig.savefig(output_path, dpi=200, bbox_inches="tight", facecolor="white")
        print(f"  ✅ 画廊已保存: {output_path} ({output_path.stat().st_size / 1024:.0f} KB)")
    plt.close(fig)


def _format_item_md(data, rank_label):
    chunk_id = data["chunk_id"]
    doc_part = chunk_id.split("_chunk_")[0] if "_chunk_" in chunk_id else chunk_id[:30]
    reason = data.get("raw_response", "").replace("判断: ", "").replace("判断:", "").replace("理由: ", "").replace("理由:", "")
    if "判断:" in reason:
        reason = reason.split("判断:")[-1].strip()
    reason = reason.replace("\n", " ").replace("\r", " ").strip()
    if len(reason) > 300:
        reason = reason[:297] + "..."
    lines = [f"### #{rank_label}: {doc_part}", ""]
    lines.append(f"- **Chunk ID**: `{chunk_id}`")
    lines.append(f"- **判决**: {JUDGMENT_LABELS.get(data['judgment'], data['judgment'])}")
    lines.append(f"- **理由**: {reason}")
    if data["formulas"]:
        lines.append(f"- **公式 ({len(data['formulas'])} 个)**:")
        for fm in data["formulas"][:3]:
            lines.append(f"  - `{fm['latex'][:80]}`")
    lines.append("")
    return "\n".join(lines)


def generate_captions(gallery_best, gallery_worst, output_path, all_results=None):
    lines = []
    lines.append("# 跨模态对齐画廊 — 文字说明")
    lines.append("")
    lines.append("> 基于 MiMo-V2.5 视觉审计引擎对 9,227 条跨模态图片-公式共现项的判决结果，")
    lines.append("> 按对齐质量排序提取 Top 10 最佳和最差对。")
    lines.append("")
    lines.append(f"- **数据来源**: `benchmark/agent/results/visual_audit_results.jsonl` (9,227 条)")
    lines.append(f"- **视觉引擎**: MiMo-V2.5 (mimo-v2.5)")
    lines.append(f"- **审计方法**: 逐对判断图片内容与同 chunk LaTeX 公式的语义相关性")
    lines.append(f"- **画廊文件**:")
    lines.append(f"  - `docs/assets/alignment_gallery_best.png` — Top 10 最佳对齐")
    lines.append(f"  - `docs/assets/alignment_gallery_worst.png` — Top 10 最差对齐")
    lines.append("")

    lines.append("## 判决分布概览")
    lines.append("")
    lines.append("| 判决 | 数量 | 占比 |")
    lines.append("|:--|--:|--:|")
    if all_results is None:
        all_results = read_results()
    dist = Counter(r.get("judgment", "unknown") for r in all_results if "error" not in r)
    for j in ["consistent", "partially_consistent", "inconsistent", "uncertain"]:
        c = dist.get(j, 0)
        pct = c / len(all_results) * 100 if all_results else 0
        lines.append(f"| {JUDGMENT_LABELS.get(j, j)} | {c} | {pct:.1f}% |")
    lines.append("")

    lines.append("## Top 10 最佳对齐")
    lines.append("")
    for i, data in enumerate(gallery_best):
        lines.append(_format_item_md(data, i + 1))

    lines.append("## Top 10 最差对齐")
    lines.append("")
    for i, data in enumerate(gallery_worst):
        lines.append(_format_item_md(data, i + 1))

    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"  ✅ 说明文档已保存: {output_path}")


def main():
    print("=" * 64)
    print("  视觉审计 Top10 画廊生成器")
    print("=" * 64)

    print("\n[1/4] 读取审计结果...")
    results = read_results()
    print(f"  共读取 {len(results)} 条审计记录")

    print("\n[2/4] 准备 Top 10 最佳对齐...")
    gallery_best = prepare_gallery_data(results, mode="best")
    print(f"  提取 {len(gallery_best)} 个最佳对齐项")

    print("\n[3/4] 准备 Top 10 最差对齐...")
    gallery_worst = prepare_gallery_data(results, mode="worst")
    print(f"  提取 {len(gallery_worst)} 个最差对齐项")

    print("\n[4/4] 生成画廊图片...")
    best_path = ASSETS_DIR / "alignment_gallery_best.png"
    worst_path = ASSETS_DIR / "alignment_gallery_worst.png"

    print("  绘制最佳画廊...")
    draw_gallery(gallery_best, mode="best", output_path=best_path)
    print("  绘制最差画廊...")
    draw_gallery(gallery_worst, mode="worst", output_path=worst_path)

    captions_path = EVIDENCE_DIR / "alignment_gallery_captions.md"
    print("  生成说明文档...")
    generate_captions(gallery_best, gallery_worst, captions_path, all_results=results)

    print(f"\n{'=' * 64}")
    print(f"  产出文件:")
    print(f"    ✅ {best_path}")
    print(f"    ✅ {worst_path}")
    print(f"    ✅ {captions_path}")
    print(f"{'=' * 64}")


if __name__ == "__main__":
    main()
