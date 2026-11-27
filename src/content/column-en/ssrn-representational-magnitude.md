---
title: "Does a Larger Internal Representation Mean the Decision Depends on It More?"
subtitle: "Representational Magnitude Does Not Predict Decision Sensitivity in Large Language Models"
date: "2026-11-27"
excerpt: "We asked whether a dimension that is more prominent in an LLM's internal representation also matters more for its decisions. In seven model families, representational magnitude and per-unit causal sensitivity did not agree, and their ordering reversed with the decision being asked. A walk-through of our SSRN preprint."
readingMinutes: 12
showImage: false
image: "/column-images/ssrn-representational-magnitude/overview.png"
imageAlt: "Overview of the causal gain analysis framework in five steps: factorial prompts, state contrasts, vector construction, bidirectional intervention, and gain estimation."
authors:
  - name: "Keito Inoshita"
    url: "/en/about/"
    affiliation: "Kansai University"
tldr: "An emotional state carries two dimensions at once: its valence and the option it supports (the action dimension). In seven instruction-tuned LLM families, valence was 9 to 17 times larger than the action dimension in the representation, and it also had the larger raw effect on the choice. Per unit magnitude, however, the choice was more sensitive to the action dimension in every family. When the same vectors were read out by a question about feeling, this ordering reversed in all seven families. Representational magnitude does not predict decision sensitivity."
links:
  - label: "Preprint (SSRN)"
    url: "https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7685786"
citation: |
  @misc{inoshita2026magnitude,
    title        = {Representational Magnitude Does Not Predict Decision Sensitivity
                    in Large Language Models},
    author       = {Inoshita, Keito},
    year         = {2026},
    howpublished = {SSRN preprint, abstract id 7685786}
  }
---

<div class="teaser">
<div>

Magnitude

In the representation, **valence is 9.32–17.12 times larger** than the action dimension, and its raw effect on the choice is 3.24–9.20 times larger.

</div>
<div>

Gain

Per unit magnitude the order flips. Under the action question, **the action dimension has the higher gain in all seven families** (R_act = +0.83 to +1.88).

</div>
<div>

Decision

Read out by "how does the person feel?", the **same vectors reverse the ordering in all seven families** (R_val = −3.57 to −1.16).

</div>
</div>

## Is a more prominent dimension more important?

Interpretability research uses linear probes and representation engineering to describe which concepts an LLM encodes and how strongly. These descriptions often carry an implicit assumption: **a dimension that is more prominent in the representation is also more important for behavior**. Yet decodability does not show that a representation is used, and this assumption is rarely tested directly.

Emotion is a domain where the assumption can be tested precisely. In a social decision, one emotional state carries more than one piece of information. Being grateful for an option is a pleasant state, and it also indicates which option the person is likely to choose. **Valence and the supported option** are therefore two dimensions of the same internal state. The paper calls the second one the action dimension for brevity. Operationally it represents which of two options the state supports, not a generic action tendency.

Comparing such co-represented dimensions raises three challenges.

1. Most prior work asks whether a single variable is readable or causally effective. It does not compare the causal weight of several dimensions within one state.
2. The raw effect of a dimension mixes its size in the representation with the sensitivity of the output to it. A large dimension can have a large raw effect even if the output is not especially sensitive to it.
3. Testing whether the weighting is fixed by the representation or changes with the decision requires **reading out the same vectors under different decisions**. Extracting vectors separately for each decision would mix a change in the representation with a change in the readout.

## The causal gain analysis framework

<figure>
  <img src="/column-images/ssrn-representational-magnitude/overview-1600.webp" alt="Overview of the causal gain analysis framework" />
  <figcaption><strong>Figure 1.</strong> Overview of the framework (Figure 1 of the paper): (a) factorial prompts, (b) state contrasts, (c) vector construction, (d) intervention under two questions, and (e) gain estimation. The bars on the right are schematic.</figcaption>
</figure>

The starting point is a simple decomposition. To first order, the change in the output log-odds caused by a small added vector δ is the product of its magnitude ‖δ‖ and the sensitivity of the output to its direction. A raw effect mixes the two, so **dividing the effect by the magnitude isolates the directional sensitivity**. The paper calls this the causal gain G and defines the log gain ratio R_d = log G_A − log G_V. A positive R_d means the decision is more sensitive to the action dimension per unit magnitude; a negative R_d means it is more sensitive to valence.

The framework has five steps.

