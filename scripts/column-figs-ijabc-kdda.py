"""Figures for the KDDA research-blog post. Every number is copied from the
final IJABC manuscript (Authors/4_experiment.tex tables); nothing is recomputed
except gaps to Golden, which are simple differences of table values.
The paper's own figures (overview, confusion matrices, feature distribution)
are converted from the manuscript PDFs separately and copied into OUT."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

OUT = "/Users/ishitatakashishou/Sites/affectosphere-lab/public/column-images/ijabc-kdda/"
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

METHODS = ["LOZP", "CAZP", "AGOS", "ARISE", "KDDA"]
COLORS = [LIGHT, LIGHT, STEEL, GREY, AMBER]

# 1. Classification accuracy, DistilBERT trained on synthetic data only
#    (Table: tab:classification). Golden = trained on real data.
acc = {
    "IMDb":     ([.698, .802, .810, .813, .826], [.003, .003, .008, .010, .002], .863),
    "Yelp":     ([.802, .781, .872, .852, .872], [.004, .045, .021, .023, .019], .889),
    "Emotions": ([.233, .371, .300, .317, .405], [.002, .021, .004, .124, .006], .459),
}
fig, axes = plt.subplots(1, 3, figsize=(9.6, 3.4))
for ax, (ds, (m, s, g)) in zip(axes, acc.items()):
    x = np.arange(len(METHODS))
    ax.bar(x, m, yerr=s, color=COLORS, width=.66, capsize=3,
           error_kw=dict(ecolor="#333", lw=1))
    ax.axhline(g, color=INK, ls="--", lw=1)
    ax.text(-.4, g + .012, f"Golden (real) {g:.3f}", fontsize=9, color="#333")
    for xi, v, col in zip(x, m, COLORS):
        ax.text(xi, .015, f"{v:.3f}", ha="center", fontsize=8.5, rotation=90,
                color="#333" if col == LIGHT else "white", va="bottom")
    ax.set_xticks(x, METHODS, rotation=40, ha="right")
    ax.set_title(ds, fontsize=11)
    ax.set_ylim(0, 1.0)
axes[0].set_ylabel("Accuracy on 2,000 real test texts")
fig.tight_layout()
save(fig, "classification.png")

# 2. Distance to Golden for the four distribution metrics
#    (Table: tab:diversity_alignment). |method - Golden|, smaller = closer.
golden = {"IMDb": [.736, 1.543, 0.0, .141], "Yelp": [.717, 1.598, 0.0, .245],
          "Emotions": [.804, 1.583, 0.0, .226]}
vals = {
    "IMDb": {"LOZP": [.264, 1.567, .890, .616], "CAZP": [.488, 1.609, .605, .387],
             "AGOS": [.524, 1.398, .506, .306], "ARISE": [.525, 1.399, .510, .266],
             "KDDA": [.580, 1.562, .474, .320]},
    "Yelp": {"LOZP": [.287, 1.489, .859, .696], "CAZP": [.581, 1.609, .552, .424],
             "AGOS": [.600, 1.454, .477, .361], "ARISE": [.600, 1.453, .491, .383],
             "KDDA": [.677, 1.500, .483, .317]},
    "Emotions": {"LOZP": [.361, 1.509, 1.017, .893], "CAZP": [.606, 1.598, .536, .480],
                 "AGOS": [.686, 1.560, .477, .477], "ARISE": [.454, 1.524, .657, .768],
                 "KDDA": [.718, 1.477, .388, .292]},
}
metrics = ["MCD", "CE", "FID", "CD"]
fig, axes = plt.subplots(3, 4, figsize=(9.6, 6.6), sharey=True)
for r, ds in enumerate(["IMDb", "Yelp", "Emotions"]):
    for c, met in enumerate(metrics):
        ax = axes[r, c]
        gaps = [abs(vals[ds][mm][c] - golden[ds][c]) for mm in METHODS]
        best = int(np.argmin(gaps))
        y = np.arange(len(METHODS))[::-1]
        ax.barh(y, gaps, color=COLORS, height=.62,
                edgecolor=[INK if i == best else "none" for i in range(5)], linewidth=1.2)
        for yi, gv in zip(y, gaps):
            ax.text(gv + .01, yi, f"{gv:.3f}", va="center", fontsize=8)
        ax.set_yticks(y, METHODS, fontsize=9)
        ax.set_xlim(0, max(gaps) * 1.45 + .01)
        ax.tick_params(axis="x", labelsize=8)
        if r == 0:
            ax.set_title(met, fontsize=11)
        if c == 0:
            ax.set_ylabel(ds, fontsize=11)
fig.supxlabel("|value − Golden|  (smaller = closer to real data; outlined = closest)", fontsize=10)
fig.tight_layout()
save(fig, "distance-to-golden.png")

# 3. Ablation on Emotions (Table: tab:ablation). |value - Golden|.
abl_g = [.804, 1.583, 0.0, .226]
abl = [("KDDA (full)", [.718, 1.481, .390, .295], AMBER),
       ("w/o Domain Profile", [.635, 1.552, .604, .498], LIGHT),
       ("w/o Negative Example", [.542, 1.530, .552, .480], LIGHT),
       ("w/o Jaccard Filter", [.590, 1.561, .530, .455], LIGHT),
       ("w/o NLL Filter", [.603, 1.530, .510, .444], LIGHT)]
fig, axes = plt.subplots(1, 4, figsize=(9.6, 2.9), sharey=True)
for c, met in enumerate(metrics):
    ax = axes[c]
    y = np.arange(len(abl))[::-1]
    for yi, (lab, v, col) in zip(y, abl):
        gv = abs(v[c] - abl_g[c])
        ax.barh(yi, gv, color=col if col != LIGHT else GREY, height=.62)
        ax.text(gv + .008, yi, f"{gv:.3f}", va="center", fontsize=8.5)
    ax.set_yticks(y, [a[0] for a in abl], fontsize=9.5)
    ax.set_title(met, fontsize=11)
    ax.set_xlim(0, .78)
    ax.tick_params(axis="x", labelsize=8)
fig.supxlabel("|value − Golden| on Emotions (smaller = closer to real data)", fontsize=10)
fig.tight_layout()
save(fig, "ablation.png")
print("done")
