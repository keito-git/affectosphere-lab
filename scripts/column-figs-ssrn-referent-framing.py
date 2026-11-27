"""Figures for the referent-framing research-blog post. Every number is copied
from the SSRN preprint (abstract id 7649338), Section V text and Tables III-IV;
nothing is recomputed. pipeline.png is converted from the paper's own Fig. 1."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

OUT = "/Users/ishitatakashishou/Sites/affectosphere-lab/public/column-images/ssrn-referent-framing/"
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


# 1. Person x referent crossing, preliminary run on Qwen2.5-7B (Sec. V-B text / Fig. 2).
lab = ["1st person\nreferent: the model", "1st person\nreferent: another",
       "3rd person\nreferent: the model", "3rd person\nreferent: another"]
v = [.460, .934, .828, .865]
fig, ax = plt.subplots(figsize=(7.2, 3.3))
cols = [AMBER, GREY, GREY, GREY]
ax.bar(range(4), v, color=cols, width=.6)
for i, x in enumerate(v):
    ax.text(i, x + .015, f"{x:.3f}", ha="center", fontsize=10)
ax.axhline(.5, color="#666", ls="--", lw=1)
ax.text(3.45, .51, "chance", color="#666", fontsize=9.5, ha="right")
ax.set_xticks(range(4), lab, fontsize=9.5)
ax.set_ylim(.3, 1.02)
ax.set_ylabel("identification AUC")
ax.set_title("Qwen2.5-7B, preliminary run (shared calibration)", fontsize=10, color="#555")
save(fig, "person-referent.png")

# 2. Five first-person referents, difference from human role-play (Sec. V-C, V-D text).
conds = ["this\nassistant", "named\nassistant", "an AI\nassistant", "fictional\nAI"]
setA = [-.046, -.052, -.099, .015]
setB = [-.085, np.nan, -.084, .008]   # named assistant not reported for set B
x = np.arange(4); w = .36
fig, ax = plt.subplots(figsize=(7.2, 3.5))
ax.axvspan(-.5, 2.5, color=STEEL, alpha=.07, lw=0)
ax.text(1, .045, "referent presented as real", ha="center", color=STEEL, fontsize=10)
ax.text(3, .045, "fictional", ha="center", color="#7B5E28", fontsize=10)
ax.bar(x - w/2, setA, w, color=[STEEL]*3 + [AMBER], label="stimulus set A (9 models)")
ax.bar(x + w/2, setB, w, color=[STEEL]*3 + [AMBER], alpha=.5, hatch="//",
       edgecolor="white", label="stimulus set B (5 models)")
for xi, a, b in zip(x, setA, setB):
    ax.text(xi - w/2, a + (.004 if a > 0 else -.004), f"{a:+.3f}", ha="center",
            va="bottom" if a > 0 else "top", fontsize=9)
    if not np.isnan(b):
        ax.text(xi + w/2, b + (.004 if b > 0 else -.004), f"{b:+.3f}", ha="center",
                va="bottom" if b > 0 else "top", fontsize=9)
    else:
        ax.text(xi + w/2, -.006, "n/r", ha="center", va="top", fontsize=9, color="#777")
ax.axhline(0, color="#444", lw=.8)
ax.set_xticks(x, conds)
ax.set_ylim(-.13, .06)
ax.set_ylabel("AUC difference from\nhuman role-play")
ax.legend(frameon=False, loc="lower left", fontsize=9)
save(fig, "referent-conditions.png")

# 3. Referential reality x referent type, stimulus set A, 9 models (Sec. V-C text / Fig. 6a).
fig, ax = plt.subplots(figsize=(6.2, 3.4))
ax.plot([0, 1], [.819, .887], "-o", color=AMBER, lw=2, ms=8, label="AI referent")
ax.plot([0, 1], [.837, .871], "-o", color=STEEL, lw=2, ms=8, label="human referent")
for xx, yy, c in [(0, .819, AMBER), (1, .887, AMBER), (0, .837, STEEL), (1, .871, STEEL)]:
    ax.text(xx + (-.06 if xx == 0 else .06), yy, f"{yy:.3f}", ha="right" if xx == 0 else "left",
            va="center", fontsize=10, color=c)
ax.set_xticks([0, 1], ["referent presented as real", "referent fictional"])
ax.set_xlim(-.4, 1.4)
ax.set_ylim(.8, .9)
ax.set_ylabel("identification AUC")
ax.legend(frameon=False, loc="upper left")
save(fig, "reality-type.png")

# 4. Replication: this assistant minus fictional AI on both stimulus sets (Table III).
mods = ["Qwen2.5-3B-Instruct", "Qwen2.5-7B-Instruct", "Qwen2.5-32B-Instruct", "Qwen3-8B", "Qwen3-14B"]
a = [-.194, -.076, -.131, .018, -.054]
b = [-.116, -.100, -.197, -.008, -.044]
fig, ax = plt.subplots(figsize=(5.6, 4.4))
ax.plot([-.25, .05], [-.25, .05], ls=":", color="#888", lw=1)
ax.axhline(0, color="#bbb", lw=.7); ax.axvline(0, color="#bbb", lw=.7)
ax.scatter(a, b, s=60, color=AMBER, zorder=3)
off = {"Qwen2.5-3B-Instruct": (5, -12), "Qwen2.5-7B-Instruct": (6, 2),
       "Qwen2.5-32B-Instruct": (6, 2), "Qwen3-8B": (-6, -14), "Qwen3-14B": (6, 4)}
for m, xa, yb in zip(mods, a, b):
    ax.annotate(m, (xa, yb), xytext=off[m], textcoords="offset points", fontsize=9,
                ha="right" if m == "Qwen3-8B" else "left")
ax.set_xlim(-.25, .05); ax.set_ylim(-.25, .05)
ax.set_xlabel("stimulus set A (this assistant − fictional AI)")
ax.set_ylabel("stimulus set B (independent rewrite)")
ax.text(-.245, .03, "means: A −0.087, B −0.093\nSpearman ρ = 0.90", fontsize=9.5, va="top")
save(fig, "replication.png")

# 5. Epistemic stance x referential reality, 9 models (Sec. V-F text / Fig. 8a).
fig, ax = plt.subplots(figsize=(6.2, 3.4))
ax.plot([0, 1], [.848, .872], "-o", color=STEEL, lw=2, ms=8, label="real ARIA (this assistant)")
ax.plot([0, 1], [.930, .889], "-o", color=AMBER, lw=2, ms=8, label="fictional ARIA (novel)")
for xx, yy, c in [(0, .848, STEEL), (1, .872, STEEL), (0, .930, AMBER), (1, .889, AMBER)]:
    ax.text(xx + (-.06 if xx == 0 else .06), yy, f"{yy:.3f}", ha="right" if xx == 0 else "left",
            va="center", fontsize=10, color=c)
ax.set_xticks([0, 1], ["state is a matter of fact", "state may be freely composed"])
ax.set_xlim(-.4, 1.4)
ax.set_ylim(.83, .95)
ax.set_ylabel("identification AUC")
ax.legend(frameon=False, loc="upper right", fontsize=9.5)
save(fig, "epistemic.png")

# 6. Primary contrasts, all three affects vs anger/joy only (Table IV).
rows = [("Critical comparison (20 models)", -.036, -.041, "14/20, p=.048", "13/20, p=.059"),
        ("This assistant vs fictional AI (9)", -.062, -.069, "8/9, p=.020", "8/9, p=.027"),
        ("Real vs fictional AI (9)", -.081, -.096, "9/9, p=.004", "9/9, p=.004"),
        ("Permission to report (9)", .076, .069, "9/9, p=.004", "8/9, p=.055"),
        ("This assistant vs fictional AI (5, set B)", -.093, -.076, "5/5, p=.063", "4/5, p=.188")]
fig, ax = plt.subplots(figsize=(7.4, 3.6))
y = np.arange(len(rows))[::-1]; h = .34
for yi, (lab_, m3, m2, s3, s2) in zip(y, rows):
    c = AMBER if lab_.startswith("Real") else STEEL
    ax.barh(yi + h/2, m3, h, color=c)
    ax.barh(yi - h/2, m2, h, color=c, alpha=.45)
    for val, yy, s in [(m3, yi + h/2, s3), (m2, yi - h/2, s2)]:
        ax.text(val + (.004 if val > 0 else -.004), yy, f"{val:+.3f}  ({s})", va="center",
                ha="left" if val > 0 else "right", fontsize=8.5)
ax.axvline(0, color="#444", lw=.8)
ax.set_yticks(y, [r[0] for r in rows], fontsize=9.5)
ax.set_xlim(-.2, .17)
ax.set_xlabel("mean effect (AUC); dark = 3 affects, light = anger & joy only")
save(fig, "restriction.png")
print("done")
