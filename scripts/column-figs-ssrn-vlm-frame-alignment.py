"""Figures for the research-blog post on "Frame Alignment Redirects Person-State
Attribution Toward the Wrong Person in Vision-Language Models" (SSRN 7685781).
Every number is copied from the SSRN manuscript source
(~/Desktop/研究/論文/新研究_視覚の根本課題/SSRN用_2026-11-06/source/numbers.tex,
supp_tables.tex and the tables in sec/4_experiments.tex); nothing is recomputed.
overview.png and stimulus.png are converted from the paper's own figure PDFs."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

OUT = "/Users/ishitatakashishou/Sites/affectosphere-lab/public/column-images/ssrn-vlm-frame-alignment/"
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


# 1. Alignment effect under definitions A and B (Table "tab:main"; numbers.tex
#    EightAlign*, NineAlign*, TwentyStackAlign*, RealAlign*).
studies = ["S1\nschematic", "S2\nschematic", "S3\nschematic", "S5\nphotographs"]
dA = [(.21, .13, .28), (.16, .09, .24), (.21, .13, .28), (.18, .11, .25)]
dB = [(.03, -.02, .07), (.00, -.04, .04), (.05, .00, .10), (.17, .11, .23)]
x = np.arange(4); w = .34
fig, ax = plt.subplots(figsize=(7.2, 3.4))
for off, data, c, lab in [(-w/2, dA, AMBER, "Definition A (position in frame 1)"),
                          (w/2, dB, STEEL, "Definition B (individual fixed in words)")]:
    m = np.array([d[0] for d in data]); lo = np.array([d[1] for d in data]); hi = np.array([d[2] for d in data])
    ax.bar(x + off, m, w, color=c, label=lab, yerr=[m - lo, hi - m], capsize=3,
           error_kw=dict(ecolor="#333", lw=1))
    for xi, mi, h in zip(x + off, m, hi):
        ax.text(xi, h + .012, f"{mi:+.2f}" if mi else "0.00", ha="center", fontsize=9.5)
ax.axhline(0, color="#444", lw=.8)
ax.set_xticks(x, studies)
ax.set_ylim(-.06, .38)
ax.set_ylabel("Alignment effect  E(s=0) − E(s=1)")
ax.legend(frameon=False, loc="upper left", fontsize=9.5, ncol=1)
save(fig, "align-effect.png")

# 2. Graded shifts (Figure "fig:dose"; numbers.tex DoseEA*/DoseEB* for S4,
#    RealEA*/RealEB* for S5). Bootstrap bands of the paper figure are not in the text, so omitted.
fig, axes = plt.subplots(1, 2, figsize=(7.4, 3.2), sharey=True)
s4 = [0, .25, .5, .75, 1]
axes[0].plot(s4, [.52, .44, .32, .31, .30], "-o", color=AMBER, lw=1.8, label="A: position in frame 1")
axes[0].plot(s4, [.09, .05, .04, .03, .06], "--s", color=STEEL, lw=1.6, label="B: individual fixed in words")
axes[0].set_title("S4  schematic people", fontsize=11)
s5 = [0, .5, 1]
axes[1].plot(s5, [.52, .44, .34], "-o", color=AMBER, lw=1.8)
axes[1].plot(s5, [.38, .28, .21], "--s", color=STEEL, lw=1.6)
axes[1].set_title("S5  face photographs", fontsize=11)
for a in axes:
    a.set_xticks([0, .25, .5, .75, 1])
    a.set_xlabel("Shift of frame 2 (slots)")
    a.set_ylim(0, .62)
axes[0].set_ylabel("Origin error E")
fig.legend(*axes[0].get_legend_handles_labels(), loc="lower center", ncol=2,
           frameon=False, bbox_to_anchor=(.5, -.08), fontsize=10)
fig.subplots_adjust(bottom=.25, wspace=.12)
save(fig, "dose.png")

# 3. Geometric and wording controls (Table "tab:format").
ctrl = [("S2  stacked, frame 2 shifted", .16, .09, .24, AMBER),
        ("S2  stacked, both frames shifted", -.02, -.09, .06, LIGHT),
        ("S3  stacked", .21, .13, .28, AMBER),
        ("S3  side by side", .06, .00, .13, LIGHT),
        ("S3  stacked, A + neutral sentence", .33, .26, .40, STEEL)]
fig, ax = plt.subplots(figsize=(7.2, 3.0))
y = np.arange(len(ctrl))[::-1]
for yi, (lab, m, lo, hi, c) in zip(y, ctrl):
    ax.barh(yi, m, color=c, height=.58, xerr=[[m - lo], [hi - m]], capsize=3,
            error_kw=dict(ecolor="#333", lw=1))
    ax.text(max(hi, 0) + .012, yi, f"{m:+.2f}", va="center", fontsize=10)
ax.axvline(0, color="#444", lw=.8)
ax.set_yticks(y, [c[0] for c in ctrl])
ax.set_xlim(-.12, .48)
ax.set_xlabel("Alignment effect under definition A (95% CI)")
save(fig, "controls.png")

# 4. Joint answers in S7 (Figure "fig:joint"; numbers.tex SevRateB/SevRateBSh,
#    SevRateA/SevRateASh) and separate-vs-joint comparison (Table "tab:sepjoint").
fig, axes = plt.subplots(1, 2, figsize=(7.6, 3.2), gridspec_kw=dict(width_ratios=[1, 1.15]))
ax = axes[0]
xx = np.arange(2); w = .36
ax.bar(xx - w/2, [.14, .04], w, color=AMBER, label="Old place + origin state (J_old)")
ax.bar(xx + w/2, [.00, .01], w, color=STEEL, label="Correct place + origin state (J_cor)")
for xi, v in zip(xx - w/2, [.14, .04]):
    ax.text(xi, v + .006, f"{v:.2f}", ha="center", fontsize=9.5)
for xi, v in zip(xx + w/2, [.00, .01]):
    ax.text(xi, v + .006, f"{v:.2f}", ha="center", fontsize=9.5)
ax.set_xticks(xx, ["s = 0\n(aligned)", "s = 1\n(shifted)"])
ax.set_ylim(0, .24)
ax.set_ylabel("Rate on gated scenes")
ax.set_title("S7  one joint answer", fontsize=11)
ax = axes[1]
src = ["Separate place\nand state prompts", "One joint\nanswer"]
okx = [.18, .00]; oldx = [.09, .14]
ax.bar(xx - w/2, oldx, w, color=AMBER)
ax.bar(xx + w/2, okx, w, color=STEEL)
for xi, v in zip(xx - w/2, oldx):
    ax.text(xi, v + .006, f"{v:.2f}", ha="center", fontsize=9.5)
for xi, v in zip(xx + w/2, okx):
    ax.text(xi, v + .006, f"{v:.2f}", ha="center", fontsize=9.5)
ax.set_xticks(xx, src)
ax.set_ylim(0, .24)
ax.set_title("S7 at s = 0: where the answers come from", fontsize=11)
fig.legend(*axes[0].get_legend_handles_labels(), loc="lower center", ncol=2,
           frameon=False, bbox_to_anchor=(.5, -.1), fontsize=9.5)
fig.subplots_adjust(bottom=.28, wspace=.25)
save(fig, "joint.png")

# 5. Badge intervention in S8 (Figure "fig:badge"; numbers.tex BadgeRate*,
#    BadgePosRate, BadgePosRateSh, BadgeNoneRateSh, BadgePersonRateSh).
conds = ["No badge", "Person-fixed\nbadge", "Person-fixed badge\n+ number in prompt", "Position-fixed\nbadge"]
s0 = [.18, .07, .03, .63]
s1 = [.04, .00, None, .34]
cols = [GREY, STEEL, STEEL, AMBER]
fig, ax = plt.subplots(figsize=(7.2, 3.4))
xx = np.arange(4); w = .36
for i in range(4):
    ax.bar(xx[i] - w/2, s0[i], w, color=cols[i])
    ax.text(xx[i] - w/2, s0[i] + .012, f"{s0[i]:.2f}", ha="center", fontsize=9.5)
    if s1[i] is not None:
        ax.bar(xx[i] + w/2, s1[i], w, color=cols[i], alpha=.4, hatch="///", edgecolor="white")
        ax.text(xx[i] + w/2, s1[i] + .012, f"{s1[i]:.2f}", ha="center", fontsize=9.5)
    else:
        ax.text(xx[i] + w/2, .015, "n/r", ha="center", fontsize=9, color="#777")
ax.set_xticks(xx, conds, fontsize=9.5)
ax.set_ylim(0, .72)
ax.set_ylabel("Coherent misattribution J_old")
from matplotlib.patches import Patch
ax.legend([Patch(color="#888"), Patch(facecolor="#888", alpha=.4, hatch="///", edgecolor="white")],
          ["s = 0 (aligned)", "s = 1 (shifted)"], frameon=False, loc="upper left")
save(fig, "badge.png")

# 6. Six models in S9 (supp Table "tab:supp-s9", SuppNineRows: B at s=0 without badge,
#    B with person badge, B with position badge).
models = [("Qwen3-VL-8B", .16, .05, .59, True),
          ("InternVL3.5-14B", .17, .09, .35, True),
          ("InternVL3.5-8B", .24, .12, .42, False),
          ("Gemma-3-12B", .13, .09, .22, False),
          ("Gemma-3-27B", .28, .14, .36, False),
          ("Mistral-Small\n3.1-24B", .19, .10, .13, False)]
fig, ax = plt.subplots(figsize=(8.4, 3.8))
xx = np.arange(len(models)); w = .26
for i, (name, nb, pe, po, valid) in enumerate(models):
    a = 1 if valid else .38
    ax.bar(i - w, pe, w, color=STEEL, alpha=a)
    ax.bar(i, nb, w, color=GREY, alpha=a)
    ax.bar(i + w, po, w, color=AMBER, alpha=a)
ax.set_xticks(xx, [m[0] + ("\n(valid)" if m[4] else "\n(descriptive)") for m in models], fontsize=8.8)
ax.set_ylim(0, .68)
ax.set_ylabel("J_old at s = 0")
ax.legend([Patch(color=STEEL), Patch(color=GREY), Patch(color=AMBER)],
          ["Person-fixed badge", "No badge", "Position-fixed badge"], frameon=False,
          loc="upper right", fontsize=9.5)
save(fig, "models.png")
print("done")
