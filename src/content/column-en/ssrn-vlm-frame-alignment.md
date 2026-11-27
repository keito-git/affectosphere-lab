---
title: "Can Panel Layout Make a VLM Describe the Wrong Person?"
subtitle: "Frame Alignment Redirects Person-State Attribution Toward the Wrong Person in Vision-Language Models"
date: "2026-11-27"
excerpt: "When a short video is given to a VLM as one image of stacked frames, does the layout of the frames change whose expression the model reports? A walk-through of our SSRN preprint."
readingMinutes: 13
showImage: false
image: "/column-images/ssrn-vlm-frame-alignment/overview.png"
imageAlt: "The five stages of the analysis framework: generate rotating two-frame scenes, shift frame 2, vary the reference and badges, query the VLM, and compute the error measures."
authors:
  - name: "Keito Inoshita"
    url: "/en/about/"
    affiliation: "Kansai University"
tldr: "In a two-frame panel where three people rotate by one position, another person moves into the image column the target used to occupy. We shifted frame 2 horizontally in graded steps and changed nothing else. In Qwen3-VL-8B, column alignment raised reports of the person now standing in the target's former column, and the error fell gradually with the shift. When asked for place and state in one answer, the model reported the other person's place and state together. Badges that stay with each person reduced the error, and badges that stay with each position raised it sharply. InternVL3.5-14B showed no alignment effect, but the badges steered it in the same directions."
links:
  - label: "Preprint (SSRN)"
    url: "https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7685781"
citation: |
  @misc{inoshita2026framealignment,
    title        = {Frame Alignment Redirects Person-State Attribution Toward the Wrong Person
                    in Vision-Language Models},
    author       = {Inoshita, Keito},
    howpublished = {SSRN preprint, abstract id 7685781},
    year         = {2026}
  }
---

<div class="teaser">
<div>

Align

Aligned columns raise the error. In Qwen3-VL-8B, the alignment effect under a positional reference is **+0.16 to +0.21**.

</div>
<div>

Replace

The error is not a misread expression but **the wrong person**. In one joint answer, the other person's place and state come back together (0.14 vs 0.00).

</div>
<div>

Steer

Badges move the error. Position-fixed badges: **0.18 → 0.63**. Person-fixed badges: 0.18 → 0.07.

</div>
</div>

## Stacked frames blur who is where

One way to let a vision-language model (VLM) read a short video is to arrange several frames as panels in a single image. An image model can then handle time without training on video.

To describe how a person changes over time, the model must first find the same individual in each frame and then report that individual's state. The paper calls this step **temporal person-state attribution**. Errors here are hard to notice, because the reported state is a valid state of someone else in the scene.

When frames are stacked vertically, the same horizontal position in each frame falls in the same image column. If people move, one column can show the target in frame 1 and another person in frame 2. Our question is whether this shared column acts as a cue for "same person" and pulls the answer toward one predictable wrong person.

## The analysis framework

<figure>
  <img src="/column-images/ssrn-vlm-frame-alignment/overview-1600.webp" alt="Flow of the attribution analysis framework" />
  <figcaption><strong>Figure 1.</strong> The five stages of the framework (figure from the paper): scene generation, column-overlap manipulation, reference and cue manipulation, queries, and measures.</figcaption>
</figure>

<figure>
  <img src="/column-images/ssrn-vlm-frame-alignment/stimulus-1600.webp" alt="One schematic scene in the aligned and shifted layouts" />
  <figcaption><strong>Figure 2.</strong> One schematic scene (figure from the paper). The dashed band marks the column of the target T in frame 1. (a) In the aligned layout, the other person O stands in this column in frame 2. (b) Frame 2 is shifted by one slot.</figcaption>
</figure>

Each scene has three people who all rotate by one position in frame 2. The other person O then stands at the position the target T held in frame 1, which we call the origin. The question asks for T's state in frame 2. Reporting O's state is an **origin error**, and its rate is E.

The framework has five stages.

1. **Scene generation.** The same scene logic is rendered with schematic figures and with real face photographs (KDEF). A static control without rotation is also generated.
2. **Column-overlap manipulation.** Only frame 2 is shifted by s slots. At s = 0 the columns align fully; at s = 1 they no longer overlap. People, positions and states stay fixed. The alignment effect is E(s=0) − E(s=1). Two controls shift both frames together or place them side by side.
3. **Reference and cue manipulation.** Definition A names the target by position ("the person in the left position in frame 1"). Definition B fixes the individual in words ("the same individual even if they move"). Definition C is a role: whoever stands at that position in each frame. Visible badges either stay with each person or stay with each position.
4. **Queries.** Separate questions ask for the place or the state. A joint query asks for both in one answer. Local questions check that the expressions are read correctly.
5. **Measures and validity.** In joint answers, J_old is the rate of the old place with O's state (the whole other person), and J_cor the rate of the correct place with O's state. Models that cannot read the expressions well enough are reported only descriptively.

