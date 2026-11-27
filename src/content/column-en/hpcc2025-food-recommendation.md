---
title: "Can Lifestyle Cues from Images and Nutrition Improve Food Recommendation?"
subtitle: "GNN-Enhanced Multimodal Fusion with Contrastive Learning for Smart Health Oriented Food Recommendation System"
date: "2026-11-27"
excerpt: "We built GNNMF-CL, a food recommender that reads which lifestyle a dish suits from its image, nutrition, ingredients and cooking directions, and links dishes to users with graph neural networks. A walk-through of our IEEE HPCC 2025 paper, which received the Best Paper Award."
readingMinutes: 10
showImage: false
image: "/column-images/hpcc2025-food-recommendation/architecture.png"
imageAlt: "GNNMF-CL architecture. Three kinds of features are extracted from the image, nutrition, ingredients and cooking directions, then fused by an HGT that links user and food nodes to produce a recommendation score."
authors:
  - name: "Ryutaro Matsuoka"
    affiliation: "Shiga University"
  - name: "Keito Inoshita"
    url: "/en/about/"
    affiliation: "Kansai University"
  - name: "Xiaokang Zhou"
    affiliation: "Kansai University / RIKEN Center for AIP"
  - name: "Zhigao Zheng"
    affiliation: "Wuhan University"
  - name: "Akira Kawai"
    affiliation: "Shiga University"
  - name: "Katsutoshi Yada"
    affiliation: "Kansai University"
tldr: "People choose food not only by looks and ingredients but also by lifestyle goals such as losing weight or saving time. GNNMF-CL aligns VLM-written image captions with nutritional data through contrastive learning to obtain a lifestyle feature, encodes the ingredient–cooking-direction relations with a HAN as a taste preference feature, and extracts a visual feature with ResNet-50. An HGT fuses the three into a user–food graph. On AllRecipes it reaches an AUC of 0.7148 and a Recall@10 of 0.1297, above all baselines. Its NDCG@10 of 0.0247, however, is below HAFR (0.0455), so top-rank ordering remains a weakness. The paper received the Best Paper Award at IEEE HPCC 2025."
citation: |
  @inproceedings{matsuoka2025gnnmfcl,
    title     = {{GNN}-Enhanced Multimodal Fusion with Contrastive Learning for
                 Smart Health Oriented Food Recommendation System},
    author    = {Matsuoka, Ryutaro and Inoshita, Keito and Zhou, Xiaokang and
                 Zheng, Zhigao and Kawai, Akira and Yada, Katsutoshi},
    booktitle = {Proceedings of the IEEE International Conference on High
                 Performance Computing and Communications (HPCC)},
    pages     = {864--871},
    year      = {2025},
    month     = aug
  }
---

<div class="teaser">
<div>

Lifestyle

VLM-written captions and nutritional data are **aligned by contrastive learning** to describe which lifestyle a dish suits.

</div>
<div>

Fuse

Visual, lifestyle and taste preference features are **fused into a user–food graph with an HGT**.

</div>
<div>

Result

On AllRecipes: **AUC 0.7148** (HAFR 0.6435) and **Recall@10 0.1297**. NDCG@10, however, is below HAFR.

</div>
</div>

## Food is chosen to fit a lifestyle

Recommender systems have moved from purchase histories and demographics to multiple sources such as images and text. Food recommendation has used dish images or calorie information. Few studies, however, have combined ingredients, cooking directions and nutrition and asked how they shape user preference.

Ingredients partly overlap across dishes, and the same ingredients are perceived differently when boiled or grilled. Food choice also depends strongly on **lifestyle goals**. People managing their weight tend to prefer low-calorie dishes, busy workers prefer efficient nutrition, and pregnant women or people with health conditions may need to avoid certain ingredients.

This study therefore extracts **lifestyle-related features** from dishes, in addition to features already used in recommendation, and aims to recommend food that fits each user's health goals and dietary restrictions.

## How GNNMF-CL works

