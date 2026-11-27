"""Figures for the ssrn-behavioral-steering research-blog post.

Every number is copied from the P1 manuscript
(~/Desktop/研究/論文/感情に対応する内部状態がAIの推論能力を変える/
 プロジェクト1_制御可能性の二重解離/04_原稿/Neurocomputing投稿用/sections/,
 sec5_experiments.tex, P1_Table2_v1.tex, P1_Table3_v1.tex). Nothing is recomputed.
The method and task figures are the paper's own PDFs, rasterised with pdftoppm.
"""
import os
import subprocess
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

OUT = "/Users/ishitatakashishou/Sites/affectosphere-lab/public/column-images/ssrn-behavioral-steering/"
SRC = os.path.expanduser(
    "~/Desktop/研究/論文/感情に対応する内部状態がAIの推論能力を変える/"
    "プロジェクト1_制御可能性の二重解離/04_原稿/Neurocomputing投稿用/figures/")
os.makedirs(OUT, exist_ok=True)

AMBER, STEEL, GREY, LIGHT = "#C4974A", "#3D6B8C", "#9AA0A6", "#D9D4CB"
plt.rcParams.update({
    "font.family": "Arial", "font.size": 11, "axes.edgecolor": "#444",
    "axes.linewidth": 0.8, "axes.spines.top": False, "axes.spines.right": False,
    "xtick.color": "#333", "ytick.color": "#333", "axes.labelcolor": "#222",
    "savefig.dpi": 220, "savefig.bbox": "tight", "savefig.facecolor": "white",
})


def save(fig, name):
    fig.savefig(OUT + name)
    plt.close(fig)


# 0. Paper figures (Figure 1 = framework, Figure 2 = task), read-only source.
for src, dst in [("fig_method_v4", "framework"), ("fig_task_v3", "task")]:
    subprocess.run(["pdftoppm", "-png", "-r", "220", "-singlefile",
                    SRC + src + ".pdf", OUT + dst], check=True)

# 1. Interchange: real direction vs optimisation-matched nulls (Sec. 5.2 text).
#    Qwen3-8B held-out fold: real F_c 0.883; nulls mean 0.464, max 0.714; p_O = 0.020.
#    OLMo-2-7B: real 1.08; nulls mean 0.527, max 0.929; p_O = 0.020.
models = ["Qwen3-8B", "OLMo-2-7B"]
real = [0.883, 1.08]; nmean = [0.464, 0.527]; nmax = [0.714, 0.929]
x = np.arange(2); w = .25
fig, ax = plt.subplots(figsize=(7.2, 3.4))
ax.bar(x - w, nmean, w, color=LIGHT, label="Matched nulls: mean (n = 50)")
ax.bar(x, nmax, w, color=GREY, label="Matched nulls: max")
ax.bar(x + w, real, w, color=AMBER, label="Real direction $w_{c\\neg v}$")
for xi, a, b, c in zip(x, nmean, nmax, real):
    ax.text(xi - w, a + .02, f"{a:.3f}", ha="center", fontsize=9.5)
    ax.text(xi, b + .02, f"{b:.3f}", ha="center", fontsize=9.5)
    ax.text(xi + w, c + .02, "0.883" if c == .883 else "1.08", ha="center", fontsize=9.5)
    ax.text(xi, 1.25, "$p_O$ = 0.020", ha="center", fontsize=10, color="#555")
ax.set_xticks(x, models)
ax.set_ylim(0, 1.35)
ax.set_ylabel("Transfer fraction $F_c$ (interchange)")
ax.legend(frameon=False, loc="upper left", fontsize=9.5, ncol=3, bbox_to_anchor=(0, -.12))
save(fig, "interchange-nulls.png")

# 2. Natural-amplitude interchange during generation (Table 2, P1_Table2_v1.tex).
rows = [("Qwen3-8B  $w_{c\\neg v}$", -0.0002, 1.000, 0.021, 0.190),
        ("Qwen3-8B  $w_{v\\neg c}$", 0.027, 0.095, 0.014, 0.476),
        ("OLMo-2-7B  $w_{c\\neg v}$", 0.004, 0.810, -0.040, 0.095),
        ("OLMo-2-7B  $w_{v\\neg c}$", -0.041, 0.143, -0.016, 0.476)]
