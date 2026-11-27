"""Figures for the DSAIS (Applied Soft Computing) research-blog post.

Every number is copied from the second-revision manuscript
(ASC_revision/revision2/latex_source_rev2.zip: 3_methodology.tex and
4_experiment-and-analysis.tex). Nothing is recomputed. The source table is
named above each figure.
"""
import os
import subprocess
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

ZIP = os.path.expanduser(
    "~/Desktop/研究/論文/ドライバー支援の研究/ドライバー支援評価指標/提出版/"
    "ASC_revision/revision2/latex_source_rev2.zip")
TMP = ("/private/tmp/claude-501/-Users-ishitatakashishou/"
       "62e336aa-c915-4181-a249-1463c108b1af/scratchpad/asc-driver-intervention-safety/src/")
OUT = "/Users/ishitatakashishou/Sites/affectosphere-lab/public/column-images/asc-driver-intervention-safety/"
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


# 1. The paper's own architecture figure (Figure 1), PDF -> PNG.
if not os.path.exists(TMP + "fig1_architecture.pdf"):
    os.makedirs(TMP, exist_ok=True)
    subprocess.run(["unzip", "-o", "-q", ZIP, "fig1_architecture.pdf", "-d", TMP], check=True)
subprocess.run(["pdftoppm", "-png", "-r", "170", "-singlefile",
                TMP + "fig1_architecture.pdf", OUT + "architecture"], check=True)

# 2. Response to a single task at maximum risk (Table: tab:capacity), with theta_L.
tasks = ["TCR\ntraffic", "VCR\nvehicle", "DER\nemotion", "DBR\nbehaviour"]
add = [.200, .200, .350, .250]
lam = [.300, .300, .525, .375]
x = np.arange(4); w = .36
fig, ax = plt.subplots(figsize=(7.2, 3.4))
ax.bar(x - w/2, add, w, color=GREY, label="Weighted sum (submitted)")
ax.bar(x + w/2, lam, w, color=AMBER, label="Choquet integral, Sugeno λ-measure")
for xi, a, l in zip(x, add, lam):
    ax.text(xi - w/2, a + .01, f"{a:.3f}", ha="center", fontsize=9.5)
    ax.text(xi + w/2, l + .01, f"{l:.3f}", ha="center", fontsize=9.5)
ax.axhline(.30, color=STEEL, ls="--", lw=1.2, label="θ_L = 0.30 (LOW / MEDIUM boundary)")
ax.set_xticks(x, tasks)
ax.set_ylim(0, .64)
ax.set_ylabel("Fused risk when only this task\nis at maximum risk, R(e_k)")
ax.legend(frameon=False, loc="upper left", fontsize=9.5)
save(fig, "single-task-response.png")

# 3. Control conditions (Table: tab:control): Cohen's d vs Gold with 95% CI.
conds = ["Mismatch-tone", "Overlong", "Imperative", "Random"]
d_add = [(6.52, 5.36, 8.21), (4.05, 3.34, 5.27), (6.36, 5.19, 7.98), (1.87, 1.44, 2.48)]
d_lam = [(8.26, 7.10, 10.03), (3.84, 3.20, 4.90), (4.71, 3.73, 6.25), (1.89, 1.44, 2.54)]
n_add = [13, 50, 50, 50]; n_lam = [45, 50, 50, 50]
fig, ax = plt.subplots(figsize=(7.2, 3.3))
y = np.arange(4)[::-1]
for yi, (a, l, na, nl) in zip(y, zip(d_add, d_lam, n_add, n_lam)):
    ax.errorbar(a[0], yi + .16, xerr=[[a[0] - a[1]], [a[2] - a[0]]], fmt="o",
                color="#777", ms=7, capsize=3, lw=1.2)
    ax.errorbar(l[0], yi - .16, xerr=[[l[0] - l[1]], [l[2] - l[0]]], fmt="o",
                color=AMBER, ms=7, capsize=3, lw=1.2)
    ax.text(a[2] + .15, yi + .16, f"d = {a[0]:.2f}  (n = {na})", va="center", fontsize=9, color="#555")
    ax.text(l[2] + .15, yi - .16, f"d = {l[0]:.2f}  (n = {nl})", va="center", fontsize=9, color="#7B5E28")
