---
title: "Can Layered Personas Make LLM-Generated Emotion Text Closer to Real Data?"
subtitle: "Persona-Based Synthetic Data Generation Using Multi-Stage Conditioning with Large Language Models for Emotion Recognition"
date: "2026-11-27"
excerpt: "PersonaGen builds a persona step by step, from age and occupation to social background, scene and writing style, and then asks an LLM to write emotional text. Its output is distributionally closer to real tweets than existing prompting schemes, but it does not yet replace real data. A walk-through of our International Journal of Activity and Behavior Computing paper."
readingMinutes: 10
showImage: false
image: "/column-images/ijabc-persona-synthetic-data/framework.png"
imageAlt: "PersonaGen framework. A persona is built in three stages (base attributes, socio-cultural background, scene and style) and then passed to an LLM to generate emotional text."
authors:
  - name: "Keito Inoshita"
    url: "/en/about/"
    affiliation: "Kansai University"
  - name: "Rushia Harada"
    affiliation: "Almondays Co., Ltd."
tldr: "Emotion data are subjective, and collecting them faces ethical and practical limits. PersonaGen stacks a persona in stages (base attributes, then socio-cultural background, then scene and style), checks each stage with an LLM for plausibility, and then has GPT-4.1-mini write emotional text. Its 3,500 generated texts can be classified by emotion with an overall F1 of 0.80 (LightGBM), and GPT-4o rates them highly on naturalness. Against real tweets, PersonaGen beats two existing schemes on PRD-Fβ, KL and histogram similarity, but is the worst of the three on FID. A classifier trained on synthetic data alone reaches F1 0.321, well below the 0.567 obtained with real training data."
links:
  - label: "Preprint (arXiv)"
    url: "https://arxiv.org/abs/2507.13380"
citation: |
  @article{inoshita2026persona,
    title   = {Persona-Based Synthetic Data Generation Using Multi-Stage Conditioning
               with Large Language Models for Emotion Recognition},
    author  = {Inoshita, Keito and Harada, Rushia},
    journal = {International Journal of Activity and Behavior Computing},
    volume  = {1},
    pages   = {1--18},
    year    = {2026}
  }
---

<div class="teaser">
<div>

Generate

A persona is built in **three stages**; 7 emotions × 500 texts = **3,500 texts**.

</div>
<div>

Separate

Overall **F1 0.80** by emotion. Joy and pleasure blur together at 0.62 and 0.61.

</div>
<div>

Compare

Closeness to real tweets: PRD-Fβ **0.367** vs 0.259 and 0.282 for existing schemes. On FID it is the weakest.

</div>
</div>

## Why emotion data are scarce

One reason emotion recognition improves slowly is the lack of high-quality emotion data. Emotional expression varies widely between people. It depends on personality, social and cultural background, and the situation at hand. This makes it hard to build a dataset that covers many kinds of people.

Collection itself is also constrained. In workplaces and healthcare settings, there are psychological burdens and privacy concerns. Collecting emotional responses from children or the elderly is often considered infeasible under current ethical frameworks.

LLMs offer an alternative. Given a persona or a situation, an LLM can write emotional text that fits it. This study asks **how personas should be built so that the generated emotional text is diverse and close to real data**.

## How PersonaGen works

<figure>
  <img src="/column-images/ijabc-persona-synthetic-data/framework-1600.webp" alt="PersonaGen framework" />
  <figcaption><strong>Figure 1.</strong> Overview of PersonaGen (Figure 1 of the paper). The three stages on the left build the persona and scene; the LLM on the right writes the text.</figcaption>
</figure>

PersonaGen does not set a persona in one shot. It builds it in stages.

1. **Base attributes**: age group, gender, occupation and personality type (32 MBTI types) are sampled from distributions that follow real demographics and surveys. Implausible pairs, such as "elementary school student" and "lawyer", are removed by rules beforehand.
2. **Socio-cultural background**: seven attributes are added: education, prefecture, geographic location, family structure, religion, values and income. They are sampled conditionally, for example education by age group and income by life stage.
3. **Scene and style**: five elements are set: location, activity, interlocutor, medium and language style. One example is "chatting with a doctor via SNS while waiting in a hospital lobby" with a "polite tone, youth slang, emotionally expressive, spoken style".
4. **Generation**: all of this, plus the target emotion, goes into a single prompt. The LLM writes at most two short sentences.

At each stage an LLM labels the combination as "natural", "rare but plausible" or "implausible", and only the first two are kept. This catches odd combinations that the rules miss.

Restricting the scene elements gives data for a specific use. For social media, the activity can be fixed to "SNS posting"; for workplace studies, the location and interlocutor can be set accordingly. Experiment 4 uses this to produce tweet-style text.

## Experiment 1: Are the emotions distinguishable?

<p class="experiment-label">Experiment 1</p>

<div class="setup">

**Setup**

- Generator: GPT-4.1-mini (temperature 1.2)
- Emotions: joy, anger, sadness, pleasure, surprise, fear, neutral; 500 texts each (3,500 in total)
- Embeddings: all-MiniLM-L6-v2
- Classifier: LightGBM, 80% train / 20% test

</div>

We first placed the generated texts in an embedding space to see whether they cluster by emotion.

<figure>
  <img src="/column-images/ijabc-persona-synthetic-data/tsne-1600.webp" alt="t-SNE of synthetic emotion texts" />
  <figcaption><strong>Figure 2.</strong> t-SNE projection of the 3,500 generated texts (Figure 2 of the paper). Sadness, fear and anger form clusters; joy and pleasure overlap.</figcaption>
</figure>

Sadness, fear and anger form fairly distinct clusters. Joy and pleasure partly overlap. Both are positive emotions with similar arousal, so this likely reflects how close they are in meaning.

