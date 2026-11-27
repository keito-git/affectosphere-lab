---
title: "Does Emotion Steering Reach the Emotion, or Only the Emotion Word?"
subtitle: "Emotion Steering Is Specific to the Human Emotion Partition yet Remains Bound to Its Output Encoding"
date: "2026-11-27"
excerpt: "Steering directions built from human emotion categories beat a variance-matched control and other partitions of the same grain. When the output was switched from emotion words to opaque codes, the same directions barely worked. A walk-through of our SSRN preprint, which tests steering through three control gates."
readingMinutes: 13
showImage: false
image: "/column-images/ssrn-steering-human-partition/gates.png"
imageAlt: "Structure of the three control gates. Gate I matches the direction's size, Gate II the source of the partition, and Gate III the output encoding."
authors:
  - name: "Keito Inoshita"
    url: "/en/about/"
    affiliation: "Kansai University"
tldr: "When adding a direction to a hidden state changes the output, this is often read as evidence that the model represents the emotion. That reading is only as strong as the control. We define three control gates and apply them in order across nine models from five families. Directions estimated from 13 human emotion categories beat a floor matched term by term in activation variance (Gate I) and other partitions of the same grain (Gate II) in almost every model. But when the same 13 categories were answered as opaque codes (Gate III), none of the five eligible models met the criterion. Successful steering does not by itself establish an encoding-invariant semantic representation."
links:
  - label: "Preprint (SSRN)"
    url: "https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7634898"
  - label: "Code"
    url: "https://github.com/keito-git/nativeaffect-prereg"
citation: |
  @misc{inoshita2026steeringpartition,
    title        = {Emotion Steering Is Specific to the Human Emotion Partition yet
                    Remains Bound to Its Output Encoding},
    author       = {Inoshita, Keito},
    year         = {2026},
    howpublished = {SSRN preprint, abstract id 7634898}
  }
---

<div class="teaser">
<div>

Gate I

Against a floor matched term by term in variance, **8 of 9 models** clear a majority of the 13 categories (median +2.83 SD).

</div>
<div>

Gate II

The directions beat random partitions and **partitions more decodable than the human one**. The effect is specific to the human partition.

</div>
<div>

Gate III

Read out as opaque codes, the median drops **from +2.33 SD to +0.45 SD**, and none of the 5 eligible models meets the criterion.

</div>
</div>

## From "we could move it" to "it is represented"

Adding a direction to a hidden state and reading the change in the output is now a standard tool for studying affect in large language models (LLMs). Emotion categories and valence can be decoded from hidden states with high accuracy, and moving a state along such a direction changes the emotional content of what the model writes. In affective computing, this success is often taken as evidence for a stronger claim: that the model represents the emotion that was controlled.

That step rests on a comparison. A direction is called specific because it moves the output more than other directions do. Three features of the comparison are left unmatched, and each can produce the effect on its own.

1. **The size of the direction.** Directions with large activation variance move the output whatever they mean.
2. **The source of the labels.** Thirteen directions fitted to thirteen class labels will move a 13-way readout whatever the classes are.
3. **The output encoding.** Does the direction move the emotion, or only the emotion word?

In this study we define a control gate for each of these and apply all three, in order, to a single set of directions.

## The three control gates

<figure>
  <img src="/column-images/ssrn-steering-human-partition/gates-1600.webp" alt="The three control gates" />
  <figcaption><strong>Figure 1.</strong> Overview figure from the paper. Top: the measurement pipeline shared by all gates. Bottom: what each gate holds fixed, what it varies and what it licenses.</figcaption>
</figure>

Intervention strength is matched on the output side in every condition. The coefficient is bisected until the Jensen–Shannon distance between next-token distributions before and after reaches the same value (J* = 0.05) over the full vocabulary. Directions with different norms are therefore compared at the same output perturbation. The readout is signed: it uses the difference between adding and subtracting the direction.

At every gate the statistic compares the best member of the candidate family with the best member of a matched family. The advantage of picking the best of several directions is granted to the control as well.

**Gate I** uses a floor that randomizes only **the signs** of a direction's coordinates in the eigenbasis of the activations.

<figure>
  <img src="/column-images/ssrn-steering-human-partition/floor.png" alt="Sign-randomised floor construction" />
  <figcaption><strong>Figure 2.</strong> How the Gate I floor is built (figure from the paper). (a) Flipping signs leaves every eigenvalue-weighted variance term unchanged. (b) For a principal direction, only ±u_k satisfies the condition, so the floor coincides with the target.</figcaption>
</figure>

Flipping signs leaves each "eigenvalue × squared coordinate" term unchanged, so variance and norm match exactly, term by term, rather than approximately. One consequence is that a principal direction has no matched floor under this criterion. The strict comparison is therefore limited to emotion-category axes and appraisal axes.

