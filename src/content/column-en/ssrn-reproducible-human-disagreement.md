---
title: "How Much of Human Disagreement Can a Text Model Actually Predict?"
subtitle: "How Much Reproducible Human Disagreement Can Text Models Recover?"
date: "2026-11-27"
excerpt: "When a model that predicts annotator disagreement scores low, we cannot tell whether the model is weak or the reference disagreement simply does not repeat. We measure the reproducibility of disagreement directly with disjoint annotator groups and normalize prediction scores by it. A walk-through of our SSRN preprint."
readingMinutes: 12
showImage: false
image: "/column-images/ssrn-reproducible-human-disagreement/overview.png"
imageAlt: "Overview of the evaluation. A reproducibility curve is measured with disjoint annotator groups, model predictions are mapped to the disagreement of a group of the same size, and the agreement is normalized by the human reproducibility to give a recoverable share and an annotator-equivalent count."
authors:
  - name: "Keito Inoshita"
    url: "/en/about/"
    affiliation: "Kansai University"
tldr: "Models that predict annotator disagreement are scored against the disagreement of three to five annotators, a reference that changes when another group labels the same item. We measure the reproducibility of disagreement directly with disjoint annotator groups and divide the model–human agreement by it, giving a recoverable share. On five emotion, natural language inference (NLI) and safety datasets, fine-tuned encoders recovered only part of the reproducible disagreement (0.15 to 0.63 under matched conditions). A second dataset of the same task changed the share as much as a change of task did. The number of annotators a model is worth changed several-fold when only the vote format changed."
links:
  - label: "Preprint (SSRN)"
    url: "https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7685790"
  - label: "Code"
    url: "https://github.com/keito-git/reproducible-disagreement-recovery"
citation: |
  @misc{inoshita2026reproducibledisagreement,
    title        = {How Much Reproducible Human Disagreement Can Text Models Recover?},
    author       = {Inoshita, Keito},
    year         = {2026},
    howpublished = {SSRN preprint, abstract id 7685790}
  }
---

<div class="teaser">
<div>

Normalize

Score disagreement prediction against **human reproducibility**. A raw correlation of 0.30 is a share of 0.61 when reproducibility is 0.147, but 0.22 when it is 0.413.

</div>
<div>

Partial

Under matched conditions the recovered share is **0.63** for safety, **0.27** for emotion and **0.15** for NLI. A second dataset of the same task moves it as much as a change of task.

</div>
<div>

Protocol

The same emotion model is worth **1.25 annotators** with multi-label votes and **more than 5** with one-hot votes drawn from the same annotations.

</div>
</div>

## What is disagreement prediction compared against?

Annotators often disagree on subjective language tasks. In emotion recognition, natural language inference (NLI) and the safety rating of conversations, this disagreement is increasingly treated as information rather than error. Models are trained on vote distributions instead of majority labels, and shared tasks evaluate how well they reproduce the disagreement itself. All of this assumes that the disagreement on an item is, at least in part, a property of the item that can be predicted from its text.

It is still unclear how much of the observed disagreement is predictable from text at all. Item-level disagreement is usually measured with three to five annotators. When another group of three labels the same item, the disagreement changes. A model is therefore scored against a reference that is itself noisy. A low score can mean that the model misses information in the text, or that the reference does not repeat. Existing evaluations do not separate the two.

This study measures **how much of the disagreement that repeats across human annotator groups can be recovered from text**.

## How the evaluation works

<figure>
  <img src="/column-images/ssrn-reproducible-human-disagreement/overview-1600.webp" alt="Overview of the reliability-normalized evaluation framework" />
  <figcaption><strong>Figure 1.</strong> Overview of the evaluation (Figure 1 of the paper). On the human side, a reproducibility curve is measured with disjoint annotator groups. On the model side, predictions are mapped to the disagreement of a group of the same size. The two are compared against the same reference groups and normalized by the reproducibility.</figcaption>
</figure>

The disagreement D of a group is one minus the share of the most frequent class in its mean vote. The evaluation has five steps.

