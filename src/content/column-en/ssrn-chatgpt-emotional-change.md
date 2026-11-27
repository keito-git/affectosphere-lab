---
title: "Did Emotions in AI Discussions Change After ChatGPT?"
subtitle: "Emotional Change in AI-Related Online Discussions After ChatGPT Is Directionally Stable but Not Robust to Analytic Choices"
date: "2026-11-27"
excerpt: "Did the emotions expressed in AI-related discussions on Hacker News change after ChatGPT was released? Adding analytic choices one at a time, we found that an increase in fear was stable in direction but not robust. A walk-through of our SSRN preprint."
readingMinutes: 13
showImage: false
image: "/column-images/ssrn-chatgpt-emotional-change/framework.png"
imageAlt: "MI-CITS framework. Hacker News stories are split into an AI group and a control group, monthly means are measured with three emotion instruments, and the claim is tested on a seven-step evidence ladder."
authors:
  - name: "Keito Inoshita"
    url: "/en/about/"
    affiliation: "Kansai University"
tldr: "After ChatGPT was released, the share of AI stories on Hacker News rose from 1.6% to 9.5%, a 5.8-fold increase. That change is beyond doubt. Whether fear increased in AI-related discussions, however, depended on analytic choices. Starting from the simplest design and adding a control group, multiple instruments, resampling, placebo dates, trend forms and control-group constructions one at a time, the increase in fear was positive in all 10 samplings but significant after Holm correction in only 3. The other instruments did not confirm it, and a flexible pre-release trend removed most of it. Because the protective steps also lose power, the change is unconfirmed, not shown to be absent."
links:
  - label: "Preprint (SSRN)"
    url: "https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7649299"
  - label: "Code"
    url: "https://github.com/keito-git/hnaffect"
citation: |
  @misc{inoshita2026chatgptemotion,
    title        = {Emotional Change in AI-Related Online Discussions After ChatGPT
                    Is Directionally Stable but Not Robust to Analytic Choices},
    author       = {Inoshita, Keito},
    howpublished = {SSRN preprint, abstract id 7649299},
    year         = {2026}
  }
---

<div class="teaser">
<div>

Attention

Attention to AI rose **5.8-fold**: AI stories went from 1.6% before the release to 9.5% after, at every step of the ladder.

</div>
<div>

Direction

The increase in fear was **positive in all 10 samplings**, but significant after Holm correction in only 3.

</div>
<div>

Robustness

A spline pre-trend moved it from **+0.98 pp to +0.17 pp** (p = 0.481). The other two instruments did not confirm it.

</div>
</div>

## Why before–after emotion comparisons are fragile

To study how society received a new technology, researchers often compare the emotions in social media posts before and after an event. The release of ChatGPT on November 30, 2022 has become a prime target of such studies.

These comparisons are fragile. An event changes which topics appear on a platform. The mood of the whole platform shifts at the same time. Emotion classifiers differ substantially in accuracy, and the posts analyzed are only one sample from a population. In volatile monthly series, p-values also change greatly with the assumed pre-event trend and with the choice of standard errors. When these factors act together, a change that is not robust can be reported as a significant result.

This study therefore uses the release of ChatGPT as a large natural case to measure **how much a before–after comparison of social media emotions depends on analytic choices**.

## MI-CITS: an evidence ladder built one step at a time

<figure>
  <img src="/column-images/ssrn-chatgpt-emotional-change/framework.png" alt="MI-CITS framework" />
  <figcaption><strong>Figure 1.</strong> Data collection, the MI-CITS framework and the generalization checks. Each rung of the evidence ladder adds exactly one source of variation.</figcaption>
</figure>

The design follows one principle. Instead of reporting a single estimate under a single set of choices, **the analysis starts from the simplest design and adds one source of variation at a time, so that the step at which a conclusion changes can be identified**. We call this staged design a multi-instrument comparative interrupted time-series (MI-CITS) framework.

| Step | What is added | Question |
|---|---|---|
| 1 | Interrupted time series on the AI group alone | The design most prior work uses; kept for comparison |
| 2 | Gap series against non-AI discussions | Does it survive removing platform-wide movements? |
| 3 | Instruments M1, M2, M3 | Is it a property of one classifier? |
| 4 | 10 resamplings and a bootstrap | Does it depend on which posts were sampled? |
| 5 | Placebo dates before the release | Do the fluctuations alone produce an estimate this large? |
| 6 | Seasonality, trend form, local windows | Does it depend on the assumed pre-release trend? |
| 7 | Topic-matched and synthetic controls | Does it depend on how the control group is built? |

