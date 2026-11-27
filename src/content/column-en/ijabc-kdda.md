---
title: "Can an LLM Generate Usable Emotion Data from 20 Example Sentences per Class?"
subtitle: "KDDA: A Knowledge-Driven Domain and Diversity Alignment Framework for Emotion Data Generation with Large Language Models"
date: "2026-11-27"
excerpt: "We propose KDDA, a framework that generates emotion data with an LLM without training on real data, guided only by style statistics taken from 20 sentences per class. A walk-through of our paper in the International Journal of Activity and Behavior Computing."
readingMinutes: 11
showImage: false
image: "/column-images/ijabc-kdda/overview.png"
imageAlt: "KDDA overview. A domain profile built from human prior knowledge guides LLM generation, Jaccard filtering and NLL-based selection, which together build up the synthetic dataset."
authors:
  - name: "Keito Inoshita"
    url: "/en/about/"
    affiliation: "Kansai University"
  - name: "Hayato Tomisu"
  - name: "Xiaokang Zhou"
  - name: "Akira Kawai"
  - name: "Katsutoshi Yada"
tldr: "Emotion data are hard to collect. KDDA uses only 20 sentences per class as domain knowledge and turns them into statistical distributions of features such as sentence length, comma count and topic (a domain profile). The LLM writes six candidates at a time under this profile; candidates that are too similar to existing data are dropped by Jaccard similarity, and one is selected by its NLL under the profile. A DistilBERT trained only on KDDA data reaches 0.826 accuracy on IMDb and 0.405 on Emotions, above the four compared methods. On Yelp it ties AGOS at 0.872."
citation: |
  @article{inoshita2026kdda,
    title   = {{KDDA}: A Knowledge-Driven Domain and Diversity Alignment Framework
               for Emotion Data Generation with Large Language Models},
    author  = {Inoshita, Keito and Tomisu, Hayato and Zhou, Xiaokang and
               Kawai, Akira and Yada, Katsutoshi},
    journal = {International Journal of Activity and Behavior Computing},
    volume  = {1},
    pages   = {1--24},
    year    = {2026}
  }
---

<div class="teaser">
<div>

Profile

The only real data used are **20 sentences per class**, and only their statistics (length, commas and so on) are kept, not their content.

</div>
<div>

Select

From six candidates, **drop the ones that are too similar** and keep the one that best fits the domain distribution.

</div>
<div>

Train

A classifier trained only on generated data reaches 0.826 on IMDb and 0.405 on Emotions, above the four compared methods.

</div>
</div>

## Why emotion data run short

Emotion recognition models depend heavily on human-labeled data, and emotion data are harder to collect than most language data. In workplaces, healthcare and education, participants' psychological burden and the purpose of data use are closely scrutinized. When children or older adults are involved, ethical review is stricter still. As a result, the available emotion datasets lean toward open sources such as tweets and product reviews.

This study asks whether emotion data can be produced **without using real data directly for training or generation**. Human knowledge is not discarded entirely: we keep knowledge about the target domain, such as "people tend to write this way in this setting", and use it to guide an LLM to write plausible emotional sentences.

If an LLM is simply given emotion labels and asked to write a lot, two problems appear. The sentences become similar to one another (too little diversity), and they drift away from how the target domain is actually written (domain mismatch). KDDA is designed to control both at once.

## How KDDA works

<figure>
  <img src="/column-images/ijabc-kdda/overview-1600.webp" alt="KDDA framework overview" />
  <figcaption><strong>Figure 1.</strong> Overview of KDDA (figure from the paper). Left: building the domain profile. Center: generation and diversity expansion. Right: NLL-based domain alignment.</figcaption>
</figure>

KDDA works in three stages.

1. **Domain profile construction.** We take 20 representative sentences per emotion class from the target domain. Rule-based parsing counts ten feature categories, including sentence length, comma count, clause type, type of the first word, topic and whether an emotion adjective is explicit. The per-class probability distribution P_e over these features is the domain profile. No LLM is used at this stage.
2. **Generation and diversity expansion.** A feature specification (e.g., "19–26 words, one comma, topic: work") is sampled from P_e and written into the prompt as natural-language constraints. Recently accepted sentences and sentences to avoid are added to the prompt as negative examples, and the LLM is told to write something different. It writes six candidates per call. A candidate is discarded as redundant if its word-level Jaccard similarity to the synthetic data is 0.62 or more, or its bigram Jaccard similarity is 0.40 or more.
3. **NLL-based selection.** For each remaining candidate, we compute how well the sentence alone fits P_e (local NLL) and how close the whole dataset's feature distribution gets to P_e once the sentence is added (global NLL). One candidate is chosen by comparing global NLL first, then local NLL, then a diversity score, and is added to the dataset.

