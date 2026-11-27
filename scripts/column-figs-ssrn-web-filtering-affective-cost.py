"""Figures for the research-blog post on SSRN 7647739
("The Hidden Affective Cost of Web Quality Filtering").
Every number is copied from the SSRN source (EmotionsWithoutWords SSRN_preprint/latex_source,
sections/experiments.tex tables and text); nothing is recomputed. The method figure
(overview.png) is the paper's own fig1_overview.pdf converted with pdftoppm."""
import shutil
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

OUT = "/Users/ishitatakashishou/Sites/affectosphere-lab/public/column-images/ssrn-web-filtering-affective-cost/"
SCRATCH = ("/private/tmp/claude-501/-Users-ishitatakashishou/62e336aa-c915-4181-a249-1463c108b1af/"
           "scratchpad/ssrn-web-filtering-affective-cost/overview.png")
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


# 0. Method figure: the paper's Figure 1 (fig1_overview.pdf -> PNG).
shutil.copy(SCRATCH, OUT + "overview.png")

# 1. Held-out M1 of the eight corpora with the BoW floor (Table "tab:e1").
corp = [("FineWeb", .493), ("RedPajama-V2", .485), ("RefinedWeb", .484), ("C4", .478),
        ("SlimPajama", .471), ("Pile", .465), ("Dolma", .460), ("FineWeb-Edu", .456)]
fig, ax = plt.subplots(figsize=(7.2, 3.5))
y = np.arange(len(corp))[::-1]
for yi, (n, v) in zip(y, corp):
    c = AMBER if n == "FineWeb-Edu" else (STEEL if n == "FineWeb" else LIGHT)
    ax.barh(yi, v - .34, left=.34, height=.62, color=c)
    ax.text(v + .002, yi, f"{v:.3f}", va="center", fontsize=10)
ax.axvline(.362, color=GREY, ls="--", lw=1)
ax.text(.364, y[0] + .55, "BoW floor 0.362", color="#666", fontsize=9.5)
ax.set_yticks(y, [c[0] for c in corp])
ax.set_xlim(.34, .52)
ax.set_ylim(-.6, len(corp) - .1)
ax.set_xlabel("Held-out M1 (macro-F1, 13 emotions, emotion words scrubbed)")
save(fig, "corpora.png")

# 2. Corpus densities per 1,000 words, FineWeb vs FineWeb-Edu (Table "tab:e1";
#    relative drops 27% / 74% / 70% stated in the text).
feats = ["Emotion words", "First-person\nsingular", "Narrative\nclauses"]
fw = [3.33, 12.10, 3.59]; edu = [2.41, 3.05, 1.06]; drop = ["−27%", "−74%", "−70%"]
fig, ax = plt.subplots(figsize=(6.8, 3.3))
x = np.arange(3); w = .36
ax.bar(x - w/2, fw, w, color=STEEL, label="FineWeb (source)")
ax.bar(x + w/2, edu, w, color=AMBER, label="FineWeb-Edu (filtered)")
for xi, a, b, d in zip(x, fw, edu, drop):
    ax.text(xi - w/2, a + .25, f"{a:.2f}", ha="center", fontsize=9.5)
    ax.text(xi + w/2, b + .25, f"{b:.2f}", ha="center", fontsize=9.5)
    ax.text(xi, max(a, b) + 1.4, d, ha="center", fontsize=11, color="#7B5E28", fontweight="bold")
ax.set_xticks(x, feats)
ax.set_ylim(0, 15)
ax.set_ylabel("Per 1,000 words")
ax.legend(frameon=False, loc="upper right")
save(fig, "densities.png")

# 3. Knowledge benchmark vs held-out M1 for the FineWeb pair (Section "Knowledge Gains";
#    knowledge = mean of MMLU, ARC, OpenBookQA; M1 from Table "tab:e1").
fig, axes = plt.subplots(1, 2, figsize=(7.2, 3.0))
for ax, vals, ttl, lim in [(axes[0], [.395, .455], "Knowledge benchmarks\n(mean of MMLU, ARC, OBQA)", (.35, .48)),
                           (axes[1], [.493, .456], "Emotion structure\n(held-out M1)", (.43, .51))]:
    ax.bar([0, 1], [v - lim[0] for v in vals], bottom=lim[0], color=[STEEL, AMBER], width=.55)
    for i, v in enumerate(vals):
        ax.text(i, v + .003, f"{v:.3f}", ha="center", fontsize=10.5)
    ax.set_xticks([0, 1], ["FineWeb", "FineWeb-Edu"])
    ax.set_ylim(*lim)
    ax.set_title(ttl, fontsize=10.5, loc="left")
fig.tight_layout()
save(fig, "knowledge.png")

# 4. Robustness of the FineWeb - FineWeb-Edu difference in M1 (Table "tab:robust").
rb = [("Discovery, one fold seed (P1)", .029, .013, .045),
      ("Held-out, one fold seed", .029, .012, .046),
      ("Held-out, five fold seeds", .037, .025, .048),
      ("Writer-grouped folds", .035, .024, .046),
      ("Logistic regression without PCA", .028, .016, .039),
      ("MLP probe", .038, .028, .047),
      ("Nearest-centroid probe", .062, .053, .072),
      ("EmpatheticDialogues (external)", .026, .018, .034),
      ("Zero-shot label completion", .012, -.004, .029)]
