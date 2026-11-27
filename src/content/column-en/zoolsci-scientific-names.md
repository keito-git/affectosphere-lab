---
title: "Can an LLM Read Where Scientific Names Come From?"
subtitle: "Automated Labeling of Scientific Names and Etymological Trend Analysis in Phytophagous Arthropods Using Large Language Model"
date: "2026-11-27"
excerpt: "We used an LLM to classify the origins of the species epithets of 2,705 plant-feeding insects and mites. For morphology, host, geography and people, it agreed well with human labels and reproduced long-term naming trends. A walk-through of our Zoological Science paper."
readingMinutes: 10
showImage: false
image: "/column-images/zoolsci-scientific-names/pipeline.png"
imageAlt: "Study pipeline. The Heard et al. (2023) dataset is reorganised into six categories, labelled with GPT-4o mini, and compared with human labels."
authors:
  - name: "Kota Nojiri"
    affiliation: "The University of Tokyo"
  - name: "Keito Inoshita"
    url: "/en/about/"
    affiliation: "Kansai University"
  - name: "Haruto Sugeno"
    affiliation: "Fukushima University"
tldr: "Species epithets are named after many things: shape and colour, host plants, the place where a species was found, people, and more. Finding the origin of a name means reading the original description, which makes large-scale analysis slow. We classified the epithets of 2,705 phytophagous arthropods into six categories with GPT-4o mini and compared the result with human labels. For Morphology, Host, Geography and People, F1 was above 75%, accuracy was around 90%, and Cohen's κ was above 0.7. Ecology & Behavior and Other stayed in the 30% range for F1. Over time, morphology-based names declined while geography- and people-based names increased, the same pattern earlier work found in spiders, and the LLM labels reproduced it."
links:
  - label: "Paper (Zoological Science)"
    url: "https://doi.org/10.2108/zs250025"
citation: |
  @article{nojiri2025automated,
    title   = {Automated Labeling of Scientific Names and Etymological Trend
               Analysis in Phytophagous Arthropods Using Large Language Model},
    author  = {Nojiri, Kota and Inoshita, Keito and Sugeno, Haruto},
    journal = {Zoological Science},
    volume  = {42},
    number  = {5},
    year    = {2025},
    doi     = {10.2108/zs250025}
  }
---

<div class="teaser">
<div>

Accuracy

Morphology, Host, Geography and People reach **F1 above 75%**. The highest is Morphology at 82.6%.

</div>
<div>

Agreement

For the same four categories, **Cohen's κ is 0.70–0.76**. Ecology & Behavior and Other are around 0.3.

</div>
<div>

Trends

Both human and LLM labels show **fewer morphology names and more geography and people names** over time.

</div>
</div>

## Why the origin of a name is hard to trace

An animal's scientific name has two parts: the genus and the species epithet. As long as authors follow the minimum rules of the International Code of Zoological Nomenclature, they are free to choose the epithet. Origins are therefore diverse: shape and colour, habitat, distribution, people, and cultural background. For parasites and species that depend heavily on another organism, the epithet is sometimes the name of the host.

Scientific names have also become the subject of ethical debate. Examples are names that honour criminals or racists, and a gender imbalance in eponyms (names after people), of which about 90% commemorate men. Some call for revising the Code; others argue that nomenclatural stability should come first.

Statistics on name origins are the basis for such debates. Earlier studies, however, read the literature name by name and cross-checked random samples, which takes a great deal of effort. It is estimated that over 80% of arthropods are still undescribed, so spending large resources on analysing names that already exist is not practical.

Our earlier study (Inoshita et al., 2025) showed that an LLM can classify the origins of spider epithets about as well as human annotators. That result covered a single group, spiders. In this study we asked **whether the same works for phytophagous arthropods, a different group whose categories include Host**, and we also examined how naming trends changed over time.

## Method

<figure>
  <img src="/column-images/zoolsci-scientific-names/pipeline-1600.webp" alt="Study pipeline" />
  <figcaption><strong>Figure 1.</strong> Study pipeline. We reorganised the categories of an open dataset into six, labelled every epithet with GPT-4o mini, and compared the result with the human labels.</figcaption>
</figure>

We used the open etymological dataset of phytophagous arthropods published by Heard et al. (2023). It covers 30 species often studied for host-associated differentiation, together with the species of their genera, 2,709 species in total. Four species had no publication year and were removed, leaving 2,705 species.

The original dataset uses seven categories. To match earlier work, we reorganised them into six:

| Original category | Category in this study | Meaning |
|---|---|---|
| Morphology | Morphology | Morphological traits such as size, shape and colour |
| Host | Host | The host taxon |
| Place | Geography | Distribution or the site where the species was found |
| Behavior, Habitat | Ecology & Behavior | Habitat and behavioural traits |
| Person | People | Names honouring individuals, such as scientists |
| Other | Other | Names that fit none of the above |

The LLM was GPT-4o mini, accessed through OpenAI's API. We used the prompt from the earlier study and added few-shot examples suited to this group. With the human labels as ground truth, we computed accuracy, precision, recall and F1 per category, Cohen's κ, and the error in yearly counts (MAE). Temporal trends were analysed with generalized additive models (GAMs), which can capture gradual, non-linear changes in naming fashion.

## Experiment 1: How accurate is each category?

<p class="experiment-label">Experiment 1</p>

<div class="setup">