All intervals are 95% bootstrap intervals with 10,000 resamples.

## Experiment 1: Does column alignment raise the error?

<p class="experiment-label">Experiment 1</p>

<div class="setup">

**Setup**

- Model: Qwen3-VL-8B-Instruct (main model), greedy decoding
- Studies: S1–S3 (schematic, 216 scenes each) and S5 (photographs, 216 scenes)
- Comparison: s = 0 vs s = 1, definition A vs definition B

</div>

<figure>
  <img src="/column-images/ssrn-vlm-frame-alignment/align-effect-1600.webp" alt="Alignment effect under definitions A and B" />
  <figcaption><strong>Figure 3.</strong> Alignment effect E(s=0) − E(s=1) with 95% intervals. With schematic people the effect appears only under the positional definition A and is near zero under B. With photographs (S5) it remains under B.</figcaption>
</figure>

Column alignment raised the origin error in every study. With schematic people (S1–S3), the effect under A was +0.21, +0.16 and +0.21, and under B it was close to zero.

With photographs the pattern changed. In S5 the effect was +0.18 under A and +0.17 under B, and the interaction was +0.01 [−0.07, 0.09]. Fixing the individual in words lowered the overall error but did not remove the alignment effect. Local and static accuracies in S5 were 0.90 and 0.94, so a general failure to read the scenes cannot explain the effect. With three sampled answers per prompt, the effects were +0.21 under A and +0.17 under B.

## Experiment 2: Graded shifts

<p class="experiment-label">Experiment 2</p>

<figure>
  <img src="/column-images/ssrn-vlm-frame-alignment/dose-1600.webp" alt="Origin error under graded shifts" />
  <figcaption><strong>Figure 4.</strong> Origin error against the shift of frame 2: S4 with schematic people (five levels, left) and S5 with photographs (three levels, right). The bootstrap bands of the paper's figure are omitted.</figcaption>
</figure>

In S4, the error under A fell from 0.52 at s = 0 to 0.30 at s = 1, with a slope of −0.23 [−0.31, −0.16] per slot. Under B it stayed low, with a slope of −0.03 [−0.07, 0.01]. Most of the decline occurred between s = 0.25 and s = 0.5, as the frames lost about half of their column overlap.

In S5, both curves declined with the shift, and the curve under B stayed above zero at every level. Accuracy under the role definition C also fell from 0.86 to 0.76, so reading the frame-2 position was itself easier in the aligned layout.

The size of the effect depended on the horizontal offset of frame 1, but its direction was the same for both offsets in both studies.

## Experiment 3: Separating the geometric factors

<p class="experiment-label">Experiment 3</p>

<figure>
  <img src="/column-images/ssrn-vlm-frame-alignment/controls-1600.webp" alt="Geometric and wording controls" />
  <figcaption><strong>Figure 5.</strong> Alignment effect under definition A for the geometric and wording controls, with 95% intervals. Shifting both frames together gives no effect, and the side-by-side format gives a much smaller one.</figcaption>
</figure>

Shifting both frames together keeps them aligned with each other and only moves their absolute position. This changed the error by −0.02, whereas shifting frame 2 alone changed it by +0.16. The effect follows the relative alignment of the frames, not the absolute position of frame 2.

Placing the same frames side by side lowered the effect to +0.06, a difference of +0.14 [0.05, 0.24] from the stacked format. The two formats also differ in aspect ratio, so this comparison does not isolate column sharing alone. It does show that the large effect requires the stacked format in which the frames share columns.

The last row checks whether definition B worked only because it is longer. Adding a neutral sentence of similar length to A left the effect at +0.33.

## Experiment 4: A wrong state, or the wrong person?

<p class="experiment-label">Experiment 4</p>

<div class="setup">

**Setup**

- Study: S7 (photographs; 246 of 288 scenes in which the states of T and O were read correctly)
- Query: place and state in one joint answer; separate queries on the same scenes
- Reference: the marked person as "this same individual", with no name

</div>

