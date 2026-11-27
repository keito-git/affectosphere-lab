---
title: "Is Emotion Steering About Emotion, or About Where the Direction Sits?"
subtitle: "What Looks Like Emotion Steering Is Largely the Geometry of the Representation Space"
date: "2026-11-27"
excerpt: "A claim that adding an emotion direction to a language model changes its output rests on a comparison: the direction moved the output more than a control did. Using a pre-registered procedure, we show that where the control is drawn from changes the verdict. A walk-through of our SSRN preprint."
readingMinutes: 12
showImage: false
image: "/column-images/ssrn-steering-is-geometry/pipeline.png"
imageAlt: "How the reference set decides the verdict. Activation variance is concentrated in a few principal components; a direction judged specific against full-space controls becomes indistinguishable from controls drawn from the same subspace."
authors:
  - name: "Keito Inoshita"
    url: "/en/about/"
    affiliation: "Kansai University"
tldr: "Saying that a steering direction is emotion-specific is a comparison against control directions. The usual control is drawn uniformly from the whole representation space. But activation variance is concentrated in a few principal components, so any direction in that subspace moves the output more, whatever it means. Controls drawn from inside the subspace moved the output about twice as much as full-space controls, and this held in three model families and at four subspace widths. A valence direction built from human ratings beat the full-space control and was indistinguishable from the in-subspace control."
links:
  - label: "Preprint (SSRN)"
    url: "https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7633458"
  - label: "Code"
    url: "https://github.com/keito-git/nativeaffect-prereg"
citation: |
  @misc{inoshita2026steeringgeometry,
    title        = {What Looks Like Emotion Steering Is Largely the Geometry of the
                    Representation Space},
    author       = {Inoshita, Keito},
    year         = {2026},
    howpublished = {SSRN preprint, abstract id 7633458}
  }
---

<div class="teaser">
<div>

Floor

Controls drawn inside the subspace move the output **about 1.8–2.4 times** as much as full-space controls (confirmation half, all four layers).

</div>
<div>

Generalize

The gap reproduces in **three model families and four subspace widths** (ratios 1.56–3.77).

</div>
<div>

Reference

A valence direction built from human ratings **beats the full-space control in all four layers** and **beats the in-subspace control in none of 16 cells**.

</div>
</div>

## What is an "emotion-specific" direction compared with?

Adding an estimated direction to the internal state of a language model changes what it writes. This procedure, activation steering, is now widely used to control how models express emotion.

Every such result is a comparison. A direction is called emotion-specific because injecting it changes the output more than injecting a control direction. Estimation and injection have been refined in many ways, but **how the control direction is chosen** has received almost no attention. Most studies still draw it uniformly from the whole representation space.

That default is not neutral. The activations of a language model concentrate most of their variance in a small subspace. A direction lying in that subspace moves the output more than a uniformly drawn direction, whatever it means. The effect of a direction's content therefore cannot be separated from the effect of its position.

In this study we ask what a claim of directional specificity requires, and we build a procedure to audit it.

## Writing the claim as a comparison with a reference set

<figure>
  <img src="/column-images/ssrn-steering-is-geometry/pipeline-1600.webp" alt="Why the reference set decides the claim" />
  <figcaption><strong>Figure 1.</strong> Overview figure from the paper. (a) Activation variance is concentrated in a few components. (b) The four reference sets differ in where in the space they may lie. (c) The same direction is judged specific or not depending on which reference set it is compared against.</figcaption>
</figure>

We define specificity as a property of a pair: a candidate direction u and a reference set R. It is the probability that u changes the output more than a direction from R, minus the probability that it changes it less. Cliff's δ estimates this quantity.

Three conditions follow, and they must hold together.

1. **Report the estimation procedure and the seed.** Procedures with equal predictive accuracy can return nearly orthogonal directions.
2. **Report the injection layer and position.** The sign of the effect depends on both.
3. **Draw the reference set from the same region as the candidate.** Otherwise content and position are confounded.

For Condition 3 we built four controls, ordered by the confound each removes.

| Control | Construction | What it holds fixed |
|---|---|---|
| Full-space random | uniform on the unit sphere of the 2048-d space | nothing |
| Axis-orthogonal | full-space draw, orthogonalized against the candidate | subspace variance |
| In-plane random | uniform within the span of the top 10 PCs | the dominant subspace |
| VMIC | in-plane draw, coefficients weighted by each PC's standard deviation | the dominant subspace and the variance spectrum |

