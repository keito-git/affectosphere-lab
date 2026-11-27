---
title: "Do Language Models Really Differ in How They Represent Emotion?"
subtitle: "Large Language Models Share an Affective Geometry, but Apparent Differences Largely Reflect Measurement Depth"
date: "2026-11-27"
excerpt: "We read emotion representations from every layer of 38 open language models and asked whether the models differ, or only the places where they are read. The geometry is shared; most of the apparent differences come from measurement depth. A walk-through of our SSRN preprint."
readingMinutes: 13
showImage: false
image: "/column-images/ssrn-shared-affective-geometry/verdicts.png"
imageAlt: "Between-model standard deviation of five indices against the equivalence margin. The two geometric indices fall well below the margin; the three linear decodability indices lie above it at the representative layer."
authors:
  - name: "Keito Inoshita"
    url: "/en/about/"
    affiliation: "Kansai University"
tldr: "Comparisons of emotion inside LLMs usually read each model at one conventionally chosen layer. We read 38 models from 9 lineages (0.44B–33B parameters) at every layer, under three stimulus conditions, and defined universality as a between-model standard deviation below a margin calibrated on human cross-linguistic variation (Δ = 0.136). The geometry is shared: orthogonality between the dimensional (VAD) and categorical subspaces and circularity pass the equivalence test across a 75-fold range of size. Linear decodability looks model-specific at the representative layer, but aligning each model at its own peak depth removes 61.0% of the between-model SD for arousal. Separation already exists at the embedding layer, while decodability appears only after transformer computation. The intervention analysis is exploratory and its sign depends on where the vector is injected."
links:
  - label: "Preprint (SSRN)"
    url: "https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7551120"
citation: |
  @misc{inoshita2026affectgeometry,
    title        = {Large Language Models Share an Affective Geometry, but Apparent
                    Differences Largely Reflect Measurement Depth},
    author       = {Inoshita, Keito},
    year         = {2026},
    howpublished = {SSRN preprint, abstract id 7551120}
  }
---

<div class="teaser">
<div>

Shared

**Geometry is common** to 38 models. Between-model SD is 0.053 for orthogonality and 0.049 for circularity, against a margin of 0.136.

</div>
<div>

Depth

**Differences are mostly depth.** Aligning each model at its peak removes 61.0% of the between-model SD in arousal decodability.

</div>
<div>

Dissociated

**Separation precedes computation.** Subspaces are already separated at layer 0; linear decodability appears only after the forward pass.

</div>
</div>

## Are the models different, or the measurements?

Evidence has been accumulating that LLMs share some structure for emotion: linear emotion directions, a valence–arousal circumplex in middle layers, similar representational distance matrices across families. However, these studies do not share a measurement protocol. They probe different layers, use different stimuli and use different criteria for "similar".

This matters because the best probing layer moves between models and datasets. If one model concentrates its affective signal at 40% depth and another at 80%, reading both at the same conventional layer will make them look different even when their representations are not.

So this study asks a precise question: **when affective geometry appears to differ between models, is that a real representational difference, or a difference in where the models were read?** Reading position is treated as an experimental variable rather than a fixed choice.

## How the analysis works

<figure>
  <img src="/column-images/ssrn-shared-affective-geometry/pipeline-1600.webp" alt="Analysis pipeline" />
  <figcaption><strong>Figure 1.</strong> The analysis pipeline. Last-token activations are taken from every layer, decomposed into continuous (VAD) and discrete subspaces, compared by principal angles, read at three positions, and tested for equivalence against a margin from human data.</figcaption>
</figure>

Four quantities are computed for every model, layer and stimulus condition.

1. **Orthogonality (orth).** The smallest principal angle between the VAD subspace and the discrete-category subspace, divided by π/2. Near 1 means the two are independent; near 0 means they are nearly collinear.
2. **Circularity (CI).** How circumplex-like the stimuli look when projected into the VAD subspace.
3. **Linear decodability (R²).** How well linear regression recovers valence, arousal and dominance from the activations.
4. **Interaction excess.** Whether the geometry differs between high- and low-arousal stimuli beyond what a random split produces.

**Universality** is defined as an equivalence problem. An index is universal when the between-model standard deviation is shown to be smaller than a margin Δ. The margin, Δ = 0.136, is derived from human cross-linguistic variation in emotion semantics and was fixed before the confirmation data were opened. Stimuli were split 50/50 into a discovery set, used only to set up procedures, and a confirmation set, examined once.

<div class="setup">

**Setup**

