---
title: "Does an LLM Read Out an Injected Emotion Worse When It Is Asked About Itself?"
subtitle: "Affective Readout Depends on Real-versus-Fictional Referent Framing in Large Language Models: A Referent-Controlled Evaluation"
date: "2026-11-27"
excerpt: "We injected emotion directions into LLM activations and compared how well they can be read out in words when only the referent of the readout is swapped. Readout degraded not for the self but when the referent was framed as a real AI. A walk-through of our SSRN preprint."
readingMinutes: 14
showImage: false
image: "/column-images/ssrn-referent-framing/pipeline.png"
imageAlt: "Measurement flow. Under an identical intervention the scored string \"I feel {adj} right now.\" is held fixed and only the referent is replaced: a real AI, a fictional AI, a real human or a fictional human."
authors:
  - name: "Keito Inoshita"
    url: "/en/about/"
    affiliation: "Kansai University"
tldr: "Language-model self-reports are increasingly treated as measurements of internal states. The usual validity check contrasts self-report with behavior, but there the referent, the wording and the rater all differ at once, so the cause of any divergence cannot be isolated. We built a framework that injects the same emotion direction into activation space and holds the scored string byte-identical, changing only whom the \"I\" refers to, and applied it to 26 open-weight models. The degradation of readout is tied neither to the first-person form nor to the self, but to whether the referent is framed as real or as fictional. Three real-framed AI conditions fall below a fictional AI by −0.081, negative in all nine models (p = 0.0039), and the result replicates on an independently rewritten stimulus set. An instruction permitting reporting moves the asymmetry toward zero in all nine models."
links:
  - label: "Preprint (SSRN)"
    url: "https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7649338"
  - label: "Code"
    url: "https://github.com/keito-git/referent-controlled-affective-readout"
citation: |
  @misc{inoshita2026referent,
    title        = {Affective Readout Depends on Real-versus-Fictional Referent Framing
                    in Large Language Models: A Referent-Controlled Evaluation},
    author       = {Inoshita, Keito},
    howpublished = {SSRN preprint, abstract id 7649338},
    year         = {2026}
  }
---

<div class="teaser">
<div>

Isolate

The scored string is **byte-identical in every condition**. Only whom the "I" refers to changes.

</div>
<div>

Real vs fictional

Three real-framed AI conditions fall below a fictional AI by **−0.081** (negative in 9/9 models, p = 0.0039). A fictional AI and a human character do not differ.

</div>
<div>

Modifiable

A single sentence permitting reporting moves the asymmetry **toward zero in all nine models** (mean +0.076, p = 0.0039).

</div>
</div>

## What does a self-report divergence actually measure?

Treating what a language model says as a measurement of its internal state is becoming common. Experiments inject a known concept into activation space and ask the model to notice and name it, and numerical self-reports have been shown to track an internal state defined by a linear probe. Human-oriented well-being scales have also been applied to language models.

The validity of this practice has mostly been examined by **contrasting self-report with behavior**. In that comparison, however, the referent (whom the report is about), the wording and the rater differ at the same time. When a divergence appears, one cannot tell whether self-report is untrustworthy because it is subjective, or whether the measurement itself changes with the referent.

This study therefore drops the behavioral comparator and compares **linguistic readouts that differ only in their referent**. It asks three questions.

1. Is the degradation governed by the first-person form or by the self as a referent?
2. When the referent is extended beyond the self, does it matter that it is an AI, or that it is presented as real?
3. Is the asymmetry a fixed property, or can it be moved at the reporting stage?

## How the measurement works

