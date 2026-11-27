"""Figures for the research-blog post on "How Much Reproducible Human Disagreement
Can Text Models Recover?" (SSRN 7685790). Every plotted number is copied from the
manuscript (sec5_experiments.tex, Tables 2-6 and text); the only arithmetic is the
three-way partition of Eq. (7), which uses r33 and m_E from Table 2.
The overview figure (overview.png) is the paper's own Figure 1, converted from PDF."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Patch

OUT = "/Users/ishitatakashishou/Sites/affectosphere-lab/public/column-images/ssrn-reproducible-human-disagreement/"
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


# 1. Recoverable share on the main datasets, full vs matched (Table 2: tab:main).
ds = ["Safety\nDICES-990", "Emotion\nBRIGHTER English", "NLI\nChaosNLI"]
full = [(.79, .75, .83), (.32, .27, .38), (.35, .30, .42)]
matched = [(.63, .57, .68), (.27, .22, .33), (.15, .10, .21)]
full_lab = ["Full", "Full", "Full (MNLI checkpoint)"]
match_lab = ["Matched votes", "Matched", "Matched"]
x = np.arange(3); w = .36
fig, ax = plt.subplots(figsize=(7.2, 3.6))
for off, vals, col, labs in [(-w/2, matched, AMBER, match_lab), (w/2, full, STEEL, full_lab)]:
    m = [v[0] for v in vals]
    err = [[v[0] - v[1] for v in vals], [v[2] - v[0] for v in vals]]
    ax.bar(x + off, m, w, color=col, yerr=err, capsize=3,
           error_kw=dict(ecolor="#333", lw=1))
    for xi, v in zip(x + off, vals):
        ax.text(xi, v[2] + .02, f"{v[0]:.2f}", ha="center", fontsize=10)
ax.set_xticks(x, ds)
ax.set_ylim(0, 1.0)
ax.set_ylabel(r"Recoverable share $R_{\mathrm{text}}$ (n = 3)")
ax.legend(handles=[Patch(color=AMBER, label="Matched condition (no task-aligned pretraining)"),
                   Patch(color=STEEL, label="Full condition")],
          frameon=False, loc="upper right", fontsize=9.5)
save(fig, "main-share.png")

# 2. Three-way partition of Var(D_3) (Table 2 r33 and m_E; Eq. 7; paper Figure 2).
# (label, r33, m_E, R_text as reported in Table 2)
rows = [("BRIGHTER English, Full", .413, .364, .32),
        ("BRIGHTER English, Matched", .413, .336, .27),
        ("ChaosNLI, Full (MNLI ckpt)", .179, .252, .35),
        ("ChaosNLI, Matched", .179, .164, .15),
        ("DICES-990, Full", .147, .341, .79),
        ("DICES-990, Matched votes", .147, .303, .63)]
fig, ax = plt.subplots(figsize=(7.2, 3.5))
y = np.arange(len(rows))[::-1]
for yi, (lab, r, m, rt) in zip(y, rows):
    pred, unc, non = m ** 2, r - m ** 2, 1 - r
    ax.barh(yi, pred, color=STEEL, height=.62)
    ax.barh(yi, unc, left=pred, color=AMBER, height=.62)
    ax.barh(yi, non, left=r, color=LIGHT, height=.62)
    ax.text(1.01, yi, f"R = {rt:.2f}", va="center", fontsize=9.5, color="#333")
ax.set_yticks(y, [r[0] for r in rows])
ax.set_xlim(0, 1)
ax.set_xlabel(r"Share of the variance of three-annotator disagreement $D_3$")
ax.legend(handles=[Patch(color=STEEL, label=r"text-predictable  $m_E^2$"),
                   Patch(color=AMBER, label=r"repeatable, not captured  $r_{33}-m_E^2$"),
                   Patch(color=LIGHT, label=r"non-repeatable  $1-r_{33}$")],
          frameon=False, loc="upper center", bbox_to_anchor=(.42, -.2), ncol=3, fontsize=9)
save(fig, "partition.png")

# 3. Two datasets of the same task (Table 2 and Table 3: tab:second).
pairs = [("Safety", [("DICES-990\nseven votes", .63, .57, .68), ("DICES-350\nseven votes", .17, .10, .27)]),
         ("Emotion", [("BRIGHTER\nEnglish\nall votes", .32, .27, .38), ("BRIGHTER\nGerman\nall votes, XLM-R", .53, .44, .62)])]
fig, axes = plt.subplots(1, 2, figsize=(7.4, 3.5), sharey=True)
for ax, (task, items) in zip(axes, pairs):
    for i, (lab, m, lo, hi) in enumerate(items):
        ax.bar(i, m, .55, color=STEEL if i == 0 else AMBER, yerr=[[m - lo], [hi - m]],
               capsize=3, error_kw=dict(ecolor="#333", lw=1))
        ax.text(i, hi + .02, f"{m:.2f}", ha="center", fontsize=10)
    ax.set_xticks([0, 1], [it[0] for it in items], fontsize=9.5)
    ax.set_title(task, fontsize=11)
    ax.set_xlim(-.6, 1.6)
axes[0].set_ylim(0, .8)
axes[0].set_ylabel(r"$R_{\mathrm{text}}$ (n = 3, 95% interval)")
save(fig, "second-datasets.png")

# 4. Alternative predictors in the matched condition (Table 4: tab:controls).
preds = ["Surface features\n+ ridge", "Frozen Qwen2.5-7B\nembeddings + ridge",
         "Majority-label\nclassifier", "Direct regression\nof E[D3]", "Distribution\nmodel"]
vals = {"Emotion": [.00, .25, .14, .32, .27],
        "NLI": [.00, .15, .05, .14, .15],
        "Safety": [.05, .56, .30, .58, .63]}
cols = [LIGHT, GREY, GREY, STEEL, AMBER]
fig, axes = plt.subplots(1, 3, figsize=(7.4, 3.4), sharey=True)
for ax, (task, v) in zip(axes, vals.items()):
    yy = np.arange(5)[::-1]
    ax.barh(yy, v, color=cols, height=.6)
    for yi, vv in zip(yy, v):
        ax.text(vv + .015, yi, f"{vv:.2f}", va="center", fontsize=9.5)
    ax.set_title(task, fontsize=11)
    ax.set_xlim(0, .78)
    ax.set_yticks(yy, preds, fontsize=9)
axes[1].set_xlabel(r"$R_{\mathrm{text}}$ (matched condition, n = 3)")
save(fig, "controls.png")

# 5. Group size n = 2, 3, 4 (Table 5: tab:groupsize).
# last element: y position of the text label (shifted only to avoid overlap)
gs = [("DICES-990, Full", [.83, .79, .78], STEEL, "-", .78),
      ("DICES-990, Matched votes", [.66, .63, .62], STEEL, "--", .62),
      ("ChaosNLI, Full (MNLI ckpt)", [.38, .35, .35], GREY, "-", .385),
      ("BRIGHTER English, Full", [.29, .32, .34], AMBER, "-", .335),
      ("BRIGHTER English, Matched", [.26, .27, .30], AMBER, "--", .285),
      ("ChaosNLI, Matched", [.17, .15, .16], GREY, "--", .16)]
fig, ax = plt.subplots(figsize=(7.2, 3.6))
for lab, v, c, ls, ty in gs:
    ax.plot([2, 3, 4], v, ls, marker="o", color=c, lw=1.6, ms=5)
    ax.text(4.08, ty, lab, va="center", fontsize=9, color="#333")
ax.set_xticks([2, 3, 4])
ax.set_xlim(1.85, 5.4)
ax.set_ylim(0, .95)
ax.spines["bottom"].set_bounds(2, 4)
ax.set_xlabel("Annotator group size n")
ax.set_ylabel(r"$R_{\mathrm{text}}(n)$")
save(fig, "group-size.png")

# 6. Vote format: R_text moves moderately, n* moves several-fold
#    (Section 5.6 text; Table 6: tab:nstar; matched BRIGHTER English and matched ChaosNLI).
fig, (a1, a2) = plt.subplots(1, 2, figsize=(7.4, 3.3))
labs = ["Emotion\nmulti-label", "Emotion\none-hot redraw", "NLI\none-hot"]
r = [.27, .36, .15]
a1.bar(range(3), r, .55, color=[AMBER, STEEL, GREY])
for i, v in enumerate(r):
    a1.text(i, v + .01, f"{v:.2f}", ha="center", fontsize=10)
a1.set_xticks(range(3), labs, fontsize=9)
a1.set_ylim(0, .5)
a1.set_ylabel(r"$R_{\mathrm{text}}$ (matched)")
a1.set_title("Recoverable share", fontsize=11)
# n*(3): 1.25 [0, 1.91]; > 5 (above measured curve, k_max = 5); 2.73 [2.19, 3.60]
a2.bar(0, 1.25, .55, color=AMBER, yerr=[[1.25 - 0], [1.91 - 1.25]], capsize=3,
       error_kw=dict(ecolor="#333", lw=1))
a2.bar(1, 5, .55, color=STEEL, alpha=.35, hatch="///", edgecolor=STEEL, lw=0)
a2.annotate("", (1, 6.3), (1, 5.05), arrowprops=dict(arrowstyle="->", color=STEEL, lw=1.4))
a2.bar(2, 2.73, .55, color=GREY, yerr=[[2.73 - 2.19], [3.60 - 2.73]], capsize=3,
       error_kw=dict(ecolor="#333", lw=1))
a2.text(0, 2.15, "1.25", ha="center", fontsize=10)
a2.text(1, 6.45, "> 5\n(above measured curve)", ha="center", fontsize=9)
a2.text(2, 3.75, "2.73", ha="center", fontsize=10)
a2.set_xticks(range(3), labs, fontsize=9)
a2.set_ylim(0, 7.6)
a2.set_ylabel(r"Annotator-equivalent count $n^*(3)$")
a2.set_title("Annotator-equivalent count", fontsize=11)
fig.tight_layout(w_pad=2.5)
save(fig, "vote-format.png")
print("done")
