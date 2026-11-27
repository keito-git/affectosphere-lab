---
title: "Can an LLM's Ability to Write Sarcasm Help It Recognize Sarcasm?"
subtitle: "Label-Conditioned Speaker–Listener Model with Bayes-Based Cross-Family Fusion for LLM-Oriented Sarcasm Recognition"
date: "2026-11-27"
excerpt: "LLMs can write sarcastic text, but they still judge real posts unreliably. We let the ability to write sarcasm inform its recognition without generating any text: label-conditioned speaker LLMs are turned into sarcasm scores by Bayes' rule. A walk-through of our IEEE SocialCom 2026 paper."
readingMinutes: 12
showImage: false
image: "/column-images/socialcom2026-lslm-bcf/architecture.png"
imageAlt: "LSLM-BCF architecture. In the upper lane, a listener LLM scores a post by the logit difference of the label tokens; in the lower lane, two speaker LLMs compute the likelihood ratio of the post under the two labels. The standardized scores are added into the final score."
authors:
  - name: "Keito Inoshita"
    url: "/en/about/"
    affiliation: "Kansai University"
  - name: "Xiaokang Zhou"
    affiliation: "Kansai University / RIKEN AIP"
  - name: "Akira Kawai"
    affiliation: "Shiga University"
  - name: "Huazhong Liu"
    affiliation: "Zhejiang Normal University"
  - name: "Katsutoshi Yada"
    affiliation: "Kansai University"
tldr: "We pair a listener LLM that discriminates sarcasm with speaker LLMs that learn how a post is written under the sarcastic and the sincere label. Each speaker computes the likelihood of the observed post under both labels, and Bayes' rule turns the ratio into a sarcasm score, so no text is generated. LSLM-BCF averages two speakers from different model families and adds them to the listener. It achieves the highest F1 among the compared methods on all four sarcasm datasets and improves the test AUC of the listener on every dataset (0.870 to 0.889 on iSarcasm). In contrast, three approaches that use generated texts for training or inference gave no improvement."
links:
  - label: "Paper (IEEE SocialCom, accepted)"
    url: "https://lab.affectosphere.group/en/news/20261118-socialcom2026-lslm-bcf/"
citation: |
  @inproceedings{inoshita2026lslmbcf,
    title     = {Label-Conditioned Speaker--Listener Model with Bayes-Based Cross-Family
                 Fusion for {LLM}-Oriented Sarcasm Recognition},
    author    = {Inoshita, Keito and Zhou, Xiaokang and Kawai, Akira and Liu, Huazhong
                 and Yada, Katsutoshi},
    booktitle = {Proceedings of the IEEE International Conference on Social Computing
                 and Networking (SocialCom)},
    year      = {2026},
    note      = {Accepted, to appear}
  }
---

<div class="teaser">
<div>

Invert

Speaker likelihood ratios become **sarcasm scores by Bayes' rule**. Not a single token is generated.

</div>
<div>

Fuse

**Two speakers from different model families** are averaged and added to the listener. This is more stable across datasets than one speaker.

</div>
<div>

Gain

**Highest F1** on all four datasets. The listener's AUC rises by +1.9 points on iSarcasm (0.889).

</div>
</div>

## Does writing sarcasm help with recognizing it?

Sarcasm is common on social media, and it reverses the literal meaning of a post. Read literally, "what a fantastic service" after a long delay gives the opposite of the author's opinion. When social media posts feed opinion analysis or harmful content detection, a recognizer must capture not only what a post says but also the attitude behind its wording.

Large language models (LLMs) can write sarcastic posts on demand. Yet their judgment of whether a real post is sarcastic remains unreliable. Pragmatics holds that understanding sarcasm requires inferring what the speaker expected and which attitude the speaker expressed. Since humans can imagine how a statement would sound if it were meant sincerely, the ability to write sarcasm should support the ability to recognize it.

Turning generation into better discrimination is not straightforward, however. The paper names three issues.

- Generated texts carry the style and sampling noise of the generator. A recognizer that uses them as training data or as rewrites at inference may learn these artifacts instead of knowledge that transfers to real posts.
- A generative model trained only to reproduce posts is not tuned to the difference between sarcastic and sincere wording. A model trained mainly to discriminate may overlap with what the recognizer already knows.
- A single generative model inherits the biases of one model family, so what it adds may vary across datasets.

Our approach is therefore to **pass generative knowledge to the recognizer through the likelihood of the observed post, not through generated text**.

## How LSLM-BCF works

<figure>
  <img src="/column-images/socialcom2026-lslm-bcf/architecture-1600.webp" alt="LSLM-BCF architecture" />
  <figcaption><strong>Figure 1.</strong> Architecture of LSLM-BCF (figure from the paper). The upper lane is the listener, which discriminates; the lower lane holds two speakers, which model generation. The speakers only compute likelihoods and never sample text.</figcaption>
