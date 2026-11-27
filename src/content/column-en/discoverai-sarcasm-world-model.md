---
title: "Can Sarcasm Be Read as a Prediction Error?"
subtitle: "World model inspired sarcasm reasoning with large language model agents"
date: "2026-11-27"
excerpt: "We treat sarcasm as a gap between what the words say and how the situation would normally be judged. WM-SAR splits this reasoning across LLM agents that output numbers, and leaves the final call to a logistic regression. A walk-through of our Discover Artificial Intelligence paper."
readingMinutes: 12
showImage: false
image: "/column-images/discoverai-sarcasm-world-model/framework.png"
imageAlt: "WM-SAR framework. Five agents for literal meaning, context, norms, inconsistency and intention output scalars that are combined by a logistic regression."
authors:
  - name: "Keito Inoshita"
    url: "/en/about/"
    affiliation: "Kansai University"
  - name: "Shinnosuke Mizuno"
    affiliation: "The University of Tokyo"
tldr: "Sarcasm shows up as a gap: the words praise, but the situation would normally be judged negatively. WM-SAR follows the world-model sequence of observation, latent state, prediction, prediction error and decision. Separate LLM agents produce the literal evaluation, a context hypothesis, the norm-based expectation, their difference and the speaker's intention, and only the final decision is made by a lightweight logistic regression. It beats all baselines on three benchmarks (average macro-F1 0.750), and removing the intention score causes by far the largest drop. It still misses sarcasm that looks like sincere praise on every signal."
links:
  - label: "Paper (Discover Artificial Intelligence)"
    url: "https://doi.org/10.1007/s44163-026-01360-7"
citation: |
  @article{inoshita2026wmsar,
    title   = {World model inspired sarcasm reasoning with large language model agents},
    author  = {Inoshita, Keito and Mizuno, Shinnosuke},
    journal = {Discover Artificial Intelligence},
    volume  = {6},
    number  = {606},
    year    = {2026},
    doi     = {10.1007/s44163-026-01360-7}
  }
---

<div class="teaser">
<div>

Decompose

The sarcasm decision is split into **five roles** (literal, context, norm, inconsistency, intention), each giving a number and a rationale.

</div>
<div>

Integrate

The final call is made by a **logistic regression**, not an LLM. Average macro-F1 over three datasets is 0.750, the best of all methods.

</div>
<div>

Diagnose

Removing the intention score drops average macro-F1 from **0.750 to 0.558**. A large gap alone does not make sarcasm.

</div>
</div>

## Where does sarcasm flip?

Sarcasm is an utterance that praises on the surface but criticizes in fact. In "Brilliant work breaking the server", the words are positive, but a crashed server would normally be judged negatively. Reading sarcasm therefore requires more than the literal meaning. We also need to infer how the situation should be evaluated by social norms and what the speaker intends.

Recent PLMs and LLMs detect sarcasm well, but the decision is usually left to a single model. It is then unclear which cues the model used, and when it fails, whether the failure came from meaning, context or intention.

In this work we treat sarcasm as **a mismatch between observation and prediction**. World models in computer vision follow the sequence observation → latent state → prediction → prediction error → decision. Sarcasm can be defined as a mismatch between the literal evaluation (observation) and the evaluation expected from the situation (prediction), so it fits this sequence directly.

## How WM-SAR works

<figure>
  <img src="/column-images/discoverai-sarcasm-world-model/framework-1600.webp" alt="WM-SAR framework" />
  <figcaption><strong>Figure 1.</strong> Framework of WM-SAR (figure from the paper). Each agent outputs a number and a natural-language rationale; a logistic regression combines them.</figcaption>
</figure>

WM-SAR (World-Model-inspired SArcasm Reasoning) splits the reasoning into five agents. All agents run on GPT-4.1-mini.

