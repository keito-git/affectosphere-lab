"""Figures for the IPSJ Digital Practice research-blog post.

Source: final camera-ready manuscript
(生成AIの実社会への導入と乗り越えるべき壁2027/最終提出版_20261027/1_tex/Inoshita_TDP.tex).
The paper is a practice paper; figures redraw its own structures in English
(Figure 1, Table 1, Table 3 scenario table, Table 4 checklist) and plot only
numbers stated in the text. Nothing is invented.
"""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Polygon
import numpy as np

OUT = "/Users/ishitatakashishou/Sites/affectosphere-lab/public/column-images/ipsj-dp-llm-uncertainty/"
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


# 1. Pipeline and the seven practices (Figure 1 of the paper, redrawn in English).
stages = ["Data\npreparation", "Evaluation\ndesign", "Model\noperation", "Decision\nmaking", "Social\nacceptance"]
prac = [["P3  Estimate cost\nat design time", "P4  Select the\ndataset"],
        ["P1  Treat uncertainty\nas a distribution", "P5  Design the\nevaluation metrics"],
        ["P2  Calibrate, minding\nmetric independence"],
        ["P6  Decide substitution\nby instance type"],
        ["P7  Explain uncertainty\nin practical terms"]]
cols = ["#E8D5B5", "#D9C29A", AMBER, "#7FA3BF", STEEL]
fig, ax = plt.subplots(figsize=(9.6, 3.9))
ax.axis("off"); ax.set_xlim(0, 10); ax.set_ylim(.6, 4.2)
w = 1.92
for i, (s, c) in enumerate(zip(stages, cols)):
    x0 = .05 + i * 1.99
    pts = [(x0, 3.0), (x0 + w - .22, 3.0), (x0 + w, 3.55), (x0 + w - .22, 4.1), (x0, 4.1),
           (x0 + (.22 if i else 0), 3.55)]
    ax.add_patch(Polygon(pts, closed=True, fc=c, ec="white", lw=1.5))
    ax.text(x0 + w / 2, 3.55, s, ha="center", va="center", fontsize=10.5,
            color="white" if i >= 2 else INK, fontweight="bold")
    for j, p in enumerate(prac[i]):
        y = 2.25 - j * 1.15
        ax.add_patch(FancyBboxPatch((x0 + .04, y - .45), w - .2, .9,
                     boxstyle="round,pad=0,rounding_size=.06", fc="white", ec="#999", lw=.9, ls="--"))
        ax.text(x0 + .04 + (w - .2) / 2, y, p, ha="center", va="center", fontsize=8.5)
save(fig, "overview.png")

# 2. Which project grounds which practice (Section 2 text: each subsection names the
# practices it underlies; A1 maps DC1 -> P1 and DC4/DC5 -> P6/P7).
projects = ["A1  Affective computing survey", "A2  Human vs LLM emotion judgements",
            "A3  MCMC uncertainty decomposition", "A4  EDL sarcasm detection"]
pr = ["P1", "P2", "P3", "P6", "P7"]
M = np.array([[1, 0, 0, 1, 1],
              [1, 1, 1, 1, 0],
              [1, 1, 0, 0, 0],
              [1, 0, 0, 1, 0]])
fig, ax = plt.subplots(figsize=(7.4, 3.0))
for i in range(4):
    for j in range(5):
        y = 3 - i
        fc = AMBER if M[i, j] else "#F1EEE8"
        ax.add_patch(FancyBboxPatch((j + .08, y + .1), .84, .8,
                     boxstyle="round,pad=0,rounding_size=.08", fc=fc, ec="white"))
        if M[i, j]:
            ax.text(j + .5, y + .5, "✓", ha="center", va="center", color="white", fontsize=13, fontfamily="DejaVu Sans")
ax.set_xlim(0, 5); ax.set_ylim(0, 4)
ax.set_xticks([j + .5 for j in range(5)], pr)
ax.set_yticks([3 - i + .5 for i in range(4)], projects)
ax.xaxis.tick_top(); ax.tick_params(length=0)
for s in ax.spines.values():
    s.set_visible(False)
save(fig, "projects.png")

# 3. Two calibration targets (Section 3.2, A3): temperature scaling improved ECE by
# about 59% and made JSD to the human distribution worse. The paper gives no
# magnitude for the JSD change, so the figure shows direction only.
fig, ax = plt.subplots(figsize=(6.4, 4.0))
ax.set_xlim(-1, 1); ax.set_ylim(-1, 1)
ax.axhline(0, color="#bbb", lw=.8); ax.axvline(0, color="#bbb", lw=.8)
ax.set_xticks([]); ax.set_yticks([])
ax.set_xlabel("Label-oriented calibration (ECE)  →  better", labelpad=8)
ax.set_ylabel("Fidelity to human distribution (JSD)  →  better", labelpad=8)
ax.plot(0, 0, "o", color=GREY, ms=11)
ax.text(-.22, .06, "before", fontsize=10, color="#555")
ax.annotate("", xy=(.72, -.55), xytext=(0, 0),
            arrowprops=dict(arrowstyle="-|>", color=AMBER, lw=2.4))
