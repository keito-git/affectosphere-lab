"""Figures for the MSCF-CFA (NLDB 2025) research-blog post. Every number is copied
from the camera-ready manuscript (MSCF-CFA0503.pdf, Tables 2 and 3); nothing is
recomputed. The architecture, MSCF, CFA and PCA figures are the paper's own
Figures 1, 2, 3 and 5, copied as PNGs."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

OUT = "/Users/ishitatakashishou/Sites/affectosphere-lab/public/column-images/nldb2025-multiscale-fusion/"
AMBER, STEEL, GREY, LIGHT = "#C4974A", "#3D6B8C", "#9AA0A6", "#D9D4CB"
plt.rcParams.update({
    "font.family": "Arial", "font.size": 11, "axes.edgecolor": "#444",
    "axes.linewidth": 0.8, "axes.spines.top": False, "axes.spines.right": False,
    "xtick.color": "#333", "ytick.color": "#333", "axes.labelcolor": "#222",
    "savefig.dpi": 220, "savefig.bbox": "tight", "savefig.facecolor": "white",
})

def save(fig, name):
    fig.savefig(OUT + name)
    plt.close(fig)

# 1. Main comparison, F1 (Table 2).
rows = [("DualCL", 69.45, LIGHT), ("BiLSTM", 71.51, LIGHT), ("MHA-BiLSTM", 73.59, LIGHT),
        ("Transformer", 74.26, LIGHT), ("MF-CNN (backbone)", 74.60, GREY),
        ("RoBERTa+DBLoss", 75.14, STEEL), ("MSCF-CFA", 79.37, AMBER)]
fig, ax = plt.subplots(figsize=(7.2, 3.4))
y = np.arange(len(rows))[::-1]
for yi, (lab, v, c) in zip(y, rows):
    ax.barh(yi, v - 65, left=65, height=.62, color=c)
    ax.text(v + .15, yi, f"{v:.2f}", va="center", fontsize=10)
ax.set_yticks(y, [r[0] for r in rows])
ax.set_xlim(65, 82)
ax.set_xlabel("F1 (%) on the sarcasm detection test set")
save(fig, "main-results.png")

# 2. All four metrics for the three key models (Table 2).
metrics = ["Accuracy", "Precision", "Recall", "F1"]
mods = [("MF-CNN (backbone)", [74.84, 75.88, 74.88, 74.60], GREY),
        ("RoBERTa+DBLoss", [75.23, 75.53, 75.21, 75.14], STEEL),
        ("MSCF-CFA", [79.40, 79.58, 79.42, 79.37], AMBER)]
x = np.arange(4); w = .26
fig, ax = plt.subplots(figsize=(7.2, 3.3))
for i, (lab, vals, c) in enumerate(mods):
    ax.bar(x + (i - 1) * w, vals, w, color=c, label=lab)
    for xi, v in zip(x, vals):
        ax.text(xi + (i - 1) * w, v + .15, f"{v:.1f}", ha="center", fontsize=8.5)
ax.set_xticks(x, metrics)
ax.set_ylim(70, 82)
ax.set_ylabel("Score (%)")
ax.legend(frameon=False, ncol=3, loc="upper center", bbox_to_anchor=(.5, -.1))
save(fig, "metrics.png")

# 3. Ablation (Table 3), F1.
ab = [("MSCF-CFA (full)", 79.37, AMBER), ("w/o MSCF", 78.74, LIGHT),
      ("w/o CFA", 78.73, LIGHT), ("w/o WCE", 77.66, STEEL)]
fig, ax = plt.subplots(figsize=(7.2, 2.6))
y = np.arange(len(ab))[::-1]
for yi, (lab, v, c) in zip(y, ab):
    ax.barh(yi, v - 76, left=76, height=.58, color=c)
    d = "" if lab.startswith("MSCF") else f"  ({v - 79.37:+.2f})"
    ax.text(v + .05, yi, f"{v:.2f}{d}", va="center", fontsize=10)
ax.set_yticks(y, [a[0] for a in ab])
ax.set_xlim(76, 80.6)
ax.set_xlabel("F1 (%); parentheses = change from the full model")
save(fig, "ablation.png")
print("done")