The outcome is the Jensen–Shannon divergence (JSD) between next-token distributions before and after the intervention. It needs no auxiliary judge, so nothing from the direction-finding step re-enters the evaluation. The stimuli were split into a discovery half and a confirmation half before any confirmatory result was seen.

## Experiment 1: How much harder is an in-subspace control?

<p class="experiment-label">Experiment 1</p>

<div class="setup">

**Setup**

- Model: Apertus-v1.1-1.5B (d = 2048), layers 5 / 7 / 10 / 12
- Intervention stimuli: 40 sentences, 20 emotion categories (10 positive, 10 negative) × 2 templates; 20 per half
- Subspace: top 10 principal components (a uniform direction falls there with probability 10/2048 ≈ 0.0049)
- Strength: five relative strengths from 0.01 to 0.20; 0.05 is primary
- Registered criterion (C1): q < 0.05 in at least 3 of 4 layers, and a ratio of at least 1.5 in all four

</div>

<figure>
  <img src="/column-images/ssrn-steering-is-geometry/floor-ratio-1600.webp" alt="In-plane vs full-space floor" />
  <figcaption><strong>Figure 2.</strong> Left: output change (JSD) for each control on the confirmation half. Right: ratio of the in-plane to the full-space floor. The dashed line is the registered bar of 1.5.</figcaption>
</figure>

C1 held in all four layers of the confirmation half. The ratios were 2.429, 1.935, 1.795 and 1.796 at layers 5, 7, 10 and 12, against 2.731, 2.424, 1.936 and 1.982 on the discovery half.

The reason is geometric. An in-plane direction lies in the top-10 span with certainty, while a full-space direction does so with probability 0.0049. Swapping the control alone raises the bar about twofold before any question of meaning is asked.

The variance-weighted VMIC exceeded the full-space control by factors of 1.87 to 2.38, but it was not always harder than the unweighted in-plane control. The paper therefore does not defend VMIC as the hardest floor. It defends it as the control that puts the candidate and the reference set under the same variance spectrum.

## Experiment 2: Does this hold across models and subspace widths?

<p class="experiment-label">Experiment 2</p>

Experiment 1 used one model and fixed the subspace at rank ten. Both concern the control, not any candidate, so they can be tested without extracting directions. We measured three model families at four depths each and swept the rank k over 2, 5, 10 and 20.

<figure>
  <img src="/column-images/ssrn-steering-is-geometry/cross-model-1600.webp" alt="Floor ratio across models and subspace widths" />
  <figcaption><strong>Figure 3.</strong> Ratio of the in-plane to the full-space floor (α = 0.05, averaged over four depths). Every point lies above a ratio of 1.</figcaption>
</figure>

The in-plane floor exceeded the full-space floor in every model and at every rank, by factors of 1.56 to 3.77. In SmolLM2-1.7B the gap is about twice that of the main model. The full-space control is too permissive in all three families.

The ratio generally falls as the subspace widens, though not strictly. SmolLM2 and Phi-3-mini both peak at k = 5 and reach their minimum at k = 20. Rank ten is not a special point; it is one position on a continuum, at 0.68 to 0.72 of explained variance.

<figure>
  <img src="/column-images/ssrn-steering-is-geometry/vmic-ratio-1600.webp" alt="VMIC over in-plane ratio" />
  <figcaption><strong>Figure 4.</strong> Ratio of VMIC to the unweighted in-plane floor. It is mostly above 1 in Apertus and below 1 everywhere in SmolLM2 and Phi-3-mini.</figcaption>
</figure>

We did not expect this. Matching a control to the variance spectrum is not the same as making it harder.

## Experiment 3: A direction whose content is known

<p class="experiment-label">Experiment 3</p>

Next we tested **a direction whose emotional content is established independently**, rather than an extracted axis. It is a ridge regression from the activations of 287 GoEmotions validation sentences onto published lexical norms (human valence ratings). This direction is known to carry valence.

- C2a: does it move the output more than the full-space control?
- C2b: does it move the output more than the in-plane control?

If C2a holds and C2b fails, the full-space comparison cannot tell an emotion-specific effect from the generic advantage of sitting in the dominant subspace.