**Gate II** keeps the estimator, layer, strength, readout and class sizes identical and changes only where the partition comes from. There are two comparison families. One shuffles the emotion labels across rows. The other clusters the activations and **keeps only partitions at least as decodable as the human emotion partition**.

**Gate III** freezes the directions, layer, strength and floor, and changes only the output encoding. The 13 categories are named by meaningless single letters, the codebook is given in the prompt, and the readout is the probability of the 13 letters.

## Experiment 1: Do the directions beat a variance-matched floor? (Gate I)

<p class="experiment-label">Experiment 1</p>

<div class="setup">

**Setup**

- Models: nine instruction-tuned models from five families, split in advance into a discovery cohort (4) and a confirmation cohort (5); one middle-to-late layer fixed per model
- Stimuli: crowd-enVENT (13 emotion categories; 21 of its 23 appraisal dimensions)
- Directions: ridge regression onto the 13 category indicators (emotion family, K = 13) and onto appraisal ratings (K = 21)
- Strength: J* = 0.05; 50 floor draws per target at Gate I
- Evaluation: how many of 13 targets beat the floor (a majority, 7/13, passes), and the standardised excess in SD

</div>

<figure>
  <img src="/column-images/ssrn-steering-human-partition/gates-1-2-1600.webp" alt="Targets cleared at Gates I and II" />
  <figcaption><strong>Figure 3.</strong> Number of the 13 targets that beat the control, per model (single-token readout). Amber is Gate I; blue and grey are the two Gate II controls. The dashed line marks a majority (7/13).</figcaption>
</figure>

Directions estimated from human emotion categories cleared a majority of the 13 targets in 8 of 9 models. The median standardised excess was +2.83 SD (family-clustered 95% interval [+1.77, +2.86]). A second readout based on synonym sets gave the same conclusion.

Enlarging the scoring set to 256 unused sentences strengthened the result: 9 of 9 models passed, with a median of +3.56 SD [+2.39, +3.78]. OLMo-2-13B and Gemma-2-9B, which sat on the boundary with 32 sentences, rose to 9/13 and 8/13.

The size of the floor matters too. With 10 draws the figures were 9 models and +3.17 SD, but 10 draws underestimate the tail of the null and overstated the effect by up to 0.9 SD. The paper uses the 50-draw values throughout.

## Experiment 2: Would any other partition do? (Gate II)

<p class="experiment-label">Experiment 2</p>

Passing Gate I leaves an obvious objection: maybe any 13-way split would work.

Against 100 random partitions, the aggregate statistic of the emotion family beat all 100 in every model under both readouts (p_G = 0.0099, the lower bound with 100 draws). On the count criterion, 7 of 9 models passed under the single-token readout and 8 of 9 under the synonym-set readout.

Random partitions are harder to decode from the activations than the human partition. To rule out the reading that the human partition worked only because it was predictable, we collected 30 partitions from activation clustering that were **at least as decodable as the human one**. Where the rule was hardest to satisfy, this took up to 16,500 attempts.

The emotion family still won in 8 of 9 models under the single-token readout and 9 of 9 under the synonym-set readout (median +2.67 SD). The comparison partitions reached a probe quality of 0.9730–0.9919, above the human partition's 0.9546–0.9775.

We name the models that did not pass. Llama-3.1-8B gave 6/13 under both readouts against random partitions. Phi-3-medium sat on the boundary (6/13 and 7/13) against both controls. Both still beat all 100 random partitions on the aggregate statistic.

A third family, clustered on character n-grams, reached a probe quality of at most 0.862–0.881, so no partition fell in the required band. We report it as not constructible rather than relaxing the rule.

## Experiment 3: Re-encoding the output (Gate III)

<p class="experiment-label">Experiment 3</p>

Gate III asks the model to answer the same 13 categories as single-letter codes. Because this requires consulting a table, each model first had to pass a validity check fixed in advance: at least 7 of 13 categories read above chance and a median AUC of at least 0.65, on both codebooks. Five of nine models qualified. The other four returned the first code in the list for every stimulus.

<figure>
  <img src="/column-images/ssrn-steering-human-partition/gate3-1600.webp" alt="Gate III by model" />
  <figcaption><strong>Figure 4.</strong> For the five judged models: median excess with the same directions on the emotion-word readout (amber) and the code readout (blue), and with the gradient direction for the codes (light grey, positive control), codebook 1. Numbers above the bars are targets cleared.</figcaption>
</figure>

None of the five models met the criterion under either codebook. The second codebook is a derangement of the first, so no category keeps its letter, and the result is not an accident of one symbol assignment.

