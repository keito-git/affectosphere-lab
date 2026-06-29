---
title: "Managing Hundreds of Billions of SKUs with AI: What JD.com's System Teaches Retailers"
date: "2026-06-29"
excerpt: "JD.com built Oxygen AIIC, an LLM/VLM-centric product knowledge platform serving 700 million users. A 37% drop in information quality issues and 80%+ automated attribute completion offer a concrete reference for any retailer considering AI-driven PIM transformation."
image: "/column-images/jd-oxygen-aiic-industrial-llm-vlm-item-understanding-management.png"
imageAlt: "A vast digital product catalog flowing into an AI processing hub with LLM and vision model nodes"
readingMinutes: 5
basedOnPaper: "JD Oxygen AI Item Center (Oxygen AIIC) V1: An Industrial-Scale LLM/VLM-Centric Solution for Item Understanding, Management, and Applications"
basedOnPaperUrl: "https://arxiv.org/abs/2606.28070"
---

Messy product data is one of the oldest and most persistent problems in retail and e-commerce.

Missing attributes, inconsistent category labels, duplicate SKUs — these are not just operational inconveniences. They translate directly into degraded search results, weaker recommendations, and revenue the business never captures because customers can't find what they want.

A preprint published in June 2026 describes how JD.com tackled this at a scale most retailers will never face — but in ways that carry real design lessons for businesses of any size.

The system is called Oxygen AIIC, an AI Item Center built to manage product knowledge across more than 700 million users and hundreds of billions of SKUs.

---

## Three things this article covers

- How Oxygen AIIC's four-component architecture handles product knowledge management at industrial scale
- The two-stage "Semantic Search then Discrimination" pipeline that achieves 94.2% precision and 82.8% recall
- What EC operations teams, IT departments, and marketing teams should take from this as a PIM transformation reference

---

## ① The four components

Oxygen AIIC is organized around four interconnected elements.

First, ontology management. This covers the structural framework defining product categories, attributes, and relationships — maintained as a dynamically evolving knowledge base with millions of entries.

Second, item identification. The system determines when two product listings refer to the same item and handles deduplication and consolidation at SKU level.

Third, a self-improving model layer. Rather than relying on static models requiring manual retraining, the system learns from usage patterns and continuously improves its own accuracy.

Fourth, an integrated data hub. This consolidates product information from diverse sources and distributes it to downstream systems across the organization.

Together, these components handle hundreds of millions of product updates per day.

---

## ② The pipeline that makes it work

The technical centerpiece is what the paper calls "Semantic Search then Discrimination" — a two-stage process.

Stage one uses semantic search to narrow down candidate items. Stage two applies LLM and VLM reasoning to make precise discriminations among the candidates. This two-stage approach achieved 94.2% precision and 82.8% recall on item understanding tasks.

The logic is straightforward. Running deep model inference on every possible item pair at once is computationally prohibitive at this scale. Narrowing the candidate set through semantic search first makes precise judgment feasible without sacrificing throughput.

LLMs bring general language comprehension. VLMs (vision-language models) can interpret product images alongside text. In an e-commerce context where both product titles and images carry important signals, this multimodal design reflects the actual nature of the problem.

---

## ③ The numbers

Three figures from the paper stand out.

Information quality issues dropped by 37%. Errors, missing values, and inconsistencies in product data fell by more than a third through AI-assisted management.

Automated attribute completion exceeded 80%. More than four out of five product attributes that would previously have required human input are now filled automatically.

Daily processing volume runs at hundreds of millions of updates. These figures reflect the system operating in production at JD.com scale, not benchmark results from a controlled test environment.

---

## ④ What this means for EC operations, IT, and marketing teams

For EC operations teams, automated attribute completion is the most immediately applicable use case. When a product enters the catalog without complete size, material, or color data, search and filter functionality degrades. Customers searching for specific product types may fail to find what the business actually sells. LLMs that infer missing attributes from product titles, descriptions, and images address this problem directly.

The relevant KPIs here are attribute completion rate before and after AI integration, and information quality error counts. A baseline measurement before deployment gives you the basis for quantifying what changes.

For IT and data architecture teams, the ontology management component is the longer-term consideration. Product categories are not static — new types emerge, existing categories split or merge, and vocabulary evolves. Maintaining a classification system through manual effort has a ceiling. The Oxygen AIIC approach, where the ontology itself is treated as a dynamically maintained AI-managed knowledge base, offers a different model.

For product and marketing teams, the downstream implications are significant. Recommendation systems, search ranking, and targeted advertising all depend on the system understanding what a product actually is. When attribute data is complete and accurate at scale, those capabilities improve without any additional work on the recommendation or ad systems.

---

## ⑤ Questions to ask when planning a PIM overhaul

Three questions stand out as useful starting points.

What is your current attribute completion rate? Quantifying the gap tells you the baseline for estimating what AI-assisted completion could realistically deliver. Without this number, any projection is guesswork.

How is your product taxonomy currently maintained? If ontology updates depend on a small team working from change requests, there is likely a backlog and a quality ceiling. Understanding the bottleneck tells you where AI-assisted management could have the most impact.

How will you handle the build-vs-buy decision? JD.com built in-house, which reflects their scale and the strategic centrality of their product data infrastructure. For most organizations, integrating LLM/VLM capabilities through APIs or PIM platforms that are beginning to embed these models is the more realistic path. Data governance — specifically, which product data can be routed through external systems — is a question that needs resolving in parallel.

---

## The reframe worth taking away

Most public discussion of LLM deployment focuses on chatbots, content generation, or customer-facing applications. Product data management — accurate, systematic, at industrial scale — is less visible but arguably more foundational to how e-commerce actually functions.

The Oxygen AIIC paper is valuable precisely because it demonstrates something that smaller pilots cannot: that LLMs and VLMs can be integrated into industrial-scale operational infrastructure and deliver measurable, quantified improvements to data quality.

The reframe to take away is not "AI as a chatbot" but "AI as infrastructure for knowledge management." That shift in how to think about where LLMs belong in an organization is where the next generation of enterprise AI adoption is likely to land.

---

## Reference

1. Oxygen AIIC, Chan Long, Chao Liu, et al. (JD.com team) (2026). *JD Oxygen AI Item Center (Oxygen AIIC) V1: An Industrial-Scale LLM/VLM-Centric Solution for Item Understanding, Management, and Applications*. arXiv preprint.

<p class="ai-notice"><small>* This article was written in part with AI assistance and may contain inaccuracies.</small></p>
