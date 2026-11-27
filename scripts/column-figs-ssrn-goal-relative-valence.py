"""Figures for the research-blog post on "Language Models Read the Word Before They
Weigh the Stake" (SSRN 7580938). Every number is copied from the SSRN manuscript
(GoalRelativeValence_ARR2026Oct/04_原稿/en_ssrn, built PDF main_en_SSRN_nonanon_20261008.pdf);
nothing is recomputed. The overview figure (overview.png) is the paper's own Figure 1,
converted from figures/fig_overview4.pdf with pdftoppm, not drawn here."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

OUT = "/Users/ishitatakashishou/Sites/affectosphere-lab/public/column-images/ssrn-goal-relative-valence/"
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


# 1. Lexical leakage audit (Table 1 / Appendix D): bag-of-words vs best layer-wise probe.
data = ["SST-2", "GoEmotions", "Our stimuli"]
bow = [.75, .77, .50]
probe = [(.88, .91), (.78, .81), None]  # range over 10 models; no probe row for our stimuli
fig, ax = plt.subplots(figsize=(7.2, 3.0))
y = np.arange(3)[::-1]
for yi, b, p in zip(y, bow, probe):
    ax.barh(yi + .17, b, height=.32, color=GREY)
    ax.text(b + .01, yi + .17, f"{b:.2f}", va="center", fontsize=10)
    if p:
        ax.barh(yi - .17, p[1], height=.32, color=STEEL)
        ax.text(p[1] + .01, yi - .17, f"{p[0]:.2f}–{p[1]:.2f}", va="center", fontsize=10)
    else:
        ax.text(b + .09, yi + .17, "(outcome at chance from words; no probe row)", va="center",
                fontsize=9.5, color="#666")
ax.axvline(.5, color="#999", ls=":", lw=1)
ax.set_yticks(y, data)
ax.set_xlim(0, 1.08)
ax.set_xlabel("Accuracy")
from matplotlib.patches import Patch
ax.legend(handles=[Patch(color=GREY, label="bag-of-words classifier"),
                   Patch(color=STEEL, label="best layer-wise probe (range over 10 models)")],
          frameon=False, loc="lower center", bbox_to_anchor=(.5, 1.0), ncol=2, fontsize=9.5)
save(fig, "leak-audit.png")

# 2. Middle vs late band conflict-cell AUC per model (Appendix E, Table 4).
models = ["Qwen2.5-7B-Inst.", "Mistral-7B-Inst.", "Falcon3-7B-Inst.", "Granite-3.1-8B-Inst.",
          "OLMo-2-7B-Inst. †", "Phi-4 (14B)", "Qwen2.5-14B-Inst.", "Qwen2.5-32B-Inst."]
eot_mid = [.01, .10, .00, .12, .11, .04, .00, .00]
eot_late = [.35, .78, .40, .61, .58, .59, .61, .56]
rsp_mid = [.24, .34, .15, .50, .31, .42, .09, .09]
rsp_late = [.83, 1.00, .95, 1.00, .71, .88, .98, .87]
fig, axes = plt.subplots(1, 2, figsize=(8.4, 3.9), sharey=True)
y = np.arange(len(models))[::-1]
for ax, mid, late, ttl in [(axes[0], eot_mid, eot_late, "End of text"),
                           (axes[1], rsp_mid, rsp_late, "Response position")]:
    for yi, a, b in zip(y, mid, late):
        ax.plot([a, b], [yi, yi], color=LIGHT, lw=2.4, zorder=1)
    ax.scatter(mid, y, color=GREY, s=36, zorder=2, label="middle band (0.20–0.45)")
    ax.scatter(late, y, color=AMBER, s=46, zorder=3, label="late band (0.60–0.90)")
    ax.axvline(.5, color="#999", ls=":", lw=1)
    ax.set_xlim(-.03, 1.05)
    ax.set_title(ttl, fontsize=11)
    ax.set_xlabel("Conflict-cell AUC for the stake")
axes[0].set_yticks(y, models)
axes[0].text(.02, -1.0, "← follows the wording", fontsize=9, color="#666")
axes[0].text(.62, -1.0, "follows the stake →", fontsize=9, color="#666")
axes[0].set_ylim(-1.4, len(models) - .4)
axes[1].legend(frameon=False, loc="lower left", fontsize=9, bbox_to_anchor=(0.0, -0.02))
fig.tight_layout()
save(fig, "bands.png")

# 3. Transition depth d* at the response position (Table 4) with the patching
#    crossing-depth range 0.38–0.64 reported in Section 4.6.
dstar = [.54, .40, .49, .37, .41, .36, .53, .45]
fig, ax = plt.subplots(figsize=(7.2, 3.4))
ax.axvspan(.38, .64, color=STEEL, alpha=.12, lw=0)
ax.text(.51, len(models) - .35, "patching crossing depth\n(range over models: 0.38–0.64)",
        ha="center", va="bottom", fontsize=9.5, color=STEEL)
ax.scatter(dstar, y, color=AMBER, s=50, zorder=3)
for yi, d in zip(y, dstar):
    ax.text(d + .012, yi, f"{d:.2f}", va="center", fontsize=9.5)
ax.set_yticks(y, models)
ax.set_xlim(.2, .8)
ax.set_ylim(-.6, len(models) + .7)
ax.set_xlabel("Relative depth of the transition d* (response position)")
save(fig, "transition-depth.png")

# 4. Controls and the question before the response (Sections 4.4 and 4.5): only
#    the ranges stated in the text are drawn (late-band AUC, response position).
rows = [("Valence, no extra question", .71, 1.00, AMBER),
        ("Location control (upper bound)", None, .44, GREY),
        ("Material control (upper bound)", None, .46, GREY),
        ("Q: evaluative ('good or bad?')", .75, 1.00, AMBER),
        ("Q: 'who is named?'", .00, .37, STEEL),
        ("Q: 'how many sentences?'", .11, .52, STEEL)]
fig, ax = plt.subplots(figsize=(7.2, 3.4))
yy = np.arange(len(rows))[::-1]
for yi, (lab, lo, hi, c) in zip(yy, rows):
    if lo is None:
        ax.plot([hi], [yi], marker="<", color=c, ms=9)
        ax.text(hi - .03, yi, f"≤ {hi:.2f}", va="center", ha="right", fontsize=9.5)
    else:
        ax.plot([lo, hi], [yi, yi], color=c, lw=6, solid_capstyle="butt")
        ax.text(hi + .02, yi, f"{lo:.2f}–{hi:.2f}", va="center", fontsize=9.5,
                bbox=dict(fc="white", ec="none", pad=.5))
ax.axvline(.5, color="#999", ls=":", lw=1)
ax.axhline(2.5, color="#ccc", lw=.8)
ax.set_yticks(yy, [r[0] for r in rows])
ax.set_xlim(0, 1.18)
ax.set_xlabel("Late-band conflict-cell AUC at the response position (range over models)")
save(fig, "controls-task.png")

# 5. Behavioural regression J = bA*A + bL*L + bAL*AL (Table 3): stake vs wording coefficient.
bmodels = ["Qwen2.5-7B-Inst.", "Mistral-7B-Inst.", "Falcon3-7B-Inst.", "Granite-3.1-8B-Inst.",
           "OLMo-2-7B-Inst. †", "Phi-4 (14B)", "Qwen2.5-14B-Inst.", "Qwen2.5-32B-Inst.",
           "Qwen2.5-7B (base) †", "OLMo-2-7B (base) †"]
bA = [25.1, 20.0, 12.3, 13.1, 8.6, 20.9, 48.5, 51.2, 2.7, 1.4]
bL = [7.1, 4.0, 3.0, 2.9, 1.9, 3.1, 5.6, 6.2, 1.5, 1.0]
fig, ax = plt.subplots(figsize=(7.2, 4.0))
yb = np.arange(len(bmodels))[::-1]
ax.barh(yb + .19, bA, height=.36, color=STEEL, label="βA  stakeholder's outcome")
ax.barh(yb - .19, bL, height=.36, color=AMBER, label="βL  surface wording")
for yi, a, l in zip(yb, bA, bL):
    ax.text(a + .6, yi + .19, f"{a:.1f}", va="center", fontsize=8.5)
    ax.text(l + .6, yi - .19, f"{l:.1f}", va="center", fontsize=8.5)
ax.set_yticks(yb, bmodels)
ax.set_xlim(0, 58)
ax.set_xlabel("Regression coefficient on the good-vs-bad log-probability difference")
ax.legend(frameon=False, loc="lower right", fontsize=9.5)
save(fig, "behaviour.png")
