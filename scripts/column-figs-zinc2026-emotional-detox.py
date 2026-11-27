"""Figures for the MALLET (IEEE ZINC 2026) research-blog post. Every number is
copied from the camera-ready manuscript (camera-ready-1571260788.pdf; same values
as section4-eg.tex in the arXiv source); nothing is recomputed."""
import os
import subprocess
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

OUT = "/Users/ishitatakashishou/Sites/affectosphere-lab/public/column-images/zinc2026-emotional-detox/"
# The paper's own method figure (overview.pdf from the arXiv source zip, extracted to scratch).
OVERVIEW_PDF = ("/private/tmp/claude-501/-Users-ishitatakashishou/62e336aa-c915-4181-a249-1463c108b1af/"
                "scratchpad/zinc2026-emotional-detox/src/Authors/Figures/overview.pdf")
AMBER, STEEL, GREY, LIGHT = "#C4974A", "#3D6B8C", "#9AA0A6", "#D9D4CB"
plt.rcParams.update({
    "font.family": "Arial", "font.size": 11, "axes.edgecolor": "#444",
    "axes.linewidth": 0.8, "axes.spines.top": False, "axes.spines.right": False,
    "xtick.color": "#333", "ytick.color": "#333", "axes.labelcolor": "#222",
    "savefig.dpi": 220, "savefig.bbox": "tight", "savefig.facecolor": "white",
})
os.makedirs(OUT, exist_ok=True)


def save(fig, name):
    fig.savefig(OUT + name)
    plt.close(fig)


# 0. Method figure (Fig. 1 of the paper), PDF -> PNG.
if os.path.exists(OVERVIEW_PDF):
    subprocess.run(["pdftoppm", "-png", "-r", "160", "-singlefile", OVERVIEW_PDF,
                    OUT + "overview"], check=True)

MODES = ["RAW", "BALANCED", "COOL"]
MCOL = [GREY, STEEL, AMBER]

# 1. Primary metrics across presentation modes (Table I: summary).
metrics = [("Mean stimulus score S̄  (lower = calmer)", [0.482, 0.419, 0.389], "{:.3f}"),
           ("High-Impact Rate HIR  (share with S > 0.6)", [0.446, 0.354, 0.330], "{:.3f}"),
           ("Emotion Balance Index EBI  (higher = more even)", [0.316, 0.338, 0.346], "{:.3f}"),
           ("Flesch Reading Ease FRE  (higher = easier)", [39.91, 30.23, 34.54], "{:.2f}")]
fig, axes = plt.subplots(2, 2, figsize=(8.6, 5.6))
for ax, (lab, vals, fmt) in zip(axes.flat, metrics):
    x = np.arange(3)
    ax.bar(x, vals, color=MCOL, width=.62)
    for xi, v in zip(x, vals):
        ax.text(xi, v * 1.01, fmt.format(v), ha="center", va="bottom", fontsize=9.5)
    ax.set_xticks(x, MODES)
    ax.set_ylim(0, max(vals) * 1.18)
    ax.set_title(lab, fontsize=10.5, loc="left")
fig.tight_layout(h_pad=1.6)
save(fig, "mode-metrics.png")

# 2. Effect sizes of paired t-tests, Holm-corrected, n = 800 (Table II: tests).
# |d| is plotted; sign of EBI d is negative because EBI increases.
rows = [("S  RAW vs BALANCED", 0.210, STEEL), ("S  RAW vs COOL", 0.282, AMBER),
        ("EBI  RAW vs BALANCED", 0.151, STEEL), ("EBI  RAW vs COOL", 0.201, AMBER),
        ("FRE  RAW vs BALANCED", 0.609, STEEL), ("FRE  RAW vs COOL", 0.339, AMBER)]
fig, ax = plt.subplots(figsize=(7.2, 3.4))
y = np.arange(len(rows))[::-1]
for yi, (lab, d, c) in zip(y, rows):
    ax.barh(yi, d, color=c, height=.6)
    ax.text(d + .008, yi, f"{d:.3f}", va="center", fontsize=9.5)
for v, t in [(0.2, "small"), (0.5, "medium")]:
    ax.axvline(v, color="#888", ls=":", lw=1)
    ax.text(v + .005, y[0] + .55, t, color="#666", fontsize=9)