1. **Reproducibility curve.** For each item, the annotators are randomly permuted. The first n form group A and the next k form group B, so the two never share an annotator. The correlation across items between the disagreement of A and B is averaged over 200 partitions, giving a curve c(n, k). Its value at k = n is the reproducibility r<sub>nn</sub>. The curve is read only inside the measured range and never extrapolated with the Spearman–Brown formula, whose additive error model a non-linear measure such as D does not satisfy.
2. **Judgment model.** An encoder predicts the vote distribution from text alone. It is trained with soft-label cross-entropy against the mean vote of each training item (the distribution model).
3. **Finite-group mapping.** The naive score "1 − max probability" relates non-linearly to the disagreement of a small group. An item with two equally likely classes has 1 − max = 0.5, but three one-hot votes give D of either 0 or 1/3, with an expected value of 0.25. A mapping g (ridge or isotonic regression, whichever has the smaller cross-validated error) is therefore fitted on development items to the expected disagreement of n annotators, placing the model prediction E(x) on the human scale.
4. **Normalization.** The agreement m<sub>E</sub> between E and the disagreement of group A is computed against the same groups A as the human curve. The **recoverable share is R<sub>text</sub> = m<sub>E</sub><sup>2</sup> / r<sub>nn</sub>**, which has the form of the classical correction for attenuation. A value of 1 means all reproducible disagreement is recovered, and 0 means none of it.
5. **Annotator-equivalent count.** The count n\* is the size of a disjoint human group that agrees with A as well as the model does, read from the curve. It depends on the vote format, so it is a secondary measure.

The same quantities partition the variance of disagreement into three parts: a part that another group of n annotators does not reproduce (1 − r<sub>nn</sub>), a part the model predicts from text (m<sub>E</sub><sup>2</sup>), and a part that repeats but is not captured (r<sub>nn</sub> − m<sub>E</sub><sup>2</sup>). The reproducibility here is between random groups from the same annotator pool, not the variance of a latent true disagreement, so R<sub>text</sub> is a lower bound on what the text can carry.

## Experiment 1: Recoverable share on the three main datasets

<p class="experiment-label">Experiment 1</p>

<div class="setup">

**Setup**

- Data: BRIGHTER English (emotion), ChaosNLI (NLI), DICES-990 (safety); BRIGHTER German and DICES-350 as second datasets
- Group size: n = 3, a typical budget for subjective annotation
- Models: RoBERTa-large and its MNLI-fine-tuned checkpoint (English), XLM-RoBERTa-large (German); predictions averaged over 3 seeds
- Training conditions: Full (all training items and all votes; NLI starts from the MNLI checkpoint) and Matched (starts from RoBERTa-large, 7 votes per training item, at most 1,868 training items)
- Intervals: 95% percentile intervals from 500 item bootstrap samples

</div>

| Dataset | Task | Vote format | Items | Annotators per item | Split (train / dev / test) |
|---|---|---|---|---|---|
| BRIGHTER English | Emotion | Multi-label, 7 classes | 5,655 | 5–30 | 3,911 / 349 / 1,395 |
| BRIGHTER German | Emotion | Multi-label, 7 classes | 5,407 | 3–9 | 3,244 / 541 / 1,622 |
| ChaosNLI | NLI | One-hot, 3 classes | 3,113 | 100 | 1,868 / 311 / 934 |
| DICES-990 | Safety | One-hot, 3 classes | 990 | 69–76 | 5-fold cross-fitting |
| DICES-350 | Safety | One-hot, 3 classes | 350 | 123 | 5-fold cross-fitting |

<figure>
  <img src="/column-images/ssrn-reproducible-human-disagreement/main-share-1600.webp" alt="Recoverable share on the main datasets" />
  <figcaption><strong>Figure 2.</strong> Recoverable share R<sub>text</sub> on the three main datasets (n = 3, error bars are 95% intervals). Amber is the Matched condition and blue the Full condition. For DICES-990 the Full condition already starts from RoBERTa-large with fewer than 1,868 training items, so only the number of votes is matched.</figcaption>
</figure>

Under matched conditions, the share was 0.63 for safety, 0.27 for emotion and 0.15 for NLI. The differences exceed their uncertainty: safety is above emotion by 0.35 [0.28, 0.42] and above NLI by 0.47 [0.40, 0.54], and emotion is above NLI by 0.12 [0.06, 0.19]. For NLI, starting from the MNLI checkpoint raises the share from 0.15 to 0.35 (a difference of 0.20 [0.15, 0.26]). Task-aligned prior knowledge changes the share within one dataset.

Splitting the variance of disagreement into its three parts shows the overall picture.

<figure>
  <img src="/column-images/ssrn-reproducible-human-disagreement/partition-1600.webp" alt="Partition of the variance of three-annotator disagreement" />
  <figcaption><strong>Figure 3.</strong> Partition of the variance of three-annotator disagreement D<sub>3</sub>. Blue is predicted from text, amber repeats across groups but is not captured, and light grey does not repeat in another group of three. Blue plus amber equals r<sub>33</sub>, and the blue fraction of that span is R<sub>text</sub>. Bars are computed from r<sub>33</sub> and m<sub>E</sub> in the paper's table.</figcaption>
