"""Figures for the research-blog post on "The Same Data Can Help or Harm:
Learner-State-Dependent Data Value in Emotion Recognition" (SSRN 7685783).
Every number is copied from the SSRN manuscript (main.tex text and tables/*.tex
in TNNLS投稿用_v5/SSRN用/source); nothing is recomputed. The method figures
(overview.png, directions.png) are converted from the paper's own PDFs."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

OUT = "/Users/ishitatakashishou/Sites/affectosphere-lab/public/column-images/ssrn-learner-state-data-value/"
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


# 1. Exchange rate of label-conditioned generation across n
#    (Section "Evaluation of the Exchange Rate", text: GoEmotions, RoBERTa-base;
#    f = 0.00 at 500, 0.23 at 4k, -0.75 at 16k, -0.71 at full; n0 ≈ 6,700;
#    full real pool = 31,756 from Table "Statistics of the two corpora").
n = np.array([500, 4000, 16000, 31756])
f = np.array([0.00, 0.23, -0.75, -0.71])
fig, ax = plt.subplots(figsize=(7.2, 3.5))
ax.axhspan(0, .45, color=AMBER, alpha=.08, lw=0)
ax.axhspan(-1.0, 0, color=STEEL, alpha=.06, lw=0)
ax.axhline(0, color="#444", lw=.8)
ax.plot(n, f, "-o", color=AMBER, ms=7, lw=1.8)
labels = ["0.00", "+0.23", "−0.75", "−0.71"]
offs = [(0, 10), (0, 10), (0, -18), (0, -18)]
for xi, yi, t, o in zip(n, f, labels, offs):
    ax.annotate(t, (xi, yi), textcoords="offset points", xytext=o, ha="center", fontsize=10)
ax.axvline(6700, color=GREY, ls="--", lw=1)
ax.text(6700 * 1.08, .33, "zero point $n_0$ ≈ 6,700", color="#555", fontsize=10)
ax.text(560, .36, "helps", color="#7B5E28", fontsize=10)
ax.text(560, -.9, "harms", color=STEEL, fontsize=10)
ax.set_xscale("log")
ax.set_xticks(n, ["500", "4k", "16k", "full\n(31,756)"])
ax.minorticks_off()
ax.set_ylim(-1.0, .45)
ax.set_xlabel("Real-data size n of the student (log scale)")
ax.set_ylabel("Exchange rate f(n)")
ax.set_title("GoEmotions, RoBERTa-base, label-conditioned generation (one-hot labels)",
             fontsize=10.5, loc="left")
save(fig, "exchange-curve.png")

# 2. Value of different pools at the late stage
#    (Section "Evaluation of the Exchange Rate", text values).
go = [("Generated, one-hot", -0.71, GREY),
      ("Generated, teacher argmax", -0.51, LIGHT),
      ("Generated, teacher soft", 0.31, AMBER),
      ("Back-translation (real, edited)", 0.57, STEEL)]
wr = [("Generated, one-hot", -0.65, GREY),
      ("Real, reader labels", 0.67, STEEL),
      ("Real, writer labels", 0.70, STEEL)]
fig, axes = plt.subplots(1, 2, figsize=(9.2, 3.2), gridspec_kw=dict(width_ratios=[4, 3], wspace=.75))
for ax, rows, title in [(axes[0], go, "GoEmotions: f on the full pool"),
                        (axes[1], wr, "WRIME: late-stage f")]:
    y = np.arange(len(rows))[::-1]
    for yi, (lab, v, c) in zip(y, rows):
        ax.barh(yi, v, color=c, height=.58)
        ax.text(v + (.04 if v >= 0 else -.04), yi, f"{v:+.2f}".replace("-", "−"), va="center",
                ha="left" if v >= 0 else "right", fontsize=10)
    ax.axvline(0, color="#444", lw=.8)
    ax.set_yticks(y, [r[0] for r in rows])
    ax.set_xlim(-1.05, 1.0)
    ax.set_xlabel("Exchange rate f")
    ax.set_title(title, fontsize=10.5, loc="left")
save(fig, "pool-rates.png")

# 3. Entropy-matched direction intervention (Table "tab2_direction_v5").
dirs = ["teacher", "prior", "uniform", "permuted"]
wr25 = [-0.07, -0.59, -0.80, -0.63]
wr50 = [0.20, -0.55, -0.93, -0.75]
go50_s0 = [-0.0213, -0.0017, 0.0120, 0.0223]
go50_s1 = [-0.0176, 0.0035, 0.0187, 0.0281]
fig, axes = plt.subplots(1, 2, figsize=(9.6, 3.5), gridspec_kw=dict(wspace=.35))
ax = axes[0]
x = np.arange(4); w = .36
ax.bar(x - w/2, wr25, w, color=LIGHT, label="a = 0.25")
ax.bar(x + w/2, wr50, w, color=[AMBER, GREY, GREY, GREY], label="a = 0.5")
for xi, v in zip(x, wr50):
    ax.text(xi + w/2, v + (.03 if v >= 0 else -.03), f"{v:+.2f}".replace("-", "−"), ha="center",
            va="bottom" if v >= 0 else "top", fontsize=9)
ax.axhline(-0.65, color=STEEL, ls="--", lw=1)
ax.text(-.45, -0.69, "one-hot labels: −0.65", color=STEEL, fontsize=9, va="top", ha="left")
ax.axhline(0, color="#444", lw=.8)
ax.set_xticks(x, dirs)
ax.set_ylim(-1.1, .4)
ax.set_ylabel("Late-stage f (mean of 3 seeds) ↑")
ax.set_title("WRIME", fontsize=10.5, loc="left")
ax.legend(frameon=False, loc="upper right", fontsize=9)
ax = axes[1]
ax.scatter(x - .08, go50_s0, color=[AMBER, GREY, GREY, GREY], s=46, zorder=3, label="seed 0")
ax.scatter(x + .08, go50_s1, color=[AMBER, GREY, GREY, GREY], s=46, marker="s", zorder=3, label="seed 1")
ax.axhspan(0.0174, 0.0219, color=STEEL, alpha=.15, lw=0)
ax.text(-.4, 0.0225, "one-hot (+0.0174 / +0.0219)", color=STEEL, fontsize=9)
ax.axhline(0, color="#444", lw=.8)
ax.set_xticks(x, dirs)
ax.set_xlim(-.5, 3.5)
ax.set_ylim(-.03, .036)
ax.set_ylabel("Late-stage ΔCE (a = 0.5) ↓")
ax.set_title("GoEmotions", fontsize=10.5, loc="left")
ax.legend(frameon=False, loc="lower right", fontsize=9)
save(fig, "direction.png")

# 4. Same-data teacher on WRIME (Table "tab3_same_teacher_v5").
ns = ["8k", "16k", "25.5k (full)"]
st = [("Gen / teacher", [0.48, 0.13, 0.02], AMBER, "o"),
      ("Gen / one-hot", [-0.07, -0.72, -1.15], STEEL, "s"),
      ("Gen / permuted", [-0.18, -0.75, -1.36], GREY, "^"),
      ("Gen / uniform", [-0.24, -0.94, -1.53], "#777", "D")]
fig, ax = plt.subplots(figsize=(7.2, 3.5))
xs = np.arange(3)
for lab, v, c, mk in st:
    ax.plot(xs, v, "-" + mk, color=c, lw=1.6, ms=6, label=lab)
    ax.text(2.08, v[-1] + (.09 if v[-1] > 0 else 0), f"{lab}  " + f"{v[-1]:+.2f}".replace("-", "−"), va="center", fontsize=9.5, color=c)
ax.axhline(0, color="#444", lw=.8)
ax.set_xticks(xs, ns)
ax.set_xlim(-.2, 3.1)
ax.set_ylim(-1.7, .7)
ax.set_xlabel("Real-data size n (teacher and student share the same real data)")
ax.set_ylabel("Exchange rate f")
save(fig, "same-teacher.png")

# 5. Cost of the permuted direction, strength-matched (Table "tab6_matched").
cols = ["Δgen\n(unmatched)", "Δgen\nTV-matched", "Δgen\nKL-matched", "Δreal"]
go_c = [-1.07, -0.99, -1.06, -0.88]
wr_c = [-0.97, -0.73, -0.87, -0.37]
seeds_go = ["", "2/3", "3/3", ""]
seeds_wr = ["", "3/3", "3/3", ""]
fig, axes = plt.subplots(1, 2, figsize=(9.6, 3.4), sharey=True, gridspec_kw=dict(wspace=.12))
for ax, vals, sd, title in [(axes[0], go_c, seeds_go, "GoEmotions"), (axes[1], wr_c, seeds_wr, "WRIME")]:
    cs = [AMBER, "#D9B77A", "#D9B77A", STEEL]
    ax.bar(range(4), vals, color=cs, width=.6)
    for i, (v, s) in enumerate(zip(vals, sd)):
        t = f"{v:+.2f}".replace("-", "−") + (f"\n({s})" if s else "")
        ax.text(i, v - .03, t, ha="center", va="top", fontsize=9.5)
    ax.axhline(0, color="#444", lw=.8)
    ax.set_xticks(range(4), cols, fontsize=9.5)
    ax.set_title(title, fontsize=10.5, loc="left")
    ax.set_ylim(-1.35, .05)
axes[0].set_ylabel("Cost of permuted direction\n(Δ late-stage f, mean of 3 seeds)")
save(fig, "matched-cost.png")

# 6. Update-trajectory probe (Section "Update Trajectory Analysis", text:
#    rho = 0.63 after 1 update, 0.90 after 2, 0.93 after 5, then between
#    0.88 and 0.94 until the end of three epochs = 423 steps; WRIME, n = 16k).
fig, ax = plt.subplots(figsize=(7.2, 3.2))
ax.fill_between([5, 423], .88, .94, color=AMBER, alpha=.22, lw=0)
ax.text(40, .955, "stays within 0.88–0.94 up to step 423", color="#7B5E28", fontsize=10)
ax.plot([1, 2, 5], [.63, .90, .93], "-o", color=AMBER, ms=7, lw=1.8)
for xi, yi in zip([1, 2, 5], [.63, .90, .93]):
    ax.annotate(f"{yi:.2f}", (xi, yi), textcoords="offset points", xytext=(8, -12), fontsize=10)
ax.set_xscale("log")
ax.set_xticks([1, 2, 5, 10, 100, 423], ["1", "2", "5", "10", "100", "423"])
ax.minorticks_off()
ax.set_ylim(.5, 1.0)
ax.set_xlabel("Number of actual updates on the auxiliary pool (log scale)")
ax.set_ylabel("Spearman ρ between\n−ΔCE(t) and f")
save(fig, "trajectory.png")
print("done")