<figure>
  <img src="/column-images/ssrn-steering-is-geometry/reference-direction-1600.webp" alt="Reference direction against two controls" />
  <figcaption><strong>Figure 5.</strong> Cliff's δ of the human valence direction (confirmation half, every layer × strength cell). Left: against the full-space control. Right: against the in-plane control.</figcaption>
</figure>

C2a held in all four layers of the confirmation half, with δ at the primary strength of +0.25, +0.50, +0.80 and +0.75, all at q < 0.05.

C2b showed no significant advantage in any of the 16 cells. More than that, δ was negative in 14 of 16 cells and reached −1.00. The largest value was +0.10 at layer 10 (q = 1.000). The direction is displaced below the floor, not balanced near zero.

After the registered analysis, we also compared it with VMIC. δ was negative in all 32 cells across both halves. This comparison was not pre-registered and is supplementary.

A direction cannot lose its meaning by being compared with something else. The difference between the two panels is a property of the comparisons. The common control registers this direction as clearly effective; a control drawn from the same subspace cannot tell it apart from an arbitrary orientation in that subspace.

## Experiment 4: What about the extracted axes?

<p class="experiment-label">Experiment 4</p>

We extracted three axes per layer by independent component analysis (ICA) and compared each with VMIC (C4, 48 cells). The registered criterion was that at most 2 of the 12 primary-strength cells reach significance.

One primary cell did (layer 5, axis 2, δ = +0.45). Across all 48 cells, 8 were significant, all at the two largest strengths, and 3 of those had δ = +0.00. C4 was satisfied.

As registered, this shows indistinguishability from the in-subspace control, not the absence of an effect. With 20 stimuli per half, power is limited. The extracted axes were never compared with the full-space control, so we make no claim about that comparison.

## Experiment 5: Checking the instruments themselves

<p class="experiment-label">Experiment 5</p>

Two supporting analyses are also reported.

The first is a secondary metric of how consistently the output moves. It failed its positive control (separating the human valence direction from its floor) at all four layers, so, as registered, it was withdrawn. Its numerical agreement with the JSD results is not read as corroboration.

The second asks how much of each extracted axis lies inside the human valence–arousal–dominance (VAD) subspace.

<figure>
  <img src="/column-images/ssrn-steering-is-geometry/estimator-1600.webp" alt="Overlap under two estimators" />
  <figcaption><strong>Figure 6.</strong> Overlap of the same 12 axes with the VAD subspace under two estimators (log scale): 0.065–1.81% with ridge regression, 7.9–22.1% with covariance principal components.</figcaption>
</figure>

The registered criterion (at least 10 of 12 cells below 5%) held in all 12 cells under ridge regression. Under covariance principal components, the same axes gave 7.9–22.1%, more than an order of magnitude larger. Reporting either estimator alone would license a confident statement in the opposite direction from the other. Changing the seed did not move the conclusion; changing the estimator did. This is Condition 1 on real data. This analysis estimates the subspace from all sentences, so it carries no out-of-sample information.

## What we found, and what remains open

Three findings stand out.

- Specificity must be written as a property of **a direction and a reference set together**, not of the direction alone. Three conditions follow: the estimator and seed, the injection site, and the region the reference set is drawn from.
- The common full-space control is too permissive. The confound reproduces across three model families and four subspace widths.
- Even a direction known to carry valence beats the full-space control and is indistinguishable from the in-subspace control. Effects attributed to emotional meaning may not be separable from the geometry the direction occupies.

There are limitations. The semantic and axis-level analyses use one model, one language and one extraction, so their values are not general constants; only the control-confound analysis is shown to generalize. Two registered criteria treat the absence of a significant excess as a pass, and no equivalence margin was fixed in advance. The VMIC comparison was not pre-registered. A registered signed readout, meant to recover the sign of the effect, did not meet its criterion, so the sign is unresolved. No non-emotion direction was tested, so whether the extracted axes are specifically emotional or merely high-variance remains open.

Next steps are to select candidate directions by output sensitivity rather than representational stability, and to apply the procedure to attributes beyond emotion.

The pre-registration with its amendment history, the analysis code and the stimuli are at [github.com/keito-git/nativeaffect-prereg](https://github.com/keito-git/nativeaffect-prereg). This post describes a preprint that has not been peer reviewed.
