"""Figures for the 'Must a Machine Feel before it can Ask?' research-blog post.
The paper is a theoretical argument and reports no measured data. Every figure here
is a faithful re-drawing of a table or a passage in the SSRN manuscript
(06_MM版/ssrn_20260928/main_ssrn.tex); no numbers are plotted. Figures 1 and 2 of the
paper (problem-discovery-gap.png, appraisal-complementarity.png) are cropped from
the SSRN PDF separately."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

OUT = "/Users/ishitatakashishou/Sites/affectosphere-lab/public/column-images/ssrn-functional-emotion-problem-discovery/"
AMBER, STEEL, GREY, LIGHT, INK = "#C4974A", "#3D6B8C", "#9AA0A6", "#D9D4CB", "#1A1A1A"
plt.rcParams.update({
    "font.family": "Arial", "font.size": 11, "axes.edgecolor": "#444",
    "axes.linewidth": 0.8, "axes.spines.top": False, "axes.spines.right": False,
    "xtick.color": "#333", "ytick.color": "#333", "axes.labelcolor": "#222",
    "savefig.dpi": 220, "savefig.bbox": "tight", "savefig.facecolor": "white",
})

# Symbol -> (cell colour, text) used by the grid figures.
SYM = {"o": (AMBER, "✓"), "x": ("#F1EFEB", "✗"), "t": (LIGHT, "△"),
       "up": (AMBER, "↑"), "eq": (LIGHT, "="), "-": ("white", "—"), "?": ("#E8EEF3", "?")}


def save(fig, name):
    fig.savefig(OUT + name)
    plt.close(fig)


def grid(rows, cols, cells, name, width, highlight_last=True, col_w=1.0, title=None):
    nr, nc = len(rows), len(cols)
    fig, ax = plt.subplots(figsize=(width, .42 * nr + .9))
    for i, row in enumerate(cells):
        for j, s in enumerate(row):
            fc, t = SYM[s]
            y = nr - 1 - i
            ax.add_patch(plt.Rectangle((j * col_w, y), col_w * .94, .86, fc=fc, ec="white"))
            ax.text(j * col_w + col_w * .47, y + .43, t, ha="center", va="center", fontsize=12,
                    color="white" if fc == AMBER else INK, fontfamily="DejaVu Sans")
    for i, r in enumerate(rows):
        y = nr - 1 - i + .43
        bold = highlight_last and i == nr - 1
        ax.text(-.15, y, r, ha="right", va="center", fontsize=10.5,
                fontweight="bold" if bold else "normal")
    for j, c in enumerate(cols):
        ax.text(j * col_w + col_w * .47, nr + .2, c, ha="center", va="bottom", fontsize=10.5)
    if highlight_last:
        ax.plot([0, nc * col_w], [.93, .93], color="#444", lw=.8, clip_on=False)
    ax.set_xlim(0, nc * col_w)
    ax.set_ylim(0, nr + .9)
    ax.axis("off")
    if title:
        ax.set_title(title, fontsize=11, loc="left")
    save(fig, name)


# 1. Component-removal thought experiment (Section 5.1 and 5.3). Which of the four
#    elements each system has, and whether Z is posed as a new problem in the hard case.
rows = ["F  (all elements)", "O-1  (no lack retention)", "O-2  (no appraisal representation)",
        "O-3  (appraisal, not used for recruitment)", "O-4  (no adoption budget)"]
cols = ["Lack\nretention", "Appraisal\nrepresentation", "Complementary\nrecruitment",
        "Adoption\nbudget", "New problem\nposed (hard case)"]
cells = [["o", "o", "o", "o", "o"],
         ["x", "o", "o", "o", "x"],
         ["o", "x", "-", "o", "x"],  # recruitment by appraisal is moot without an appraisal
         ["o", "o", "x", "o", "x"],
         ["o", "o", "o", "x", "x"]]
fig, ax = plt.subplots(figsize=(9.2, 3.3))
nr = len(rows)
for i, row in enumerate(cells):
    for j, s in enumerate(row):
        fc, t = SYM[s]
        x = j * 1.25 + (.35 if j == 4 else 0)
        y = nr - 1 - i
        ax.add_patch(plt.Rectangle((x, y), 1.18, .86, fc=fc, ec="white"))
        ax.text(x + .59, y + .43, t, ha="center", va="center", fontsize=12,
                color="white" if fc == AMBER else INK, fontfamily="DejaVu Sans")
for i, r in enumerate(rows):
    ax.text(-.15, nr - 1 - i + .43, r, ha="right", va="center", fontsize=10.5,
            fontweight="bold" if i == 0 else "normal")
for j, c in enumerate(cols):
    x = j * 1.25 + (.35 if j == 4 else 0)
    ax.text(x + .59, nr + .15, c, ha="center", va="bottom", fontsize=10)
notes = ["", "lack not sustained", "link left to chance (≈ BM/N)", "Z never comes to attention",
         "verification not funded"]
for i, n in enumerate(notes):
    if n:
        ax.text(5 * 1.25 + .45, nr - 1 - i + .43, n, va="center", fontsize=9.5, color="#555")
ax.set_xlim(0, 9.2)
ax.set_ylim(0, nr + 1.0)
ax.axis("off")
save(fig, "thought-experiment.png")

# 2. Routes that could play role (b) in the hard case (Table 1 of the manuscript).
rows = ["Content similarity (memory, embeddings)", "Analogy by relational structure",
        "Predictive encoding", "Random combination", "External connector (human, other system)",
        "Scalar curiosity, grounded reward", "Relevance predictor trained on past resolutions",
        "Schematization by a concern-conditioned LM", "Complementary appraisal types"]
cols = ["Links unrelated\ncontent", "Unresolved state\nas anchor", "Rate above\nchance"]
cells = [["x", "t", "-"], ["o", "t", "-"], ["o", "t", "up"], ["o", "o", "eq"], ["o", "t", "-"],
         ["t", "x", "-"], ["o", "o", "?"], ["o", "t", "?"], ["o", "o", "up"]]
grid(rows, cols, cells, "routes.png", 8.4, col_w=1.35)

# 3. Existing AI components vs. the four elements (Table 2 of the manuscript).
rows = ["Memory module: vector search", "Goal-conditioned RL", "LM goal generation",
        "Scalar curiosity: RND, ICM", "Structural analogy module", "Emotion-aware retrieval",
        "Appraisal-based affect agent: EMA", "Emotion in RL", "Interoceptive regulation",
        "Discovery-oriented research agents", "Functional emotion (this paper)"]
cols = ["Retention", "Appraisal", "Recruitment", "Budget"]
cells = [["x", "x", "x", "x"], ["x", "x", "x", "x"], ["t", "x", "x", "x"], ["t", "x", "x", "x"],
         ["x", "x", "t", "x"], ["x", "t", "x", "x"], ["x", "o", "x", "x"], ["t", "t", "x", "x"],
         ["t", "x", "x", "x"], ["x", "x", "x", "t"], ["o", "o", "o", "o"]]
grid(rows, cols, cells, "ai-components.png", 7.6, col_w=1.2)

# 4. Structure of the two-stage argument (Sections 3.4, 4.1 and 4.3).
fig, ax = plt.subplots(figsize=(9.4, 4.6))
ax.set_xlim(0, 10)
ax.set_ylim(0, 6)
ax.axis("off")


def box(x, y, w, h, text, fc="#F4F2EE", ec="#444", lw=1.0, fs=10, bold=False, ls="-"):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.02,rounding_size=0.08",
                                fc=fc, ec=ec, lw=lw, ls=ls))
    ax.text(x + w / 2, y + h / 2, text, ha="center", va="center", fontsize=fs,
            fontweight="bold" if bold else "normal", wrap=True)


def arrow(x1, y1, x2, y2):
    ax.annotate("", (x2, y2), (x1, y1), arrowprops=dict(arrowstyle="-|>", color="#333", lw=1.2))


box(.1, 4.6, 2.9, 1.2, "Premises P1–P5\n(expansion, allocation by utility,\nscarcity, scope of intelligence,\nunresolved states)", fs=9)
box(.1, 2.9, 2.9, 1.2, "Hard case\nresolving experience unrelated\nin content; verification scarce", fs=9)
box(3.6, 3.75, 3.0, 1.6, "Conclusion 1: role necessity\n(a) retain the unresolved state\n(b) selection signal σ(L, Z)\n(c) fund verification beyond utility",
    fc="#F3E9D6", ec=AMBER, lw=1.4, fs=9.5)
ax.text(5.1, 3.45, "conditional structural necessity", ha="center", fontsize=9, color="#7B5E28", style="italic")
box(3.6, .9, 3.0, 1.6, "Hypotheses R1 (realization)\nand R2 (transfer)\n+ world premise ρw > 0", fc="#E8EEF3", ec=STEEL, lw=1.2, fs=9.5)
box(7.2, 2.3, 2.7, 1.6, "Conclusion 2:\nfunctional emotion\ngives a reason to a system\nthat keeps expanding", fc="#F3E9D6", ec=AMBER, lw=1.4, fs=9.5)
ax.text(8.55, 2.0, "defeasible reason", ha="center", fontsize=9, color="#7B5E28", style="italic")
arrow(3.0, 5.2, 3.6, 4.8)
arrow(3.0, 3.5, 3.6, 4.2)
arrow(6.6, 4.5, 7.2, 3.5)
arrow(6.6, 1.7, 7.2, 2.7)
box(7.2, 4.5, 2.7, 1.3, "Not claimed: emotion is the\nonly route to discovery", fc="white", ec=GREY, fs=9, ls="--")
box(7.2, .3, 2.7, 1.3, "Not claimed: phenomenal\nexperience (functional roles only)", fc="white", ec=GREY, fs=9, ls="--")
save(fig, "argument-structure.png")

# 5. How the six predictions relate (Section 6.1, paragraph on relations among predictions).
fig, ax = plt.subplots(figsize=(9.0, 3.6))
ax.set_xlim(0, 10)
ax.set_ylim(0, 4.4)
ax.axis("off")
box(.1, 2.6, 2.9, 1.3, "(1) Complementarity\nbeats same type, random,\nvalence flip, content predictor", fc="#F3E9D6", ec=AMBER, lw=1.3, fs=9)
box(3.5, 2.6, 2.9, 1.3, "(2) Transfer\nadvantage persists under\nnew concerns and domains", fc="#F3E9D6", ec=AMBER, lw=1.3, fs=9)
box(6.9, 2.6, 3.0, 1.3, "(5) World coupling\nadvantage grows with ρw,\nvanishes at ρw = 0", fc="#F3E9D6", ec=AMBER, lw=1.3, fs=9)
box(.1, .3, 1.4, 1.3, "(3) Direction\nswap removes\nadvantage", fc="#E8EEF3", ec=STEEL, fs=8.8)
box(1.6, .3, 1.4, 1.3, "(4) Concern\ndependence", fc="#E8EEF3", ec=STEEL, fs=8.8)
box(6.9, .3, 3.0, 1.3, "(6) Erosion\nmyopic self-improvement cuts\nverification; insulated budget\nprevents it", fc="white", ec=GREY, fs=8.8)
arrow(.8, 2.6, .8, 1.6)
arrow(2.3, 2.6, 2.3, 1.6)
ax.text(3.2, 2.05, "diagnostic only if (1) holds", fontsize=9, color=STEEL, style="italic")
ax.text(5.0, 4.15, "each tests the advantage of the mechanism independently", ha="center", fontsize=9.5, color="#7B5E28")
ax.text(6.75, .95, "tests self-binding,\nindependent of the mechanism", ha="right", fontsize=9, color="#555", style="italic")
save(fig, "predictions.png")
print("done")
