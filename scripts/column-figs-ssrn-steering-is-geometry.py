"""Figures for the research-blog post on SSRN 7633458
("What Looks Like Emotion Steering Is Largely the Geometry of the Representation Space").
Every number is copied from the SSRN source (NativeAffect TNNLS SSRN version,
source/tables/*.tex); nothing is recomputed. The method figure (pipeline.png) is the
paper's own fig1_pipeline.pdf converted with pdftoppm."""
import shutil
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

OUT = "/Users/ishitatakashishou/Sites/affectosphere-lab/public/column-images/ssrn-steering-is-geometry/"
SCRATCH = ("/private/tmp/claude-501/-Users-ishitatakashishou/62e336aa-c915-4181-a249-1463c108b1af/"
           "scratchpad/ssrn-steering-is-geometry/pipeline.png")
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


# 0. Method figure: the paper's Fig. 1 (fig1_pipeline.pdf -> PNG).
shutil.copy(SCRATCH, OUT + "pipeline.png")

# 1. In-plane vs full-space floor per layer (Table IV), confirmation and discovery halves.
layers = [5, 7, 10, 12]
conf_in = [0.982, 0.926, 1.8, 2.7]
conf_full = [0.404, 0.479, 0.980, 1.5]
conf_ratio = [2.429, 1.935, 1.795, 1.796]
disc_ratio = [2.731, 2.424, 1.936, 1.982]
fig, axes = plt.subplots(1, 2, figsize=(9.2, 3.4), gridspec_kw=dict(width_ratios=[1.25, 1]))
ax = axes[0]
x = np.arange(4); w = .36
ax.bar(x - w/2, conf_full, w, color=GREY, label="Full-space control")
ax.bar(x + w/2, conf_in, w, color=STEEL, label="In-plane control")
ax.set_xticks(x, [f"L{l}" for l in layers])
ax.set_ylabel("Floor JSD ($\\times 10^{-3}$)")
ax.set_title("Floor magnitude, confirmation half", fontsize=11, loc="left")
ax.legend(frameon=False, loc="upper left")
ax.set_ylim(0, 3.2)
ax = axes[1]
ax.plot(x, disc_ratio, "-o", color=LIGHT, mec="#999", ms=6, lw=1.4, label="Discovery half")
ax.plot(x, conf_ratio, "-o", color=AMBER, ms=7, lw=1.8, label="Confirmation half")
for xi, v in zip(x, conf_ratio):
    ax.text(xi, v - .17, f"{v:.2f}", ha="center", fontsize=9.5, color="#7B5E28")
ax.axhline(1.5, color="#666", ls="--", lw=1)
ax.text(3.05, 1.53, "registered bar 1.5", ha="right", fontsize=9, color="#555")
ax.axhline(1.0, color=GREY, ls=":", lw=1)
ax.set_xticks(x, [f"L{l}" for l in layers])
ax.set_ylim(.9, 3.0)
ax.set_ylabel("In-plane / full-space")
ax.set_title("Floor ratio (α = 0.05)", fontsize=11, loc="left")
ax.legend(frameon=False, loc="upper right", fontsize=9.5)
fig.tight_layout()
save(fig, "floor-ratio.png")

# 2. Cross-model floor ratio vs subspace rank (Table XIV).
k = [2, 5, 10, 20]
models = [("Apertus-1.5B", [1.97, 1.79, 1.76, 1.58], AMBER, "o"),
          ("SmolLM2-1.7B", [2.56, 3.77, 3.56, 2.64], STEEL, "s"),
          ("Phi-3-mini-3.8B", [1.74, 1.76, 1.73, 1.56], GREY, "^")]
fig, ax = plt.subplots(figsize=(6.6, 3.5))
for name, v, c, m in models:
    ax.plot(range(4), v, "-" + m, color=c, ms=7, lw=1.8, label=name)
ax.axhline(1.0, color="#666", ls="--", lw=1)
ax.text(3.1, 1.04, "ratio = 1 (no confound)", ha="right", fontsize=9, color="#555")
ax.set_xticks(range(4), [f"k = {kk}" for kk in k])
ax.set_ylim(.8, 4.1)
ax.set_xlabel("Width of the dominant subspace (top-k PCs)")
ax.set_ylabel("In-plane / full-space floor")
ax.legend(frameon=False, loc="upper center", ncol=3, fontsize=9.5, bbox_to_anchor=(.5, 1.12))
save(fig, "cross-model.png")

# 3. Reference (human valence) direction: Cliff's delta vs full-space (C2a) and
#    vs in-plane (C2b), every layer x strength cell (Table V, confirmation half).
alphas = [0.03, 0.05, 0.1, 0.2]
c2a = np.array([[0.5, 0.25, 0.5, 0.9],
                [0.5, 0.5, 0.6, 0.9],
                [0.55, 0.8, 0.95, 1.0],
                [0.65, 0.75, 1.0, 1.0]])
