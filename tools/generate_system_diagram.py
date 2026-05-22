import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np

OUTPUT = r"d:\WorkPlace\AI\MinerU-public-release\docs\submissions\shared\assets\system_architecture.png"

plt.rcParams.update({
    'font.family': 'sans-serif',
    'font.sans-serif': ['Microsoft YaHei', 'DejaVu Sans'],
    'font.size': 10,
})

fig, ax = plt.subplots(1, 1, figsize=(20, 14))
ax.set_xlim(0, 20)
ax.set_ylim(0, 14)
ax.set_aspect('auto')
ax.axis('off')

BG = '#0B1120'
CARD_BG = '#111B2E'
BORDER = '#1E3A5F'
ACCENT_ORANGE = '#F59E0B'
ACCENT_BLUE = '#3B82F6'
ACCENT_GREEN = '#10B981'
ACCENT_PURPLE = '#8B5CF6'
ACCENT_RED = '#EF4444'
TEXT_WHITE = '#F1F5F9'
TEXT_GRAY = '#94A3B8'
CHUNK_GREEN = '#059669'
DOC_BLUE = '#2563EB'

fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)


def draw_card(cx, cy, w, h, color, border_color=None, radius=0.3):
    box = FancyBboxPatch((cx - w/2, cy - h/2), w, h,
                         boxstyle=f"round,pad=0,rounding_size={radius}",
                         facecolor=color, edgecolor=border_color or color,
                         linewidth=1.5, zorder=2)
    ax.add_patch(box)


def draw_icon(cx, cy, icon_type, size=0.35, zorder=10):
    if icon_type == 'github':
        path_data = [
            (np.array([-1, -1, -0.55, -1, -1, -0.55, -0.55, 0, 0.55, 0.55, 1, 1, 0.55, 1, 1, 0.55, 0.55, 0, -0.55]),
             np.array([-0.5, -0.8, -0.8, -1, -0.8, -0.5, -0.2, 0, -0.2, -0.5, -0.8, -1, -1.2, -1.2, -1, -0.7, -1, -1, -1])),
        ]
        for xp, yp in path_data:
            ax.fill(cx + xp * size * 0.5, cy + yp * size * 0.5, color=TEXT_WHITE, zorder=zorder, alpha=0.9)
    elif icon_type == 'hf':
        ax.text(cx, cy, '\uD83E\uDD17', fontsize=size * 24, ha='center', va='center', zorder=zorder)
    elif icon_type == 'demo':
        ax.plot(cx, cy, 'o', color=ACCENT_GREEN, markersize=size * 10, zorder=zorder, alpha=0.8)
        ax.text(cx, cy, '\u25B6', fontsize=size * 14, ha='center', va='center', zorder=zorder+1, color='white')


def draw_arrow(x1, y1, x2, y2, color=TEXT_GRAY, lw=1.5, zorder=1, style='simple'):
    ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle='->', color=color, lw=lw,
                                connectionstyle='arc3,rad=0'), zorder=zorder)


fig.text(10, 13.55, 'CONTROLMIND  —  Cross-Track Unified Architecture', ha='center', va='center',
         fontsize=20, fontweight='bold', color=TEXT_WHITE, zorder=20)
fig.text(10, 13.10, 'One Corpus · Three Tracks · Full Reproducibility   |   CC-BY-4.0', ha='center', va='center',
         fontsize=11, color=TEXT_GRAY, zorder=20)

# ── TOP: Cross-cutting findings bar ──
findings_y = 12.35
bar_w, bar_h = 18.5, 0.9
bar = FancyBboxPatch((10 - bar_w/2, findings_y - bar_h/2), bar_w, bar_h,
                     boxstyle="round,pad=0,rounding_size=0.25",
                     facecolor='#1A2740', edgecolor='#2D4A6F', linewidth=1.5, zorder=2)
ax.add_patch(bar)
ax.text(10, findings_y + 0.38, 'CROSS-CUTTING FINDINGS', ha='center', va='center',
        fontsize=8, color=TEXT_GRAY, fontweight='bold', zorder=3, alpha=0.7)
findings = ['PPL Paradox', 'Anti-Scaling Law', 'Vision Injection', 'QLoRA Cross-Arch', 'Fleiss\' \u03BA=0.575']
for i, f in enumerate(findings):
    fx = 3.5 + i * 3.4
    ax.text(fx, findings_y + 0.02, f, ha='center', va='center', fontsize=10,
            color=ACCENT_ORANGE, fontweight='bold', zorder=3)

# ── TRACK CARDS ──
track_y = 10.1
track_w, track_h = 5.4, 3.8
tracks = [
    {'x': 3.7, 'color': '#1A2740', 'border': ACCENT_BLUE, 'title': 'TRACK 1 — Sci-Align',
     'sub': '4-Dimension Benchmark', 'items': [
         ('500 Questions', 'A/B/C/D balanced'),
         ('9-Model Leaderboard', 'MiMo-v2-flash 0.647'),
         ('CC-BY-4.0 \u00B7 HuggingFace', 'core.json 1.1 MB'),
         ('Fleiss\' \u03BA=0.575', '14-Entity Judge Matrix'),
     ], 'icons': ['hf']},
    {'x': 10, 'color': '#1A2740', 'border': ACCENT_PURPLE, 'title': 'TRACK 2 — Data Agent',
     'sub': '14-Intent Autonomous Agent', 'items': [
         ('14 Intent Registry', '8-dim validation'),
         ('391s D-Flywheel Loop', 'arXiv \u2192 Parse \u2192 Chunk'),
         ('Self-Correction 50%', '\u0394 +0.352 mean score'),
         ('4-Path Scheduling', 'API / Ollama / vLLM / Script'),
     ], 'icons': ['github']},
    {'x': 16.3, 'color': '#1A2740', 'border': ACCENT_GREEN, 'title': 'TRACK 3 — Medical RAG',
     'sub': 'Evidence-Grounded Clinical QA', 'items': [
         ('97 PMC Papers', '3,348 Medical Chunks'),
         ('MedBench 630 Q', 'VLM EI 4.33%'),
         ('Vision Injection 8/8', 'Text-only 0/8 \u2192 Full 8/8'),
         ('Hybrid FAISS+BM25', 'IMRAD-aware Chunking'),
     ], 'icons': ['demo']},
]

