"""Figures for the SSRN research-blog post (ssrn-generated-texts-llm-readers).
Every number is copied from the SSRN manuscript (main_ssrn.tex, 2026-11-10, and the
table row files it inputs: tables/harm_rows.tex, relabel_rows.tex, decomp_rows.tex,
js_rows.tex, readers_rows.tex) or from its Results text. Nothing is recomputed.
flow.png is the paper's own Figure 1 (fig1_cl_flow.pdf), rasterised unchanged."""
import os
import subprocess
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

SRC = ("/Users/ishitatakashishou/Desktop/研究/論文/CAIのための感情データ合成/"
       "プロジェクト3_判断の割れと合成の効果/04_原稿/CHBR投稿用/source/figures/")
OUT = "/Users/ishitatakashishou/Sites/affectosphere-lab/public/column-images/ssrn-generated-texts-llm-readers/"
os.makedirs(OUT, exist_ok=True)
AMBER, STEEL, GREY, LIGHT, INK = "#C4974A", "#3D6B8C", "#9AA0A6", "#D9D4CB", "#1A1A1A"
plt.rcParams.update({
    "font.family": "Arial", "font.size": 11, "axes.edgecolor": "#444",
    "axes.linewidth": 0.8, "axes.spines.top": False, "axes.spines.right": False,
    "xtick.color": "#333", "ytick.color": "#333", "axes.labelcolor": "#222",
    "savefig.dpi": 220, "savefig.bbox": "tight", "savefig.facecolor": "white",
})
LV = ["Low", "Mid", "High"]


def save(fig, name):
    fig.savefig(OUT + name)
    plt.close(fig)


def grouped(ax, series, colors, labels, width=.26, fmt="{:+.3f}", fs=8.5):
    x = np.arange(len(series[0]))
    k = len(series)
    for i, (s, c, lab) in enumerate(zip(series, colors, labels)):
        xs = x + (i - (k - 1) / 2) * width
        ax.bar(xs, s, width, color=c, label=lab)
        for xi, v in zip(xs, s):
            ax.text(xi, v + (.002 if v >= 0 else -.002), fmt.format(v).replace("-", "−"),
                    ha="center", va="bottom" if v >= 0 else "top", fontsize=fs)
    ax.axhline(0, color="#444", lw=.8)
    return x


# 0. Paper Figure 1 (analysis flow), rasterised from the PDF.
subprocess.run(["pdftoppm", "-png", "-r", "220", "-singlefile", SRC + "fig1_cl_flow.pdf", OUT + "flow"], check=True)

# 1. One-hot generated data on the majority-label student: raw vs calibrated CE (Table harm_rows).
fig, axes = plt.subplots(1, 2, figsize=(8.4, 3.3), sharey=True)
for ax, name, raw, cal in [(axes[0], "WRIME (Japanese)", [.012, .062, .079], [.022, .019, .003]),
                           (axes[1], "GoEmotions (English)", [.009, .082, .095], [.019, .029, .011])]:
    x = grouped(ax, [raw, cal], [LIGHT, STEEL], ["Raw CE", "Calibrated CE (after temperature scaling)"], width=.36)
    ax.set_xticks(x, LV)
    ax.set_xlabel("Human disagreement level")
    ax.set_title(name, fontsize=11)
    ax.set_ylim(0, .112)
axes[0].set_ylabel("Δ CE vs. majority-label student\n(positive = harm)")
axes[0].legend(frameon=False, loc="upper left", fontsize=9)
save(fig, "harm.png")

# 2. Label sources of generated texts on the majority-label student, WRIME (Table relabel_rows).
fig, ax = plt.subplots(figsize=(7.6, 3.4))
rows = [("One-hot", [.022, .020, .003], LIGHT),
        ("Hard-teacher mix", [-.008, -.005, -.009], GREY),
        ("p*-teacher mix", [-.010, -.019, -.016], "#D9B77A"),
        ("p*-teacher", [-.022, -.037, -.024], AMBER)]
x = grouped(ax, [r[1] for r in rows], [r[2] for r in rows], [r[0] for r in rows], width=.2, fs=8)
ax.set_xticks(x, [f"{l} disagreement" for l in LV])
ax.set_ylim(-.05, .035)
ax.set_ylabel("Calibrated Δ CE\n(negative = gain)")
ax.legend(frameon=False, ncol=4, loc="upper center", bbox_to_anchor=(.5, 1.13), fontsize=9)
save(fig, "relabel.png")

# 3. Decomposition: soft real labels vs. generated texts vs. distillation (Table decomp_rows).
fig, axes = plt.subplots(1, 2, figsize=(11.0, 3.8), sharey=True)
data = {"WRIME (Japanese)": ([-.029, -.046, -.075], [-.011, -.012, -.005], [-.015, -.019, -.009]),
        "GoEmotions (English)": ([-.059, -.119, -.112], [-.011, -.014, -.012], [-.023, -.022, -.022])}
