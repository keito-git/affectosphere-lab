---
title: "Can an LLM Match Taxonomists in Classifying Zooplankton Names?"
subtitle: "Applying large language models to expert-based etymological classification in zooplankton"
date: "2026-11-27"
excerpt: "We compared expert and LLM classifications of the epithet origins of 989 rotifers and microcrustaceans. Overall accuracy was 0.84 and κ 0.74. Morphology and People agreed closely, while the LLM strongly over-assigned Culture. A walk-through of our Journal of Plankton Research paper."
readingMinutes: 9
showImage: false
image: "/column-images/jpr-zooplankton-etymology/pipeline.png"
imageAlt: "Study pipeline. Expert-labelled zooplankton epithets are classified with GPT-4o-mini, and agreement and long-term trends are compared."
authors:
  - name: "Haruto Sugeno"
    affiliation: "Fukushima University"
  - name: "Keito Inoshita"
    url: "/en/about/"
    affiliation: "Kansai University"
  - name: "Kota Nojiri"
    affiliation: "The University of Tokyo"
tldr: "Etymological studies of scientific names rely on taxonomists reading original descriptions, which is slow. Using a dataset in which experts labelled the epithet origins of 989 zooplankton species (rotifers and microcrustaceans), we tested how closely GPT-4o-mini matches the experts. Overall accuracy was 0.84 and Cohen's κ 0.74. F1 was high for Morphology (0.92), People (0.91) and Geography (0.83), moderate for Ecology & Behavior (0.62) and low for Culture (0.20): many names the LLM called Culture were assigned elsewhere by experts. GAMs on yearly and decadal counts reproduced the long-term trends, with a significant difference between methods only for Culture at the yearly scale (P = 0.04)."
links:
  - label: "Paper (Journal of Plankton Research)"
    url: "https://doi.org/10.1093/plankt/fbag061"
citation: |
  @article{sugeno2026applying,
    title   = {Applying large language models to expert-based etymological
               classification in zooplankton},
    author  = {Sugeno, Haruto and Inoshita, Keito and Nojiri, Kota},
    journal = {Journal of Plankton Research},
    volume  = {48},
    number  = {5},
    pages   = {fbag061},
    year    = {2026},
    doi     = {10.1093/plankt/fbag061}
  }
---

<div class="teaser">
<div>

Agreement

Overall accuracy **0.84**, Cohen's κ **0.74**. All 989 species were classified in 14 minutes.

</div>
<div>

Strong

Morphology (F1 **0.92**) and People (**0.91**) reach precision 0.97 and match the experts closely.

</div>
<div>

Weak

Culture has F1 **0.20**. Precision is 0.12: the LLM labels too many names as Culture.

</div>
</div>

## Can an LLM stand in for expert etymological labels?

Species epithets come from morphology, ecology and behaviour, distribution, people, culture and more. Their origins underpin studies of naming history and debates such as gender imbalance in eponyms. Checking an origin, however, means reading the original description, which is hard when descriptions are old or give no etymology.

Zooplankton have many old original descriptions, yet new species are still being described. This makes them good for studying long-term naming trends, but also a hard case for etymological judgement.

The dataset of Macêdo et al. (2023) used here contains **etymological labels assigned by taxonomic experts** for rotifers and microcrustaceans. With expert labels as the reference, it is well suited to measuring the accuracy and biases of automated LLM classification. LLM-based etymology labelling had been tried on some arthropod groups; here we examined in detail where an LLM agrees with experts and where it does not.

## Method

<figure>
  <img src="/column-images/jpr-zooplankton-etymology/pipeline-1600.webp" alt="Study pipeline" />
  <figcaption><strong>Figure 1.</strong> Study pipeline. With expert labels as the reference, we measured the agreement of LLM labels and how well they reproduce long-term naming trends.</figcaption>
</figure>

The data are an open dataset of zooplankton species described between 1758 and 2021 (Macêdo et al., 2023). We analysed the 989 species whose publication years could be obtained.

The LLM was GPT-4o-mini via the OpenAI API, with temperature 0 and a few-shot prompt, classifying each epithet into five categories: Morphology, Ecology & Behavior, Geography, People and Culture.

With the expert labels as reference, we built a confusion matrix and computed accuracy, Cohen's κ, and per-category precision, recall and F1. Standardized residuals from a chi-squared test (with |r| > 2 as the threshold) showed which category pairs deviate. For long-term trends, we fitted quasi-Poisson GAMs to yearly and decade-binned counts and compared the expert and LLM curves.

## Experiment 1: How well do they agree overall?

<p class="experiment-label">Experiment 1</p>

<div class="setup">

**Setup**