The LLM's parameters are never changed. All control comes from the prompt and from statistics-based selection.

## Experimental setup

<div class="setup">

**Setup**

- Real data (Golden): IMDb (movie reviews, positive/negative), Yelp (business reviews, positive/negative), Emotions (Twitter; joy, anger, sadness, love, surprise, fear)
- Domain knowledge: 20 random sentences per class from each dataset, used only for feature extraction and excluded from training and test sets
- Amount generated: 2,500 per class for the binary datasets (5,000 total), 1,000 per class for Emotions (6,000 total); the same for every compared method
- LLM: GPT-4.1-mini-2025-04-14 with default parameters
- Compared methods: LOZP (label-only zero-shot), CAZP (directive prompts such as "write a positive sentence"), AGOS (generation conditioned on persona and other attributes), ARISE (rule induction with bootstrapped synthetic data)
- Test: 2,000 real texts with no overlap; mean of three random seeds

</div>

Four metrics describe the distributions. All are computed on all-MiniLM-L6-v2 sentence embeddings, and **a value closer to the real data (Golden) is better**.

| Metric | What it measures |
|---|---|
| MCD (Mean Cosine Distance) | Average cosine distance between sentences; larger means more varied |
| CE (Cluster Entropy) | How evenly the data spread across clusters in embedding space |
| FID (Fréchet Inception Distance) | Distance between the generated and real distributions; 0 for Golden |
| CD (Centroid Distance) | Distance between class centroids; how well classes separate |

## Experiment 1: Do the generated data resemble real data?

<p class="experiment-label">Experiment 1</p>

<figure>
  <img src="/column-images/ijabc-kdda/distance-to-golden-1600.webp" alt="Distance to Golden for four distribution metrics" />
  <figcaption><strong>Figure 2.</strong> Absolute difference between each method's value and Golden (real data). Shorter is closer to real data; the outlined bar is the closest method in each cell. KDDA is in amber.</figcaption>
</figure>

On MCD, KDDA is closest to Golden on all three datasets, with gaps of only 0.040 on Yelp and 0.086 on Emotions, so it keeps a degree of variety close to real data. On FID, KDDA is closest on IMDb and Emotions; on Yelp, AGOS (0.477) is marginally ahead of KDDA (0.483). On CD, KDDA is closest on Yelp and Emotions, while ARISE is closest on IMDb.

CE is KDDA's weak spot. CAZP is closest on Yelp and Emotions, and KDDA's values sit slightly below Golden.

The largest margin appears on the six-class Emotions dataset. KDDA's FID is 0.388, against 0.477 for the next best method (AGOS), and its CD is 0.292, while the closest baseline (AGOS) is at 0.477. ARISE drifts far on Emotions (FID 0.657, CD 0.768), which the paper reads as instability in multi-class settings.

The paper summarizes that KDDA is closest to Golden in 9 of the 12 metrics. Counting the bold cells in the table gives 8 for KDDA (MCD, CE and FID on IMDb; MCD and CD on Yelp; MCD, FID and CD on Emotions).

## Experiment 2: Training a classifier on generated data only

<p class="experiment-label">Experiment 2</p>

We trained DistilBERT only on each method's generated data and tested on 2,000 real texts (3 epochs for IMDb and Yelp, 5 for Emotions, batch size 128). Golden is the same model trained on the same number of real texts and serves as an upper reference.

<figure>
  <img src="/column-images/ijabc-kdda/classification-1600.webp" alt="Classification accuracy on real test data" />
  <figcaption><strong>Figure 3.</strong> Accuracy of DistilBERT trained only on generated data (mean and standard deviation over three seeds). The dashed line is Golden, trained on the same number of real texts.</figcaption>
</figure>

| Dataset | Golden | LOZP | CAZP | AGOS | ARISE | KDDA |
|---|---|---|---|---|---|---|
| IMDb (F1) | 0.863 | 0.692 | 0.799 | 0.808 | 0.811 | **0.824** |
| Yelp (F1) | 0.889 | 0.802 | 0.771 | 0.872 | 0.849 | **0.872** |
| Emotions (F1) | 0.460 | 0.193 | 0.358 | 0.283 | 0.269 | **0.386** |

