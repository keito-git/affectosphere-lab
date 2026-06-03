---
title: "What an Image Makes You Feel Matters More Than What It Shows"
date: "2026-06-04"
excerpt: "The same image can trigger completely different emotional responses depending on cultural background. A new perception-modeling framework that captures both factual and affective dimensions of visual experience could reshape how global creative teams pre-screen their visuals."
image: "/column-images/affective-visual-perception-percept.png"
imageAlt: "Abstract visualization of people from different cultural backgrounds experiencing different emotional responses while viewing the same artwork"
readingMinutes: 5
basedOnPaper: "Beyond Semantics: Modeling Factual and Affective Perceptual Experiences from Vision-Language Data"
basedOnPaperUrl: "https://arxiv.org/abs/2606.03345"
---

Hi, I'm Keito Inoshita from Affectosphere Group.

A question that comes up often in global marketing: "How will this visual land in another culture?"

It's not usually a concern about whether the image is understood. It's a concern about whether it feels right. A product image that reads as fresh and optimistic in one market can come across as cold or even ominous somewhere else — not because of a translation problem, but because the emotional resonance of certain visual elements varies across cultural contexts.

The gap between "correctly understood" and "emotionally received as intended" is a problem that semantic image analysis can't solve.

A paper published on arXiv in June 2026 (Youssef Mohamed, Kenneth Ward Church, Mohamed Elhoseiny et al., arXiv:2606.03345) tackles this directly. The researchers propose P-Topics (Perception Topics) — a modeling framework that jointly captures factual perception (what is depicted) and affective perception (what emotional experience the image evokes) from vision-language data, implemented as PercepT (Perception topic Transformer).

---

## 3 Points for Today

1. A new paradigm for affective modeling: instead of asking "what emotion label does this image match," this framework asks "what emotional perception topic structure does it activate" — which is closer to how people actually experience images.
2. Cultural variation is structural, not random: the research shows that the same image elicits different affective responses across cultural groups, and that these patterns can be learned from data.
3. Business application: treating PercepT-style evaluation as "affective QA" for creative assets could allow global teams to pre-screen visuals for cross-cultural emotional risk before deployment.

---

## ① The Gap Between Semantic and Affective Understanding

Image recognition AI has become highly capable at the semantic level: identifying objects, scenes, faces, and actions. If you need to know whether an image contains a dog or a sunset or a person smiling, current computer vision handles that well.

But the creative challenge in marketing and design isn't usually semantic. It's affective.

White flowers read as purity and hope in some contexts, and as mourning and death in others. Neither reading is wrong at the semantic level — the flowers are correctly identified. The difference is in the affective layer: what experience the image activates in the viewer.

The P-Topics model addresses this by constructing a topic space that jointly represents both layers. It takes vision-language data — images paired with emotional annotations in multiple languages — and learns a structured representation of how factual content and affective experience co-occur and vary.

PercepT implements this as a Transformer-based model. On the ArtELingo dataset (artworks annotated by speakers of Arabic, English, and Chinese), it achieves a silhouette score of 0.97 (up from the baseline's 0.37) and an AUC of 0.94 (up from 0.77). These are not incremental improvements — the baseline comparison suggests that previous approaches were not successfully capturing the structure of affective perception at all.

---

## ② Cultural Patterns in Emotional Response Are Learnable

The ArtELingo dataset is particularly interesting for this research. It collects emotional annotations for the same artworks from speakers of multiple languages — making it possible to study not just individual variation but cultural-group variation in affective response.

The finding that stands out from this study is not simply "different people feel differently about the same image." That's known. The finding is that these differences follow learnable, culturally structured patterns.

The P-Topics model captures clusters of affective response that correspond to cultural background. This matters because it shifts affective perception from "unpredictable individual subjectivity" to "partially predictable structure that can be modeled."

From an affective AI research perspective, this is a meaningful step. Most emotion AI work has treated emotion as a label classification problem: map the input to a category (happy, sad, angry, fearful). This paper argues — and demonstrates — that a topic-based representation of perceptual experience is more informative and more accurate.

The perceptual experience is not a single label. It's a position in a space where multiple dimensions of factual and affective meaning co-exist. That's a more realistic model of how images actually land.

---

## ③ How Creative and Marketing Teams Could Use This

Thinking through operational applications if a PercepT-style API were available.

### Cross-cultural affective screening before launch

The most direct application: a pre-launch filter for visual assets used in global campaigns. Before rolling out product imagery or advertising visuals to a new market, run them through an affective perception model calibrated for that cultural context.

This fits naturally in the workflow of global marketing or e-commerce creative directors. The question shifts from "does this look good?" to "does this evoke the intended emotional experience for this specific audience?" — answered with data rather than intuition.

A practical KPI: track the number of creative assets flagged for cultural affective mismatch before deployment, and measure the correlation with post-launch engagement or brand sentiment in those markets over time.

### Automated affective QA for brand social accounts

Brand teams publishing high volumes of visual content face a version of the same problem at scale. A human reviewer can't pre-screen every image for subtle emotional misalignment. An affective perception model running as an automated QA step — flagging assets that score high on unintended negative emotion clusters — could surface risks before they become visible in engagement data.

This is especially relevant for brands operating in culturally diverse markets or running localized content at scale.

### UI/UX design validation

For product designers working on onboarding flows, dashboard interfaces, or health and finance applications, the affective layer of visual design matters more than is often acknowledged. Whether a particular visual pattern evokes calm and trust versus urgency and anxiety affects user behavior, even when users can't articulate why.

The ability to evaluate the affective response to UI visuals without running user studies every time would reduce design iteration costs and make affective considerations a practical part of the design process rather than an afterthought.

---

## Affective AI, Moving Past the Label

What this research represents in the broader trajectory of affective AI is a shift in problem framing.

For most of the field's history, the question has been: "What emotion label does this input correspond to?" That framing is tractable for benchmarks. But it misses most of what makes affective experience interesting and practically important.

The more useful question for real creative, clinical, and product applications is: "What kind of perceptual experience does this input generate, across what kinds of people, under what cultural conditions?"

The paper's title, "Beyond Semantics," signals exactly this ambition. Semantic understanding is necessary but not sufficient. Affective perceptual experience is the layer that determines how content actually lands.

P-Topics and PercepT are early steps toward making that layer measurable. That's worth paying attention to.

That's all for today!

---

## References

1. Youssef Mohamed, Kenneth Ward Church, Mohamed Elhoseiny (2026). *Beyond Semantics: Modeling Factual and Affective Perceptual Experiences from Vision-Language Data*. arXiv preprint.

<p class="ai-notice"><small>* This article was written in part with AI assistance and may contain inaccuracies.</small></p>
