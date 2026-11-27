---
title: "What Does Annotator Disagreement Reveal about How Emotions Move in Conversation?"
subtitle: "Bayesian Spectral Emotion Transition Discovery from Multi-Annotator Disagreement"
date: "2026-11-27"
excerpt: "Instead of collapsing conversational emotion labels by majority vote, we kept the full distribution of annotator votes and used it to study how emotions follow one another. Disgust and anger readily alternate, while joy and anger rarely follow each other, and this structure emerges without supervision. A walk-through of our IEEE ICDM 2026 paper."
readingMinutes: 12
showImage: false
image: "/column-images/icdm2026-bayesian-spectral-transition/pipeline.png"
imageAlt: "BSETD pipeline. Stage 1 builds a posterior over the emotion-transition matrix from multi-annotator soft labels; Stage 2 separates inertia from contagion with a graph-Laplacian spectral decomposition."
authors:
  - name: "Keito Inoshita"
    url: "/en/about/"
    affiliation: "Kansai University"
  - name: "Takato Ueno"
    affiliation: "Shiga University"
tldr: "In EmotionLines, annotators disagree on 72.6% of utterances and 14.3% receive no majority at all. BSETD keeps the vote distributions (soft labels), estimates the emotion-transition matrix in a Bayesian way, and attaches a credible interval and an FDR-controlled significance decision to each cell. A spectral decomposition of the graph then separates inertia (persistence within a speaker) from contagion (transfer across speakers). On EmotionLines, disgust→anger is the most over-represented transition (log2 lift +0.94) and joy→anger the most under-represented (−0.90). Across five data sources the recovered structure correlates at 0.79–0.98. The discovered edges are associations, not causal effects."
links:
  - label: "Paper (IEEE ICDM 2026, accepted)"
    url: "https://lab.affectosphere.group/en/news/20260816-icdm2026-bsetd/"
  - label: "Preprint (arXiv)"
    url: "https://arxiv.org/abs/2606.01906"
  - label: "Code"
    url: "https://github.com/keito-git/bayesian-spectral-emotion-transition-discovery"
citation: |
  @inproceedings{inoshita2026bsetd,
    title     = {Bayesian Spectral Emotion Transition Discovery from
                 Multi-Annotator Disagreement},
    author    = {Inoshita, Keito and Ueno, Takato},
    booktitle = {Proceedings of the IEEE International Conference on Data Mining (ICDM)},
    year      = {2026},
    note      = {Accepted, to appear}
  }
---

<div class="teaser">
<div>

Discover

**disgust ↔ anger** is over-represented (log2 lift +0.94 / +0.86); **joy ↔ anger** is under-represented (−0.90 / −0.89).

</div>
<div>

Separate

An emotion is more likely to persist within the same speaker than across speakers for **all seven emotions**. The largest gap is anger (+0.146).

</div>
<div>

Replicate

Across five sources, the transition structure correlates at **0.91–0.98** within English and **0.79–0.85** with Chinese M3ED.

</div>
</div>

## What majority voting throws away

Emotions change over the course of a conversation. A speaker who starts out neutral becomes joyful after encouragement, stays that way for a few turns, and is then surprised by unexpected news. The structure of these transitions, that is, which emotion tends to follow which, underlies applications from mental-health screening to dialogue systems.

Conversational emotion corpora, however, usually compress the judgments of several annotators into one label by majority vote. In EmotionLines, the five annotators disagree on 72.6% of utterances, and 14.3% receive no majority. These figures reflect genuine perceptual ambiguity rather than annotation error. Majority voting removes this uncertainty, and the removal cannot be undone.

Work on Emotion Recognition in Conversation (ERC) has focused on predicting the next emotion label. There, labels are prediction targets, not objects whose transition structure is to be understood. This study asks a different question: **can we discover the transition structure of emotions without supervision while keeping the vote distributions (soft labels)?**

## How BSETD works

<figure>
  <img src="/column-images/icdm2026-bayesian-spectral-transition/pipeline-1600.webp" alt="BSETD pipeline" />
  <figcaption><strong>Figure 1.</strong> Overview of BSETD (Figure 1 of the paper). Stage 1 builds the posterior over the transition matrix from soft labels and splits it into same-speaker (inertia) and cross-speaker (contagion) parts. Stage 2 applies a spectral decomposition to the symmetrized matrix and extracts low-frequency (inertia) and high-frequency (contagion) components.</figcaption>
