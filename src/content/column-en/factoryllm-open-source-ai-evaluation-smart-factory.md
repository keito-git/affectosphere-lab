---
title: "Don't Send Factory Manuals to the Cloud ── What Manufacturers Need Before Deploying LLMs"
date: "2026-06-16"
excerpt: "Manufacturers want LLMs for equipment fault diagnosis. But sending proprietary technical documents to an external API is a security non-starter. FactoryLLM — an open-source framework for local, safe LLM evaluation in smart factories — addresses this head-on. Here's what DX teams, maintenance engineers, and IT vendors can take away."
image: "/column-images/factoryllm-open-source-ai-evaluation-smart-factory.png"
imageAlt: "Factory equipment icons and technical manual documents connected in a closed circuit on a local server — no external cloud link"
readingMinutes: 5
basedOnPaper: "FactoryLLM: A Safe and Open-Source AI Playground for Evaluating LLMs in Smart Factories"
basedOnPaperUrl: "https://arxiv.org/abs/2606.14119"
---

Hi, I'm Keito Inoshita from Affectosphere Group.

DX teams in manufacturing tend to hit the same wall.

"We want to use AI for equipment fault diagnosis. But we can't send our technical documents to a cloud API — it's a security violation."

"We want to test which LLMs actually work on our internal documentation. But we have no standard way to evaluate them."

"To get AI adoption approved internally, we need to quantify performance upfront. But there's no evaluation environment."

These three obstacles exist simultaneously. That's the reality of AI deployment in smart factories.

---

## 3 Points for Today

1. The core problem: deploying LLMs in factories means clearing two walls — proprietary data leakage risk and the absence of an evaluation benchmark.
2. What FactoryLLM does: an open-source framework that processes technical documents locally and benchmarks LLMs with industry-standard metrics.
3. What teams can try now: concrete use cases for maintenance departments, DX teams, and IT vendors, with KPI candidates.

---

## The Two Walls of Factory AI

A study published on arXiv (Yash Pulse, Yong-Bin Kang, Abhik Banerjee, Abdur Forkan, Prem Prakash Jayaraman) addresses both obstacles directly.

When a manufacturer tries to apply LLMs to equipment fault diagnosis, two issues appear almost universally.

The first is proprietary data leakage risk. Equipment specifications, maintenance manuals, and fault history records are core competitive assets. Sending them to an external cloud API draws immediate pushback from security, legal, and leadership.

The second is the absence of an evaluation baseline. "How well does this LLM actually work on our technical documents?" has no standard answer. Many companies end up trying ChatGPT, finding it "looks pretty good," and stopping there — with no rigorous benchmarking.

FactoryLLM is a framework designed to solve both problems at once.

---

## How FactoryLLM Works

The design has three key elements.

Local-only processing. Document analysis and LLM queries all run in a local environment — nothing is sent to external cloud services. This is the core security fix.

Standard metric-based evaluation. The framework implements industry-standard evaluation metrics, including groundedness scores that measure whether LLM responses are grounded in the source documents. Multiple LLMs can be compared on a level playing field.

Configurable model settings. Users can swap in different LLMs and parameters for evaluation. "How do GPT-4o and Llama 3 compare on our own technical documentation?" becomes an answerable question.

For evaluation, the paper used 30 maintenance-related queries covering autonomous vehicles and planning software technical documents. According to the paper, all tested models achieved groundedness scores of 0.88 or above — demonstrating that LLMs can reach practical utility levels on specialized factory documentation.

---

## Why Open-Source Matters Here

The fact that FactoryLLM is open-source carries specific weight in a manufacturing context.

Building an AI evaluation tool in-house is prohibitively expensive and technically demanding for most manufacturers. But outsourcing the evaluation process to a vendor makes that process a black box.

Open-source means the evaluation logic can be inspected internally. Adoption decisions are made with full understanding of how scores are calculated. Custom evaluation queries for your specific equipment can be added. From an information security and AI governance standpoint — and for internal approval processes — this transparency is a meaningful advantage.

---

## A Concrete Use Case

Here's how this plays out for a maintenance department.

Use case: pre-deployment LLM evaluation for equipment maintenance.

Departments involved: maintenance team and production engineering, with IT setting up the local environment.

Current gap: equipment fault manuals are voluminous. New operators spend too long finding the right response procedure. The team wants LLM assistance for automatic answers — but doesn't know which model to use or whether any will perform adequately.

Using FactoryLLM: load your actual equipment manuals into the local FactoryLLM environment. Define queries that reflect real maintenance questions ("what's the verification procedure for error code XX?"). Run evaluation across multiple LLMs. Measure groundedness score, answer quality, and response time.

KPI candidates:
- Groundedness scores on evaluation queries (the paper suggests 0.88+ as a practical benchmark)
- Practitioner ratings of "usable responses" (5-point survey)
- Change in average fault response time after LLM deployment

For IT vendors and system integrators pitching to manufacturers: running FactoryLLM on a prospective client's technical documents and delivering a comparative LLM performance report could become a standard part of the proposal process. It gives the client concrete data to take to internal approvals.

For AI governance teams: accumulating FactoryLLM evaluation reports as pre-deployment performance records could serve as internal control documentation for audits and compliance.

---

## The "Pre-Process" That Manufacturing AI Is Missing

Manufacturing DX conversations tend to focus on "after AI is deployed." But the actual friction is almost always in the "before" phase — evaluation, quantification, and accountability.

FactoryLLM proposes an environment for handling that pre-process safely and rigorously. Evaluate without exposing data externally. Compare models on standard metrics. Attach results to internal approval documents.

For teams caught between the security requirements specific to manufacturing and the pressure to adopt AI, this feels like a genuinely useful option to test.

That's all for today!

---

## References

1. Yash Pulse, Yong-Bin Kang, Abhik Banerjee, Abdur Forkan, Prem Prakash Jayaraman (2026). *FactoryLLM: A Safe and Open-Source AI Playground for Evaluating LLMs in Smart Factories*. arXiv preprint.

<p class="ai-notice"><small>* This article was written in part with AI assistance and may contain inaccuracies.</small></p>