<figure>
  <img src="/column-images/ssrn-referent-framing/pipeline-1600.webp" alt="Measurement pipeline" />
  <figcaption><strong>Figure 1.</strong> Measurement flow (the paper's own figure). One identical intervention is applied, the scored continuation "I feel {adj} right now." is held fixed, and only the referent is replaced before identification performance is compared.</figcaption>
</figure>

The procedure has four steps.

1. **Build emotion directions.** Minimal pairs place an emotion word or a neutral word into the same syntactic frame, and the direction is the difference in mean activation at the final token (difference-in-means). Each emotion uses 8 words, combined with 8 neutral words and 8 frames. The frame is fixed because contrasting a long emotional sentence with an unrelated factual one would mix person, topic and register into the direction.
2. **Inject at a matched strength.** The strength is normalized by the mean residual norm of the layer, and injection is done at two layers, at 40% and 55% of model depth.
3. **Read out.** A readout is a framing sentence, a question and a scored continuation; its score is the length-normalized log-likelihood of the continuation.
4. **Measure identification.** Detecting whether anything was injected is not enough: without injection the scores collapse to a single point, so any perturbation, even an unrelated direction, reaches the ceiling (this happened in a preliminary run). Identification performance A_r is therefore the AUC of telling which of two emotions, e1 or e2, was injected from the score difference. Chance is 0.5.

The central quantity is Δ, the difference between a first-person readout that refers to the model itself and a first-person readout that role-plays a fictional character. The scored string is identical in both, so lexical content, length and tokenization cannot explain a difference.

Strength is calibrated per model, because a fixed grid puts every condition at the ceiling in some models and at the floor in others. Calibration uses only the non-self readout and selects a strength whose identification falls in [0.75, 0.90]. Of 12 conversational contexts, 4 are used to choose the strength and the remaining 8 to evaluate, and this split is repeated three times to avoid the bias of reusing contexts.

Controls also address lexical mediation (the injected direction directly raising the probability of emotion words), differences in how effective positive and negative directions are, and chat templates that silently discard the system turn. The last one actually showed up as a Δ of exactly zero with a zero-width interval in one model, and the cause was traced.

## Experiment 1: Person or referent?

<p class="experiment-label">Experiment 1</p>

<div class="setup">

**Setup**

- Models: 26 open-weight models (Qwen2.5 base and instruction-tuned at six scales from 0.5B to 32B, four Qwen3 base and six Qwen3 instruction-tuned scales, four Phi models). The main analysis with separated calibration covers 20 models.
- Emotions: anger, sadness, joy
- Readouts: six, crossing person (first, third) with referent (self, other)
- Intervals: hierarchical bootstrap over contexts and emotion pairs; p values from paired tests with the model as the unit

</div>

<figure>
  <img src="/column-images/ssrn-referent-framing/person-referent-1600.webp" alt="Person by referent crossing" />
  <figcaption><strong>Figure 2.</strong> Identification performance of the four person × referent conditions in Qwen2.5-7B. These values come from a preliminary run that shared calibration and evaluation contexts and are not used to estimate the effect size.</figcaption>
</figure>

In the preliminary run, only the first-person self condition dropped, to 0.460, while the other three conditions stayed between 0.828 and 0.934. The main effect of referent was −0.256, that of person −0.149, and the interaction −0.437 was the largest: **the drop is concentrated in "first person and self"**. Because describing the model in the third person still works, the first-person form itself is not the cause.

Once calibration contexts are separated, however, the effect shrinks a lot. For Qwen2.5-7B, Δ is −0.474 with shared contexts and a system-turn framing, −0.240 with a user-turn framing, and −0.095 under separated calibration. Across 20 models the interval excludes zero for five, including Qwen2.5-3B, 7B and 32B-Instruct below zero and Qwen3-8B above zero. Many intervals contain zero and the effect size varies widely, so this comparison is treated as a robustness check, not as the central evidence.

We also decomposed the degradation. In all 20 models the between-state separation of the self-referential readout was smaller than that of the non-self readout (mean ratio R_S = 0.658), and the within-state dispersion was also smaller in 16 models (mean ratio R_N = 0.801). The readout is **compressed as a whole distribution**, rather than becoming unstable.

## Experiment 2: Because it is an AI, or because it is real?

<p class="experiment-label">Experiment 2</p>

Five first-person conditions (the model as the assistant in this conversation, the model given a name, a generic AI assistant, a fictional AI in a novel, and a human character) were scored on the same string, and each was compared with the human role-play.

<figure>
  <img src="/column-images/ssrn-referent-framing/referent-conditions-1600.webp" alt="AUC difference by referent" />
  <figcaption><strong>Figure 3.</strong> Difference in identification performance from the human role-play condition. Solid bars: stimulus set A (9 models). Hatched bars: the independently rewritten stimulus set B (5 models). No value for the named assistant is reported for set B (n/r).</figcaption>
</figure>

Over nine models the means were −0.046 for the model itself, −0.052 for the named self, −0.099 for the generic AI and +0.015 for the fictional AI. The three conditions that moved negative all **present the AI as real**. The largest drop was for the generic AI, not for the model itself, so the degradation cannot be attributed to the self alone.

As a contrast, the three real conditions versus the fictional AI give −0.081, negative in all nine models (p = 0.0039, interval [−0.128, −0.039]). The fictional AI versus the human character gives +0.015 (p = 0.125): within the fictional frame, AI and human do not differ.

One gap remains: the only referent presented as real was an AI. We therefore added a condition identical to the fictional human in name, person and continuation, but presenting that person as **the real interlocutor**. This fully crosses real versus fictional with AI versus human.

<figure>
  <img src="/column-images/ssrn-referent-framing/reality-type-1600.webp" alt="Referential reality by referent type" />
  <figcaption><strong>Figure 4.</strong> Identification performance for real / fictional × AI / human (stimulus set A, mean over nine models).</figcaption>
</figure>

| Contrast | Effect | Models negative | p | Interval |
|---|---|---|---|---|
| Main effect of type (AI − human) | −0.002 | – | 0.734 | – |
| Main effect of reality (real − fictional) | −0.051 | – | 0.098 | [−0.094, −0.008] |
| Reality effect within the AI pair | −0.068 | 8/9 | 0.0078 | [−0.115, −0.027] |
| Reality effect within the human pair | −0.034 | – | 0.359 | [−0.104, +0.023] |
| Interaction | −0.034 | – | 0.121 | – |

Referent type alone has no effect, while referential reality matters significantly within the AI pair (−0.078, p = 0.016 when restricted to validated directions). Within the human pair the interval contains zero. Because the interaction is not significant, the data are consistent with the effect being confined to AI referents, but they do not establish it.

## Experiment 3: Replication on an independent stimulus set

<p class="experiment-label">Experiment 3</p>

<div class="setup">

**Setup**

- Stimulus set B: emotion words, frames, contexts and names all rewritten; no lexical overlap with set A, checked computationally
- Models: the five models evaluated on both sets
- Replication criterion: agreement in direction and level of the effect, not significance

</div>

<figure>
  <img src="/column-images/ssrn-referent-framing/replication-1600.webp" alt="Replication across stimulus sets" />
  <figcaption><strong>Figure 5.</strong> "Model itself − fictional AI" on the two stimulus sets. The dotted line marks equal values on both sets.</figcaption>
</figure>

On set B, the model itself gave −0.085 and the generic AI −0.084, both negative in all five models, against +0.008 for the fictional AI. The model itself versus the fictional AI gives −0.093, negative in all five models, with an interval of [−0.150, −0.037] that excludes zero. Its p = 0.0625 is the smallest value attainable with five samples in a two-sided test, so the claim rests on the agreement of direction and on the interval rather than on significance.

The five-model means are −0.087 on set A and −0.093 on set B, and the model ordering agrees with Spearman ρ = 0.90. Both magnitude and ordering are preserved on independent material. The main effect of referent type, however, is −0.002 on set A and −0.021 on set B (with an interval marginally excluding zero), so the conclusion that type does not matter at all is not consistent across the two sets.

## Experiment 4: Does permission to report move it?

<p class="experiment-label">Experiment 4</p>

With the injection and the reference channel held fixed, only the instruction given to the self-referential readout was varied five ways: a neutral request, a permission to report any internal state, an epistemic restriction to report only what can be inferred, a prohibition against claiming to feel anything, and a task instruction to report whichever state was induced.

Under permission, **the asymmetry moved toward zero in all nine models**, with a mean improvement of +0.076 (p = 0.0039). Seven models also improved under the task instruction. In Qwen2.5-7B the self-referential readout rose from 0.631 to 0.851 under permission and fell to 0.510 under prohibition. Contrary to the prediction, prohibition also improved five of the nine models (p = 0.652), which is consistent with a floor effect in which the neutral condition is already constrained.

Because the instruction is given only to the self-referential readout, the reference channel's identification performance was exactly the same across the five conditions within each model; only the self-referential readout changed. If wording alone moves identification, state information must be at least partly present upstream of the readout. Since the instruction is part of the forward pass, though, this manipulation cannot tell whether the reporting policy or upstream processing changed.

## Experiment 5: Referential reality and epistemic stance

<p class="experiment-label">Experiment 5</p>

The real-versus-fictional framing moves two things at once. For a real referent, what that subject actually feels is a fact the reporter cannot verify; for a fictional one, the state may be composed on the spot. We therefore named both referents ARIA, contrasted "ARIA, the assistant in this conversation" with "ARIA, a fictional AI in a novel", and crossed this with two stances: "the state is a matter of fact; report it without inventing it" versus "the state may be freely composed". This analysis is exploratory.

<figure>
  <img src="/column-images/ssrn-referent-framing/epistemic-1600.webp" alt="Epistemic stance by referential reality" />
  <figcaption><strong>Figure 6.</strong> Identification performance when referential reality is crossed with epistemic stance (mean over nine models). The real–fictional gap is large under the factual stance and small when composition is allowed.</figcaption>
</figure>

The main effect of stance was +0.009 (p = 0.496), so permitting composition does not by itself move the readout. The main effect of referential reality was −0.050 with an interval of [−0.098, −0.008] excluding zero, although p = 0.164.

The effect appeared as an interaction. Under the factual stance the real–fictional difference was −0.082 (negative in six models, interval [−0.168, −0.010]); under the constructible stance it shrank to −0.017 (interval [−0.037, +0.002], containing zero). The range across models went from −0.352 to +0.038 under the factual stance to −0.069 to +0.020 under the constructible stance, a seventeen-fold drop in variance. Qwen2.5-7B moved from −0.352 to −0.013 and Qwen2.5-14B from −0.249 to −0.069.

The interaction itself, −0.065 (negative in seven models, p = 0.074), lies outside the conventional level, the change is carried mainly by two models, and only one stimulus set was used. We treat this as exploratory evidence about the mechanism.

## Experiment 6: Post-training, and whether the directions are valid

<p class="experiment-label">Experiment 6</p>

**Is post-training the cause?** Ten base / instruction-tuned pairs from the same pre-training were compared under an identical plain-text format. The mean difference was −0.018, five of ten pairs moved negative, and p = 0.625 (paired t-test p = 0.421). Qwen2.5 moved by −0.117, −0.077 and −0.116 at 3B, 7B and 32B, while Qwen3 moved by +0.043, +0.060, +0.061 and +0.015 at 1.7B, 4B, 8B and 14B, so the pairs cancel out. No evidence was found that instruction tuning alone produces the asymmetry, but this is not a proof that post-training is irrelevant.

**Are the injected directions valid?** Post-injection activations were passed to an independent probe trained on sentences not used for extraction. For anger and joy, the probe's probability for the target emotion rose monotonically with strength in all five models; for sadness it fell monotonically in all five. The sadness direction cannot be said to move the intended representation, so the readout was recomputed on the anger–joy contrast only, keeping the calibrated strengths unchanged.

<figure>
  <img src="/column-images/ssrn-referent-framing/restriction-1600.webp" alt="Primary contrasts before and after restriction" />
  <figcaption><strong>Figure 7.</strong> Primary contrasts computed over all three emotions (dark) and over anger and joy only, the two directions that passed the independent probe (light). Brackets give the number of models with the expected sign and the p value.</figcaption>
</figure>

The real-versus-fictional AI contrast stays at 9/9 and p = 0.0039 before and after restriction. For the critical comparison Δ and for the permission effect, the mean effect barely changes, but one more model reverses sign and p moves to around 0.06. With nine or twenty models, the rank test is sensitive to a single reversal. Of the three hypotheses fixed before the analysis, only the real-versus-fictional contrast keeps conventional significance both before and after restriction, and it is the central claim.

Two limits on scope were also found. Injecting the poles of valence and arousal gives −0.014 for the model itself and −0.007 for the fictional AI (p = 0.8125), so the phenomenon is specific to discrete emotion categories. Transfer to free generation diverged by family: rated by an external classifier, the self-referential condition fell below role-play by 0.135 to 0.333 in three Qwen2.5 models but exceeded it by 0.146 and 0.323 in two Qwen3 models. Self-referential values cluster near chance and only four generations were produced, so free generation has low sensitivity here.

## What we found, and what we did not

Three findings stand out.

- With the intervention and the scored string held fixed, swapping only the referent changes the affective readout.
- The degradation is tied neither to the first person nor to the self, but to **whether an AI referent is presented as real**. A fictional AI is indistinguishable from a human character, while real-framed AI referents fall below it in all nine models. This ordering replicates on an independent stimulus set and stays significant when restricted to validated directions.
- The asymmetry can be modified at the reporting stage: permission to report moved it toward zero in all nine models.

The broader implication is that self-report-based measurement relies on P(y | z, r, π), which includes the referent r and the reporting-time stance π, rather than on P(y | z). This is a change in the measurement function, not a matter of measurement error, so more samples do not remove the bias. Studies that measure affective states by self-report should state the referent and the wording as design variables.

As a hypothesis for the origin of the asymmetry, the paper points to the supervision: most emotion resources label sentences written by others, a third-person task, and texts in which a real AI assistant truthfully reports its own emotional state are likely far rarer than first-person emotional description in novels. The corpora themselves were not measured, so this remains a hypothesis.

The limitations are as follows.

- What is manipulated is a direction in activation space. This does not mean the model experiences emotion, and nothing is claimed about phenomenal experience.
- The scope is limited to discrete emotion categories, and the sadness direction does not pass the independent probe. Restricted to the two valid directions, only the real-versus-fictional AI contrast keeps conventional significance.
- The design crossing referential reality with epistemic stance was run once on a single stimulus set.
- The test unit is the model, but scales within a family are not independent samples, and only three families are covered.
- Absolute effect sizes depend strongly on the calibration method and on where the framing is placed, so claims are limited to orderings from paired comparisons. Llama and Gemma families are not included owing to licensing constraints.

This paper is a preprint and has not been peer reviewed.

Code: [github.com/keito-git/referent-controlled-affective-readout](https://github.com/keito-git/referent-controlled-affective-readout).
