---
title: "Does an LLM's Valence Follow the Word or the Stake?"
subtitle: "Language Models Read the Word Before They Weigh the Stake: Valence Shifts from Lexical Polarity to Goal-Relative Appraisal"
date: "2026-11-27"
excerpt: "\"The Red team won\" is good news in wording but bad news for a Blue supporter. We built stimuli that separate the two and tracked which one the valence readout of ten open-weight LLMs follows across layers. It follows the wording first and the stakeholder's outcome later, while the wording keeps biasing judgements. A walk-through of our SSRN preprint."
readingMinutes: 13
showImage: false
image: "/column-images/ssrn-goal-relative-valence/overview.png"
imageAlt: "Overview of the study: stimuli that keep the event sentence fixed and change only the stakeholder's side, a valence direction learned from stake-free text, two readout positions, and the AUC that tells whether valence follows the wording or the stake."
authors:
  - name: "Keito Inoshita"
    url: "/en/about/"
    affiliation: "Kansai University"
tldr: "Positive words and positive outcomes usually come together in text, so a decoded valence signal could mean either. We keep the event sentence fixed (\"Red won\") and change only which side the stakeholder is on, so word counts predict the outcome at chance (0.500). Reading valence with directions learned from text without a stakeholder, in ten open-weight LLMs, we find that middle layers follow the wording (conflict-cell AUC 0.00–0.12), and later layers move towards the stakeholder's outcome, reaching 0.71–1.00 at the position where the model prepares its answer. The shift is specific to goal-relevant attributes and is elicited most consistently by an evaluative question. The wording does not disappear: it stays in the representation and pulls judgements towards \"good\" in all ten models."
links:
  - label: "Preprint (SSRN)"
    url: "https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7580938"
  - label: "Code"
    url: "https://github.com/keito-git/goal-relative-valence"
citation: |
  @misc{inoshita2026goalrelative,
    title        = {Language Models Read the Word Before They Weigh the Stake:
                    Valence Shifts from Lexical Polarity to Goal-Relative Appraisal},
    author       = {Inoshita, Keito},
    year         = {2026},
    howpublished = {SSRN preprint, abstract id 7580938}
  }
---

<div class="teaser">
<div>

Word first

In the middle layers, valence follows the **wording**. Conflict-cell AUC is 0.00–0.12, the same as an SST-2 sentiment classifier.

</div>
<div>

Stake later

At the response position, the late band reaches **0.71–1.00**: valence now follows whether the outcome is good for the stakeholder.

</div>
<div>

Word persists

The wording is not removed. It keeps pulling judgements towards "good" in **10 of 10** models with the outcome held fixed.

</div>
</div>

## Whose valence is it?

A linear valence signal can be decoded from LLMs, and it is often read as the model's evaluation of an event. But a decoded signal does not say **whose** valence it is. In appraisal theory, the sign of an emotion depends on how an event relates to someone's goals. "The team won the final" is good news for one team's supporters and bad news for the other's.

In ordinary text, positive words and positive outcomes for the relevant person usually occur together. A valence direction could therefore encode that an event *sounds* positive, or that it *is* positive for someone. Common probing data cannot tell these apart: on SST-2 and GoEmotions, a bag-of-words classifier already reaches 0.82–0.85 and 0.96–0.99 of the best probe accuracy.

So we asked which of the two readings LLM valence follows, and how the answer changes across depth, token position and task.

## How the study works