<figure>
  <img src="/column-images/hpcc2025-food-recommendation/architecture-1600.webp" alt="GNNMF-CL architecture" />
  <figcaption><strong>Figure 1.</strong> GNNMF-CL architecture (Fig. 1 of the paper). Three kinds of features are built from the four inputs on the left; the HGT in the centre links food and user nodes; the right side computes recommendation probabilities.</figcaption>
</figure>

The inputs are the dish image, nutritional data, ingredient list, cooking directions and user information. Five modules process them.

| Module | Input | Method | Output |
|---|---|---|---|
| Visual feature | Image | ResNet-50 (fine-tuned on Food-101) | Visual feature |
| Lifestyle intention feature | Image, nutrition | VLM (nanoLLaVA-1.5) + Sentence-BERT + contrastive learning | Lifestyle feature |
| Sensing feature | Ingredients, cooking directions | Sentence-BERT + HAN | Taste preference feature |
| Multimodal fusion | Three features, users | HGT | Food and user embeddings |
| Recommendation | Two embeddings | MLP + sigmoid | Recommendation probability |

### Lifestyle feature: aligning captions and nutrition

<figure>
  <img src="/column-images/hpcc2025-food-recommendation/lifestyle-module.png" alt="Lifestyle intention feature module" />
  <figcaption><strong>Figure 2.</strong> Lifestyle intention feature module (Fig. 2 of the paper). Caption and nutrition features of the same dish are pulled together; those of different dishes are pushed apart.</figcaption>
</figure>

A VLM (nanoLLaVA-1.5) looks at the dish image and writes a caption covering nutritional attributes, lifestyle suitability and health benefits. Sentence-BERT encodes the caption. In parallel, the nutritional data are preprocessed into a nutrient vector.

The caption vector and nutrient vector of the same dish form a positive pair; pairs with other dishes in the mini-batch are negatives. Contrastive learning with temperature 0.3 aligns them in a shared space. In addition, the nutrient features are clustered by k-means into six clusters (values from 2 to 20 were tested, with a clear elbow at 6), and two cluster-level losses keep each cluster tight and the clusters apart.

### Taste preference feature: ingredient–direction relations with a HAN

Sentence-BERT encodes the ingredient list and the cooking directions. A graph is built from ingredient nodes and cooking-direction (taste) nodes; ingredients with cosine similarity of 0.75 or higher are merged as duplicates. A Heterogeneous graph Attention Network (HAN) passes messages in both directions between the two node types, and the final cooking-direction node representation becomes the taste preference feature.

### Fusion and training

Each food node is connected to its three feature nodes, and to a user node when an interaction exists. A Heterogeneous Graph Transformer (HGT) passes messages over this graph, so that users learn from the dishes they interacted with and dishes receive signals from other dishes through shared users.

The loss is the sum of five terms: the BPR loss, the contrastive loss, the intra- and inter-cluster losses, and the XENDCG ranking loss.

## Experiment 1: Do the features separate after training?

<p class="experiment-label">Experiment 1</p>

<div class="setup">

**Setup**

- Data: AllRecipes (a UK recipe site; about 68,000 users, 456,000 food items and 33,400 ingredients; ratings from 1 to 5)
- Split: the training, validation and test sets provided with the dataset
- Main settings: node embedding 128 dims, image input 1,024 dims, contrastive temperature 0.3, cluster-loss weight 1.2 with margin 0.5, Adam (learning rate 1×10⁻⁵)
- Visualization: the three feature types projected to 2D with UMAP

</div>

<figure>
  <img src="/column-images/hpcc2025-food-recommendation/umap-1600.webp" alt="UMAP of multimodal features before and after learning" />
  <figcaption><strong>Figure 3.</strong> UMAP of the three feature types (Fig. 5 of the paper). (a) Before and (b) after representation learning. Red is visual, blue is sensing (taste preference) and green is lifestyle intention.</figcaption>
</figure>

Before learning, the three feature types overlap in the same region. After learning, they form three well-separated clusters. The paper reads this as each module capturing complementary, non-redundant information. This is a qualitative, visual check.

## Experiment 2: Comparison with existing recommenders

<p class="experiment-label">Experiment 2</p>

<div class="setup">

**Setup**

