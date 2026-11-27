---
title: "Does Steering a Concept Direction Show the Model Uses That Concept?"
subtitle: "Behavioral Steering Does Not Establish Concept-Specific Causal Control in Language Models"
date: "2026-11-27"
excerpt: "If pushing a concept direction inside a language model changes its behaviour, does the model decide through that concept? We set out the evidence such a claim needs and compared real directions with nulls trained by the same procedure. Concept selectivity and the behavioural effect never held together at the same doses. A walk-through of our SSRN preprint."
readingMinutes: 13
showImage: false
image: "/column-images/ssrn-behavioral-steering/framework.png"
imageAlt: "Evaluation framework in five stages: rating validity, interchange at the rating prompt, natural-amplitude interchange, additive steering at matched doses, and comparison with null directions."
authors:
  - name: "Keito Inoshita"
    url: "/en/about/"
    affiliation: "Kansai University"
tldr: "When activation steering changes behaviour, the direction is often read as controlling behaviour through the concept that names it. This study proposes the Selectivity–Effect Overlap Criterion, an evidential criterion for concept-specific causal control. It checks rating validity, selectivity under additive steering, and a behavioural effect at the same doses, each against random directions and against nulls trained by the same procedure with permuted targets. For controllability and success expectation in a two-phase decision task with two language models, interchange interventions find directions that carry each concept selectively. Under additive steering, however, their selectivity is not distinguishable from the optimisation-matched nulls, and the behavioural effect beats random directions but not these nulls. Even a rule variable with known ground truth fails the behavioural step: a representation that reports a variable need not be the one that mediates behaviour."
links:
  - label: "Preprint (SSRN)"
    url: "https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7705480"
  - label: "Code"
    url: "https://github.com/keito-git/concept-direction-validity"
citation: |
  @misc{inoshita2026steering,
    title        = {Behavioral Steering Does Not Establish Concept-Specific Causal
                    Control in Language Models},
    author       = {Inoshita, Keito},
    year         = {2026},
    howpublished = {SSRN preprint, abstract id 7705480}
  }
---

<div class="teaser">
<div>

Interchange

Under interchange, the controllability direction carries **0.883** of the rating difference; the best of 50 matched nulls reaches 0.714.

</div>
<div>

Steering

Under additive steering, its selectivity is 0.412, while the matched-null 95th percentile is **0.575–0.599**. No dose beats the nulls.

</div>
<div>

Rule control

A rule with known ground truth still fails the behavioural step. At the choice, the full state carries **74%** of the gap; the direction carries **< 0.01%**.

</div>
</div>

## A behavioural effect is not a concept attribution

Many concepts appear to be encoded as directions in the residual stream of large language models. Adding a vector along such a direction during inference can change the generated text and the decisions of a model. From the viewpoint of emotion research, if pushing a direction that corresponds to the appraisal of controllability changes a decision, it is tempting to conclude that the model uses this appraisal to decide.

A behavioural effect alone, however, does not show that the direction acts **through the concept that names it**. The paper lists three reasons.

1. The rating that names the concept may not measure the variable that drives the behaviour.
2. A direction that is concept-selective under one intervention may lose its selectivity under another. Interchange and additive steering place the internal state in different regions.
3. Random directions are the usual null for steering, but they do not share the training procedure of the real direction. A real direction can beat random directions because of how it was trained rather than because of the concept.

The study therefore states what evidence a claim of concept-specific control needs, and collects each piece with a test that a direction **can fail**.

## The evaluation framework

<figure>
  <img src="/column-images/ssrn-behavioral-steering/framework-1600.webp" alt="Evaluation framework" />
  <figcaption><strong>Figure 1.</strong> The evaluation framework (Figure 1 of the paper). Five stages collect the evidence; the Selectivity–Effect Overlap Criterion at the bottom is decided from stages 1, 4 and 5.</figcaption>
</figure>

The Selectivity–Effect Overlap Criterion supports a direction as a causal control variable for a concept only if three checks succeed in order.

1. **Rating validity**: without intervention, the rating separates the two defining conditions and predicts the behaviour (the 95% interval of the AUC excludes 0.5).
2. **Selectivity**: at some dose of additive steering, the selectivity S(α), which measures how much only the target rating moves, beats both random directions and optimisation-matched nulls. These doses form the set A_S.
3. **Behavioural effect**: within A_S, the behavioural effect B(α) beats both null families.

