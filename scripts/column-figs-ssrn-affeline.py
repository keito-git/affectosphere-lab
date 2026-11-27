"""Figures for the Affeline research-blog post. Every number is copied from the
SSRN manuscript (paper/Affeline_SSRN_20261031: Tables 3-5, Sections 4.2-4.6, 5.1,
and generated/tab_transfer.tex, the source of Figure 4); nothing is recomputed
except the simple per-task differences noted below."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

OUT = "/Users/ishitatakashishou/Sites/affectosphere-lab/public/column-images/ssrn-affeline/"
SRC = ("/private/tmp/claude-501/-Users-ishitatakashishou/62e336aa-c915-4181-a249-1463c108b1af/"
       "scratchpad/ssrn-affeline/")
AMBER, STEEL, GREY, LIGHT = "#C4974A", "#3D6B8C", "#9AA0A6", "#D9D4CB"
plt.rcParams.update({
    "font.family": "Arial", "font.size": 11, "axes.edgecolor": "#444",
    "axes.linewidth": 0.8, "axes.spines.top": False, "axes.spines.right": False,
    "xtick.color": "#333", "ytick.color": "#333", "axes.labelcolor": "#222",
    "savefig.dpi": 220, "savefig.bbox": "tight", "savefig.facecolor": "white",
})

def save(fig, name):
    fig.savefig(OUT + name)
    plt.close(fig)

# 0. Method figures: crops of the manuscript's own Figure 1 and Figure 2
#    (pages 5 and 6 rendered at 220 dpi with pdftoppm).
Image.open(SRC + "pg-05.png").crop((325, 160, 1350, 955)).save(OUT + "architecture.png")
Image.open(SRC + "pg-06.png").crop((205, 510, 1460, 925)).save(OUT + "late-read.png")

# 1. Per-task gain over same-capacity specialists (Table 3: Delta_k and 95% CI,
#    in each task's own direction, EmoBank MAE sign as reported).
t3 = [("FinancialPhraseBank", 1584, -.0007, -.0055, .0042),
      ("Stance (5 topics)", 2620, .0009, -.0139, .0157),
      ("SemEval-2025 Track A", 2768, .0013, -.0096, .0122),
      ("SemEval-2025 Track B", 2768, -.0197, -.0216, -.0177),
      ("Irony detection", 2862, .0450, .0077, .0824),
      ("ABSA Restaurant", 3061, .0176, .0021, .0330),
      ("TweetEval-Emotion", 3257, .0000, -.0026, .0026),
      ("EI-reg EN", 7102, -.0539, -.0664, -.0414),
      ("EmoBank VAD (MAE)", 8062, -.0053, -.0078, -.0027),
      ("MELD", 9989, -.0121, -.0213, -.0029),
      ("HateXplain", 15383, -.0122, -.0276, .0032),
      ("WRIME reader (ja)", 30000, -.0118, -.0160, -.0075),
      ("WRIME writer (ja)", 30000, .0073, .0002, .0143),
      ("GoEmotions", 43410, -.0121, -.0230, -.0012),
      ("EmpatheticDialogues", 76673, .0156, .0103, .0208)]
fig, ax = plt.subplots(figsize=(7.4, 5.6))
y = np.arange(len(t3))[::-1]
for yi, (lab, n, d, lo, hi) in zip(y, t3):
    c = AMBER if n <= 4000 else STEEL
    ax.plot([lo, hi], [yi, yi], color=c, lw=1.6)
    ax.plot(d, yi, "o", color=c, ms=7)
ax.axvline(0, color=GREY, ls="--", lw=1)
ax.axhline(7.5, color="#bbb", lw=.6)
ax.text(.092, 7.75, "low-resource (≤ 4,000 train)", color="#7B5E28", ha="right", fontsize=9.5)
ax.text(.092, 6.95, "high-resource", color=STEEL, ha="right", fontsize=9.5)
ax.set_yticks(y, [f"{a}  (n={n:,})" for a, n, *_ in t3])
ax.set_xlim(-.075, .095)
ax.set_xlabel("Δ_k = Affeline − same-capacity specialist (95% CI, 3 seeds; + = Affeline better)")
save(fig, "per-task-gain.png")

# 2. Resource groups (Section 4.2 text).
grp = [("Low-resource\n(7 tasks)", .0064, "wins 5 / 7", AMBER),
       ("Low-resource\nexcl. irony (6)", -.0001, "wins 4 / 6", "#D9B77A"),
       ("High-resource\n(8 tasks)", -.0106, "wins 2 / 8", STEEL)]
fig, ax = plt.subplots(figsize=(6.4, 3.3))
for i, (lab, v, w, c) in enumerate(grp):
    ax.bar(i, v, color=c, width=.55)
    ax.text(i, v + (.0007 if v >= 0 else -.0007), f"{v:+.4f}\n{w}",
            ha="center", va="bottom" if v >= 0 else "top", fontsize=10)
ax.axhline(0, color="#444", lw=.8)
ax.set_xticks(range(3), [g[0] for g in grp])
ax.set_ylim(-.016, .011)
ax.set_ylabel("Mean Δ_k vs. specialist")
ax.set_title("Mann–Whitney U: p = 0.1325 (all), p = 0.2453 (irony excluded)", fontsize=10, color="#555")
save(fig, "resource-groups.png")

# 3. Held-out transfer (generated/tab_transfer.tex = data of manuscript Figure 4).
fr = [1, 5, 10, 100]
tx = [("TweetEval-Emotion", "macro-F1 ↑", [.716, .779, .795, .809], [.233, .264, .310, .430], .830),
      ("EmoBank", "MAE ↓", [.447, .297, .264, .208], [.559, .446, .394, .290], .152),
      ("HateXplain", "macro-F1 ↑", [.564, .586, .596, .656], [.367, .427, .436, .510], .694)]
fig, axs = plt.subplots(1, 3, figsize=(10, 3.3))
for ax, (name, met, a, b, sp) in zip(axs, tx):
    ax.plot(fr, a, "-o", color=AMBER, lw=1.8, label="Affeline repr. (frozen)")
    ax.plot(fr, b, "--s", color=GREY, lw=1.5, label="Qwen3-8B-Base repr.")
    ax.axhline(sp, color=STEEL, ls=":", lw=1.2, label="Same-capacity specialist (8B)")
    ax.set_xscale("log"); ax.set_xticks(fr, ["1%", "5%", "10%", "100%"])
    ax.minorticks_off()
    ax.set_title(name, fontsize=11); ax.set_ylabel(met)
    ax.set_xlabel("Held-out labels used")
fig.tight_layout()
h, l = axs[0].get_legend_handles_labels()
fig.legend(h, l, frameon=False, ncol=3, loc="lower center", bbox_to_anchor=(.5, -.08))
save(fig, "transfer.png")

# 4. Late-Read vs early-channel (Table 4). Difference = Late-Read − Early-channel,
#    sign flipped for EmoBank (MAE, lower is better) so + means Late-Read better.
t4 = [("GoEmotions", .5403, .5234, 1), ("WRIME-r", .6840, .6856, 1), ("WRIME-w", .5388, .5412, 1),
      ("MELD", .6610, .6586, 1), ("TweetEmo", .8312, .8302, 1), ("EI-reg", .7948, .7689, 1),
      ("EmoBank (MAE)", .1497, .1572, -1), ("ABSA", .8991, .8982, 1), ("Irony", .8411, .8412, 1),
      ("HateXplain", .6891, .6817, 1), ("Empathetic", .3683, .3721, 1), ("Financial", .9749, .9854, 1),
      ("SemEval25-A", .7863, .7883, 1), ("SemEval25-B", .8141, .8108, 1), ("Stance", .7955, .7953, 1)]
d4 = [s * (l - e) for _, e, l, s in t4]
print("Late-Read ahead on", sum(v > 0 for v in d4), "tasks; mean diff", round(np.mean(d4), 4))
fig, ax = plt.subplots(figsize=(7.2, 4.6))
y = np.arange(len(t4))[::-1]
ax.barh(y, d4, color=[AMBER if v > 0 else LIGHT for v in d4], height=.62)
ax.axvline(0, color="#444", lw=.8)
ax.set_yticks(y, [t[0] for t in t4])
ax.set_xlabel("Late-Read − early-channel (task direction; + = Late-Read better)")
ax.set_title("Late-Read ahead on 6 / 15 tasks, mean difference −0.0030", fontsize=10, color="#555")
save(fig, "late-vs-early.png")

# 5. Error vs reader-writer disagreement on WRIME (Section 5.1 text).
fig, ax = plt.subplots(figsize=(6.2, 3.3))
x = np.arange(2); w = .36
low = [.1995, .3372]; high = [.2883, .6262]
ax.bar(x - w/2, low, w, color=LIGHT, label="least-disagreeing third")
ax.bar(x + w/2, high, w, color=AMBER, label="most-disagreeing third")
for xi, a, b in zip(x, low, high):
    ax.text(xi - w/2, a + .01, f"{a:.4f}", ha="center", fontsize=9.5)
    ax.text(xi + w/2, b + .01, f"{b:.4f}", ha="center", fontsize=9.5)
ax.set_xticks(x, ["WRIME reader\n(Spearman +0.307)", "WRIME writer\n(Spearman +0.621)"])
ax.set_ylabel("Mean per-sentence error")
ax.set_ylim(0, .72)
ax.legend(frameon=False, loc="upper left")
save(fig, "wrime-disagreement.png")
print("done")