y = np.arange(len(rows))[::-1]; h = .34
fig, ax = plt.subplots(figsize=(7.2, 3.4))
for yi, (lab, sh, psh, cl, pcl) in zip(y, rows):
    ax.barh(yi + h/2, sh, h, color=STEEL)
    ax.barh(yi - h/2, cl, h, color=AMBER)
    sh_txt = "−0.0002" if sh == -0.0002 else f"{sh:+.3f}".replace("-", "−")
    ax.text(.052, yi + h/2, f"shift {sh_txt}  (p = {psh:.3f})", va="center", fontsize=9)
    ax.text(.052, yi - h/2, f"clamp {cl:+.3f}".replace("-", "−") + f"  (p = {pcl:.3f})", va="center", fontsize=9)
ax.axvline(0, color="#444", lw=.8)
ax.set_yticks(y, [r[0] for r in rows])
ax.set_xlim(-.06, .13)
ax.set_xticks([-.05, -.025, 0, .025, .05])
ax.set_xlabel("Δ switch probability after a lost packet")
from matplotlib.patches import Patch
ax.legend(handles=[Patch(color=STEEL, label="Shift"), Patch(color=AMBER, label="Clamp")],
          frameon=False, loc="upper left", fontsize=9.5, bbox_to_anchor=(0, -.2), ncol=2)
save(fig, "natural-amplitude.png")

# 3. Selectivity S(alpha) under additive steering (Sec. 5.4 text).
#    Qwen3-8B w_c¬v: 0.412 (0.26), 0.411 (0.5), 0.365 (1), 0.246 (2), -0.007 (8).
#    Matched-null 95th percentile at alpha 0.26-1: between 0.575 and 0.599 (range only).
#    OLMo-2-7B w_c¬v: 0.406 (0.26), 0.020 (16), -0.012 (32).
fig, ax = plt.subplots(figsize=(7.2, 3.6))
qa = [0.26, 0.5, 1, 2, 8]; qs = [0.412, 0.411, 0.365, 0.246, -0.007]
oa = [0.26, 16, 32]; os_ = [0.406, 0.020, -0.012]
ax.fill_between([0.26, 1], 0.575, 0.599, color=GREY, alpha=.45, lw=0)
ax.text(0.27, 0.615, "matched-null 95th pct. (0.575–0.599, α = 0.26–1)", fontsize=9.5, color="#555")
ax.plot(qa, qs, "-o", color=AMBER, lw=1.8, ms=6, label="Qwen3-8B  $w_{c\\neg v}$")
ax.plot(oa, os_, "s", color=STEEL, ms=7, label="OLMo-2-7B  $w_{c\\neg v}$ (reported doses only)")
ax.axhline(0, color="#444", lw=.8)
ax.set_xscale("log")
ax.set_xticks([0.26, 0.5, 1, 2, 8, 16, 32], ["0.26", "0.5", "1", "2", "8", "16", "32"])
ax.set_ylim(-.1, .7)
ax.set_xlabel("Dose α (multiples of the natural gap g)")
ax.set_ylabel("Selectivity S(α)")
ax.legend(frameon=False, loc="lower left", fontsize=9.5)
save(fig, "selectivity.png")

# 4. Random vs optimisation-matched nulls, p-values for each test (Table 3 + Sec. 5.2/5.5/5.7).
tests = [("Interchange $F_c$, Qwen3-8B", None, 0.020),
         ("Selectivity, Qwen3-8B $w_{c\\neg v}$", 0.020, 0.529),
         ("Selectivity, Qwen3-8B $w_{v\\neg c}$", 0.020, 0.510),
         ("Selectivity, OLMo-2-7B $w_{c\\neg v}$", 0.039, 0.412),
         ("Behaviour α = 1, Qwen3-8B $w_{c\\neg v}$", 0.039, 0.059),
         ("Behaviour α = 8, Qwen3-8B $w_{c\\neg v}$", 0.020, 0.078),
         ("Rule: selectivity α = 1", 0.020, 0.020),
         ("Rule: behaviour, generated tokens", 0.392, 0.980),
         ("Rule: behaviour, choice position", 0.020, 0.588),
         ("Rule: interchange at choice", 0.020, 0.412)]
