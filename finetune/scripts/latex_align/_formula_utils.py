"""
共享工具: LaTeX公式提取 + Jaccard指纹匹配
供 latex_align/ 下所有脚本 import 使用
"""
import os, re
from pathlib import Path

def project_root():
    return Path(__file__).resolve().parents[3]

def extract_latex_formulas(tex_path):
    with open(tex_path, 'r', encoding='utf-8', errors='replace') as f:
        content = f.read()
    content = re.sub(r'(?<!\\)%.*', '', content)
    formulas = []
    for m in re.finditer(r'\\\[(.*?)\\\]', content, re.DOTALL):
        formulas.append(m.group(1).strip())
    for m in re.finditer(r'\$\$(.*?)\$\$', content, re.DOTALL):
        formulas.append(m.group(1).strip())
    env_pat = re.compile(
        r'\\begin\{((?:equation|align|gather|multline|flalign|eqnarray)\**)\}(.*?)\\end\{\1\}',
        re.DOTALL
    )
    for m in env_pat.finditer(content):
        formulas.append(m.group(2).strip())
    return formulas

def extract_md_display(md_path):
    with open(md_path, 'r', encoding='utf-8', errors='replace') as f:
        content = f.read()
    return [m.group(1).strip() for m in re.finditer(r'\$\$(.*?)\$\$', content, re.DOTALL)]

def extract_md_all(md_path):
    with open(md_path, 'r', encoding='utf-8', errors='replace') as f:
        content = f.read()
    formulas = []
    for m in re.finditer(r'\$\$(.*?)\$\$', content, re.DOTALL):
        formulas.append(('display_dollar', m.group(1).strip()))
    for m in re.finditer(r'(?<!\$)\$(?!\$)(.+?)(?<!\$)\$(?!\$)', content):
        formulas.append(('inline', m.group(1).strip()))
    return formulas

def fingerprint(s):
    s = re.sub(r'\s+', ' ', s).strip()
    s = re.sub(r'\\label\{[^}]*\}', '', s)
    s = re.sub(r'\\tag\{[^}]*\}', '', s)
    s = re.sub(r'\\nonumber', '', s)
    s = re.sub(r'\\notag', '', s)
    s = s.lower()
    s = re.sub(r'\\[a-z]+', '', s)
    s = re.sub(r'[^a-z0-9]', ' ', s)
    return ' '.join(sorted(set(s.split()))[:20])

def jaccard(a, b):
    a, b = set(a.split()), set(b.split())
    if not a or not b:
        return 0.0
    return len(a & b) / len(a | b)

def find_best_match(fp, candidates, threshold=0.3):
    best_score = 0.0
    best_idx = -1
    for i, c in enumerate(candidates):
        c_fp = fingerprint(c) if isinstance(c, str) else fingerprint(c[1])
        score = jaccard(fp, c_fp)
        if score > best_score:
            best_score = score
            best_idx = i
    return best_idx, best_score

def align_stats(latex_fm, md_fm):
    lf_fp = [fingerprint(f) for f in latex_fm]
    mf_fp = [fingerprint(f) for f in md_fm]
    l2m = sum(1 for l in lf_fp if any(jaccard(l, m) >= 0.3 for m in mf_fp))
    m2l = sum(1 for m in mf_fp if any(jaccard(m, l) >= 0.3 for l in lf_fp))
    return l2m, m2l

PAPERS = [
    ("2202.13453", "Fourier_Hermite_DP"),
    ("2204.06207", "Safe_Stochastic_MPC"),
    ("2205.02881", "Region_free_MPC"),
    ("2205.12632", "Robust_DDP"),
    ("2206.07915", "Barrier_Safety_SOS"),
]