- Models: 38 open-weight LLMs from 9 lineages (Qwen3 / Qwen3-Swallow, AllenAI OLMo-style, Apertus, Granite 4.2, LLM-jp-4, GPT-OSS, GLM-4.7-Flash, Gemma 4, QwQ / Mistral Small), 0.44B–33.2B parameters
- Stimuli: EmoBank sentences without emotion words (condB, VAD ratings); 171 emotion words in a fixed frame (word templates); 1,131 items in both EmoBank and SemEval-2007 (combined set, VAD and six emotion intensities)
- Readout: last token, every layer, PCA-compressed
- Test: TOST equivalence test (α = 0.05) on the between-model SD, Benjamini–Hochberg correction

</div>

## Experiment 1: Is the geometry shared?

<p class="experiment-label">Experiment 1</p>

<figure>
  <img src="/column-images/ssrn-shared-affective-geometry/verdicts-1600.webp" alt="Primary universality verdicts" />
  <figcaption><strong>Figure 2.</strong> Between-model SD for five indices at the representative layer (word templates). The dashed line is the margin Δ. The two geometric indices pass; the three decodability indices do not.</figcaption>
</figure>

Orthogonality (SD 0.053, p = 6.26 × 10⁻¹⁰) and circularity (SD 0.049, p = 5.13 × 10⁻¹¹) both pass the equivalence test. Their spread across models is well under the margin, across a 75-fold range of parameter count. Mean pairwise RDM correlation between models is 0.747.

At the same layer, all three linear decodability indices fail: R²_V 0.197, R²_A 0.316, R²_D 0.259, all above 0.136. Read naively, this says the models share the shape of the emotion space but differ in how readable it is. The later experiments show that most of the second half is a depth effect.

A saturation control checks that the geometric result is not an artifact of subspace size. Random subspaces drawn in the same PCA space give orthogonality 0.691 for 6-dimensional subspaces and 0.038 for 47-dimensional ones. The observed values sit far from both.

<figure>
  <img src="/column-images/ssrn-shared-affective-geometry/saturation-1600.webp" alt="Saturation control" />
  <figcaption><strong>Figure 3.</strong> Observed orthogonality compared with random subspaces of the two dimensionalities used. The observed 0.467 and 0.460 lie well outside both random ranges, so the value is not an artifact of subspace size.</figcaption>
</figure>

On the combined set, mean orthogonality is 0.460 with SD 0.039 (universal, p = 2.40 × 10⁻¹⁴). The pre-registered decision tree, which sorts models into dimensional or discrete types, left 36 of 38 models (combined set) and 32 of 38 (word templates) inconclusive, because they concentrate near 0.460, between the 0.15 and 0.50 thresholds. A Gaussian mixture prefers a single component and a dip test finds no bimodality. **Models do not split into "dimensional" and "discrete" types; they share an intermediate relation.** The interaction excess was inconclusive (p = 0.233).

## Experiment 2: Are decodability differences real?

<p class="experiment-label">Experiment 2</p>

We aligned each model at its own peak layer (chosen on the discovery set) and recomputed the between-model SD on the confirmation set.

<figure>
  <img src="/column-images/ssrn-shared-affective-geometry/alignment-1600.webp" alt="Peak alignment" />
  <figcaption><strong>Figure 4.</strong> Between-model SD before and after per-model peak alignment (confirmation set). Alignment reduces the spread for every decodability index and for circularity, but not for orthogonality.</figcaption>
</figure>

| Index | Raw SD | Aligned SD | Change |
|---|---|---|---|
| R²_V | 0.042 | 0.031 | −25.9% |
| R²_A | 0.181 | 0.071 | −61.0% |
| R²_D | 0.105 | 0.082 | −22.0% |
| CI | 0.020 | 0.016 | −19.8% |
| orth | 0.035 | 0.043 | +20.2% |

The arousal reduction is 61.0% on the confirmation set, larger than the 30.7% seen on the discovery set, so it is not a discovery-set artifact. Orthogonality does not benefit from alignment; its spread was already small. This asymmetry is the core of the paper: **the shape of the geometry is stable across depth, while decodability peaks at model-specific depths.** Peak depth itself varies widely (SD 0.18, range 0.15 to 1.00 in relative depth).

All 38 models follow a similar single-peaked trajectory across layers. The median pairwise correlation of the depth profiles over 703 model pairs is 0.856 for R²_V and 0.847 for R²_A.

## Experiment 3: Does the verdict follow the reading position?

<p class="experiment-label">Experiment 3</p>

<figure>
  <img src="/column-images/ssrn-shared-affective-geometry/readout-1600.webp" alt="Readout positions" />
  <figcaption><strong>Figure 5.</strong> Between-model SD of arousal decodability at different reading positions. The two stimulus conditions use different items and should not be compared with each other directly.</figcaption>
</figure>

