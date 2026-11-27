"""Figures for the ACE-Net research-blog post. Every number is copied from the
KBS R3 manuscript (05_experiments.tex tables); nothing is recomputed."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

OUT = "/Users/ishitatakashishou/Sites/affectosphere-lab/public/column-images/ace-net/"
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

# 1. Main GoEmotions comparison (Table: main, Group A, A5 omitted for scale).
rows = [("A1  Baseline (DeBERTa-v3-base)", .4559, .0079, GREY),
        ("A2  + RAG (TF-IDF neighbours)", .452, .003, LIGHT),
        ("A3  + LLM context (concatenated)", .4552, .004, LIGHT),
        ("A4  + Self-training", .4604, .003, LIGHT),
        ("A6  Prefix-tuning (1 token)", .5037, .0072, STEEL),
        ("ACE-Net", .4965, .0065, AMBER)]
fig, ax = plt.subplots(figsize=(7.2, 3.4))
y = np.arange(len(rows))[::-1]
for yi, (lab, m, s, c) in zip(y, rows):
    ax.barh(yi, m - .43, left=.43, height=.62, color=c, xerr=s,
            error_kw=dict(ecolor="#333", lw=1, capsize=3))
    ax.text(m + s + .002, yi, f"{m:.4f}".rstrip("0"), va="center", fontsize=10)
ax.axvline(.4559, color=GREY, ls="--", lw=1)
ax.set_yticks(y, [r[0] for r in rows])
ax.set_xlim(.43, .525)
ax.set_xlabel("GoEmotions macro-F1 (28 classes, mean ± std over 5 seeds)")
save(fig, "main-results.png")

# 2. Injection-layer sweep (Table: layer-sweep).
L = np.arange(12)
m = np.array([.4748,.4679,.4857,.4819,.4886,.4969,.5004,.4930,.4987,.4732,.4382,.3728])
s = np.array([.0043,.0115,.0063,.0021,.0058,.0060,.0068,.0066,.0043,.0182,.0109,.0613])
fig, ax = plt.subplots(figsize=(7.2, 3.6))
ax.axvspan(4.5, 8.5, color=AMBER, alpha=.12, lw=0)
ax.text(6.5, .523, "effective band (L5–L8)", ha="center", color="#7B5E28", fontsize=10)
ax.fill_between(L, m - s, m + s, color=STEEL, alpha=.15, lw=0)
ax.plot(L, m, "-o", color=STEEL, ms=5, lw=1.6)
ax.plot([8], [.4987], "o", color=AMBER, ms=9, zorder=5)
ax.annotate("L = 8 (used)", (8, .4987), (9.1, .512), fontsize=10,
            arrowprops=dict(arrowstyle="-", color="#555", lw=.8))
ax.axhline(.4559, color=GREY, ls="--", lw=1)
ax.text(0, .4585, "baseline A1 (no injection)", color="#666", fontsize=9.5)
ax.set_xticks(L)
ax.set_ylim(.30, .53)
ax.set_xlabel("Injection layer L (0-based)")
ax.set_ylabel("macro-F1")
save(fig, "layer-sweep.png")

# 3. Core-mechanism ablation (Table: abl-core).
ab = [("C_full  (dictionary + Gumbel + adaptive τ)", .4965, .0065, AMBER),
      ("C_fixedτ  (fixed temperature)", .4947, .0062, LIGHT),
      ("C_noGumbel  (deterministic softmax)", .4948, .0078, LIGHT),
      ("C_nodiversity  (no diversity loss)", .4958, .0078, LIGHT),
      ("C_latefusion  (add at final CLS)", .4906, .0025, LIGHT),
      ("C_freevec  (one learned vector at L=8)", .4960, .0051, STEEL)]
fig, ax = plt.subplots(figsize=(7.2, 3.2))
y = np.arange(len(ab))[::-1]
for yi, (lab, mm, ss, c) in zip(y, ab):
    ax.errorbar(mm, yi, xerr=ss, fmt="o", color=c if c != LIGHT else "#777",
                ms=8, capsize=3, lw=1.2)
ax.axvline(.4965, color=AMBER, ls=":", lw=1)
ax.axvline(.4559, color=GREY, ls="--", lw=1)
ax.text(.4562, y[-1] - .55, "baseline A1", color="#666", fontsize=9.5)
ax.set_yticks(y, [a[0] for a in ab])
ax.set_xlim(.45, .51)
ax.set_ylim(-.9, len(ab) - .4)
ax.set_xlabel("GoEmotions macro-F1 (mean ± std over 5 seeds)")
save(fig, "ablation.png")

# 4. Selectivity across datasets (Table: crossdataset).
ds = ["GoEmotions\nimplicit, context-deficient", "SemEval-2018 E-c\nrare, ambiguous", "ISEAR\nexplicit, self-contained"]
d = [.041, .013, -.001]
p = ["p = 2.7e-5", "p = 0.003", "p = 0.81 (n.s.)"]
fig, ax = plt.subplots(figsize=(7.2, 3.3))
bars = ax.bar(range(3), d, color=[AMBER, "#D9B77A", LIGHT], width=.58)
for i, (v, pp) in enumerate(zip(d, p)):
    ax.text(i, max(v, 0) + .0015, f"{v:+.3f}\n{pp}", ha="center", va="bottom", fontsize=10)
ax.axhline(0, color="#444", lw=.8)
ax.set_xticks(range(3), ds)
ax.set_ylim(-.006, .055)
ax.set_ylabel("Δ macro-F1 (ACE-Net − baseline)")
save(fig, "selectivity.png")

# 5. Tail-3 decomposition (Table: tail3).
groups = ["All 28 classes", "25 classes\n(tail-3 excluded)", "Tail-3 only"]
base = [.4559, .5060, .0387]; ace = [.4965, .5136, .3539]
bs = [.0079, .0058, .0430]; as_ = [.0065, .0057, .0313]
x = np.arange(3); w = .36
fig, ax = plt.subplots(figsize=(7.2, 3.4))
ax.bar(x - w/2, base, w, yerr=bs, color=GREY, label="Baseline A1", capsize=3)
ax.bar(x + w/2, ace, w, yerr=as_, color=AMBER, label="ACE-Net", capsize=3)
for xi, b, a in zip(x, base, ace):
    ax.text(xi, max(a, b) + .05, f"Δ {a-b:+.3f}", ha="center", fontsize=10)
ax.set_xticks(x, groups)
ax.set_ylim(0, .65)
ax.set_ylabel("macro-F1")
ax.legend(frameon=False, loc="upper right")
save(fig, "tail3.png")

# 6. How much of the gain standard rebalancing reaches (Table: longtail).
lt = [("Logit adjustment", .0165), ("Class-balanced loss", .0207), ("ACE-Net", .0405)]
fig, ax = plt.subplots(figsize=(7.2, 2.4))
y = np.arange(3)[::-1]
for yi, (lab, v) in zip(y, lt):
    ax.barh(yi, v, color=AMBER if lab == "ACE-Net" else STEEL, height=.55)
    ax.text(v + .0008, yi, f"+{v:.4f}  ({v/.0405*100:.0f}% of ACE-Net gain)" if lab != "ACE-Net" else f"+{v:.4f}", va="center", fontsize=10)
ax.set_yticks(y, [l for l, _ in lt])
ax.set_xlim(0, .058)
ax.set_xlabel("Δ macro-F1 over baseline A1 (GoEmotions)")
save(fig, "rebalancing.png")

# 7. FORGE-Ω correlations (Table: forge-omega, frequency-controlled n = 444).
fo = [("ΔL  DeBERTa-v3-base", .345, .051, AMBER),
      ("ΔL  BERT-base", .4767, .0339, AMBER),
      ("Î  (allocation entropy)", 0.0, 0, LIGHT),
      ("ΔL_mask  (label-free surrogate)", .066, 0, LIGHT)]
fig, ax = plt.subplots(figsize=(7.2, 2.8))
y = np.arange(4)[::-1]
for yi, (lab, v, e, c) in zip(y, fo):
    ax.barh(yi, v, color=c, height=.55, xerr=e if e else None, capsize=3)
    t = "≈ 0 (n.s.)" if lab.startswith("Î") else (f"r = {v:.3f} (n.s.)" if v < .1 else f"r = {v:.3f}")
    ax.text(max(v + e, 0) + .01, yi, t, va="center", fontsize=10)
ax.set_yticks(y, [f[0] for f in fo])
ax.set_xlim(0, .62)
ax.set_xlabel("Pearson r with per-example improvement (frequency-controlled subset, n = 444)")
save(fig, "forge-omega.png")
print("done")
