---
title: "Can an LLM Turn Down the Emotional Volume of News Without Changing the Facts?"
subtitle: "Multi-Agent Large Language Model Based Emotional Detoxification Through Personalized Intensity Control for Consumer Protection"
date: "2026-11-27"
excerpt: "We used an LLM to rewrite only the anger- and anxiety-inducing wording of news texts and checked whether the facts survive. Stimulus intensity fell by up to 19.3% with near-zero correlation to semantic preservation, but not in world news, where the facts themselves are high-stimulus. A walk-through of our IEEE ZINC 2026 paper."
readingMinutes: 10
showImage: false
image: "/column-images/zinc2026-emotional-detox/overview.png"
imageAlt: "MALLET overview. A real-time pipeline with an Emotion Analysis Agent and an Emotion Adjustment Agent, and weekly personalization with a Balance Monitoring Agent and a Personal Guide Agent."
authors:
  - name: "Keito Inoshita"
    url: "/en/about/"
    affiliation: "Kansai University"
tldr: "Sensational headlines expose readers to anger and anxiety and get in the way of calm decisions. MALLET uses four agents to measure the stimulus intensity of a news text, rewrite it into calmer wording while keeping the facts (two levels, BALANCED and COOL), give weekly advice on consumption bias, and recommend a presentation mode that suits the reader's sensitivity. On 800 AG News texts, the mean stimulus score fell by 13.1% (BALANCED) and 19.3% (COOL). The size of the reduction was almost uncorrelated with semantic preservation, so the two can be controlled independently. In the World category, where the facts themselves are high-stimulus, the score barely moved."
links:
  - label: "Paper (IEEE ZINC)"
    url: "https://doi.org/10.1109/zinc69910.2026.11655671"
citation: |
  @inproceedings{inoshita2026mallet,
    title     = {Multi-Agent Large Language Model Based Emotional Detoxification
                 Through Personalized Intensity Control for Consumer Protection},
    author    = {Inoshita, Keito},
    booktitle = {Proceedings of the IEEE ZINC},
    year      = {2026},
    month     = jun,
    doi       = {10.1109/zinc69910.2026.11655671}
  }
---

<div class="teaser">
<div>

Reduce

Mean stimulus score **0.482 (RAW) → 0.389 (COOL)**, −19.3%. The share of texts above the threshold falls from 0.446 to 0.330.

</div>
<div>

Preserve

SBERT similarity **0.846 / 0.827**; NLI contradiction 1.9% / 3.6%. Correlation with the size of the reduction: r ≈ −0.04.

</div>
<div>

Limit

**No effect on World news** (BALANCED −0.1%, COOL 2.2%). Words like "explosion" or "attack" are facts, not decoration.

</div>
</div>

## Intervening on how news is told, not on what it says

In the attention economy, sensational headlines and extreme rhetoric spread because they capture attention. Strong emotional stimulation raises anger and anxiety and makes calm judgment harder, including when consumers read the news.

Consumer-side countermeasures have mostly targeted **the information itself**, for example fake news detection. This study looks at the emotional side of the reader instead. The idea is to keep the facts and **lower only the stimulus intensity of the wording**, so that consumers can take in information calmly.

Text style transfer has mainly aimed to flip emotional polarity (positive ⇔ negative). Here the target is not polarity but **intensity**, and the question is whether it can be adjusted in graded steps.

## How MALLET works

<figure>
  <img src="/column-images/zinc2026-emotional-detox/overview-1600.webp" alt="MALLET overview" />
  <figcaption><strong>Figure 1.</strong> Overview of MALLET (the figure from the paper). The upper half is the per-text real-time pipeline; the lower half is weekly personalization.</figcaption>
</figure>

MALLET (Multi-Agent LLM-based Emotional deToxification) chains four agents.

1. **Emotion Analysis Agent.** A 6-emotion BERT classifier (anger, fear, sadness, joy, love, surprise) gives a probability distribution for each text. The **stimulus score S** (0 to 1) is the sum of anger, fear and surprise. **HIR** (High-Impact Rate) is the share of texts with S above 0.6, and **EBI** (Emotion Balance Index) measures how evenly the six emotions are spread. Flesch Reading Ease (FRE) is tracked in parallel.
2. **Emotion Adjustment Agent.** GPT-4.1-mini rewrites the text while keeping facts, proper nouns and numbers. **BALANCED** is one sentence with sensational words replaced by neutral ones. **COOL** adds one more sentence of background or definitions. Length stays within ±20% of the original, at temperature 0.2. Semantic preservation is checked with SBERT cosine similarity and an NLI contradiction rate.
3. **Balance Monitoring Agent.** It aggregates each consumer's weekly browsing (mean S, HIR, EBI, mean of each emotion) and passes the summary to an LLM, which writes concrete advice.
4. **Personal Guide Agent.** From a consumer's sensitivity profile, an LLM picks an initial presentation mode (RAW, BALANCED or COOL) and gives a one-sentence reason.