</figure>

The non-repeatable part was 59% for emotion, 82% for NLI and 85% for safety. Most of the disagreement of three annotators does not repeat in another three. The part that repeats but is not captured was 28–30% for emotion, 12–15% for NLI and 3–6% for safety. Safety has little reproducible disagreement, but the tested models capture most of it. Emotion has the most reproducible disagreement, but the models capture only about 27–32% of it.

## Experiment 2: A second dataset of the same task

<p class="experiment-label">Experiment 2</p>

To check whether the ordering in Experiment 1 is a property of the task, the same evaluation was run on a second dataset for safety and for emotion.

<figure>
  <img src="/column-images/ssrn-reproducible-human-disagreement/second-datasets-1600.webp" alt="Recoverable share on second datasets of the same task" />
  <figcaption><strong>Figure 4.</strong> Recoverable share on two datasets of the same task, with 95% intervals. Safety compares DICES-990 and DICES-350 (both with seven votes per training item); emotion compares BRIGHTER English and German (both with all training items and all votes).</figcaption>
</figure>

DICES-350 gave 0.17, far below the 0.63 of DICES-990. BRIGHTER German gave 0.53, above the 0.32 of English. As a result, the ordering of safety above emotion does not hold for the second datasets. DICES-350 is below German by 0.35 [0.22, 0.47], and its difference from matched English, −0.10 [−0.19, 0.01], is not clear.

**The spread within a task is as large as the spread between tasks.** Many factors differ between the two datasets of each task, however. DICES-350 has only 280 training items per fold and a lower r<sub>33</sub> of 0.107. German differs from English in language, encoder, label set and annotator pool. The German result does not come from items whose annotators are exhausted by the two groups: without the mapping, restricting the test items to those with at least seven or eight annotators gives 0.52 and 0.49, against 0.49 for all items. The remaining factors cannot be separated with the present data, so the share is reported for each task–dataset setting, including its annotation procedure.

## Experiment 3: Other training objectives and predictors

<p class="experiment-label">Experiment 3</p>

To test whether the low shares come from how the distribution model is trained, four other predictors were compared in the Matched condition.

<figure>
  <img src="/column-images/ssrn-reproducible-human-disagreement/controls-1600.webp" alt="Recoverable share of alternative predictors" />
  <figcaption><strong>Figure 5.</strong> Recoverable share by predictor in the Matched condition: surface features (length, punctuation and so on) with ridge regression, frozen Qwen2.5-7B-Instruct embeddings with ridge regression, a majority-label classifier, a model that regresses the expected three-annotator disagreement directly, and the distribution model (amber).</figcaption>
</figure>

Four results stand out.

- **Regressing disagreement directly gains little.** The gain over the distribution model is +0.05 in matched emotion and −0.02 in full emotion. The distribution model is equal or better for NLI and safety. With direct regression, emotion still exceeds NLI by 0.18 [0.12, 0.25].
- **Soft labels carry more than the uncertainty of a majority-label classifier.** The majority-label classifier recovers only 31–51% of the share of the distribution model on all three datasets.
- **Surface features recover almost nothing** (0.00–0.05).
- **Frozen embeddings of a 7B LLM do not exceed the fine-tuned encoders** (0.25 / 0.15 / 0.56).

## Experiment 4: Group size, training votes and seeds

<p class="experiment-label">Experiment 4</p>

If the share were an artifact of groups of three, it would change with the group size. Both r<sub>nn</sub> and m<sub>E</sub> were recomputed for n = 2, 3 and 4.

<figure>
  <img src="/column-images/ssrn-reproducible-human-disagreement/group-size-1600.webp" alt="Recoverable share across group sizes" />
  <figcaption><strong>Figure 6.</strong> Recoverable share R<sub>text</sub>(n) for group sizes n = 2 to 4. Solid lines are Full and dashed lines Matched (for DICES-990, only the votes are matched).</figcaption>
</figure>

Within each condition the share changes by at most 0.05, and the ordering of the conditions does not change.

The number of training votes matters for safety but hardly for emotion. For BRIGHTER English, m<sub>E</sub> is 0.341, 0.346 and 0.364 with one, three and all votes per training item. For DICES-990, reducing the training votes to seven lowers the share from 0.79 to 0.63. Seed variation is small: the standard deviation of R<sub>text</sub> across three single-seed models is at most 0.035, below the main differences between datasets (0.12 or larger).