labs = ["Soft real labels (vs. majority-label student)",
        "+ generated, same-data teacher (vs. soft-real)",
        "+ generated, full-data teacher (vs. soft-real)"]
for ax, (name, s) in zip(axes, data.items()):
    x = grouped(ax, list(s), [AMBER, STEEL, LIGHT], labs, width=.27, fs=7.6)
    ax.set_xticks(x, LV)
    ax.set_xlabel("Human disagreement level")
    ax.set_title(name, fontsize=11)
    ax.set_ylim(-.14, .01)
axes[0].set_ylabel("Calibrated Δ CE (negative = gain)")
axes[0].legend(frameon=False, loc="lower center", bbox_to_anchor=(1.05, -.42), ncol=3, fontsize=8.8)
save(fig, "decomposition.png")

# 4. Disagreement of humans vs. simulated readers on WRIME test texts (Results text).
fig, axes = plt.subplots(1, 2, figsize=(8.6, 3.2), gridspec_kw=dict(width_ratios=[1.6, 1]))
ax = axes[0]
x = grouped(ax, [[0.000, .174, .453], [.121, .118, .184]], [GREY, AMBER],
            ["Human annotators (D)", "10 simulated LLM readers (D_sim)"], width=.36, fmt="{:.3f}", fs=9)
ax.set_xticks(x, [f"{l}" for l in LV])
ax.set_xlabel("Human disagreement level")
ax.set_ylabel("Mean disagreement")
ax.set_ylim(0, .52)
ax.legend(frameon=False, loc="upper left", fontsize=9)
ax.text(1.0, .27, "Spearman ρ(D_sim, D) = 0.185", fontsize=9, ha="center", color="#444")
ax = axes[1]
ax.bar([0, 1], [21.6, 41.5], color=[GREY, AMBER], width=.55)
for i, v in enumerate([21.6, 41.5]):
    ax.text(i, v + 1, f"{v}%", ha="center", fontsize=10)
ax.set_xticks([0, 1], ["Humans", "Simulated\nreaders"])
ax.set_ylim(0, 50)
ax.set_ylabel("Unanimous test texts (%)")
fig.tight_layout()
save(fig, "reader-disagreement.png")

# 5. JSD from the human label distribution by level (Table js_rows).
rows = [("Simulated readers, vote share", [.260, .359, .487], AMBER, "-o"),
        ("Simulated readers, entropy-matched", [.364, .362, .402], "#D9B77A", "-s"),
        ("Class prior of training texts (ignores the text)", [.642, .521, .448], GREY, "--^"),
        ("Soft-real student (never saw test texts)", [.239, .228, .265], STEEL, "-D")]
fig, ax = plt.subplots(figsize=(7.4, 3.4))
for lab, v, c, st in rows:
    ax.plot(range(3), v, st, color=c, label=lab, lw=1.8, ms=6)
ax.annotate("0.487", (2, .487), (2.06, .50), fontsize=9, color="#7B5E28")
ax.annotate("0.448", (2, .448), (2.06, .43), fontsize=9, color="#555")
ax.set_xticks(range(3), [f"{l} disagreement" for l in LV])
ax.set_xlim(-.2, 2.35)
ax.set_ylim(.15, .7)
ax.set_ylabel("Mean JSD from human distribution")
ax.legend(frameon=False, fontsize=8.8, loc="upper center", bbox_to_anchor=(.5, 1.27), ncol=2)
save(fig, "jsd.png")

# 6. Labels of generated texts on the soft-real student, WRIME (Table readers_rows).
rows = [("Same-data p*-teacher", [-.011, -.012, -.005], STEEL),
        ("Simulated readers, vote share", [-.001, .027, .007], AMBER),
        ("Simulated readers, mean probability", [-.003, .026, .007], "#D9B77A"),
        ("Simulated readers, entropy-matched", [-.002, .018, .008], LIGHT)]
fig, ax = plt.subplots(figsize=(7.8, 3.4))
x = grouped(ax, [r[1] for r in rows], [r[2] for r in rows], [r[0] for r in rows], width=.2, fs=7.8)
ax.set_xticks(x, [f"{l} disagreement" for l in LV])
ax.set_ylim(-.02, .036)
ax.set_ylabel("Calibrated Δ CE vs. soft-real student\n(positive = harm)")
ax.legend(frameon=False, ncol=2, loc="upper center", bbox_to_anchor=(.5, 1.25), fontsize=9)
save(fig, "reader-labels.png")
print("done")