- Metrics: AUC, NDCG@10 and Recall@10
- Negatives: because food popularity is long-tailed, 500 negative items per user are sampled by training-set popularity
- Baselines: LDA, FM, MF-BPR, VBPR, FM-VBPR and HAFR (a food recommender using hierarchical attention over images and ingredients)

</div>

<figure>
  <img src="/column-images/hpcc2025-food-recommendation/baselines-1600.webp" alt="Comparison with baselines" />
  <figcaption><strong>Figure 4.</strong> Comparison with baselines (Table I of the paper). Gold is GNNMF-CL; blue is HAFR, the strongest baseline. GNNMF-CL is higher on AUC and Recall@10 and lower on NDCG@10.</figcaption>
</figure>

GNNMF-CL reaches an AUC of 0.7148, above every baseline including HAFR (0.6435). Its Recall@10 of 0.1297 is about twice that of HAFR (0.0674).

Its NDCG@10 of 0.0247, however, is below HAFR (0.0455), LDA and FM. NDCG rewards placing relevant items at the very top of the list. The paper interprets this as GNNMF-CL favouring broad coverage of relevant dishes over strict top-rank ordering, and names top-rank NDCG as an area for improvement.

## Experiment 3: Removing contrastive learning and the HAN

<p class="experiment-label">Experiment 3</p>

<div class="setup">

**Setup**

- w/o CL: contrastive learning removed from the lifestyle intention feature module
- w/o HAN: the HAN-based sensing feature replaced with randomly initialized features
- Metrics: Precision, Recall, F1 and NDCG (all @10), and AUC

</div>

<figure>
  <img src="/column-images/hpcc2025-food-recommendation/ablation-1600.webp" alt="Ablation study" />
  <figcaption><strong>Figure 5.</strong> Ablation (Table II of the paper). The full model is best on Precision, Recall and F1; removing contrastive learning gives the highest NDCG.</figcaption>
</figure>

The full model is best on Precision@10, Recall@10 and F1@10, which indicates that both contrastive learning and the HAN help. Its Recall@10 is 0.146.

On NDCG@10 alone, w/o CL scores highest (0.035). The paper suggests that contrastive learning changes the positions of items in the top-k list and may favour diversity and coverage over strict ranking.

<figure>
  <img src="/column-images/hpcc2025-food-recommendation/ablation-auc-1600.webp" alt="Ablation AUC" />
  <figcaption><strong>Figure 6.</strong> AUC in the ablation (values from the paper's text). The axis starts at 0.70, which makes the differences look large; they are 0.001 to 0.004.</figcaption>
</figure>

The AUC values are close: 0.715 for the full model, 0.711 for w/o CL and 0.716 for w/o HAN. The paper also plots differences in the true positive rate along the ROC curve. Without contrastive learning the difference is consistently negative, while without the HAN it is slightly positive in some regions. The paper concludes that removing contrastive learning consistently hurts discrimination, whereas the contribution of the HAN is more subtle and context-dependent.

Note that the full model's Recall@10 and NDCG@10 differ between Table I (0.1297 and 0.0247) and Table II (0.146 and 0.025). The paper does not explain the difference, so each table's values are reported here as printed.

## What we learned and what remains open

The study shows the following.

- Aligning VLM-written captions with nutritional data through contrastive learning yields a lifestyle feature for dishes. After training, the visual, taste preference and lifestyle features fall into separate clusters.
- GNNMF-CL, which fuses the three features into a user–food graph with an HGT, beats all baselines on AUC and Recall@10 on AllRecipes.
- In the ablation, removing contrastive learning lowers Precision, Recall, F1 and AUC. The contribution of the HAN is smaller.

There are also limitations.

- NDCG@10 is below the baselines, so top-rank ordering needs work.
- Several pre-trained modules are used without fine-tuning for the food or nutrition domain.
- Lifestyle goals are modelled only implicitly; the attributes users prioritize when choosing food are not modelled explicitly.
- The data come from an English-speaking recipe site only, and generalization to other cultures and regions is untested.

Future work will aim to capture and explain each user's decision factors, to make recommendations more reliable and transparent.

This paper received the Best Paper Award at IEEE HPCC 2025.
