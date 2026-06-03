---
title: "Emotion Data Is Shifting From “Collect” to “Create” — A Third Option Called Synthetic Data"
date: "2026-06-01"
excerpt: "Emotion-labeled data is hard to collect because of annotator burden, privacy, and representativeness. Three recent papers show that pairing domain knowledge with LLMs can resolve ethics and cost at the same time. Five minutes for data-ops leaders."
image: "/column-images/synthetic-emotion-data.png"
imageAlt: "Scattered data points with missing regions filled in by amber dots, overlaid with a faint human silhouette"
readingMinutes: 5
basedOnPaper: "Persona-Based Synthetic Data Generation Using Multi-Stage Conditioning with Large Language Models for Emotion Recognition"
basedOnPaperUrl: "https://arxiv.org/"
---

> _This article is an English translation of the original Japanese column. Some phrasing has been adapted for English readers._

Hello — this is Inoshita from Affectosphere Group.

A data-platform lead asked me recently:

“We want to lift our sentiment-analysis accuracy, but we're starved for labeled data. The moment we try to collect more, both the cost and the ethics bar go up sharply.”

I really get this.

Emotion-data sourcing is structurally different from ordinary annotation work.
Spending all day labeling texts full of anger, grief, and dread leaves a real secondary mental load on the annotators themselves.

On top of that, emotion data is among the most sensitive personal information — it's the inner life.
GDPR and Japan's APPI demand particular caution; collecting respectfully from minority customer segments, specific cultural groups, or vulnerable populations is structurally hard.

“We can't collect, so accuracy stays low. Accuracy stays low, so the product can't launch.”
Somebody has to break this loop.

Synthetic emotional data has picked up rapidly over the past year or two as the most credible answer.
Today I want to translate three papers we published in 2025-2026[^1][^2][^3] into the language of data operations and ethics owners.

[^1]: Keito Inoshita, Rushia Harada, "Persona-Based Synthetic Data Generation Using Multi-Stage Conditioning with Large Language Models for Emotion Recognition", International Journal of Activity and Behavior Computing, vol. 1, pp. 1-18, 2026.
[^2]: Keito Inoshita, Hayato Tomisu, Xiaokang Zhou, Akira Kawai, Katsutoshi Yada, "KDDA: A Knowledge-Driven Domain and Diversity Alignment Framework for Emotion Data Generation with Large Language Models", International Journal of Activity and Behavior Computing, vol. 1, pp. 1-24, 2026.
[^3]: Keito Inoshita, Xiaokang Zhou, Akira Kawai, Katsutoshi Yada, "Geometric Control-Based Data Augmentation with Cluster-Conditioned Interpolation and Extrapolation for Imbalanced Learning in LLM", arXiv preprint, 2025.

---

## Three-line takeaway

1. Value: in more situations than people realize, “create” is now more rational than “collect” across ethics, cost, and accuracy. The old assumption that synthetic data is a degraded version is genuinely outdated.
2. Design backbone: combining geometric control, statistical featurization of domain knowledge, and multi-stage persona conditioning gets synthetic data close to real data.
3. Affective AI lens: the domains where you cannot ethically collect — mental health, minors, vulnerable populations — are exactly where synthetic data unlocks the biggest value. Whether your organization can step into those domains is the watershed for affective-AI deployment.

In order.

---

## 1. Three papers, three different roles

### CIEGAD — geometrically complete minority classes

CIEGAD (Cluster-conditioned Interpolation/Extrapolation Geometric Augmentation for Data) addresses the inevitable class imbalance in emotion data.

“Joy” and “sadness” are everywhere; “awe” and “contempt” are scarce.

CIEGAD applies cluster-wise interpolation (to fill in holes) and extrapolation (to push out the margins) under geometric control in the embedding space.
A simple idea that works: between existing samples, you can fill gaps; outside cluster boundaries, you can widen the margin.
By conditioning an LLM to produce texts that fit those geometric anchors, F1 and recall for minority classes improve consistently.

### KDDA — convert domain knowledge into statistical features and generate

KDDA (Knowledge-Driven Data Augmentation) is bolder.
Instead of collecting data directly from individuals, you convert human knowledge about the target domain into statistical features and condition an LLM on those.

For a domain like “workplace stress,” you build a domain profile from characteristic vocabulary frequencies, typical situations, and signature emotion patterns, and use it as the generation condition.
The output gets double-filtered — lexical de-duplication and statistical-fit evaluation.

A classifier trained only on synthetic data hit a distribution close to real data on the bulk of the evaluation metrics.
“Create without collecting” has moved within practical reach.

### PersonaGen — multi-stage personas to reproduce natural stylistic variance

PersonaGen weaves the everyday fact that “the same emotion looks different across speakers” into synthetic data.