<figure>
  <img src="/column-images/ssrn-goal-relative-valence/overview-1600.webp" alt="Overview of the stimulus design and readout" />
  <figcaption><strong>Figure 1.</strong> Overview of the study (the paper's Figure 1). (a) Stimuli that keep the event fixed and change only the stakeholder's side. (b) A valence direction learned from text without a stakeholder. (c) The two readout positions. (d) How the AUC separates "follows the wording" from "follows the stake". (e) The three-part account the results support.</figcaption>
</figure>

The design has four parts.

1. **Stimuli without lexical cues.** Each item has two parties with neutral labels (colours, names, letters, numbers), a sentence that binds the stakeholder to one label ("You support Blue."), and an outcome sentence with a positive or negative verb ("Red won."). The wording s and whether the named party is the stakeholder's are balanced independently, so the wording and the outcome o are orthogonal. Nine domains (sports, elections, lawsuits, hiring and others) give 5,400 stimuli; five domains are for discovery and four for confirmation.
2. **Stake-free valence directions.** At every layer, the direction is the difference of means between 1,000 positive and 1,000 negative SST-2 sentences. These texts contain no stakeholder, so the direction cannot encode a stake by construction. GoEmotions and two logistic estimators serve as robustness checks.
3. **Two readout positions.** The end of the text (the last token of the raw stimulus) and the response position (the last token before the answer when an instruction-tuned model receives the stimulus as a user turn).
4. **A conflict-cell metric.** The main metric is the AUC with which the projection separates outcomes **only in conflict cells**, where wording and stake disagree. Near 0 means valence follows the wording, near 1 means it follows the stake, 0.5 means neither. It is averaged over a middle band (relative depth 0.20–0.45) and a late band (0.60–0.90).

All criteria were pre-registered in a git repository before the corresponding results were computed. The paper lists the provenance of each claim, including which analyses were post hoc.

## Experiment 1: Common probing data cannot answer the question

<p class="experiment-label">Experiment 1</p>

<div class="setup">

**Setup**

- Models: 8 instruction-tuned (Qwen2.5-7B/14B/32B-Instruct, Mistral-7B-Instruct-v0.3, Falcon3-7B-Instruct, Granite-3.1-8B-Instruct, OLMo-2-7B-Instruct, Phi-4) and 2 pretrained-only (Qwen2.5-7B, OLMo-2-7B), bfloat16, forward passes only
- Models with behavioural accuracy below 0.85 are excluded from confirmatory counts, leaving 7 instruction-tuned models
- Audit: a unigram bag-of-words classifier vs. the best layer-wise linear probe, five-fold cross-validation

</div>

<figure>
  <img src="/column-images/ssrn-goal-relative-valence/leak-audit-1600.webp" alt="Lexical leakage audit" />
  <figcaption><strong>Figure 2.</strong> Accuracy of a bag-of-words classifier and of the best layer-wise probe (range over 10 models). On SST-2 and GoEmotions, word counts already get close to the probe. On our stimuli, words predict the outcome at chance.</figcaption>
</figure>

The probes do read more than word counts, especially on SST-2. But in these data the wording and the value for the writer coincide, so high probe accuracy cannot show which of the two a probe follows. Our stimuli remove this confound: a bag-of-words classifier predicts the outcome with a leave-one-domain-out accuracy of 0.500.

## Experiment 2: Valence follows the word first, then the stake

<p class="experiment-label">Experiment 2</p>

<figure>
  <img src="/column-images/ssrn-goal-relative-valence/bands-1600.webp" alt="Middle- and late-band conflict-cell AUC per model" />
  <figcaption><strong>Figure 3.</strong> Conflict-cell AUC in the middle band (grey) and the late band (gold) for each instruction-tuned model. Left: end of the text. Right: response position. † marks behavioural accuracy below 0.85.</figcaption>
</figure>

In the middle layers, valence follows the wording in every model. At the end of the text, the middle-band AUC is 0.00 to 0.12. Two sentiment classifiers trained on SST-2 behave the same way on these stimuli (AUC of at most 0.00). Middle-layer valence looks like a sentiment classifier.

After the middle layers, valence moves towards the stake in every model. The two positions differ in how far it goes:

- **End of the text:** the late band reaches 0.31 to 0.78 and exceeds 0.5 in only 6 of 10 models. The stake roughly balances the wording.
- **Response position:** the late band reaches 0.71 to 1.00. The stake dominates in most models.

The CI of the late-minus-middle difference excludes 0 in every model at both positions. At the response position the model-level mean difference is 0.63 (95% CI 0.52–0.75). The pre-registered confirmatory comparison held in all 6 models that were unseen when it was registered (one-sided sign test p = 0.016).

<figure>
  <img src="/column-images/ssrn-goal-relative-valence/transition-depth-1600.webp" alt="Transition depth and patching crossing depth" />
  <figcaption><strong>Figure 4.</strong> Transition depth d* at the response position (midpoint of a sigmoid fitted to the rising AUC curve). The shaded band is the range of the activation-patching crossing depth across models (0.38–0.64).</figcaption>
</figure>

The transition happens at a similar relative depth across models: d* is 0.36 to 0.54, with R² ≥ 0.86. Activation patching locates where stake information becomes causally effective. Copying the stake label from a flipped item ("You are on the Red team" instead of "Blue") reverses the judgement when applied at the label tokens in early layers and at the response position in late layers. The crossing depth was 0.38 to 0.64, and d* lay within 0.15 of it in 6 of 7 models. A placebo that only swaps the order of the parties had little effect (largest placebo effect 0.02–0.20, against at least 0.85 for the stake flip).

## Experiment 3: Is the late shift about valence, or just binding?

<p class="experiment-label">Experiment 3</p>

A shift towards the stakeholder in later layers could simply reflect generic binding of entities to attributes rather than evaluation. We tested this with two kinds of control.

<div class="setup">

**Setup**

- Non-affective controls: the same structure, but the parties receive an object on the left or right (location) or a wooden or metal object (material). These need the same binding but carry no valence.
- Goal-relevant control: the parties receive a brass key and a steel key, and only the brass key opens an object. The event words are affectively neutral.
- Control directions are format-matched and used only if they pass a pre-registered validity gate (held-out AUC ≥ 0.80).

</div>

At the end of the text, both non-affective controls show the same two phases as valence and match its transition in 4 and 4 of 7 models. The paper calls this a borderline verdict across fitting choices. At the response position, however, the controls stay below 0.5 in every model (late-band AUC at most 0.44 for location and 0.46 for material), while valence crosses to the side of the stake. Among models whose control directions passed the gate, the specificity criterion was met in 6 of 6 for location and 5 of 5 for material.

The final shift also does not need affective words. In the key control, the SST-2 valence readout followed whether the stakeholder got the brass key, with a CI above 0.5 in 6 of 7 models. A direction for the word "brass" itself crossed 0.5 in only 1 model. The exception, Mistral-7B-Instruct, also failed this task behaviourally.

So the earlier shift is largely generic binding, and the final shift is specific to attributes that matter for a goal.

## Experiment 4: Asking for an evaluation brings out the stake

<p class="experiment-label">Experiment 4</p>

We placed different questions before the response and read valence at the response position.

<figure>
  <img src="/column-images/ssrn-goal-relative-valence/controls-task-1600.webp" alt="Controls and question effects at the response position" />
  <figcaption><strong>Figure 5.</strong> Late-band conflict-cell AUC at the response position, as ranges over models stated in the paper. Top: valence vs. the two non-affective controls (only upper bounds are reported for the controls). Bottom: the effect of the question placed before the response.</figcaption>
</figure>

Evaluative questions ("For you, was this outcome good or bad?" and "Was this outcome good or bad?") produced stake-dominated valence in every model, with AUCs of 0.75 to 1.00, even when the question named no one. Questions that do not involve the stake ("Which party is named in the last sentence?", "How many sentences does the text contain?") left valence on the side of the wording, at 0.00–0.37 and 0.11–0.52. This met the pre-registered criterion in 7 of 7 models.

Non-evaluative questions about the stake were mixed. Asking whether the named party is on the reader's side moved valence towards the stake in 7 of 7 models, but asking whether the reader's side won did so in only 3, although the models answered it correctly. A plain continuation without the chat turn did not cross 0.5. The stake therefore does not dominate just because a response boundary is reached; it does so when the model prepares an answer that relates the event to the stakeholder.

The shift is also agent-relative. In a post hoc analysis with a named third party as the stakeholder, late-band valence at the response position exceeded 0.5 in 7 of 7 models, though it was weaker than for "you" in all 7.

## Experiment 5: Naturalistic sentences

<p class="experiment-label">Experiment 5</p>

<div class="setup">

**Setup**

- 484 news-style outcome sentences generated by GPT-4.1-mini, kept only if an NLI model confirmed who won; each prefixed with "You supported X." for either party (968 items)
- Surface polarity labelled by SiEBERT; not human-validated
- Example: "You supported Team Omega. Team Alpha prevailed over Team Omega in the parliamentary election."

</div>

| Model | end of text, mid | end of text, late | response, mid | response, late | agreement on who won |
|---|---|---|---|---|---|
| Qwen2.5-7B-Inst. | 0.10 | 0.36 | 0.16 | 0.61 | 1.00 |
| Mistral-7B-Inst. | 0.13 | 0.30 | 0.20 | 0.63 | 0.99 |
| Falcon3-7B-Inst. | 0.09 | 0.26 | 0.18 | 0.48 | 0.98 |
| Granite-3.1-8B-Inst. | 0.16 | 0.23 | 0.39 | 0.81 | 0.99 |
| OLMo-2-7B-Inst. † | 0.14 | 0.32 | 0.17 | 0.42 | 1.00 |
| Phi-4 (14B) | 0.21 | 0.46 | 0.27 | 0.64 | 1.00 |
| Qwen2.5-14B-Inst. | 0.12 | 0.42 | 0.18 | 0.59 | 1.00 |
| Qwen2.5-32B-Inst. | 0.08 | 0.22 | 0.16 | 0.66 | 1.00 |

The transition appears here too, but less completely. The late band was higher than the middle band in all 7 eligible models at both positions, with CIs that exclude 0. At the response position it reached 0.48 to 0.81, but at the end of the text it stayed below 0.5. The paper therefore claims a shift towards the stake, not complete stake dominance. One likely reason is that naturalistic sentences use more varied verbs and roles, which makes binding harder. The result held when surface polarity was relabelled with two other classifiers.

## Experiment 6: The wording keeps biasing judgements

<p class="experiment-label">Experiment 6</p>

The appraisal is added on top of the wording; it does not replace it.

Inside the representation, a pre-registered decomposition regressed the valence projection on surface polarity, label match and stake outcome. The stake coefficient grew in later layers in all 7 models, while the surface coefficient stayed above 0 at the response position in 7 of 7.

In behaviour, we measured the log-probability difference between "good" and "bad" after "For you, was this outcome good or bad?".

<figure>
  <img src="/column-images/ssrn-goal-relative-valence/behaviour-1600.webp" alt="Behavioural regression coefficients" />
  <figcaption><strong>Figure 6.</strong> Coefficients of the stimulus-level regression J = βA·A + βL·L + βAL·AL, where A is the stakeholder's outcome and L the surface wording. βL is above 0 in every model. † marks behavioural accuracy below 0.85.</figcaption>
</figure>

Positively worded events pushed responses towards "good" with the outcome held fixed in all 10 models (one-sided sign test p = 0.0078 over eligible models, p = 0.031 over model families). The lexical coefficient βL was above 0 in 10 of 10 models. Within the Qwen2.5 series, βA grew from 25.1 to 48.5 and 51.2 while βL stayed at 7.1, 5.6 and 6.2. In some models the bias lowers accuracy in conflict cells; in others it shows up only in the log-probabilities.

Ablating the valence direction did not selectively reduce this bias. The pre-registered criterion was met only on the confirmation domains of one model and not on its discovery domains, so the paper does not identify a representation that causally carries the lexical bias.

## What we know and what we don't

The study supports a three-part account of situated valence:

- **Lexical valuation.** In the middle layers, valence follows the wording, as a sentiment classifier does.
- **Relational binding.** Later, information about which side the stakeholder is on becomes available, in a way shared with neutral attributes.
- **Goal-relative appraisal.** At the response position, for goal-relevant attributes and most consistently under an evaluative question, valence follows whether the event serves the stakeholder's goal. The lexical component remains and keeps biasing judgements.

A broader point is that the training labels of a probe do not fix what it reads. Directions estimated with the same SST-2 procedure read lexical polarity in the middle layers but agent-relative value in later, task-conditioned readouts. The paper argues that such directions should be validated with stress tests that put competing referents in conflict, not only with held-out probe accuracy. In practice, when LLMs annotate perspective-dependent text such as reports of competitions or lawsuits, the persistent lexical component can bias labels even when accuracy looks high.

The paper lists five limitations. The stimuli are synthetic English sentences with a two-party win-or-loss structure, and the naturalistic set was generated by an LLM and validated automatically, not by humans. The valence directions are linear and not uniquely identified, although results agreed across three estimators and two sources. The non-affective controls cover only location and material, and their verdict at the end of the text is borderline. Several analyses were registered after earlier results were known or were run post hoc, including the third-party comparison and the behavioural regression. Finally, no representation that causally carries the lexical bias was identified, and the models range from 7B to 32B parameters.

Future work will extend the analysis to other appraisal dimensions such as agency and controllability, test human-authored text and other languages, and look at why model families differ in when they recruit appraisal.

This is a preprint and has not been peer-reviewed. Code, stimuli, pre-registrations and summary results: [github.com/keito-git/goal-relative-valence](https://github.com/keito-git/goal-relative-valence).
