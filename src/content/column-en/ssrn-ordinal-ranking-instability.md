---
title: "Does an Ordinal Emotion Benchmark Rank Systems by Accuracy or by Output Resolution?"
subtitle: "Output-Resolution-Driven Ranking Instability in Ordinal Emotion Benchmarks Based on a Tiered Invariance and Label-Order Testbed"
date: "2026-11-27"
excerpt: "We built TILT, an emotion benchmark whose ordinal ground truth is fixed by construction rather than annotation, and asked how far a ranking moves when only the value of a tie changes. The ranking reflected output resolution, not accuracy. A walk-through of our SSRN preprint."
readingMinutes: 13
showImage: false
image: "/column-images/ssrn-ordinal-ranking-instability/overview.png"
imageAlt: "The TILT construction. Four cue slots of a scenario are flipped one at a time to form a five-rung ladder; an LLM writes each item as a diary entry and a letter; judge models from other families measure the leaning toward pole_b."
authors:
  - name: "Keito Inoshita"
    url: "/en/about/"
    affiliation: "Kansai University"
tldr: "When systems are scored by how often they satisfy an ordinal constraint (more cues toward an emotion must not lower the leaning toward it), what a tie is worth is a free reporting choice. Writing that choice as one parameter λ makes the score S + λT, so a convention can move a score by exactly the tie rate T. On twenty estimators, 134 of 190 pairwise verdicts (R = 0.705) can be overturned by the convention alone. The score correlates +0.02 with independent accuracy and +0.72 with the number of distinct values an estimator can emit. Reading the same classifiers by four-ballot polling instead of exactly moves their score from 0.648 to 0.440, below every language model polled at the same budget."
links:
  - label: "Preprint (SSRN)"
    url: "https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7649298"
  - label: "Code / Data"
    url: "https://github.com/keito-git/tilt-benchmark"
citation: |
  @misc{inoshita2026tilt,
    title        = {Output-Resolution-Driven Ranking Instability in Ordinal Emotion
                    Benchmarks Based on a Tiered Invariance and Label-Order Testbed},
    author       = {Inoshita, Keito},
    year         = {2026},
    howpublished = {SSRN preprint, abstract id 7649298}
  }
---

<div class="teaser">
<div>

Convention

Changing only how ties are counted can overturn **134 of 190 pairwise verdicts (R = 0.705)**.

</div>
<div>

Resolution

The score correlates **+0.02** with independent accuracy and **+0.72** with the number of distinct output values.

</div>
<div>

Intervention

Polling the same classifiers four times instead of reading them exactly: **0.648 → 0.440**, below every polled language model.

</div>
</div>

## Turning an ordinal constraint into a score

Emotion labels disagree strongly across annotators. In GoEmotions, three or more annotators agreed on at least one label in 17,763 of 58,009 examples (31%). Methods that model this disagreement are growing, but the "true distribution" they try to recover is never observed, so verification falls back on proxies.

We therefore built a benchmark in which **the ground-truth relations are fixed by construction rather than by annotation**. What a construction can fix is not a label but a relation: this item should lean further toward anger than that one.

Scoring how often such a relation is satisfied requires one more decision: **what a tie between two outputs is worth**. Counting it as a failure, as a success, as half a point, or dropping it from the denominator are all defensible. We asked how far this choice can move a ranking, and what determines how many ties there are.

## How TILT is built

<figure>
  <img src="/column-images/ssrn-ordinal-ranking-instability/overview-1600.webp" alt="TILT construction" />
  <figcaption><strong>Figure 1.</strong> The TILT construction (Fig. 1 of the paper). The number of cue slots set toward pole_b defines a five-rung ladder. The corpus ships two relational constraints, MON and INV, not a distribution.</figcaption>
</figure>

TILT (Tiered Invariance and Label-Order Testbed) is built in four steps.

1. **Scenario**: one sentence fixes the situation (e.g. a running dispute with a neighbour), a pair of competing emotions (e.g. anger and sadness), and four **cue slots**. Each slot holds one fact pulling toward each emotion.
2. **Ladder**: the number of slots set toward pole_b is n_b = round(4α) for α ∈ {0, .25, .5, .75, 1}, giving five rungs.
3. **Generation**: an open-weight LLM writes two sentences that reflect the four selected facts without stating them and without naming an emotion. Each assignment is written as a diary entry and as a letter, and the whole grid is repeated three times.
4. **Judging**: four judge model families distinct from the generator (Qwen, Mistral, Gemma, DeepSeek) make a forced two-way choice, giving the leaning toward pole_b.

