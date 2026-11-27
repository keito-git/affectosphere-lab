"""Figures for the GNNMF-CL (IEEE HPCC 2025) research-blog post.

Every number is copied from the final manuscript
~/Desktop/研究/論文/食品推薦システムの論文/GNNMF-CL0715_final.pdf
(Table I, Table II and Section V text); nothing is recomputed.
The architecture, lifestyle-module and UMAP figures are the paper's own
figures, copied from the final .docx (word/media/image1, image2, image5).
"""
import shutil
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

OUT = "/Users/ishitatakashishou/Sites/affectosphere-lab/public/column-images/hpcc2025-food-recommendation/"
MEDIA = ("/private/tmp/claude-501/-Users-ishitatakashishou/62e336aa-c915-4181-a249-1463c108b1af/"
         "scratchpad/hpcc2025-food-recommendation/docx/word/media/")
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


# 0. Paper figures (Fig. 1 architecture, Fig. 2 lifestyle module, Fig. 5 UMAP).
import os
os.makedirs(OUT, exist_ok=True)
for src, dst in [("image1.png", "architecture.png"),
                 ("image2.png", "lifestyle-module.png"),
                 ("image5.png", "umap.png")]:
    shutil.copyfile(MEDIA + src, OUT + dst)

# 1. Comparison with baselines (Table I): AUC, NDCG@10, Recall@10.
models = ["LDA", "MF-BPR", "FM", "VBPR", "FM-VBPR", "HAFR", "GNNMF-CL"]
auc = [.5154, .5622, .5710, .5808, .5840, .6435, .7148]
ndcg = [.0376, .0376, .0396, .0296, .0372, .0455, .0247]
rec = [.0601, .0567, .0607, .0431, .0580, .0674, .1297]
colors = [LIGHT] * 5 + [STEEL, AMBER]
fig, axes = plt.subplots(1, 3, figsize=(10.5, 3.6))
for ax, vals, name, lim in zip(axes, [auc, recall := rec, ndcg],
                               ["AUC", "Recall@10", "NDCG@10"],
                               [(.45, .76), (0, .15), (0, .052)]):
    y = np.arange(len(models))[::-1]
    ax.barh(y, [v - lim[0] for v in vals], left=lim[0], color=colors, height=.62)
    for yi, v in zip(y, vals):
        ax.text(v + (lim[1] - lim[0]) * .015, yi, f"{v:.4f}", va="center", fontsize=9)
    ax.set_yticks(y, models if ax is axes[0] else [""] * len(models))
    ax.set_xlim(lim[0], lim[1] + (lim[1] - lim[0]) * .22)
    ax.set_title(name, fontsize=11)
    ax.tick_params(axis="y", length=0)
fig.text(.5, -.02, "AllRecipes test set, 500 popularity-based negatives per user (Table I)",
         ha="center", fontsize=10, color="#444")
fig.tight_layout()
save(fig, "baselines.png")

# 2. Ablation (Table II, all metrics @10).
metrics = ["Precision", "Recall", "F1", "NDCG"]
full = [.067, .146, .092, .025]
nocl = [.061, .136, .084, .035]
nohan = [.063, .130, .085, .020]
x = np.arange(4); w = .26
fig, ax = plt.subplots(figsize=(7.2, 3.4))
for off, vals, c, lab in [(-w, full, AMBER, "GNNMF-CL"),
                          (0, nocl, STEEL, "w/o CL"),
                          (w, nohan, GREY, "w/o HAN")]:
    ax.bar(x + off, vals, w, color=c, label=lab)
    for xi, v in zip(x + off, vals):
        ax.text(xi, v + .002, f"{v:.3f}", ha="center", fontsize=8.5)
ax.set_xticks(x, [m + "@10" for m in metrics])
ax.set_ylim(0, .165)
ax.set_ylabel("Score")
ax.legend(frameon=False, loc="upper right")
save(fig, "ablation.png")

# 3. Ablation AUC (Section V-D text: 0.715 / 0.711 / 0.716).
ab = [("GNNMF-CL", .715, AMBER), ("w/o CL", .711, STEEL), ("w/o HAN", .716, GREY)]
fig, ax = plt.subplots(figsize=(7.2, 2.2))
y = np.arange(3)[::-1]
for yi, (lab, v, c) in zip(y, ab):
    ax.barh(yi, v - .70, left=.70, color=c, height=.55)
    ax.text(v + .0004, yi, f"{v:.3f}", va="center", fontsize=10)
ax.set_yticks(y, [a[0] for a in ab])
ax.set_xlim(.70, .72)
ax.set_xlabel("AUC (ablation; axis starts at 0.70)")
save(fig, "ablation-auc.png")
print("done")
