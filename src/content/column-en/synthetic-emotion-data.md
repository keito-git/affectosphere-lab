---
title: "Building \"Plausible\" Data Without Collecting Personal Data — The Practice of Synthetic Emotion Data"
date: "2026-05-31"
excerpt: "Collecting emotion-labeled data has long been blocked by the walls of annotator burden, privacy, and representativeness. The latest research on synthetic data shows that the shift from \"collect\" to \"create\" can resolve ethics and cost at the same time. A 5-minute read for data operations, marketing AI, and ethics owners."
image: "/column-images/synthetic-emotion-data.svg"
imageAlt: "Abstract visual of scattered data points with missing regions filled in by amber dots, overlaid with faint human silhouettes"
readingMinutes: 5
basedOnPaper: "CIEGAD / KDDA / PersonaGen"
basedOnPaperUrl: "https://arxiv.org/"
---

> _This article is an English translation of the original Japanese column. Some phrasing has been adapted for English readers._

## Why "synthetic emotion data" is becoming a management issue

Customer-service AI, marketing automation, internal-communication analysis. What ultimately powers the accuracy of these systems is, in the end, emotion-labeled text data. But the moment you try to collect it, you run into several walls at once.

First, the psychological burden on annotators. Labeling text saturated with anger, sadness, and fear all day long produces secondary mental harm in its own right. Second, privacy. Emotion data is the most sensitive kind, connecting directly to a person's interior, and GDPR and personal-information protection laws treat it with particular care. Third, representativeness. Collecting data from minority customer groups, users in specific cultural contexts, or socially vulnerable populations in an ethically careful way is structurally difficult.

"We cannot collect, so the model has no accuracy; the model has no accuracy, so we cannot ship the business." A way to break this loop has rapidly drawn attention over the past year or two: synthetic emotional data. This column translates three studies published in 2025–2026 into the working language of data operations, marketing AI, and ethics owners.

---

## Three facts the research established

### 1. CIEGAD: minority classes in imbalanced data can be "geometrically supplemented"

CIEGAD (Cluster-conditioned Interpolation/Extrapolation Geometric Augmentation for Data) prescribes a treatment for the class-frequency imbalance that always shows up in emotion data. Frequent emotions like joy and sadness have abundant samples, while rare ones like awe and contempt have very few. The method corrects this imbalance by geometrically controlling "interpolation (filling holes)" and "extrapolation (extending peripheries)" within each cluster.

Interpolating between existing samples in the embedding space fills holes; extrapolating outside a cluster widens its periphery. Asking an LLM to generate text conditioned accordingly stably improves F1 and recall on minority classes.

### 2. KDDA: convert domain knowledge into statistical features, then synthesize

KDDA (Knowledge-Driven Data Augmentation) takes a bolder stance. Instead of collecting data directly from individuals, it converts human knowledge about a target domain into statistical features and uses them to condition LLM generation.

For a domain such as "workplace stress," KDDA constructs a "domain profile" from features specific to that domain — vocabulary frequencies, typical situations, characteristic emotion patterns — and uses it as the generation condition. Generated data is double-filtered through lexical-overlap suppression and statistical consistency evaluation based on Negative Log-Likelihood (NLL). The outcome: an emotion classifier trained solely on synthetic data achieved the distribution closest to real data on 9 of 12 metrics. "Creating without collecting" is now reaching practical levels.

### 3. PersonaGen: multi-stage personas — attributes → socio-cultural background → situational context — reproduce natural stylistic variation

PersonaGen weaves the obvious-but-easily-forgotten fact that "the same emotion is expressed differently by different people" into the synthetic data. "Sadness" voiced by a teenage student and "sadness" voiced by a sixty-year-old physician differ widely in vocabulary, style, and social framing.

PersonaGen stacks persona conditions in three stages — attributes, socio-cultural background, situational context — and reproduces stylistic differences appropriate to each character. The same emotion label yields diverse expressions tuned to the speaker, and downstream-task performance approaches that of real data. Multi-stage persona conditioning has emerged as the key to jointly securing expressive diversity and emotion-label consistency.

---

## What this research tells data operations

Three takeaways.

1. For minority classes and vulnerable populations, "synthesize" is increasingly more rational than "collect" — on ethics, cost, and accuracy all at once. The conventional wisdom that "synthetic data is a degraded version of real data," dominant only a few years ago, is clearly shifting.
2. If domain knowledge can be converted into statistical features, you can reproduce a domain's emotion distribution without collecting any personal data. That is a powerful alternative to GDPR and personal-information protection regimes.
3. Finer-grained persona conditioning dramatically increases the realism of synthetic data. Region- and attribute-level tuning of marketing AI and customer-service AI becomes possible without real-data collection.

