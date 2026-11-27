---
title: "Can a CNN Catch Sarcasm by Looking at Several Scales at Once?"
subtitle: "Multi-Scale Convolutional Fusion with Contrastive Feature Alignment for Imbalanced Data Classification"
date: "2026-11-27"
excerpt: "To detect sarcasm, where the literal meaning and the intent point in opposite directions, we combined MSCF, which looks at several scales at once through convolutions with different dilation rates, and CFA, which pulls classes apart with contrastive learning. A walk-through of our NLDB 2025 paper, which received the Best Paper Award."
readingMinutes: 10
showImage: false
image: "/column-images/nldb2025-multiscale-fusion/architecture.png"
imageAlt: "MSCF-CFA framework. RoBERTa embeddings pass through MF-CNN for local features, MSCF for multi-scale fusion, and CFA for contrastive feature alignment before classification."
authors:
  - name: "Keito Inoshita"
    url: "/en/about/"
    affiliation: "Kansai University"
  - name: "Takato Ueno"
    affiliation: "Shiga University"
  - name: "Xiaokang Zhou"
    affiliation: "Kansai University / RIKEN Center"
tldr: "Sarcasm says the opposite of what it means, which hurts sentiment analysis and opinion mining. We propose MSCF-CFA. It builds on a Multi-Filter CNN (MF-CNN) and adds MSCF, which runs convolutions with dilation rates 1, 2 and 4 in parallel; CFA, which expands the feature space and separates classes with contrastive learning; and a weighted cross-entropy (WCE) that up-weights minority classes. On a sarcasm detection dataset of 3,834 texts it reaches an F1 of 79.37%, ahead of all six baselines on every metric (the best baseline, RoBERTa+DBLoss, reaches 75.14%). Removing any component lowers F1 by 0.6 to 1.7 points, and removing WCE causes the largest drop."
links:
  - label: "Paper (NLDB 2025)"
    url: "https://doi.org/10.1007/978-3-031-97141-9_1"
citation: |
  @inproceedings{inoshita2025mscfcfa,
    title     = {Multi-Scale Convolutional Fusion with Contrastive Feature Alignment
                 for Imbalanced Data Classification},
    author    = {Inoshita, Keito and Ueno, Takato and Zhou, Xiaokang},
    booktitle = {Natural Language Processing and Information Systems (NLDB 2025)},
    series    = {Lecture Notes in Computer Science},
    volume    = {15836},
    year      = {2025},
    doi       = {10.1007/978-3-031-97141-9_1}
  }
---

<div class="teaser">
<div>

Compare

F1 of **79.37%**, 4.23 points above the best of six baselines (RoBERTa+DBLoss, 75.14%).

</div>
<div>

Ablate

**Removing any of MSCF, CFA or WCE hurts.** Removing WCE hurts most, with F1 falling to 77.66%.

</div>
<div>

Visualize

In PCA, **sarcastic and non-sarcastic texts move to opposite ends** as features pass MF-CNN, MSCF and CFA.

</div>
</div>

## Why sarcasm is hard

Automatic analysis of posts on social media and review sites now supports marketing and the tracking of social trends. Sarcasm is a persistent problem here. "What a wonderful weather!" can be a complaint about bad weather. Because **the literal meaning and the intent are opposite**, standard text classifiers misread such texts.

For sarcasm detection, CNNs have outperformed RNNs because they are good at extracting local expressions. A common choice is the Multi-Filter CNN (MF-CNN), which captures n-gram features with filters of several sizes. The paper identifies three limits of MF-CNN.

1. With only a few kernel sizes, it struggles to capture **long-range and multi-scale dependencies**.
2. Features of the same class are not pulled together enough, and features of different classes are not pushed apart enough, so **the embeddings lack discriminative power**.
3. Sarcastic texts are often a minority, and under **class imbalance** the model leans toward the majority class.

MSCF-CFA adds one component for each of these limits.

## How MSCF-CFA works

