"""Figures for the research-blog post on SSRN 7634898
("Emotion Steering Is Specific to the Human Emotion Partition yet Remains Bound to Its
Output Encoding"). Every number is copied from the SSRN source (NativeAffect TAFFC SSRN
version, source/sections/tab*.tex and 04_results.tex); nothing is recomputed.
gates.png and floor.png are the paper's own fig1_three_gates.pdf and
fig2_floor_construction.pdf converted with pdftoppm."""
import shutil
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

OUT = "/Users/ishitatakashishou/Sites/affectosphere-lab/public/column-images/ssrn-steering-human-partition/"
SCRATCH = ("/private/tmp/claude-501/-Users-ishitatakashishou/62e336aa-c915-4181-a249-1463c108b1af/"
           "scratchpad/ssrn-steering-human-partition/")
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


# 0. Paper figures (Fig. 1 three gates, Fig. 2 floor construction).
shutil.copy(SCRATCH + "gates.png", OUT + "gates.png")
shutil.copy(SCRATCH + "floor.png", OUT + "floor.png")

# 1. Targets cleared (single-token readout) at Gate I (Table tab1_gate1), Gate II random
#    partitions (tab2_gate2) and Gate II activation-clustered partitions (tab3_gate2act).
models = ["Llama-3.2-1B", "Llama-3.1-8B", "OLMo-2-7B", "OLMo-2-13B", "Gemma-2-2B",
          "Gemma-2-9B", "Ministral-8B", "Mistral-Nemo-12B", "Phi-3-medium"]
g1 = [10, 10, 9, 6, 11, 8, 9, 12, 8]
g2r = [10, 6, 8, 8, 10, 7, 9, 11, 6]
g2a = [8, 7, 10, 9, 11, 7, 8, 8, 6]
fig, ax = plt.subplots(figsize=(9.2, 3.6))
x = np.arange(9); w = .27
ax.bar(x - w, g1, w, color=AMBER, label="Gate I: variance-matched floor")
ax.bar(x, g2r, w, color=STEEL, label="Gate II: 100 random partitions")
ax.bar(x + w, g2a, w, color=GREY, label="Gate II: 30 more-decodable partitions")
ax.axhline(7, color="#444", ls="--", lw=1, label="Majority (7/13)")
ax.set_xticks(x, models, rotation=30, ha="right", fontsize=9.5)
ax.set_yticks(range(0, 14, 2))
ax.set_ylim(0, 13.5)
ax.set_ylabel("Targets cleared (of 13)")
ax.legend(frameon=False, loc="upper center", ncol=2, fontsize=9, bbox_to_anchor=(.5, 1.18))
save(fig, "gates-1-2.png")

# 2. Gate III, codebook 1: median standardised excess (SD) on the emotion-word readout,
#    the code readout and the gradient positive control (Table tab4_gate3).
m3 = ["Llama-3.1-8B", "OLMo-2-13B", "Gemma-2-9B", "Ministral-8B", "Mistral-Nemo-12B"]
word = [3.19, 2.46, 1.53, 2.74, 2.82]
code = [0.62, 1.30, 0.59, 0.02, 1.55]
grad = [6.39, 5.95, 4.97, 4.92, 7.76]
wc = ["10/13", "9/13", "6/13", "9/13", "11/13"]
cc = ["2/13", "3/13", "4/13", "2/13", "6/13"]
fig, ax = plt.subplots(figsize=(8.6, 3.6))
x = np.arange(5); w = .27
ax.bar(x - w, word, w, color=AMBER, label="Emotion-word readout")
ax.bar(x, code, w, color=STEEL, label="Code readout (same directions)")
ax.bar(x + w, grad, w, color=LIGHT, label="Gradient direction for codes (control)")
for xi, a, b, ta, tb in zip(x, word, code, wc, cc):
    ax.text(xi - w, a + .12, ta, ha="center", fontsize=8.5)
    ax.text(xi, b + .12, tb, ha="center", fontsize=8.5)
ax.set_xticks(x, m3)
ax.set_ylim(0, 8.6)
ax.set_ylabel("Median standardised excess (SD)")
ax.legend(frameon=False, loc="upper left", fontsize=9)
save(fig, "gate3.png")

# 3. Paired summary behind an identical prefix (Section IV, Gate III text): medians over
#    the five judged models.
lab = ["Emotion-word readout", "Code readout", "Gradient control"]
med = [2.33, 0.45, 5.95]
cnt = ["9.0 / 13", "3.0 / 13", "13.0 / 13"]
fig, ax = plt.subplots(figsize=(6.4, 2.4))
y = np.arange(3)[::-1]
ax.barh(y, med, color=[AMBER, STEEL, LIGHT], height=.55)
for yi, v, c in zip(y, med, cnt):
    ax.text(v + .1, yi, f"+{v:.2f} SD   (targets cleared {c})", va="center", fontsize=9.5)
ax.set_yticks(y, lab)
ax.set_xlim(0, 9.5)
ax.set_xlabel("Median standardised excess, identical prefix (SD)")
save(fig, "paired.png")

# 4. Category-wise pass rates at Gate I (Table tab5_category, single-token readout),
#    with the readout AUC for that category.
cats = ["surprise", "trust", "disgust", "joy", "shame", "pride", "relief", "sadness",
        "boredom", "anger", "guilt", "fear", "no-emotion"]
npass = [9, 9, 8, 8, 8, 7, 7, 7, 6, 5, 4, 3, 2]
auc = [0.860, 0.978, 0.976, 0.907, 0.952, 0.967, 0.929, 0.971, 0.965, 0.943, 0.956, 0.968, 0.874]
fig, ax = plt.subplots(figsize=(7.4, 4.2))
y = np.arange(13)[::-1]
cols = [AMBER if c in ("surprise", "fear") else STEEL for c in cats]
ax.barh(y, npass, color=cols, height=.62)
for yi, n, a in zip(y, npass, auc):
    ax.text(n + .1, yi, f"{n}/9   AUC {a:.3f}", va="center", fontsize=9)
ax.set_yticks(y, cats)
ax.set_xlim(0, 12.2)
ax.set_xticks(range(0, 10, 3))
ax.set_xlabel("Models clearing the variance-matched floor (of 9)")
save(fig, "category.png")
print("done")
