"""Figures for the LSLM-BCF research-blog post. Every number is copied from the
IEEE SocialCom 2026 author version (revised_3_review/overleaf_upload: tables/*.tex
and the macros in numbers*.tex used by sections/04_experiments.tex); nothing is
recomputed. The method figures (architecture / prl-loss / fusion) are the paper's
own PDFs converted with pdftoppm and are not produced here."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

OUT = "/Users/ishitatakashishou/Sites/affectosphere-lab/public/column-images/socialcom2026-lslm-bcf/"
AMBER, STEEL, GREY, LIGHT, INK = "#C4974A", "#3D6B8C", "#9AA0A6", "#D9D4CB", "#1A1A1A"
plt.rcParams.update({
    "font.family": "Arial", "font.size": 11, "axes.edgecolor": "#444",
    "axes.linewidth": 0.8, "axes.spines.top": False, "axes.spines.right": False,
    "xtick.color": "#333", "ytick.color": "#333", "axes.labelcolor": "#222",
    "savefig.dpi": 220, "savefig.bbox": "tight", "savefig.facecolor": "white",
})
DS = ["iSarcasm", "EPIC", "MUStARD", "SCv2"]


def save(fig, name):
    fig.savefig(OUT + name)
    plt.close(fig)


# 1. Macro-F1 on the four test sets (Table tab_all, F1 columns; subset of rows).
rows = [("Zero-shot LLM (Qwen2.5-14B)", [.604, .619, .681, .748], LIGHT),
        ("DeBERTa-v3-large", [.657, .687, .687, .825], LIGHT),
        ("Generative SFT", [.704, .708, .714, .829], GREY),
        ("Discriminative listener", [.726, .705, .704, .826], STEEL),
        ("LSLM-BCF", [.751, .714, .728, .844], AMBER)]
fig, ax = plt.subplots(figsize=(7.6, 3.6))
x = np.arange(len(DS))
w = 0.16
for i, (lab, v, c) in enumerate(rows):
    ax.bar(x + (i - 2) * w, v, w * .92, color=c, label=lab,
           edgecolor="#888" if c == LIGHT else c, lw=.5)
for xi, v in zip(x, rows[-1][1]):
    ax.text(xi + 2 * w, v + .006, f"{v:.3f}", ha="center", fontsize=8.5, color="#7B5E28")
ax.set_xticks(x, DS)
ax.set_ylim(.55, .87)
ax.set_ylabel("Macro-F1 (test, mean of 5 seeds)")
ax.legend(fontsize=8.8, frameon=False, ncol=3, loc="upper center",
          bbox_to_anchor=(.5, -.12))
save(fig, "f1-comparison.png")

# 2. Test AUC: listener alone vs LSLM-BCF (Table tab_ablation rows
#    "LSLM-BCF" and "w/o speakers"; gains match the text: +1.9/+1.8/+5.4/+1.2).
lsn = [.870, .818, .799, .909]
ful = [.889, .836, .853, .921]
gain = ["+1.9", "+1.8", "+5.4", "+1.2"]
fig, ax = plt.subplots(figsize=(7.0, 3.0))
y = np.arange(len(DS))[::-1]
for yi, a, b, g in zip(y, lsn, ful, gain):
    ax.plot([a, b], [yi, yi], color="#BBB", lw=2.2, zorder=1)
    ax.plot(a, yi, "o", color=STEEL, ms=9, zorder=2)
    ax.plot(b, yi, "o", color=AMBER, ms=9, zorder=2)
    ax.text(b + .006, yi, f"{g} pt", va="center", fontsize=10)
ax.plot([], [], "o", color=STEEL, label="Discriminative listener")
ax.plot([], [], "o", color=AMBER, label="LSLM-BCF")
ax.set_yticks(y, DS)
ax.set_xlim(.78, .95)
ax.set_ylim(-.6, 3.6)
ax.set_xlabel("Test AUC (mean of 5 seeds)")
ax.legend(frameon=False, fontsize=9.5, ncol=2, loc="upper center",
          bbox_to_anchor=(.5, 1.13))
save(fig, "auc-gain.png")

# 3. Robustness and controls on iSarcasm (Sec. IV-C text / Fig. fig_robust:
#    test stats 0.889, validation stats 0.888, permuted 0.798, negated 0.585,
#    listener alone 0.870).
rb = [("LSLM-BCF, test statistics", .889, AMBER),
      ("LSLM-BCF, validation statistics", .888, AMBER),
      ("Control: speaker score permuted", .798, LIGHT),
      ("Control: speaker score negated", .585, LIGHT)]
fig, ax = plt.subplots(figsize=(7.0, 2.8))
y = np.arange(len(rb))[::-1]
for yi, (lab, v, c) in zip(y, rb):
    ax.barh(yi, v - .5, left=.5, height=.6, color=c,
            edgecolor="#888" if c == LIGHT else c, lw=.5)
    ax.text(v + .005, yi, f"{v:.3f}", va="center", fontsize=10)
ax.axvline(.870, color=STEEL, ls="--", lw=1.2)
ax.text(.872, y[0] + .45, "listener alone 0.870", color=STEEL, fontsize=9.5)
ax.set_yticks(y, [r[0] for r in rb])
ax.set_xlim(.5, .95)
ax.set_ylim(-.6, 3.8)
ax.set_xlabel("iSarcasm test AUC")
save(fig, "robustness.png")

# 4. Ablation, mean AUC over the four datasets (Table tab_ablation, "Mean" column).
ab = [("LSLM-BCF", .875, AMBER),
      ("w/o PRL loss", .875, LIGHT),
      ("w/o family-A speaker", .867, LIGHT),
      ("w/o family-B speaker", .864, LIGHT),
      ("w/o speakers (listener only)", .849, STEEL),
      ("w/o listener", .852, LIGHT),
      ("w/o listener and family-A speaker", .816, LIGHT),
      ("w/o listener and family-B speaker", .823, LIGHT)]
fig, ax = plt.subplots(figsize=(7.0, 3.6))
y = np.arange(len(ab))[::-1]
for yi, (lab, v, c) in zip(y, ab):
    ax.barh(yi, v - .80, left=.80, height=.62, color=c,
            edgecolor="#888" if c == LIGHT else c, lw=.5)
    ax.text(v + .001, yi, f"{v:.3f}", va="center", fontsize=9.5)
ax.set_yticks(y, [a[0] for a in ab])
ax.set_xlim(.80, .885)
ax.set_xlabel("Mean test AUC over four datasets")
save(fig, "ablation.png")

# 5. Gain over the listener by sarcasm mechanism (Sec. IV-F text and Fig. fig_mech;
#    cross-validated iSarcasm validation posts, 87 sarcastic vs 259 sincere).
#    Left: two-speaker gain with n. Right: single-family speaker gains (MxA*, MxB*).
mech = [("Tone markers", 4.7, 36), ("Exaggeration", 1.9, 28),
        ("Polarity reversal", 0.1, 33), ("Pretense", -3.4, 6),
        ("No clear mechanism", -0.6, 13)]
fig, (a1, a2) = plt.subplots(1, 2, figsize=(8.2, 3.2),
                             gridspec_kw=dict(width_ratios=[1.35, 1]))
y = np.arange(len(mech))[::-1]
for yi, (lab, g, n) in zip(y, mech):
    c = AMBER if lab == "Tone markers" else (LIGHT if g <= 0 else "#E2C99A")
    a1.barh(yi, g, height=.6, color=c, edgecolor="#888" if c == LIGHT else c, lw=.5)
    tx = 9.8 if lab == "Tone markers" else g
    a1.text(tx + (.25 if g >= 0 else -.25), yi, f"{g:+.1f}  (n={n})", va="center",
            ha="left" if g >= 0 else "right", fontsize=9)
a1.errorbar(4.7, y[0], xerr=[[4.7 - .3], [9.5 - 4.7]], fmt="none",
            ecolor="#333", capsize=3, lw=1)
a1.axvline(0, color="#444", lw=.8)
a1.set_yticks(y, [m[0] for m in mech])
a1.set_xlim(-10, 16)
a1.set_xlabel("AUC gain over listener (points)\nerror bar: 95% CI, reported for tone markers only")
a1.set_title("Two-speaker LSLM-BCF", fontsize=10.5)
fam = [("Tone markers", 2.8, 4.1), ("Exaggeration", 3.2, -0.8)]
yy = np.arange(2)[::-1]
for yi, (lab, a, b) in zip(yy, fam):
    a2.barh(yi + .18, a, height=.34, color=AMBER)
    a2.barh(yi - .18, b, height=.34, color=STEEL)
    a2.text(a + (.15 if a >= 0 else -.15), yi + .18, f"{a:+.1f}", va="center",
            ha="left" if a >= 0 else "right", fontsize=9)
    a2.text(b + (.15 if b >= 0 else -.15), yi - .18, f"{b:+.1f}", va="center",
            ha="left" if b >= 0 else "right", fontsize=9)
from matplotlib.patches import Patch
a2.axvline(0, color="#444", lw=.8)
a2.set_yticks(yy, [f[0] for f in fam])
a2.set_xlim(-2.5, 5.8)
a2.set_ylim(-.7, 1.7)
a2.set_xlabel("AUC gain over listener (points)")
a2.set_title("One speaker fused with listener", fontsize=10.5)
a2.legend(handles=[Patch(color=AMBER, label="family-A speaker only"),
                   Patch(color=STEEL, label="family-B speaker only")],
          frameon=False, fontsize=8.5, loc="upper center", bbox_to_anchor=(.5, -.25), ncol=1)
fig.tight_layout(w_pad=2.5)
save(fig, "mechanism.png")
print("done")
