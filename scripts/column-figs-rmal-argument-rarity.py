"""Figures for the AROA (Research Methods in Applied Linguistics) research-blog post.

Every number is copied from the final R3 manuscript
(再投稿_revision/RMAL_R3/source/Authors/documents/4_experiment-and-analysis.tex).
The manuscript folder is read only; nothing there is modified.
"""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

SRC = os.path.expanduser(
    "~/Desktop/研究/論文/教育x立命館/レポートの独創性評価/再投稿_revision/RMAL_R3/"
    "source/Authors/figures_png/framework.png")
OUT = "/Users/ishitatakashishou/Sites/affectosphere-lab/public/column-images/rmal-argument-rarity/"
os.makedirs(OUT, exist_ok=True)
AMBER, STEEL, GREY, LIGHT, INK = "#C4974A", "#3D6B8C", "#9AA0A6", "#D9D4CB", "#1A1A1A"
plt.rcParams.update({
    "font.family": "Arial", "font.size": 11, "axes.edgecolor": "#444",
    "axes.linewidth": 0.8, "axes.spines.top": False, "axes.spines.right": False,
    "xtick.color": "#333", "ytick.color": "#333", "axes.labelcolor": "#222",
    "savefig.dpi": 220, "savefig.bbox": "tight", "savefig.facecolor": "white",
})
Image.MAX_IMAGE_PIXELS = None


def save(fig, name):
    fig.savefig(OUT + name)
    plt.close(fig)


# 1. The paper's own framework figure (Figure 1), downscaled from 11300 px wide.
im = Image.open(SRC).convert("RGB")
w = 2400
im.resize((w, round(im.height * w / im.width)), Image.LANCZOS).save(OUT + "framework.png", optimize=True)

# 2. Student vs AI, Cohen's d by assignment (Table: tab:comparison, primary protocol).
# Positive d = students higher.
meas = ["Structural\nrarity", "Claim\nrarity", "Evidence\nrarity", "Dialogic\nelaboration"]
car = [.34, .99, -.38, 1.05]
ele = [.51, -.01, .12, -.81]
x = np.arange(4); bw = .36
fig, ax = plt.subplots(figsize=(7.2, 3.5))
ax.bar(x - bw/2, car, bw, color=STEEL, label="Car-free cities")
ax.bar(x + bw/2, ele, bw, color=AMBER, label="Electoral College")
for xi, a, b in zip(x, car, ele):
    for xx, v in [(xi - bw/2, a), (xi + bw/2, b)]:
        ax.text(xx, v + (.04 if v >= 0 else -.04), f"{v:+.2f}", ha="center",
                va="bottom" if v >= 0 else "top", fontsize=9.5)
ax.axhline(0, color="#444", lw=.8)
ax.set_xticks(x, meas)
ax.set_ylim(-1.15, 1.5)
ax.set_ylabel("Cohen's d (students − AI)")
ax.text(3.55, 1.42, "positive = student essays more atypical", ha="right", fontsize=9, color="#555")
ax.legend(frameon=False, loc="lower left", fontsize=9.5)
save(fig, "student-vs-ai.png")

# 3. Within-population rarity, AI relative to students (Section 4.2, 500 per population;
# Section 4.4 for C0 and C1 at 250 per population).
fig, ax = plt.subplots(figsize=(7.2, 3.4))
groups = [("Claims\nmain AI essays (500)", [.32, .36], AMBER),
          ("Evidence\nmain AI essays (500)", [.58, .64], AMBER),
          ("Claims\nC0 imitation (250)", [.34, .39], LIGHT),
          ("Claims\nC1 novelty (250)", [.62, .56], STEEL)]
x = np.arange(4)
for xi, (lab, vals, c) in zip(x, groups):
    ax.bar([xi - .18, xi + .18], vals, .34, color=c, edgecolor="white")
    for xx, v in zip([xi - .18, xi + .18], vals):
        ax.text(xx, v + .02, f"{v:.2f}", ha="center", fontsize=9.5)
ax.axhline(1, color=GREY, ls="--", lw=1)
ax.text(3.55, 1.02, "student level = 1", ha="right", fontsize=9, color="#666", va="bottom")
ax.set_xticks(x, [g[0] for g in groups], fontsize=9.5)
ax.set_ylim(0, 1.12)
ax.set_ylabel("Within-population rarity,\nAI ÷ students")
ax.text(-.4, -.27, "Left bar: Car-free cities   Right bar: Electoral College",
        transform=ax.get_xaxis_transform(), fontsize=9, color="#555")
save(fig, "homogeneity.png")

# 4. Reference-corpus composition (Section 4.2): student-AI d, student-only vs mixed corpus.
fig, ax = plt.subplots(figsize=(7.2, 2.9))
rows = [("Claim rarity", .47, 1.58), ("Evidence rarity", -.11, 1.05)]
y = np.arange(2)[::-1]
for yi, (lab, a, b) in zip(y, rows):
    ax.annotate("", xy=(b, yi), xytext=(a, yi),
                arrowprops=dict(arrowstyle="-|>", color="#777", lw=1.4))
    ax.plot(a, yi, "o", color=STEEL, ms=10, zorder=3)
    ax.plot(b, yi, "o", color=AMBER, ms=10, zorder=3)
    ax.text(a, yi + .2, f"{a:+.2f}", ha="center", fontsize=10, color=STEEL)
    ax.text(b, yi + .2, f"{b:+.2f}", ha="center", fontsize=10, color="#7B5E28")