<figure>
  <img src="/column-images/nldb2025-multiscale-fusion/architecture-1600.webp" alt="MSCF-CFA framework overview" />
  <figcaption><strong>Figure 1.</strong> Overview of MSCF-CFA (Figure 1 of the paper). From left to right: RoBERTa embedding, local feature extraction by MF-CNN, multi-scale fusion by MSCF, and feature alignment and classification by CFA.</figcaption>
</figure>

The pipeline has four stages.

1. **Embedding.** Each text is tokenized and turned into a sequence of 768-dimensional vectors (length 128) by a pre-trained RoBERTa.
2. **MF-CNN.** 2D convolutions with filter sizes 2, 3 and 4 (100 filters each) capture bigram- and trigram-like features. Max pooling and a linear layer reduce them to 256 dimensions.
3. **MSCF (Multi-Scale Convolutional Fusion).** 1D convolutions with dilation rates 1, 2 and 4 run in parallel. Their outputs are concatenated and linearly transformed, with a residual connection and Layer Normalization. Two such blocks are stacked.
4. **CFA (Contrastive Feature Alignment).** Features are expanded into four feature spaces, averaged, and projected to 64 dimensions. A contrastive loss (temperature τ = 0.7) on this projection pulls same-class samples together and pushes different classes apart.

<figure>
  <img src="/column-images/nldb2025-multiscale-fusion/mscf.png" alt="Mechanism of MSCF" />
  <figcaption><strong>Figure 2.</strong> The MSCF block (Figure 2 of the paper). Each branch uses a different dilation rate, so the block sees short-range and long-range dependencies at the same time.</figcaption>
</figure>

<figure>
  <img src="/column-images/nldb2025-multiscale-fusion/cfa.png" alt="Mechanism of CFA" />
  <figcaption><strong>Figure 3.</strong> The CFA module (Figure 3 of the paper). Features are expanded into several spaces, averaged, projected to a low dimension, and trained with a contrastive loss.</figcaption>
</figure>

A classifier then predicts the class. The loss is the sum of a cross-entropy weighted by inverse class frequency (WCE) and the contrastive loss, with weight α = 0.1 on the contrastive term. WCE increases the loss of minority classes so that the model does not neglect them.

## Experiment 1: Comparison with existing methods

<p class="experiment-label">Experiment 1</p>

<div class="setup">

**Setup**

- Data: a sarcasm detection dataset (3,834 texts labeled "sarcasm" or "non-sarcasm"), 80% train / 20% test
- Embedding: pre-trained RoBERTa (768 dimensions)
- Baselines: MF-CNN, BiLSTM, Transformer, DualCL (contrastive learning), RoBERTa+DBLoss (a loss for imbalanced data), MHA-BiLSTM (sarcasm-specific)
- Training: batch size 64, 100 epochs, learning rate 1e-4
- Metrics: Accuracy, Precision, Recall, F1

</div>

<figure>
  <img src="/column-images/nldb2025-multiscale-fusion/main-results-1600.webp" alt="F1 of all models" />
  <figcaption><strong>Figure 4.</strong> F1 on the test set. Grey is the MF-CNN backbone; blue is RoBERTa+DBLoss, the best baseline. The x-axis starts at 65%.</figcaption>
</figure>

| Model | Accuracy | Precision | Recall | F1 |
|---|---|---|---|---|
| MF-CNN | 74.84 | 75.88 | 74.88 | 74.60 |
| BiLSTM | 71.58 | 71.82 | 71.60 | 71.51 |
| Transformer | 74.45 | 75.10 | 74.41 | 74.26 |
| DualCL | 69.49 | 69.61 | 69.51 | 69.45 |
| RoBERTa+DBLoss | 75.23 | 75.53 | 75.21 | 75.14 |
| MHA-BiLSTM | 73.66 | 73.98 | 73.69 | 73.59 |
| **MSCF-CFA** | **79.40** | **79.58** | **79.42** | **79.37** |

