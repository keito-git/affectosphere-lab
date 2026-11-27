"""Figures for the Free Anchors (WSDM 2027) research-blog post. Every plotted
number is copied from the camera-ready source (WSDM2027_prp0459_source.zip,
sections/6_experiments.tex and 9_ethics.tex); nothing is recomputed.
Figure 1 is a schematic of Theorem T3 and plots no data."""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

OUT = "/Users/ishitatakashishou/Sites/affectosphere-lab/public/column-images/wsdm2027-free-anchors/"
os.makedirs(OUT, exist_ok=True)
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


# 1. Schematic of the gauge theorem T3 (Section 4.2): vertex profiles admit
#    only permutations, interior profiles admit a continuum. No data plotted.
V = np.array([[0, 0], [1, 0], [.5, np.sqrt(3) / 2]])
fig, axes = plt.subplots(1, 2, figsize=(7.6, 3.4))
titles = ["Point contract\n(true profiles at vertices)",
          "Distribution contract\n(true profiles in the interior)"]
for ax, t in zip(axes, titles):
    ax.fill(V[:, 0], V[:, 1], color="#F4F1EA", ec="#666", lw=1)
    for (x, y), lab in zip(V, ["label 1", "label 2", "label 3"]):
        dy = -.09 if y < .1 else .05
        ax.text(x, y + dy, lab, ha="center", va="center", fontsize=9.5, color="#555")
    ax.set_title(t, fontsize=11)
    ax.set_xlim(-.18, 1.18); ax.set_ylim(-.42, 1.0)
    ax.set_aspect("equal"); ax.axis("off")
ax = axes[0]
ax.plot(V[:, 0], V[:, 1], "o", color=AMBER, ms=11, zorder=5)
ax.text(.5, -.3, "only relabelling\n(permutations) remains", ha="center",
        fontsize=9.5, color="#333")
ax = axes[1]
P = np.array([[.38, .22], [.62, .25], [.5, .46]])
ang = np.linspace(0, 2 * np.pi, 60)
for (x, y) in P:
    ax.fill(x + .085 * np.cos(ang), y + .085 * np.sin(ang), color=STEEL, alpha=.18, lw=0)
    ax.plot(x, y, "o", color=STEEL, ms=8, zorder=5)
ax.text(.5, -.3, "a continuum of equally good\nexplanations (dimension L(L-1))",
        ha="center", fontsize=9.5, color="#333")
fig.text(.5, -.03, "Schematic for illustration only (not data).", ha="center",
         fontsize=9, color="#777")
save(fig, "gauge-schematic.png")

# 2. Diameter as families are added (Table: tab:diversification).
#    m = 0 rows are the kernel-free bound 2(1 - eta), not a baseline.
fig, axes = plt.subplots(1, 2, figsize=(7.6, 3.3), sharey=True)
data = [("LLMJudge (L = 4)", ["none", "+GPT", "+Llama", "+T5"],
         [1.9296, 1.6336, 1.6287, 1.6287]),
        ("TREC-COVID panel (L = 3)", ["none", "+GPT", "+6 more\nproviders"],
         [1.8957, 1.1066, 1.1066])]
for ax, (t, labs, v) in zip(axes, data):
    cols = [LIGHT] + [AMBER] + [STEEL] * (len(v) - 2)
    ax.bar(range(len(v)), v, color=cols, width=.6,
           hatch=["//"] + [None] * (len(v) - 1), edgecolor=["#999"] + cols[1:])
    for i, val in enumerate(v):
        ax.text(i, val + .03, f"{val:.4f}", ha="center", fontsize=9.5)
    ax.set_xticks(range(len(v)), labs, fontsize=10)
    ax.set_title(t, fontsize=11)
    ax.set_ylim(0, 2.2)
axes[0].set_ylabel("Diameter of identification set (ℓ1)")
fig.text(.5, -.04, "Hatched: m = 0, kernel-free bound 2(1−η); not a baseline.",
         ha="center", fontsize=9, color="#666")
save(fig, "diversification.png")

# 3. Family boundaries in agreement (Section 6.2 text, Definition A):
#    within- vs cross-family Pearson phi, and LOFO Spearman rho with 95% CI.
fig, axes = plt.subplots(1, 2, figsize=(7.6, 3.0), gridspec_kw=dict(width_ratios=[1, 1.5]))
ax = axes[0]
ax.bar([0, 1], [.589, .494], color=[STEEL, LIGHT], width=.55)
for i, v in enumerate([.589, .494]):
    ax.text(i, v + .015, f"{v:.3f}", ha="center", fontsize=10)
ax.set_xticks([0, 1], ["within\nfamily", "cross\nfamily"])
ax.set_ylim(0, .72)
ax.set_ylabel("Mean Pearson φ (binarised)")
ax.set_title("Agreement", fontsize=11)
ax = axes[1]
lofo = [("hold out GPT", .841, .832, .850), ("hold out Llama", .874, .865, .881),
        ("hold out T5", .804, .793, .813)]
