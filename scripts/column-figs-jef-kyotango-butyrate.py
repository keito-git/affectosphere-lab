"""Figures for the Kyotango butyrate research-blog post. Every number is copied
from the accepted JEF R1 manuscript (改稿R1_JEF/manuscript/Authors/4_Foodways.tex
and 5_Score.tex tables); nothing is recomputed. The method-flow and mechanism
figures are the paper's own PDFs, rasterised with pdftoppm."""
import subprocess
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

OUT = "/Users/ishitatakashishou/Sites/affectosphere-lab/public/column-images/jef-kyotango-butyrate/"
SRC = ("/Users/ishitatakashishou/Desktop/研究/論文/湧太郎の研究/浜詰遺跡から見る京丹後長寿の秘訣/"
       "改稿R1_JEF/manuscript/figures/")
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

# 0. Paper's own figures (Fig. 1 method flow, Fig. 10 mechanism), read-only source.
for pdf, png in [("fig_method_flow.pdf", "method-flow"), ("fig10_mechanism.pdf", "mechanism")]:
    subprocess.run(["pdftoppm", "-png", "-r", "110", "-singlefile", SRC + pdf, OUT + png], check=True)

# 1. Hamazume fish remains, >=2 mm fraction (Table: tab:fish, N = 1,472).
fish = [("Exocoetidae\n(flying fish)", 488, 34), ("Tetraodontidae\n(pufferfish)", 432, 29),
        ("Clupeidae\n(mainly sardine)", 351, 24)]
fig, ax = plt.subplots(figsize=(7.2, 2.8))
y = np.arange(3)[::-1]
for yi, (lab, n, p) in zip(y, fish):
    ax.barh(yi, n, color=AMBER if yi == 2 else STEEL, height=.58)
    ax.text(n + 8, yi, f"{n} specimens ({p}%)", va="center", fontsize=10)
ax.set_yticks(y, [f[0] for f in fish])
ax.set_xlim(0, 640)
ax.set_xlabel("NISP in the ≥2 mm sieve fraction (N = 1,472), Hamazume 6th excavation")
save(fig, "fish.png")

# 2. Hamazume shellfish, top species by MNI (Table: tab:shellfish). Oyster is ">100".
shell = [("Pacific oyster", 100, "Brackish lagoon", ">100"),
         ("Japanese turban shell", 86, "Open sea, rocky", "86"),
         ("Globular surf clam", 69, "Open sea, sandy", "69"),
         ("Yamato clam", 28, "Brackish lagoon", "28"),
         ("Rock shell", 16, "Open sea, rocky", "16"),
         ("Bloody clam", 13, "Inner bay", "13"),
         ("Japanese hard clam", 3, "Inner bay", "3")]
hab_col = {"Brackish lagoon": AMBER, "Open sea, rocky": STEEL, "Open sea, sandy": "#7FA3BF",
           "Inner bay": GREY}
fig, ax = plt.subplots(figsize=(7.2, 3.4))
y = np.arange(len(shell))[::-1]
for yi, (lab, v, h, t) in zip(y, shell):
    ax.barh(yi, v, color=hab_col[h], height=.6, hatch="//" if t.startswith(">") else None,
            edgecolor="white" if not t.startswith(">") else "#7B5E28", lw=0)
    ax.text(v + 1.5, yi, f"MNI {t}", va="center", fontsize=10)
ax.set_yticks(y, [s[0] for s in shell])
ax.set_xlim(0, 125)
ax.set_xlabel("Minimum number of individuals (MNI)")
for h, c in hab_col.items():
    ax.barh(np.nan, 0, color=c, label=h)
ax.legend(frameon=False, loc="lower right", fontsize=9.5, title="Habitat", title_fontsize=9.5)
save(fig, "shellfish.png")