Only two relations are claimed as ground truth. **MON**: the leaning toward pole_b must be non-decreasing in the number of slots set toward it. **INV**: two items with identical cues that differ only in register must receive the same leaning.

For same-valence pairs (such as anger and fear), the four slots are bound to **appraisal dimensions**, the opposite poles of questions such as "who is responsible" and "can it still be undone". The released corpus has 37 scenarios and 1,021 items (511 diary, 510 letter), with 702 constraints. A manipulation check of whether each cue reached the text (cue fidelity) gives 0.834 overall; items at or below 0.5 are quarantined, and the 89 excluded items are released in a separate file.

The scoring conventions are placed on one axis. For estimator i, let S be the fraction of ordered pairs it strictly increases, T the fraction it ties, and V the fraction it inverts. If a tie is worth λ points (0 to 1), the score is

**M(λ) = S + λT**.

Three closed-form results follow: a convention can move a score by exactly T (Proposition 1); two estimators exchange places at λ* = (S_j − S_i) / (T_i − T_j), so the exchange is reachable by a defensible convention when 0 < λ* < 1 (Proposition 2); and the condition under which the benchmark contradicts an external accuracy axis (Proposition 3). The paper states that each is elementary and claims no mathematical novelty for them. The share of pairs that can be reversed is the convention-instability index R.

## Experiment 1: Does the construction do what it claims?

<p class="experiment-label">Experiment 1</p>

<div class="setup">

**Setup**

- Reference panel: four model families disjoint from the generator, 16,824 votes, option order counterbalanced
- Measure: MON_ρ, the mean within-ladder Spearman correlation between α and the leaning. The endpoints were the screening criterion, so the headline uses interpolated rungs only
- Control: cue slots unbound from appraisal dimensions (plain content opposites), on the same 15 scenarios with the same generator and judges

</div>

On the released corpus MON_ρ is 0.631 (95% CI [0.541, 0.714]). Including the endpoints raises it to 0.804, but the endpoints are the acceptance criterion itself, so that is not the headline.

<figure>
  <img src="/column-images/ssrn-ordinal-ranking-instability/binding-1600.webp" alt="Appraisal binding versus unbound control" />
  <figcaption><strong>Figure 2.</strong> Mean panel mass on pole_b at each rung for same-valence scenarios. Gold: slots bound to appraisal dimensions. Blue and grey: the unbound control, which falls from α = 0.25 to 0.5 and is not monotone.</figcaption>
</figure>

Removing the appraisal binding drops MON_ρ from 0.865 to 0.311, and the control stays low with the same screen or without it (0.323). According to the paper, without a named dimension the generator does not keep the two sides equally severe and writes the pole_b side as the milder situation. That is exactly the cue a valence-only signal can read, and exactly what the same-valence tier is meant to exclude.

Regenerating eight scenarios with a second generator family preserved order (MON_ρ 0.810 → 0.675) while invariance degraded (INV gap 0.136 → 0.223). Replicate counts differ, so the paper reports the direction rather than the magnitude.

## Experiment 2: How far can the tie convention move a ranking?

<p class="experiment-label">Experiment 2</p>

<div class="setup">

**Setup**

- Twenty estimators: 7 supervised classifiers (continuous scores), 12 zero-shot language models polled with a fixed ballot budget, and the valence-only lexicon VADER
- Independent accuracy: GoEmotions test split, same forced-choice protocol
- Conventions: tie = 0 (strict), tie = 1 (non-decreasing), tie = 0.5, ties excluded

</div>

<figure>
  <img src="/column-images/ssrn-ordinal-ranking-instability/conventions-1600.webp" alt="Twenty estimators under two tie conventions" />
  <figcaption><strong>Figure 3.</strong> The same predictions and constraints scored with tie = 0 and tie = 1. The classifiers never tie and do not move; the language models and the lexicon rise by their tie rate. The two groups swap order.</figcaption>
</figure>

The seven continuous classifiers never tie on this corpus, but they invert 34–38% of ordered pairs. The twelve polled language models tie on 28–43% and invert only 6–11%. Charging ties as failures therefore puts the classifiers on top, and charging them as successes puts the language models on top. **Which family a convention favours is fixed before any system is run.**