Using the same embeddings, we trained a LightGBM classifier on the seven emotions.

<figure>
  <img src="/column-images/ijabc-persona-synthetic-data/per-emotion-f1-1600.webp" alt="Per-emotion F1" />
  <figcaption><strong>Figure 3.</strong> F1 per emotion (Table 5 of the paper). All emotions except joy and pleasure (blue) exceed 0.8.</figcaption>
</figure>

The overall F1 is 0.80. Fear (0.92), anger (0.91) and sadness (0.89) are high; joy (0.62) and pleasure (0.61) are lower. The confusion matrix also shows joy and pleasure being mixed up, with some overlap between neutral and pleasure. Separating close emotions more clearly will need additional conditioning.

## Experiment 2: How varied are the expressions?

<p class="experiment-label">Experiment 2</p>

Beyond separability, we checked whether texts within one emotion vary. We used three measures. Mean cosine distance (MCD) shows how far apart texts of the same emotion are. Cluster entropy (CE) shows how evenly they spread. Centroid distance (CD) shows how far apart the emotion centroids are.

<figure>
  <img src="/column-images/ijabc-persona-synthetic-data/diversity-1600.webp" alt="Semantic diversity per emotion" />
  <figcaption><strong>Figure 4.</strong> MCD and CE per emotion (Table 4 of the paper). The y-axes do not start at zero.</figcaption>
</figure>

Surprise, anger and neutral have high MCD (0.73–0.75) and thus more varied expressions. Joy (0.572) and pleasure (0.586) are lower, with more similar wording. The two emotions that were confused in Experiment 1 also have the narrowest range of expression.

## Experiment 3: Does the text read as human-written?

<p class="experiment-label">Experiment 3</p>

GPT-4o scored each text on a five-point scale for four criteria: emotion match, grammaticality, lexical diversity and appropriateness, and structure and logic.

<figure>
  <img src="/column-images/ijabc-persona-synthetic-data/human-likeness-1600.webp" alt="Human-likeness scores" />
  <figcaption><strong>Figure 5.</strong> GPT-4o scores on four criteria (mean ± std, values from Figure 4 of the paper). The y-axis starts at 3.</figcaption>
</figure>

Grammaticality scores 5.00 and structure and logic 4.83. Emotion match (4.65) and lexical diversity (4.68) vary more, with some spread for surprise and joy. Note that this is an LLM-based rating, not a human one.

## Experiment 4: How close is it to real tweets?

<p class="experiment-label">Experiment 4</p>

<div class="setup">

**Setup**

- Real data: a public Kaggle dataset of emotional tweets (joy, anger, sadness, love, surprise, fear)
- Synthetic data: scene fixed to single-turn SNS posts, with short, informal tweet-like language; 500 texts per emotion (3,000 in total)
- Baselines: AttrPrompt (randomly sampled attributes in one flat prompt) and RandPersona (independently sampled persona attributes with no coherence control)

</div>

We first compared how close each synthetic distribution is to the real data on four measures.

<figure>
  <img src="/column-images/ijabc-persona-synthetic-data/similarity-1600.webp" alt="Similarity to gold tweets" />
  <figcaption><strong>Figure 6.</strong> Distributional similarity to real tweets (Table 6 of the paper). ↓ means lower is better; ↑ means higher is better.</figcaption>
</figure>

| Method | FID ↓ | PRD-Fβ ↑ | KL ↓ | HC ↑ |
|---|---|---|---|---|
| AttrPrompt | **0.388** | 0.259 | 0.070 | 0.982 |
| RandPersona | 0.397 | 0.282 | 0.055 | 0.986 |
| PersonaGen | 0.414 | **0.367** | **0.049** | **0.988** |

PersonaGen is best on PRD-Fβ, KL and histogram-cosine (HC). On FID it is the weakest of the three, so it does not win on every measure. The paper reads this as a trade-off between lexical variety and statistical homogeneity.

Next, we replaced the training split of the real data with each synthetic set, trained a six-class LightGBM classifier, and tested it on the real test set.

<figure>
  <img src="/column-images/ijabc-persona-synthetic-data/downstream-1600.webp" alt="Downstream classification" />
  <figcaption><strong>Figure 7.</strong> Performance on the real test set when training on synthetic data only (Table 7 of the paper). The blue bars at the top use real training data.</figcaption>
</figure>

No synthetic set reaches the classifier trained on real data (accuracy 0.568, F1 0.567). Among the synthetic sets, PersonaGen is best on all four measures: accuracy 0.359, precision 0.400, recall 0.359 and F1 0.321. Its F1, however, is almost the same as AttrPrompt's 0.320. We therefore position PersonaGen data as a supplement to real data, not a replacement.

Finally, two authors independently read sampled outputs to check whether emotion words and situations fit the target emotion. A fear example reads: "Feeling lost and uncertain about the future. The weight of being unemployed fills me with fear." It ties the emotion to a concrete worry, unemployment.

## What we know and what we don't

The study shows the following.

- Generating from a persona built in stages yields text in which most of the seven emotions can be told apart (overall F1 0.80) and that reads naturally in grammar and structure.
- Against real tweets, the output is distributionally closer than with random attribute prompting (PRD-Fβ, KL, HC), but not on FID.
- A classifier trained only on synthetic data stays far below one trained on real data.

There are limits. The comparison with real data uses a single tweet dataset; conversational, news and clinical corpora are untested. Only one generator was used, so it is unknown whether other LLMs change the results. Close emotions such as joy and pleasure are still not well separated. The framework covers static text only, without dialogue flow, temporal dynamics or multimodal context.

Next steps are evaluation on several kinds of corpora, checking sensitivity to the LLM and sampling settings, and conditioning that separates close emotions (valence–arousal or appraisal attributes, and contrastive prompting).