# 3. BPPS by era, stacked axes A-D, median of 4 raters, with rater range (Table: tab:scores).
eras = ["Jomon", "Yayoi–\nKofun†", "Nara–\nHeian", "Medieval", "Early\nModern", "Modern"]
A = [1.25, 0.5, 1.75, 1.75, 2.5, 2.0]
B = [0.5, 0.0, 1.0, 1.5, 2.25, 2.0]
C = [2.25, 2.0, 1.75, 1.75, 1.0, 1.5]
D = [1.75, 1.75, 2.0, 2.0, 1.0, 2.0]
tot = [5.75, 4.25, 6.5, 7.0, 6.75, 7.5]
lo = [5.0, 4.0, 6.0, 6.5, 6.0, 7.0]
hi = [7.0, 5.0, 7.0, 7.0, 7.0, 8.5]
cols = [AMBER, "#8A6A35", STEEL, LIGHT]
labs = ["A: Soluble fiber", "B: Fermented / preserved", "C: Seafood diversity", "D: Overall diversity"]
x = np.arange(6)
fig, ax = plt.subplots(figsize=(7.4, 3.8))
bottom = np.zeros(6)
for vals, c, l in zip([A, B, C, D], cols, labs):
    bars = ax.bar(x, vals, .6, bottom=bottom, color=c, label=l, edgecolor="white", lw=.6)
    bars[1].set_hatch("//")
    bottom += np.array(vals)
ax.errorbar(x, tot, yerr=[np.array(tot) - lo, np.array(hi) - tot], fmt="none",
            ecolor="#333", capsize=3, lw=1)
for xi, t, h in zip(x, tot, hi):
    ax.text(xi, h + .2, f"{t:g}", ha="center", fontsize=10, fontweight="bold")
ax.set_xticks(x, eras)
ax.set_ylim(0, 10)
ax.set_ylabel("BPPS (0–10, median of 4 raters)")
ax.legend(frameon=False, ncol=2, fontsize=9.5, loc="upper left")
ax.text(5.45, -2.2, "† proxy data (Aoya-Kamijichi, Tottori)", ha="right", fontsize=9, color="#555")
save(fig, "bpps-era.png")

# 4. Axis profile heatmap (Table: tab:scores, axes A-D).
M = np.array([A, B, C, D])
fig, ax = plt.subplots(figsize=(7.4, 2.8))
from matplotlib.colors import LinearSegmentedColormap
cmap = LinearSegmentedColormap.from_list("amb", ["#FFFFFF", AMBER, "#6E4F1C"])
im = ax.imshow(M, cmap=cmap, vmin=0, vmax=2.5, aspect="auto")
for i in range(4):
    for j in range(6):
        ax.text(j, i, f"{M[i, j]:g}", ha="center", va="center", fontsize=10,
                color="white" if M[i, j] >= 1.9 else INK)
ax.set_xticks(range(6), eras)
ax.set_yticks(range(4), labs)
for s in ax.spines.values():
    s.set_visible(False)
ax.tick_params(length=0)
cb = fig.colorbar(im, ax=ax, fraction=.03, pad=.02)
cb.set_label("Axis score (0–2.5)", fontsize=9.5)
cb.outline.set_visible(False)
save(fig, "axis-profile.png")

# 5. Inter-rater agreement by axis, all four raters (Table: tab:reliability).
ax_names = ["A: Soluble fiber", "B: Fermented foods", "C: Seafood diversity", "D: Overall diversity"]
exact = [42, 72, 44, 31]
within = [69, 92, 83, 83]
fig, ax = plt.subplots(figsize=(7.2, 3.0))
y = np.arange(4)[::-1]
ax.barh(y, within, .6, color=LIGHT, label="within 0.5 pt")
ax.barh(y, exact, .6, color=STEEL, label="exact match")
for yi, e, w in zip(y, exact, within):
    ax.text(e - 1.5, yi, f"{e}%", va="center", ha="right", color="white", fontsize=10)
    ax.text(w + 1.5, yi, f"{w}%", va="center", fontsize=10)
ax.set_yticks(y, ax_names)
ax.set_xlim(0, 105)
ax.set_xlabel("Share of rater pairs (24 cells, 4 raters)")
ax.legend(frameon=False, loc="upper center", fontsize=9.5, ncol=2, bbox_to_anchor=(0.5, 1.14))
save(fig, "agreement.png")
print("done")