The criterion is asymmetric. A pass is strong evidence for concept-specific control. A failure is not treated as evidence that the concept is unused.

The second pillar is the **optimisation-matched null direction**. It is trained with the same loss, data, learning rate and number of epochs as the real direction, and only the target labels are permuted. Comparing against these nulls separates the contribution of the concept from that of the training procedure. Each test uses 50 random directions and 50 optimisation-matched nulls.

<figure>
  <img src="/column-images/ssrn-behavioral-steering/task-1600.webp" alt="Two-phase decision task" />
  <figcaption><strong>Figure 2.</strong> The two-phase decision task (Figure 2 of the paper). After phase 1, the model rates controllability c and success expectation v on a 0–9 scale. In phase 2, the behavioural readout is the probability of switching servers after a lost packet.</figcaption>
</figure>

In phase 1, the model repairs a machine over 20 rounds by choosing one of three procedures. In the high-control condition the outcome depends on the choice. In the low-control condition the outcomes are copied from a paired high-control episode, so the number of successes is matched but the choice has no effect. In phase 2, with phase 1 kept in the context, the model routes packets through one of three servers over 12 rounds.

<div class="setup">

**Setup**

- Models: Qwen3-8B (thinking mode off) and OLMo-2-1124-7B-Instruct, both in bfloat16
- Intervention layer: decoder block 24 (Qwen3-8B) and block 21 (OLMo-2-7B, same relative depth)
- Direction learning: 60 episode triads; main analyses on one of five folds (192 training and 48 test interchange cases)
- Behavioural test: decisions after a lost packet in 40 held-out episodes (199 for Qwen3-8B, 198 for OLMo-2-7B)
- Nulls: 50 random and 50 optimisation-matched directions per test (smallest attainable p-value 1/51 = 0.020)

</div>

## Experiment 1: Interchange finds concept-selective directions

<p class="experiment-label">Experiment 1</p>

At the last token of the rating prompt, we exchanged only the component along the direction with that of another input and measured how much of the c and v rating differences moved (the transfer fraction F).

| Model | Direction | F_c | F_v |
|---|---|---|---|
| Qwen3-8B (5 folds pooled) | w_c¬v | 0.90 | 0.12 |
| Qwen3-8B (5 folds pooled) | w_v¬c | 0.04 | 0.87 |
| OLMo-2-7B (3 folds pooled) | w_c¬v | 0.90 | 0.07 |
| OLMo-2-7B (3 folds pooled) | w_v¬c | 0.05 | 0.90 |

The controllability direction w_c¬v carries almost all of the c difference and little of v. The success-expectation direction w_v¬c does the reverse.

<figure>
  <img src="/column-images/ssrn-behavioral-steering/interchange-nulls-1600.webp" alt="Interchange against optimisation-matched nulls" />
  <figcaption><strong>Figure 3.</strong> Interchange transfer F_c of the real direction against the mean and maximum of 50 optimisation-matched nulls. The Qwen3-8B value is from the main-analysis fold (0.883).</figcaption>
</figure>

The nulls reach a mean of 0.464 and a maximum of 0.714 in Qwen3-8B, and a mean of 0.527 and a maximum of 0.929 in OLMo-2-7B. None reaches the real direction (p_O = 0.020 in both). **Interchange at the rating prompt supports the concept attribution.**

## Experiment 2: Natural-amplitude interchange does not change the decision

<p class="experiment-label">Experiment 2</p>

Next, at every generated token of the phase-2 reasoning, we set the direction to the value it takes in the other control condition, either by shifting by the natural difference or by clamping the projection. The choice itself is read from an unsteered forward pass.

<figure>
  <img src="/column-images/ssrn-behavioral-steering/natural-amplitude-1600.webp" alt="Natural-amplitude interchange during generation" />
  <figcaption><strong>Figure 4.</strong> Change in switch probability under natural-amplitude interchange (Table 2 of the paper). No p-value falls below 0.09.</figcaption>
</figure>