ax.text(.76, -.55, "temperature\nscaling", fontsize=10, color="#7B5E28", va="center")
ax.text(.0, -.56, "ECE about 59% better", fontsize=9.5, color="#7B5E28", ha="left", va="top")
ax.text(.62, -.82, "JSD worse (direction only;\nmagnitude not given in the paper)",
        fontsize=9, color="#555", ha="center")
ax.text(.62, .66, "expected beforehand", fontsize=9.5, color=STEEL)
ax.annotate("", xy=(.6, .6), xytext=(0, 0),
            arrowprops=dict(arrowstyle="-|>", color=STEEL, lw=1.4, ls="--"))
for s in ["top", "right"]:
    ax.spines[s].set_visible(False)
save(fig, "calibration.png")

# 4. Human-review bottleneck (Section 3.4, P6 note): child-oriented feed with mandatory
# human review stopped at its first 6 articles; the general feed without review
# published 379 over the following ~2 weeks in the same period.
fig, ax = plt.subplots(figsize=(7.2, 2.4))
ax.barh([1, 0], [6, 379], color=[AMBER, GREY], height=.55)
ax.text(6 + 5, 1, "6  (stopped: reviewing could not be kept up)", va="center", fontsize=10)
ax.text(379 + 5, 0, "379", va="center", fontsize=10)
ax.set_yticks([1, 0], ["Children's feed\n(every article human-reviewed)",
                       "General feed\n(no human review)"])
ax.set_xlim(0, 440)
ax.set_xlabel("Articles published (same period, about two weeks)")
save(fig, "review-bottleneck.png")

# 5. Stage-by-stage checklist (Table 4 of the paper): items per stage and practice.
stg = ["Design", "Implementation", "Operation"]
items = {  # copied item by item from Table 4
    "Design": ["P4", "P1/P5", "P2", "P3"],
    "Implementation": ["P1", "P2", "P2", "P3"],
    "Operation": ["P6", "P6", "P7", "P7"],
}
labels = {
    "Design": ["Dataset keeps per-annotator labels", "Metrics include a distribution distance",
               "Calibration target stated first", "Total calls × unit price estimated"],
    "Implementation": ["Aggregate + per-category profiles used", "Several calibration methods compared",
                       "Per-category degradation checked", "Retry and logging made generic"],
    "Operation": ["Substitution judged per instance type", "LLM first pass + human review built in",
                  "Uncertainty translated for the receiver", "Explanation designed from the start"],
}
fig, ax = plt.subplots(figsize=(9.6, 3.8))
ax.axis("off"); ax.set_xlim(0, 3); ax.set_ylim(0, 5)
scol = ["#E8D5B5", AMBER, STEEL]
for i, s in enumerate(stg):
    ax.add_patch(FancyBboxPatch((i + .03, 4.25), .94, .6, boxstyle="round,pad=0,rounding_size=.05",
                                fc=scol[i], ec="none"))
    ax.text(i + .5, 4.55, s, ha="center", va="center", fontsize=11, fontweight="bold",
            color=INK if i == 0 else "white")
    for k, (lab, p) in enumerate(zip(labels[s], items[s])):
        y = 3.6 - k * .95
        ax.add_patch(FancyBboxPatch((i + .03, y - .38), .94, .76, boxstyle="round,pad=0,rounding_size=.04",
                                    fc="#F7F4EE", ec="#ccc", lw=.8))
        ax.text(i + .07, y, "☐", va="center", fontsize=9, fontfamily="DejaVu Sans"); ax.text(i + .14, y, lab, va="center", fontsize=8.6)
        ax.text(i + .94, y - .25, p, ha="right", va="center", fontsize=8, color="#7B5E28")
ax.annotate("", xy=(2.98, 4.97), xytext=(.03, 4.97),
            arrowprops=dict(arrowstyle="-|>", color="#777", lw=1))
save(fig, "checklist.png")

# 6. Application scenarios (Table 3 of the paper): which practices each domain uses,
# plus the prerequisites the practices cannot cover.
doms = ["Business\n(customer reviews)", "Education\n(learner monitoring)", "Healthcare\n(mood-log self-monitoring)"]
colsP = ["P1", "P2", "P3", "P5", "P6", "P7", "Prerequisite\n(institutional /\nethical)"]
D = np.array([[1, 0, 1, 1, 1, 1, 0],
              [1, 0, 0, 0, 1, 1, 1],
              [1, 1, 0, 0, 1, 1, 1]])
fig, ax = plt.subplots(figsize=(8.4, 2.9))
for i in range(3):
    for j in range(7):
        y = 2 - i
        last = j == 6
        fc = (STEEL if last else AMBER) if D[i, j] else "#F1EEE8"
        ax.add_patch(FancyBboxPatch((j + .08, y + .1), .84, .8,
                     boxstyle="round,pad=0,rounding_size=.08", fc=fc, ec="white"))
        if D[i, j]:
            ax.text(j + .5, y + .5, "✓", ha="center", va="center", color="white", fontsize=13, fontfamily="DejaVu Sans")
ax.set_xlim(0, 7); ax.set_ylim(0, 3)
ax.set_xticks([j + .5 for j in range(7)], colsP, fontsize=9.5)
ax.set_yticks([2 - i + .5 for i in range(3)], doms)
ax.xaxis.tick_top(); ax.tick_params(length=0)
for s in ax.spines.values():
    s.set_visible(False)
save(fig, "scenarios.png")
print("done")