</figure>

BSETD (Bayesian Spectral Emotion Transition Discovery) runs in two stages over the seven Ekman categories (neutral, joy, sadness, fear, anger, surprise, disgust).

1. **Stage 1: Bayesian posterior.** For each pair of adjacent utterances, the outer product of their soft labels is added to a 7×7 matrix of soft transition counts. With one-hot labels this reduces to ordinary transition counts. A Dirichlet–Multinomial model with a Dirichlet prior on each row gives the posterior in closed form, and the prior concentration is set by empirical Bayes. Each cell receives a 95% credible interval and a lift relative to the marginal distribution, and the 42 off-diagonal cells are tested with Benjamini–Hochberg FDR control. Counting same-speaker pairs and cross-speaker pairs separately gives an inertia matrix and a contagion matrix.
2. **Stage 2: Spectral decomposition.** The posterior-mean transition matrix is treated as a weighted graph, symmetrized, and its normalized graph Laplacian is eigendecomposed. The spectrum is split at the median eigenvalue. The diagonal of the low-frequency component gives an inertia index I_j, and the off-diagonal of the high-frequency component gives a contagion index C_j.

Two caveats apply. Symmetrization discards the difference between j→k and k→j in Stage 2, so direction is carried only by Stage 1 and the speaker-conditioned splits. And a discovered edge is **an association, not a causal effect**. In the example in Figure 1, joy about a concert is followed by sadness about the rain: an external event, not emotional transmission, produces that transition.

## Experiment 1: Which transitions are over- and under-represented?

<p class="experiment-label">Experiment 1</p>

<div class="setup">

**Setup**

- Data: EmotionLines (29,245 utterances, 2,000 dialogues, five annotators per utterance), with the vote distribution used as the soft label
- Measure: log2 lift (the log ratio of the transition probability to the marginal probability of the next emotion)
- Significance: BH-FDR (q = 0.10) over the 42 off-diagonal cells

</div>

<figure>
  <img src="/column-images/icdm2026-bayesian-spectral-transition/top-transitions-1600.webp" alt="Top-10 transitions by log2 lift" />
  <figcaption><strong>Figure 2.</strong> The ten transitions with the largest |log2 lift| on EmotionLines (Table I of the paper). Gold marks over-represented transitions; blue marks under-represented ones.</figcaption>
</figure>

There are 27,245 utterance pairs. With this much mass, every off-diagonal cell in the BH-FDR list rejects the independence null, so the paper ranks transitions by effect size (log2 lift) rather than by significance.

The most over-represented transitions are disgust→anger (+0.94) and anger→disgust (+0.86), adjacent petals on Plutchik's wheel. The most under-represented are joy→anger (−0.90) and anger→joy (−0.89). These two are not opposite on Plutchik's wheel, but they lie on opposite sides of the valence axis in Russell's circumplex. Both are high-arousal emotions, so arousal alone cannot explain the result. Without any distance supervision, signatures of two different affective spaces emerge from transition statistics alone.

fear→anger (+0.49) is also over-represented. The paper notes that this is consistent with appraisal accounts linking fear to later defensive or aggressive responses, while stating that BSETD estimates only a conditional association.

## Experiment 2: Does an emotion stay with the speaker or move to the partner?

<p class="experiment-label">Experiment 2</p>

Stage 1 was fit separately to same-speaker pairs (inertia) and cross-speaker pairs (contagion), and the self-loops, the probability that an emotion is followed by the same emotion, were compared.

<figure>
  <img src="/column-images/icdm2026-bayesian-spectral-transition/inertia-contagion-1600.webp" alt="Self-loop posterior means on inertia and contagion splits" />
  <figcaption><strong>Figure 3.</strong> Posterior means of the self-loops (Table II of the paper). Gold is the same-speaker split, blue is the cross-speaker split; the number on the right is the difference.</figcaption>
</figure>

