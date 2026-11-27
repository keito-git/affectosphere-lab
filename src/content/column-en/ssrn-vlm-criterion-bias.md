---
title: "Does the Same Fear/Surprise Confusion Mean the Same Failure?"
subtitle: "Same Confusion, Different Failure: Separating Criterion Bias from Separability Loss in Vision-Language Models"
date: "2026-11-27"
excerpt: "VLMs tend to call fearful faces \"surprised\". The same error can mean that the model cannot tell the two emotions apart, or that it can and still applies a displaced decision criterion. A walk-through of our SSRN preprint, which separates the two with signal detection theory."
readingMinutes: 12
showImage: false
image: "/column-images/ssrn-vlm-criterion-bias/framework.png"
imageAlt: "Overview of the diagnostic framework. Label-word scores and the final hidden state of a VLM are read out, described by separability (AUC) and the decision criterion c, and diagnosed with four analyses."
authors:
  - name: "Keito Inoshita"
    url: "/en/about/"
    affiliation: "Kansai University"
tldr: "Across four open VLMs and six face datasets (24 cells), the fear/surprise criterion lies on the surprise side in every cell. The failure behind it, however, differs between image types. On posed and synthetic faces, the output still separates the two emotions, and the shifted criterion survives every label-free reference. On in-the-wild images, content-free calibration removes most of the shift for three models, and output separability is lower. Anger and disgust fail in yet another way: their distinction is linearly decodable from the final hidden state but weakly reflected in the output. A confusion matrix alone cannot identify the failure mechanism."
links:
  - label: "Preprint (SSRN)"
    url: "https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7685198"
citation: |
  @misc{inoshita2026sameconfusion,
    title        = {Same Confusion, Different Failure: Separating Criterion Bias
                    from Separability Loss in Vision-Language Models},
    author       = {Inoshita, Keito},
    year         = {2026},
    howpublished = {SSRN preprint, abstract id 7685198}
  }
---

<div class="teaser">
<div>

Same error

The fear/surprise criterion lies **on the surprise side in all 24 cells**. The two-choice criterion ranges from −6.64 to −0.21.

</div>
<div>

Different failure

On posed and synthetic faces, **the output still separates the two (AUC 0.75–0.97) but the criterion is shifted**. On in-the-wild images, separability itself drops.

</div>
<div>

Poor transfer

A correction fitted on one image type **transfers poorly to the other**. An offset fitted on posed faces over-corrects in-the-wild images.

</div>
</div>

## Separating what lies behind one error

Vision-language models (VLMs) such as Gemma 3, Qwen3-VL and InternVL3.5 answer free-form questions about images, and they are now used to read people, including their facial expressions. General-purpose VLMs often reach an F1 near zero for fear, and fear is easily confused with surprise, as it is in human perception. The question of this study is not whether VLMs make this error, but **why they make it computationally**.

Accuracy and confusion matrices summarize only the final answer. The same "fear answered as surprise" error can have at least two causes.

- The output **cannot separate** the two emotions (loss of separability).
- The output separates them, but **the decision threshold sits on the surprise side** (a shifted criterion).

Signal detection theory treats a binary decision in exactly these two terms. This study applies it to the output of a VLM and compares the output with the model's internal state, to test whether the same confusion arises from the same failure.

## The diagnostic framework

<figure>
  <img src="/column-images/ssrn-vlm-criterion-bias/framework-1600.webp" alt="Diagnostic framework" />
  <figcaption><strong>Figure 1.</strong> Overview of the diagnostic framework (figure from the paper). (a) Label-word scores and the final hidden state are read out, (b) each pair is described by separability (AUC) and the criterion c, and (c) four analyses ask where each property comes from.</figcaption>
</figure>

For two classes a (fear) and b (surprise), the difference of the label-word log-probabilities, d(x) = s_b(x) − s_a(x), serves as the decision variable.

