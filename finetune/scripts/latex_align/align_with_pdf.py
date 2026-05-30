"""
三源对齐验证: LaTeX源码 ↔ MinerU MD ↔ PDF
验证 MinerU 从 PDF 中提取的公式是否与 LaTeX 源码一致，
以及 PDF 原始文本中是否包含这些公式（粗略验证）。

用法:
  conda run -n myenv python finetune/scripts/latex_align/align_with_pdf.py [arxiv_id]
  不传参则跑 5 篇全部
"""
import os, re, sys
from _formula_utils import (
    project_root, PAPERS, extract_latex_formulas, extract_md_display,
    fingerprint, jaccard, align_stats
)

LATEX_DIR = os.path.join(project_root(), "tmp", "latex_align")

def find_latex_for_arxiv(arxiv_id, label):
    paper_dir = os.path.join(LATEX_DIR, f"{arxiv_id}_{label}")
    if not os.path.isdir(paper_dir):
        return []
    formulas = []
    for root, dirs, files in os.walk(paper_dir):
        for f in files:
            if f.endswith('.tex'):
                formulas.extend(extract_latex_formulas(os.path.join(root, f)))
    return formulas

def find_md_for_arxiv(arxiv_id):
    proc_dir = os.path.join(project_root(), "data", "processed")
    for d in os.listdir(proc_dir):
        if d.startswith(arxiv_id):
            md_files = [f for f in os.listdir(os.path.join(proc_dir, d)) if f.endswith('.md')]
            if md_files:
                return extract_md_display(os.path.join(proc_dir, d, md_files[0]))
    return []

def extract_pdf_text_math(pdf_path):
    math_indicators = []
    try:
        import fitz
        doc = fitz.open(pdf_path)
        for page_num in range(min(len(doc), 5)):
            page = doc[page_num]
            text = page.get_text("text")
            lines = text.split('\n')
            for line in lines:
                stripped = line.strip()
                if not stripped:
                    continue
                math_score = 0
                if re.search(r'[∑∫∏∂∇∆∞∈∉⊂⊃∧∨¬∀∃⇒⇔]', stripped):
                    math_score += 3
                if re.search(r'[α-ωΑ-Ω]', stripped):
                    math_score += 2
                if stripped.count('=') >= 2:
                    math_score += 2
                if re.search(r'[a-zA-Z]\s*=\s*', stripped):
                    math_score += 1
                if re.search(r'\\[a-z]+', stripped):
                    math_score += 2
                if math_score >= 3:
                    math_indicators.append((page_num + 1, stripped[:200], math_score))
        doc.close()
        return math_indicators
    except ImportError:
        return [("N/A", "pymupdf (fitz) 未安装 — 跳过PDF文本提取", 0)]
    except Exception as e:
        return [("N/A", f"PDF读取失败: {e}", 0)]

def find_pdf_for_arxiv(arxiv_id):
    pdf_dir = os.path.join(project_root(), "data", "pdf", "arXiv")
    for f in os.listdir(pdf_dir):
        if f.startswith(arxiv_id) and f.endswith('.pdf'):
            return os.path.join(pdf_dir, f)
    return None

arxiv_filter = sys.argv[1] if len(sys.argv) > 1 else None

for arxiv_id, label in PAPERS:
    if arxiv_filter and arxiv_id != arxiv_filter:
        continue

    print(f"\n{'='*70}")
    print(f"三源对齐: {arxiv_id} ({label})")
    print('='*70)

    latex_fm = find_latex_for_arxiv(arxiv_id, label)
    print(f"  源1 (LaTeX源码): {len(latex_fm)} 展示公式")

    md_fm = find_md_for_arxiv(arxiv_id)
    print(f"  源2 (MinerU MD): {len(md_fm)} 展示公式")

    has_fitz = False
    pdf_math = []
    pdf_path = find_pdf_for_arxiv(arxiv_id)
    if pdf_path:
        pdf_math = extract_pdf_text_math(pdf_path)
        has_fitz = pdf_math and pdf_math[0][0] != "N/A"
        if has_fitz:
            print(f"  源3 (PDF文本): {len(pdf_math)} 数学表达式块")
        else:
            print(f"  源3 (PDF文本): {pdf_math[0][1] if pdf_math else '未知错误'}")
    else:
        print(f"  源3 (PDF文本): [WARN] PDF文件未找到")

    l2m, m2l = align_stats(latex_fm, md_fm)

    print(f"\n  --- 双向对齐 ---")
    print(f"  LaTeX -> MinerU: {l2m}/{len(latex_fm)} = {l2m/len(latex_fm)*100:.1f}%" if latex_fm else "  LaTeX -> MinerU: 0/0")
    print(f"  MinerU -> LaTeX: {m2l}/{len(md_fm)} = {m2l/len(md_fm)*100:.1f}%" if md_fm else "  MinerU -> LaTeX: 0/0")

    if pdf_math and has_fitz:
        pdf_fp = [fingerprint(t[1]) for t in pdf_math]
        l2p = sum(1 for l in latex_fm if any(jaccard(fingerprint(l), p) >= 0.3 for p in pdf_fp))
        m2p = sum(1 for m in md_fm if any(jaccard(fingerprint(m), p) >= 0.3 for p in pdf_fp))
        print(f"  LaTeX -> PDF:   {l2p}/{len(latex_fm)} = {l2p/len(latex_fm)*100:.1f}%" if latex_fm else "  LaTeX -> PDF:   0/0")
        print(f"  MinerU -> PDF:  {m2p}/{len(md_fm)} = {m2p/len(md_fm)*100:.1f}%" if md_fm else "  MinerU -> PDF:  0/0")

        if pdf_math:
            print(f"\n  PDF数学块样例 (前3条):")
            for page, text, score in pdf_math[:3]:
                preview = re.sub(r'\s+', ' ', text)[:100]
                print(f"    P{page} [score={score}]: {preview}")
    else:
        print(f"\n  PDF文本: 跳过 — 需要安装 pymupdf (pip install PyMuPDF)")

    print(f"\n  --- 结论 ---")
    if l2m / max(len(latex_fm), 1) >= 0.7:
        print(f"  ✅ LaTeX↔MinerU 对齐良好")
    elif l2m / max(len(latex_fm), 1) >= 0.5:
        print(f"  ⚠️ LaTeX↔MinerU 部分对齐")
    else:
        print(f"  ❌ LaTeX↔MinerU 对齐不足 (检测到模板稀释或多文件结构)")

print(f"\n{'='*70}")
print("注意: PDF文本提取是粗略验证，仅提取每页前5页的文本块。")
print("如需精确验证，建议: pip install PyMuPDF")
