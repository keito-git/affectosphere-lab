"""Figures for the research-blog post on "Same Confusion, Different Failure" (SSRN 7685198).
Every number is copied from the SSRN manuscript source
(~/Desktop/研究/論文/新研究_VLM感情_CVPR2027/SSRN用_2026-11-10/source/: numbers.tex,
supp_tables.tex, sec/4_experiments.tex); nothing is recomputed from raw data."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

OUT = "/Users/ishitatakashishou/Sites/affectosphere-lab/public/column-images/ssrn-vlm-criterion-bias/"
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

DATASETS = ["KDEF", "JAFFE", "WSEFEP", "UIBVFED", "RAF-DB", "ExpW"]
WILD = {"RAF-DB", "ExpW"}
MODELS = ["Gemma 3", "Qwen3-VL", "InternVL3.5", "Mistral"]
MARK = {"Gemma 3": "o", "Qwen3-VL": "s", "InternVL3.5": "D", "Mistral": "^"}

# Supplementary Table "tab:full" (SuppFullRows): seven-way AUC (first token),
# seven-way c (first token), two-choice c (full label) with 95% bootstrap interval.
FULL = {
    "KDEF":    [(.912, -2.52, -2.05, -2.54, -1.72), (.937, -2.53, -1.58, -1.88, -1.35),
                (.901, -2.51, -1.46, -1.72, -1.26), (.893, -1.15, -0.95, -1.20, -0.74)],
    "JAFFE":   [(.933, -1.57, -1.02, -2.01, -0.45), (.973, -2.08, -1.00, -1.66, -0.56),
                (.964, -2.61, -1.39, -2.40, -0.79), (.949, -1.25, -1.14, -2.14, -0.54)],
    "WSEFEP":  [(.920, -7.36, -6.20, -8.00, -5.20), (.905, -4.44, -3.24, -4.37, -2.63),
                (.848, -9.22, -6.64, -10.56, -4.69), (.869, -2.45, -2.40, -3.12, -2.00)],
    "UIBVFED": [(.825, -1.89, -1.50, -2.08, -1.06), (.750, -4.65, -1.81, -2.15, -1.53),
                (.839, -3.88, -2.74, -3.34, -2.36), (.782, -1.47, -1.33, -1.74, -1.04)],
    "RAF-DB":  [(.767, -0.61, -0.21, -0.28, -0.14), (.827, -1.35, -0.74, -0.83, -0.65),
                (.714, -1.65, -1.05, -1.16, -0.95), (.606, -0.53, -0.49, -0.57, -0.41)],
    "ExpW":    [(.690, -0.95, -0.72, -0.81, -0.65), (.751, -1.26, -0.77, -0.85, -0.69),
                (.642, -1.74, -1.47, -1.59, -1.37), (.648, -0.73, -0.79, -0.88, -0.71)],
}

# 1. Two-choice fear/surprise criterion with 95% intervals in all 24 cells (tab:full).
fig, ax = plt.subplots(figsize=(7.2, 5.4))
labels, y = [], 0
yt = []
for ds in DATASETS[::-1]:
    for mi, m in enumerate(MODELS[::-1]):
        auc, c7, c2, lo, hi = FULL[ds][MODELS.index(m)]
        col = STEEL if ds in WILD else AMBER
        ax.errorbar(c2, y, xerr=[[c2 - lo], [hi - c2]], fmt=MARK[m], color=col,
                    ms=5.5, capsize=2.5, lw=1)
        yt.append(y); labels.append(f"{ds}  ·  {m}")
        y += 1
    y += .6
ax.axvline(0, color="#444", ls="--", lw=1)
ax.set_yticks(yt, labels, fontsize=8.5)
ax.set_xlim(-11, 1)
ax.set_xlabel("Two-choice fear/surprise criterion c  (negative = threshold on the surprise side)")
ax.text(-10.8, yt[-1] + 1.2, "posed / synthetic", color="#7B5E28", fontsize=10)
ax.text(-10.8, 8.3, "in the wild", color=STEEL, fontsize=10)
ax.set_ylim(-1, yt[-1] + 2.2)
save(fig, "criterion.png")

# 2. Seven-way output AUC vs seven-way criterion (tab:full, first-token columns).
fig, ax = plt.subplots(figsize=(7.2, 4.0))
for ds in DATASETS:
    for mi, m in enumerate(MODELS):
        auc, c7 = FULL[ds][mi][:2]
        ax.scatter(c7, auc, marker=MARK[m], s=46, color=STEEL if ds in WILD else AMBER,
                   edgecolor="white", lw=.6, zorder=3)
ax.axvline(0, color="#444", ls="--", lw=1)
for m in MODELS:
    ax.scatter([], [], marker=MARK[m], color="#777", label=m)
ax.scatter([], [], marker="s", color=AMBER, label="posed / synthetic")
ax.scatter([], [], marker="s", color=STEEL, label="in the wild")
ax.legend(frameon=False, fontsize=9, ncol=3, loc="lower left", bbox_to_anchor=(0, -.42))
ax.set_xlabel("Seven-way criterion c")
ax.set_ylabel("Seven-way output AUC\n(fear vs. surprise)")
ax.set_xlim(-9.8, .6)
ax.set_ylim(.55, 1.0)
save(fig, "auc-vs-criterion.png")

# 3. Separability loss counts at the 0.15 cutoff (Supplementary Table "tab:cutoff").
fig, ax = plt.subplots(figsize=(7.2, 3.0))
rows = [("Anger/disgust, posed + synthetic", 13, 16, AMBER),
        ("Anger/disgust, in the wild", 0, 8, LIGHT),
        ("Fear/surprise, posed + synthetic", 0, 16, LIGHT),
        ("Fear/surprise, in the wild", 2, 8, STEEL)]
yy = np.arange(len(rows))[::-1]
for yi, (lab, k, n, c) in zip(yy, rows):
    ax.barh(yi, n, color="#F1EEE8", height=.6)
    ax.barh(yi, k, color=c, height=.6)
    ax.text(n + .3, yi, f"{k} / {n} cells", va="center", fontsize=10)
ax.set_yticks(yy, [r[0] for r in rows])
ax.set_xlim(0, 19.5)
ax.set_xlabel("Cells with probe AUC − output AUC ≥ 0.15 (separability loss)")
save(fig, "separability-loss.png")

# 4. Calibration hierarchy, mean over 4 models with range (Table "tab:hier").
refs = ["Raw", "Content-\nfree", "Neutral\nfaces", "Other\nexpressive", "Supervised\noffset"]
HIER = {  # mean, lo, hi per reference
    "KDEF":    [(-2.18, -2.53, -1.15), (-1.30, -2.32, -.36), (-1.71, -2.66, -1.05), (-1.85, -2.44, -1.37), (.22, .05, .29)],
    "JAFFE":   [(-1.88, -2.61, -1.25), (-.95, -2.26, -.40), (-.53, -1.48, .55), (-.92, -1.30, -.59), (.30, .03, .65)],
    "WSEFEP":  [(-5.87, -9.22, -2.45), (-4.35, -8.91, -1.52), (-4.54, -7.35, -1.36), (-3.55, -4.98, -2.52), (.11, .02, .20)],
    "UIBVFED": [(-2.97, -4.65, -1.47), (-1.83, -3.62, -.69), (-1.66, -1.99, -1.34), (-1.50, -1.95, -.90), (.20, .16, .25)],
    "RAF-DB":  [(-1.03, -1.65, -.53), (-.31, -1.41, .12), (-.88, -1.51, -.65), (-.69, -1.24, -.29), (.05, -.05, .18)],
    "ExpW":    [(-1.17, -1.74, -.73), (-.57, -1.52, -.15), (-.95, -1.46, -.56), (-.95, -1.42, -.53), (.12, .03, .24)],
}
fig, axes = plt.subplots(1, 2, figsize=(8.2, 3.8), sharey=False)
x = np.arange(5)
for ax, group, title in [(axes[0], ["KDEF", "JAFFE", "WSEFEP", "UIBVFED"], "Posed / synthetic"),
                         (axes[1], ["RAF-DB", "ExpW"], "In the wild")]:
    for gi, ds in enumerate(group):
        v = HIER[ds]
        m = np.array([a[0] for a in v]); lo = np.array([a[1] for a in v]); hi = np.array([a[2] for a in v])
        off = (gi - (len(group) - 1) / 2) * .14
        col = [AMBER, "#D9B77A", "#8C6A2E", GREY][gi] if title.startswith("Posed") else [STEEL, "#7FA3BF"][gi]
        ax.errorbar(x + off, m, yerr=[m - lo, hi - m], fmt="-o", color=col, ms=5, lw=1.3,
                    capsize=2.5, label=ds)
    ax.axhline(0, color="#444", ls="--", lw=1)
    ax.axvspan(.5, 3.5, color=LIGHT, alpha=.25, lw=0)
    ax.set_xticks(x, refs, fontsize=8.2)
    ax.set_title(title, fontsize=11)
    ax.legend(frameon=False, fontsize=9, loc="lower right")
axes[0].set_ylabel("Fear/surprise criterion c\n(mean of 4 models, range bars)")
axes[0].set_ylim(-9.6, 1.2); axes[1].set_ylim(-2, .6)
axes[0].text(2, .75, "label-free references", ha="center", fontsize=8.5, color="#666")
axes[1].text(2, .42, "label-free references", ha="center", fontsize=8.5, color="#666")
fig.tight_layout()
save(fig, "calibration.png")

# 5. Cross-dataset transfer of the supervised offset: mean absolute criterion (sec:transfer-res).
tr = [("posed/synth. → other posed/synth.", .80, AMBER), ("in the wild → posed/synth.", 1.08, LIGHT),
      ("posed/synth. → in the wild", .72, LIGHT), ("in the wild → other in the wild", .34, STEEL)]
fig, ax = plt.subplots(figsize=(7.2, 2.6))
yy = np.arange(4)[::-1]
for yi, (lab, v, c) in zip(yy, tr):
    ax.barh(yi, v, color=c, height=.58)
    t = f"{v:.2f}" + ("   over-corrects; mean accuracy change −0.058" if v == .72 else "")
    ax.text(v + .02, yi, t, va="center", fontsize=10)
ax.set_yticks(yy, [t[0] for t in tr])
ax.set_xlim(0, 1.6)
ax.set_xlabel("Mean |criterion| after applying a source offset to a target dataset (lower is better)")
save(fig, "transfer.png")

# 6. In-context examples on KDEF: two-choice criterion per condition (Supplementary Table "tab:ex").
conds = ["No examples", "Examples,\ntrue labels", "Examples,\nswapped labels", "Examples,\nno labels",
         "Neutral faces", "Blank images"]
EX = {  # criterion per model (Gemma 3, Qwen3-VL, InternVL3.5, Mistral)
    "No examples": [-1.69, -1.60, -1.43, -.86],
    "Examples,\ntrue labels": [-.16, -.66, -.93, -.32],
    "Examples,\nswapped labels": [-.02, -.77, -.98, -.44],
    "Examples,\nno labels": [-.61, -.78, -.76, -.45],
    "Neutral faces": [-1.87, -1.63, -1.64, -1.17],
    "Blank images": [-1.28, -1.31, -1.29, -.62],
}
fig, ax = plt.subplots(figsize=(7.4, 3.4))
w = .19
x = np.arange(len(conds))
cols = [AMBER, "#D9B77A", STEEL, GREY]
for mi, m in enumerate(MODELS):
    ax.bar(x + (mi - 1.5) * w, [EX[c][mi] for c in conds], w, color=cols[mi], label=m)
ax.axhline(0, color="#444", lw=.8)
ax.set_xticks(x, conds, fontsize=8.8)
ax.set_ylabel("KDEF two-choice criterion c")
ax.set_ylim(-2.1, .2)
ax.legend(frameon=False, fontsize=9, ncol=4, loc="lower center", bbox_to_anchor=(.5, -.42))
save(fig, "examples.png")
print("done")
