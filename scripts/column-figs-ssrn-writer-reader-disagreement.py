"""Figures for the writer-reader disagreement research-blog post. Every number is
copied from the SSRN real-name manuscript (SSRN_20261030/latex_source, tables/*.tex
and documents/experiments.tex); nothing is recomputed. Figure 1 (framework) is the
paper's own fig1_framework_v9.pdf converted to PNG with pdftoppm."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

OUT = "/Users/ishitatakashishou/Sites/affectosphere-lab/public/column-images/ssrn-writer-reader-disagreement/"
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


# 2. Prompt-induced shift of k=0 students, 3 seeds (tables/prompt.tex).
rows = [("crowd-enVent · GPT-4o-mini · attribution", [-10, 38, 23]),
        ("crowd-enVent · Qwen3-8B · attribution", [-7, 40, 52]),
        ("WRIME · GPT-4o-mini · elicitation", [6, 1, -9]),
        ("WRIME · GPT-4o-mini · attribution", [11, 3, 4]),
        ("WRIME · Qwen3-8B · elicitation", [-34, -38, -33]),
        ("WRIME · Qwen3-8B · attribution", [-14, -22, -16])]
fig, ax = plt.subplots(figsize=(7.4, 3.4))
y = np.arange(len(rows))[::-1]
for yi, (lab, v) in zip(y, rows):
    ax.plot([min(v), max(v)], [yi, yi], color=LIGHT, lw=5, solid_capstyle="round", zorder=1)
    ax.scatter(v, [yi] * 3, color=STEEL, s=34, zorder=3)
ax.axvline(0, color="#444", lw=.8)
ax.text(1.5, len(rows) - .35, "toward reader →", fontsize=9.5, color="#555")
ax.text(-1.5, len(rows) - .35, "← toward writer", fontsize=9.5, color="#555", ha="right")
ax.set_yticks(y, [r[0] for r in rows])
ax.set_xlim(-45, 60)
ax.set_ylim(-.6, len(rows) - .1)
ax.set_xlabel("Prompt-induced shift D, % of reference gap G (dots = 3 seeds)")
save(fig, "prompt-shift.png")

# 3. Population-level shift vs text-level alignment at k=100 (tables/textlevel.tex).
#    Dotted line in the right panel: alignment between two disjoint reader groups
#    (experiments.tex, Sec. text-level: 0.68 crowd-enVent, 0.42 WRIME).
methods = ["Reference models", "Calibration", "Calibration, shuffled", "Prior ratio",
           "Marginal constant", "FT, anchors only", "FT, synthetic + anchors"]
cols = [GREY, AMBER, LIGHT, LIGHT, LIGHT, STEEL, STEEL]
data = {"crowd-enVent": ([1.00, .73, .65, .62, .62, .97, 1.64],
                         [.137, .113, .039, .081, None, .096, .128], .68),
        "WRIME": ([1.00, .43, .37, .37, .37, .48, .60],
                  [.116, .024, .001, .027, None, .035, .055], .42)}
fig, axes = plt.subplots(2, 2, figsize=(8.4, 5.6), sharey="row")
yy = np.arange(len(methods))[::-1]
for r, (corpus, (dg, A, rg)) in enumerate(data.items()):
    a1, a2 = axes[r]
    a1.barh(yy, dg, color=cols, height=.6)
    for yi, v in zip(yy, dg):
        a1.text(v + .02, yi, f"{v:.2f}", va="center", fontsize=9)
    a1.set_xlim(0, 1.9)
    a1.set_yticks(yy, methods)
    a1.set_title(f"{corpus}: population level (D/G)", fontsize=10.5, loc="left")
    for yi, v, c in zip(yy, A, cols):
        if v is None:
            a2.text(.004, yi, "n/a (reads no text)", va="center", fontsize=9, color="#777")
        else:
            a2.barh(yi, v, color=c, height=.6)
            a2.text(v + .004, yi, f"{v:.3f}", va="center", fontsize=9)
    a2.set_xlim(0, .75)
    a2.axvline(rg, color=INK, ls=":", lw=1)
    a2.text(rg - .01, yy[0] + .55, f"two reader groups: {rg:.2f}", ha="right", fontsize=9, color="#444")
    a2.set_title(f"{corpus}: text level (alignment A)", fontsize=10.5, loc="left")
    a2.set_ylim(-.6, len(methods) - .1)
axes[1][0].set_xlabel("D/G")
axes[1][1].set_xlabel("A")
fig.tight_layout()
save(fig, "shift-vs-alignment.png")

# 4. Direct difference supervision with all 30,000 WRIME labels (tables/direct.tex).
dr = [("Separate models", .118, -.023, GREY),
      ("Shared encoder", .125, .001, STEEL),
      ("Shared + diff. loss", .124, -.002, STEEL),
      ("Difference only", .100, .003, LIGHT),
      ("Direction only*", .114, .011, LIGHT),
      ("Writer mean, all (no text)", .220, .048, AMBER),
      ("Shared + writer, all", .244, .051, AMBER)]
fig, axes = plt.subplots(1, 2, figsize=(8.4, 3.3), sharey=True)
yy = np.arange(len(dr))[::-1]
for yi, (lab, a, r2, c) in zip(yy, dr):
    axes[0].barh(yi, a, color=c, height=.6)
    axes[0].text(a + .004, yi, f"{a:.3f}", va="center", fontsize=9)
    axes[1].barh(yi, r2, color=c, height=.6)
    axes[1].text(r2 + (.002 if r2 >= 0 else -.002), yi, f"{r2:+.3f}", va="center",
                 ha="left" if r2 >= 0 else "right", fontsize=9)
axes[0].set_yticks(yy, [d[0] for d in dr])
axes[0].set_xlim(0, .3)
axes[0].set_xlabel("Alignment A")
axes[1].axvline(0, color="#444", lw=.8)
axes[1].set_xlim(-.045, .075)
axes[1].set_xlabel("Explained text-level variance R²_text")
axes[0].axhline(1.5, color="#bbb", lw=.8)
axes[1].axhline(1.5, color="#bbb", lw=.8)
fig.tight_layout()
save(fig, "direct-supervision.png")

# 5. Writer-side input visibility on crowd-enVent (tables/visibility.tex).
groups = ["Size-matched writer model", "Whole-pool writer model"]
conds = ["masked", "unmasked", "+ keywords"]
A = [[.130, .208, .368], [.233, .389, .373]]
fig, ax = plt.subplots(figsize=(7.2, 3.3))
x = np.arange(2)
w = .26
for j, (cond, c) in enumerate(zip(conds, [GREY, STEEL, AMBER])):
    vals = [A[0][j], A[1][j]]
    ax.bar(x + (j - 1) * w, vals, w, color=c, label=f"writer input: {cond}")
    for xi, v in zip(x, vals):
        ax.text(xi + (j - 1) * w, v + .008, f"{v:.3f}", ha="center", fontsize=9)
ax.set_xticks(x, groups)
ax.set_ylim(0, .5)
ax.set_ylabel("Alignment A (803 test texts)")
ax.legend(frameon=False, loc="upper left", fontsize=9.5)
save(fig, "input-visibility.png")

# 6. Error split of the writer-reader difference on crowd-enVent (tables/app_cov.tex).
cv = [("Mean prediction", 1.561, .721, 1.000),
      ("Reader-pool texts,\nshared (358)", 1.424, .567, .991),
      ("Writer-pool subsets,\ndisjoint (358)", 1.432, .564, 1.005),
      ("Whole writer pool\n(4,860)", .913, .165, 1.283)]
fig, ax = plt.subplots(figsize=(7.6, 3.5))
x = np.arange(len(cv))
w = .26
for j, (lab, c) in enumerate([("writer error E_w", STEEL), ("error covariance C", LIGHT),
                               ("text-level error E_text", AMBER)]):
    vals = [r[j + 1] for r in cv]
    ax.bar(x + (j - 1) * w, vals, w, color=c, label=lab)
    for xi, v in zip(x, vals):
        ax.text(xi + (j - 1) * w, v + .02, f"{v:.2f}", ha="center", fontsize=8.5)
ax.axhline(1.0, color=GREY, ls="--", lw=1)
ax.set_xticks(x, [r[0] for r in cv], fontsize=9.5)
ax.set_ylim(0, 1.85)
ax.set_ylabel("Share of text-level variance V")
ax.legend(frameon=False, loc="upper left", fontsize=9.5, ncol=3)
save(fig, "error-covariance.png")
print("done")