For EmoBank condB read at a common relative depth of 0.60, all three decodability indices pass (SD 0.074, 0.033 and 0.029 for V, A and D). Arousal moves from not universal at the representative layer to universal under both alignment procedures. Word templates stay above the margin at both positions (0.316 and 0.151), so, as the paper puts it, the change of verdict follows the reading condition rather than the reading position.

The verdicts are also sensitive to the margin. Orthogonality and circularity stay universal for all executed margins from 0.136 to 0.172 and at the cap of 0.20, but the smallest variant (Δ_B = 0.0397) makes every index not universal.

The robustness has limits. When one lineage is held out while choosing the common depth, valence stays below the margin in 8 of 8 folds, but arousal exceeds it in 3 of 8 and dominance in 2 of 8. **Valence universality is robust; arousal and dominance are fragile.**

## Experiment 4: Is it specific to emotion?

<p class="experiment-label">Experiment 4</p>

Seven models were run on the same EmoBank sentences with emotion labels replaced by non-affective surface features (sentence length, word length, punctuation density and six topic clusters).

<figure>
  <img src="/column-images/ssrn-shared-affective-geometry/control-1600.webp" alt="Non-emotion control" />
  <figcaption><strong>Figure 6.</strong> Linear decodability for emotion labels and for the surface-feature control at depth 0.60 (7 models). The control is easier to decode, yet dimension–discrete separation is higher under emotion labels in every model.</figcaption>
</figure>

The control condition also passes the equivalence test for orthogonality, so a conserved subspace arrangement is not unique to emotion. Its degree is different, however: all 7 of 7 models show higher separation for emotion than for the control (two-sided binomial p = 0.016), even though the control is more decodable (0.434 vs 0.233). The paper reads this as a gradient, not as affective exclusivity.

The embedding layer gives a second clue. On word templates, orthogonality at layer 0 is about the same as at depth 0.60 (median ratio 1.00, Wilcoxon p = 0.365), while all R² values are negative at layer 0 in all 38 models. On news headlines (6 models), layer-0 orthogonality is higher than after the forward pass in 6 of 6. **Separation is already present in the input space; linear decodability appears through computation.** The paper notes that this reading comes from comparing layers and was not tested by manipulating the embedding layer.

## Experiment 5: Do the directions act on the output?

<p class="experiment-label">Experiment 5</p>

This analysis is **exploratory**: its protocol amendments were not version-controlled. Six models from six lineages (1.5B–8B) were selected, and one was excluded for architectural reasons. In the remaining five, an estimated valence direction was added at relative depth 0.60, and the shift in next-token output was compared with a random direction of the same norm.

<figure>
  <img src="/column-images/ssrn-shared-affective-geometry/patching-1600.webp" alt="Activation patching" />
  <figcaption><strong>Figure 7.</strong> Left: difference between the valence direction and a random direction at six injection ratios (stimulus-last position). Right: the same direction at α = 0.5 injected at two positions.</figcaption>
</figure>

At the stimulus-last position, the valence direction beats the random direction in 5 of 5 models at every ratio (at α = 0.5, mean +0.4837, one-sided paired t p = 0.0293). Injected at the prompt-last position instead, the same direction gives a negative mean (−0.5818) and a positive sign in only 1 of 5 models. The evidence is thin: dropping one of two specific models makes the t-test non-significant.

Geometric similarity also does not predict functional similarity. Across 15 model pairs, the correlation between RDM similarity and similarity of intervention effects is r = −0.103 (p_perm = 0.733). With 15 pairs this is a null result, not proof of independence.

Correspondence with human structure exists at a coarse level. The mean LLM RDM correlates with the human RDM (Mantel r = 0.348, p = 0.011), and mean per-model RSA is 0.390. The cross-linguistic structure is not reproduced: the pre-registered colexification coefficient is null (β = −0.029, p = 0.944).

## What we know and what we don't

The study supports three conclusions.

- The relational geometry of emotion (orthogonality, circularity, the intermediate dimensional–discrete relation) is shared across 38 LLMs under a margin calibrated on human data.
- Much of the apparent difference in linear decodability comes from reading models at different depths. Measurement depth is part of the claim, not a technical detail.
- Separation and decodability are different properties: the first is already present at the embedding layer, the second appears after computation.

There are clear limits. The margin is taken from one colexification dataset and may be noise-inflated, and the smallest margin variant reverses every verdict. The non-emotion control covers only 7 models. The combined set consists only of news headlines. Arousal and dominance universality do not survive every lineage exclusion. The intervention analysis is exploratory, covers 5 models and a next-token readout, and was not tested above 8B. The depth-alignment interpretation is correlational and has not been verified causally.

Future work should test the geometry–function relation on a larger and more varied set of models, estimate the margin from broader cross-linguistic data, and extend the control to more non-affective dimensions.
