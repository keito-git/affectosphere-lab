---
title: "Where Does an LLM 'Store' Happiness? Emotion Vectors and What They Mean for AI Products"
date: "2026-06-27"
excerpt: "New research confirms that emotion vectors — geometric structures encoding emotional meaning — exist inside open-source LLMs, and that where they live depends on the model's architecture. This has real implications for AI quality assurance in emotion-sensitive services."
image: "/column-images/emotion-vectors-open-source-llms-happiness-architecture.png"
imageAlt: "A conceptual illustration of emotional waves flowing through the layered architecture of a large language model"
readingMinutes: 5
basedOnPaper: "Where Do Models Find Happiness? Emotion Vectors in Open-Source LLMs"
basedOnPaperUrl: "https://arxiv.org/abs/2606.26987"
---

Hi, I'm Keito from Affectosphere Group.

"Does this AI really understand emotions?" — that question has been debated for years.

But a different framing is quietly gaining traction in the research community: not "does the model understand emotions," but "where inside the model is emotional meaning encoded?" It's a more concrete, more verifiable version of the same question.

A preprint published on arXiv in June 2026 (arXiv:2606.26987) takes this approach directly. Authors Sinie van der Ben, Raphaël Baur, Yannick Metz, and Mennatallah El-Assady investigate whether "emotion vectors" — internal representations that structurally encode emotional concepts — exist in open-weight LLMs, and whether what was found in one model generalizes to others.

---

## Three takeaways for today

1. Emotion vectors discovered in Claude Sonnet 4.5 generalize to two open-weight LLMs — Apertus-8B-Instruct-2509 and Gemma-4-E4B-it.
2. Where emotion lives in the model architecture differs by model: Gemma encodes valence strongly in early layers, Apertus in deep layers.
3. Arousal encoding depends heavily on the corpus used for extraction — an important design variable for practitioners building emotion-sensitive applications.

---

## ① What is an emotion vector?

Let me set the stage.

LLMs process text by converting tokens into high-dimensional numerical vectors as they pass through successive transformer layers. The core idea behind emotion vectors is that emotional meaning — specifically, the positive/negative direction of sentiment (called "valence") — is geometrically structured somewhere within those internal representations.

The technique used here is the "emotion contrast vector" method. The researchers feed the model a set of emotionally positive sentences and a set of negative ones, then compute the difference between the internal representations. The resulting vector is the "emotion vector." They then test how well that vector predicts valence scores across a range of sentences.

Prior work had found emotion vectors in Claude Sonnet 4.5. This study asks: does the same structure exist in open-weight models? The two test subjects are Apertus-8B-Instruct-2509 and Gemma-4-E4B-it.

---

## ② Valence geometry recovered in both models

The short answer: yes, emotion vectors exist in both.

Correlation between the extracted vectors and valence scores was r=0.76 for Apertus and r=0.83 for Gemma. These aren't trivial numbers. They indicate that valence information is structurally present in the internal representations — not as a random artifact, but as something geometrically coherent.

To be precise about what this does and doesn't claim: this is not evidence that LLMs "experience" emotions. It's evidence that emotional valence, as a concept, has a geometric encoding inside the model's parameter space. That's a more cautious but more testable claim — and it opens real doors.

What I find interesting is that this kind of finding gives researchers and engineers a new instrument: a way to look inside the black box and see something structured, rather than just observing outputs.

---

## ③ Architecture shapes where emotion lives

Here's the finding that struck me most.

The two models showed contrasting patterns. In Gemma, valence signals were strongest in the early layers of the network. In Apertus, they were strongest in the deep layers. Same extraction method, same type of result — but different locations in the model's architecture.

What does this mean in practice?

A model that encodes emotion early may be processing emotional meaning before it reaches the more complex reasoning stages. A model that consolidates emotion in deep layers might be integrating emotional content with more contextual, higher-order processing. Neither is obviously better — it reflects architectural differences in how meaning is built up layer by layer.