ax.plot([], [], "o", color=STEEL, label="Student-only reference corpus")
ax.plot([], [], "o", color=AMBER, label="Mixed corpus (students + AI)")
ax.axvline(0, color="#444", lw=.8)
ax.set_yticks(y, [r[0] for r in rows])
ax.set_xlim(-.4, 1.9); ax.set_ylim(-.6, 1.6)
ax.set_xlabel("Cohen's d (students − AI)")
ax.legend(frameon=False, loc="lower right", fontsize=9.5)
save(fig, "composition.png")

# 5. Generation strategy (Table: tab:promptvar), d versus students.
conds = ["C0 imitation", "C1 novelty-seeking", "C2 persona"]
dc = [.46, -.51, .21]
de = [-.07, -1.94, -.46]
x = np.arange(3); bw = .36
fig, ax = plt.subplots(figsize=(7.2, 3.4))
ax.bar(x - bw/2, dc, bw, color=STEEL, label="Claim rarity")
ax.bar(x + bw/2, de, bw, color=AMBER, label="Evidence rarity")
for xi, a, b in zip(x, dc, de):
    for xx, v in [(xi - bw/2, a), (xi + bw/2, b)]:
        ax.text(xx, v + (.05 if v >= 0 else -.05), f"{v:+.2f}", ha="center",
                va="bottom" if v >= 0 else "top", fontsize=9.5)
ax.axhline(0, color="#444", lw=.8)
ax.set_xticks(x, conds)
ax.set_ylim(-2.35, .85)
ax.set_ylabel("Cohen's d vs student essays\n(negative = AI more atypical)")
ax.legend(frameon=False, loc="lower left", fontsize=9.5)
save(fig, "generation-strategy.png")

# 6. Perturbation test (Table: tab:perturbation), mean change in final score.
edits = ["Paraphrase\n(no argument changed)", "Irrelevant but\nunusual claim added",
         "Evidence replaced by\nfabricated evidence", "Relevant uncommon\nargument added"]
fs = [.181, .043, .405, .037]
sig = ["***", "**", "***", "*"]
cols = [GREY, GREY, AMBER, STEEL]
fig, ax = plt.subplots(figsize=(7.2, 3.3))
y = np.arange(4)[::-1]
ax.barh(y, fs, color=cols, height=.58)
for yi, v, s in zip(y, fs, sig):
    ax.text(v + .006, yi, f"+{v:.3f} {s}", va="center", fontsize=10)
ax.set_yticks(y, edits)
ax.set_xlim(0, .48)
ax.set_xlabel("Mean change in final score vs unedited essay (n = 100 per edit)")
save(fig, "perturbation.png")

# 7. Expert ratings (Table: tab:expert), Spearman rho with rated originality.
sc = ["Final score", "Dialogic elaboration", "Claim rarity", "Evidence rarity", "Structural rarity"]
allr = [.33, .38, .17, .02, .04]
wst = [.29, .36, .14, -.15, -.18]
sigA = ["***", "***", "", "", ""]
sigW = ["**", "***", "", "", ""]
y = np.arange(5)[::-1]; bh = .36
fig, ax = plt.subplots(figsize=(7.2, 3.5))
ax.barh(y + bh/2, allr, bh, color=STEEL, label="All 120 essays")
ax.barh(y - bh/2, wst, bh, color=AMBER, label="Within strata (conservative)")
for yi, a, b, sa, sw in zip(y, allr, wst, sigA, sigW):
    for yy, v, s in [(yi + bh/2, a, sa), (yi - bh/2, b, sw)]:
        ax.text(v + (.01 if v >= 0 else -.01), yy, f"{v:+.2f}{s}", va="center",
                ha="left" if v >= 0 else "right", fontsize=9)
ax.axvline(0, color="#444", lw=.8)
ax.set_yticks(y, sc)
ax.set_xlim(-.3, .52)
ax.set_xlabel("Spearman ρ with one expert's originality rating")
ax.legend(frameon=False, loc="lower right", fontsize=9)
save(fig, "expert.png")

# 8. Reference-corpus size (Section 4.3): rank agreement of the final score.
n = [50, 100, 200, 300, 400]
rho = [.91, .96, .98, .99, 1.00]
fig, ax = plt.subplots(figsize=(7.2, 2.9))
ax.plot(n, rho, "-o", color=AMBER, lw=1.8, ms=7)
for a, b in zip(n, rho):
    ax.text(a, b - .018, f"{b:.2f}", ha="center", va="top", fontsize=9.5)
ax.set_xticks(n)
ax.set_ylim(.84, 1.02)
ax.set_xlabel("Reference corpus size (student essays)")
ax.set_ylabel("Mean rank agreement (ρ)\nwith full corpus")
save(fig, "reference-size.png")
print("done")
