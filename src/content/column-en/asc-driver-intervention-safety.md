---
title: "How Should We Score an LLM's Warning to a Driver?"
subtitle: "Safety-Aware Evaluation of LLM-Generated Driver Intervention Messages through Multi-Task Risk Fusion"
date: "2026-11-27"
excerpt: "When an LLM turns in-cabin recognition results into a message for the driver, how do we judge the message? We propose DSAIS, a five-dimension score, and a risk fusion that does not dilute a single severe hazard. A walk-through of our Applied Soft Computing paper."
readingMinutes: 14
showImage: false
image: "/column-images/asc-driver-intervention-safety/architecture.png"
imageAlt: "Framework architecture: four-task recognition from in-cabin video, risk fusion, LLM message generation and DSAIS evaluation."
authors:
  - name: "Keito Inoshita"
    url: "/en/about/"
    affiliation: "Kansai University"
tldr: "We built a framework that recognises four things from in-vehicle cameras (traffic context, vehicle state, driver emotion and driver behaviour) and has an LLM turn them into an intervention message for the driver. Message quality is scored by DSAIS on five dimensions: risk-tone alignment, contextual relevance, conciseness, cognitive load and driver acceptability. We show that a weighted mean over the four tasks lets a single maximal hazard sink into LOW, and replace it with a Choquet integral with respect to a Sugeno λ-measure. Experiments show that emotion misrecognition disrupts the intervention most, and that BERTScore barely registers the disruption. No driver ratings were collected, so whether DSAIS matches how drivers perceive the messages is still open."
links:
  - label: "Paper (Applied Soft Computing)"
    url: "https://doi.org/10.1016/j.asoc.2026.116630"
  - label: "Data (AIDE)"
    url: "https://github.com/ydk122024/AIDE"
citation: |
  @article{inoshita2027dsais,
    title   = {Safety-Aware Evaluation of {LLM}-Generated Driver Intervention
               Messages through Multi-Task Risk Fusion},
    author  = {Inoshita, Keito},
    journal = {Applied Soft Computing},
    volume  = {204},
    pages   = {116630},
    year    = {2027},
    doi     = {10.1016/j.asoc.2026.116630}
  }
---

<div class="teaser">
<div>

Measure

DSAIS scores messages on **five dimensions** and separates deliberately degraded messages at Cohen's d = 1.87–8.26.

</div>
<div>

Fuse

Under a weighted mean, a driver on a handheld phone gets R = 0.295, **LOW**. Under the λ-measure, 0.384, MEDIUM.

</div>
<div>

Diagnose

Emotion misrecognition disrupts the message most for 5 of 6 methods. BERTScore varies by **0.080**; structural match by **0.404**.

</div>
</div>

## Beyond "Please focus on driving"

According to NHTSA, distracted driving was involved in about 3,021 fatal crashes and 3,275 deaths in 2023, roughly 8% of US traffic deaths. Drowsy driving appears in 1–2% of crashes in official statistics, but the AAA Foundation for Traffic Safety estimates that, allowing for underreporting, it was involved in 17.6% of fatal crashes in 2017–2021.

Driver monitoring can now recognise traffic context, vehicle state, driver emotion and driver behaviour at the same time. Yet the interventions are still beeps and fixed lines such as "Please focus on driving". A driver who is tired, on the phone and changing lanes in heavy traffic gets the same sentence.

LLMs could tailor the message to the state. Three things were missing, though.

1. **A way to measure quality.** BLEU, ROUGE and BERTScore measure similarity to a reference. They cannot tell whether the tone fits the urgency, whether the message is short enough to read while driving, or whether a stressed driver would accept it.
2. **A way to hand the recognition results to the LLM.** There was no framework for combining four tasks into one prompt.
3. **Knowledge of which recognition errors matter.** It was unknown which task's misclassification hurts the message most.

The paper states plainly that the parts are established (rule-based linguistic scoring, LLM judges, weighted risk combination) and claims no new algorithm among them. The contribution is the combination: **dimensions chosen for this domain, a fusion operator derived from a stated safety requirement, and the evidence needed to judge whether the score measures what it claims to**.

## The framework and DSAIS

<figure>
  <img src="/column-images/asc-driver-intervention-safety/architecture-1600.webp" alt="Framework architecture" />
  <figcaption><strong>Figure 1.</strong> The framework (Figure 1 of the paper). From left: four-task recognition, risk fusion, LLM generation and DSAIS evaluation.</figcaption>
</figure>

The framework has four modules.

