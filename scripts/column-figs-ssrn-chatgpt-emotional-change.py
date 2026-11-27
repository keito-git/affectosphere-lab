"""Figures for the research-blog post on the SSRN preprint 7649299
("Emotional Change in AI-Related Online Discussions After ChatGPT Is Directionally
Stable but Not Robust to Analytic Choices"). Every number is copied from the SSRN
manuscript (01_paper_HNAffect_emotional_change_SSRN.pdf, Tables 2-5 and Sec. 4.4);
nothing is recomputed. framework.png and cits-schematic.png are the paper's own
Figures 1 and 2, converted from PDF with pdftoppm."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

OUT = "/Users/ishitatakashishou/Sites/affectosphere-lab/public/column-images/ssrn-chatgpt-emotional-change/"
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


# 1. Single-series vs comparative level change, M1, sample 1 (Table 2).
emo = ["Anger", "Disgust", "Fear", "Joy", "Neutral", "Sadness", "Surprise"]
single = [-0.02, -0.40, 0.49, -0.15, -0.21, 0.06, 0.23]
comp = [0.14, -0.75, 0.98, -0.42, 0.92, -0.43, -0.44]
holm = ["1.000", "1.000", "<0.001", "1.000", "1.000", "0.497", "1.000"]
x = np.arange(len(emo)); w = .38
fig, ax = plt.subplots(figsize=(7.4, 3.6))
ax.bar(x - w/2, single, w, color=GREY, label="Step 1: single series (AI group only)")
ax.bar(x + w/2, comp, w, color=[AMBER if e == "Fear" else STEEL for e in emo],
       label="Step 2: comparative (AI − control)")
for xi, v, h in zip(x, comp, holm):
    ax.text(xi + w/2, v + (.05 if v >= 0 else -.05), f"Holm p\n{h}", ha="center",
            va="bottom" if v >= 0 else "top", fontsize=8, color="#333")
ax.axhline(0, color="#444", lw=.8)
ax.set_xticks(x, emo)
ax.set_ylim(-1.15, 1.45)
ax.set_ylabel("Level change β2 (pp)")
ax.legend(frameon=False, loc="lower left", bbox_to_anchor=(0, 1.0), ncol=2, fontsize=9.5)
save(fig, "primary-estimates.png")

# 2. Instruments: fear level change across ten samplings (Table 3).
inst = ["M1  DistilRoBERTa", "M2  GoEmotions RoBERTa", "M3  NRC lexicon"]
pos = [10, 9, 5]; sig = [8, 2, 0]; std_b2 = [1.02, 0.22, 0.35]
rho = [0.27, 0.27, 0.19]; auc = [0.75, 0.75, 0.65]
fig, ax = plt.subplots(figsize=(7.4, 2.8))
y = np.arange(3)[::-1]
ax.barh(y + .18, pos, .34, color=LIGHT, label="β2 > 0")
ax.barh(y - .18, sig, .34, color=[AMBER, STEEL, STEEL], label="p < 0.05 (nominal)")
for yi, p_, s_, b, r, a in zip(y, pos, sig, std_b2, rho, auc):
    ax.text(p_ + .15, yi + .18, f"{p_}/10", va="center", fontsize=9.5)
    ax.text(s_ + .15, yi - .18, f"{s_}/10", va="center", fontsize=9.5)
    ax.text(11.4, yi, f"std. β2 (sample 1) {b:+.2f}\nρ = {r:.2f}, AUC = {a:.2f}",
            va="center", fontsize=9, color="#333")
ax.set_yticks(y, inst)
ax.set_xlim(0, 16)
ax.set_xticks(range(0, 11, 2))
ax.set_xlabel("Number of the 10 independent samplings (fear, level change)")
ax.legend(frameon=False, loc="lower right", fontsize=9, bbox_to_anchor=(.66, -.02))
save(fig, "instruments.png")

# 3. Resampling: ten samplings and two-stage cluster bootstrap (Sec. 4.4 text).
lab = ["β2 > 0", "nominal p < 0.05", "Holm p < 0.05", "sign agrees\nacross M1–M3"]
samp = [100, 80, 30, 40]        # 10/10, 8/10, 3/10, 4/10 (Sec. 4.3-4.4)
boot = [96.5, 47.6, 18.1, 40.8]  # % of 1,000 bootstrap replicates
x = np.arange(4); w = .36
fig, ax = plt.subplots(figsize=(7.4, 3.3))
ax.bar(x - w/2, samp, w, color=STEEL, label="10 independent samplings")
ax.bar(x + w/2, boot, w, color=AMBER, label="1,000 bootstrap replicates")
for xi, a, b in zip(x, samp, boot):
    ax.text(xi - w/2, a + 1.5, f"{a:.0f}%", ha="center", fontsize=9.5)
    ax.text(xi + w/2, b + 1.5, f"{b:.1f}%", ha="center", fontsize=9.5)
ax.set_xticks(x, lab)
ax.set_ylim(0, 118)
ax.set_ylabel("Share (%)")
ax.legend(frameon=False, loc="upper right", fontsize=9.5)
save(fig, "resampling.png")

# 4. Specification and control-group variants for M1 fear (Table 4).
rows = [("Linear pre-trend (primary)", .98, "<0.001", AMBER),
        ("Month fixed effects", .97, "<0.001", LIGHT),
        ("Fourier terms, K = 2", 1.01, "<0.001", LIGHT),
        ("Quadratic pre-trend", .54, "0.017", LIGHT),
        ("ARIMA(1,0,0) errors", .93, "0.033", LIGHT),
        ("Spline pre-trend", .17, "0.481", STEEL),
        ("Local window ±12 months", -.01, "0.982", STEEL),
        ("Local window ±24 months", .66, "0.016", LIGHT),
        ("Local window ±36 months", .29, "0.260", LIGHT),
        ("Story-weighted means", .87, "0.001", LIGHT),
        ("Topic-matched control", .45, "0.009", LIGHT),
        ("Synthetic control", .13, "rank 16/21", LIGHT),
        ("AI-targeted comments", 1.29, "<0.001", LIGHT),
        ("AI-mentioning comments", 1.40, "<0.001", LIGHT),
        ("AI-mentioning, pooled, spline", .12, "0.721", STEEL)]
group = ["Step 6"] * 10 + ["Step 7"] * 2 + ["Subset"] * 3
fig, ax = plt.subplots(figsize=(7.4, 5.6))
y = np.arange(len(rows))[::-1]
for yi, (l, v, p, c) in zip(y, rows):
    ax.barh(yi, v, color=c, height=.62)
    ax.text(max(v, 0) + .03, yi, f"{v:+.2f}  (p {p})" if not p.startswith("rank") else f"{v:+.2f}  ({p})",
            va="center", fontsize=9)
for yb in (y[9] - .5, y[11] - .5):
    ax.axhline(yb, color="#bbb", lw=.7, ls=":")
ax.set_yticks(y, [f"{g}:  {r[0]}" for g, r in zip(group, rows)], fontsize=9.5)
ax.axvline(0, color="#444", lw=.8)
ax.set_xlim(-.1, 1.9)
ax.set_xlabel("Level change β2 of M1 fear (pp), sample 1")
save(fig, "specification.png")

# 5. Simulation: false-positive rate and power (Table 5).
meth = ["Single series", "Comparative", "Comp. + placebo", "Local ±24", "Spline pre-trend"]
fp = {"no drift": [11.1, 10.3, 3.7, 17.3, 13.1],
      "0.5× drift": [16.2, 17.4, 7.5, 17.9, 14.9],
      "1.0× drift": [30.6, 31.7, 14.3, 21.7, 21.2]}
pw = {"δ = 0.5": [44.9, 47.1, 25.1, 35.2, 37.0], "δ = 1.0": [70.2, 72.9, 51.8, 62.7, 66.7]}
fig, (a1, a2) = plt.subplots(1, 2, figsize=(9.2, 3.6), gridspec_kw=dict(wspace=.35))
x = np.arange(len(meth)); w = .26
for i, (k, c) in enumerate(zip(fp, [LIGHT, GREY, AMBER])):
    a1.bar(x + (i - 1) * w, fp[k], w, color=c, label=k)
a1.axhline(5, color=STEEL, ls="--", lw=1)
a1.text(4.55, 6, "nominal 5%", color=STEEL, fontsize=9, ha="right")
a1.set_xticks(x, meth, rotation=30, ha="right")
a1.set_ylabel("False-positive rate (%), δ = 0")
a1.set_title("(a) No true effect", fontsize=11)
a1.legend(frameon=False, fontsize=9, loc="upper center", bbox_to_anchor=(.55, 1.0))
w2 = .38
for i, (k, c) in enumerate(zip(pw, [STEEL, AMBER])):
    a2.bar(x + (i - .5) * w2, pw[k], w2, color=c, label=k)
a2.set_xticks(x, meth, rotation=30, ha="right")
a2.set_ylabel("Power (%), drift 1.0×")
a2.set_ylim(0, 100)
a2.set_title("(b) True effect δ (in SD)", fontsize=11)
a2.legend(frameon=False, fontsize=9, loc="upper right")
save(fig, "simulation.png")
print("done")
