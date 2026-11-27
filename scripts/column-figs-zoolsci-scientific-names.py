"""Figures for the Zoological Science research-blog post (zoolsci-scientific-names).
Every number is copied from the published article (Nojiri, Inoshita, Sugeno 2025,
Zoological Science 42(5), doi:10.2108/zs250025): Table 1 and the Results text.
Nothing is recomputed from data."""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
import numpy as np

OUT = "/Users/ishitatakashishou/Sites/affectosphere-lab/public/column-images/zoolsci-scientific-names/"
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


# 1. Study pipeline (Materials and Methods text; no numbers beyond those stated there).
fig, ax = plt.subplots(figsize=(8.6, 2.9))
ax.set_xlim(0, 100); ax.set_ylim(0, 30); ax.axis("off")
boxes = [
    (1, "Dataset", "Heard et al. (2023)\n2,709 species\n(4 without year removed\n→ 2,705 analysed)", LIGHT),
    (26, "Categories", "7 original labels\nmerged into 6:\nMorphology, Host,\nGeography, Ecology &\nBehavior, People, Other", LIGHT),
    (51, "LLM labeling", "GPT-4o mini\n(OpenAI API)\nprompt of Inoshita\net al. (2025)\n+ few-shot examples", AMBER),
    (76, "Comparison", "Accuracy, Precision,\nRecall, F1\nCohen's κ, MAE\nGAM of temporal\ntrends (quasibinomial)", "#C9D7E3"),
]
for x, head, body, c in boxes:
    ax.add_patch(FancyBboxPatch((x, 3), 22, 22, boxstyle="round,pad=0.4,rounding_size=1.2",
                                fc=c, ec="#555", lw=0.8))
    ax.text(x + 11, 22, head, ha="center", va="center", fontsize=11, weight="bold", color=INK)
    ax.text(x + 11, 12.5, body, ha="center", va="center", fontsize=8.6, color="#222", linespacing=1.35)
for x in (23.6, 48.6, 73.6):
    ax.annotate("", (x + 2.2, 14), (x, 14), arrowprops=dict(arrowstyle="-|>", color="#555", lw=1.1))
save(fig, "pipeline.png")

# 2. Precision / recall / F1 by category (Table 1).
cats = ["Morphology", "Host", "Geography", "Ecology &\nBehavior", "People", "Other"]
acc = [88.3, 90.3, 94.1, 94.5, 93.0, 85.0]
prec = [80.6, 89.1, 68.7, 29.9, 71.6, 43.3]
rec = [84.6, 66.9, 84.7, 33.7, 90.8, 34.2]
f1 = [82.6, 76.4, 75.8, 31.7, 80.0, 38.3]
x = np.arange(len(cats)); w = .26
fig, ax = plt.subplots(figsize=(7.6, 3.5))
ax.bar(x - w, prec, w, color=LIGHT, label="Precision")
ax.bar(x, rec, w, color=GREY, label="Recall")
ax.bar(x + w, f1, w, color=AMBER, label="F1")
for xi, v in zip(x, f1):
    ax.text(xi + w, v + 1.5, f"{v:.1f}", ha="center", fontsize=9, color="#7B5E28")
ax.axhline(75, color=STEEL, ls="--", lw=1)
ax.text(5.55, 76.5, "75%", color=STEEL, fontsize=9, ha="right")
ax.set_xticks(x, cats)
ax.set_ylim(0, 105)
ax.set_ylabel("%  (LLM vs. human labels)")
ax.legend(frameon=False, ncol=3, loc="upper center", bbox_to_anchor=(.5, 1.12))
save(fig, "prf1.png")

# 3. Accuracy vs. F1 per category (Table 1): high accuracy can hide a low F1.
fig, ax = plt.subplots(figsize=(7.2, 3.3))
y = np.arange(len(cats))[::-1]
for yi, a, f in zip(y, acc, f1):
    low = f < 50
    ax.plot([f, a], [yi, yi], color=LIGHT, lw=3, zorder=1)
    ax.plot(f, yi, "o", color=STEEL if low else AMBER, ms=9, zorder=3)
    ax.plot(a, yi, "s", color=GREY, ms=8, zorder=3)
    ax.text(f - 2, yi, f"{f:.1f}", ha="right", va="center", fontsize=9)
    ax.text(a + 2, yi, f"{a:.1f}", ha="left", va="center", fontsize=9)
ax.set_yticks(y, [c.replace("\n", " ") for c in cats])
ax.set_xlim(20, 103)
ax.set_xlabel("%")
ax.plot([], [], "s", color=GREY, label="Accuracy")
ax.plot([], [], "o", color=AMBER, label="F1")
ax.legend(frameon=False, loc="upper left")
save(fig, "accuracy-vs-f1.png")

# 4. Cohen's kappa per category (Results text). Reference line 0.4 = acceptable (Discussion).
kc = ["People", "Morphology", "Geography", "Host", "Other", "Ecology & Behavior"]
kv = [.758, .738, .724, .703, .299, .286]
fig, ax = plt.subplots(figsize=(7.2, 3.0))
y = np.arange(len(kc))[::-1]
ax.barh(y, kv, color=[AMBER if v >= .4 else STEEL for v in kv], height=.58)
for yi, v in zip(y, kv):
    if v >= .4:
        ax.text(v + .012, yi, f"κ = {v:.3f}", va="center", fontsize=9.5)
    else:
        ax.text(v - .012, yi, f"κ = {v:.3f}", va="center", ha="right", fontsize=9.5, color="white")
ax.axvline(.4, color="#555", ls="--", lw=1)
ax.text(.405, y[0] + .55, "0.4 (acceptable agreement in the paper)", fontsize=9, color="#555")
ax.set_yticks(y, kc)
ax.set_xlim(0, .92)
ax.set_ylim(-.6, len(kc) - .1)
ax.set_xlabel("Cohen's κ between human and LLM labels")
save(fig, "kappa.png")

# 5. Species counts for the three categories whose counts are stated in the Results text.
cc = ["Morphology", "Host", "People"]
hum = [894, 646, 534]; llm = [940, 486, 534]
x = np.arange(3); w = .36
fig, ax = plt.subplots(figsize=(6.4, 3.1))
ax.bar(x - w/2, hum, w, color=GREY, label="Human-based")
ax.bar(x + w/2, llm, w, color=AMBER, label="LLM-based")
for xi, h, l in zip(x, hum, llm):
    ax.text(xi - w/2, h + 12, f"{h}", ha="center", fontsize=9.5)
    ax.text(xi + w/2, l + 12, f"{l}", ha="center", fontsize=9.5)
ax.set_xticks(x, cc)
ax.set_ylim(0, 1080)
ax.set_ylabel("Number of species")
ax.legend(frameon=False, loc="upper right")
save(fig, "counts.png")
print("done")