“Sadness” written by a teenager and “sadness” written by a 60-year-old physician differ in vocabulary, register, and social context.

PersonaGen stacks persona conditions in three stages — attributes, sociocultural background, situational context — to reproduce the stylistic variance that fits each persona.
The same emotion label produces diverse expressions across speakers.
The paper shows that raising the granularity of persona conditioning is the key to combining expressive diversity with label fidelity.

---

## 2. What this generates for business

Put the three together and the underlying change is this.

It's not just that “collecting” gets cheaper. The reach extends to “domains you couldn't reach before.”

Three places this lands.

First, sourcing cost.
Quality annotation of emotion-labeled text runs anywhere from a few hundred to a few thousand yen per sentence.
Replacing even part of that with synthetic data routinely cuts annual sourcing cost by an order of magnitude.

Second, annotator protection.
Forcing annotators to label endless streams of anger, violence, and despair is a domain with a real, growing legal record in the content-moderation industry.
Even partial replacement with synthetic data moves you forward on duty-of-care.

Third, regulatory get-ahead.
EU AI Act, tighter GDPR interpretation, ongoing APPI revisions — all of them raise the bar for processing that infers people's inner states.
The longer you accumulate real data, the more your exposure compounds when regulation shifts.
Migrating gradually to synthetic data is closer to risk hedging than to pure tech investment.

---

## 3. The part I most want to convey as an affective-AI lab

This is where I really want to put weight.

The real value of synthetic emotion data is not cost savings.

The real value is making affective AI reachable in domains where ethics has prevented us from going.

Concretely:

- Text analysis of mental-health consultations
- Child-abuse helplines and DV hotlines
- Conversational analysis in elderly care
- Early detection of suicide risk
- Research on emotional expression in minority cultures

Each of these maximizes the ethics bar the moment you try to collect real data.
Collecting from the people involved often imposes additional burden on them.

But these are also the places where affective AI has the highest social value.

KDDA and PersonaGen really matter here.
You turn expert knowledge into statistical features and create data that does not correspond to any specific real person, but is faithful to the affective distribution of that domain.
You build AI to support the people in those situations without taking data from them directly.
That's the biggest impact when affective AI meets synthetic data.

Our lab's core stance is to treat emotion as ambiguous and many-sided, on purpose.
And the most ambiguous, most delicate emotion almost always lives in the places where data is hardest to collect.

Synthetic data is, I think, the technical bridge into those places.
But used carelessly, it mass-produces convincing-looking falsehoods.
Coupling with domain knowledge, quality auditing, and transparency of the generation pipeline must all be designed carefully or it collapses fast.

---

## So what do you do tomorrow?

Three moves you can run.

- Sort your current emotion-data inventory into two columns: “replaceable by synthetic” and “must remain real.” Just this much sharpens the conversation dramatically.
- Pick one annotation category with high annotator load and run a synthetic-data pilot. Not full replacement — a hybrid of human-labeled and synthetic is the realistic answer.
- Deliberately mix synthetic data into your evaluation set, and make “regional and demographic accuracy parity” a KPI. This structurally reduces the silent loss of minority groups.

“We can't collect, so we give up” is shifting into “we can't collect, so we build.”
The premise of data strategy is turning over in the affective-AI domain — quickly.

---

## Closing

“The ability to create data, not the ability to collect it, decides your next competitive edge” — slightly grand, but in affective AI it's becoming literally true.

Synthetic data can turn toxic with one wrong move, technically or ethically.
Which means the design judgment of “what to create and what to leave uncreated” will matter more, not less.

If you ever wonder, “is our data strategy really fine as it is?” — start with the two-column sort.
You'll be surprised how many items quietly say, “this is fine to synthesize.”

That's it for now.

---

## References

1. Keito Inoshita, Rushia Harada (2026). *Persona-Based Synthetic Data Generation Using Multi-Stage Conditioning with Large Language Models for Emotion Recognition*. International Journal of Activity and Behavior Computing, vol. 1, pp. 1-18.
2. Keito Inoshita, Hayato Tomisu, Xiaokang Zhou, Akira Kawai, Katsutoshi Yada (2026). *KDDA: A Knowledge-Driven Domain and Diversity Alignment Framework for Emotion Data Generation with Large Language Models*. International Journal of Activity and Behavior Computing, vol. 1, pp. 1-24.
3. Keito Inoshita, Xiaokang Zhou, Akira Kawai, Katsutoshi Yada (2025). *Geometric Control-Based Data Augmentation with Cluster-Conditioned Interpolation and Extrapolation for Imbalanced Learning in LLM*. arXiv preprint.

<p class="ai-notice"><small>* This article was written in part with AI assistance and may contain inaccuracies.</small></p>
