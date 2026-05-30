"""
提取 LaTeX 源码和 MinerU 解析 Markdown 中的公式，做对齐验证
用法: conda run -n myenv python finetune/scripts/latex_align/extract_formulas.py
"""
import os, re, json
from _formula_utils import (
    project_root, PAPERS, extract_latex_formulas, extract_md_all,
    fingerprint, jaccard as jaccard_similarity, find_best_match
)

LATEX_DIR = os.path.join(project_root(), "tmp", "latex_align")

def find_processed_dir(arxiv_id):
    data_proc = os.path.join(project_root(), "data", "processed")
    for d in os.listdir(data_proc):
        if d.startswith(arxiv_id):
            return os.path.join(data_proc, d)
    return None

def find_latex_tex(arxiv_id, label):
    paper_dir = os.path.join(LATEX_DIR, f"{arxiv_id}_{label}")
    if not os.path.isdir(paper_dir):
        return []
    tex_files = []
    for root, dirs, files in os.walk(paper_dir):
        for f in files:
            if f.endswith('.tex') and not f.startswith('.'):
                tex_files.append(os.path.join(root, f))
    return tex_files

def normalize_formula(formula):
    s = re.sub(r'\s+', ' ', formula).strip()
    s = re.sub(r'\\label\{[^}]*\}', '', s)
    s = re.sub(r'\\tag\{[^}]*\}', '', s)
    s = re.sub(r'\\nonumber', '', s)
    s = re.sub(r'\\notag', '', s)
    s = re.sub(r'(?<!\\)\n', '', s)
    s = re.sub(r'\s+', ' ', s).strip()
    return s

results = {}
for arxiv_id, label in PAPERS:
    print(f"\n{'='*60}")
    print(f"论文: {arxiv_id} ({label})")
    print('='*60)

    tex_files = find_latex_tex(arxiv_id, label)
    print(f"  LaTeX文件数: {len(tex_files)}")

    all_latex_fm = []
    for tf in tex_files:
        fm = [(('display_bracket' if False else 'display'), f) for f in extract_latex_formulas(tf)]
        rel_path = os.path.relpath(tf, os.path.join(LATEX_DIR, f"{arxiv_id}_{label}"))
        print(f"    {rel_path}: {len(fm)} 公式")
        all_latex_fm.extend(fm)

    print(f"  LaTeX公式总数: {len(all_latex_fm)}")

    proc_dir = find_processed_dir(arxiv_id)
    md_formulas = []
    if proc_dir:
        md_files = [f for f in os.listdir(proc_dir) if f.endswith('.md')]
        if md_files:
            md_path = os.path.join(proc_dir, md_files[0])
            md_formulas = extract_md_all(md_path)
            print(f"  MinerU MD: {md_files[0]} -> {len(md_formulas)} 公式")
        else:
            print(f"  MinerU MD: [WARN] 未找到 .md 文件")
    else:
        print(f"  MinerU MD: [WARN] 未找到 processed 目录")

    latex_display = [fc for _, fc in all_latex_fm]
    md_display = [fc for ft, fc in md_formulas if ft != 'inline']

    print(f"\n  --- 对齐分析 ---")
    print(f"  LaTeX展示公式: {len(latex_display)}")
    print(f"  MinerU展示公式: {len(md_display)}")

    aligned = 0
    aligned_details = []
    remaining_md = list(range(len(md_display)))
    for i, lf in enumerate(latex_display):
        lf_fp = fingerprint(lf)
        candidates = [md_display[j] for j in remaining_md]
        best_idx, best_score = find_best_match(lf_fp, candidates)
        if best_score >= 0.3 and best_idx >= 0:
            aligned += 1
            aligned_details.append({
                'idx': i, 'score': round(best_score, 3),
                'md_idx': remaining_md[best_idx],
                'latex_preview': normalize_formula(lf)[:80],
                'md_preview': normalize_formula(md_display[remaining_md[best_idx]])[:80],
            })
            del remaining_md[best_idx]

    alignment_rate = aligned / len(latex_display) * 100 if latex_display else 0

    print(f"\n  对齐率: {aligned}/{len(latex_display)} = {alignment_rate:.1f}%")

    mismatches_shown = 0
    print(f"\n  典型匹配示例 (score >= 0.5):")
    for ad in aligned_details:
        if ad['score'] >= 0.5 and mismatches_shown < 3:
            print(f"    [score={ad['score']}] LaTeX: {ad['latex_preview'][:60]}...")
            print(f"                    MinerU: {ad['md_preview'][:60]}...")
            mismatches_shown += 1

    results[arxiv_id] = {
        'label': label, 'tex_files': len(tex_files),
        'latex_formulas_total': len(all_latex_fm),
        'latex_display_formulas': len(latex_display),
        'md_formulas_total': len(md_formulas),
        'md_display_formulas': len(md_display),
        'aligned': aligned, 'alignment_rate': round(alignment_rate, 1),
    }

print(f"\n{'='*60}")
print("最终对齐报告:")
print(f"{'='*60}")
print(f"{'arXiv ID':<16} {'标签':<20} {'LaTeX公式':<10} {'MinerU公式':<10} {'对齐率':<10}")
print('-'*66)
for arxiv_id, info in results.items():
    print(f"{arxiv_id:<16} {info['label']:<20} {info['latex_display_formulas']:<10} {info['md_display_formulas']:<10} {info['alignment_rate']:<10}%")

report_path = os.path.join(LATEX_DIR, "alignment_report.json")
with open(report_path, 'w', encoding='utf-8') as f:
    json.dump(results, f, indent=2, ensure_ascii=False)
print(f"\n报告保存: {report_path}")
