"""Figures for the MEM-MCL (IEEE DSS 2024) research-blog post.

Sources:
- Method figures: crops of Fig. 1 and Fig. 4 of the manuscript PDF
  (MEM-MCL folder, clean_version.pdf; read only, rendered to the scratch dir).
- Table III of the manuscript: task difficulty scores and ranks.
- Fig. 7 / Fig. 8 of the manuscript are bar charts without printed values. The
  values plotted here are the per-task scores in the authors' result sheet
  (図表/マージ論文結果.xlsx, Sheet1), which match the bars of Fig. 7 and Fig. 8.
Nothing is recomputed except simple differences between those values.
"""
import os
import subprocess
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

OUT = "/Users/ishitatakashishou/Sites/affectosphere-lab/public/column-images/dss2024-evolutionary-merging/"
SCR = "/private/tmp/claude-501/-Users-ishitatakashishou/62e336aa-c915-4181-a249-1463c108b1af/scratchpad/dss2024-evolutionary-merging/"
PDF = os.path.expanduser(
    "~/Desktop/研究/論文/感情分析に対するLLM進化的モデルマージに関する研究/論文/"
    "MEM-MCL(多段階進化的モデルマージとデータ駆動のカリキュラム学習)/clean_version.pdf")
os.makedirs(OUT, exist_ok=True)
os.makedirs(SCR, exist_ok=True)

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


# 0. Method figures: crop Fig. 1 (page 3) and Fig. 4 (page 4) from a 300-dpi render.
subprocess.run(["pdftoppm", "-r", "300", "-png", "-f", "3", "-l", "4", PDF, SCR + "hi"], check=True)
k = 300 / 110  # crop boxes were measured on a 110-dpi render
Image.open(SCR + "hi-3.png").convert("RGB").crop(
    (int(160 * k), int(92 * k), int(755 * k), int(378 * k))).save(OUT + "framework.png")
Image.open(SCR + "hi-4.png").convert("RGB").crop(
    (int(118 * k), int(82 * k), int(802 * k), int(368 * k))).save(OUT + "mem-mechanism.png")

# Task order and groups (Table I).
tasks = ["SC-2class-sen", "SC-2class-doc", "SC-3class", "SC-5class",
         "ABSA-ATSA", "ABSA-ACSA", "ABSA-TSD", "ABSA-ASD", "ABSA-ASTE", "ABSA-ASQP",
         "MAST-11class", "MAST-28class", "MAST-Hate", "MAST-Offensive", "MAST-Irony"]

# 1. Difficulty scores and ranks (Table III).
score = [4.5, 5, 5.5, 8, 4.5, 5.5, 6.5, 7.5, 9.5, 11.5, 18.5, 35.5, 9.5, 9.5, 9.5]
rank = [1, 2, 3, 6, 4, 5, 7, 8, 12, 13, 14, 15, 9, 10, 11]
order = np.argsort(rank)
gcol = {"SC": LIGHT, "ABSA": GREY, "MAST": STEEL}
fig, ax = plt.subplots(figsize=(7.2, 4.6))
y = np.arange(15)[::-1]
for yi, i in zip(y, order):
    g = tasks[i].split("-")[0]
    ax.barh(yi, score[i], color=gcol[g], height=.66)
    ax.text(score[i] + .4, yi, f"{score[i]:g}", va="center", fontsize=9.5)
ax.set_yticks(y, [f"{rank[i]:>2}. {tasks[i]}" for i in order], fontsize=10)
ax.set_xlim(0, 40)
ax.set_xlabel("Difficulty score = 1.0·C + 0.5·V + 2.0·Z + 5.0·S  (curriculum order, top = first)")
from matplotlib.patches import Patch
ax.legend(handles=[Patch(color=gcol[g], label=g) for g in gcol], frameon=False, loc="upper right")
save(fig, "difficulty.png")

# 2. Base vs expert vs MEM (values behind manuscript Fig. 7).
base = [92.8, 47.4, 36.8, 45, 18.76, 2.75, 50.59, 20.25, 24.6, 8.6, 3, 5.8, 38.04, 18.16, 63.29]
expert = [92.2, 95.2, 86.6, 47.2, 61.52, 7.5, 53.68, 24.25, 25.2, 9, 15.2, 12.2, 19.13, 22.42, 52.3]
mem = [91, 94.8, 87.6, 39.2, 67.22, 9.25, 48.46, 20.5, 24.8, 9.2, 4.6, 10.6, 25.34, 22.29, 59.94]