| World-model component | Module in WM-SAR | Output |
|---|---|---|
| Observation | Literal meaning agent | Literal evaluation M_literal ∈ [−1, 1] |
| Latent state inference | Context constructor agent | Context hypothesis C(u) (relationship, scene, preceding event) |
| State prediction | Norm and expectation reasoner | Expected evaluation in that situation, E_norm ∈ [−1, 1] |
| Prediction error | Inconsistency detector | D = M_literal − E_norm and sign disagreement SD ∈ {0, 1} |
| Decision | Intention reasoner + logistic regression | Sarcastic-intent score T_sar ∈ [0, 1] and final probability |

Two design choices matter.

1. **The prediction error is computed by subtraction, not by an LLM.** The literal and norm agents output values on the same [−1, 1] scale, and D is their deterministic difference. The sign test uses a neutral band of ±0.05.
2. **The final decision is made by logistic regression, not by an LLM.** Its inputs are |D|, T_sar and SD plus their combinations (D + T, T − D, D × T, √T, log(1 + T) and others). The regularization strength and the decision threshold are chosen by cross-validation on train + val.

A large D is only a candidate necessary condition for sarcasm. Exaggeration or humour can also produce it. For this reason the intention reasoner, which infers the speaker's intent through theory-of-mind reasoning, is kept as a separate path.

## Experiment 1: comparison with existing methods

<p class="experiment-label">Experiment 1</p>

<div class="setup">

**Setup**

- Data: IAC-V1 and IAC-V2 (online debate posts), SemEval-2018 Task 3 (English tweets); each split 8:1:1
- Metrics: Accuracy and macro-F1
- Baselines: MIARN, SAWS, DC-Net, fine-tuned BERT, zero-shot GPT-4.1-mini, the CoC / GoC / BoC prompting strategies, and the multi-agent method CAF-I
- Every LLM-based method uses GPT-4.1-mini (CAF-I was re-run with GPT-4.1-mini instead of its original GPT-4o)

</div>

<figure>
  <img src="/column-images/discoverai-sarcasm-world-model/main-results-1600.webp" alt="Main results" />
  <figcaption><strong>Figure 2.</strong> Macro-F1 on the three datasets and their average. Amber is WM-SAR, blue is zero-shot GPT-4.1-mini, dark grey is BERT.</figcaption>
</figure>

WM-SAR has the highest Accuracy and macro-F1 on all three datasets. Its average macro-F1 is 0.750, above GPT-4.1-mini alone (0.730) and BERT (0.713).

Notably, with the same GPT-4.1-mini, the reasoning prompts CoC, GoC and BoC score below plain zero-shot (average 0.698–0.722). Splitting the reasoning into roles, extracting numbers and combining them worked better than using the LLM output directly. The margins are not large everywhere, though: on IAC-V2 WM-SAR is only 0.001 above BERT.

## Experiment 2: which signals matter?

<p class="experiment-label">Experiment 2</p>

We removed the logistic-regression inputs one at a time.

<figure>
  <img src="/column-images/discoverai-sarcasm-world-model/ablation-1600.webp" alt="Ablation" />
  <figcaption><strong>Figure 3.</strong> Macro-F1 when a signal is removed: w/o D removes the gap strength |D|, w/o T the intention score, w/o S the sign disagreement, and w/o Interaction the combination features. Values are transcribed from the paper's figure.</figcaption>
</figure>

Removing the intention score (w/o T) causes by far the largest drop, from 0.750 to 0.558 on average. The gap between surface and norm is not enough to identify sarcasm.

Removing |D| gives 0.742 and removing the interaction features gives 0.738 on average: smaller but consistent drops. Removing SD slightly raises the score on SemEval-2018 (0.720 vs. 0.714), which suggests that |D| and T_sar carry most of the signal in short, informal tweets.

## Experiment 3: changing the LLM size

<p class="experiment-label">Experiment 3</p>

We replaced the LLM inside the agents with GPT-4.1, GPT-4.1-mini or GPT-4.1-nano, keeping everything else fixed.

