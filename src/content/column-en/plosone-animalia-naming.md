---
title: "What Do 1.5 Million Animal Names Say About the History of Taxonomy?"
subtitle: "Historical, taxonomic, and cultural patterns in scientific naming across Animalia"
date: "2026-11-27"
excerpt: "We used an LLM to classify the origins of about 1.54 million valid animal names and traced more than 250 years of naming history. Descriptions dropped during the world wars, naming shifted from morphology to places and people, and patterns differed by phylum and by authors' region. A walk-through of our PLOS One paper."
readingMinutes: 12
showImage: false
image: "/column-images/plosone-animalia-naming/pipeline.png"
imageAlt: "Study pipeline. Categories are designed on a spider dataset, every Animalia name is labelled by an LLM, 240 names are validated by hand, and then the analyses are run."
authors:
  - name: "Kota Nojiri"
    affiliation: "The University of Tokyo"
  - name: "Keito Inoshita"
    url: "/en/about/"
    affiliation: "Kansai University"
  - name: "Haruto Sugeno"
    affiliation: "Fukushima University"
  - name: "Takumi Taga"
    affiliation: "Nagoya University"
tldr: "Species epithets record not only biology but also the people and times that produced them. Earlier etymological studies covered single groups such as spiders or molluscs. We classified all valid animal names in the Catalogue of Life into four categories (Morphology, Geography, People, Other) with an LLM (GPT-4.1-mini) and studied naming history across Animalia. On 240 hand-checked names, agreement was 86.7%. Descriptions dropped sharply in the 1920s and 1950s, the share of morphology names fell, and geography and people names rose. Naming also differed among phyla and among author regions inferred from names. Individual names remain uncertain to classify, but consistent patterns appear at large scale."
links:
  - label: "Paper (PLOS One)"
    url: "https://doi.org/10.1371/journal.pone.0353612"
  - label: "Code (Zenodo)"
    url: "https://doi.org/10.5281/zenodo.19364291"
citation: |
  @article{nojiri2026historical,
    title   = {Historical, taxonomic, and cultural patterns in scientific
               naming across Animalia},
    author  = {Nojiri, Kota and Inoshita, Keito and Sugeno, Haruto and Taga, Takumi},
    journal = {PLOS One},
    volume  = {21},
    number  = {7},
    pages   = {e0353612},
    year    = {2026},
    doi     = {10.1371/journal.pone.0353612}
  }
---

<div class="teaser">
<div>

History

Descriptions **dropped in the 1920s and 1950s**, a pattern seen in almost every phylum.

</div>
<div>

Taxonomy

Across Animalia, **morphology names declined while geography and people names rose**, but each phylum has its own path.

</div>
<div>

Culture

Patterns differ by inferred author region: **European names favour morphology**, Latin American names favour people.

</div>
</div>

## What scientific names record

Binomial nomenclature has served as the common framework for naming animals for more than 250 years. A species epithet can encode morphology, ecology and behaviour, geographic origin, cultural references, or the names of people linked to the research. A scientific name is therefore both a taxonomic label and a record of how people have observed and valued organisms.

Parts of this record have recently drawn attention: the gender imbalance in eponyms (names honouring people) and names referring to historically controversial individuals. Quantifying long-term naming trends gives useful context for such debates.

Systematic studies of epithet etymology are still rare. They have covered specific groups such as helminths, phytophagous arthropods, molluscs, planarians, rotifers, decapods and spiders. These studies found that morphology-based names declined and geography- and people-based names increased. Whether this is a local pattern or one shared across Animalia was unknown.

Tracing an etymology means reading original descriptions and knowing Latin and Greek, so doing this by hand for all animals is not feasible. Earlier work showed that LLMs can classify epithets with around 90% accuracy, so this study set out to **reconstruct the naming history of all Animalia quantitatively with an LLM for the first time**. The aim is not to judge whether particular names are appropriate, and the paper makes no normative claim about how species should be named.

## Method

<figure>
  <img src="/column-images/plosone-animalia-naming/pipeline-1600.webp" alt="Study pipeline" />
  <figcaption><strong>Figure 1.</strong> Study pipeline. We designed the categories on spider data, labelled every Animalia name with an LLM, validated the labels by hand, merged them into four categories, and then ran the analyses.</figcaption>
</figure>

**Category design.** Category definitions in earlier etymological studies varied, which made them hard to compare. We clustered semantic embeddings of the 48,464 spider epithets compiled by Mammola et al. with K-means. Seven coherent clusters emerged. Morphology showed clear substructure, while Ecology & Behavior and Culture did not form clusters. From this we defined six categories:

| Category | Meaning | Examples |
|---|---|---|
| Abstract Morphology | General appearance or abstract traits, such as size, texture or overall impression | hirtus, pusillus, maximus |
| Specific Morphology | Visually verifiable features, such as colour, pattern or particular structures | quadrifasciatus, tenuipes, spinulatus |
| Conceptual Morphology | Metaphorical or conceptual interpretations of morphology | unica, diabolica, diversa |
| Geography | Distribution or the locality where the species was first found | taiwanensis, tibetensis, japonica |
| People | People associated with the species or the authors | lorenzoi, rovertsi, soyoae |
| Other | Names that fit none of the above | – |

On a random subset of 5,000 Animalia species, principal component analysis showed that names in the same category formed coherent clusters.

**LLM labelling.** We took every currently accepted animal name with a publication year from the Catalogue of Life and labelled it with GPT-4.1-mini (temperature 0) into the six categories. A name could receive more than one label. People was first split into Male and Female, but Female labels were so rare that the two were merged.

**Author region.** For each author string, the LLM estimated the most plausible country of origin from the name alone. Countries were grouped into six broad cultural classes: African, East Asian, European, Latin American, Middle Eastern and South Asian names. No ground truth exists for historical authors, so these labels are broad, name-based regional proxies, not individual nationality. A sanity check of 236 sampled names found most assignments broadly plausible at the regional level.

**Analyses.** We counted names per year, modelled each category's share over time with quasibinomial GAMs, and drew heatmaps of category shares by phylum and by author region.

## Experiment 1: How far can the LLM labels be trusted?

<p class="experiment-label">Experiment 1</p>

<div class="setup">

**Setup**

- Validation set: 240 epithets, stratified so that each time period (4) × category (6) cell has at least 10
- Ground truth: manual labels based on original descriptions (cases that could not be judged were excluded)
- Metric: agreement between manual and LLM labels

</div>

<figure>
  <img src="/column-images/plosone-animalia-naming/validation-1600.webp" alt="Validation agreement" />
  <figcaption><strong>Figure 2.</strong> Agreement on the validation set. With six categories it was 76.7%. Merging the three morphology categories raised Morphology to 93.3% and the four-category total to 86.7%.</figcaption>
</figure>

Pooled agreement with six categories was 76.7%. It was highest for Specific Morphology, Geography and People, and lower for Conceptual Morphology and Other. When the three morphology categories were treated as one, Morphology agreement rose to 93.3% and overall agreement to 86.7%.

Most errors were therefore confusions among the morphology sub-categories, with few errors between morphology and the other categories. All later analyses use **four categories: Morphology, Geography, People and Other**.

## Experiment 2: How did the number of descriptions change?

<p class="experiment-label">Experiment 2</p>

<figure>
  <img src="/column-images/plosone-animalia-naming/paper-fig1-1600.webp" alt="Annual counts by naming category across Animalia" />
  <figcaption><strong>Figure 3.</strong> Annual number of Animalia species in each naming category. Reproduced from Fig 1 of the paper (CC BY 4.0).</figcaption>
</figure>

New descriptions increased after the mid-19th century, and every category grew in absolute numbers. The striking features are **sharp drops around the 1920s and the 1950s**, visible in almost all phyla.

The paper links these drops to the disruption of World War I (1914–1918) and World War II (1939–1945), when scientific personnel and resources were redirected to the war effort. Groups with long, stable research attention, such as Chordata, Cnidaria, Echinodermata and Rotifera, showed more muted declines.

## Experiment 3: Which categories rose and which fell?

<p class="experiment-label">Experiment 3</p>

To look at shares rather than counts, we estimated the proportion of each category with GAMs.

<figure>
  <img src="/column-images/plosone-animalia-naming/paper-fig3-1600.webp" alt="GAM-estimated proportions across Animalia" />
  <figcaption><strong>Figure 4.</strong> Change in category shares across Animalia (GAM, bands are 95% confidence intervals). Reproduced from Fig 3 of the paper (CC BY 4.0).</figcaption>
</figure>

Across Animalia, **the share of Morphology declined over the past two centuries, while Geography and People rose continuously** and became dominant in modern naming. This matches trends reported for individual groups.

The paper suggests one explanation: better optical microscopes, electron microscopy and molecular techniques such as PCR and DNA sequencing allowed taxonomists to split morphologically similar species. When species are separated by subtle differences that are hard to express in an epithet, place and person names may become more practical.

Phyla differ, however:

| Phylum | Trend reported in the paper |
|---|---|
| Arthropoda | Nearly identical to Animalia as a whole |
| Nematoda, Rotifera | Declining use of People from around 2000 |
| Annelida, Bryozoa, Porifera | People increased around 2000 |
| Bryozoa | After 2000, both People and Geography increased |
| Chordata | Relatively high People share through the 19th century; sharp rise of Geography around 2000 |
| Rotifera | People rose from around the 1950s and then declined; Morphology declined monotonically throughout |

For Bryozoa's sharp post-2000 rise, the paper points to a small community of describers: 1,680 species were described after 2000, but only 260 distinct author patterns appear. The preferences of a few taxonomists may therefore dominate the pattern.

## Experiment 4: Do phyla have their own naming cultures?

<p class="experiment-label">Experiment 4</p>

<figure>
  <img src="/column-images/plosone-animalia-naming/paper-fig5-1600.webp" alt="Heatmap of naming categories across phyla" />
  <figcaption><strong>Figure 5.</strong> Category shares by phylum; darker cells mean a higher share. Reproduced from Fig 5 of the paper (CC BY 4.0).</figcaption>
</figure>

Naming conventions differed clearly among phyla. Morphology was the most common category in most phyla. In Acanthocephala, Kinorhyncha, Onychophora, Platyhelminthes and Tardigrada, Morphology was relatively low and People was used more often. Geography was used less in Ctenophora, Entoprocta, Porifera, Rotifera and Sipuncula.

The paper offers several possible explanations, such as the marine-taxonomy tradition of naming species after research vessels, and the larger share of early-described species in some groups, when morphology-based naming dominated. It notes that these explanations cannot be tested directly with the present data.

Animalia-wide trends also need careful reading:

<figure>
  <img src="/column-images/plosone-animalia-naming/arthropoda-share-1600.webp" alt="Share of Arthropoda in the dataset" />
  <figcaption><strong>Figure 6.</strong> Of the 1,538,390 species analysed, 1,193,760 are arthropods, nearly 80%.</figcaption>
</figure>

The Animalia-level trends mainly reflect Arthropoda. Global patterns alone hide lineage-specific trajectories, which is why phylum-level comparison matters.

## Experiment 5: Does naming differ by author region?

<p class="experiment-label">Experiment 5</p>

<figure>
  <img src="/column-images/plosone-animalia-naming/paper-fig6-1600.webp" alt="Heatmap of naming categories by cultural name class" />
  <figcaption><strong>Figure 7.</strong> Category shares by the cultural class inferred from author names. Reproduced from Fig 6 of the paper (CC BY 4.0).</figcaption>
</figure>

Naming differed among inferred author regions. Latin American names showed the highest use of People, followed by Middle Eastern and South Asian names. East Asian names showed markedly lower use of People. European names used Morphology most and had the lowest share of Geography of all regions.

<figure>
  <img src="/column-images/plosone-animalia-naming/paper-fig7-1600.webp" alt="Cultural composition of authors over time" />
  <figcaption><strong>Figure 8.</strong> Cultural composition of the authors of species described each year. Reproduced from Fig 7 of the paper (CC BY 4.0).</figcaption>
</figure>

Until the early 20th century, nearly all species were described by authors of inferred European origin. Authors from other regions entered from the mid-20th century, and their share grew most after the 1970s. European authors still contribute most descriptions today.

The paper does not claim causation here. Early descriptions in the 18th and 19th centuries were dominated by European authors who relied on morphology, so time period may drive both authorship and naming patterns. For the low use of People among East Asian names, the paper raises the hypothesis that short and structurally similar surnames common in countries such as China and Korea may be less suited to epithets, while noting that cultural norms or other factors may also contribute.

## What we found and what remains open

The study shows three things:

- Naming across Animalia has historical structure. Descriptions dropped during the world wars, and the dominant categories shifted from morphology to places and people as biological techniques advanced.
- Naming trends differ among phyla, reflecting the traditions of each taxonomic community. Animalia-wide trends mainly reflect Arthropoda.
- Naming also differs among inferred author regions, and new naming cultures may be forming as participation in taxonomy diversifies.

There are limits. Classifying individual names remains uncertain, especially among the morphology sub-categories. Author regions are inferred from names and could not be validated against ground truth. The scheme has no host category for parasitic animals, so patterns such as the recent decline of People in Nematoda may include misclassifications. The explanations offered for phylum and regional differences are hypotheses that this dataset alone cannot test.

The scripts used for processing, analysis and validation are on GitHub and archived on [Zenodo](https://doi.org/10.5281/zenodo.19364291).