ax.set_yticks(y, [r[0] for r in rows])
ax.set_xlim(0, .7)
ax.set_ylim(-.6, len(rows) - .1)
ax.set_xlabel("|Cohen's d|  (all six comparisons p_adj < 0.001)")
save(fig, "effect-sizes.png")

# 3. Mean stimulus score by AG News category (Table III: category).
cats = ["World", "Sports", "Business", "Sci/Tech"]
raw = [0.659, 0.393, 0.500, 0.374]
bal = [0.660, 0.312, 0.396, 0.308]
cool = [0.645, 0.260, 0.350, 0.299]
dcool = ["2.2%", "33.8%", "30.0%", "20.0%"]
fig, ax = plt.subplots(figsize=(7.2, 3.6))
x = np.arange(4)
w = .26
for k, (vals, c, lab) in enumerate(zip([raw, bal, cool], MCOL, MODES)):
    ax.bar(x + (k - 1) * w, vals, w, color=c, label=lab)
for xi, t, top in zip(x, dcool, raw):
    ax.text(xi, max(top, .40) + .03, "COOL −" + t, ha="center", fontsize=9.5, color="#7B5E28")
ax.set_xticks(x, cats)
ax.set_ylabel("Mean stimulus score S̄")
ax.set_ylim(0, .82)
ax.legend(frameon=False, ncol=3, loc="upper right", fontsize=9.5)
save(fig, "category.png")

# 4. NLI judgement distribution, original as premise (Table IV: semantic).
ent = [95.1, 27.8]
neu = [3.0, 68.6]
con = [1.9, 3.6]
fig, ax = plt.subplots(figsize=(7.2, 2.4))
y = np.array([1, 0])
ax.barh(y, ent, color=STEEL, height=.55, label="entailment")
ax.barh(y, neu, left=ent, color=LIGHT, height=.55, label="neutral")
ax.barh(y, con, left=np.add(ent, neu), color="#B5553C", height=.55, label="contradiction")
for yi, e, n, c in zip(y, ent, neu, con):
    ax.text(e / 2, yi, f"{e}%", ha="center", va="center", color="white", fontsize=9.5)
    if n > 10:
        ax.text(e + n / 2, yi, f"{n}%", ha="center", va="center", fontsize=9.5)
        ax.text(101.5, yi, f"contr. {c}%", va="center", fontsize=9.5)
    else:
        ax.text(101.5, yi, f"neutral {n}%\ncontr. {c}%", va="center", fontsize=9.5)
ax.set_yticks(y, ["BALANCED\n(SBERT 0.846)", "COOL\n(SBERT 0.827)"])
ax.set_xlim(0, 100)
ax.set_xlabel("Share of rewritten texts (%)")
ax.legend(frameon=False, ncol=3, loc="lower center", bbox_to_anchor=(.5, 1.0), fontsize=9.5)
save(fig, "semantic.png")

# 5. Weekly summary of five pseudo-consumers (Table V: users).
ids = ["0", "1", "2", "3", "4"]
hir = [0.53, 0.46, 0.50, 0.44, 0.41]
anger = [0.398, 0.322, 0.364, 0.313, 0.328]
fig, ax = plt.subplots(figsize=(7.2, 3.2))
x = np.arange(5)
ax.bar(x - .18, hir, .34, color=AMBER, label="HIR")
ax.bar(x + .18, anger, .34, color=STEEL, label="mean anger probability")
for xi, h, a in zip(x, hir, anger):
    ax.text(xi - .18, h + .01, f"{h:.2f}", ha="center", fontsize=9)
    ax.text(xi + .18, a + .01, f"{a:.3f}", ha="center", fontsize=9)
ax.plot([-.6, 4.55], [.5, .5], color="#888", ls=":", lw=1)
ax.text(4.62, .5, "HIR = 0.5", fontsize=9, color="#666", va="center")
ax.set_xticks(x, [f"Consumer {i}" for i in ids])
ax.set_xlim(-.6, 5.1)
ax.set_ylim(0, .68)
ax.legend(frameon=False, ncol=2, loc="upper right", fontsize=9.5)
save(fig, "consumers.png")
print("done")
