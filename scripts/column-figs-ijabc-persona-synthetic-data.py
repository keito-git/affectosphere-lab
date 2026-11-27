"""Figures for the PersonaGen (IJABC 2026) research-blog post. Every number is
copied from the final submitted manuscript (PersonaGen_提出版.zip, 4_experiment.tex
tables and the value labels printed on its Figure 4); nothing is recomputed.
The framework diagram and t-SNE plot are the paper's own figures (PDF -> PNG)."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

OUT = "/Users/ishitatakashishou/Sites/affectosphere-lab/public/column-images/ijabc-persona-synthetic-data/"
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

EMO = ["sadness", "joy", "surprise", "pleasure", "anger", "fear", "neutral"]

# 1. Semantic diversity per emotion (Table 4: MCD, CE; CD = 0.484 overall).
mcd = [.596, .572, .736, .586, .730, .712, .748]
ce = [1.603, 1.572, 1.541, 1.582, 1.595, 1.556, 1.584]
fig, axes = plt.subplots(1, 2, figsize=(7.6, 3.2))
cols = [STEEL if e in ("joy", "pleasure") else LIGHT for e in EMO]
for ax, v, lab, lo, hi in [(axes[0], mcd, "Mean cosine distance (MCD)", .5, .78),
                          (axes[1], ce, "Cluster entropy (CE)", 1.5, 1.62)]:
    x = np.arange(7)
    ax.bar(x, v, color=cols, width=.62)
    for xi, vi in zip(x, v):
        ax.text(xi, vi + (hi - lo) * .015, f"{vi:.3f}", ha="center", fontsize=8.5)
    ax.set_xticks(x, EMO, rotation=40, ha="right")
    ax.set_ylim(lo, hi)
    ax.set_title(lab, fontsize=11)
fig.text(.5, -.04, "Blue: joy and pleasure (lowest MCD). Centroid distance across categories: CD = 0.484.",
         ha="center", fontsize=9.5, color="#555")
fig.tight_layout()
save(fig, "diversity.png")

# 2. Per-emotion classification F1 of synthetic texts (Table 5, LightGBM, 80/20 split).
f1 = [.89, .62, .85, .61, .91, .92, .83]
order = np.argsort(f1)
fig, ax = plt.subplots(figsize=(7.2, 3.2))
y = np.arange(7)
for yi, i in zip(y, order):
    c = STEEL if EMO[i] in ("joy", "pleasure") else AMBER
    ax.barh(yi, f1[i], color=c, height=.6)
    ax.text(f1[i] + .01, yi, f"{f1[i]:.2f}", va="center", fontsize=10)
ax.axvline(.80, color=GREY, ls="--", lw=1)
ax.text(.805, 6.45, "overall F1 = 0.80", color="#555", fontsize=9.5)
ax.set_yticks(y, [EMO[i] for i in order])
ax.set_xlim(0, 1.0)
ax.set_xlabel("F1 (LightGBM on MiniLM embeddings, 3,500 synthetic texts)")
save(fig, "per-emotion-f1.png")

# 3. Human-likeness (GPT-4o, 5-point scale) — value labels printed on the paper's Figure 4.
crit = ["Emotion Match", "Grammaticality", "Lexical Diversity", "Structure & Logic"]
m = [4.65, 5.00, 4.68, 4.83]; s = [.56, .03, .47, .37]
fig, ax = plt.subplots(figsize=(7.2, 3.0))
x = np.arange(4)
ax.bar(x, m, yerr=s, color=AMBER, width=.55, capsize=3, error_kw=dict(ecolor="#333", lw=1))
for xi, mi, si in zip(x, m, s):
    ax.text(xi, mi + si + .06, f"{mi:.2f} ± {si:.2f}", ha="center", fontsize=10)
ax.set_xticks(x, crit)
ax.set_ylim(3, 5.8)
ax.set_yticks([3, 4, 5])
ax.set_ylabel("Score (1–5, mean ± std)")
save(fig, "human-likeness.png")

# 4. Similarity to real tweets (Table 6).
meth = ["AttrPrompt", "RandPersona", "PersonaGen"]
mc = [LIGHT, GREY, AMBER]
metrics = [("FID ↓", [.388, .397, .414]), ("PRD-Fβ ↑", [.259, .282, .367]),
           ("KL ↓", [.070, .055, .049]), ("Histogram-cosine ↑", [.982, .986, .988])]
fig, axes = plt.subplots(1, 4, figsize=(8.4, 2.9))
for ax, (name, v) in zip(axes, metrics):
    ax.bar(range(3), v, color=mc, width=.62)
    lo = min(v) * (.97 if name.startswith("Hist") else 0)
    hi = max(v) * (1.006 if name.startswith("Hist") else 1.2)
    ax.set_ylim(lo, hi)
    for i, vi in enumerate(v):
        ax.text(i, vi + (hi - lo) * .02, f"{vi:.3f}", ha="center", fontsize=8.5)
    ax.set_xticks(range(3), ["Attr", "Rand", "Persona\nGen"], fontsize=9)
    ax.set_title(name, fontsize=10.5)
    ax.tick_params(axis="y", labelsize=8.5)
fig.tight_layout()
save(fig, "similarity.png")

# 5. Downstream: train on synthetic, test on gold tweets (Table 7).
rows = [("Gold data (real training set)", .568, .567, STEEL),
        ("AttrPrompt", .348, .320, LIGHT),
        ("RandPersona", .326, .288, GREY),
        ("PersonaGen", .359, .321, AMBER)]
fig, ax = plt.subplots(figsize=(7.2, 3.0))
y = np.arange(4)[::-1]; w = .36
for yi, (lab, acc, f, c) in zip(y, rows):
    ax.barh(yi + w/2, acc, w, color=c)
    ax.barh(yi - w/2, f, w, color=c, alpha=.55)
    ax.text(acc + .006, yi + w/2, f"Acc {acc:.3f}", va="center", fontsize=9.5)
    ax.text(f + .006, yi - w/2, f"F1 {f:.3f}", va="center", fontsize=9.5)
ax.set_yticks(y, [r[0] for r in rows])
ax.set_xlim(0, .7)
ax.set_xlabel("6-class emotion classification on the gold test set (LightGBM)")
save(fig, "downstream.png")
print("done")