fig, ax = plt.subplots(figsize=(7.2, 3.8))
y = np.arange(len(rb))[::-1]
for yi, (n, m, lo, hi) in zip(y, rb):
    c = GREY if n.startswith("Zero-shot") else AMBER
    ax.plot([lo, hi], [yi, yi], color=c, lw=2)
    ax.plot(m, yi, "o", color=c, ms=7)
    ax.text(hi + .002, yi, f"{m:.3f}", va="center", fontsize=9.5)
ax.axvline(0, color="#444", lw=.8)
ax.set_yticks(y, [r[0] for r in rb])
ax.set_xlim(-.01, .085)
ax.set_xlabel("M1 difference, FineWeb − FineWeb-Edu (95% CI)")
save(fig, "robustness.png")

# 5. Odds ratios per SD for passing the educational filter (Table "tab:audit").
fits = ["Shard 1, base", "Shard 1, topic + domains", "Shard 2, base",
        "Shard 2, topic + domains", "Shard 1, parser proxy"]
OR = {"First person": [(.25, .20, .31), (.26, .20, .33), (.24, .20, .29), (.28, .23, .35), (.25, .19, .31)],
      "Narrative": [(.73, .60, .86), (.74, .60, .87), (.72, .59, .83), (.71, .57, .82), (.79, .63, .95)],
      "Emotion words": [(.98, .89, 1.05), (.91, .82, .97), (.88, .81, .95), (.87, .80, .94), (.90, .82, .97)]}
cols = {"First person": AMBER, "Narrative": STEEL, "Emotion words": GREY}
fig, ax = plt.subplots(figsize=(7.2, 3.6))
base = np.arange(len(fits))[::-1] * 1.0
for k, (feat, vals) in enumerate(OR.items()):
    off = (1 - k) * .22
    for yi, (m, lo, hi) in zip(base, vals):
        ax.plot([lo, hi], [yi + off, yi + off], color=cols[feat], lw=2)
        ax.plot(m, yi + off, "o", color=cols[feat], ms=6, label=feat if yi == base[0] else None)
ax.axvline(1, color="#444", lw=.8, ls="--")
ax.set_yticks(base, fits)
ax.set_xlim(0, 1.15)
ax.set_xlabel("Odds ratio per SD for being kept (95% CI); 1 = no association")
ax.legend(frameon=False, loc="upper center", ncol=3, bbox_to_anchor=(.45, 1.12), fontsize=10)
save(fig, "audit.png")

# 6. Retention after vocabulary deletion at 124M (Table "tab:e2"); exploratory, gate not met.
conds = ["emo-core", "emo-strict", "freq-matched", "class-matched"]
R1 = [(.78, .58, 1.06), (.76, .57, 1.02), (.83, .61, 1.12), (.72, .53, .98)]
R2 = [(.81, .59, 1.13), (.76, .56, 1.07), (.87, .69, 1.19), (.82, .65, 1.17)]
fig, ax = plt.subplots(figsize=(7.2, 3.3))
x = np.arange(4)
for vals, off, c, lab in [(R1, -.12, AMBER, "R1  category structure"), (R2, .12, STEEL, "R2  within-negative")]:
    for xi, (m, lo, hi) in zip(x, vals):
        ax.plot([xi + off] * 2, [lo, hi], color=c, lw=2)
        ax.plot(xi + off, m, "o", color=c, ms=7, label=lab if xi == 0 else None)
ax.axhline(1, color="#444", lw=.8, ls="--")
ax.text(3.45, 1.01, "full = 1", ha="right", va="bottom", fontsize=9, color="#555")
ax.set_xticks(x, conds)
ax.set_ylim(.4, 1.3)
ax.set_ylabel("Retention vs full (95% CI)")
ax.legend(frameon=False, loc="lower left", ncol=2, fontsize=10)
save(fig, "deletion.png")

# 7. Measurability gate across scales (Section "Measurability Across Model Scales";
#    124M: 0.0279 [0.021, 0.033]; 360M: 0.053 [0.051, 0.055];
#    1.71B FineWeb held-out floor-exceeding M1 = 0.131, no seed CI).
fig, ax = plt.subplots(figsize=(6.4, 3.2))
pts = [("124M", .0279, .021, .033, GREY), ("360M", .053, .051, .055, STEEL), ("1.71B\n(FineWeb)", .131, None, None, AMBER)]
for i, (n, m, lo, hi, c) in enumerate(pts):
    if lo is not None:
        ax.plot([i, i], [lo, hi], color=c, lw=2.5)
    ax.plot(i, m, "o", color=c, ms=9)
    ty = .018 if n == "124M" else m
    ax.text(i + .1, ty, f"{m:.3f}" if n != "124M" else f"{m:.4f} [0.021, 0.033]", va="center", fontsize=10)
ax.axhline(.03, color="#B5543C", ls="--", lw=1)
ax.text(2.4, .034, "gate: ΔM1 ≥ 0.03", ha="right", fontsize=9.5, color="#B5543C")
ax.set_xticks(range(3), [p[0] for p in pts])
ax.set_xlim(-.4, 2.5)
ax.set_ylim(0, .15)
ax.set_ylabel("Floor-exceeding M1 (held-out)")
save(fig, "scale.png")
print("done")