These translate into concrete moves on the risk-management and value-creation sides.

---

## Risk management: three areas to act on now

### Risk 1: Privacy regulation — emotion data is drifting toward "special category" treatment

Emotion data is not yet explicitly designated as a "special category" in many jurisdictions, but the regulatory trajectory is clearly tightening. The EU AI Act, evolving GDPR interpretations, and amendments to Japan's APPI all raise the bar for processing that infers a person's interior. The longer you keep collecting and storing real emotion data, the more risk accumulates against future regulatory shifts.

What to do: take inventory of your emotion-data collection pipelines and classify them into "replaceable by synthetic data" and "real data is essential." Build a phased migration plan with legal, starting from the former.

### Risk 2: Annotator protection — organizational responsibility for secondary mental harm

Labeling large volumes of anger-, sadness-, and violence-laden data is an area where problems have repeatedly surfaced in the content-moderation industry. Litigation cases are growing, and the question is moving squarely into the territory of corporate duty-of-care for employee safety.

What to do: identify the labeling categories with the highest mental load and work with engineering to map which parts can be replaced by synthetic data generation. For parts that cannot be fully replaced, set up rotation, breaks, and mental-health support for annotators.

### Risk 3: Representativeness bias — AI that misses minorities becomes backlash material

Sentiment-analysis AI trained solely on real data structurally tilts toward majority expression. The risk of misclassifying utterances from minority cultural groups, people with disabilities, or specific age groups as "abnormal" or "negative" is high. Once such misclassifications get media coverage, brand damage is severe.

What to do: deliberately diversify your AI evaluation datasets using synthetic data. Supplement minority samples with geometric-control methods like CIEGAD, and adopt regional and attribute-level accuracy parity as a KPI.

---

## Value creation: three opportunities hidden in the same research

Every risk has a value opposite.

### Opportunity 1: AI deployment to ethically hard-to-collect domains

Mental health, children, elder care, abuse counseling — areas where ethical real-data collection is extremely difficult — cannot adopt AI without synthetic data. Combining knowledge-driven generation like KDDA with multi-stage persona conditioning like PersonaGen opens the possibility of building emotion-understanding AI even in these domains. These are new business areas with substantial social impact.

### Opportunity 2: Dramatic reduction in data-collection cost

Annotation costs for emotion-labeled data, when quality is taken seriously, run from hundreds to thousands of yen per sentence. It is not unusual for partial replacement with synthetic data alone to cut annual data-procurement costs by an order of magnitude. Reinvesting the savings into quality evaluation and auditing of synthetic data lets you raise quality and ethics together.

### Opportunity 3: Pre-emptive response to niche segments

Persona conditioning like PersonaGen's lets you synthesize data for "the new customer segment we want to reach" before that segment actually shows up. Marketing-message testing, pre-training of customer-support AI, region-level tuning of UI wording — preparation time for niche segments can be cut substantially.

---

## A 5-item action checklist for business practitioners

Things you can move on tomorrow.

- [ ] Inventory: classify the emotion data you currently collect into "synthetically replaceable" and "real data essential"
- [ ] Annotator protection: identify high-load labeling work and map, with engineering, where synthetic generation can take over
- [ ] Regulatory response: build, with legal, an emotion-data risk map and a synthetic-data policy
- [ ] Diversity audit: add synthetic data to existing AI evaluation sets and adopt regional and attribute-level accuracy parity as a KPI
- [ ] Pilot plan: in an ethically hard-to-collect niche domain (mental health, minority cultural groups, etc.), trial one new use case built on synthetic data

---

## Closing — the premise of data strategy is shifting from "collect" to "create"

Research on synthetic emotion data is quietly overturning the long-held premise that "data is something you collect." Instead of giving up because collection is hard, the new posture is to create precisely because collection is not possible.

What CIEGAD, KDDA, and PersonaGen show is that combining "geometric control," "statistical-feature encoding of domain knowledge," and "multi-stage persona conditioning" allows synthetic data to move beyond being a degraded substitute and reach a quality that complements — and at times exceeds — real data. This is a rare technical advance that addresses ethics, cost, and representativeness all at once.

The next time someone asks "is our data strategy really fine as-is?", I hope this column's checklist is what comes to mind. Not the power to collect data but the power to create data will decide the next competitive advantage.

---

> This article is a business-oriented rewrite of recent synthetic emotion-data research, including _"CIEGAD"_, _"KDDA"_, and _"PersonaGen"_.

<p class="ai-notice"><small>* This article was written in part with AI assistance and may contain inaccuracies.</small></p>