<figure>
  <img src="/column-images/ssrn-vlm-frame-alignment/joint-1600.webp" alt="Joint answer types in S7" />
  <figcaption><strong>Figure 6.</strong> Left: the two error types in one joint answer. Only J_old (old place with O's state) responds to alignment. Right: at s = 0, pairing answers from separate prompts versus one joint answer.</figcaption>
</figure>

J_old was 0.14 at s = 0 and 0.04 at s = 1, an alignment effect of +0.10 [0.07, 0.14]. J_cor stayed near zero in both layouts, with an effect of 0.00 [−0.02, 0.01]. Under alignment, the model reported **the other person's place and state together**.

Separate queries give a different picture. When each scene's separate place answer is paired with its separate state answer, "correct place with O's state" appears at a rate of 0.18. In one joint answer this pairing almost never occurs (0.00). The apparent wrong state for a correctly located target came from inconsistency between prompts. The joint answer shows that the model attributed the whole description of O to the target.

## Experiment 5: Steering the error with badges

<p class="experiment-label">Experiment 5</p>

<figure>
  <img src="/column-images/ssrn-vlm-frame-alignment/badge-1600.webp" alt="Badge intervention in S8" />
  <figcaption><strong>Figure 7.</strong> J_old in S8. Person-fixed badges reduce the error; position-fixed badges raise it sharply. "n/r": the paper does not report the s = 1 value for this condition.</figcaption>
</figure>

S8 used 288 new scenes, 235 of which passed the perception gate. Without badges, the alignment effect on J_old was +0.14 [0.09, 0.19], reproducing S7.

Person-fixed badges lowered J_old at s = 0 from 0.18 to 0.07 (−0.11 [−0.15, −0.07]). Adding one sentence that gives the target's badge number lowered it to 0.03. The alignment effect shrank to +0.06 and +0.03 but did not disappear.

Position-fixed badges had the opposite effect, because O, now in the origin, wears the target's badge in frame 2. J_old at s = 0 rose to 0.63 and was still 0.34 in the shifted layout. The two badge types look the same, so badge salience cannot explain these opposite changes. The model followed the correspondence that the badge carried, and alignment added to this cue.

## Experiment 6: Six models

<p class="experiment-label">Experiment 6</p>

<div class="setup">

**Setup**

- Study: S9 (photographs, 288 scenes; no badge, person badge, position badge)
- Expressions: angry, happy and surprised, the three that all six models read best
- Validity: at least 144 scenes pass the gate and static joint accuracy is at least 0.80 at both shifts

</div>

Before S9, eleven further models were screened, and none was valid under the criteria of S1–S8, mostly because they misread expressions even in the static world. S9 therefore reduced the expressions to three and compared six models under one protocol. Two models met the criteria.

| Model | Gated scenes | Static accuracy | Alignment effect on J_old | No badge | Person badge | Position badge |
|---|---|---|---|---|---|---|
| Qwen3-VL-8B | 271 | 0.92 | +0.14 [0.10, 0.18] | 0.16 | 0.05 | 0.59 |
| InternVL3.5-14B | 247 | 0.84 | +0.03 [−0.01, 0.06] | 0.17 | 0.09 | 0.35 |

(The three badge columns give J_old at s = 0.)

<figure>
  <img src="/column-images/ssrn-vlm-frame-alignment/models-1600.webp" alt="J_old of six models in S9" />
  <figcaption><strong>Figure 8.</strong> J_old at s = 0 for the six models in S9. The four lighter models missed the validity criteria, so their values are descriptive.</figcaption>
</figure>

The alignment effect appeared only in Qwen3-VL-8B. InternVL3.5-14B had a similar J_old at s = 0 (0.17 against 0.16), but it stayed at 0.15 in the shifted layout, so its effect was only +0.03.

The badges steered both models in the same directions. Person-fixed badges lowered J_old by −0.12 in Qwen3-VL-8B and −0.08 in InternVL3.5-14B; position-fixed badges raised it by +0.43 and +0.18. Descriptively, position-fixed badges raised J_old in five of the six models and person-fixed badges lowered it in all six. Sensitivity to column alignment depended on the model, while following the correspondence carried by visible cues held in both valid models.

## What we learned, and what remains open

The study supports three points.

- Panel geometry can decide whose state a VLM reports. In a model sensitive to it, a shared image column acts as a cue for cross-frame correspondence. This is not a misread expression: the local and static checks show the expressions are read correctly.
- The error replaces the whole person and is internally consistent, so it is hard to detect. Separate questions about place and state hide this structure, so attribution should be evaluated with answers that report the person and the state together. High expression accuracy does not guarantee a correct report about a person.
- What held across models was cue following, not the alignment effect itself. For panel-based video methods, layouts without exact column alignment and identity marks that stay with each person are two simple safeguards.

There are also limitations. The alignment effect was confirmed in only one model, Qwen3-VL-8B, while the badge result held in both valid models. Ten further models missed the validity criteria and cannot test the claim. The stimuli are controlled two-frame panels with three people, not natural videos with more frames, motion and occlusion. Most studies used greedy decoding with one run per prompt, and sampled answers were checked only for S5 and S7. The person state is a posed facial expression, which is not the same as an internal emotion.

Next, we plan to locate where cross-frame correspondence is resolved inside VLMs and to test panels built from real videos with more frames.

The paper states that the generation code, image identifiers and labels are released, but the preprint gives no URL, so no link is listed here. KDEF images are not redistributed, as their license does not allow it.
