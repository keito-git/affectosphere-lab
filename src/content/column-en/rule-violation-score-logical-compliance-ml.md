---
title: "Beyond Accuracy: Measuring Logical Compliance of Predictive Models"
date: "2026-06-23"
excerpt: "Two AI models with identical accuracy scores can have drastically different rule violation rates. A study published on arXiv introduces the Rule Violation Score (RVS), quantifying logical compliance that accuracy metrics alone fail to capture — with direct implications for medical and financial AI procurement."
image: "/column-images/rule-violation-score-logical-compliance-ml.png"
imageAlt: "A flat illustration of a balance scale with an accuracy score on the left and a rule violation score on the right"
readingMinutes: 5
basedOnPaper: "Rule Violation Score: A Metric for Measuring Logical Compliance of Machine Learning Models"
basedOnPaperUrl: "https://arxiv.org/abs/2606.20208"
---

Hello. This is Keito Inoshita from Affectosphere Group.

When evaluating AI models, we default to accuracy, F1, and AUC — metrics that measure predictive performance. But in high-risk domains like healthcare and finance, there is a second question that demands an answer.

"Does this model's output comply with business rules?"

A model that scores high on accuracy but repeatedly violates regulatory constraints or logical requirements cannot be safely deployed — and may expose the organization to legal risk or harm to end users.

A study published on arXiv in 2026 (Delplanque, Genevès, Layaïda, Faure) proposes the Rule Violation Score (RVS), a metric that quantifies this "logical compliance" directly.

Today I want to walk through this research and its implications for AI procurement and model risk management.

---

## Today's 3 Points

1. Core value: RVS makes visible that two models with near-identical accuracy can show dramatically different rule violation rates.
2. Design: RVS distinguishes hard rules (strict constraints) from soft rules (statistical patterns), automatically generates SQL queries from Horn clauses, and applies across datasets and model types.
3. Validation: Evaluated on three benchmarks in knowledge graph prediction and relational regression, confirming behaviors that accuracy metrics fail to capture.

---

## ① What Accuracy Misses

Machine learning evaluation has long been organized around a single question: how well does the model match the ground truth labels?

That is a reasonable question. But it rests on an implicit assumption.

It assumes the training data fully captures the rules the model should follow.

In practice, that assumption often fails.

Consider a medical diagnosis AI. Clinical guidelines may specify that "if symptom A is present, treatment B must always be considered." That rule may appear in the training data, but if it is not embedded in the loss function, the model can treat it as optional.

Consider a financial credit scoring AI. A hard business rule might prohibit assigning any credit limit to an applicant with zero declared income. A model that maximizes accuracy can silently violate that rule on edge cases without penalty.

These failures of logical consistency do not show up in accuracy scores. RVS is designed exactly to measure them.

---

## ② Hard Rules vs. Soft Rules

A critical design choice in RVS is the distinction between two types of rules.

Hard rules are absolute constraints. They encode legal and regulatory requirements, mandatory business policies, and logic that must never be violated. A violation here is immediately problematic.

Soft rules capture statistically observed patterns. They are tendencies extracted inductively from data, and exceptions are possible. They represent expected behavior rather than inviolable constraints.

This distinction matters enormously in practice.

The EU AI Act, for example, imposes stringent requirements on "high-risk AI" systems — including medical diagnosis, credit scoring, and hiring tools — covering transparency, explainability, and conformity. The weight of a hard rule violation versus a soft rule deviation is entirely different from a compliance standpoint.

RVS preserves this distinction in its quantification, making it well-suited for use by compliance teams who need to differentiate severity levels.

---

## ③ From Horn Clauses to SQL: The Automation Architecture

A key implementation insight in RVS is the automatic generation of SQL queries from Horn clauses.

Horn clauses are a logical rule representation format. Any rule of the form "if condition A and condition B, then conclusion C holds" can be expressed as a Horn clause. Many business rules fit this form.

By converting Horn clauses to SQL queries automatically, the evaluation pipeline does not depend on a specific machine learning framework or data format. This is what makes it applicable across model types.

In practice, this means the same RVS pipeline can compare model A from vendor X against model B from vendor Y using a consistent measuring stick.

In AI procurement, this matters because vendor-provided accuracy metrics often differ subtly in definition, making cross-vendor comparisons unreliable. A standardized evaluation metric like RVS directly addresses that gap.

---

## ④ "Same Accuracy, Different Risk": The Core Finding

The study evaluates RVS on three benchmarks covering knowledge graph prediction and relational regression.

The most important result is this: two models with near-identical predictive accuracy can show substantially different RVS scores.

Models that appear equivalent when evaluated on accuracy alone turn out to differ significantly in how often they violate business rules.

This is an invisible risk in model selection.

Think about it in a medical AI context. Model A: 97% accuracy, low clinical guideline violation rate. Model B: 97% accuracy, high clinical guideline violation rate. Accuracy scores would suggest these models are equivalent. They are not.

The same pattern holds for financial and hiring AI. "The model we selected for its accuracy turns out to violate business rules frequently" — this may have been happening all along, invisible only because there was no metric to detect it.

---

## Applications: AI Auditing and Model Risk Management

RVS translates directly into operational practice. Here are three concrete applications.

First, embedding RVS in AI procurement review processes. When comparing models from multiple vendors, require RVS alongside accuracy metrics. Procurement evaluated on both accuracy and compliance creates incentives for vendors to optimize logical consistency, not just predictive performance.

Second, adding RVS to continuous monitoring KPIs. For models in production, track RVS alongside accuracy on a regular cadence. Model drift sometimes appears first in compliance behavior rather than accuracy — RVS enables early detection.

Third, EU AI Act conformity documentation. For high-risk AI systems under EU AI Act requirements, RVS can serve as objective evidence that "this model is logically compliant with applicable business rules" — improving explainability to regulators.

---

## The Procurement Trap: Over-Reliance on Accuracy

The era of selecting AI models purely on accuracy scores may be drawing to a close.

Accuracy is important. But it measures fit against labeled examples — which is a different question from compliance with business rules.

Organizations deploying AI in high-risk domains need to evaluate both dimensions separately.

What RVS shows is that high-accuracy, low-compliance models exist. Knowing this before making a procurement decision is fundamentally different from not knowing it.

"Accuracy × compliance" as the dual criterion for high-risk AI selection may be on its way to becoming standard practice.

---

## Reference

1. Guillaume Olivier Delplanque, Pierre Genevès, Nabil Layaïda, Zephirin Faure (2026). *Rule Violation Score: A Metric for Measuring Logical Compliance of Machine Learning Models*. arXiv preprint arXiv:2606.20208.

<p class="ai-notice"><small>* This article was written in part with AI assistance and may contain inaccuracies.</small></p>