1. **Four-task recognition.** The recognition model CauPsi outputs a label and a confidence for traffic context (TCR), vehicle state (VCR), driver emotion (DER) and driver behaviour (DBR). Any model that outputs labels and confidences can be swapped in.
2. **Risk fusion.** Each label has a risk score (e.g. anger 0.9, phone use 0.8, dozing off 1.0), multiplied by its confidence. The four contributions are fused into one risk R, split into LOW (below 0.3), MEDIUM and HIGH (0.6 and above). The module also keeps the last five frames and a session count of risky behaviour.
3. **LLM generation.** All of this goes into a structured prompt. The LLM returns, in JSON, a message of at most 15 words, a self-reported tone and a risk level.
4. **DSAIS evaluation.** The message is scored on five dimensions.

| Dimension | What it measures | How |
|---|---|---|
| S_risk | Risk-tone alignment | Judge tone classification plus a continuous distance |
| S_context | Relevance to the driver's state | GPT-5 judge, 1–5 scale |
| S_clarity | Conciseness | Rule (word count) |
| S_load | Cognitive load | Rule (information elements, spaCy) |
| S_accept | Driver acceptability | Rule and judge combined (β = 0.4) |

DSAIS is the mean of the five. To allow continuous monitoring in the vehicle, rules are used wherever possible and the judge only where needed. Each dimension corresponds to a property studied with human participants in human-factors research on in-vehicle messages.

### A requirement a weighted mean cannot meet

The original design added up the four task risks with weights (emotion 0.35, behaviour 0.25, traffic 0.20, vehicle 0.20). The paper states a requirement:

> **Requirement R1.** If one task is at maximum risk and the others are unremarkable, the driver must not be classified LOW.

A weighted mean meets R1 only if every weight is at least θ_L = 0.30. Four weights summing to one force the smallest to 0.25 or less, so **no weighted mean over four tasks can satisfy R1**. In practice, a driver operating a handheld phone, with the other three tasks unremarkable, had R = 0.295 and was classified LOW.

The fusion was therefore replaced by a Choquet integral with respect to a Sugeno λ-measure. The single-task masses are the original weights rescaled by the smallest factor that satisfies R1 (0.300, 0.300, 0.525, 0.375), and the rest follows from normalisation (λ = −0.722). **No new parameter is tuned.** The Shapley values, the average contribution of each task, keep the original order: emotion 0.367 > behaviour 0.247 > traffic and vehicle 0.193.

<figure>
  <img src="/column-images/asc-driver-intervention-safety/single-task-response-1600.webp" alt="Single-task response" />
  <figcaption><strong>Figure 2.</strong> Fused risk when only one task is at maximum risk, from the operator table of the paper. The weighted mean (grey) stays below the LOW boundary of 0.30 for three of the four tasks; the λ-measure (amber) reaches it for all four.</figcaption>
</figure>

## Experiment 1: Does DSAIS tell good messages from bad ones?

<p class="experiment-label">Experiment 1</p>

<div class="setup">

**Setup**

- Data: AIDE (3,062 driving clips, four camera views, four task labels). All 609 clips of the official test split
- Generators: Qwen2.5-7B / 14B, Llama-3.1-8B, Gemma-2-9B, GPT-5-mini, and a rule-based baseline that picks fixed templates
- Recognition model retrained under four seeds (mean four-task accuracy 81.20 ± 0.32%)
- Judges: GPT-5 (primary), Claude Sonnet 4, Qwen2.5-32B

</div>

We first built deliberately degraded messages and checked whether DSAIS separates them from high-quality ones (Gold): a gentle tone on a HIGH-risk clip (Mismatch-tone), messages far over the length limit (Overlong), bare commands (Imperative), and irrelevant sentences (Random).

<figure>
  <img src="/column-images/asc-driver-intervention-safety/control-1600.webp" alt="Control conditions" />
  <figcaption><strong>Figure 3.</strong> Cohen's d against Gold with 95% confidence intervals. For every condition the lower bound sits well above the pre-specified target of d ≥ 0.8.</figcaption>
</figure>

All conditions separate with large effects. Random is the smallest (d = 1.87) because irrelevant sentences do not lower conciseness or load; only the context dimension drops. Mismatch-tone matters most for safety, but the weighted mean places only 13 clips in HIGH. The λ-measure places 45 there, so the same manipulation can be tested on a larger sample (d = 8.26, 95% CI [7.10, 10.03]).

We also checked judge agreement.

| Dimension | Three-judge average, ICC(C,3) | Single judge, absolute, ICC(1,1) | ICC(1,1) without Qwen-32B |
|---|---|---|---|
| S_context | 0.817 | 0.531 | 0.769 |
| S_accept | 0.797 | 0.338 | 0.706 |