y = np.arange(len(tests))[::-1]
fig, ax = plt.subplots(figsize=(7.2, 4.6))
ax.axvspan(0, 0.05, color=AMBER, alpha=.12, lw=0)
ax.axvline(0.05, color="#7B5E28", ls="--", lw=1)
ax.text(0.055, y[0] + .55, "p = 0.05", color="#7B5E28", fontsize=9.5)
for yi, (lab, pr, po) in zip(y, tests):
    if pr is not None:
        ax.plot([pr, po], [yi, yi], color=LIGHT, lw=1.5, zorder=1)
        ax.plot(pr, yi, "o", color=GREY, ms=7, zorder=2)
    ax.plot(po, yi, "D", color=STEEL, ms=7, zorder=3)
ax.plot([], [], "o", color=GREY, label="vs random directions ($p_R$)")
ax.plot([], [], "D", color=STEEL, label="vs optimisation-matched nulls ($p_O$)")
ax.set_yticks(y, [t[0] for t in tests])
ax.set_xlim(0, 1.02)
ax.set_ylim(-.7, len(tests) - .2)
ax.set_xlabel("Empirical p-value (50 nulls per family; minimum 0.020)")
ax.legend(frameon=False, loc="lower right", fontsize=9.5)
save(fig, "null-pvalues.png")

# 5. Rule positive control (Sec. 5.6-5.7).
fig, (a1, a2) = plt.subplots(1, 2, figsize=(7.6, 3.4), gridspec_kw=dict(width_ratios=[1.35, 1]))
# (a) behavioural effect vs dose; A_S = {0.26, 0.5, 1}.
a1.axvspan(0.22, 1.15, color=AMBER, alpha=.12, lw=0)
a1.text(0.5, 0.425, "$A_S$", ha="center", color="#7B5E28", fontsize=10)
a1.plot([0.26, 0.5, 1, 8], [0.002, 0.019, 0.033, 0.231], "-o", color=AMBER, lw=1.8, label="push on generated tokens")
a1.plot([4, 8], [0.064, 0.095], "--s", color=STEEL, lw=1.4, label="push at choice position")
a1.text(0.27, 0.06, "choice position\nwithin $A_S$: B ≤ 0.001", fontsize=8.5, color=STEEL)
a1.set_xscale("log")
a1.set_xticks([0.26, 0.5, 1, 4, 8], ["0.26", "0.5", "1", "4", "8"])
a1.minorticks_off()
a1.set_ylim(-.02, .45)
a1.set_xlabel("Dose α")
a1.set_ylabel("Behavioural effect B(α)")
a1.legend(frameon=False, loc="upper left", fontsize=8.5, bbox_to_anchor=(.0, .9))
a1.set_title("(a) Steering the rule direction", fontsize=10.5, loc="left")
# (b) interchange at the choice position: share of the 0.718 switch-probability gap.
a2.bar([0, 1], [74, 0.01], color=[STEEL, AMBER], width=.55)
a2.text(0, 76, "74%", ha="center", fontsize=10)
a2.text(1, 3, "< 0.01%", ha="center", fontsize=10)
a2.set_xticks([0, 1], ["Full hidden\nstate", "Rule direction\n$w_{p\\neg v}$"])
a2.set_ylim(0, 90)
a2.set_ylabel("Share of switch gap transferred (%)")
a2.set_title("(b) Interchange at the choice", fontsize=10.5, loc="left")
fig.tight_layout()
save(fig, "rule-control.png")
print("done")
