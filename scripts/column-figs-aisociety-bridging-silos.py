"""Figures for the 'Bridging the Silos' (AI & Society) research-blog post.

This is a position paper with no experiments, so the figures are conceptual.
Figures 1-2 are the paper's own figures (PDF -> PNG). Figures 3-5 redraw
structures stated in the paper; every cell/label is copied from the
manuscript (revision_v3_clean, sections/*.tex). Nothing is invented.
"""
import os
import subprocess
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

SRC = os.path.expanduser(
    "~/Desktop/研究/論文/レビュー論文/提出版/revision_v3_clean/figures/")
OUT = "/Users/ishitatakashishou/Sites/affectosphere-lab/public/column-images/aisociety-bridging-silos/"
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


# 1-2. The paper's own figures (Figure 1: six-layer pipeline; Figure 2: cascade).
for src, dst in [("fig1_1_six_layer_pipeline.pdf", "pipeline"),
                 ("fig8_1_cascade.pdf", "cascade")]:
    subprocess.run(["pdftoppm", "-png", "-r", "160", "-singlefile",
                    SRC + src, OUT + dst], check=True)

# 3. DC x Pattern coupling matrix (Table: tab:dc_pattern_matrix, Section 9).
pats = ["Pattern 1\nTheory ↔ Data", "Pattern 2\nModeling ↔ Interaction",
        "Pattern 3\nTechnology ↔ Ethics", "Pattern 4\nData ↔ Application"]
dcs = ["DC1", "DC2", "DC3", "DC4", "DC5"]
M = [["primary", "indirect", "indirect", "indirect", "indirect"],
     ["indirect", "primary", "primary", "indirect", "indirect"],
     ["indirect", "secondary", "indirect", "secondary", "primary"],
     ["indirect", "indirect", "primary", "primary", "indirect"]]
col = {"primary": AMBER, "secondary": STEEL, "indirect": "#F1EEE8"}
tcol = {"primary": "white", "secondary": "white", "indirect": "#8A8F94"}
fig, ax = plt.subplots(figsize=(7.4, 3.6))
for i, row in enumerate(M):
    for j, v in enumerate(row):
        y = len(M) - 1 - i
        ax.add_patch(FancyBboxPatch((j + .06, y + .08), .88, .84,
                     boxstyle="round,pad=0,rounding_size=.08",
                     fc=col[v], ec="white", lw=1.5))
        ax.text(j + .5, y + .5, v, ha="center", va="center",
                color=tcol[v], fontsize=10,
                fontweight="bold" if v != "indirect" else "normal")
ax.set_xlim(0, 5); ax.set_ylim(0, 4)
ax.set_xticks([j + .5 for j in range(5)], dcs)
ax.set_yticks([len(M) - 1 - i + .5 for i in range(4)], pats)
ax.xaxis.tick_top()
for s in ax.spines.values():
    s.set_visible(False)
ax.tick_params(length=0)
save(fig, "dc-matrix.png")

# 4. Socio-philosophical stakes -> design criteria (Sections 8.6 and 9.1-9.5).
# DC1 -> algorithmic conformity; DC2, DC3, DC5 -> emotional agency;
# DC4 -> institutional power; DC5 also holds the other two stakes in check.
fig, ax = plt.subplots(figsize=(7.4, 3.9))
ax.axis("off"); ax.set_xlim(0, 10.1); ax.set_ylim(0, 6)
stakes = {"Algorithmic conformity": 4.9, "Emotional agency": 3.0,
          "Institutional power": 1.1}
dcy = {"DC1  theory-explicit representation": 5.4,
       "DC2  bounded intervention": 4.3,
       "DC3  longitudinal evaluation": 3.2,
       "DC4  deployment-specific accountability": 2.1,
       "DC5  user-retained interpretive authority": 1.0}
for name, y in stakes.items():
    ax.add_patch(FancyBboxPatch((.1, y - .45), 3.3, .9,
                 boxstyle="round,pad=0,rounding_size=.12", fc=STEEL, ec="none"))
    ax.text(1.75, y, name, ha="center", va="center", color="white",
            fontsize=11, fontweight="bold")
for name, y in dcy.items():
    ax.add_patch(FancyBboxPatch((5.3, y - .36), 4.75, .72,
                 boxstyle="round,pad=0,rounding_size=.1",
                 fc=AMBER if name.startswith("DC5") else "#EBDDC3", ec="none"))
    ax.text(5.45, y, name, ha="left", va="center",
            color="white" if name.startswith("DC5") else INK, fontsize=10)
links = [("DC1", "Algorithmic conformity", "-"),
         ("DC2", "Emotional agency", "-"),
         ("DC3", "Emotional agency", "-"),
         ("DC4", "Institutional power", "-"),
         ("DC5", "Emotional agency", "-"),
         ("DC5", "Algorithmic conformity", "--"),
         ("DC5", "Institutional power", "--")]
for dc, st, ls in links:
    y1 = [v for k, v in dcy.items() if k.startswith(dc)][0]
    ax.annotate("", xy=(3.45, stakes[st]), xytext=(5.25, y1),
                arrowprops=dict(arrowstyle="-|>", color="#555", lw=1.1, ls=ls))
ax.text(4.3, 5.9, "protects against / answers", ha="center", fontsize=9.5,
        color="#555", style="italic")
ax.plot([6.0, 6.5], [.15, .15], color="#555", lw=1.1, ls="--")
ax.text(6.6, .15, "DC5 also holds the other two stakes in check",
        va="center", fontsize=9, color="#555")
save(fig, "stakes.png")

# 5. Positioning of prior surveys (Table: tab:1_prior_surveys, 11 prior surveys).
# Cross-layer central: No = 10, Partial = 1. Prescriptive stance: Yes = 2, No = 9.
cats = ["Cross-layer\ndependence central?", "Prescriptive\nstance?"]
fig, ax = plt.subplots(figsize=(7.2, 2.6))
yspace = 1.15
segs = [[("No", 10, LIGHT), ("Partial", 1, STEEL)],
        [("No", 9, LIGHT), ("Yes", 2, STEEL)]]
for i, row in enumerate(segs):
    left = 0
    yy = (1 - i) * 1.15
    for lab, n, c in row:
        ax.barh(yy, n, left=left, color=c, height=.55, ec="white")
        if n == 1:  # too narrow for an inside label
            ax.text(left + n / 2, yy - .42, f"{lab} ({n})", ha="center",
                    va="top", color=STEEL, fontsize=9.5)
        else:
            ax.text(left + n / 2, yy, f"{lab}  ({n})", ha="center",
                    va="center", color="white" if c == STEEL else INK,
                    fontsize=10)
        left += n
    ax.barh(yy, 1.6, left=11.6, color=AMBER, height=.55)
    ax.text(12.4, yy, "Yes", ha="center", va="center", color="white",
            fontsize=10, fontweight="bold")
ax.text(5.5, 1.7, "11 prior surveys", ha="center", fontsize=10, color="#444")
ax.text(12.4, 1.7, "This paper", ha="center", fontsize=10, color="#7B5E28")
ax.set_yticks([1.15, 0], cats)
ax.set_xticks([])
ax.spines["bottom"].set_visible(False)
ax.set_xlim(0, 13.4); ax.set_ylim(-.6, 1.95)
ax.set_yticks([1.15, 0], cats)
save(fig, "prior-surveys.png")
print("done")