**Setup**

- Data: species epithets of 2,705 phytophagous arthropods
- Ground truth: human labels from Heard et al. (2023), reorganised into six categories
- Metrics: accuracy, precision, recall and F1 per category

</div>

<figure>
  <img src="/column-images/zoolsci-scientific-names/prf1-1600.webp" alt="Precision, recall and F1 by category" />
  <figcaption><strong>Figure 2.</strong> Precision, recall and F1 by category. The dashed line marks 75%. Morphology, Host, Geography and People exceed 75% F1; Ecology & Behavior and Other are in the 30% range.</figcaption>
</figure>

F1 was 82.6% for Morphology, 80.0% for People, 76.4% for Host and 75.8% for Geography, with a reasonable balance between precision and recall. For Host, precision was 89.1% and recall 66.9%: when the LLM said "host", it was usually right, but it put some human-labelled host names into other categories.

Ecology & Behavior (F1 31.7%) and Other (38.3%) were low. The earlier spider study also found low accuracy for Ecology & Behavior and for culture-related names. The paper suggests that one reason is the limited data on ecology and behaviour, which makes deep contextual meaning hard for the model to grasp.

<figure>
  <img src="/column-images/zoolsci-scientific-names/accuracy-vs-f1-1600.webp" alt="Accuracy versus F1 by category" />
  <figcaption><strong>Figure 3.</strong> Accuracy (squares) and F1 (circles) by category. Ecology & Behavior has the highest accuracy, 94.5%, but an F1 of only 31.7%.</figcaption>
</figure>

Accuracy alone is 85% or higher in every category. Ecology & Behavior is actually the highest at 94.5%. This happens because most species do not belong to that category, so answering "not this category" already scores well. To see whether a category is picked up correctly, F1 has to be read alongside accuracy.

## Experiment 2: How well does it agree with humans?

<p class="experiment-label">Experiment 2</p>

We computed Cohen's κ per category as a measure of agreement corrected for chance.

<figure>
  <img src="/column-images/zoolsci-scientific-names/kappa-1600.webp" alt="Cohen's kappa by category" />
  <figcaption><strong>Figure 4.</strong> Cohen's κ by category. The dashed line is 0.4, which the paper treats as acceptable agreement.</figcaption>
</figure>

Agreement was above 0.7 for all four main categories: People 0.758, Morphology 0.738, Geography 0.724 and Host 0.703. Ecology & Behavior (0.286) and Other (0.299) showed only fair agreement. The error in yearly counts (MAE) was below 1 in every category.

The LLM reproduces human labels well for the main categories, but it has limits for categories that are ambiguous or mix many kinds of names.

## Experiment 3: Does it produce the same category counts?

<p class="experiment-label">Experiment 3</p>

<figure>
  <img src="/column-images/zoolsci-scientific-names/counts-1600.webp" alt="Species counts by category" />
  <figcaption><strong>Figure 5.</strong> Number of species assigned to each category by human and LLM labelling, for the three categories whose counts are given in the paper's text.</figcaption>
</figure>

Overall, the number of species in each category was similar for both methods. The largest human categories were Morphology (894 species), Host (646) and People (534); the LLM likewise assigned the most species to Morphology (940), Host (486) and People (534). The LLM's smaller Host count matches the lower Host recall seen in Experiment 1.

## Experiment 4: How did naming change over time?

<p class="experiment-label">Experiment 4</p>

We estimated the change in each category's share over time with GAMs, fitting human and LLM labels in one model so their curves can be compared. Dispersion ratios were low (0.25 for the human model, 0.24 for the LLM model), showing no evidence of overdispersion.

| Category | Human labels | LLM labels |
|---|---|---|
| Morphology | Decline, with a trend shift around 1900 | Decline; the shift around 1900 does not appear |
| Host | Decline | Decline (different rate of decline) |
| Geography | Increase | Increase (nearly identical curve) |
| People | Increase | Increase (nearly identical curve) |
| Ecology & Behavior, Other | Patterns differ between methods | Patterns differ between methods |

The decline of morphology-based names and the rise of geography- and people-based names match earlier studies on spiders and rotifers, suggesting a general trend across taxa.

In the human labels, however, Morphology dropped sharply around 1900, and this change did not appear in the LLM curve. The paper concludes that **LLM labels are suitable for long-term trend analysis, but subtle changes may be missed**.

The paper suggests that the sharp drop around 1900 may relate to the rediscovery of Mendel's work and to new techniques such as electron microscopy, which shifted taxonomic descriptions toward genetic and ultrastructural perspectives. This is one interpretation, and the paper notes that the etymology of individual species needs closer study.

## What we found and what remains open

The study shows three things:

- For phytophagous arthropods too, LLM labels agree well with human labels for Morphology, Host, Geography and People (F1 above 75%, κ above 0.7). The method carries over to arthropods beyond spiders.
- LLM labels reproduce the long-term decline of morphology names and the rise of geography and people names. The classification took about one hour.
- Host-based names have declined. Earlier work found that species named after their hosts are more often chosen for host-associated differentiation studies, so naming practice may influence which species receive research attention.

There are limits. Ecology & Behavior and Other are still inaccurate and need human checking. The paper notes that checking only these categories by hand would still save effort overall. Subtle changes, such as the shift in Morphology around 1900, were missed by the LLM labels. Further evaluation on other taxa is needed.