On IMDb, KDDA reaches 0.826 accuracy and 0.824 F1, above every baseline. On Yelp it ties AGOS at 0.872 accuracy. Emotions is harder for every method because the six class boundaries overlap, but KDDA's 0.405 accuracy is above the best baseline, CAZP, at 0.371. ARISE varies strongly across seeds on Emotions (standard deviation 0.124).

A gap to Golden remains: 0.037 on IMDb and 0.054 on Emotions. Generated data alone did not reach the level of real data.

## Experiment 3: Which emotions get confused?

<p class="experiment-label">Experiment 3</p>

<figure>
  <img src="/column-images/ijabc-kdda/confusion-matrices-1600.webp" alt="Confusion matrices on the Emotions dataset" />
  <figcaption><strong>Figure 4.</strong> Confusion matrices on Emotions (figure from the paper). Rows are true labels, columns are predictions. (a) is Golden, trained on real data; (f) is KDDA.</figcaption>
</figure>

LOZP and AGOS lean toward predicting fear: the fear column is large for almost every true class, a sign that their generated data collapsed onto a few expressions. KDDA's matrix has a clearer diagonal. It gets 116 joy and 107 anger texts right, the most among all six methods for those two classes.

Fear and sadness are harder. 77 sadness texts are predicted as anger, and fear is spread across anger and sadness. However, even Golden, trained on real data, predicts 68 fear texts as sadness. The paper interprets this confusion as coming from the semantic overlap among negative emotions rather than from the generation mechanism.

## Experiment 4: Distributions in embedding space

<p class="experiment-label">Experiment 4</p>

We embedded the generated Emotions data into 384 dimensions and projected them to two dimensions with Independent Component Analysis (ICA). Each ellipse marks the mean ± 2 standard deviations of the real data for one class, that is, where real data are expected to lie.

<figure>
  <img src="/column-images/ijabc-kdda/feature-distribution-1600.webp" alt="ICA projection of real and synthetic embeddings" />
  <figcaption><strong>Figure 5.</strong> Generated data (points) against the range of real data (ellipses), figure from the paper. Colors are emotion classes. (e) is KDDA.</figcaption>
</figure>

LOZP forms clear clusters per emotion, but their centers sit far from the real ellipses. ARISE also forms clear clusters but does not cover the real distribution. AGOS spreads widely, with only about half of its points inside the ellipses. KDDA's points gather inside the ellipses with few outliers.

## Experiment 5: Which components matter?

<p class="experiment-label">Experiment 5</p>

On Emotions, we removed KDDA's components one at a time.

<figure>
  <img src="/column-images/ijabc-kdda/ablation-1600.webp" alt="Ablation study on Emotions" />
  <figcaption><strong>Figure 6.</strong> Absolute difference from Golden after removing each component (Emotions). The full model is in amber.</figcaption>
</figure>

The full model is closest to Golden on MCD, FID and CD. On CE alone it is the furthest (gap 0.102); the paper attributes this to moderate cohesion within clusters rather than over-dispersion.

Each component plays a different role.

- Removing the **domain profile** causes the largest drift: FID 0.604 and CD 0.498. It is the core of distributional alignment.
- Removing **negative examples** drops MCD to 0.542 (Golden: 0.804), with many repeated, safe sentences.
- Removing the **Jaccard filter** also lowers diversity.
- Removing the **NLL filters** moderately widens the gap in FID and CD; the paper sees them as stabilizers that fine-tune global consistency.

## What we know and what we don't

The study shows the following.

- Style statistics from only 20 sentences per class are enough to steer LLM generation toward a target domain. Classifiers trained only on KDDA data beat the four compared methods on IMDb and Emotions and tie AGOS on Yelp.
- The domain profile aligns the distribution, while negative examples and the Jaccard filter expand diversity.
- The margin is largest on multi-class Emotions, where KDDA's FID of 0.388 is the closest to real data.

There are limits.

- The domain profile depends on human prior knowledge. We used 20 sentences, but the form and amount of knowledge may change the results, and cultural or linguistic biases in that knowledge can carry over to the generated data.
- A gap to models trained on real data remains. How much synthetic training is needed for reliable generalization to real settings is still unclear.
- The evaluation covers three English datasets, relatively few emotion classes and a GPT-family LLM. In finer-grained taxonomies or other languages, separating close emotions such as sadness and anger may become harder.

Next, we plan to try other forms of domain knowledge, such as descriptive guidelines, to extend KDDA to multilingual settings, and to evaluate it on finer-grained emotion taxonomies.