For w_c¬v in Qwen3-8B, the shift changes the switch probability by −0.0002 (p = 1.00) and the clamp by +0.021 (p = 0.19). The behaviour itself barely depends on the control condition: the natural switch rates are 0.415 (high control) and 0.479 (low control) in Qwen3-8B, and 0.592 and 0.587 in OLMo-2-7B. The natural difference along the direction is not enough to move the decision.

## Experiment 3: Under additive steering, the directions are no more selective than the nulls

<p class="experiment-label">Experiment 3</p>

What about a larger push? We added the direction at α times its natural gap g and measured the rating selectivity S(α) at each dose. S = 1 means only c moves; S = 0 means c and v move equally.

<figure>
  <img src="/column-images/ssrn-behavioral-steering/selectivity-1600.webp" alt="Selectivity under additive steering" />
  <figcaption><strong>Figure 5.</strong> Selectivity S(α) under additive steering. The grey band is the range of the matched-null 95th percentile in Qwen3-8B at α = 0.26–1. OLMo-2-7B is shown as points at the doses reported in the text.</figcaption>
</figure>

For w_c¬v in Qwen3-8B, S is 0.412 at α = 0.26, 0.411 at 0.5 and 0.365 at 1. Each value beats all 50 random directions (p_R = 0.020). The optimisation-matched nulls, however, reach a 95th percentile between 0.575 and 0.599 at the same doses, giving p_O = 0.529, 0.569 and 0.686. At higher doses selectivity declines, to −0.007 at α = 8.

The same pattern holds for the second concept (w_v¬c in Qwen3-8B, S = 0.410 at α = 0.26, p_O = 0.510) and for the second model (w_c¬v in OLMo-2-7B, S = 0.406, p_O = 0.412). A_S is empty for every concept direction. **The selectivity seen under interchange does not survive additive steering.**

## Experiment 4: Behavioural effects beat random directions but not matched nulls

<p class="experiment-label">Experiment 4</p>

Because A_S is empty, the behavioural step of the criterion is not run, and behavioural effects are reported descriptively.

<figure>
  <img src="/column-images/ssrn-behavioral-steering/null-pvalues-1600.webp" alt="p-values against the two null families" />
  <figcaption><strong>Figure 6.</strong> For each test in the paper, the p-value against random directions (p_R, grey circles) and against optimisation-matched nulls (p_O, blue diamonds). Against random directions alone, many tests look significant.</figcaption>
</figure>

For w_c¬v in Qwen3-8B, B = −0.069 at α = 1 (p_R = 0.039, p_O = 0.059) and B = −0.214 at α = 8 (p_R = 0.020, p_O = 0.078). Compared only with random directions, the effect looks concept-specific, but two or three of the matched nulls reach the same size. In OLMo-2-7B the effects stay at or below 0.06 in absolute value up to α = 8, with the opposite sign to Qwen3-8B.

Across the 50 Qwen3-8B nulls, interchange transfer F_c and the behavioural effect are uncorrelated (r = −0.05). **Nulls that carry more of c do not move the decision more.**

## Experiment 5: Can the criterion be passed at all?

<p class="experiment-label">Experiment 5</p>

To check that the criterion is not simply impossible to pass, we built two positive controls in Qwen3-8B at block 24, at the decision prompt of phase 2.

- **Self-report control**: the model rates how likely it is to choose a different server than in the previous round. Without intervention, the mean rating is 1.57 after a lost packet and 1.59 after an arrived packet (p = 0.61), and the AUC for predicting a switch is 0.58 (95% interval [0.45, 0.70]). The model actually switches after 47.0% of lost packets and 4.3% of arrived packets, yet the rating does not track this. The control fails the validity step and is not evaluated further.
- **Rule control**: one sentence is added to the phase-2 task, stating that packets go through the same server as before (KEEP) or through a different one (ROTATE). In all 40 rating-test episodes the rating is 9.00 under ROTATE and 0.00 under KEEP; the switch probability is 1.00 and 0.28; the AUC is 0.90. Under interchange, w_p¬v transfers the full rule-rating difference (F_p = 1.00) and none of v (F_v = 0.00).