Computing λ* for all 190 pairs, 134 cross inside 0 < λ* < 1, so R = 0.705. Resampling ladders in scenario clusters gives a 95% interval of [0.605, 0.742]. 79 pairs have an interval for λ* wholly inside (0, 1), that is, they are reversible beyond resampling error, and 89 more are consistent with reversal without establishing it. For 159 of the 190 pairs, some defensible λ makes the benchmark contradict the external accuracy ordering. The identity between convention spread and tie rate (Proposition 1) holds for all twenty estimators to the rounding of the released numbers (10⁻⁶).

On the hard split (300 items built from scenarios that failed the screen), one set of predictions produces three different winners.

| Estimator | Strict | Non-dec. | Tie = 0.5 | Excl. | Tie rate |
|---|---|---|---|---|---|
| RoBERTa-GoEmotions | **0.628** | 0.628 | **0.628** | 0.628 | 0.000 |
| DistilRoBERTa-7 | 0.583 | 0.583 | 0.583 | 0.583 | 0.000 |
| GPT-5.6-luna | 0.244 | 0.911 | 0.578 | **0.733** | 0.667 |
| VADER | 0.000 | **1.000** | 0.500 | — | 1.000 |

VADER returns one value on every item of this split, so all of its pairs tie. It scores 0.000, 1.000, 0.500 or nothing, depending only on the convention.

## Experiment 3: What does the score track?

<p class="experiment-label">Experiment 3</p>

<figure>
  <img src="/column-images/ssrn-ordinal-ranking-instability/accuracy-vs-score-1600.webp" alt="Accuracy versus strict MON score" />
  <figcaption><strong>Figure 4.</strong> Independent accuracy against the strict MON score. Scores separate by group, that is, by output format, not by accuracy.</figcaption>
</figure>

No convention correlates with independent accuracy (Spearman +0.02 strict, +0.11 non-decreasing, +0.15 half credit, +0.17 ties excluded). The number of distinct values an estimator can emit correlates +0.72 under strict and −0.84 under non-decreasing, and the tie rate itself −0.74. Accuracy and resolution are nearly independent on this panel (+0.01).

A permutation null agrees (p = 0.93 against accuracy, p = 0.0004 against resolution). Dropping any one estimator keeps the resolution correlations in [+0.68, +0.82], while the accuracy ones straddle zero throughout. Splitting the accuracy axis into cross-valence and same-valence halves to match TILT's tiers gives +0.03 and −0.01.

The paper treats this as a **statement of scope**, not a defect. TILT measures compliance with relations that are true by construction; it is not offered as a proxy for accuracy on natural text. A sign reversal we had observed on an earlier five-estimator panel disappeared once the panel was widened, and the paper retires it as a caution about narrow panels.

## Experiment 4: What happens when scores are rounded?

<p class="experiment-label">Experiment 4</p>

To find where the tie rate comes from without touching any system, the predictions of the seven classifiers and VADER were rounded to B levels, Q_B(p) = round(Bp)/B, and re-scored with everything else fixed.

<figure>
  <img src="/column-images/ssrn-ordinal-ranking-instability/quantisation-1600.webp" alt="Quantisation sweep" />
  <figcaption><strong>Figure 5.</strong> Left: tie rate against the number of levels B. Right: mean displacement of the twenty-system ranking under strict increase. No prediction changes.</figcaption>
</figure>

Rounding to eight levels moves a system 6.7 places out of twenty on average and the most accurate system down seventeen places, while nothing any system predicts has changed. An equal-frequency quantiser with bin edges at each estimator's own quantiles gives the same direction and a larger displacement at the coarsest setting. What moves the ranking is the number of values a system can express, not the shape of the rounding.

## Experiment 5: The same model, measured two ways

<p class="experiment-label">Experiment 5</p>

Rounding coarsens a score from outside. The second intervention applies the panel's own protocol to the classifiers: instead of reading each classifier's probability exactly, draw K ballots from it and score the fraction. Model, corpus and constraints are identical; only the measurement changes.

<figure>
  <img src="/column-images/ssrn-ordinal-ranking-instability/same-model-1600.webp" alt="Same classifiers polled K times" />
  <figcaption><strong>Figure 6.</strong> The seven classifiers polled K times from their own probabilities (group means over 200 draws). At the panel's budget K = 4 the strict score falls below the weakest polled language model (0.514).</figcaption>
