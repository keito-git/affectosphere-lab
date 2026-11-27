"""Figures for the 'Representational Magnitude' research-blog post (SSRN 7685786).
Every number is copied from the SSRN manuscript (manuscript.tex text and tables,
supplementary.tex Table S1); nothing is recomputed. overview.png and factorial.png
are the paper's own Figures 1-2, converted from PDF separately."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

OUT = "/Users/ishitatakashishou/Sites/affectosphere-lab/public/column-images/ssrn-representational-magnitude/"
AMBER, STEEL, GREY, LIGHT, INK = "#C4974A", "#3D6B8C", "#9AA0A6", "#D9D4CB", "#1A1A1A"
plt.rcParams.update({
    "font.family": "Arial", "font.size": 11, "axes.edgecolor": "#444",
    "axes.linewidth": 0.8, "axes.spines.top": False, "axes.spines.right": False,
    "xtick.color": "#333", "ytick.color": "#333", "axes.labelcolor": "#222",
    "savefig.dpi": 220, "savefig.bbox": "tight", "savefig.facecolor": "white",
})
FAM = ["Qwen2.5", "Llama-3.1", "Gemma-2", "Mistral", "OLMo-2", "Granite-3.1", "Falcon3"]


def save(fig, name):
    fig.savefig(OUT + name)
    plt.close(fig)


def range_bar(ax, y, lo, hi, color, label):
    ax.plot([lo, hi], [y, y], color=color, lw=9, solid_capstyle="butt", alpha=.9)
    ax.text(hi, y + .32, label, ha="right", va="bottom", fontsize=9.5, color="#333")


# 1. Magnitude vs raw effect vs gain, ranges over seven families
#    (Section V-B text: ||V||/||A|| 9.32-17.12, |kV|/|kA| 3.24-9.20, R_act +0.83 to +1.88).
fig, axes = plt.subplots(1, 3, figsize=(9.6, 2.6))
ax = axes[0]
ax.set_xscale("log")
range_bar(ax, 0, 9.32, 17.12, STEEL, "9.32 – 17.12")
ax.axvline(1, color=GREY, ls="--", lw=1)
ax.set_xlim(.8, 30)
ax.set_title("(a) Magnitude  ‖V‖ / ‖A‖", fontsize=11, loc="left")
ax.set_xlabel("ratio (log scale; >1 = valence larger)")
ax = axes[1]
ax.set_xscale("log")
range_bar(ax, 0, 3.24, 9.20, STEEL, "3.24 – 9.20")
ax.axvline(1, color=GREY, ls="--", lw=1)
ax.set_xlim(.8, 30)
ax.set_title("(b) Raw effect on choice  |k_V| / |k_A|", fontsize=11, loc="left")
ax.set_xlabel("ratio (log scale; >1 = valence larger)")
ax = axes[2]
range_bar(ax, 0, .83, 1.88, AMBER, "+0.83 – +1.88")
ax.axvline(0, color=GREY, ls="--", lw=1)
ax.set_xlim(-.5, 2.5)
ax.set_title("(c) Gain ratio  R_act", fontsize=11, loc="left")
ax.set_xlabel("log G_A − log G_V (>0 = action larger)")
for a in axes:
    a.set_yticks([])
    a.set_ylim(-.8, 1.2)
    a.spines["left"].set_visible(False)
fig.tight_layout(w_pad=2.0)
save(fig, "magnitude-vs-gain.png")

# 2. Ranges of R_d over seven families, transferred / own vectors, finite and gradient
#    (Sections V-C and V-D text).
rows = [("R  (finite), transferred", (.83, 1.88), (-3.57, -1.16)),
        (r"$R^{\nabla}$ (gradient), transferred", (.85, 1.78), (-3.44, -.93)),
        (r"$R^{\nabla}$ (gradient), own vectors", (.38, 1.52), (-2.75, -1.21))]
fig, ax = plt.subplots(figsize=(7.4, 2.9))
y = np.arange(len(rows))[::-1]
for yi, (lab, a, v) in zip(y, rows):
    ax.plot(a, [yi + .13] * 2, color=AMBER, lw=8, solid_capstyle="butt")
    ax.plot(v, [yi - .13] * 2, color=STEEL, lw=8, solid_capstyle="butt")
    ax.text(a[1] + .08, yi + .13, f"{a[0]:+.2f} to {a[1]:+.2f}", va="center", fontsize=9.5)
    ax.text(v[0] - .08, yi - .13, f"{v[0]:+.2f} to {v[1]:+.2f}", va="center", ha="right", fontsize=9.5)
ax.axvline(0, color="#444", lw=.8)
ax.set_yticks(y, [r[0] for r in rows])
ax.set_xlim(-5.2, 3.0)
ax.set_ylim(-.6, len(rows) - .4)
ax.plot([], [], color=AMBER, lw=6, label="action question")
ax.plot([], [], color=STEEL, lw=6, label="evaluation question")
ax.legend(frameon=False, loc="upper left", bbox_to_anchor=(0, -.22), ncol=2)
ax.set_xlabel("log gain ratio (range over seven families; >0 = action larger)")
save(fig, "reversal-ranges.png")


def dumbbell(name, act, val, xlab, xlim, act_lab="action question", val_lab="evaluation question"):
    fig, ax = plt.subplots(figsize=(7.2, 3.6))
    y = np.arange(len(FAM))[::-1]
    for yi, (am, alo, ahi), (vm, vlo, vhi) in zip(y, act, val):
        ax.plot([vm, am], [yi, yi], color=LIGHT, lw=2, zorder=1)
        ax.errorbar(am, yi, xerr=[[am - alo], [ahi - am]], fmt="o", color=AMBER, ms=7, capsize=3, zorder=3)
        ax.errorbar(vm, yi, xerr=[[vm - vlo], [vhi - vm]], fmt="o", color=STEEL, ms=7, capsize=3, zorder=3)
    ax.axvline(0, color="#444", lw=.8)
    ax.set_yticks(y, FAM)
    ax.set_xlim(*xlim)
    ax.set_xlabel(xlab)
    ax.plot([], [], "o", color=AMBER, label=act_lab)
    ax.plot([], [], "o", color=STEEL, label=val_lab)
    ax.legend(frameon=False, loc="upper left", bbox_to_anchor=(0, -.16), ncol=2)
    save(fig, name)


# 3. Receiver's own vectors (Table IV: tab5_transfer.tex).
own_act = [(1.35, .94, 1.91), (.55, .24, 1.04), (1.60, 1.20, 2.35), (1.08, .66, 1.74),
           (.73, .41, 1.11), (1.00, .58, 1.59), (.36, .02, .80)]
own_val = [(-1.49, -1.94, -1.22), (-1.66, -1.76, -1.57), (-1.38, -1.57, -1.21), (-2.81, -3.96, -2.26),
           (-2.25, -2.56, -2.01), (-1.77, -1.94, -1.61), (-2.36, -2.94, -2.00)]
dumbbell("own-vectors.png", own_act, own_val,
         "log gain ratio R_d with the receiver's own vectors (95% bootstrap CI)", (-4.4, 2.8))

# 4. Answer formats without valence words (Table II: tab2_formats.tex), R_val, transferred.
sym = [(-3.71, -6.69, -2.70), (-2.55, -2.78, -2.36), (-1.22, -1.67, -.81), (-1.46, -1.62, -1.32),
       (-2.56, -2.98, -2.29), (-3.37, -5.29, -2.62), (-1.93, -2.45, -1.58)]
yn = [(-1.54, -1.75, -1.38), (-1.71, -1.92, -1.51), (-1.20, -1.37, -1.03), (-2.57, -2.86, -2.35),
      (-3.30, -4.50, -2.69), (-1.79, -1.93, -1.68), (-1.08, -1.28, -.92)]
fig, ax = plt.subplots(figsize=(7.2, 3.6))
y = np.arange(len(FAM))[::-1]
for yi, (sm, slo, shi), (ym, ylo, yhi) in zip(y, sym, yn):
    ax.errorbar(sm, yi + .14, xerr=[[sm - slo], [shi - sm]], fmt="s", color=STEEL, ms=6, capsize=3)
    ax.errorbar(ym, yi - .14, xerr=[[ym - ylo], [yhi - ym]], fmt="o", color=GREY, ms=6, capsize=3)
ax.axvline(0, color="#444", lw=.8)
ax.set_yticks(y, FAM)
ax.set_xlim(-7.2, .6)
ax.set_xlabel("R_val under the evaluation question, transferred vectors (95% CI)")
ax.plot([], [], "s", color=STEEL, label="symbol format (Z / K)")
ax.plot([], [], "o", color=GREY, label="yes / no format")
ax.legend(frameon=False, loc="upper left", bbox_to_anchor=(0, -.16), ncol=2)
save(fig, "answer-formats.png")

# 5. Partial log gain ratios after controlling contrast overlap (Table III: tabS4_partial.tex).
p_act = [(2.13, 1.39, 4.31), (.90, .52, 1.47), (2.07, 1.45, 3.61), (1.02, .67, 1.47),
         (1.11, .80, 1.58), (1.00, .55, 1.61), (1.35, .88, 1.99)]
p_val = [(-.94, -1.21, -.65), (-2.75, -3.01, -2.55), (-1.66, -2.06, -1.34), (-1.78, -2.13, -1.54),
         (-1.79, -2.07, -1.49), (-1.67, -1.85, -1.50), (-1.50, -1.79, -1.26)]
dumbbell("partial-ratios.png", p_act, p_val,
         "partial log gain ratio, transferred vectors (95% bootstrap CI)", (-3.6, 4.8))

# 6. Layer sweep of R_act - R_val, receiver's own vectors (Table S1: tabS2_layer_sweep_wide.tex).
sweep = {
    "Qwen2.5": ([.15, .30, .44, .52, .59, .74, .89], [1.13, -1.54, 5.58, 2.85, 2.44, 1.81, 2.64],
                [-4.89, -5.83, 1.87, 2.30, 1.93, 1.25, -.33], [4.33, .14, 6.12, 3.68, 3.48, 2.78, 5.38], .52),
    "Llama-3.1": ([.16, .29, .32, .45, .61, .74, .90], [1.97, 6.27, 2.21, .85, 1.31, 2.01, 4.71],
                  [.31, 4.12, 1.90, -2.35, -1.59, 1.23, 3.30], [4.83, 8.67, 2.70, 3.17, 4.15, 3.27, 8.41], .32),
    "Gemma-2": ([.15, .29, .44, .61, .76, .90], [-.30, -2.95, 2.98, -.94, 2.45, 2.26],
                [-2.94, -6.85, 2.54, -2.28, -.97, -.60], [4.54, 1.89, 3.72, .07, 5.57, 5.95], .44),
    "Mistral": ([.16, .29, .39, .45, .61, .74, .90], [-.78, 2.40, 3.89, 3.90, 1.12, 2.48, 6.18],
                [-4.98, 1.98, 3.19, 3.20, -1.73, .88, 2.30], [2.20, 2.98, 5.33, 5.95, 4.47, 5.11, 8.53], .39),
    "OLMo-2": ([.16, .29, .35, .45, .61, .74, .90], [-.24, 1.60, 2.97, 2.46, -.89, -1.11, .57],
               [-3.31, .43, 2.61, 2.03, -2.82, -4.15, -.05], [1.55, 4.16, 3.39, 3.12, .57, .13, 1.65], .35),
    "Granite-3.1": ([.15, .31, .38, .46, .59, .74, .90], [.19, .75, 2.77, 2.02, -2.09, .63, -.93],
                    [-4.53, .33, 2.31, .30, -5.49, -.68, -3.61], [3.69, 1.31, 3.42, 4.90, -.94, 1.36, 1.29], .38),
    "Falcon3": ([.15, .30, .44, .59, .74, .89], [-.27, -.21, 2.73, 7.15, 4.31, 1.61],
                [-3.78, -3.41, 2.08, 1.78, 2.96, .32], [3.06, 2.95, 3.53, 6.10, 7.68, 4.49], .44),
}
fig, axes = plt.subplots(2, 4, figsize=(10.4, 5.0), sharex=True, sharey=True)
for ax, (fam, (d, m, lo, hi, ls)) in zip(axes.flat, sweep.items()):
    ax.fill_between(d, lo, hi, color=STEEL, alpha=.15, lw=0)
    ax.plot(d, m, "-o", color=STEEL, ms=4, lw=1.4)
    i = d.index(ls)
    ax.plot([ls], [m[i]], "o", color=AMBER, ms=8, zorder=5)
    ax.axvline(ls, color=AMBER, ls=":", lw=1)
    ax.axhline(0, color="#444", lw=.8)
    if fam == "Falcon3":  # point estimate lies outside its interval at depth 0.59 (Supp. S-III)
        ax.plot([.59], [7.15], "o", mfc="white", mec=STEEL, ms=6, zorder=6)
        ax.text(.60, 8.6, "unstable", fontsize=8.5, color="#666")
    ax.set_title(fam, fontsize=10.5)
    ax.set_ylim(-7.5, 10)
    ax.set_xlim(.1, .95)
axes.flat[-1].axis("off")
axes.flat[-1].text(.02, .62, "orange dot / dotted line:\nselected layer ℓ*\n\nband: 95% bootstrap CI",
                   fontsize=9.5, color="#333", transform=axes.flat[-1].transAxes)
fig.supxlabel("relative depth", fontsize=11)
fig.supylabel("R_act − R_val (own vectors)", fontsize=11)
fig.tight_layout()
save(fig, "layer-sweep.png")
print("done")