Averaged over three judges, agreement is high; a single judge's absolute agreement is lower. Removing the local Qwen-32B judge, however, raises it to 0.71–0.77. The shortfall comes from this particular judge, not from using one judge, so **one sufficiently capable judge is enough**. Removing the GPT-5 judge lowers agreement (0.338 → 0.180 for S_accept), so there is no evidence that the judge favours GPT-5-mini, its sibling.

## Experiment 2: Could a general-purpose LLM evaluator replace it?

<p class="experiment-label">Experiment 2</p>

All 3,654 ground-truth-condition messages were also scored with G-Eval, and each DSAIS dimension was correlated with it.

<figure>
  <img src="/column-images/asc-driver-intervention-safety/geval-1600.webp" alt="Correlation with G-Eval" />
  <figcaption><strong>Figure 4.</strong> Correlation of each DSAIS dimension with the G-Eval overall score. G-Eval largely recovers contextual relevance (blue) and does not recover risk-tone alignment, acceptability or cognitive load (amber).</figcaption>
</figure>

The result splits in two. **G-Eval largely recovers contextual relevance** (r = 0.755), and the paper concedes that this dimension is not new. Risk-tone alignment (−0.173), acceptability (−0.176) and cognitive load (0.049) are not recovered. G-Eval rewards fluent, elaborate messages, and elaboration is a burden for a driver reading at speed. GPT-5-mini gets the highest G-Eval score of any method and ranks last on DSAIS.

In place of driver ratings, the paper also runs metamorphic tests: rewriting a suggestion as a command should lower acceptability, adding empty filler should lower conciseness, and reformatting whitespace or the final full stop should not move the score. Of six relations, four hold, two move the right way but too little ("weak"), and none moves the wrong way. Re-judging the same message moves the composite by 0.050 on average, which is the resolution limit of a single-judge comparison.

## Experiment 3: Do real recognition outputs ever reach HIGH?

<p class="experiment-label">Experiment 3</p>

We counted the risk levels when the inputs are the recognition model's predictions rather than ground-truth labels.

| Fusion | Input | LOW | MEDIUM | HIGH |
|---|---|---|---|---|
| Weighted mean | Ground truth | 383 | 213 | 13 |
| Weighted mean | Prediction (4 seeds) | 531.0 ± 7.4 | 78.0 ± 7.4 | 0.0 ± 0.0 |
| λ-measure | Ground truth | 273 | 291 | 45 |
| λ-measure | Prediction (4 seeds) | 458.8 ± 9.8 | 144.3 ± 5.6 | 6.0 ± 4.3 |

With the weighted mean, **no clip reaches HIGH** under predicted inputs (the maximum is 0.545). The cause is arithmetic. The thresholds were set on the ground-truth scale, where every confidence is 1. Predicted confidences average 0.596–0.785, so every contribution shrinks by about a third. The λ-measure recovers a HIGH band in three of four seeds, but modestly and without guarantee. The paper gives a rate-matched recalibration (θ_H = 0.427 ± 0.007 under prediction) and uses it for the prediction-condition results that follow.

Sixteen synthetic driver trajectories with predictions fixed in advance tested the fusion further. The phone case reaches 0.295 (LOW) under the weighted mean and 0.384 (MEDIUM) under the λ-measure. A control in which all tasks are moderately elevated was predicted to stay LOW, and neither operator met that prediction. The paper reports this failure as is.

## Experiment 4: Which generator is best?

<p class="experiment-label">Experiment 4</p>

<figure>
  <img src="/column-images/asc-driver-intervention-safety/comparison-1600.webp" alt="Sub-score profile per method" />
  <figcaption><strong>Figure 5.</strong> DSAIS and the five dimensions for each method (ground-truth condition, weighted-mean fusion, 609 clips). Darker means higher.</figcaption>
</figure>

On the composite, the rule-based templates score highest (0.833). Short fixed templates get perfect conciseness and load, and the paper notes that this does not reflect capability as an intervention system. Among LLMs, Gemma-2-9B has the highest composite (0.807), and Qwen2.5-7B the smallest standard deviation (0.056).

GPT-5-mini is last on the composite (0.663) but first of six on acceptability (0.764) and risk-tone alignment (0.748). Its messages average 12.8 words and lose heavily on conciseness. **Read from the composite alone, the API model looks unsuitable; the dimensions do not support that conclusion.**

Splitting contextual relevance by risk level changes the picture again.

