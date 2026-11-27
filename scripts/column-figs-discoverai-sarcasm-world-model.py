"""Figures for the WM-SAR research-blog post (Discover Artificial Intelligence).
Every number is copied from the R1 manuscript (manuscript_R1_clean/English.tex
tables and the manuscript's ablation figure); nothing is recomputed."""
import shutil
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

SRC = "/Users/ishitatakashishou/Desktop/研究/論文/皮肉検出に関する研究/世界モデルもどき/manuscript_R1_clean/"
OUT = "/Users/ishitatakashishou/Sites/affectosphere-lab/public/column-images/discoverai-sarcasm-world-model/"
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

# 0. The paper's own figures, copied unchanged (Fig. framework, Fig. lr_weights).
shutil.copy(SRC + "framework.png", OUT + "framework.png")
shutil.copy(SRC + "lr_weight_analysis.png", OUT + "lr-weights.png")

# 1. Main comparison, Macro-F1 per dataset (Table: perf_comp).
methods = ["MIARN", "SAWS", "DC-Net", "BERT", "GPT-4.1-mini", "+CoC", "+GoC", "+BoC", "CAF-I", "WM-SAR"]
f1 = {  # IAC-V1, IAC-V2, SemEval-2018, Avg.
    "MIARN": (.641, .735, .650, .675), "SAWS": (.476, .598, .600, .558),
    "DC-Net": (.557, .713, .675, .648), "BERT": (.655, .790, .694, .713),
    "GPT-4.1-mini": (.724, .768, .698, .730), "+CoC": (.685, .775, .676, .712),
    "+GoC": (.684, .759, .650, .698), "+BoC": (.695, .773, .697, .722),
    "CAF-I": (.644, .648, .638, .643), "WM-SAR": (.745, .791, .714, .750)}
def col(m):
    if m == "WM-SAR": return AMBER
    if m == "GPT-4.1-mini": return STEEL
    if m == "BERT": return GREY
    return LIGHT
fig, axes = plt.subplots(1, 4, figsize=(11.5, 3.9), sharey=True)
for k, (ax, name) in enumerate(zip(axes, ["IAC-V1", "IAC-V2", "SemEval-2018", "Average"])):
    y = np.arange(len(methods))[::-1]
    vals = [f1[m][k] for m in methods]
    ax.barh(y, vals, color=[col(m) for m in methods], height=.7)
    for yi, v in zip(y, vals):
        ax.text(v + .004, yi, f"{v:.3f}", va="center", fontsize=8.5)
    ax.set_xlim(.45, .84)
    ax.set_title(name, fontsize=11)
    ax.set_xlabel("Macro-F1")
axes[0].set_yticks(np.arange(len(methods))[::-1], methods)
fig.tight_layout()
save(fig, "main-results.png")

# 2. Ablation, Macro-F1 (manuscript Fig. ablation, bottom row; values printed on bars).
conds = ["WM-SAR (full)", "w/o D", "w/o T", "w/o S", "w/o Interaction"]
abl = {"IAC-V1": (.745, .733, .538, .727, .733), "IAC-V2": (.791, .784, .575, .783, .783),
       "SemEval-2018": (.714, .708, .562, .720, .699), "Average": (.750, .742, .558, .743, .738)}
ccol = [AMBER, LIGHT, STEEL, LIGHT, LIGHT]
hatch = [None, None, None, "///", ".."]
fig, ax = plt.subplots(figsize=(8.6, 3.6))
x = np.arange(4)
w = .16
for i, c in enumerate(conds):
    vals = [abl[d][i] for d in abl]
    ax.bar(x + (i - 2) * w, vals, w * .92, color=ccol[i], label=c,
           edgecolor="#777" if ccol[i] == LIGHT else "none", lw=.4, hatch=hatch[i])
    for xi, v in zip(x, vals):
        ax.text(xi + (i - 2) * w, v + .004, f"{v:.3f}", ha="center", fontsize=7, rotation=90)