## Experiment 5: Vote format and "how many annotators"

<p class="experiment-label">Experiment 5</p>

Recent work expresses LLM judges as a number of equivalent human annotators. We tested whether such counts are comparable across vote formats. Each multi-label vote of BRIGHTER English was replaced by one class drawn from that vote, making the emotion votes one-hot as in NLI and safety.

<figure>
  <img src="/column-images/ssrn-reproducible-human-disagreement/vote-format-1600.webp" alt="Effect of vote format on recoverable share and annotator-equivalent count" />
  <figcaption><strong>Figure 7.</strong> Changing only the vote format (all Matched). Left: recoverable share. Right: annotator-equivalent count n*(3). The one-hot emotion model lies above the measured curve (up to 5 annotators) and is shown as "&gt; 5". Error bars are 95% intervals.</figcaption>
</figure>

| Dataset | Vote format | Condition | n*(3) [95% interval] |
|---|---|---|---|
| BRIGHTER English | Multi-label | Full | 1.76 [1.19, 2.54] |
| BRIGHTER English | Multi-label | Matched | 1.25 [0, 1.91] |
| BRIGHTER English | One-hot redraw | Matched | > 5 in all samples |
| ChaosNLI | One-hot | Full, MNLI checkpoint | 6.15 [4.76, 7.21] |
| ChaosNLI | One-hot | Matched | 2.73 [2.19, 3.60] |
| DICES-990 | One-hot | Full | > 20 |
| DICES-990 | One-hot | Matched votes | 17.4 [14.3, > 20] |

With one-hot votes, the human reproducibility r<sub>33</sub> drops from 0.413 to 0.118, and the share of the matched model rises from 0.27 to 0.36 [0.27, 0.46]. Over 50 redraws the share has a mean of 0.35 and ranges from 0.28 to 0.40, a moderate shift.

The annotator-equivalent count moves much more. The same emotion model is worth 1.25 annotators with multi-label votes and more than five with one-hot votes. This holds in every bootstrap sample and in all 50 redraws. Because the matched NLI model is worth 2.73 annotators, **the ordering of emotion and NLI reverses with the vote format alone**.

The reason lies in the human curve. A single multi-label vote already expresses graded disagreement, so c(3,1) = 0.322. One-hot votes from small groups give only coarse values of D, so c(3,2) = 0.079. The lower the human curve, the more annotators the same model agreement is worth.

## What we found and what remains open

The study supports three points.

- Text models recover only **part** of the disagreement that repeats across annotator groups: 0.15 to 0.63 under matched conditions, with a remaining part that repeats but is not captured.
- The share depends on the **task–dataset setting** and on the prior knowledge of the model, not on the task alone. A statement such as "emotion disagreement is less predictable than safety disagreement" is not supported by these data.
- Annotator-equivalent counts are not a property of the model alone; they depend strongly on the **annotation protocol (vote format)**. They should be compared only within one format and protocol. Across protocols, the recoverable share is the safer summary.

In practice, disagreement prediction should be evaluated against the measured reproducibility of its reference. A raw correlation of 0.30 corresponds to a share of 0.61 when r<sub>33</sub> = 0.147, but only 0.22 when r<sub>33</sub> = 0.413. When labels produced by a judgment model replace or augment human annotation, they can carry only what the model recovers from text; for emotion in BRIGHTER English, 68–73% of the reproducible disagreement was not carried. Soft labels still carried more than a majority-label classifier, so when item-level disagreement is needed, training on vote distributions is preferable to training on majority labels.

There are four main limitations. Each task has at most two datasets, so the factors behind the spread within a task cannot be separated. The models are fine-tuned encoders and frozen embeddings of one 7B LLM, so R<sub>text</sub> describes the tested models and is a lower bound for text models in general. R<sub>text</sub> also changes with the vote format, though less than n\*, and its bootstrap intervals cover item sampling but not seed variation. Finally, the human reference is reproducibility between groups from one annotator pool, so disagreement shared by the whole pool but not by another population counts as reproducible.

Next steps are to compare several datasets per task that differ in one factor at a time (language, annotator pool, training size), to test generative and fine-tuned LLMs to raise the lower bound, and to examine whether the uncaptured part reflects knowledge current models lack or information outside the text, such as the background of annotators.

Code, data splits and derived results: [github.com/keito-git/reproducible-disagreement-recovery](https://github.com/keito-git/reproducible-disagreement-recovery).