Separating analysis from adjustment lets each part be updated on its own. The two-level modes let the amount of reduction vary from reader to reader.

## Experiment 1: How much does the stimulus drop?

<p class="experiment-label">Experiment 1</p>

<div class="setup">

**Setup**

- Data: 800 English news texts from AG News, 200 from each of World, Sports, Business and Sci/Tech
- Conditions: RAW (original), BALANCED and COOL for the same texts (within-subject design)
- Metrics: stimulus score S, HIR (θ = 0.6), EBI, FRE
- Tests: two-tailed paired t-tests with Holm correction; effect size as Cohen's d

</div>

<figure>
  <img src="/column-images/zinc2026-emotional-detox/mode-metrics-1600.webp" alt="Primary metrics across presentation modes" />
  <figcaption><strong>Figure 2.</strong> Main metrics by presentation mode. Grey is the original (RAW), blue is BALANCED, gold is COOL.</figcaption>
</figure>

The originals had a mean stimulus score of 0.482 and an HIR of 0.446, so about 45% of them exceeded the 0.6 threshold. BALANCED reduced the mean score by 13.1% and HIR by 20.6%; COOL reduced them by 19.3% and 26.0%. COOL reduces more, which the paper attributes to the supplementary sentence raising the share of neutral wording. EBI rose from 0.316 to 0.338 and 0.346, so the emotional bias also eased.

Readability went down. FRE fell to 30.23 for BALANCED (−24.3%) and 34.54 for COOL (−13.5%). Under the one-sentence constraint BALANCED tends to choose more abstract words; the plain explanation in COOL's extra sentence partly offsets this.

<figure>
  <img src="/column-images/zinc2026-emotional-detox/effect-sizes-1600.webp" alt="Effect sizes of paired t-tests" />
  <figcaption><strong>Figure 3.</strong> Absolute effect sizes of the six comparisons, all with Holm-adjusted p &lt; 0.001. Dotted lines mark Cohen's "small" (0.2) and "medium" (0.5).</figcaption>
</figure>

All six comparisons were significant. The effect sizes for the stimulus reduction, however, were d = 0.210 (BALANCED) and d = 0.282 (COOL), which are **small** by Cohen's criteria. The readability drop for BALANCED was larger, a medium effect of d = 0.609.

## Experiment 2: Which news does it work on?

<p class="experiment-label">Experiment 2</p>

<figure>
  <img src="/column-images/zinc2026-emotional-detox/category-1600.webp" alt="Mean stimulus score by category" />
  <figcaption><strong>Figure 4.</strong> Mean stimulus score by category. Labels show the reduction by COOL. Only World barely changes.</figcaption>
</figure>

| Category | RAW | BALANCED | COOL | Reduction (BAL) | Reduction (COOL) |
|---|---|---|---|---|---|
| World | 0.659 | 0.660 | 0.645 | −0.1% | 2.2% |
| Sports | 0.393 | 0.312 | 0.260 | 20.6% | 33.8% |
| Business | 0.500 | 0.396 | 0.350 | 20.8% | 30.0% |
| Sci/Tech | 0.374 | 0.308 | 0.299 | 17.8% | 20.0% |

Sports, Business and Sci/Tech showed large reductions. World stayed almost flat and even rose slightly under BALANCED (−0.1%). World news covers conflicts and terrorism, where the events themselves are high-stimulus. Words such as "explosion" and "attack" are not sensational decoration but are needed to state the facts, so they cannot be neutralized at the lexical level. The paper suggests that such content needs a different intervention, such as staged information disclosure.

## Experiment 3: Which emotions went down?

<p class="experiment-label">Experiment 3</p>

The stimulus score compresses six probabilities into one number, so we also looked at each emotion.

The largest change was in **anger**, whose mean probability fell from 0.34 to 0.24 (about −29%). The LLM replaced sensational words such as "scorching" and "outrage" with neutral ones such as "recorded" and "reported". At the same time **joy** rose from 0.37 to 0.42 (BALANCED) and 0.45 (COOL). The paper attributes this to the softmax constraint: probability mass removed from anger is redistributed, and joy, whose features are closest to neutral wording in this classifier, receives the largest share.

