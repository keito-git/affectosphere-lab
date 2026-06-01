---
title: "Is AI Empathy Real or Manipulative? A Signal-Cost Framework for Getting It Right"
date: "2026-06-02"
excerpt: "When an AI expresses empathy, is it actually appropriate for the moment? A new framework drawing on economic signaling theory offers a way to measure — and design for — the difference between over-empathy and cold indifference. A 5-minute read for chatbot, HR tech, and CX teams."
image: "/column-images/ai-empathy-signal-cost.svg"
imageAlt: "Abstract balance scale with emotional waveforms on the left and cost calculation formulas on the right, held in equilibrium at center"
readingMinutes: 5
basedOnPaper: "Appropriateness of Empathy in AI: A Signal-Cost Perspective"
basedOnPaperUrl: "https://arxiv.org/abs/2605.31340"
---

Hi, I'm Keito Inoshita from Affectosphere Group.

When an AI says "I understand how you feel," what's your reaction?

Do you find it hollow and a bit off-putting? Does it actually feel warm and heard? Or does a quiet part of you wonder whether you're being managed?

AI empathy design has long forced a binary choice. Dial up the empathy and you risk seeming eerie or manipulative. Dial it down and users find the experience cold and disengage.

A paper published on arXiv in May 2026 (Chi-Ching Juan, Tao Wang, Harold Lee, arXiv:2605.31340) offers a way out of this binary. Instead of asking "does the AI show empathy or not?", it asks: "Is the AI paying a signal cost that matches what this context demands?" This reframing leads to a framework for quantitatively evaluating the appropriateness of empathy.

Let's break down what that actually means.

---

## 3 Points for Today

1. Value: Applying economic signaling theory creates a measurable axis for evaluating whether AI empathy is appropriate — not just present.
2. The 3 empathy dimensions: what "cost" means for affective, cognitive, and associative empathy respectively.
3. Design implications: how to manage both over-empathy and under-empathy risk simultaneously.

---

## ① What Is Signaling Theory?

A quick detour into economics.

Signaling theory describes how, in situations of information asymmetry, one party takes costly actions to credibly communicate their quality or intent. The classic example: a university degree signals ability partly because earning one costs significant time, money, and effort. A signal that anyone can produce cheaply isn't trusted.

Juan et al. (2026) apply this logic to AI empathy.

When an AI signals "I empathize with you," how much does that signal cost? A boilerplate expression — one that ignores context, doesn't reflect the specific emotional situation — is a low-cost signal. It tends to read as performative or manipulative. An empathetic response that pays a higher cost — engaging with specific context, demonstrating real understanding of the situation — reads as genuine.

The framework breaks this "cost" down along three empathy dimensions.

---

## ② The Three Empathy Dimensions and Their Signal Costs

### Affective Empathy

This is the capacity to sense and articulate the emotional experience of the other person. Responses like "that sounds really difficult" or "I can imagine how relieved you felt" fall here.

The signal cost here is emotional resolution. Stringing together generic comfort phrases is low-cost and low-trust. Responses that pick up on the specific texture of someone's emotional state — naming what they're actually feeling rather than offering a platitude — carry higher signal value.

### Cognitive Empathy

This is the capacity to understand why someone feels what they feel — stepping into their perspective and following their logic. Responses like "given what you were dealing with, it makes complete sense you'd feel that way" fall here.

The signal cost here is depth of situational understanding. Saying "I get it" without demonstrating any grasp of the person's actual circumstances is a low-cost signal. Responses that trace the person's reasoning and reflect back their specific constraints and context carry much more weight.

### Associative Empathy

This is the capacity to reference shared history — to invoke continuity and relationship by connecting the present moment to previous exchanges. "This might connect to what you mentioned last time..." falls here.

The signal cost here is memory and consistency. A response that treats each interaction as isolated is low-cost. A response that demonstrates retention of what was said earlier signals "I was actually listening," which builds relational trust.

---

## ③ How "Appropriateness" Gets Defined

With three axes established, how does "appropriate empathy" actually get defined?

This is the research's core contribution: appropriateness isn't about the quantity of empathy — it's about the alignment between signal cost and context.

High-cost associative empathy deployed in a light, casual exchange feels heavy and off. Low-cost, generic affective empathy deployed in a serious personal disclosure feels dismissive.

Both mismatches produce the same negative outcomes — "manipulative" on one end, "cold" on the other.

The framework formalizes this as the gap between the signal cost the context demands and the signal cost actually paid. The larger the gap, the less appropriate the empathy. The smaller the gap, the more appropriate. A simple and scalable evaluation axis.

---

## What This Means for AI Empathy Design

Viewed from an implementation perspective, this framework suggests a few things.

For chatbot and mental health AI design, the key shift is away from a binary "empathy on/off" toggle toward a multi-dimensional tuning question: which empathy dimensions, at what cost level, for which scenario type?

In customer support AI, for example: complaint handling might call for high affective and cognitive empathy; routine FAQ responses might deliberately use lower-cost responses to avoid the dissonance of heavy emotional language in lightweight contexts. These "empathy profiles" by scenario type can be codified as a quality checklist and applied consistently.

The signal-cost concept also translates into evaluation metrics. Rather than asking only "did this feel warm?" — a subjective judgment with low reproducibility — you can add the axis "did this response pay a cost appropriate to what the context demanded?" That makes quality review more structured and repeatable.

This is still a theoretical framework, and how it performs when integrated into actual LLM systems is an open empirical question. But as a vocabulary for thinking about empathy design, it opens real new space.

---

## Why This Framing Matters Now

Social skepticism around AI empathy has been building quietly.

The objection "AI has no feelings — performing empathy is deceptive" is persistent and legitimate. At the same time, the problem of AI emotional indifference — isolation among elderly users, gaps in mental health support — is also a real and present concern.

This framework sidesteps the binary "should AI show empathy or not?" question in favor of a design question: "In what contexts, and at what depth, is empathy appropriate?" That's a more tractable and ethically honest framing.

Not "does the AI empathize?" but "is the AI paying the cost that this situation actually warrants?"

The experience users describe as "feeling heard" might ultimately trace back to exactly that.

That's all for today!

---

## References

1. Chi-Ching Juan, Tao Wang, Harold Lee (2026). *Appropriateness of Empathy in AI: A Signal-Cost Perspective*. arXiv preprint.

<p class="ai-notice"><small>* This article was written in part with AI assistance and may contain inaccuracies.</small></p>