For all seven emotions, persistence is higher within the same speaker. The gap is largest for anger (+0.146) and sadness (+0.116): these emotions tend to persist while the same person holds the floor and fade when the turn passes. The gap is smallest for joy (+0.022) and surprise (+0.039), whose probability of being taken up by a new speaker is about the same as that of persisting. This agrees with the high social transmissibility reported by Hatfield and colleagues.

The over-representation of disgust→anger and anger→disgust is also stronger within speakers (log2 lift +1.28 / +1.14) than across speakers (+0.72 / +0.66). The escalation from anger to contempt or disgust that Gottman identified as a predictor of relationship breakdown thus appears to deepen within the speaker rather than being driven by the partner. Conversely, fear→anger is the only inter-emotion pair whose cross-speaker lift exceeds its same-speaker lift.

## Experiment 3: Does the same structure appear in other corpora and languages?

<p class="experiment-label">Experiment 3</p>

<div class="setup">

**Setup**

- EmotionLines: votes from five real annotators (primary evaluation)
- MELD: 13,708 utterances; single labels turned into pseudo-soft labels by Dirichlet smoothing (concentration 3.0)
- DailyDialog: 102,979 utterances, used as one-hot labels
- DailyDialog-LLM: the same utterances relabeled by GPT-5.4-mini, five independent samples at temperature 1.0
- M3ED: 23,893 utterances from Chinese TV dramas, three annotators each
- Comparison: Pearson correlation of posterior means over the 42 off-diagonal cells

</div>

<figure>
  <img src="/column-images/icdm2026-bayesian-spectral-transition/cross-corpus-1600.webp" alt="Cross-corpus correlations" />
  <figcaption><strong>Figure 4.</strong> Pearson correlations of the transition structure (42 off-diagonal cells) across the five sources (Table III of the paper).</figcaption>
</figure>

Within English sources the correlations are 0.91–0.98, and between Chinese M3ED and the three English corpora they are 0.79–0.85. Even between real-annotator EmotionLines and pseudo-soft MELD the correlation is 0.910 (95% CI [0.899, 0.917]), so which transitions are over-represented is preserved when the way soft labels are produced changes. The paper reads the lower cross-lingual values as leaving room for language- and culture-specific deviation.

The self-loops on the diagonal, by contrast, vary considerably. DailyDialog has the strongest neutral persistence, and M3ED shows the strongest persistence of negative emotions such as anger (0.65) and sadness (0.54).

On the same utterances, human hard labels and LLM virtual soft labels yield a correlation of 0.979, so the structure is nearly identical. Yet the LLM's five samples disagree on only 12.5% of utterances, an order of magnitude below the 72.6% for the real annotators. LLMs reproduce the structure of the modal label but strongly compress human uncertainty, and the paper does not read this agreement as a substitute for multiple human judgments.

## Experiment 4: Separating inertia and contagion spectrally

<p class="experiment-label">Experiment 4</p>

Stage 2 was applied to the EmotionLines posterior-mean matrix. The seven eigenvalues split at the median λ* ≈ 0.88 into four low-frequency and three high-frequency modes.

<figure>
  <img src="/column-images/icdm2026-bayesian-spectral-transition/results-overview-1600.webp" alt="BSETD results on EmotionLines" />
  <figcaption><strong>Figure 5.</strong> Results on EmotionLines (Figure 2 of the paper). (a) Heatmap of log2 lift (* marks BH-FDR-significant cells). (b) Low-frequency component; node size is the inertia index. (c) High-frequency component; line width is contagion strength.</figcaption>
</figure>

<figure>
  <img src="/column-images/icdm2026-bayesian-spectral-transition/spectral-indices-1600.webp" alt="Inertia and contagion indices" />
  <figcaption><strong>Figure 6.</strong> Inertia and contagion indices per emotion (Table IV of the paper). Bottom right: emotions that persist within a speaker; top left: emotions that move readily to the partner.</figcaption>
</figure>

| Emotion | Inertia index I_j | Contagion index C_j |
|---|---|---|
| neutral | 0.378 | 0.025 |
| joy | 0.338 | 0.011 |
| sadness | 0.227 | 0.010 |
| anger | 0.206 | 0.028 |
| surprise | 0.177 | 0.031 |
| fear | 0.162 | 0.046 |
| disgust | 0.123 | 0.052 |