</figure>

LSLM-BCF combines three LLMs. Each is a LoRA adapter trained separately.

1. **Listener**: it reads the post and its context and is asked "Is the utterance sarcastic? Answer with exactly '1' or '0'." The score is the logit difference of the tokens "1" and "0". No answer is decoded, so one forward pass gives a continuous score.
2. **Label-conditioned speakers**: each is trained as a language model on "Label: sarcastic / sincere. Tweet:" followed by the post, so it learns how a post is written under each label, p(u | y). In iSarcasm, the authors' own sincere rephrases of their sarcastic posts are added as sincere examples for the speakers only.
3. **Bayes inversion**: a speaker computes the likelihood of the observed post under both labels. By Bayes' rule, the log-likelihood ratio equals the log posterior odds of sarcasm up to the log prior odds. The prior odds are the same for every post and vanish under standardization.

There are two speakers. One is from the same model family as the listener (family A, Qwen2.5-7B), and the other is from a different family (family B, Gemma-3-12B). Here, different families means LLMs that were pre-trained separately by different developers.

<figure>
  <img src="/column-images/socialcom2026-lslm-bcf/prl-loss-1600.webp" alt="PRL loss" />
  <figcaption><strong>Figure 2.</strong> Mechanism of the Posterior-Regularized Likelihood (PRL) loss (figure from the paper). A cross-entropy over the prior-weighted label posterior is added to the usual token likelihood.</figcaption>
</figure>

The family-A speaker is trained with the **PRL loss**. On top of the token likelihood, it adds a cross-entropy over the label posterior that Bayes' rule gives from the two label likelihoods. The speaker stays a generative model of posts, and its label likelihoods also separate the labels. The family-B speaker is trained with the plain negative log-likelihood (NLL) loss.

<figure>
  <img src="/column-images/socialcom2026-lslm-bcf/fusion-1600.webp" alt="Cross-family fusion" />
  <figcaption><strong>Figure 3.</strong> Cross-family fusion with Bayes speaker inversion (figure from the paper). Each score is standardized with the mean and standard deviation from the validation posts; the two speakers are averaged and added to the listener score.</figcaption>
</figure>

The final score is "standardized listener score + η × (mean of the two standardized speaker scores)". The statistics used for standardization need no labels. Once they are stored from the validation posts, new posts can be scored one at a time. Settings such as η = 1 were chosen by five-fold cross-validation on iSarcasm and were not re-tuned for the other datasets.

## Experiment 1: Comparison with existing methods

<p class="experiment-label">Experiment 1</p>

<div class="setup">

**Setup**

- Data: iSarcasm (author-labeled tweets), EPIC (replies with parent posts), MUStARD (TV-script utterances with preceding turns), SCv2 (debate-forum posts)
- Backbones: Qwen2.5-7B-Instruct for the listener and the family-A speaker; Gemma-3-12B for the family-B speaker
- Evaluation: official test splits, mean of five seeds. Precision, recall and F1 are macro-averaged over the two classes, at the threshold that maximizes validation macro-F1
- Baselines: a zero-shot LLM (Qwen2.5-14B), four prompting methods (SarcasmCue, PMP, CAF-I, SEVADE), three fine-tuned PLMs, two fine-tuned variants of Qwen2.5-7B (generative SFT and Sarcasm-R1), and the listener alone and an ensemble of three listeners. All re-implemented on the same splits

</div>

| Dataset | Train | Val | Test | Sarcastic ratio |
|---|---|---|---|---|
| iSarcasm | 3,111 | 346 | 1,393 | 0.25 |
| EPIC | 2,392 | 296 | 298 | 0.22 |
| MUStARD | 527 | 56 | 98 | 0.50 |
| SCv2 | 5,449 | 870 | 862 | 0.56 |

<figure>
  <img src="/column-images/socialcom2026-lslm-bcf/f1-comparison-1600.webp" alt="Macro-F1 comparison" />
  <figcaption><strong>Figure 4.</strong> Macro-F1 on the four datasets (selected baselines). Gold is LSLM-BCF; blue is the listener alone.</figcaption>
</figure>

LSLM-BCF has the highest F1 on all four datasets and the highest accuracy on three of them. On iSarcasm it reaches an accuracy of 0.851 and an F1 of 0.751, against 0.825 and 0.726 for the listener alone. On EPIC, generative SFT has a higher accuracy (0.809 against 0.789), while LSLM-BCF keeps the highest F1.

A second observation is that the zero-shot LLM and the prompting methods stay below every fine-tuned PLM in F1 on all four datasets. Prompt design alone does not yet solve sarcasm recognition.

## Experiment 2: Does the ranking of posts improve?