y = np.arange(3)[::-1]
for yi, (lab, m, lo, hi) in zip(y, lofo):
    ax.errorbar(m, yi, xerr=[[m - lo], [hi - m]], fmt="o", color=AMBER, ms=8, capsize=3)
    ax.text(hi + .006, yi, f"{m:.3f}", va="center", fontsize=10)
ax.set_yticks(y, [l[0] for l in lofo])
ax.set_xlim(.77, .91)
ax.set_ylim(-.6, 2.6)
ax.set_xlabel("LOFO Spearman ρ (95% CI)")
ax.set_title("Predicting a held-out family", fontsize=11)
fig.tight_layout(w_pad=2)
save(fig, "agreement.png")

# 4. Three interventions as diameter ratio (Figure: intervention_contrast,
#    values from its Description: 1.634->1.629, 1.634->1.520, 1.123->0.921).
iv = [("Add 26 judges from\ntwo lineage families", .997, "1.634 → 1.629", STEEL),
      ("Split a family\nwithin one lineage", .930, "1.634 → 1.520", LIGHT),
      ("Two unambiguous\nitems in the pool", .820, "1.123 → 0.921", AMBER)]
fig, ax = plt.subplots(figsize=(7.2, 2.9))
y = np.arange(3)[::-1]
for yi, (lab, r, s, c) in zip(y, iv):
    ax.barh(yi, r, color=c, height=.58)
    ax.text(1.008, yi, f"{r:.3f}   ({s})", va="center", fontsize=10)
ax.axvline(1, color="#444", ls="--", lw=1)
ax.set_yticks(y, [i[0] for i in iv])
ax.set_xlim(.7, 1.16)
ax.set_xlabel("Diameter after / diameter before (LLMJudge, optimised estimator)")
save(fig, "interventions.png")

# 5. Anchor sweep (Table: tab:anchor_sweep). First panel: 2-80 anchors all
#    0.9208; second panel: 12-24 anchors both 0.8451.
fig, ax = plt.subplots(figsize=(7.2, 3.3))
x1, y1 = [0, 2, 80], [1.1233, .9208, .9208]
x2, y2 = [0, 2, 12, 24], [.8895, .8532, .8451, .8451]
ax.plot(x1, y1, "-o", color=AMBER, lw=1.8, ms=7, label="LLMJudge (L = 4)")
ax.plot(x2, y2, "-s", color=STEEL, lw=1.8, ms=6, label="TREC-COVID panel (L = 3)")
ax.annotate("−18.03% with 2 items", (2, .9208), (12, 1.03), fontsize=10,
            arrowprops=dict(arrowstyle="-", color="#555", lw=.8))
ax.annotate("−5.0%", (12, .8451), (30, .79), fontsize=10,
            arrowprops=dict(arrowstyle="-", color="#555", lw=.8))
ax.set_xscale("symlog", linthresh=2)
ax.set_xticks([0, 2, 12, 24, 80], ["0", "2", "12", "24", "80"])
ax.set_ylim(.75, 1.18)
ax.set_xlabel("Unambiguous items (anchors) in the pool")
ax.set_ylabel("Interior diameter (ℓ1)")
ax.legend(frameon=False, loc="upper right")
save(fig, "anchor-sweep.png")

# 6. Vertex coverage of the LLMJudge pool (Section 6.3 text): minimum l1
#    distance of any of the 4,423 items to each label vertex.
fig, ax = plt.subplots(figsize=(7.2, 2.8))
d = [0.0000, .4848, .3030, .6061]
ax.bar(range(4), d, color=[AMBER, LIGHT, LIGHT, LIGHT], width=.55)
for i, v in enumerate(d):
    ax.text(i, v + .02, f"{v:.4f}", ha="center", fontsize=10)
ax.set_xticks(range(4), [f"label {i}" for i in range(4)])
ax.set_ylim(0, .72)
ax.set_ylabel("Min ℓ1 distance to vertex")
ax.set_title("Free anchors exist only for label 0 on LLMJudge", fontsize=11)
save(fig, "vertex-coverage.png")

# 7. Synthetic checks with known parameters (Table: tab:sensitivity, E1 rows).
fig, axes = plt.subplots(1, 3, figsize=(7.8, 2.9))
sets = [("T1: NRMSE", ["m = 2", "m = 3"], [.560, .310]),
        ("T3: interior diameter", ["m = 3", "m = 20"], [.327, .154]),
        ("T4: anchors at 1%", ["before", "after"], [.312, .003])]
for ax, (t, labs, v) in zip(axes, sets):
    ax.bar([0, 1], v, color=[GREY, STEEL if t.startswith("T3") else AMBER], width=.55)
    for i, val in enumerate(v):
        ax.text(i, val + .015, f"{val:.3f}", ha="center", fontsize=10)
    ax.set_xticks([0, 1], labs)
    ax.set_ylim(0, .66)
    ax.set_title(t, fontsize=11)
fig.tight_layout(w_pad=1.5)
save(fig, "synthetic.png")
print("done")