ax.set_xticks(x, list(abl))
ax.set_ylim(.5, .86)
ax.set_ylabel("Macro-F1")
ax.legend(ncol=5, frameon=False, fontsize=9, loc="upper center", bbox_to_anchor=(.5, -.12))
save(fig, "ablation.png")

# 3. Backbone robustness (Table: robustness), Macro-F1.
bb = ["GPT-4.1", "GPT-4.1-mini", "GPT-4.1-nano"]
rob = {"GPT-4.1": (.725, .792, .735, .751), "GPT-4.1-mini": (.745, .791, .714, .750),
       "GPT-4.1-nano": (.644, .702, .590, .646)}
bcol = [STEEL, AMBER, GREY]
fig, ax = plt.subplots(figsize=(7.6, 3.4))
w = .26
for i, b in enumerate(bb):
    ax.bar(x + (i - 1) * w, rob[b], w * .92, color=bcol[i], label=b)
    for xi, v in zip(x, rob[b]):
        ax.text(xi + (i - 1) * w, v + .005, f"{v:.3f}", ha="center", fontsize=8)
ax.set_xticks(x, ["IAC-V1", "IAC-V2", "SemEval-2018", "Average"])
ax.set_ylim(.5, .84)
ax.set_ylabel("Macro-F1 of WM-SAR")
ax.legend(frameon=False, fontsize=9.5, ncol=3, loc="upper left")
save(fig, "backbone.png")

# 4. Cost vs accuracy (Table: cost for time; Table: perf_comp for average Macro-F1).
pts = [("GPT-4.1-mini", .8987, .1677, .730, STEEL), ("+CoC", .7667, .0272, .712, LIGHT),
       ("+GoC", 1.2427, .1560, .698, LIGHT), ("+BoC", 1.0027, .1209, .722, LIGHT),
       ("CAF-I", 21.1047, 1.0605, .643, GREY), ("WM-SAR", 7.6520, .6622, .750, AMBER)]
fig, ax = plt.subplots(figsize=(7.0, 3.6))
offs = {"GPT-4.1-mini": (8, 6), "+CoC": (-6, -14), "+GoC": (8, -12), "+BoC": (8, -2),
        "CAF-I": (-30, 9), "WM-SAR": (-30, 9)}
for lab, t, s, f, c in pts:
    ax.errorbar(t, f, xerr=s, fmt="o", ms=9, color=c, mec="#555" if c == LIGHT else c,
                capsize=3, lw=1)
    ax.annotate(lab, (t, f), textcoords="offset points", xytext=offs[lab], fontsize=9.5)
ax.set_xscale("log")
ax.set_xticks([.5, 1, 2, 5, 10, 20], ["0.5", "1", "2", "5", "10", "20"])
ax.set_xlim(.5, 35)
ax.set_ylim(.63, .765)
ax.set_xlabel("Inference time per sample (s, mean ± std, log scale)")
ax.set_ylabel("Average Macro-F1")
save(fig, "cost.png")

# 5. Case studies: intermediate signals (Section: case studies in the manuscript).
sig = ["M_literal", "E_norm", "|D|", "T_sar"]
ok = [.10, .60, .50, .10]       # correctly classified non-sarcasm, SD = 0
miss = [.80, .80, .00, .10]     # sarcastic, misclassified as non-sarcasm, SD = 0
fig, axes = plt.subplots(1, 2, figsize=(8.6, 3.0), sharey=True)
for ax, vals, ttl in zip(axes, [ok, miss],
                         ["Case A: polite correction (non-sarcastic, correct)",
                          "Case B: \"A truly charming publication...\"\n(sarcastic, missed)"]):
    ax.bar(sig, vals, color=[STEEL, GREY, AMBER, AMBER], width=.6)
    for i, v in enumerate(vals):
        ax.text(i, v + .02, f"{v:.2f}", ha="center", fontsize=9.5)
    ax.set_title(ttl, fontsize=10)
    ax.set_ylim(0, 1)
    ax.text(3.4, .9, "SD = 0", ha="right", fontsize=9.5, color="#555")
axes[0].set_ylabel("Agent output")
fig.tight_layout()
save(fig, "cases.png")
print("done")