<figure>
  <img src="/column-images/asc-driver-intervention-safety/stratum-1600.webp" alt="Contextual relevance by risk level" />
  <figcaption><strong>Figure 6.</strong> Contextual relevance by risk level (ground-truth inputs). Templates are strong on LOW clips and fall far behind on MEDIUM.</figcaption>
</figure>

When there is no hazard, a fixed reassurance such as "You are driving smoothly" is a correct response, and a bespoke message can only add irrelevance. When there is a hazard, a template cannot name it. Qwen2.5-7B leads the templates by 0.21–0.30 on MEDIUM clips and trails by 0.01–0.24 on LOW clips. LOW clips are 63% of the test split, so the average hides the difference.

The ablation shows the same pattern. For Qwen2.5-7B and Gemma-2-9B, the four-task context and session information help on MEDIUM and HIGH clips and cost on LOW. For Llama-3.1-8B and Qwen2.5-14B they cost everywhere. The paper withdraws its earlier claim that every component contributes.

## Experiment 5: Which recognition errors disrupt the message?

<p class="experiment-label">Experiment 5</p>

We corrupted one task at a time, two tasks at once, or used the real predictions, and compared the messages with those generated from ground truth. Besides BERTScore, we used the structural match rate (SMR): the share of clips whose tone and risk level both stay the same.

<figure>
  <img src="/column-images/asc-driver-intervention-safety/bertscore-vs-smr-1600.webp" alt="BERTScore vs structural match rate" />
  <figcaption><strong>Figure 7.</strong> All 36 cells (6 methods × 6 conditions). BERTScore stays in a narrow band while SMR moves widely, and emotion misrecognition (amber) sits at the bottom.</figcaption>
</figure>

**Emotion misrecognition disrupts the intervention most for five of six methods** (SMR 0.499–0.545); for Qwen2.5-7B, behaviour errors are slightly worse. Traffic or vehicle errors do not change the direction of an intervention, but reading weariness as anger turns a rest suggestion into an emotion-regulation prompt.

Across the 36 cells, BERTScore spans 0.080 and SMR spans 0.404, five times wider. Evaluated with BERTScore alone, emotion misrecognition would look like a one-point loss, and one would not see that it changes the intervention on half the clips. Under real predictions SMR is 0.601–0.726, so roughly three messages in ten reach the driver with tone or risk level altered. The paper reads this as graceful degradation, not as no effect. Changing the confidence distribution of the corrupted task in four ways does not change which conditions are most damaging.

## Experiment 6: Does it fit in a car?

<p class="experiment-label">Experiment 6</p>

We measured the generation stage alone on an H100 NVL (fp16, no quantisation). Recognition cost is not included.

| Model | Peak memory (GiB) | Latency per message (s) | p95 (s) |
|---|---|---|---|
| Qwen2.5-7B | 15.3 | 0.40 | 0.56 |
| Llama-3.1-8B | 16.3 | 0.52 | 0.73 |
| Gemma-2-9B | 20.3 | 1.01 | 1.11 |
| Qwen2.5-14B | 29.3 | 0.63 | 0.69 |

Every model produces a message in about a second or less, so latency does not separate them. Memory does: the 7B–9B models stay below 21 GiB, the 14B model needs 29.3 GiB. Gemma-2-9B is the slowest despite being smaller than the 14B model, so speed is not set by parameter count alone. The paper concludes that the in-vehicle constraint is memory, not speed.

## What we know and what we don't

The paper establishes four points.

- DSAIS separates deliberately degraded messages at d = 1.87–8.26, and one sufficiently capable judge reaches 0.71–0.77 agreement with another.
- A weighted mean over four tasks lets a single maximal hazard sink into LOW. A Choquet integral with respect to a Sugeno λ-measure fixes this without any new parameter.
- Emotion misrecognition disrupts the intervention most, and BERTScore barely registers it.
- The composite hides trade-offs between dimensions and differences between risk levels. Which method is better depends on how often the deployment context presents a hazard and which dimension matters.

The main limit is that **no drivers rated the messages**. Every judged component comes from an LLM and has not been compared with driver ratings. What is shown is reliability and construct validity; agreement with driver perception (criterion validity) is open and needs a rating study with licensed drivers on the same five dimensions.

There are other limits. AIDE consists of independent short clips, so the session components run on a synthetic ordering. HIGH clips number only 13–45, so conclusions about the most important regime rest on small samples. Conciseness and load sit near their ceiling for most methods, which limits the composite's resolution. The label risk scores are expert-assigned and need re-specification for other data. A vision-language model reading raw frames was not compared, and the paper lists that comparison as open.

Data: the AIDE dataset is available at [github.com/ydk122024/AIDE](https://github.com/ydk122024/AIDE).