1. **Separability (output AUC)**: how well d ranks fearful images against surprised images. It does not depend on any threshold.
2. **Criterion c**: how far the threshold d = 0 used by the answer sits from the midpoint of the two class means, in units of the pooled standard deviation. A negative value means that fearful faces tend to be called surprised.
3. **Probe AUC**: the AUC of a linear probe (logistic regression) on the final hidden state. When the probe AUC exceeds the output AUC by 0.15 or more, the paper operationally calls this separability loss. The term does not imply that the information is erased from the hidden state.

Four analyses then ask where a criterion shift comes from: a hierarchy of label-free calibration references, cross-dataset transfer of a correction, a layer-wise logit lens, and interventions with example images and activation steering. Each question is asked in both option orders, and the scores are averaged to cancel position bias.

<div class="setup">

**Setup**

- Models: Gemma 3 12B, Qwen3-VL 8B, InternVL3.5 14B, Mistral Small 3.1 24B (instruction-tuned, bfloat16)
- Questions: seven-way (one word out of afraid, angry, disgusted, happy, neutral, sad, surprised) and two-choice (only the two classes of a pair)
- Intervals: 95% bootstrap intervals over 2,000 resamples of identities (images for in-the-wild data)
- Hardware: one NVIDIA RTX PRO 6000

</div>

| Dataset | Type | Images | Bootstrap units |
|---|---|---|---|
| KDEF | posed | 1,468 | 70 identities |
| JAFFE | posed | 213 | 10 identities |
| WSEFEP | posed | 207 | 30 identities |
| UIBVFED | synthetic | 660 | 20 characters |
| RAF-DB | in the wild | 2,485 | 2,485 images |
| ExpW | in the wild | 3,471 | 3,471 faces |

## Experiment 1: Which way does the criterion lean?

<p class="experiment-label">Experiment 1</p>

<figure>
  <img src="/column-images/ssrn-vlm-criterion-bias/criterion-1600.webp" alt="Fear/surprise criterion in all 24 cells" />
  <figcaption><strong>Figure 2.</strong> Fear/surprise criterion in all 24 cells (two-choice, full-word scores, with 95% intervals). A point left of the dashed line means that fearful faces tend to be called surprised. Amber marks posed and synthetic faces, blue marks in-the-wild images.</figcaption>
</figure>

The fear/surprise criterion lies on the surprise side in every cell. Its 95% interval excludes zero in 24 of 24 cells for the seven-way question and in 24 of 24 cells for the two-choice question. The seven-way criterion ranges from −9.22 to −1.16 on posed and synthetic faces and from −1.74 to −0.53 on in-the-wild images. The shift is large on posed and synthetic faces, and extreme on some datasets such as WSEFEP.

The result does not depend on how the criterion is defined or how the answer is scored. An empirical criterion, measured from the threshold with the highest balanced accuracy, is negative in 24 of 24 seven-way cells and in 19 of 20 two-choice cells. At the threshold of zero, fearful faces are misread more often than surprised faces in 24 of 24 seven-way cells. Moving from first-token scores to full-word scores changes the AUC by at most 0.003 and the criterion by at most 0.014.

## Experiment 2: Which pairs are not separated?

<p class="experiment-label">Experiment 2</p>

<figure>
  <img src="/column-images/ssrn-vlm-criterion-bias/auc-vs-criterion-1600.webp" alt="Output AUC against criterion" />
  <figcaption><strong>Figure 3.</strong> Seven-way output AUC (vertical) against the criterion (horizontal) for fear/surprise in the 24 cells. Posed and synthetic faces (amber) keep a high AUC with a large criterion shift; in-the-wild images (blue) have a smaller shift and a lower AUC.</figcaption>
</figure>

On posed and synthetic faces, the seven-way output AUC ranges from 0.75 to 0.97, so the output separates fear from surprise well. The fear error on these faces is therefore mainly **a criterion failure**.