for tk in tracks:
    cx, cy = tk['x'], track_y
    draw_card(cx, cy, track_w, track_h, tk['color'], tk['border'])
    ax.text(cx, cy + track_h/2 - 0.45, tk['title'], ha='center', va='center',
            fontsize=12, fontweight='bold', color=tk['border'], zorder=5)
    ax.text(cx, cy + track_h/2 - 0.9, tk['sub'], ha='center', va='center',
            fontsize=8, color=TEXT_GRAY, zorder=5)
    for j, (label, detail) in enumerate(tk['items']):
        iy = cy + track_h/2 - 1.4 - j * 0.65
        ax.text(cx - track_w/2 + 0.5, iy, label, ha='left', va='center',
                fontsize=9, color=TEXT_WHITE, fontweight='bold', zorder=5)
        ax.text(cx - track_w/2 + 0.5, iy - 0.28, detail, ha='left', va='center',
                fontsize=7.5, color=TEXT_GRAY, zorder=5)
    if 'icons' in tk:
        icon_x = cx + track_w/2 - 0.8
        icon_base_y = cy - track_h/2 + 0.6
        for idx, it in enumerate(tk['icons']):
            ix = icon_x
            iy = icon_base_y + idx * 1.0
            if it == 'hf':
                ax.text(ix, iy, 'HF', fontsize=9, ha='center', va='center', zorder=10,
                        color=ACCENT_ORANGE, fontweight='bold')
            elif it == 'github':
                ax.text(ix, iy, 'GH', fontsize=9, ha='center', va='center', zorder=10,
                        color=ACCENT_BLUE, fontweight='bold')
            elif it == 'demo':
                ax.text(ix, iy, 'DEMO', fontsize=8, ha='center', va='center', zorder=10,
                        color=ACCENT_GREEN, fontweight='bold')

# ── Linking arrows: tracks <-> chunks ──
for tk in tracks:
    draw_arrow(tk['x'], track_y - track_h/2, tk['x'], 7.85, color='#334155', lw=1.2)

# ── CHUNK LAYER ──
chunk_y = 6.8
draw_card(10, chunk_y, 17.5, 1.6, '#0F2027', CHUNK_GREEN)
ax.text(10, chunk_y + 0.45, '28,514 STRUCTURED CHUNKS', ha='center', va='center',
        fontsize=14, fontweight='bold', color=CHUNK_GREEN, zorder=5)
chunk_details = 'LaTeX Formulas 253,012   \u00B7   Image-Formula Pairs 4,996   \u00B7   23 Textbooks + 339 arXiv Papers   \u00B7   corpus/chunks/ on GitHub'
ax.text(10, chunk_y - 0.1, chunk_details, ha='center', va='center',
        fontsize=8.5, color=TEXT_GRAY, zorder=5)

# ── DOC LAYER ──
doc_y = 4.6
draw_card(10, doc_y, 17.5, 1.4, '#0A1628', DOC_BLUE)
ax.text(10, doc_y + 0.35, '362 DOCUMENTS  via  MinerU', ha='center', va='center',
        fontsize=14, fontweight='bold', color=DOC_BLUE, zorder=5)
ax.text(10, doc_y - 0.15, '23 Control Textbooks (ZIP Encoding, Calabi-Yau)  +  339 arXiv Papers (MPC, CBF, Adaptive, Robust, Nonlinear)',
        ha='center', va='center', fontsize=8.5, color=TEXT_GRAY, zorder=5)

# ── Arrows: docs -> chunks ──
draw_arrow(10, doc_y + 0.7, 10, chunk_y - 0.8, color=DOC_BLUE, lw=2.0)

# ── PUBLIC LINKS BAR (bottom) ──
link_y = 2.3
links = [
    ('GitHub', 'github.com/MorningStar0709/control-sci', ACCENT_BLUE),
    ('HuggingFace', 'huggingface.co/datasets/MorningStar0709/control-sci-corpus', ACCENT_ORANGE),
    ('Live Demo', 'demo.askiler.com  (code: ControlMind@2026)', ACCENT_GREEN),
]
for i, (label, url, color) in enumerate(links):
    lx = 3.5 + i * 6.5
    draw_card(lx, link_y, 5.8, 1.4, '#111B2E', color)
    ax.text(lx, link_y + 0.3, label, ha='center', va='center', fontsize=11,
            fontweight='bold', color=color, zorder=5)
    ax.text(lx, link_y - 0.25, url, ha='center', va='center', fontsize=7.5, color=TEXT_GRAY, zorder=5)

# ── LICENSE BAR ──
ax.text(10, 1.0, 'CC-BY-4.0  |  Full Reproducibility  |  DATA-TRACE Auditable  |  Single RTX 5090',
        ha='center', va='center', fontsize=9, color=TEXT_GRAY, zorder=5)

fig.savefig(OUTPUT, dpi=200, facecolor=BG, edgecolor='none', bbox_inches='tight', pad_inches=0.5)
plt.close()
print(f"Saved: {OUTPUT}")
print(f"  dpi=200, size={OUTPUT}")
