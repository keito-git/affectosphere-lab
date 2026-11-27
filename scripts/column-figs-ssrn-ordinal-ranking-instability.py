"""Figures for the TILT (ordinal ranking instability) research-blog post.
Every number is copied from the SSRN preprint source
(~/Desktop/研究/論文/TILT_appraisal順序ベンチマーク/SSRN/source/main.tex); nothing is recomputed.
overview.png is the paper's own Fig. 1, copied as is."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

OUT = "/Users/ishitatakashishou/Sites/affectosphere-lab/public/column-images/ssrn-ordinal-ranking-instability/"
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

# 1. Appraisal binding vs unbound control (Table tab:ablation).
a = [0, .25, .5, .75, 1]
rows = [("Appraisal-bound (MON_ρ = 0.865)", [.168, .324, .603, .833, .972], AMBER, "-o"),
        ("Control, same screen (MON_ρ = 0.311)", [.296, .564, .482, .688, .832], STEEL, "-s"),
        ("Control, no screen (MON_ρ = 0.323)", [.393, .577, .495, .642, .768], GREY, "--^")]
fig, ax = plt.subplots(figsize=(7.2, 3.6))
for lab, v, c, st in rows:
    ax.plot(a, v, st, color=c, label=lab, lw=1.8, ms=6)
ax.annotate("non-monotone dip", (.5, .482), (.58, .30), fontsize=9.5, color="#333",
            arrowprops=dict(arrowstyle="-", color="#555", lw=.8))
ax.set_xticks(a, ["0", ".25", ".5", ".75", "1"])
ax.set_xlabel("ladder position α (share of cue slots set toward pole_b)")
ax.set_ylabel("panel mass on pole_b")
ax.set_ylim(0, 1.05)
ax.legend(frameon=False, loc="upper left", fontsize=9.5)
save(fig, "binding.png")

# 2. Twenty estimators: strict vs non-decreasing (Table tab:conv).
clf = {"RoBERTa-GoEmotions": (.941, .660, .660, 0), "DistilRoBERTa-7": (.922, .630, .630, 0),
       "BERT-GoEmotions": (.910, .652, .652, 0), "DistilRoBERTa-7c": (.868, .652, .652, 0),
       "BERTweet-emotion": (.832, .658, .658, 0), "BERT-emotion": (.826, .660, .660, 0),
       "DistilBERT-emotion": (.802, .623, .623, 0)}
lm = {"Seed-1.6-flash": (.927, .542, .936, .394), "Command-R7B": (.907, .581, .891, .310),
      "Nova-Micro": (.888, .514, .891, .377), "Nemotron-3-nano": (.886, .573, .909, .336),
      "Grok-4.3": (.886, .536, .925, .389), "Solar-Pro4": (.883, .581, .911, .330),
      "Kimi-K2.5": (.883, .515, .945, .430), "GPT-5.6-luna": (.880, .538, .927, .389),
      "Haiku-4.5": (.876, .562, .940, .378), "MiniMax-01": (.873, .547, .907, .360),
      "GLM-5.3-flash": (.860, .543, .917, .374), "Phi-4": (.793, .617, .897, .281)}
vader = (.691, .314, .826, .512)
fig, ax = plt.subplots(figsize=(7.2, 3.8))
for d, c in ((clf, STEEL), (lm, AMBER)):
    for v in d.values():
        ax.plot([0, 1], [v[1], v[2]], "-o", color=c, lw=1, ms=4, alpha=.8)
ax.plot([0, 1], [vader[1], vader[2]], "-o", color=GREY, lw=1.4, ms=5)
ax.text(1.04, .66, "7 full-resolution\nclassifiers (never tie)", color=STEEL, va="center", fontsize=9.5)
ax.text(1.04, .92, "12 polled\nlanguage models", color="#8A6A2F", va="center", fontsize=9.5)
ax.text(1.04, .826, "VADER lexicon", color="#555", va="center", fontsize=9.5)
ax.set_xticks([0, 1], ["Strict increase\n(tie = 0 points)", "Non-decreasing\n(tie = 1 point)"])
ax.set_xlim(-.15, 1.55)
ax.set_ylim(.28, 1.0)
ax.set_ylabel("MON satisfaction rate")
save(fig, "conventions.png")

# 3. Accuracy vs strict score (Table tab:conv, columns Accuracy and Strict).
fig, ax = plt.subplots(figsize=(7.2, 3.6))
ax.scatter([v[0] for v in clf.values()], [v[1] for v in clf.values()], s=40, color=STEEL,
           label="Full-resolution classifiers")
ax.scatter([v[0] for v in lm.values()], [v[1] for v in lm.values()], s=40, color=AMBER,
           label="Polled language models")
ax.scatter([vader[0]], [vader[1]], s=40, color=GREY, label="VADER")
ax.text(.70, .44, "Spearman vs accuracy: +0.02\nSpearman vs distinct values: +0.72",
        fontsize=9.5, color="#333")
ax.set_xlabel("Independent accuracy (GoEmotions test split)")
ax.set_ylabel("MON, strict increase")
ax.set_ylim(.28, .72)
ax.legend(frameon=False, loc="lower right", fontsize=9.5)
save(fig, "accuracy-vs-score.png")

# 4. Quantisation sweep (Table tab:quant).
B = ["2", "4", "8", "16", "32", "64", "∞"]
x = np.arange(7)
q = [("RoBERTa-GoEmotions", [.644, .476, .285, .170, .109, .067, 0], STEEL),
     ("BERT-GoEmotions", [.526, .379, .241, .158, .099, .065, 0], "#6E93AE"),
     ("BERTweet-emotion", [.542, .344, .188, .136, .079, .045, 0], "#A3BACB"),
     ("VADER", [.794, .674, .573, .545, .524, .516, .512], GREY)]
mean_d = [8.4, 8.2, 6.7, 3.1, 1.4, .8, 0]
fig, (a1, a2) = plt.subplots(1, 2, figsize=(7.6, 3.3))
for lab, v, c in q:
    a1.plot(x, v, "-o", color=c, label=lab, ms=4, lw=1.5)
a1.set_xticks(x, B); a1.set_xlabel("levels B"); a1.set_ylabel("tie rate T")
a1.legend(frameon=False, fontsize=8.5, loc="upper right")
a1.set_ylim(0, .95)
a2.bar(x, mean_d, color=AMBER, width=.6)
for xi, v in zip(x, mean_d):
    a2.text(xi, v + .2, f"{v:g}", ha="center", fontsize=9)
a2.set_xticks(x, B); a2.set_xlabel("levels B")
a2.set_ylabel("mean |Δ rank| (of 20)")
a2.set_ylim(0, 10)
fig.tight_layout(w_pad=2.5)
save(fig, "quantisation.png")

# 5. Same model, polled K times (Table tab:samemodel; 0.514 / 0.507 from Sec. same-model).
K = [1, 2, 4, 8, 16, 64]
strict = [.267, .358, .440, .506, .552, .609]
nondec = [.858, .806, .761, .725, .697, .667]
fig, ax = plt.subplots(figsize=(7.2, 3.6))
ax.plot(K, strict, "-o", color=AMBER, lw=1.8, label="Strict increase (polled)")
ax.plot(K, nondec, "-s", color=STEEL, lw=1.8, label="Non-decreasing (polled)")
ax.axhline(.648, color=AMBER, ls=":", lw=1.2)
ax.text(1, .635, "read exactly: 0.648", ha="left", va="top", fontsize=9.5, color="#7B5E28")
ax.axhline(.514, color=GREY, ls="--", lw=1)
ax.text(1, .522, "weakest polled language model (strict): 0.514", fontsize=9.5, color="#555")
ax.axvline(4, color="#BBB", lw=.8)
ax.annotate("panel budget K = 4\nstrict 0.440", (4, .440), (5.5, .33), fontsize=9.5,
            arrowprops=dict(arrowstyle="-", color="#555", lw=.8))
ax.set_xscale("log", base=2)
ax.set_xticks(K, [str(k) for k in K])
ax.set_xlabel("ballots K drawn from each classifier's own probability")
ax.set_ylabel("MON score (mean of 7 classifiers)")
ax.set_ylim(.2, .92)
ax.legend(frameon=False, loc="upper right", fontsize=9.5, bbox_to_anchor=(1, .93))
save(fig, "same-model.png")

# 6. Binomial measurement model vs observed tie rate (Table tab:binom).
Kb = [1, 2, 4, 8, 16]
fig, ax = plt.subplots(figsize=(7.2, 3.4))
for lab, obs, pred, lim, c in [("GPT-5.6-luna", [.510, .421, .389, .356, .338], [.484, .434, .396, .370, .353], .338, AMBER),
                               ("Haiku-4.5", [.445, .392, .378, .346, .329], [.449, .407, .374, .353, .340], .329, STEEL)]:
    ax.plot(Kb, obs, "o", color=c, ms=7, label=f"{lab}, observed")
    ax.plot(Kb, pred, "--", color=c, lw=1.4, label=f"{lab}, predicted (no fitting)")
    ax.axhline(lim, color=c, lw=.8, alpha=.5)
ax.text(1, .318, "limit K→∞: 0.338 / 0.329", ha="left", fontsize=9, color="#555")
ax.set_xscale("log", base=2)
ax.set_xticks(Kb, [str(k) for k in Kb])
ax.set_xlabel("sampling budget K")
ax.set_ylabel("tie rate T")
ax.set_ylim(.30, .54)
ax.set_xlim(.8, 20)
ax.legend(frameon=False, fontsize=9, loc="upper right")
save(fig, "binomial.png")
print("done")
