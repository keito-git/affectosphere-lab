---
title: "Personalizing LLMs at Scale Without Per-User Models"
date: "2026-06-06"
excerpt: "Two dominant personalization approaches both hit walls at scale: retrieval quality dependency and storage costs that grow with user count. TAP-PER encodes user preferences into compact prefix embeddings, bypassing both."
image: "/column-images/compact-user-representation-tap-per.png"
imageAlt: "An abstract illustration of user preferences compressed into compact prefix embeddings passed to an LLM"
readingMinutes: 5
basedOnPaper: "Beyond Retrieval: Learning Compact User Representations for Scalable LLM Personalization"
basedOnPaperUrl: "https://arxiv.org/abs/2606.04547"
---

Hello. This is Keito Inoshita from Affectosphere Group.

When you try to scale an LLM-based service, personalization becomes unavoidable.

"User A's answer should be different from user B's answer" — that's a completely reasonable requirement. But once you try to implement it, every existing approach requires you to pay one of two costs.

A study published on arXiv in June 2026 (arXiv:2606.04547) proposes a third path: TAP-PER (Temporal Attentive Prefix for PERsonalization).

---

## Three takeaways for today

1. Current LLM personalization methods are either limited by retrieval quality or face storage costs that scale linearly with user count.
2. TAP-PER encodes user preferences as compact prefix embeddings, avoiding both problems simultaneously.
3. A design that scales without per-user adapters is directly relevant to SaaS platforms and support systems serving hundreds of thousands of users.

---

## ① The two walls of LLM personalization

There are two dominant approaches to making LLMs reflect individual differences.

The first is input-level personalization. You paste the user's behavior history or preference data directly into the prompt, and the LLM reads the context. Simple to implement, but including the full history inflates the input. The practical workaround is RAG-style retrieval — select only the relevant history and inject it — but now performance depends on retrieval quality. If retrieval misses, personalization misses.

The second is parameter-level personalization. Train a dedicated fine-tuned adapter per user. Precision is higher, but if you have 10,000 users, you need 10,000 adapters. Storage costs scale linearly with user count.

Neither wall shows up clearly in small-scale experiments. Both become visible the moment you try to deploy to a real service at scale.

---

## ② How TAP-PER works: compressing preference into a prefix

TAP-PER learns user preferences in the form of prefix embeddings.

A prefix embedding is a fixed-length vector sequence prepended to the LLM's input — passed directly into the model's computation graph, separate from the natural-language prompt. TAP-PER's goal is to compress each user's preference patterns into this prefix.

Two design choices matter here.

The first is the "Temporal Attentive" mechanism. The user's behavior history is arranged chronologically, with different weights assigned to recent versus older behavior. Since preferences change over time, prioritizing recent behavior is a natural and practical design choice.

The second is compactness. Because prefix embeddings are fixed-length, adding more users doesn't increase model parameters or storage meaningfully. No per-user adapters to maintain, and no cost explosion as you scale up.

The result: personalization without explicit history retrieval, and without per-user adapters.

---

## ③ Where this applies in practice

Setting aside the technical design, where does TAP-PER actually fit in operational contexts?

The most direct application is SaaS query-response systems. For services with hundreds of thousands of users where per-response personalization is desirable, the storage economics of per-user adapters don't work. A TAP-PER-style design keeps those costs flat.

HR tools and internal knowledge search are a strong concrete fit. Employees differ in their roles, skill levels, and domain contexts. The same question from a manager and a frontline worker probably warrants a different level of response detail. Personalizing that without per-user adapters — and without a retrieval step that might fail — is genuinely useful.

Healthcare apps are another natural candidate. Adapting health information and lifestyle suggestions to an individual's history and profile, while avoiding dependence on closed-source external APIs for privacy reasons. A self-contained design is well-suited here.

In terms of KPIs: satisfaction scores for personalized responses, ticket escalation rate changes, and per-user infrastructure costs are the natural starting measurements. All three are easy to compare before and after deployment.

---

## Design that doesn't cost more as users grow

What often gets overlooked in LLM personalization discussions is the cost after scale.

In an experimental setup, 1,000 users and 10,000 users feel the same. In a real service, a design where costs scale 10x when users scale 10x is unsustainable.

What TAP-PER proposes is personalization that doesn't scale linearly with user count. Training data is user-specific, but the inference-time storage overhead is near zero.

This is still research. But as an approach that makes "individually optimized responses for hundreds of thousands of users" feasible at the implementation level, it's worth watching.

That's it for today!

---

## Reference

1. (2026). *Beyond Retrieval: Learning Compact User Representations for Scalable LLM Personalization*. arXiv preprint. https://arxiv.org/abs/2606.04547

<p class="ai-notice"><small>* This article was written in part with AI assistance and may contain inaccuracies.</small></p>
