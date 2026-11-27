"""Figures for the 'shared affective geometry' research-blog post (SSRN 7551120).
Every number is copied from the posted SSRN PDF (ssrn-7551120.pdf, Section V,
Tables II-VII); nothing is recomputed.
The pipeline figure (pipeline.png) is the paper's own Fig. 1 (checked against the SSRN PDF)."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

OUT = "/Users/ishitatakashishou/Sites/affectosphere-lab/public/column-images/ssrn-shared-affective-geometry/"
AMBER, STEEL, GREY, LIGHT, INK = "#C4974A", "#3D6B8C", "#9AA0A6", "#D9D4CB", "#1A1A1A"
DELTA = 0.136  # pre-registered equivalence margin
plt.rcParams.update({
    "font.family": "Arial", "font.size": 11, "axes.edgecolor": "#444",
    "axes.linewidth": 0.8, "axes.spines.top": False, "axes.spines.right": False,
    "xtick.color": "#333", "ytick.color": "#333", "axes.labelcolor": "#222",
    "savefig.dpi": 220, "savefig.bbox": "tight", "savefig.facecolor": "white",
})


def save(fig, name):
    fig.savefig(OUT + name)
    plt.close(fig)


# 1. Primary universality verdicts at the representative layer (Table: tab:primary).
idx = ["orth\n(orthogonality)", "CI\n(circularity)", "R²_V\n(valence)", "R²_A\n(arousal)", "R²_D\n(dominance)"]
sd = [0.053, 0.049, 0.197, 0.316, 0.259]
cols = [AMBER, AMBER, GREY, GREY, GREY]
fig, ax = plt.subplots(figsize=(7.2, 3.4))
ax.bar(range(5), sd, color=cols, width=.58)
for i, v in enumerate(sd):
    ax.text(i, v + .006, f"{v:.3f}", ha="center", fontsize=10)
ax.axhline(DELTA, color=STEEL, ls="--", lw=1.2)
ax.text(4.45, DELTA + .007, "margin Δ = 0.136", ha="right", color=STEEL, fontsize=10)
ax.text(0.5, .30, "universal\n(geometry)", ha="center", color="#7B5E28", fontsize=10)
ax.text(3.0, .345, "not universal (linear decodability)", ha="center", color="#555", fontsize=10)
ax.set_xticks(range(5), idx)
ax.set_ylim(0, .37)
ax.set_ylabel("Between-model SD (38 models)")
save(fig, "verdicts.png")

# 2. Peak alignment: inter-model SD before/after, confirmation set (Table: tab:alignment).
names = ["R²_V", "R²_A", "R²_D", "CI", "orth"]
raw = [0.042, 0.181, 0.105, 0.020, 0.035]
ali = [0.031, 0.071, 0.082, 0.016, 0.043]
red = ["−25.9%", "−61.0%", "−22.0%", "−19.8%", "+20.2%"]
x = np.arange(5); w = .36
fig, ax = plt.subplots(figsize=(7.2, 3.4))
ax.bar(x - w/2, raw, w, color=GREY, label="Before alignment (raw)")
ax.bar(x + w/2, ali, w, color=[AMBER, AMBER, AMBER, AMBER, STEEL], label="Per-model peak aligned")
for xi, r, a, t in zip(x, raw, ali, red):
    ax.text(xi, max(r, a) + .007, t, ha="center", fontsize=10,
            color="#7B5E28" if t.startswith("−") else STEEL)
ax.set_xticks(x, names)
ax.set_ylim(0, .215)
ax.set_ylabel("Between-model SD (confirmation set)")
ax.legend(frameon=False, loc="upper right")
save(fig, "alignment.png")

# 3. Readout positions: R²_A between-model SD (Section "Readout Position Study").
lab = ["Word templates\nrepresentative layer", "Word templates\nCV peak layer",
       "EmoBank condB\ncommon depth d* = 0.60", "EmoBank condB\nCV peak layer"]
v = [0.316, 0.151, 0.033, 0.032]
fig, ax = plt.subplots(figsize=(7.2, 3.4))
ax.bar(range(4), v, color=[GREY, GREY, AMBER, AMBER], width=.58)
for i, vv in enumerate(v):
    ax.text(i, vv + .006, f"{vv:.3f}", ha="center", fontsize=10)
ax.axhline(DELTA, color=STEEL, ls="--", lw=1.2)
ax.text(3.45, DELTA + .007, "margin Δ = 0.136", ha="right", color=STEEL, fontsize=10)
ax.set_xticks(range(4), lab, fontsize=9.5)
ax.set_ylim(0, .36)
ax.set_ylabel("Between-model SD of R²_A")
save(fig, "readout.png")

# 4. Saturation control for orthogonality (Section "Evaluation of Geometric Universality").
fig, ax = plt.subplots(figsize=(7.2, 2.9))
rows = [("Random 6-dim subspaces", 0.691, 0.603, 0.775, LIGHT),
        ("Observed: word templates", 0.467, None, None, AMBER),
        ("Observed: combined set", 0.460, None, None, AMBER),
        ("Random 47-dim subspaces", 0.038, 0.003, 0.095, LIGHT)]
y = np.arange(4)[::-1]
for yi, (l, m, lo, hi, c) in zip(y, rows):
    if lo is not None:
        ax.plot([lo, hi], [yi, yi], color="#777", lw=6, alpha=.35, solid_capstyle="butt")
        ax.plot(m, yi, "o", color="#777", ms=8)
        ax.text(hi + .02, yi, f"{m:.3f}  (5–95%: {lo:.3f}–{hi:.3f})", va="center", fontsize=9.5)
    else:
        ax.plot(m, yi, "D", color=c, ms=9)
        ax.text(m + .03, yi, f"{m:.3f}", va="center", fontsize=10)
ax.set_yticks(y, [r[0] for r in rows])
ax.set_xlim(0, 1.05)
ax.set_xlabel("Orthogonality index orth (0 = collinear, 1 = orthogonal)")
save(fig, "saturation.png")

# 5. Non-emotion control (Table: tab:control, n = 7 models, d* = 0.60).
fig, ax = plt.subplots(figsize=(7.2, 2.8))
cond = ["Emotion labels", "Surface-feature control"]
m = [0.233, 0.434]; s = [0.055, 0.076]
ax.barh([1, 0], m, xerr=s, color=[AMBER, GREY], height=.55,
        error_kw=dict(ecolor="#333", lw=1, capsize=3))
ax.text(m[0] + s[0] + .01, 1, "0.233   orthogonality higher in 7/7 models", va="center", fontsize=10)
ax.text(m[1] + s[1] + .01, 0, "0.434", va="center", fontsize=10)
ax.set_yticks([1, 0], cond)
ax.set_xlim(0, .85)
ax.set_xlabel("Linear decodability R² (mean ± SD, 7 models)")
save(fig, "control.png")

# 6. Exploratory activation patching (Tables: tab:grid_ratios, tab:arm_comparison).
alpha = [0.05, 0.10, 0.20, 0.50, 1.00, 2.00]
diff = [0.0654, 0.1392, 0.2631, 0.4837, 0.6759, 0.7209]
fig, (a1, a2) = plt.subplots(1, 2, figsize=(7.6, 3.2), gridspec_kw=dict(width_ratios=[1.6, 1]))
a1.plot(range(6), diff, "-o", color=AMBER, ms=6, lw=1.6)
for i, d in enumerate(diff):
    a1.text(i, d + .04, f"{d:+.2f}", ha="center", fontsize=9)
a1.set_xticks(range(6), [str(a) for a in alpha])
a1.set_xlabel("Injection ratio α (stimulus-last)")
a1.set_ylabel("Valence − random direction")
a1.set_ylim(0, .9)
a1.set_title("sign 5/5 at every α", fontsize=10, color="#555")
a2.bar([0, 1], [0.4837, -0.5818], color=[AMBER, STEEL], width=.55)
a2.axhline(0, color="#444", lw=.8)
a2.text(0, .52, "+0.48\n5/5", ha="center", fontsize=9.5)
a2.text(1, -.62, "−0.58\n1/5", ha="center", va="top", fontsize=9.5)
a2.set_xticks([0, 1], ["stimulus-last\n(A1)", "prompt-last\n(A2)"])
a2.set_ylim(-.95, .75)
a2.set_title("α = 0.5, n = 5 models", fontsize=10, color="#555")
fig.tight_layout()
save(fig, "patching.png")