1. **Factorial prompts.** Short stories place two people in a setting with an active option (e.g., a swimming race) and a passive option (e.g., lying in a hammock in a shady grove). The target's emotional state crosses valence (pos, neg) with the supported option (act, stay) in four cells. Each prompt has a paired prompt in which the two state sentences are swapped between the people.
2. **State contrasts.** The difference between the paired prompts is taken at the question tokens of a selected layer ℓ*. The difference between the rows of the four cells is the valence contrast V, and the difference between the columns is the action contrast A. Their norms are the representational magnitudes.
3. **Vector construction.** The added vectors come either from the receiving model itself (own vectors) or from the other six families, mapped into the receiver's space by ridge regression and averaged (transferred vectors). Each cell vector is rescaled to a common norm.
4. **Bidirectional intervention.** The vectors are added and subtracted at the question tokens of ℓ*. The same vectors are read out under an **action question** ("Which will the target most likely choose?") and an **evaluation question** ("How does the target most likely feel right now?", Good / Bad).
5. **Gain estimation.** G_V, G_A and R_d are computed for each question. A local gain R∇_d is also computed from the output gradient; it does not depend on the size of the added vector.

<figure>
  <img src="/column-images/ssrn-representational-magnitude/factorial.png" alt="Factorial coding of the four cells" />
  <figcaption><strong>Figure 2.</strong> Factorial coding of the four cells and the two contrasts (Figure 2 of the paper). A positive state about an option is coded as supporting that option, and a negative state as supporting the other option. This is an experimental coding, not a psychological claim.</figcaption>
</figure>

The key design choice is that **the vectors are extracted once, under the action question, and the same vectors are used for both questions**. Because the added vectors and their norms are identical across the two questions, a change in R_d between them reflects how the model reads the same vectors, not a change in the representation.

## Experiment 1: Do magnitude and gain agree?

<p class="experiment-label">Experiment 1</p>

<div class="setup">

**Setup**

- Data: 96 English scenes (24 base scenes × 2 types × 2 option orders), 3,072 prompt pairs; the 1,536 active/passive pairs are used for the main analyses
- Models: seven instruction-tuned families (table below)
- Uncertainty: 95% bootstrap intervals from 1,000 resamples of the 24 base scenes per family
- Replication criterion: the interval excludes zero in the predicted direction in at least five of seven families, and the point estimate has the predicted sign in all seven (equivalent to a one-sided sign test with p = 0.0078)
- Unless stated otherwise, results are for the transferred vectors

</div>

| Model | Layers | ℓ* | Relative depth |
|---|---|---|---|
| Qwen2.5-7B-Instruct | 28 | 14 | 0.52 |
| Llama-3.1-8B-Instruct | 32 | 10 | 0.32 |
| gemma-2-9b-it | 42 | 18 | 0.44 |
| Mistral-7B-Instruct-v0.3 | 32 | 12 | 0.39 |
| OLMo-2-1124-7B-Instruct | 32 | 11 | 0.35 |
| granite-3.1-8b-instruct | 40 | 15 | 0.38 |
| Falcon3-7B-Instruct | 28 | 12 | 0.44 |

ℓ* is the layer at which patching an emotion contrast recovered the largest part of its effect on a separate stimulus set.

<figure>
  <img src="/column-images/ssrn-representational-magnitude/magnitude-vs-gain-1600.webp" alt="Magnitude, raw effect and gain under the action question" />
  <figcaption><strong>Figure 3.</strong> Ranges over the seven families under the action question: (a) magnitude ratio ‖V‖/‖A‖, (b) raw-effect ratio on the choice |k_V|/|k_A|, and (c) log gain ratio R_act. In (a) and (b), values above 1 mean valence is larger; in (c), values above 0 mean the action dimension has the higher gain.</figcaption>
</figure>

The valence contrast was larger than the action contrast in all seven families, with ‖V‖/‖A‖ from 9.32 to 17.12. The raw effects on the choice followed the same ordering, with |k_V|/|k_A| from 3.24 to 9.20. **Even though the question asks about the choice, valence moves the choice more.**

Per unit magnitude, the ordering reverses. G_A exceeded G_V in all seven families, R_act ranged from +0.83 to +1.88, and every interval's lower bound was above zero (replicated in 7/7). The action dimension is about one order of magnitude smaller in the representation, yet each unit of it changes the choice more than each unit of valence.

## Experiment 2: Does the ordering change with the question?

<p class="experiment-label">Experiment 2</p>

The same vectors were then read out under the evaluation question.