<p class="experiment-label">Experiment 2</p>

F1 depends on a threshold, so we also look at AUC, which does not. AUC differences are given in points (multiplied by 100), with 95% confidence intervals from 2,000 bootstrap resamples of the test posts.

<figure>
  <img src="/column-images/socialcom2026-lslm-bcf/auc-gain-1600.webp" alt="AUC gain over the listener" />
  <figcaption><strong>Figure 5.</strong> Test AUC of the listener alone (blue) and LSLM-BCF (gold). The AUC improves on every dataset.</figcaption>
</figure>

The gains over the listener are +1.9, +1.8, +5.4 and +1.2 points on iSarcasm, EPIC, MUStARD and SCv2. On every dataset, the difference is positive in at least four of five seeds. On iSarcasm, the AUC rises from 0.870 to 0.889; the difference is positive in all five seeds, with a 95% confidence interval of [+0.5, +3.3]. The intervals exclude zero on every dataset except EPIC.

One may suspect that the gain comes simply from averaging more models. Against an ensemble of three listeners, LSLM-BCF is +1.1 points higher on iSarcasm in all five seeds. However, the confidence interval [−0.4, +2.5] includes zero, and LSLM-BCF includes a larger 12B speaker. On EPIC, the ensemble has a larger area under the PR curve (0.625 against 0.595).

## Experiment 3: Does the gain come from post-specific information?

<p class="experiment-label">Experiment 3</p>

If the gain comes from information that the speaker score carries about each post, breaking that link should remove it. On iSarcasm, we ran two controls: randomly permuting the speaker score across the test posts, and negating its sign.

<figure>
  <img src="/column-images/socialcom2026-lslm-bcf/robustness-1600.webp" alt="Robustness and controls on iSarcasm" />
  <figcaption><strong>Figure 6.</strong> iSarcasm test AUC. Standardizing with validation statistics gives almost the same result. Permuting or negating the speaker score drops the AUC below the listener alone (dashed line).</figcaption>
</figure>

With validation statistics the AUC is 0.888, almost the same as 0.889 with test statistics, so scoring posts one at a time keeps the performance. Permuting the speaker score lowers the AUC to 0.798, and negating it lowers it to 0.585. Both fall below the listener alone at 0.870. Breaking the link to each post while keeping the score distribution removes the effect, so the gain comes from post-specific speaker information.

We also compared precision, recall and F1 using validation statistics and validation-chosen thresholds.

| Dataset | Listener P | Listener R | Listener F1 | LSLM-BCF P | LSLM-BCF R | LSLM-BCF F1 |
|---|---|---|---|---|---|---|
| iSarcasm | 0.701 | 0.801 | 0.726 | **0.718** | **0.811** | **0.744** |
| EPIC | 0.703 | 0.721 | 0.705 | **0.710** | **0.751** | **0.717** |
| MUStARD | 0.735 | 0.710 | 0.704 | **0.750** | **0.729** | **0.721** |
| SCv2 | 0.829 | 0.827 | 0.826 | **0.844** | **0.842** | **0.842** |

All three metrics rise on every dataset. The gain does not trade precision for recall or vice versa.

## Experiment 4: Which components matter?

<p class="experiment-label">Experiment 4</p>

We removed components and measured the test AUC. These test values were not used for model selection.

<figure>
  <img src="/column-images/socialcom2026-lslm-bcf/ablation-1600.webp" alt="Ablation study" />
  <figcaption><strong>Figure 7.</strong> Mean AUC over the four datasets when components are removed. Blue is the listener alone, without speakers.</figcaption>
</figure>

Removing both speakers lowers the AUC on every dataset. Removing the listener lowers it on all datasets except MUStARD, where the speakers alone (0.854) marginally exceed LSLM-BCF (0.853).

With only one speaker, the AUC drops sharply on some dataset. Without the family-A speaker, the variant falls up to 2.1 points below the best variant; without the family-B speaker, up to 4.0 points. In contrast, the two-family combinations stay within 1.2 points of the best variant on every dataset. The reason to combine families is **stability across datasets**, not only the mean.

The PRL loss had a limited effect. Relative to a family-A speaker trained with the NLL loss, it changes the AUC by −1.0, −0.2, +0.8 and +0.4 points on iSarcasm, EPIC, MUStARD and SCv2, leaving the mean unchanged at 0.875. It helps only on MUStARD and SCv2. Looking at the speakers alone on the validation splits explains why.

| Dataset | Speaker AUC (NLL) | Speaker AUC (PRL) | Spearman with listener (NLL) | Spearman with listener (PRL) |
|---|---|---|---|---|
| iSarcasm | 0.706 | 0.740 | 0.48 | 0.58 |
| EPIC | 0.733 | 0.749 | 0.51 | 0.55 |
| MUStARD | 0.661 | 0.659 | 0.34 | 0.46 |
| SCv2 | 0.865 | 0.899 | 0.78 | 0.87 |

