"""找出采样中最长的论文。"""
from pypdf import PdfReader
from pathlib import Path
import os

d = Path(__file__).resolve().parent.parent / "data" / "pdf" / "arXiv"
pdfs = sorted(d.glob("*.pdf"))
sample = pdfs[:50]

pages = []
for p in sample:
    r = PdfReader(str(p))
    pages.append((len(r.pages), p.name))

pages.sort(key=lambda x: -x[0])
print("Top 3 longest papers in sample:")
for n, name in pages[:3]:
    print(f"  {n:3d} pages  {name}")