Fear, sadness, love and surprise did not change much. The stability of fear is consistent with the lack of reduction in World news. The paper concludes that MALLET works mainly by selectively lowering anger, and that fear would need additional interventions.

## Experiment 4: Is the meaning preserved?

<p class="experiment-label">Experiment 4</p>

<figure>
  <img src="/column-images/zinc2026-emotional-detox/semantic-1600.webp" alt="NLI judgement distribution" />
  <figcaption><strong>Figure 5.</strong> NLI judgements with the original as premise and the rewrite as hypothesis. The mean SBERT cosine similarity is shown in brackets.</figcaption>
</figure>

SBERT similarity was 0.846 for BALANCED and 0.827 for COOL. In NLI, 95.1% of BALANCED pairs were judged as entailment. For COOL, 68.6% were neutral, because the supplementary sentence counts as information not in the original, not as a contradiction. Contradiction rates were 1.9% (BALANCED) and 3.6% (COOL).

The per-text correlation between the size of the reduction (S_RAW − S_mode) and SBERT similarity was r = −0.039 (BALANCED) and r = −0.046 (COOL). **Texts that were calmed down more did not lose more meaning.** Within this range, lowering the stimulus and keeping the meaning are not a trade-off and can be handled separately.

## Experiment 5: Weekly aggregation and advice

<p class="experiment-label">Experiment 5</p>

<div class="setup">

**Setup**

- No real browsing logs were available, so five pseudo-consumers were simulated by drawing 100 scored texts each without replacement
- The weekly summary (mean S, HIR, EBI, mean of each emotion) was passed as JSON to GPT-4.1-mini to generate advice (temperature 0.3)

</div>

<figure>
  <img src="/column-images/zinc2026-emotional-detox/consumers-1600.webp" alt="Weekly summary of pseudo-consumers" />
  <figcaption><strong>Figure 6.</strong> Weekly HIR and mean anger probability for the five pseudo-consumers. HIR ranges from 0.41 to 0.53, and anger is high for everyone (0.31 to 0.40).</figcaption>
</figure>

Anger is high across all consumers, which reflects the AG News data. Two examples show how the advice differs. Consumer 0 (HIR 0.53, above 0.5) was told to diversify away from conflict-driven news and to switch the display mode to COOL or BALANCED. Consumer 3 (joy-dominant at 0.404, HIR 0.44) was told to keep the current mode and only mix in more topics. Both pieces of advice contained a diagnosis of emotional bias, a concrete behavioral suggestion, and numerical justification.

## Experiment 6: Recommending a presentation mode

<p class="experiment-label">Experiment 6</p>

The Personal Guide Agent chose an initial mode for three personas with different sensitivity.

| Persona | Profile | Recommendation | Rationale (from the paper) |
|---|---|---|---|
| P1 | Sensitive to anxiety and anger, prone to doom-scrolling | COOL | Gentle, context-rich rewriting reduces anxiety and prevents being overwhelmed |
| P2 | Seeks both facts and emotional tone | BALANCED | Factual accuracy with a moderate tone suits a balanced consumer |
| P3 | Enjoys bold expressions but values accuracy | RAW | Keeps the boldness of the original while maintaining accuracy |

The recommendations were graded, COOL → BALANCED → RAW, in order of decreasing sensitivity. This matches the order of stimulus reduction in Experiment 1 (COOL 19.3% > BALANCED 13.1% > RAW 0%).

## What we found, and what we did not

What the study shows:

- LLM rewriting can lower the **intensity** of emotional stimulation in news in two graded steps (mean stimulus score −13.1% and −19.3%), although the effect sizes are small.
- The size of the reduction is almost uncorrelated with semantic preservation, so within this range the two are not a trade-off.
- The effect comes from removing sensational decoration. It does not work for World news, where the events themselves are high-stimulus. What went down was mainly anger; fear did not move.
- Turning weekly indicators into concrete advice, and recommending a mode that fits a reader's sensitivity, are feasible as system components.

There are clear limitations. Whether the stimulus went down is judged by an emotion classifier, so it still needs to be checked against human judgments. The readability drop in BALANCED (d = 0.609) calls for explicit readability constraints in the prompt. The Balance Monitoring Agent was evaluated on pseudo-consumers, and longitudinal tests with real browsing logs remain to be done. Only English texts were used; Japanese and other languages have not been tested.

Next steps are human evaluation, alternative interventions for inherently high-stimulus content, longitudinal evaluation on real consumer data, and multilingual support.