Under additive steering, the rule direction is **the first direction in the study that is selective against both null families**. At α = 1 it moves the rule rating by 2.84 points and v by 0.18, giving S = 0.880 against a null 95th percentile of −0.554. A_S = {0.26, 0.5, 1}, but the paper notes that the two lower doses enter only because the rule rating sits at 0 or 9 without intervention; only α = 1 is substantively selective.

## Experiment 6: The rule control still fails the behavioural step

<p class="experiment-label">Experiment 6</p>

<figure>
  <img src="/column-images/ssrn-behavioral-steering/rule-control-1600.webp" alt="Rule positive control" />
  <figcaption><strong>Figure 7.</strong> Rule positive control. (a) Behavioural effect B(α) by dose; the band marks A_S. Pushing at the choice position gives B ≤ 0.001 within A_S. (b) Interchange at the choice position. Of the 0.718 gap in switch probability, exchanging the full hidden state transfers 74%; exchanging only the component along the rule direction transfers less than 0.01%.</figcaption>
</figure>

Pushing on the generated tokens gives B = 0.002, 0.019 and 0.033 within A_S. At α = 1, seven random directions and thirty-five matched nulls reach the real effect (p_R = 0.392, p_O = 0.980). The behaviour moves clearly only outside A_S (B = 0.231 at α = 8).

Aligning the intervention with the choice readout does not help. Pushing only the last token before the choice gives at most B = 0.001 within A_S (p_R = 0.020, p_O = 0.588). Pushing both the generated tokens and the choice position gives p_R = 0.647 and p_O = 1.000.

Interchange at the choice position shows where the rule information is. Exchanging the whole hidden state between the ROTATE and KEEP prompts transfers 74% of the switch-probability difference. Exchanging only the component along the direction that carries the rule rating transfers less than 0.01% (p = 0.020 against random directions, p = 0.412 against matched nulls). **The rule information that drives the choice is present at the choice position, but not along the direction that carries the rule rating.** The rule demonstrably determines the behaviour, and the criterion still fails.

## What we know and what we don't

Where each direction stopped in the criterion (from Table 3 of the paper):

| Direction | Model | Validity | Selective doses A_S | Not met at |
|---|---|---|---|---|
| w_c¬v (controllability) | Qwen3-8B | pass | empty | selectivity |
| w_v¬c (success expectation) | Qwen3-8B | pass | empty | selectivity |
| w_c¬v (controllability) | OLMo-2-7B | pass | empty | selectivity |
| w_sw (switch self-report) | Qwen3-8B | fail | – | validity |
| w_p¬v (rule) | Qwen3-8B | pass | {0.26, 0.5, 1} | behaviour |

The study establishes three things.

- **The forms of evidence for concept attribution dissociate.** Rating validity, selectivity under interchange, selectivity under additive steering and behavioural specificity each held for some variable under some intervention, but never together for one variable at the same doses.
- **Random directions overstate behavioural specificity.** Against nulls trained by the same procedure, the behavioural effect of the controllability direction is not concept-specific.
- **A representation that reports a variable need not be the one that mediates behaviour.** The rule information was in the full hidden state at the choice, but not in the single direction that carried the rule rating.

The paper does not conclude that controllability is not a causal variable of the decision. A failure of the criterion is not evidence of absence. The variable may be used through a multi-dimensional or non-linear representation; a direction found at the rating position may not be the same coordinate at the reasoning and choice positions; attention can re-supply a rule stated in the prompt; and the meaning of a direction may depend on the intervention operator.

There are limits. The study covers two instruction-tuned models of 7B and 8B parameters and one task, and the rule variable is stated in the prompt rather than arising from experience. Every intervention acts on one linear direction at one layer. The ratings are proxies for the concepts, and S is unstable when the target rating hardly moves. Because the positive control did not pass, it is not yet shown that the criterion can be passed by any variable, and its false-negative rate is unknown. With 50 nulls per family, the smallest attainable p-value is 0.020.

Next, we plan to apply the criterion with multi-dimensional and multi-layer interventions, to adopt a selectivity measure that requires a minimum movement of the target, and to test larger models and tasks in which the concepts matter more for the decision.

This paper is a preprint and has not been peer-reviewed. Code, prompts and result files: [github.com/keito-git/concept-direction-validity](https://github.com/keito-git/concept-direction-validity).