The PRL loss raises the speaker's own AUC on three datasets. It also raises the correlation with the listener on every dataset, from 0.53 to 0.61 on average. Most of the discriminative ability that PRL adds is thus shared with the listener. Consistently, the Pearson correlation with the listener on the validation posts is 0.56 for the family-A speaker and 0.46 for the family-B speaker, which is weaker alone but overlaps least with the listener. The paper concludes that a speaker should be chosen and trained for **what it adds to the listener**, not for its accuracy alone.

## Experiment 5: Which kinds of sarcasm benefit?

<p class="experiment-label">Experiment 5</p>

We broke the cross-validated gain down by sarcasm mechanism on the 346 validation posts of iSarcasm (87 sarcastic, 259 sincere). Each sarcastic post was tagged by the majority of three LLMs (Qwen2.5-14B, Llama-3.1-8B, Gemma-3-12B), and each group was contrasted with all sincere posts. The groups are small, so this analysis is exploratory.

<figure>
  <img src="/column-images/socialcom2026-lslm-bcf/mechanism-1600.webp" alt="Gain by sarcasm mechanism" />
  <figcaption><strong>Figure 8.</strong> AUC gain over the listener by sarcasm mechanism. Left: two-speaker LSLM-BCF (the error bar is the 95% confidence interval that the paper reports for tone markers). Right: a single speaker fused with the listener.</figcaption>
</figure>

The largest gain appears on **tone markers** such as emojis and interjections. Over 36 posts, the AUC rises from 0.791 to 0.838, and its 95% confidence interval of [+0.3, +9.5] points is the only one that excludes zero. **Exaggeration** gains +1.9 points over 28 posts, mainly from the family-A speaker (+3.2) while the family-B speaker gives −0.8. On tone markers, the family-B speaker adds more (+4.1 against +2.8). The two families respond to different cues, which supports the cross-family fusion.

In contrast, the speakers add little when sarcasm is not marked in the wording. Polarity reversal, which states the opposite of the intended opinion, is unchanged at +0.1 points, and the three LLMs rarely agree on this tag (Fleiss' κ = 0.05). Pretense and posts without a clear mechanism change by −3.4 and −0.6 points, with confidence intervals that include zero. The likelihood of the wording is informative mainly when sarcasm leaves explicit cues in the post.

## Experiment 6: What about using generated text?

<p class="experiment-label">Experiment 6</p>

The starting choice of this work was to use likelihoods instead of generated text. As a control, we implemented three approaches that do use generated text, on the same backbone.

| Approach | Change in cross-validated AUC | Change in test AUC |
|---|---|---|
| Hinge loss for the listener that ranks an LLM-generated sarcastic version of each training post above its sincere version | 0.0 | −1.2 |
| Subtracting the score of a generated sincere rewrite at inference | −1.2 | — |
| Averaging the scores over generated paraphrases at inference | −0.2 | — |
| LSLM-BCF (single-speaker variant) | +0.8 | +1.2 |

Values are in points; "—" means the paper gives no value. None of the three approaches that use generated text improved the cross-validated AUC. The single-speaker LSLM-BCF improved it by +0.8 points and the test AUC by +1.2 points. The conclusion from this comparison is that generative knowledge transfers to discrimination when it is **used as evidence about an observed post rather than as generated text**.

## What we learned and what remains open

The findings are as follows.

- Inverting the likelihood ratio of label-conditioned speakers by Bayes' rule lets generative knowledge support discrimination without generating text. LSLM-BCF has the highest F1 on all four datasets and improves the listener's AUC on every one.
- The gain comes from post-specific speaker information. Breaking the link between the speaker score and each post removes it.
- Combining speakers from different model families is more stable across datasets than a single speaker. The two families respond to different cues (tone markers and exaggeration).
- The speakers help when sarcasm shows in the wording, as with tone markers and exaggeration, and not with polarity reversal or pretense.

The method adds a moderate cost at inference. A post needs one forward pass of the 7B listener and one batched pass of each speaker over the two label prompts. Since the family-A speaker can share the backbone of the listener, the weights held in memory grow from about 7.6B to about 20B parameters.

There are also limitations. Wall-clock latency was not measured. Only four English datasets, one listener backbone and two model families for the speakers were evaluated. The speakers do not read the preceding context, and the mechanism tags come from LLMs, not human annotators. On EPIC, which keeps the labels of annotators with different backgrounds who often disagree, the speakers model the wording under one aggregated label, and this disagreement may weaken their evidence (the paper states this as a conjecture).

Future work includes losses that make the generative and discriminative views more complementary, adding the preceding context to the speakers, and evaluating other model families and languages.
