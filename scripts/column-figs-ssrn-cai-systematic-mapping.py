"""Figures for the CAI systematic-mapping (SSRN preprint) research-blog post.
Every number is copied from the 2026-09-18 public manuscript
(computational_affective_intelligence/提出版/manuscript/main.tex, identical to
arxiv.zip apart from LaTeX comments); nothing is recomputed. selection-flow.png,
cai-conceptual.png, temporal.png and core-vs-external.png are the paper's own
figures, copied unchanged."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

OUT = "/Users/ishitatakashishou/Sites/affectosphere-lab/public/column-images/ssrn-cai-systematic-mapping/"
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


# 1. Ground-truth source (B axis, Table tab:b_distribution, n = 60) and
#    disagreement handling (C axis, Table tab:c_distribution, n = 44).
b_codes = ["B1 third-party consensus", "B? not determinable", "B3 self-report",
           "B7 multiple sources", "B5 designed stimulus intent", "B2 expert rating"]
b_n = [14, 14, 14, 10, 5, 3]
b_pct = [23.3, 23.3, 23.3, 16.7, 8.3, 5.0]
c_codes = ["C_none no statement in text", "C1 aggregated", "C3a perspectives preserved",
           "C3b uncertainty preserved", "C2 agreement stats only"]
c_n = [27, 10, 3, 2, 2]
c_pct = [61.4, 22.7, 6.8, 4.5, 4.5]
fig, axes = plt.subplots(1, 2, figsize=(11.0, 3.9))
for ax, codes, n, pct, hi, title in [
        (axes[0], b_codes, b_n, b_pct, "B? not determinable",
         "(a) Who supplied the labels?  (B axis, n = 60)"),
        (axes[1], c_codes, c_n, c_pct, "C_none no statement in text",
         "(b) How was disagreement handled?  (C axis, n = 44)")]:
    y = np.arange(len(codes))[::-1]
    cols = [AMBER if c == hi else LIGHT for c in codes]
    ax.barh(y, pct, color=cols, height=.62)
    for yi, k, p in zip(y, n, pct):
        ax.text(p + 1.2, yi, f"{k}  ({p:.1f}%)", va="center", fontsize=9.5)
    ax.set_yticks(y, codes, fontsize=9.5)
    ax.set_xlim(0, 85)
    ax.set_xlabel("% of papers")
    ax.set_title(title, fontsize=11, loc="left")
fig.tight_layout(w_pad=3)
save(fig, "reporting.png")

# 2. C_none rate by dataset-reuse status with Wilson 95% CIs
#    (Table tab:stratified_cnone; Fisher and chi-square values from the text of Sec. 5.1).
strata = ["Existing dataset\nreused (n = 24)", "Reuse status\nunknown (n = 11)",
          "Original label\ncollection (n = 9)", "All (n = 44)"]
rate = [79.2, 54.5, 22.2, 61.4]
lo = [59.5, 28.0, 6.3, 46.6]
hi = [90.8, 78.7, 54.7, 74.3]
cols = [AMBER, LIGHT, STEEL, GREY]
fig, ax = plt.subplots(figsize=(7.0, 4.0))
x = np.arange(len(strata))
ax.bar(x, rate, color=cols, width=.6)
ax.errorbar(x, rate, yerr=[np.subtract(rate, lo), np.subtract(hi, rate)],
            fmt="none", ecolor="#333", capsize=5, lw=1)
for xi, r, h in zip(x, rate, hi):
    ax.text(xi + .33, r, f"{r:.1f}%", va="center", ha="left", fontsize=10)
ax.set_xticks(x, strata, fontsize=9.5)
ax.set_ylim(0, 100)
ax.set_xlim(-.5, 3.85)
ax.set_ylabel("C_none rate (%), Wilson 95% CI")
ax.text(1.65, 99, "reused vs. original: Fisher two-sided p = 0.005, OR 13.3\n"
        "three strata: χ²(2) = 9.24, p = 0.010",
        ha="center", va="top", fontsize=9, color="#555")
save(fig, "reuse-strata.png")

# 3. Full-text check of the Mechanism placement (Sec. "Validating the Placement
#    Basis for Mechanism"): 190 external records -> 123 open access (ACL + arXiv)
#    -> 58 full texts -> 17 contain a vocabulary term -> 2 mechanistic use.
stages = ["External sample", "Open access\n(ACL Anthology + arXiv)", "Full text retrieved",
          "Contains a mechanism\nterm in the body", "Uses it in the\nmechanistic sense"]
vals = [190, 123, 58, 17, 2]
cols = [LIGHT, LIGHT, GREY, GREY, AMBER]
fig, ax = plt.subplots(figsize=(7.4, 3.7))
y = np.arange(len(stages))[::-1]
ax.barh(y, vals, color=cols, height=.6)
for yi, v in zip(y, vals):
    ax.text(v + 3, yi, str(v), va="center", fontsize=10.5)
ax.text(30, y[-1], "both already placed in Mechanism\nfrom their abstracts",
        va="center", fontsize=9.5, color="#7B5E28")
ax.text(30, y[-2], "15 of 17 are incidental uses\n(e.g., a question that 'probes')",
        va="center", fontsize=9.5, color="#555")
ax.set_yticks(y, stages, fontsize=9.5)
ax.set_xlim(0, 215)
ax.set_xlabel("Number of records")
save(fig, "mechanism-check.png")

# 4. Accuracy under the two scoring keys (Table tab:key_sensitivity, crowd-enVent
#    validation portion, bootstrap B = 2000).
parties = ["Best model configuration", "Model mean (11 configurations)",
           "Weakest model configuration", "Individual human reader"]
self_key = [0.728, 0.691, 0.656, 0.504]
obs_key = [0.693, 0.672, 0.638, 0.638]
delta = ["+0.036", "+0.019", "+0.018", "-0.134"]
fig, ax = plt.subplots(figsize=(7.6, 3.8))
y = np.arange(len(parties))[::-1]
for yi, a, b, d in zip(y, self_key, obs_key, delta):
    ax.plot([a, b], [yi, yi], color=LIGHT, lw=3, zorder=1)
    ax.text(max(a, b) + .012, yi, f"Δkey {d}", va="center", fontsize=9.5, color="#555")
ax.scatter(self_key, y, color=AMBER, s=65, zorder=3, label="self-report key (writer's own label)")
ax.scatter(obs_key, y, color=STEEL, s=65, zorder=3, label="observer key (majority of 4 readers)")
ax.set_yticks(y, parties, fontsize=9.5)
ax.set_xlim(.45, .85)
ax.set_ylim(-1.6, 3.5)
ax.set_xlabel("Accuracy")
ax.legend(loc="lower right", frameon=False, fontsize=9)
ax.text(.455, -1.25, "Gap (model mean - human): +0.187 vs. +0.033\n"
        "difference +0.154 [+0.120, +0.187]", fontsize=9, color="#555", va="center")
save(fig, "scoring-key.png")