</figure>

At the panel's own budget of four ballots the classifiers' strict score falls from 0.648 to 0.440. Read exactly, the seven classifiers occupy 0.623–0.660 and sit above every polled language model. Polled at the same budget, the best of them reaches only 0.507, against 0.514 for the weakest language model, so **the two groups do not overlap and the panel inverts**.

The intervention runs only in this direction, not by reading the language models' token probabilities, because the serving interface used for this panel returns no log-probabilities for any of its models. The paper states that the symmetric test remains undone.

## Experiment 6: Do ties disappear with a larger polling budget?

<p class="experiment-label">Experiment 6</p>

A judge polled K times can return only K+1 distinct values, so part of the tie rate belongs to the evaluation. Reducing GPT-5.6-luna's budget from four ballots to one moves its satisfaction rate from 0.538 to 0.441 and its distinct values from five to two. Does a larger budget remove the problem?

<figure>
  <img src="/column-images/ssrn-ordinal-ranking-instability/binomial-1600.webp" alt="Binomial tie model versus observation" />
  <figcaption><strong>Figure 7.</strong> Tie rate against the polling budget K. Dots are observed, dashed lines are the binomial model's predictions with no fitting, and horizontal lines are its limit as K → ∞. The K = 16 column is used to estimate p and is not an independent test.</figcaption>
</figure>

If an item's pole probability is p, polling K times returns Binomial(K, p)/K, so the probability that two items tie has no free parameters. This prediction matches the observed tie rate over K ≤ 8 with mean absolute errors of 0.015 (GPT-5.6-luna) and 0.007 (Haiku-4.5). Its limit, the probability that two items carry the same pole probability, is 0.338 and 0.329. Quadrupling the budget from K = 4 to 16 lowers the tie rate only from 0.389 to 0.338 and from 0.378 to 0.329. **No budget drives the tie rate to zero for these systems**, so the convention keeps deciding the ranking whatever the evaluation costs.

The invariance constraint INV has the same structure with the opposite bias. Exact equality is unreachable for a continuous score, so a tolerance ε must be chosen.

| Tolerance ε | 0 | .05 | .10 | .25 | .50 |
|---|---|---|---|---|---|
| Continuous classifiers (7) | 0.002 | 0.321 | 0.455 | 0.679 | 0.859 |
| Polled language models (12) | 0.711 | 0.711 | 0.713 | 0.799 | 0.882 |
| VADER | 0.562 | 0.608 | 0.677 | 0.869 | 0.990 |

On 0 ≤ ε ≤ 0.5, 138 of 190 pairwise verdicts cross, a tolerance-instability of 0.726. Strict MON punishes coarse output; INV at ε = 0 rewards it. The paper therefore reports neither criterion alone and emits no composite of the two.

The same analysis on CHIARO, an independently released emotion benchmark, reproduced the convention dependence, the identity between spread and tie rate (for all nine of its estimators), and the dependence on polling budget. The aggregate reversal did not reproduce. CHIARO's accuracy axis is not negatively coupled with the tie rate, which is exactly where Proposition 3 says the reversal cannot appear.

## What we found and what remains open

The study establishes three points.

- A satisfaction rate over an ordinal constraint is not a property of the estimator alone. The tie convention can overturn 134 of 190 pairwise verdicts.
- Under a fixed convention the score tracks output resolution, not independent accuracy. This is shown by interventions that change only how one model is measured, not only by correlation.
- A larger polling budget does not remove the ties, so the reporting problem cannot be spent away.

The paper therefore recommends that ordinal benchmarks **report the convention, the tie rate that bounds its effect, and R, and compare systems of different output resolution only at a matched resolution**.

The paper lists five limitations. TILT certifies order and invariance, not human ambiguity (a separation criterion in the original design did not hold). The appraisal binding is used only in the same-valence tier, so the reverse control on cross-valence items is untested. Any aggregate reversal and the value of R depend on panel composition. The judges and all stimuli are model-based, so the relations have not been validated as human percepts, and the same-valence tier rests on only fifteen scenarios. The resolution intervention is one-directional; reading the language models continuously could not be done.

The corpus, constraints, scorer and analysis code are available at [github.com/keito-git/tilt-benchmark](https://github.com/keito-git/tilt-benchmark).