<figure>
  <img src="/column-images/discoverai-sarcasm-world-model/backbone-1600.webp" alt="Backbone robustness" />
  <figcaption><strong>Figure 4.</strong> Macro-F1 of WM-SAR with different backbones.</figcaption>
</figure>

GPT-4.1 and GPT-4.1-mini average 0.751 and 0.750, almost the same. Per dataset, mini is higher on IAC-V1 and GPT-4.1 is higher on SemEval-2018. GPT-4.1-nano drops to 0.646 on average. We attribute this to weaker context construction and norm and intention reasoning, which lowers the quality of the numbers passed to the logistic regression. Once the backbone is reasonably capable, the framework works without the largest model, but we only tested this within the GPT-4.1 family.

## Experiment 4: inference time

<p class="experiment-label">Experiment 4</p>

<figure>
  <img src="/column-images/discoverai-sarcasm-world-model/cost-1600.webp" alt="Cost versus accuracy" />
  <figcaption><strong>Figure 5.</strong> Inference time per sample (log scale) against average macro-F1.</figcaption>
</figure>

Methods that call the LLM once or a few times take about one second per sample. WM-SAR uses several agents and takes 7.65 s on average, roughly one third of CAF-I (21.10 s), whose agents repeatedly consult each other. WM-SAR extracts the LLM outputs once as numbers and decides with a lightweight logistic regression. It is still heavier than the simple methods, so accuracy comes at a cost.

## Experiment 5: reading the decision

<p class="experiment-label">Experiment 5</p>

First we compared the intermediate signals between correctly and incorrectly classified test texts.

| Metric | Correct | Wrong |
|---|---|---|
| Mean T_sar | 0.417 | 0.394 |
| Mean \|D\| | 0.432 | 0.439 |
| Rate of SD = 1 | 0.245 | 0.286 |

No single signal differs much, so no single signal separates sarcasm on its own.

<figure>
  <img src="/column-images/discoverai-sarcasm-world-model/lr-weights-1600.webp" alt="Top-10 LR weights" />
  <figcaption><strong>Figure 6.</strong> Top-10 logistic-regression weights by absolute value (figure from the paper). Positive weights push toward sarcasm, negative toward non-sarcasm.</figcaption>
</figure>

The top weights belong to features built from the intention score, such as σ(T), √T and log(1 + T). T − D has a positive weight and D − T a negative one. This matches the design idea: sarcasm is more likely when the intention signal outweighs the gap, and a large gap without strong intention is less likely to be judged sarcastic.

<figure>
  <img src="/column-images/discoverai-sarcasm-world-model/cases-1600.webp" alt="Case studies" />
  <figcaption><strong>Figure 7.</strong> Agent outputs for two cases. Left: a polite corrective post correctly judged non-sarcastic. Right: a sarcastic post that was missed.</figcaption>
</figure>

For the right-hand case, "A truly charming publication. Overflowing with the warmth of human goodness.", both the literal and norm scores are 0.80, the gap is 0, and the intention score is 0.10. Every agent read it as sincere praise, so the sarcasm was missed. Sarcasm that looks positive on the surface, on the norm and on intention is a type WM-SAR handles poorly, since it relies on gaps and intention. Because each agent's numbers and rationales are kept, we can still see where the misreading happened.

## What we found, and what we did not

What we found:

- Splitting sarcasm understanding into literal meaning, context, norm, gap and intention, and combining them with logistic regression, outperformed existing deep-learning and LLM-based methods on three benchmarks.
- Intention reasoning contributes most; the gap between surface and norm works as a supporting signal.
- Because intermediate numbers and rationales are kept, a person can trace what happened for both correct and wrong predictions.

There are limitations. We only used the GPT-4.1 family and have not checked other model families. The evaluation uses sentence-level datasets, so sarcasm that needs dialogue history is not covered. Sarcasm that looks positive on every signal is easily missed, and some redundancy remains among the features (handled by L2 regularization). The reasoning inside each agent also remains partly opaque.

Next steps include testing other LLM families, extending to datasets with dialogue context, and moving toward multimodal input.