<figure>
  <img src="/column-images/ssrn-chatgpt-emotional-change/cits-schematic.png" alt="Comparative interrupted time series schematic" />
  <figcaption><strong>Figure 2.</strong> Schematic of the comparative model (not real data). A platform-wide shift moves both groups, so it cancels in the gap series D<sub>t</sub>. β2 is the level change at the release and β3 the change in slope.</figcaption>
</figure>

The core model fits a segmented regression to the gap series D<sub>t</sub>, the monthly mean of the AI group minus that of the control group. If all of Hacker News became more fearful in 2023, both groups rise and D<sub>t</sub> does not move. A change in D<sub>t</sub> is therefore specific to AI-related discussions relative to the rest of the platform. Standard errors use the Newey–West HAC estimator with lag 4.

The primary hypothesis, recorded in advance, is a positive level change β2 in fear under M1, tested two-sided. A level change and a slope change are estimated for each of the seven M1 emotions, so the 14 tests form one family corrected with the Holm method. The sampling rules, the keywords, the primary hypothesis and the scope of multiple comparisons were recorded under version control before the comments were collected.

## Experimental setup

<div class="setup">

**Setup**

- Data: Hacker News search API, January 2015 to June 2026; stories with a score of at least 20 and at least 10 comments (327,781 stories)
- Grouping: a story is in the AI group if its title matches one of 18 AI-related keyword patterns; all others form the control group
- Sampling: up to 30 stories per month and group, and up to 40 comments of five or more words per story; 10 independent samplings
- Instruments: M1 = DistilRoBERTa classifier (primary), M2 = RoBERTa trained on GoEmotions (mapped to Ekman's six emotions plus neutral), M3 = NRC Emotion Lexicon; none retrained
- Reference annotation: human annotation was not available, so Qwen2.5-14B-Instruct and Llama-3.1-8B-Instruct, run locally at temperature 0, served as reference annotators; their judgments bound measurement error and are not treated as ground truth

</div>

| Item | Value |
|---|---|
| Period | 2015/01–2026/06 |
| Stories with score ≥ 20 | 413,998 |
| Population (≥ 10 comments) | 327,781 |
| AI stories in the population | 14,048 |
| AI share, before / after | 1.6% / 9.5% |
| Stories, sample 1 | 8,044 |
| Comments, sample 1, AI / control | 124,325 / 136,175 |
| Unique comments, ten samplings | 1,830,975 |

## Experiment 1: Attention and the primary estimates (Steps 1–2)

<p class="experiment-label">Experiment 1</p>

First, attention. The monthly share of AI stories rose 5.8-fold after the release of ChatGPT and peaked at 14.3%. Attention to AI changed beyond any doubt.

<figure>
  <img src="/column-images/ssrn-chatgpt-emotional-change/primary-estimates-1600.webp" alt="Single-series vs comparative level changes" />
  <figcaption><strong>Figure 3.</strong> Level change β2 of the seven emotions under M1 (sample 1). Grey is the single series of the AI group; blue and gold are the gap series against the control group. Labels give the Holm-corrected p-values of the comparative model.</figcaption>
</figure>

At Step 1, the single-series model found an increase in fear of +0.49 pp (p = 0.002), together with rising slopes for anger and disgust. None of the three survived in the comparative model. This shows concretely how a design without a control series confuses fluctuations common to Hacker News with a change specific to AI.

At Step 2, the comparative model gave the pre-specified primary result: a level change in fear of **+0.98 pp with a Holm-corrected p < 0.001**, a relative change of +32.4% from the pre-release mean of the AI group. The same increase appeared with topic words masked (+1.01 pp), with a keyword set that is stable over the whole period (+1.46 pp) and in a comment-level model (+0.96 pp). No other M1 level or slope change survived Holm correction.

Two features already qualify this result. About half of the jump came from a **change of −0.49 pp in the control group**, not from the AI group. Likewise, the comparative decrease in sadness (−0.43 pp, nominally significant but not after Holm correction) came almost entirely from an increase of +0.49 pp in the control group, while the AI group moved by only +0.06 pp.

## Experiment 2: Does it hold under other instruments? (Step 3)

<p class="experiment-label">Experiment 2</p>

Step 3 asks whether the primary result is a property of the community or of the classifier that measured it.

<figure>
  <img src="/column-images/ssrn-chatgpt-emotional-change/instruments-1600.webp" alt="Agreement of the three instruments" />
  <figcaption><strong>Figure 4.</strong> Level change in fear under the three instruments: the number of the 10 samplings with a positive estimate and with a nominally significant one, the standardized effect in sample 1, and agreement with the language-model reference (Spearman ρ, AUC).</figcaption>
</figure>

Against the language-model reference, the Spearman correlation was 0.27 for M1 and M2 and 0.19 for M3, so M3 was the weakest instrument. The two reference models agreed on fear with a weighted κ of 0.66, and the instruments correlated with each other at only 0.18 to 0.37. None of them is a precise measurement.

In sample 1, the standardized effects of M2 and M3 were +0.22 and +0.35, with confidence intervals including zero. Across the 10 samplings, M2 mostly had the same sign as M1 but was significant in only 2, the sign of M3 was split, and all three instruments agreed in sign in only 4. **The pre-specified criterion of sign agreement across instruments was not met.**

The reference annotators also bounded the error of the grouping. On titles where both reference models agreed, the AI group had a precision of 98% and the control group a contamination of 2.5%, but the population-weighted recall was only 64%. That recall rose from 49% in 2015–2018 to 68% in 2023–2026, so the AI group captures a changing share of AI discussions over time.

## Experiment 3: The particular sample and the particular date (Steps 4–5)

<p class="experiment-label">Experiment 3</p>

Steps 4 and 5 ask how much of the primary result comes from the particular sample of posts and the particular date of the release.

<figure>
  <img src="/column-images/ssrn-chatgpt-emotional-change/resampling-1600.webp" alt="Resampling results" />
  <figcaption><strong>Figure 5.</strong> Share of the 10 independent samplings and of the 1,000 two-stage cluster bootstrap replicates meeting each condition, for the level change in M1 fear. The direction is stable; the significance is not.</figcaption>
</figure>

Across the 10 independent samplings, β2 ranged from +0.35 pp to +0.98 pp with a median of +0.60 pp. It was **positive in all 10**, nominally significant in 8 and significant after Holm correction in only 3. The bootstrap agreed: the mean β2 was +0.61 pp with a 95% interval of −0.06 pp to +1.22 pp. The first sample, on which the primary result was based, gave the largest estimate of the ten, so an analysis based on it alone would have overstated the change.

At Step 5, each month from January 2017 to June 2021 served as a placebo intervention, to see how large an estimate the fluctuations of the series produce on their own. The share of placebo estimates at least as large in absolute value as the first-sample estimate was 0.093, or 0.111 with dates thinned to six-month intervals, so the estimate did not pass calibration at the 0.05 level. 24.1% of the placebo dates were themselves nominally significant. All 5 placebo estimates that exceeded it had the opposite sign, which indicates that the fluctuations are large in both directions rather than upward in particular.

## Experiment 4: Trend form and control-group construction (Steps 6–7)

<p class="experiment-label">Experiment 4</p>

Steps 6 and 7 ask how much of the estimate is produced by the assumed counterfactual, which enters through the pre-release trend and through the control group.

<figure>
  <img src="/column-images/ssrn-chatgpt-emotional-change/specification-1600.webp" alt="Specification and control-group variants" />
  <figcaption><strong>Figure 6.</strong> β2 of M1 fear (sample 1) under alternative specifications, control groups and subsets of the AI group. Gold is the primary specification; blue marks the specifications that absorb most of the pre-release drift, where the estimate nearly disappears.</figcaption>
</figure>

Seasonal terms, ARIMA errors and story weighting left the estimate almost unchanged. **The functional form of the pre-release trend** did not. A quadratic pre-trend roughly halved the estimate, and a restricted cubic spline reduced it to +0.17 pp (p = 0.481). Within local windows of ±12, 24 and 36 months it was −0.01, +0.66 and +0.29 pp. The estimate depended on how much of the pre-release drift entered the fit, and the specifications that absorb most of it (the spline and the ±12-month window) removed it.

At Step 7, the two alternative control groups disagreed. The topic-matched control of 3,905 pairs gave +0.45 pp with a placebo exceedance rate of 0.019: smaller than the primary estimate, but calibrated. Under the same control, however, M2 and M3 gave +0.23 and −0.43 standard deviations. The synthetic control ranked the AI group 16 of 21 units, so it did not depart unusually from its own pre-release behavior.

Restricting the AI group to comments whose emotion is directed at AI, or to comments that mention AI, gave larger estimates (+1.29 pp and +1.40 pp). For AI-mentioning comments, M1 was positive in all 10 samplings and nominally significant in 9. Even there, M2 and M3 were significant in only 2 and 0 samplings, the pooled estimate of +1.16 pp had a placebo exceedance rate of 0.093, and a spline pre-trend reduced it to +0.12 pp. Emotions aimed at other targets may dilute the signal, but the restricted claim still did not survive the full ladder.

## Experiment 5: Is the fragility specific to AI?

<p class="experiment-label">Experiment 5</p>

Finally, we asked whether the fragility above is specific to the AI topic or a property of the design itself.

The first check is a set of **pseudo-treated comparisons**. Each of 20 non-AI topic clusters, built from title embeddings, was treated as if it were the AI group, and the same model was fitted at the release date.

| Target | Pseudo-treatment rejection rate |
|---|---|
| Level changes, seven emotions | 7.1% |
| Slope changes, seven emotions | 16.4% |
| Level change of fear | 10.0% |

Level changes were close to the nominal 5%, but slope changes were "detected" in about one of six cases. Because these topics may also have changed for their own reasons in late 2022, the paper reports these as pseudo-treatment rejection rates rather than false-positive rates.

The second check is a **simulation**. For each condition, 2,000 pairs of series were generated from a local-level model with AR(1) noise fitted to the pre-release Hacker News series. The null hypothesis holds by construction, so every rejection is a false positive.

<figure>
  <img src="/column-images/ssrn-chatgpt-emotional-change/simulation-1600.webp" alt="Simulation false-positive rate and power" />
  <figcaption><strong>Figure 7.</strong> Rejection rates in the simulation. (a) False-positive rate with no true effect, at 0, 0.5 and 1 times the drift estimated from Hacker News. (b) Power with a true effect, at 1 times the drift.</figcaption>
</figure>

With the drift estimated from Hacker News, the false-positive rate was 30.6% for the single-series model and 31.7% for the comparative model. Placebo calibration, a local window and a spline pre-trend reduced it to 14.3%, 21.7% and 21.2%. Without drift the comparative model still reached 10.3%, about twice the nominal level. Placebo calibration was the only method that stayed below the nominal level without drift, at 3.7%.

The protection has a cost. For a true effect of 0.5 standard deviations, power was only 25.1% with placebo calibration, 37.0% with a spline pre-trend and 35.2% with a local window. **Failing at the later steps of the ladder is not evidence that no change occurred.**

## What we found, and what remains open

The study shows the following.

- Attention to AI on Hacker News rose 5.8-fold after the release of ChatGPT, and no step of the ladder changes that.
- The increase in fear in AI-related discussions was consistent in direction under M1, but it did not survive resampling, placebo calibration, the other two instruments or a flexible pre-release trend. About half of the jump came from the control group.
- The steps that changed the conclusion were resampling, placebo calibration and the functional form of the pre-release trend. Seasonal terms, ARIMA errors and story weighting changed almost nothing.
- The fragility is not specific to AI. Slope changes were rejected for about a sixth of pseudo-treated non-AI topics, and slow drift raised the false-positive rate of the comparative model well above the nominal level.

The results support neither a claim of increased fear nor a claim of no change: the change is unconfirmed rather than absent. From these results, the paper proposes a checklist for before–after comparisons of social media emotions: (1) use a comparison series and report the treated and control estimates separately; (2) measure the same emotion with instruments of different nature and report standardized effects; (3) repeat the sampling or bootstrap the two-stage sampling; (4) report placebo exceedance rates rather than nominal p-values alone; (5) report sensitivity to the pre-event trend, including flexible and local specifications.

There are limitations. Without human annotation, the instruments and the grouping were checked against two language models, which risks circularity, and their low agreement indicates large measurement uncertainty. The target is a single English-language technology community, so the results do not generalize to other platforms or languages. The title-based grouping missed a time-varying share of AI discussions, so the measured quantity is the emotion expressed in AI-related discussions, not the emotion directed at AI. No causal effect of the release is claimed, since other AI-specific events at the same time cannot be excluded. The analyses beyond the original plan were specified after the first results were known, although each was fixed in writing before being run.

Next, we plan to apply the framework to other platforms and languages, and to compare designs that model slow drift explicitly, such as state-space formulations of the counterfactual, with the evidence ladder in terms of both false-positive control and power.

The code and the aggregate monthly series are available at [github.com/keito-git/hnaffect](https://github.com/keito-git/hnaffect). This post describes a preprint that has not been peer-reviewed.