Two controls check whether the failure is a measurement artefact.

1. **Maybe the code readout cannot be moved at all.** The gradient direction for the code probabilities, at the same layer and strength, reached 13/13 in all five models, with a median of +5.95 SD. The readout can be moved.
2. **Maybe inserting the codebook changed the hidden state.** We kept the prompt prefix identical and changed only the final cue and the readout vocabulary.

<figure>
  <img src="/column-images/ssrn-steering-human-partition/paired-1600.webp" alt="Paired comparison behind an identical prefix" />
  <figcaption><strong>Figure 5.</strong> Comparison behind an identical prefix (medians over five models): +2.33 SD for emotion words, +0.45 SD for codes, +5.95 SD for the gradient direction.</figcaption>
</figure>

The emotion-word readout cleared 9.0 of 13 targets at +2.33 SD; the code readout cleared 3.0 at +0.45 SD. The median paired difference was +1.67 SD (range +0.90 to +2.70 across models), and the emotion-word excess was larger in 49 of 65 matched targets.

Readout quality does not explain it either. Gemma-2-9B and Mistral-Nemo-12B execute the codebook perfectly (13/13, AUC 0.897 and 0.771), and the same directions still barely moved the codes.

The effect is not zero, however. The code readout's p_G falls below 0.01 in 7 of 10 cells. In the paper's words, transfer across encodings is strongly attenuated rather than absent.

## Experiment 4: Differences between categories

<p class="experiment-label">Experiment 4</p>

Gate I judges families of directions, so we also looked at which categories move. These analyses are exploratory.

<figure>
  <img src="/column-images/ssrn-steering-human-partition/category-1600.webp" alt="Category-wise pass rates" />
  <figcaption><strong>Figure 6.</strong> Per category: number of models that beat the Gate I floor (single-token readout), and the emotion-word readout's AUC for that category. Amber marks surprise and fear, contrasted in the text.</figcaption>
</figure>

Surprise and trust beat the floor in all 9 models; fear did so in 3 and no-emotion in 2.

The readout's sharpness does not explain the spread. Fear is among the categories the readout separates best (AUC 0.968) and passes in 3/9, while surprise is among those it separates least well (0.860) and passes in 9/9. Ranking categories within each model by AUC and by excess gives a median Spearman correlation of +0.08 (−0.24 to +0.43). The amount of data does not explain it either: guilt and shame both have 275 rows but land at 4/9 and 8/9.

The appraisal-vocabulary readout is barely above chance (median AUC 0.553–0.597), so the paper does not conclude from the weak appraisal result (+0.39 SD) that appraisal dimensions are causally irrelevant.

## What we found, and what remains open

The paper arranges evidence about a direction as an ordered ladder.

| Evidence | What passing it supports | What it does not establish |
|---|---|---|
| Probe decodability | The attribute is linearly recoverable from the representation | That a particular direction carries it causally |
| Gate I | The direction's effect exceeds that of variance-matched alternatives | That the partition it came from is the one that matters |
| Gate II | The effect is specific to the human partition, relative to the same-grain partitions tested | That control extends beyond the encoding that was read |
| Gate III | The effect survives re-expressing the same categories in another encoding | Invariance across tasks, domains, languages or intervention sites |

Two findings stand out.

- The effect of directions built from human emotion categories is **specific to the human emotion partition**. It beat the variance-matched floor, random partitions and more decodable partitions in almost every model.
- Yet the same directions **lose most of their effect when the categories are re-encoded**, even in models that execute the codebook perfectly. Successful steering does not by itself establish an encoding-invariant semantic representation.

The paper's practical reading: when the output is itself an emotion label, as in classification or tagging, directions built on human labels gave a +2.83 SD advantage against the strictest matched floor. When the goal is to control the semantic properties of generated text, encoding invariance has to be checked separately.

There are limitations. The Gate III judgement rests on five of nine models, and most heavily on the two that execute the codebook perfectly. Gate III is a second encoding of the same ontology; no readout we built could resolve 13 categories without emotion words (the action-verb readout failed its validity check). The study uses one layer, one English corpus and one strength for the reported numbers. The nulls are finite, so p_G is a bootstrap tail estimate, not an exact probability. The codebook and vocabulary tables were built by the author and are not independently validated.

Next steps named in the paper are measuring emotion categories without emotion vocabulary, locating across layers where the binding arises, and testing generality with re-encodings models can carry out, such as another language.

The pre-registration record, the measurement code for every gate and control, and the statistics code that recomputes every reported number are at [github.com/keito-git/nativeaffect-prereg](https://github.com/keito-git/nativeaffect-prereg). This post describes a preprint that has not been peer reviewed.