In-the-wild images behave differently. The fear/surprise output AUC drops to 0.61–0.83 on RAF-DB and to 0.64–0.75 on ExpW, so this becomes the less separable pair. The two datasets also differ inside the model. On RAF-DB, the probe AUC stays at 0.89–0.95, so the hidden state separates the two emotions better than the emotion-word scores do. On ExpW, the probe AUC is also low, at 0.71–0.77, so the hidden state itself separates them less well.

<figure>
  <img src="/column-images/ssrn-vlm-criterion-bias/separability-loss-1600.webp" alt="Separability loss counts" />
  <figcaption><strong>Figure 4.</strong> Number of cells in which the probe AUC exceeds the output AUC by 0.15 or more. Anger/disgust meets this in most posed and synthetic cells and in none of the in-the-wild cells.</figcaption>
</figure>

Anger and disgust fail in another way. The gap reaches 0.15 in 13 of 16 posed and synthetic cells, with an output AUC of 0.30–0.73 against a probe AUC of 0.83–0.97. A distinction that a linear probe can read from the final hidden state is weakly reflected in the emotion-word scores. On in-the-wild images this loss occurs in 0 of 8 cells, and the output AUC is 0.72–0.89.

The conclusion does not hinge on the 0.15 cutoff.

| Cutoff | Anger/disgust (posed + synth.) | Anger/disgust (wild) | Fear/surprise (posed + synth.) | Fear/surprise (wild) | All 21 pairs (posed + synth.) | All 21 pairs (wild) |
|---|---|---|---|---|---|---|
| 0.10 | 14 | 4 | 2 | 5 | 35 | 14 |
| 0.15 | 13 | 0 | 0 | 2 | 24 | 5 |
| 0.20 | 13 | 0 | 0 | 2 | 18 | 3 |

Each pair has 16 posed and synthetic cells and 8 in-the-wild cells.

## Experiment 3: Is the shift just a prior over answer words?

<p class="experiment-label">Experiment 3</p>

If the criterion shift were a prior over the answer words that does not depend on the image, subtracting the bias measured on content-free inputs should remove it. The study uses three label-free references of increasing image match: content-free inputs (blank and noise images and a prompt without an image), neutral faces from the same dataset, and faces from the same dataset that show neither fear nor surprise. A supervised offset that uses labels is added for comparison.

<figure>
  <img src="/column-images/ssrn-vlm-criterion-bias/calibration-1600.webp" alt="Calibration hierarchy" />
  <figcaption><strong>Figure 5.</strong> Fear/surprise criterion after each reference (mean of the four models, bars show the range over models). The grey band marks the label-free references. On posed and synthetic faces (left) the shift remains inside the band; on in-the-wild images (right) content-free calibration moves it close to zero.</figcaption>
</figure>

On in-the-wild images, content-free calibration moves the criterion of Gemma 3, Qwen3-VL and Mistral Small 3.1 to −0.05 to 0.12 on RAF-DB and to −0.32 to −0.15 on ExpW, removing most of the shift. InternVL3.5 stays at −1.41 on RAF-DB and −1.52 on ExpW.

On posed and synthetic faces, the shift remains after every label-free reference. The only exception is Qwen3-VL on JAFFE, where neutral faces move the criterion past zero to 0.55. The supervised offset brings every criterion within 0.65 of zero on its own dataset. The shift on posed and synthetic faces therefore cannot be explained by a prior shared with these references; it depends on the images.

## Experiment 4: Does a correction transfer across datasets?

<p class="experiment-label">Experiment 4</p>

The supervised offset adds one constant to the score of each class. Applying an offset fitted on one dataset to another tests whether the criterion shift is shared across datasets.

<figure>
  <img src="/column-images/ssrn-vlm-criterion-bias/transfer-1600.webp" alt="Cross-dataset transfer of the offset" />
  <figcaption><strong>Figure 6.</strong> Mean absolute criterion after applying the offset of a source dataset to a target dataset. Lower means the correction transfers better.</figcaption>
</figure>

