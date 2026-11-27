"""Figures for the BSETD (IEEE ICDM 2026) research-blog post. Every number is copied
from the camera-ready manuscript (sections/04_experiments.tex tables and text);
nothing is recomputed. pipeline.png and results-overview.png are the paper's own
Figures 1 and 2, converted to PNG separately."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

OUT = "/Users/ishitatakashishou/Sites/affectosphere-lab/public/column-images/icdm2026-bayesian-spectral-transition/"
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


# 1. Top-10 transition pairs by |log2 lift| (Table I: tab:el-top-edges).
pairs = [("disgust → anger", .94), ("joy → anger", -.90), ("anger → joy", -.89),
         ("anger → disgust", .86), ("disgust → joy", -.65), ("sadness → joy", -.59),
         ("fear → joy", -.56), ("joy → sadness", -.54), ("fear → anger", .49),
         ("neutral → anger", -.50)]
fig, ax = plt.subplots(figsize=(7.0, 4.2))
y = np.arange(len(pairs))[::-1]
for yi, (lab, v) in zip(y, pairs):
    c = AMBER if v > 0 else STEEL
    ax.barh(yi, v, color=c, height=.62)
    ax.text(v + (.03 if v > 0 else -.03), yi, f"{v:+.2f}", va="center",
            ha="left" if v > 0 else "right", fontsize=10)
ax.axvline(0, color="#444", lw=.8)
ax.set_yticks(y, [p[0] for p in pairs])
ax.set_xlim(-1.2, 1.2)
ax.set_xlabel("log2 lift  (EmotionLines, posterior mean vs. marginal)")
ax.text(.6, -1.35, "over-represented", color="#7B5E28", ha="center", fontsize=10)
ax.text(-.6, -1.35, "under-represented", color=STEEL, ha="center", fontsize=10)
ax.set_ylim(-1.8, len(pairs) - .4)
save(fig, "top-transitions.png")

# 2. Self-loop posterior means, inertia vs. contagion split (Table II: tab:inertia-contagion).
emo = ["anger", "sadness", "neutral", "fear", "disgust", "surprise", "joy"]
ine = [.297, .255, .687, .165, .158, .195, .320]
con = [.151, .139, .577, .059, .085, .155, .298]
dif = [.146, .116, .111, .106, .073, .039, .022]
fig, ax = plt.subplots(figsize=(7.0, 3.8))
y = np.arange(len(emo))[::-1]
for yi, a, b, d in zip(y, ine, con, dif):
    ax.plot([b, a], [yi, yi], color=LIGHT, lw=3, zorder=1)
    ax.text(max(a, b) + .02, yi, f"+{d:.3f}", va="center", fontsize=9.5, color="#555")
ax.scatter(con, y, color=STEEL, s=60, zorder=3, label="contagion split (different speaker)")
ax.scatter(ine, y, color=AMBER, s=60, zorder=3, label="inertia split (same speaker)")
ax.set_yticks(y, emo)
ax.set_xlim(0, .8)
ax.set_xlabel("Self-loop posterior mean  T̄_jj  (EmotionLines)")
ax.legend(loc="lower right", frameon=False, fontsize=9.5)
save(fig, "inertia-contagion.png")

# 3. Pairwise off-diagonal Pearson correlations across five sources (Table III: tab:cross-corpus).
names = ["EmotionLines", "MELD", "DailyDialog", "M3ED (zh)", "DailyDialog-LLM"]
R = np.full((5, 5), np.nan)
vals = {(0, 1): .910, (0, 2): .944, (0, 3): .854, (0, 4): .976,
        (1, 2): .916, (1, 3): .814, (1, 4): .952,
        (2, 3): .795, (2, 4): .979, (3, 4): .847}
for (i, j), v in vals.items():
    R[j, i] = v  # lower triangle
fig, ax = plt.subplots(figsize=(5.8, 4.6))
cmap = matplotlib.colors.LinearSegmentedColormap.from_list("w2a", ["#F4EEE3", AMBER, "#7B5E28"])
cmap.set_bad("white")
im = ax.imshow(R[1:, :4], cmap=cmap, vmin=.75, vmax=1.0)  # drop empty row/column
for (i, j), v in vals.items():
    ax.text(i, j - 1, f"{v:.3f}", ha="center", va="center", fontsize=10.5,
            color="white" if v > .93 else INK)
ax.set_xticks(range(4), names[:4], rotation=35, ha="right")
ax.set_yticks(range(4), names[1:])
for s in ax.spines.values():
    s.set_visible(False)
ax.tick_params(length=0)
cb = fig.colorbar(im, ax=ax, fraction=.04, pad=.03)
cb.set_label("Pearson r over 42 off-diagonal cells")
cb.outline.set_visible(False)
save(fig, "cross-corpus.png")

# 4. Stage-2 inertia vs. contagion indices (Table IV: tab:spectral-indices).
emo2 = ["neutral", "joy", "sadness", "fear", "anger", "surprise", "disgust"]
I = [.378, .338, .227, .162, .206, .177, .123]
C = [.025, .011, .010, .046, .028, .031, .052]
fig, ax = plt.subplots(figsize=(6.4, 4.2))
for e, x, yv in zip(emo2, I, C):
    c = AMBER if e in ("neutral", "joy") else STEEL if e in ("disgust", "fear") else GREY
    ax.scatter(x, yv, s=80, color=c, zorder=3)
    off = {"neutral": (-6, 8), "joy": (6, 6), "sadness": (6, -12), "fear": (8, 2),
           "anger": (8, -2), "surprise": (8, 2), "disgust": (8, 2)}[e]
    ax.annotate(e, (x, yv), xytext=off, textcoords="offset points", fontsize=10.5,
                ha="right" if off[0] < 0 else "left")
ax.set_xlabel("Inertia index  I_j  (low-frequency band)")
ax.set_ylabel("Contagion index  C_j  (high-frequency band)")
ax.set_xlim(.09, .42)
ax.set_ylim(0, .06)
save(fig, "spectral-indices.png")

# 5. Robustness: rater subsampling and downstream use (Table VI: tab:ablation).
fig, (a1, a2) = plt.subplots(1, 2, figsize=(9.2, 3.4), gridspec_kw={"width_ratios": [1, 1.25]})
rs = ["R = 2", "R = 3", "R = 4"]
rv = [.991, .997, .999]
a1.bar(rs, rv, color=[LIGHT, LIGHT, LIGHT], edgecolor=GREY, width=.55)
for i, v in enumerate(rv):
    a1.text(i, v + .0005, f"{v:.3f}", ha="center", fontsize=10)
a1.set_ylim(.98, 1.0)
a1.set_ylabel("Pearson r vs. all 5 raters")
a1.set_title("(a) Fewer raters per utterance", fontsize=11, loc="left")
models = ["LogReg + lag-5", "GRU 2-stream", "DistilBERT (frozen)"]
# LogReg: the table reports only "0.265 (no gain)", so no separate "without" bar is drawn.
before = [None, .191, .434]
after = [.265, .205, .440]
x = np.arange(3)
a2.bar(x[1:] - .18, before[1:], width=.34, color=GREY, label="without BSETD lift")
a2.bar(x + .18, after, width=.34, color=AMBER, label="with BSETD lift")
for i in range(3):
    if before[i] is not None:
        a2.text(i - .18, before[i] + .01, f"{before[i]:.3f}", ha="center", fontsize=9)
    a2.text(i + .18, after[i] + .01, f"{after[i]:.3f}", ha="center", fontsize=9)
a2.set_xlim(-.6, 2.6)
a2.text(0 + .18, .30, "(no gain)", ha="center", fontsize=9, color="#555")
a2.set_xticks(x, models)
a2.set_ylim(0, .55)
a2.set_ylabel("Next-emotion macro-F1")
a2.set_title("(b) Lift features in downstream predictors", fontsize=11, loc="left")
a2.legend(frameon=False, fontsize=9, loc="upper left")
fig.tight_layout(w_pad=2.5)
save(fig, "robustness.png")
print("done")