<figure>
  <img src="/column-images/ssrn-representational-magnitude/reversal-ranges-1600.webp" alt="Ranges of log gain ratios under the two questions" />
  <figcaption><strong>Figure 4.</strong> Ranges of the log gain ratio over the seven families under the two questions. From top: finite-intervention R (transferred vectors), gradient-based R∇ (transferred vectors), and gradient-based R∇ (own vectors). In every row, amber (action question) lies right of zero and blue (evaluation question) lies left of zero.</figcaption>
</figure>

R_val was negative in all seven families (−3.57 to −1.16), with every upper bound below zero. The difference R_act − R_val ranged from +2.37 to +4.40, with every lower bound above zero. Both the sign reversal and the difference were replicated in 7/7 families.

The added vectors and their norms are identical under the two questions. The magnitudes stay fixed, with valence 9 to 17 times larger, while the ordering of the gains reverses. This is therefore **a change in the readout**.

The reversal also appears in the local gradient, which does not depend on the size of the added vector. With transferred vectors, R∇_act ranged from +0.85 to +1.78 and R∇_val from −3.44 to −0.93. With the receiver's own vectors, the ranges were +0.38 to +1.52 and −2.75 to −1.21. Because the reversal appears with the own vectors, it is not produced by the cross-family map.

<figure>
  <img src="/column-images/ssrn-representational-magnitude/own-vectors-1600.webp" alt="Log gain ratios with each receiver's own vectors" />
  <figcaption><strong>Figure 5.</strong> R_act (amber) and R_val (blue) with each receiver's own vectors and 95% bootstrap intervals. In all seven families, the intervals sit on opposite sides of zero.</figcaption>
</figure>

The paper adds a caveat here. At the level of behavior, a question about feeling is expected to respond to valence. The nontrivial part is the combination of three observations: **the magnitudes stay fixed with valence much larger, the raw effect on the choice remains larger for valence, and yet the gain ordering reverses with the question in every family.**

## Experiment 3: Is it the answer words?

<p class="experiment-label">Experiment 3</p>

The answers "Good" and "Bad" are themselves valenced words, which might explain the negative R_val. The evaluation question was therefore rerun with two answer formats that carry no valence. In the symbol format, the letters Z and K are mapped to feeling good and feeling bad, with the mapping reversed across items. In the yes/no format, the question asks whether the target is in a good mood.

<figure>
  <img src="/column-images/ssrn-representational-magnitude/answer-formats-1600.webp" alt="R_val in two answer formats without valence words" />
  <figcaption><strong>Figure 6.</strong> R_val in two answer formats without valence words (transferred vectors, 95% intervals). All intervals lie left of zero.</figcaption>
</figure>

All upper bounds were below zero in both formats. The difference from the action question ranged from +2.42 to +5.28 (symbol) and from +2.22 to +4.32 (yes/no), with all lower bounds above zero.

Two earlier experiments with a separate stimulus set address the action side. When the answer letters were replaced by digits or by the action words themselves, the action readout stayed above zero in all seven families (ratio to the letter format: 0.61–0.96 for digits, 1.10–1.88 for action words). When the supported option was crossed with the order in which the objects appear in the story, the readout of the supported option exceeded that of object order in all seven families (ratio of the order term to the action term: 0.09–0.20). These controls argue against answer-label bias or object order as explanations.

## Experiment 4: Is it the overlap between the contrasts?

<p class="experiment-label">Experiment 4</p>

If V and A pointed in similar directions, the effect of one could leak into the other. In each receiver's own representation, the cosine between V and A ranged from 0.14 to 0.66. The added vectors, however, were nearly orthogonal, with per-prompt cosines of 0.02–0.09 for transferred vectors and 0.02–0.06 for own vectors. This is likely because the four cell vectors are rescaled to the same norm.

To control the remaining overlap, the per-direction effects were converted into partial coefficients and the log gain ratios were recomputed. This analysis was planned after the main results.

<figure>
  <img src="/column-images/ssrn-representational-magnitude/partial-ratios-1600.webp" alt="Partial log gain ratios after controlling contrast overlap" />
  <figcaption><strong>Figure 7.</strong> Partial log gain ratios after controlling the overlap (transferred vectors, 95% intervals). In all seven families, the action question stays positive and the evaluation question stays negative.</figcaption>
</figure>

All intervals stayed on the predicted side of zero in all seven families. The same pattern held for the local gradient, for the receiver's own vectors, and when one contrast was residualized on the other.

As a further check, control scenes were built in which both options are active and differ only in their object. If the action contrast were just a preference for active options, it should do nothing here. The receiver's own action contrast still shifted the choice toward the supported option in all seven families. The effect is small, 0.001 to 0.009 in log-odds, and the paper reports it as a descriptive check.

## Experiment 5: What happens at other layers?

<p class="experiment-label">Experiment 5</p>