ax.axvline(.8, color=STEEL, ls="--", lw=1)
ax.text(.9, 3.55, "target d ≥ 0.8", color=STEEL, fontsize=9.5)
ax.plot([], [], "o", color="#777", label="Additive fusion")
ax.plot([], [], "o", color=AMBER, label="λ-measure fusion")
ax.set_yticks(y, conds)
ax.set_xlim(0, 13.2); ax.set_ylim(-.6, 3.8)
ax.set_xlabel("Cohen's d against Gold (95% CI)")
ax.legend(frameon=False, loc="lower right", fontsize=9.5)
save(fig, "control.png")

# 4. Correlation with G-Eval overall (Table: tab:geval, "Overall" column).
subs = ["S_context  (contextual relevance)", "S_clarity  (conciseness)",
        "S_load  (cognitive load)", "S_risk  (risk-tone alignment)",
        "S_accept  (driver acceptability)"]
r = [.755, .441, .049, -.173, -.176]
cols = [STEEL, LIGHT, AMBER, AMBER, AMBER]
fig, ax = plt.subplots(figsize=(7.2, 3.0))
y = np.arange(5)[::-1]
ax.barh(y, r, color=cols, height=.58)
for yi, v in zip(y, r):
    ax.text(v + (.015 if v >= 0 else -.015), yi, f"{v:+.3f}", va="center",
            ha="left" if v >= 0 else "right", fontsize=10)
ax.axvline(0, color="#444", lw=.8)
ax.set_yticks(y, subs)
ax.set_xlim(-.4, .9)
ax.set_xlabel("Pearson r with G-Eval overall score (3,654 messages)")
save(fig, "geval.png")

# 5. Sub-score profile per method (Table: tab:comparison, GT, additive, 609 clips).
methods = ["Rule-based", "Qwen2.5-7B", "Qwen2.5-14B", "Llama-3.1-8B", "Gemma-2-9B", "GPT-5-mini"]
cols_ = ["DSAIS", "S_risk", "S_context", "S_clarity", "S_load", "S_accept"]
M = np.array([[.833, .743, .752, 1.000, 1.000, .667],
              [.794, .722, .747, .966, 1.000, .537],
              [.778, .735, .602, .827, .996, .732],
              [.700, .735, .571, .707, .999, .487],
              [.807, .730, .724, .972, .986, .624],
              [.663, .748, .533, .318, .954, .764]])
from matplotlib.colors import LinearSegmentedColormap
cmap = LinearSegmentedColormap.from_list("amb", ["#FFFFFF", "#EBDDC3", AMBER, "#7B5E28"])
fig, ax = plt.subplots(figsize=(7.4, 3.6))
ax.imshow(M, cmap=cmap, vmin=.3, vmax=1.0, aspect="auto")
for i in range(M.shape[0]):
    for j in range(M.shape[1]):
        ax.text(j, i, f"{M[i, j]:.3f}", ha="center", va="center", fontsize=9.5,
                color="white" if M[i, j] > .9 else INK)
ax.set_xticks(range(6), cols_)
ax.set_yticks(range(6), methods)
ax.axvline(.5, color="white", lw=4)
ax.xaxis.tick_top()
ax.tick_params(length=0)
for s in ax.spines.values():
    s.set_visible(False)
save(fig, "comparison.png")