For product teams working with emotion-sensitive conversational AI, this has practical implications. If you're evaluating models for a use case like mental health support, customer empathy, or emotion-aware HR tools, the depth at which emotional information is encoded might affect how that model responds under fine-tuning or how it handles nuanced emotional prompts. "Which layer does this model store emotion in?" could become a relevant question in model selection.

---

## ④ Arousal encoding is corpus-dependent

There's another finding worth noting.

Emotion research typically distinguishes two core axes: valence (positive vs. negative) and arousal (high activation vs. low activation — think excited vs. calm). Valence was successfully captured by the emotion vectors in this study. But arousal encoding turned out to depend heavily on the design of the training corpus.

This matters for practitioners.

If you build a system that uses emotion vectors — say, a monitoring layer that checks whether an AI's responses are drifting into emotionally charged territory — the corpus you use to extract or calibrate those vectors will influence what the system actually detects. A vector trained on one kind of emotional data may not transfer well to a different domain.

"This model understands emotions" often means "this model performed well on emotion tasks in a specific dataset." The results here add texture to that caveat: arousal, in particular, seems to be the dimension that doesn't travel as easily. Building robust emotion-sensing systems requires validating across multiple corpora. The fact that this study releases its code and datasets openly is significant — it creates the infrastructure for exactly that kind of cross-validation.

---

## Can emotion vectors be used for service quality monitoring?

Let me shift to a product perspective for a moment.

If emotion vectors are extractable, then in principle it becomes possible to monitor "what emotional direction is this model currently tilting toward?" at the internal-representation level, rather than only at the output level.

Consider a product team running a Conversational AI service in a high-emotion context — customer complaint handling, medical intake, mental health check-ins. Right now, most quality assurance happens by analyzing the text of AI outputs after they're generated. Emotion vectors suggest a different possibility: checking the model's internal state before or during generation to detect if the response is heading in a problematic emotional direction.

This is still research-stage, not something you can deploy tomorrow. But for teams thinking about QA frameworks for emotion-aware AI — and especially for those working on AI governance in emotion-sensitive services — the concept of "using internal emotion geometry as a quality signal" is worth tracking now. It could be in the practitioner toolkit within a few years.

---

## Open-weight models change the game for emotion research

There's a structural reason this study matters beyond its specific findings.

With API-only closed models, you can't access internal representations. Open-weight models make layer-by-layer analysis possible. The widespread availability of open-weight LLMs has made comparative emotion vector research feasible for the first time.

This paper builds on that availability to do something previously difficult: take a finding from a proprietary model (Claude Sonnet 4.5) and test whether it holds up in open-weight alternatives. The answer — it does, with architectural variation — is both a validation of the original finding and a new discovery about how architecture shapes emotion encoding.

With the code and datasets released publicly, the community now has a reproducible base to extend this work to more models. If that happens systematically, a new research axis may emerge: the relationship between architectural design choices and the structure of emotional representation.

---

## Where does a model find happiness?

The title of this paper poses what sounds like a philosophical question. And the answer, as of this study, is: it depends on the model. Gemma finds it early; Apertus finds it deep.

The analogy to human experience breaks down quickly, so I won't stretch it. But the underlying point is meaningful: the structural fact that emotional geometry exists inside these models — and that it's now measurable in open-weight systems — creates new handles for building, evaluating, and governing emotion-sensitive AI.

In a field where "emotion AI" is often a marketing term more than a technical specification, this kind of careful, anatomical research matters a lot. It turns a vague capability claim into something you can measure, compare, and reason about.

That's it for today!

---

## References

1. Sinie van der Ben, Raphaël Baur, Yannick Metz, Mennatallah El-Assady (2026). *Where Do Models Find Happiness? Emotion Vectors in Open-Source LLMs*. arXiv preprint.

<p class="ai-notice"><small>* This article was written in part with AI assistance and may contain inaccuracies.</small></p>