c2b = np.array([[-0.3, -0.55, -0.9, -1.0],
                [-0.4, -0.45, -0.55, -0.8],
                [-0.05, 0.1, 0.1, -0.15],
                [-0.25, -0.1, -0.05, -0.2]])
from matplotlib.colors import LinearSegmentedColormap
cmap = LinearSegmentedColormap.from_list("div", [STEEL, "#F4F2EE", AMBER])
fig, axes = plt.subplots(1, 2, figsize=(9.0, 3.4))
for ax, mat, ttl in [(axes[0], c2a, "vs full-space control (C2a)\nall 16 cells significant"),
                     (axes[1], c2b, "vs in-plane control (C2b)\nno cell significant")]:
    im = ax.imshow(mat, cmap=cmap, vmin=-1, vmax=1, aspect="auto")
    for i in range(4):
        for j in range(4):
            ax.text(j, i, f"{mat[i, j]:+.2f}", ha="center", va="center", fontsize=10, color=INK)
    ax.set_xticks(range(4), [str(a) for a in alphas])
    ax.set_yticks(range(4), [f"L{l}" for l in layers])
    ax.set_xlabel("Relative strength α")
    ax.set_title(ttl, fontsize=10.5, loc="left")
    for s in ax.spines.values():
        s.set_visible(False)
    ax.tick_params(length=0)
cb = fig.colorbar(im, ax=axes, fraction=.03, pad=.02)
cb.set_label("Cliff's δ (reference − control)")
cb.outline.set_visible(False)
save(fig, "reference-direction.png")

# 4. VMIC / in-plane floor ratio across models (Table XIV, third row of each model).
vmic = [("Apertus-1.5B", [0.94, 1.14, 1.10, 1.14], AMBER, "o"),
        ("SmolLM2-1.7B", [0.84, 0.70, 0.86, 0.92], STEEL, "s"),
        ("Phi-3-mini-3.8B", [0.86, 0.95, 0.92, 0.94], GREY, "^")]
fig, ax = plt.subplots(figsize=(6.6, 3.1))
for name, v, c, m in vmic:
    ax.plot(range(4), v, "-" + m, color=c, ms=7, lw=1.8, label=name)
ax.axhline(1.0, color="#666", ls="--", lw=1)
ax.set_xticks(range(4), [f"k = {kk}" for kk in k])
ax.set_ylim(.6, 1.3)
ax.set_xlabel("Width of the dominant subspace (top-k PCs)")
ax.set_ylabel("VMIC / in-plane floor")
ax.legend(frameon=False, loc="upper center", ncol=3, fontsize=9.5, bbox_to_anchor=(.5, 1.13))
save(fig, "vmic-ratio.png")

# 5. Overlap with the human VAD subspace under two estimators, same axes (Table VIII).
cells = ["L5-a0", "L5-a1", "L5-a2", "L7-a0", "L7-a1", "L7-a2",
         "L10-a0", "L10-a1", "L10-a2", "L12-a0", "L12-a1", "L12-a2"]
pc = [10.2719, 22.0732, 16.7771, 12.9901, 18.3093, 13.2447,
      16.6236, 20.4131, 13.9508, 11.1651, 7.929, 11.7181]
ridge = [0.1735, 0.3815, 0.8475, 0.235, 0.248, 0.8459,
         0.8117, 0.6572, 0.0647, 1.0095, 0.7, 1.8143]
fig, ax = plt.subplots(figsize=(8.0, 3.4))
x = np.arange(len(cells))
for xi, a, b in zip(x, pc, ridge):
    ax.plot([xi, xi], [b, a], color=LIGHT, lw=2, zorder=1)
ax.scatter(x, pc, color=STEEL, s=42, zorder=2, label="Covariance PCs")
ax.scatter(x, ridge, color=AMBER, s=42, zorder=2, label="Ridge regression")
ax.axhline(5.0, color="#666", ls="--", lw=1)
ax.text(3.5, 4.2, "registered 5% line", ha="center", va="top", fontsize=9, color="#555")
ax.set_yscale("log")
ax.set_ylim(.04, 40)
ax.set_xticks(x, cells, rotation=45, ha="right", fontsize=9)
ax.set_ylabel("Inside VAD subspace (%)")
ax.set_xlabel("Layer - ICA axis")
ax.legend(frameon=False, loc="upper left", bbox_to_anchor=(0, 1.02), ncol=2, fontsize=10)
save(fig, "estimator.png")
print("done")