The intervention was repeated at six relative depths from 0.15 to 0.90 and at ℓ*, using the receiver's own vectors.

<figure>
  <img src="/column-images/ssrn-representational-magnitude/layer-sweep-1600.webp" alt="Layer sweep of R_act minus R_val" />
  <figcaption><strong>Figure 8.</strong> R_act − R_val across depth (own vectors; band = 95% interval). The amber dot and dotted line mark the selected layer ℓ*. For Falcon3 at depth 0.59, the point estimate lies outside its interval; the value is unstable and is not interpreted (hollow marker).</figcaption>
</figure>

At ℓ*, the values reproduced the main experiment. However, **the build-up of the reversal toward this depth could not be confirmed**. When testing whether R_act − R_val is larger at ℓ* than at the shallowest layer, the point estimate was larger in all seven families, but the interval excluded zero in only two. At the shallowest layer both causal effects are close to zero, and the log ratio is poorly estimated.

The difference first exceeded zero with its interval between relative depths 0.16 and 0.44 in all seven families. Beyond ℓ*, the pattern was not uniform: it persisted in four families, weakened in two, and reversed with an interval below zero at one depth in one family. The paper's claims are therefore restricted to the readout at the selected intermediate site.

## Experiment 6: Do vectors from other families behave the same?

<p class="experiment-label">Experiment 6</p>

The main results above use vectors mapped from the other six families. How much of the natural effect do these mapped vectors carry? The transfer ratio divides the effect of the mapped vectors on the choice by the natural effect of the state sentence.

| Receiver | Transfer ratio (range over 6 senders) | R_act (own) | R_val (own) |
|---|---|---|---|
| Qwen2.5 | 0.08–0.11 | +1.35 | −1.49 |
| Llama-3.1 | 0.08–0.14 | +0.55 | −1.66 |
| Gemma-2 | 0.01–0.04 | +1.60 | −1.38 |
| Mistral | 0.05–0.10 | +1.08 | −2.81 |
| OLMo-2 | 0.10–0.18 | +0.73 | −2.25 |
| Granite-3.1 | 0.06–0.16 | +1.00 | −1.77 |
| Falcon3 | 0.01–0.03 | +0.36 | −2.36 |

Over the 42 sender–receiver pairs, the transfer ratio ranged from 0.01 to 0.18, so **most of the natural effect is not carried by the mapped direction**. The transferred effect is nevertheless specific to that direction. On a separate stimulus set, the mapped vectors gave transfer ratios of 0.019 to 0.147, while random directions of the same norm, drawn from the receiver's top 50 principal components, gave at most 0.009 in all 42 pairs.

Despite their small effect, the averaged transferred vectors reproduced the ordering of the own vectors (R_act positive, R_val negative) in all seven families. What is shared across families is **the relative ordering of the two gains, not the size of the effect**.

## What we found, and what remains open

Three findings stand out.

- **Representational magnitude does not predict decision sensitivity.** Valence was 9 to 17 times larger and had the larger raw effect on the choice, yet per unit magnitude the choice was more sensitive to the action dimension. A large steering effect may simply reflect a large magnitude, so the paper recommends reporting both the raw effect and the magnitude-normalized gain when comparing dimensions of different sizes.
- **Importance appeared as a relation between a representation and the decision that reads it, not as a property of the representation alone.** The same vectors, at the same layer and with the same norms, received opposite weightings under the two questions. The paper does not claim that the model judges task relevance and reweights the dimensions on purpose. It also agrees that different questions naturally imply different Jacobians; the point is that the representation alone does not fix which dimension a decision is more sensitive to.
- **Across families, the gain ordering was conserved, not the effect size.** The paper describes this as a conserved ordering of normalized causal sensitivity, not as a universal mechanism.

The paper also states its limitations.

- The claims concern the readout at the selected intermediate site, and the layer sweep did not confirm that the reversal builds up toward this depth.
- Magnitude was measured as the Euclidean norm of a factorial contrast; other measures such as decodability may rank the dimensions differently.
- Only two dimensions and one type of intervention, additive steering at the question tokens, were tested.
- The overlap control was planned after the main results, and the cross-family effect was small, so the transfer result supports the main finding but is not its primary evidence.
- The stimuli were short English stories with binary decisions, and the models were seven instruction-tuned models with 7 to 9 billion parameters.

Future work will examine a continuum of decisions rather than two, larger and base models, other pairs of co-represented dimensions, and interventions other than additive steering.

The manuscript states that the code will be released upon publication; no public URL is available yet. This post describes a preprint that has not been peer-reviewed.
