"""Figures for the Journal of Plankton Research research-blog post (jpr-zooplankton-etymology).
Source: Sugeno et al. (2026), "Applying large language models to expert-based etymological
classification in zooplankton", J. Plankton Res. 48(5), fbag061, doi:10.1093/plankt/fbag061
(published article: Methods text, Results text and Table I).
The cross-taxon figure also uses Table 1 of Nojiri, Inoshita, Sugeno (2025),
Zoological Science 42(5), doi:10.2108/zs250025. Nothing is recomputed."""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
import numpy as np

OUT = "/Users/ishitatakashishou/Sites/affectosphere-lab/public/column-images/jpr-zooplankton-etymology/"
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


# 1. Pipeline (Methods text).
fig, ax = plt.subplots(figsize=(8.6, 2.9))
ax.set_xlim(0, 100); ax.set_ylim(0, 30); ax.axis("off")
boxes = [
    (1, "Expert labels", "Macêdo et al. (2023)\nrotifers and\nmicrocrustaceans\n1758–2021\n989 species", LIGHT),
    (26, "LLM labeling", "GPT-4o-mini\n(OpenAI API)\ntemperature 0\nfew-shot prompt\n5 categories", AMBER),
    (51, "Agreement", "Confusion matrix\naccuracy, Cohen's κ\nprecision / recall / F1\nχ² + standardized\nresiduals", "#C9D7E3"),
    (76, "Trends", "Quasi-Poisson GAMs\nyearly and decadal\ncounts\nexpert vs. LLM\ncurves compared", LIGHT),
]
for x, head, body, c in boxes:
    ax.add_patch(FancyBboxPatch((x, 3), 22, 22, boxstyle="round,pad=0.4,rounding_size=1.2",
                                fc=c, ec="#555", lw=0.8))
    ax.text(x + 11, 22, head, ha="center", va="center", fontsize=11, weight="bold", color=INK)
    ax.text(x + 11, 12, body, ha="center", va="center", fontsize=8.6, color="#222", linespacing=1.35)
for x in (23.6, 48.6, 73.6):
    ax.annotate("", (x + 2.2, 14), (x, 14), arrowprops=dict(arrowstyle="-|>", color="#555", lw=1.1))
save(fig, "pipeline.png")

# 2. Precision / recall / F1 by category (Table I).
cats = ["Morphology", "Ecology &\nBehavior", "Geography", "People", "Culture"]
rec = [.87, .52, .91, .86, .64]
prec = [.97, .75, .76, .97, .12]
f1 = [.92, .62, .83, .91, .20]
x = np.arange(len(cats)); w = .26
fig, ax = plt.subplots(figsize=(7.4, 3.5))
ax.bar(x - w, prec, w, color=LIGHT, label="Precision")
ax.bar(x, rec, w, color=GREY, label="Recall")
ax.bar(x + w, f1, w, color=AMBER, label="F1")
for xi, v in zip(x, f1):
    ax.text(xi + w, v + .02, f"{v:.2f}", ha="center", fontsize=9, color="#7B5E28")
ax.set_xticks(x, cats)
ax.set_ylim(0, 1.08)
ax.set_ylabel("Score (LLM vs. expert labels)")
ax.legend(frameon=False, ncol=3, loc="upper center", bbox_to_anchor=(.5, 1.13))
save(fig, "prf1.png")

# 3. Precision vs. recall (Table I): Culture is the outlier.
fig, ax = plt.subplots(figsize=(5.6, 4.4))
for c, p, r in zip(cats, prec, rec):
    col = STEEL if c == "Culture" else AMBER
    ax.plot(r, p, "o", color=col, ms=10)
    lab = c.replace("\n", " ")
    off = {"Morphology": (-.02, .035, "right"), "People": (.02, -.06, "left"),
           "Geography": (.02, -.06, "right"), "Ecology & Behavior": (.025, 0, "left"),
           "Culture": (.025, .01, "left")}[lab]
    ax.text(r + off[0], p + off[1], lab, ha=off[2], va="center", fontsize=10)
ax.plot([0, 1], [0, 1], color=LIGHT, lw=1, ls="--")
ax.set_xlim(0, 1.05); ax.set_ylim(0, 1.05)
ax.set_xlabel("Recall")
ax.set_ylabel("Precision")
ax.text(.66, .2, "Culture: many names labelled\nCulture by the LLM were\nnot Culture for experts", fontsize=9, color=STEEL)
save(fig, "precision-recall.png")

# 4. F1 across taxa for the categories shared by both studies.
#    Zooplankton: Table I of this paper. Phytophagous arthropods: Table 1 of the Zoological Science paper (%, /100).
shared = ["Morphology", "Ecology & Behavior", "Geography", "People"]
zoo = [.92, .62, .83, .91]
phy = [.826, .317, .758, .800]
x = np.arange(4); w = .36
fig, ax = plt.subplots(figsize=(7.2, 3.3))
ax.bar(x - w/2, phy, w, color=GREY, label="Phytophagous arthropods (Zoological Science, 2025)")
ax.bar(x + w/2, zoo, w, color=AMBER, label="Zooplankton (this paper)")
for xi, a, b in zip(x, phy, zoo):
    ax.text(xi - w/2, a + .02, f"{a:.2f}", ha="center", fontsize=9)
    ax.text(xi + w/2, b + .02, f"{b:.2f}", ha="center", fontsize=9)
ax.set_xticks(x, ["Morphology", "Ecology &\nBehavior", "Geography", "People"])
ax.set_ylim(0, 1.15)
ax.set_ylabel("F1 (LLM vs. human labels)")
ax.legend(frameon=False, loc="upper center", bbox_to_anchor=(.5, 1.16), ncol=1, fontsize=9.5)
save(fig, "cross-taxa-f1.png")
print("done")