An offset fitted on in-the-wild images under-corrects posed and synthetic faces (mean 1.08), compared with 0.80 from another posed or synthetic dataset, which is lower in 3 of 4 models. An offset fitted on posed and synthetic faces over-corrects in-the-wild images and changes their mean accuracy by −0.058. Between the two in-the-wild datasets the mean is 0.34, lower than after transfer from posed faces in all four models. The surprise-minus-fear offset is negative in 24 of 24 cells and is smallest on RAF-DB for all four models.

Calibration has to be fitted on the type of images where it will be used.

## Experiment 5: Where does the output vocabulary diverge?

<p class="experiment-label">Experiment 5</p>

The logit lens passes the state at intermediate layers through the final normalization and the unembedding matrix, to trace the depth at which each pair aligns with the output vocabulary. Because the logit lens is a fixed readout that can be brittle in intermediate layers, a low value is read as weak alignment with the output vocabulary, not as an absence of information. Each pair is summarized by the drop from the late-layer peak to the final layer.

For anger/disgust, the lens AUC falls by 0.10 or more in 6 of 16 posed and synthetic cells, by up to 0.41. Over the same layers, layer-wise probes stay at or above 0.73. On RAF-DB, the final layer is the peak in all four models, and on in-the-wild images the drop is 0.00–0.09. The divergence from the output vocabulary emerges late in the network and differs between posed and in-the-wild images. For fear/surprise, the lens AUC rises in the second half of the depth and stays high on posed faces.

## Experiment 6: Can the criterion be moved on its own?

<p class="experiment-label">Experiment 6</p>

Finally, on frontal KDEF faces, two interventions test whether the criterion can be moved without changing separability. The first shows one fearful and one surprised face of other identities in a previous turn, with true labels, swapped labels, or no labels.

<figure>
  <img src="/column-images/ssrn-vlm-criterion-bias/examples-1600.webp" alt="Effect of example faces on the criterion" />
  <figcaption><strong>Figure 7.</strong> KDEF two-choice criterion under each example condition. Expressive example faces move the criterion toward zero whether their labels are true, swapped or absent; neutral faces do not.</figcaption>
</figure>

Expressive example faces move the two-choice criterion toward zero by 0.41–1.67 regardless of the labels, while the AUC changes by −0.04 to 0.03. Neutral faces of the same identities change it by −0.31 to −0.04 and do not move it toward zero. The examples act through the expressive faces they show, not through their labels.

The second intervention is activation steering: the direction "mean fear state minus mean surprise state" is added to the residual stream at three quarters of the depth. Without steering, the share of fearful faces answered "afraid" ranges from 0.09 to 0.40. Steering along the class direction raises it to at least 0.97 in every model before the answers break down, whereas random and other-class directions of the same norm never exceed 0.54.

## What we learned, and what remains open

The study shows three things.

- The fear-to-surprise error is consistent across all four models and six datasets, but **its failure mechanism differs between image types**. On posed and synthetic faces the output separates the two and the criterion is shifted; on in-the-wild images the error mixes a smaller shift (mostly shared with content-free inputs for three models) with lower separability.
- Anger and disgust show a separability failure: on posed and synthetic faces the distinction is **decodable from the hidden state but weakly reflected in the output**, and the divergence emerges in the last layers.
- A correction fitted on one image type transfers poorly to the other.

The paper therefore argues that VLM evaluations should report separability and criterion separately. A criterion failure can be corrected with a few parameters, but a class-wise additive offset does not change the ranking of images, so it cannot fix a separability failure.

There are limitations. The difference between posed and in-the-wild images is not causal evidence, since the two types also differ in intensity, cropping, pose, image quality, labeling and the people shown. The labels of in-the-wild images are annotators' judgments, not the emotions felt by the people shown. Only four open models of medium size and the seven basic emotion words were tested; closed models, other label sets or free-form answers may behave differently. The in-the-wild datasets have no identity labels, so their intervals are estimated over images and may not account for repeated identities. The causal checks with example faces and steering were run on KDEF only.

Next, the decomposition will be applied to closed models, video and other label sets, together with calibration that stays valid across image types.