- Data: epithets of 989 rotifer and microcrustacean species
- Reference: expert labels from Macêdo et al. (2023), five categories
- Metrics: accuracy, Cohen's κ, per-category precision, recall and F1

</div>

Overall accuracy was 0.84 and Cohen's κ was 0.74, which the paper describes as "substantial" agreement. Classifying all 989 epithets took 14 minutes, an average of 0.85 seconds per species.

<figure>
  <img src="/column-images/jpr-zooplankton-etymology/prf1-1600.webp" alt="Precision, recall and F1 by category" />
  <figcaption><strong>Figure 2.</strong> Precision, recall and F1 by category (Table I of the paper). Morphology and People are highest; Culture is lowest.</figcaption>
</figure>

| Category | Recall | Precision | F1 |
|---|---|---|---|
| Morphology | 0.87 | 0.97 | 0.92 |
| Ecology & Behavior | 0.52 | 0.75 | 0.62 |
| Geography | 0.91 | 0.76 | 0.83 |
| People | 0.86 | 0.97 | 0.91 |
| Culture | 0.64 | 0.12 | 0.20 |

F1 ranged widely, from 0.20 to 0.92. Morphology and People exceeded 0.9, and Geography reached 0.83. Ecology & Behavior was moderate at 0.62 and Culture low at 0.20.

## Experiment 2: Where do they disagree?

<p class="experiment-label">Experiment 2</p>

Looking at precision and recall separately shows different kinds of error.

<figure>
  <img src="/column-images/jpr-zooplankton-etymology/precision-recall-1600.webp" alt="Precision versus recall by category" />
  <figcaption><strong>Figure 3.</strong> Recall (x-axis) and precision (y-axis) by category. Morphology and People sit almost on top of each other in the upper right. Only Culture is far away.</figcaption>
</figure>

- **Morphology and People**: precision 0.97, so nearly every LLM label is right; recall is 0.86–0.87.
- **Geography**: recall 0.91 but precision 0.76, so the LLM uses this label somewhat broadly.
- **Ecology & Behavior**: precision 0.75 but recall 0.52, so nearly half of the expert-labelled names went to other categories.
- **Culture**: precision is only 0.12. Most names the LLM labelled Culture belonged to other categories for the experts.

The standardized residuals point the same way: the strongest positive residuals on the diagonal (correct matches) were for Morphology and People, while Culture had comparatively larger off-diagonal residuals. Culture-related names are where the LLM and the experts differ most.

## Experiment 3: Are long-term trends reproduced?

<p class="experiment-label">Experiment 3</p>

We modelled each category's counts over time with GAMs at yearly and decadal resolution, for both expert and LLM labels, and tested whether the curves differ.

| Category | Decade | Year |
|---|---|---|
| Morphology | P = NA | P = NA |
| Ecology & Behavior | P = NA | P = NA |
| Geography | P = NA | P = NA |
| People | P = NA | P = NA |
| Culture | P = 0.40 | **P = 0.04** |

In Table II of the paper, the P values for the four categories other than Culture are given as NA. **A significant difference between methods appeared only for Culture at the yearly scale.** The LLM labels reproduced long-term naming trends closely, and the discrepancy was limited to culture-related names.

## Experiment 4: How does this compare with another group?

<p class="experiment-label">Experiment 4</p>

We placed the F1 scores for the four shared categories next to our earlier study, which applied the same framework to phytophagous arthropods (Zoological Science, 2025).

<figure>
  <img src="/column-images/jpr-zooplankton-etymology/cross-taxa-f1-1600.webp" alt="F1 across two taxa" />
  <figcaption><strong>Figure 4.</strong> F1 for the four shared categories. Grey: phytophagous arthropods (Table 1 of the Zoological Science paper). Gold: zooplankton in this paper (Table I). The datasets and category definitions differ, so this is only a rough comparison.</figcaption>
</figure>

In both groups, Morphology, Geography and People are high and Ecology & Behavior is lowest. Values are higher overall for the expert-labelled zooplankton data. Because the datasets, the exact category definitions and the few-shot examples differ, the numerical gap should not be read directly as a difference in accuracy.

## What we found and what remains open

The study shows three things:

- On 989 expert-labelled zooplankton species, LLM labels reached substantial agreement: accuracy 0.84 and κ 0.74.
- Morphology and People agreed especially well (F1 0.92 and 0.91), while Culture had F1 0.20, with a bias toward over-assigning Culture.
- Yearly and decadal long-term trends were largely reproduced, with a significant difference only for Culture at the yearly scale.

There are limits. The LLM and the experts differed most on culture-related names, and recall for Ecology & Behavior was only 0.52. The paper recommends using LLM labels not as a replacement for expert judgement but as a complementary, human-in-the-loop tool for large-scale analyses.
