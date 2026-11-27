"""Figures for the PLOS One research-blog post (plosone-animalia-naming).
Source: Nojiri, Inoshita, Sugeno, Taga (2026), PLOS One 21(7): e0353612,
doi:10.1371/journal.pone.0353612 (CC BY 4.0).

- pipeline.png, validation.png, arthropoda-share.png are drawn here; every number is
  copied from the Materials and methods / Discussion text of the article.
- paper-fig1/3/5/6/7.png are the article's own figures (CC BY), extracted unchanged
  from the published PDF and only resized.
"""
import os
import subprocess
import tempfile
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
from PIL import Image

OUT = "/Users/ishitatakashishou/Sites/affectosphere-lab/public/column-images/plosone-animalia-naming/"
PDF = "/Users/ishitatakashishou/Downloads/journal.pone.0353612.pdf"
os.makedirs(OUT, exist_ok=True)
AMBER, STEEL, GREY, LIGHT, INK = "#C4974A", "#3D6B8C", "#9AA0A6", "#D9D4CB", "#1A1A1A"
plt.rcParams.update({
    "font.family": "Arial", "font.size": 11, "axes.edgecolor": "#444",
    "axes.linewidth": 0.8, "axes.spines.top": False, "axes.spines.right": False,
    "xtick.color": "#333", "ytick.color": "#333", "axes.labelcolor": "#222",
    "savefig.dpi": 220, "savefig.bbox": "tight", "savefig.facecolor": "white",
})


def save(fig, name):
    fig.savefig(OUT + name)
    plt.close(fig)


# 1. Pipeline (Materials and methods, sections a-e).
fig, ax = plt.subplots(figsize=(8.8, 3.1))
ax.set_xlim(0, 100); ax.set_ylim(0, 32); ax.axis("off")
boxes = [
    (1, "1. Category design", "Spider dataset\n(48,464 epithets)\nembedding + K-means\n→ 7 clusters\n→ 6 naming categories", LIGHT),
    (26, "2. LLM labeling", "All valid Animalia\nnames (Catalogue of Life)\nGPT-4.1-mini, temp. 0\nmulti-label, 6 categories", AMBER),
    (51, "3. Validation", "240 stratified epithets\nchecked against original\ndescriptions\n→ merge morphology\n→ 4 categories", "#C9D7E3"),
    (76, "4. Analyses", "Annual counts\nquasibinomial GAMs\nphylum heatmap\nauthor-region heatmap\n(name-based inference)", LIGHT),
]
for x, head, body, c in boxes:
    ax.add_patch(FancyBboxPatch((x, 2), 22, 26, boxstyle="round,pad=0.4,rounding_size=1.2",
                                fc=c, ec="#555", lw=0.8))
    ax.text(x + 11, 25, head, ha="center", va="center", fontsize=11, weight="bold", color=INK)
    ax.text(x + 11, 13, body, ha="center", va="center", fontsize=8.6, color="#222", linespacing=1.35)
for x in (23.6, 48.6, 73.6):
    ax.annotate("", (x + 2.2, 15), (x, 15), arrowprops=dict(arrowstyle="-|>", color="#555", lw=1.1))
save(fig, "pipeline.png")

# 2. Validation agreement (Materials and methods (c); S2 Table values quoted in the text).
labels = ["Six categories\n(pooled agreement)", "Morphology only\n(3 sub-categories merged)", "Four categories\n(pooled agreement)"]
vals = [76.7, 93.3, 86.7]
cols = [GREY, STEEL, AMBER]
fig, ax = plt.subplots(figsize=(6.8, 3.2))
ax.bar(range(3), vals, color=cols, width=.58)
for i, v in enumerate(vals):
    ax.text(i, v + 1.5, f"{v:.1f}%", ha="center", fontsize=10.5)
ax.set_xticks(range(3), labels)
ax.set_ylim(0, 105)
ax.set_ylabel("Agreement with manual labels (%)")
save(fig, "validation.png")

# 3. Arthropoda share of the dataset (Discussion (b)): 1,193,760 of 1,538,390 species.
arth, total = 1_193_760, 1_538_390
fig, ax = plt.subplots(figsize=(7.2, 1.6))
ax.barh([0], [arth], color=AMBER, height=.5)
ax.barh([0], [total - arth], left=[arth], color=LIGHT, height=.5)
ax.text(arth / 2, 0, f"Arthropoda\n1,193,760 species", ha="center", va="center", fontsize=10, color=INK)
ax.text(arth + (total - arth) / 2, 0, f"Other phyla\n{total - arth:,}", ha="center", va="center", fontsize=9.5, color=INK)
ax.set_yticks([])
ax.spines["left"].set_visible(False)
ax.set_xlim(0, total)
ax.set_xticks([0, 500_000, 1_000_000, total], ["0", "500k", "1M", "1,538,390"])
ax.set_xlabel("Species in the analysed Animalia dataset")
save(fig, "arthropoda-share.png")

# 4. The article's own figures (CC BY), extracted from the PDF and resized.
#    pdfimages order: image 2 = Fig 1, 3 = Fig 2, 4 = Fig 3, 5 = Fig 4, 6 = Fig 5, 7 = Fig 6, 8 = Fig 7.
keep = {2: "paper-fig1.png", 4: "paper-fig3.png", 6: "paper-fig5.png", 7: "paper-fig6.png", 8: "paper-fig7.png"}
with tempfile.TemporaryDirectory() as tmp:
    subprocess.run(["pdfimages", "-png", PDF, os.path.join(tmp, "f")], check=True)
    for idx, name in keep.items():
        im = Image.open(os.path.join(tmp, f"f-{idx:03d}.png")).convert("RGB")
        im.thumbnail((1600, 2000))
        im.save(OUT + name, optimize=True)
print("done")