def grouped(vals, labels, colors, fname, ylabel):
    fig, axes = plt.subplots(3, 1, figsize=(7.4, 7.6))
    spans = [(0, 4, "Sentiment Classification (SC)"), (4, 10, "Aspect-Based Sentiment Analysis (ABSA)"),
             (10, 15, "Multifaceted Analysis of Subjective Text (MAST)")]
    w = .26
    for ax, (a, b, title) in zip(axes, spans):
        x = np.arange(b - a)
        for j, (v, lab, c) in enumerate(zip(vals, labels, colors)):
            ax.bar(x + (j - 1) * w, v[a:b], w, color=c, label=lab)
        ax.set_xticks(x, [t.split("-", 1)[1] for t in tasks[a:b]], fontsize=10)
        ax.set_title(title, fontsize=11, loc="left")
        ax.set_ylim(0, 105)
        ax.set_ylabel(ylabel)
    axes[0].legend(frameon=False, ncol=3, loc="upper right", bbox_to_anchor=(1, 1.32))
    fig.tight_layout()
    save(fig, fname)


grouped([base, expert, mem], ["Base (Llama 2)", "Expert (per task)", "MEM (one merged model)"],
        [GREY, STEEL, AMBER], "mem-vs-base-expert.png", "Score (%)")

# 3. MEM vs Unstructured vs MEM-MCL (values behind manuscript Fig. 8).
unstr = [72.6, 92.2, 80.8, 44.2, 55.34, 15.75, 41.8, 31.5, 25.4, 8.4, 3.8, 9.8, 38.04, 42.2, 52.3]
memmcl = [85.4, 91.6, 80.2, 46.6, 67.93, 19.5, 42.28, 28.75, 24.2, 10, 6, 10.2, 38.04, 41.73, 60.17]
grouped([mem, unstr, memmcl], ["MEM", "MEM + random task order", "MEM-MCL (easy → hard)"],
        [GREY, LIGHT, AMBER], "mcl-comparison.png", "Score (%)")

# 4. Change from MEM to MEM-MCL, tasks in curriculum order (Table III ranks).
fig, ax = plt.subplots(figsize=(7.2, 4.6))
y = np.arange(15)[::-1]
for yi, i in zip(y, order):
    d = memmcl[i] - mem[i]
    ax.barh(yi, d, color=AMBER if d > 0 else LIGHT, height=.66)
    ax.text(d + (.6 if d >= 0 else -.6), yi, f"{d:+.2f}", va="center",
            ha="left" if d >= 0 else "right", fontsize=9.5)
ax.axvline(0, color="#444", lw=.8)
ax.set_yticks(y, [f"{rank[i]:>2}. {tasks[i]}" for i in order], fontsize=10)
ax.set_xlim(-12, 27)
ax.set_xlabel("MEM-MCL − MEM (points; tasks in curriculum order, top = easiest)")
save(fig, "mcl-delta.png")

# 5. Win counts over the 15 tasks (derived from the same values).
pairs = [("MEM > Base", sum(m > b for m, b in zip(mem, base))),
         ("MEM > Expert", sum(m > e for m, e in zip(mem, expert))),
         ("MEM-MCL > MEM", sum(c > m for c, m in zip(memmcl, mem))),
         ("MEM-MCL > random order", sum(c > u for c, u in zip(memmcl, unstr)))]
fig, ax = plt.subplots(figsize=(7.2, 2.6))
y = np.arange(len(pairs))[::-1]
for yi, (lab, n) in zip(y, pairs):
    ax.barh(yi, 15, color="#F1EEE8", height=.55)
    ax.barh(yi, n, color=AMBER if "MCL" in lab else STEEL, height=.55)
    ax.text(n + .2, yi, f"{n} / 15", va="center", fontsize=10)
ax.set_yticks(y, [p[0] for p in pairs])
ax.set_xlim(0, 16.5)
ax.set_xlabel("Number of tasks (out of 15) where the first model scores higher")
save(fig, "win-counts.png")
print([p for p in pairs])
print("done")