MSCF-CFA scores highest on all four metrics. Its accuracy is 4.17 points above that of RoBERTa+DBLoss (75.23%), the best baseline. The MF-CNN backbone alone reaches 74.84%, above BiLSTM (71.58%) and Transformer (74.45%), which suggests that CNNs that capture local features suit this task.

<figure>
  <img src="/column-images/nldb2025-multiscale-fusion/metrics-1600.webp" alt="Four metrics for three models" />
  <figcaption><strong>Figure 5.</strong> All four metrics for the MF-CNN backbone, the best baseline and MSCF-CFA. The gain is not limited to precision; all four metrics rise together.</figcaption>
</figure>

We also compared training loss curves (Figure 4 of the paper). MF-CNN, the simplest model, reduces its loss fastest. MSCF-CFA starts more slowly but converges around epoch 40 and ends with a lower loss than the other models.

## Experiment 2: How the features change stage by stage

<p class="experiment-label">Experiment 2</p>

To see what each component does to the features, we projected the features after MF-CNN, after MSCF and after CFA onto two dimensions with PCA.

<figure>
  <img src="/column-images/nldb2025-multiscale-fusion/pca-1600.webp" alt="PCA of features after each module" />
  <figcaption><strong>Figure 6.</strong> PCA of the features at each stage (Figure 5 of the paper): (a) after MF-CNN, (b) after MSCF, (c) after CFA. Label 1 is sarcasm and Label 0 is non-sarcasm.</figcaption>
</figure>

- **(a) After MF-CNN.** Sarcastic points tend toward the right but overlap heavily with non-sarcastic ones.
- **(b) After MSCF.** Sarcastic points shift right and non-sarcastic points shift left, so the overlap shrinks. Some ambiguous points remain in the center.
- **(c) After CFA.** The two classes sit at opposite ends of the space, and far fewer ambiguous points remain in the center.

This suggests that CFA, which expands the feature space and applies contrastive learning, strengthens class separation. Even in (c), however, some points stay in the center, which leads to the limits discussed below.

## Experiment 3: Which components matter

<p class="experiment-label">Experiment 3</p>

We built models without MSCF, without CFA and without WCE, and compared them with the full model.

<figure>
  <img src="/column-images/nldb2025-multiscale-fusion/ablation-1600.webp" alt="Ablation study" />
  <figcaption><strong>Figure 7.</strong> F1 with one component removed. Values in parentheses are the change from the full model. The x-axis starts at 76%.</figcaption>
</figure>

| Model | Accuracy | Precision | Recall | F1 |
|---|---|---|---|---|
| MSCF-CFA | 79.40 | 79.58 | 79.42 | 79.37 |
| w/o MSCF | 78.75 | 78.83 | 78.76 | 78.74 |
| w/o CFA | 78.75 | 78.84 | 78.74 | 78.73 |
| w/o WCE | 77.71 | 77.91 | 77.69 | 77.66 |

Removing MSCF or CFA lowers F1 by about 0.6 points. Removing WCE lowers it by 1.71 points, the largest drop of the three. Every component contributes, and the loss weighting matters most for keeping the classes balanced.

## What we know and what we don't

The study shows the following.

- Adding dilated convolutions at several rates (MSCF) and contrastive feature alignment (CFA) on top of a multi-filter CNN gave higher sarcasm detection accuracy than the baselines.
- In stage-by-stage PCA, class separation became clearer after MSCF and again after CFA.
- MSCF, CFA and WCE all contribute, and WCE contributes most.

There are limits. Even after CFA, the PCA shows ambiguous points that likely need deeper understanding of the text or extra input. Labeled sarcasm data are scarce, and annotation is inconsistent. The multi-scale convolutions and expanded feature spaces add parameters, which makes deployment harder in resource-constrained settings. The evaluation also uses one dataset and one split, and the paper does not report variation across seeds.

Future work includes complementing the input text, enlarging training data with weakly and self-supervised learning, and making the model lighter with distillation, quantization and pruning.

This paper received the Best Paper Award at NLDB 2025.