Neutral and joy lead the inertia ranking (0.378 / 0.338), while disgust and fear lead the contagion ranking (0.052 / 0.046). The emotions that carry inertia are not those that behave contagiously. This is consistent with Hatfield's account of high-arousal negative emotions as readily transmitted across speakers, and with Kuppens' account of neutral and positive affect as persistent within a speaker. The separation was not assumed; it comes from a single operation, splitting the spectrum at the median.

The paper stresses that these correspondences are interpretive. The two bands are statistical constructs whose behavior is consistent with the notions of inertia and contagion; the agreement validates the recovered structure but does not identify the underlying mechanisms.

## Experiment 5: How robust are the results?

<p class="experiment-label">Experiment 5</p>

Robustness was checked along five aspects: uncertainty, null distribution, subpopulations, model choices and downstream prediction.

<figure>
  <img src="/column-images/icdm2026-bayesian-spectral-transition/robustness-1600.webp" alt="Robustness checks" />
  <figcaption><strong>Figure 7.</strong> (a) Correlation with the five-rater result when only R raters are kept. (b) Next-emotion macro-F1 when BSETD lift features are added to downstream predictors (Table VI of the paper). For logistic regression the paper reports only "no gain".</figcaption>
</figure>

| Check | Result |
|---|---|
| Dialog-level cluster bootstrap (lower bound of the 95% CI of the inertia−contagion difference) | joy +0.003, anger +0.112 (zero excluded for all seven emotions) |
| Within-dialog permutation test (B = 50) | p < 0.02 |
| Correlation across six subpopulations | 0.873–0.978 |
| Friends vs. EmotionPush | 0.962 |
| Hard-label substitution (mean absolute deviation of posterior means, top-disagreement decile) | 0.014 |
| Fixed prior α = 1 | lift ranking unchanged |
| Directed Laplacian (correlation of inertia / contagion indices) | 0.91 / 0.80 |

Keeping only two to four raters reproduces the five-rater result at 0.991–0.999. In the permutation test, the observed maximum |log2 lift| of 0.94 exceeds every permutation, so the structure does not arise from the marginal distribution alone.

Adding lift features to downstream predictors helps little: no gain for logistic regression, +0.015 for a two-stream GRU and +0.007 for a frozen DistilBERT. The contribution shrinks as the encoder grows stronger, so the paper positions BSETD as a discovery framework rather than a predictor.

The hard-label row in the table matters as well. Replacing the vote distributions with majority labels leaves the lift ranking unchanged and moves the posterior means by only 0.014. The paper states this openly and **does not claim that keeping disagreement changes which transitions are found**. What hard labels cannot provide is the posterior spread behind every credible interval and FDR decision, and coverage of the 14.3% of utterances with no majority without an arbitrary tie-break.

## What we found, and what remains open

The study shows three things.

- Emotion-transition structure in conversation can be discovered without supervision from annotator vote distributions. The Plutchik-adjacent pair disgust ↔ anger is over-represented, and the valence-reversed pair joy ↔ anger is under-represented.
- Persistence is higher within the same speaker for all seven emotions. The spectral decomposition separates emotions that carry inertia (neutral, joy) from those that behave contagiously (disgust, fear).
- The structure is stable across five data sources, two languages, reduced numbers of raters and subpopulation splits.

The paper also lists six limitations. Aggregation over the whole corpus mixes dialogues whose first and second halves follow different patterns. Symmetrization in Stage 2 discards direction. The outer-product formulation assumes conditional independence between adjacent labels. The estimator sees only the emotion labels of adjacent utterances, not topic, external events or speaker roles, so an edge may reflect a shared latent cause. Disagreement also carries semantic ambiguity, category overlap and annotator-specific bias, which the present design cannot separate. Finally, the evidence is associational and reproductive rather than mechanistic, and there is no quantitative comparison with the transition structure implied by trained neural ERC models.

Next steps include per-dialog hierarchical posteriors to expose within-dialog change, a fully directional spectral analysis, and tests of whether LLM virtual annotators can reproduce the shape of human uncertainty rather than only its mode.

The code, including scripts that reproduce every table and figure, is available at [github.com/keito-git/bayesian-spectral-emotion-transition-discovery](https://github.com/keito-git/bayesian-spectral-emotion-transition-discovery).