# 6. Contextual relevance by risk level (Table: tab:stratum, ground-truth inputs).
lv = ["LOW", "MEDIUM", "HIGH"]
rb_add, qw_add = [.836, .599, .808], [.699, .827, .827]
rb_lam, qw_lam = [.943, .511, .678], [.708, .809, .789]
fig, axs = plt.subplots(1, 2, figsize=(7.4, 3.2), sharey=True)
for ax, rb, qw, ttl, ns in [(axs[0], rb_add, qw_add, "Additive fusion", "n = 383 / 213 / 13"),
                            (axs[1], rb_lam, qw_lam, "λ-measure fusion", "n = 273 / 291 / 45")]:
    x = np.arange(3); w = .36
    ax.bar(x - w/2, rb, w, color=GREY, label="Rule-based templates")
    ax.bar(x + w/2, qw, w, color=AMBER, label="Qwen2.5-7B (full framework)")
    for xi, a, b in zip(x, rb, qw):
        ax.text(xi - w/2, a + .015, f"{a:.2f}", ha="center", fontsize=8.5)
        ax.text(xi + w/2, b + .015, f"{b:.2f}", ha="center", fontsize=8.5)
    ax.set_xticks(x, lv)
    ax.set_title(f"{ttl}\n{ns}", fontsize=10)
    ax.set_ylim(0, 1.12)
axs[0].set_ylabel("S_context (ground-truth inputs)")
axs[0].legend(frameon=False, loc="upper center", fontsize=8.5, ncol=1,
              bbox_to_anchor=(1.05, -.13))
save(fig, "stratum.png")

# 7. BERTScore vs SMR across 36 cells (Table: tab:bertscore), DER highlighted.
B = {  # method: [(cond, bert, smr), ...]
    "Rule-based": [("TCR", .923, .903), ("VCR", .918, .823), ("DER", .907, .545),
                   ("DBR", .938, .882), ("2err", .911, .667), ("pred", .968, .726)],
    "Qwen2.5-7B": [("TCR", .924, .770), ("VCR", .926, .692), ("DER", .894, .631),
                   ("DBR", .901, .544), ("2err", .894, .511), ("pred", .921, .601)],
    "Qwen2.5-14B": [("TCR", .973, .840), ("VCR", .963, .771), ("DER", .939, .511),
                    ("DBR", .933, .823), ("2err", .939, .618), ("pred", .952, .708)],
    "Llama-3.1-8B": [("TCR", .938, .869), ("VCR", .934, .803), ("DER", .921, .531),
                     ("DBR", .923, .846), ("2err", .923, .644), ("pred", .928, .706)],
    "Gemma-2-9B": [("TCR", .913, .812), ("VCR", .922, .762), ("DER", .905, .499),
                   ("DBR", .907, .782), ("2err", .900, .587), ("pred", .912, .690)],
    "GPT-5-mini": [("TCR", .901, .902), ("VCR", .902, .823), ("DER", .895, .545),
                   ("DBR", .895, .881), ("2err", .894, .666), ("pred", .899, .726)],
}
fig, ax = plt.subplots(figsize=(6.6, 4.2))
for m, rows in B.items():
    for c, b, s in rows:
        if c == "DER":
            ax.plot(b, s, "o", color=AMBER, ms=8, zorder=4)
        elif c == "2err":
            ax.plot(b, s, "s", color=STEEL, ms=6, zorder=3)
        else:
            ax.plot(b, s, "o", color=LIGHT, ms=6, mec="#999", mew=.5, zorder=2)
ax.plot([], [], "o", color=AMBER, label="1err-DER (emotion misrecognised)")
ax.plot([], [], "s", color=STEEL, label="2err (two tasks misrecognised)")
ax.plot([], [], "o", color=LIGHT, mec="#999", label="other conditions")
ax.set_xlim(.80, 1.0); ax.set_ylim(.40, 1.0)
ax.annotate("BERTScore range 0.080", xy=(.934, .415), ha="center", fontsize=9.5, color="#555")
ax.annotate("", xy=(.894, .455), xytext=(.973, .455),
            arrowprops=dict(arrowstyle="<->", color="#555", lw=1))
ax.annotate("", xy=(.880, .499), xytext=(.880, .903),
            arrowprops=dict(arrowstyle="<->", color="#555", lw=1))
ax.text(.875, .70, "SMR range\n0.404", ha="right", va="center", fontsize=9.5, color="#555")
ax.set_xlabel("BERTScore F1 vs ground-truth messages")
ax.set_ylabel("Structural match rate (tone and risk level unchanged)")
ax.legend(frameon=False, loc="upper left", fontsize=9, bbox_to_anchor=(0, 1.0))
save(fig, "bertscore-vs-smr.png")
print("done")
