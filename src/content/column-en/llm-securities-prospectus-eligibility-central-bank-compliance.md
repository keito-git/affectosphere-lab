---
title: "Deutsche Bundesbank Uses LLMs to Review Prospectuses — What Financial Compliance Teams Can Learn from 91% Precision"
date: "2026-06-28"
excerpt: "A case study from Deutsche Bundesbank applies an LLM pipeline to securities collateral eligibility review. A three-stage architecture — extraction, normalization, interpretation — handles bilingual, OCR-noisy prospectuses and achieves up to 91% Precision at the document level. A concrete reference point for financial institutions building compliance AI."
image: "/column-images/llm-securities-prospectus-eligibility-central-bank-compliance.png"
imageAlt: "A flat illustration of financial documents and AI icons, with German flag colors in the background"
readingMinutes: 5
basedOnPaper: "LLM-Based Examination of Eligibility Criteria from Securities Prospectuses at the German Central Bank"
basedOnPaperUrl: "https://arxiv.org/abs/2606.27316"
---

Hello. This is Keito Inoshita from Affectosphere Group.

Securities prospectus review is one of the most resource-intensive tasks in financial compliance.

Documents run from dozens to hundreds of pages. They arrive as semi-structured files with OCR noise. They mix multiple languages. And every eligibility determination requires careful interpretation of criteria — not just pattern matching.

Deutsche Bundesbank published a research case study applying an LLM pipeline to precisely this challenge (Hamotskyi et al., arXiv:2606.27316). The system achieves up to 91% Precision on document-level eligibility classification. The design decisions are worth examining carefully.

---

## Today's 3 Points

1. A three-stage pipeline — extraction, normalization, interpretation — handles bilingual and OCR-noisy prospectuses flexibly, achieving up to 91% Precision at the document level.
2. An LLM-as-a-judge evaluation method is proposed for semantics-based quality assessment — essential when generative outputs can't be scored by string matching alone.
3. A "conservative operating profile" that minimizes false acceptances is shown to be feasible — a critical design principle for financial risk management.

---

## ① Why Traditional Approaches Hit a Wall

The prior approach to information extraction in this domain relies on Named Entity Recognition (NER): identifying dates, amounts, issuer names, and other structured fields.

NER works well for structured, clean, single-language documents. But eligibility review at a central bank involves several conditions NER struggles with.

Language mixing: German financial documents blend German and English. The parallel in Japan would be Japanese-English mixed documents for foreign bonds or cross-border transactions.

Document quality: Scanned paper prospectuses carry OCR noise. An ISIN code becomes "lS1N." Dates shift from "2026-01-01" to "202б-01-01" with Cyrillic numerals mixed in.

Interpretation: Some eligibility criteria require understanding context — not just extracting a field value, but reasoning about whether a condition is satisfied.

Shifting to generative information extraction is a rational response to these constraints.

---

## ② The Three-Stage Architecture

The system's key design choice is decomposing the task into three explicit stages.

Stage 1 — Extraction

The LLM reads prospectus text and extracts information needed for eligibility assessment. Unlike NER, it can interpret conditions written in natural language and fill in implicit gaps from context.

Stage 2 — Normalization

Extracted information is converted to standardized formats. "January 2026," "Jan. 2026," and "26/01/01" all resolve to the same canonical form. OCR noise correction happens here too.

Stage 3 — Interpretation

Normalized data is compared against eligibility criteria to produce a final determination. This step requires logical reasoning — an area where LLMs can add genuine value.

The three-stage decomposition also creates natural audit points. When the pipeline makes an error, you can identify which stage introduced it. End-to-end black-box pipelines make this much harder.

---

## ③ The Conservative Operating Profile

In financial compliance, errors are not symmetric.

- False acceptance (classifying an ineligible security as eligible): severe risk — you accept collateral you shouldn't.
- False rejection (classifying an eligible security as ineligible): operational inefficiency — a human reviewer can correct it.

Most ML systems optimize Precision and Recall equally. In this domain, minimizing false acceptances is the priority.

The research explicitly evaluates a "conservative operating profile" tuned for this asymmetry. The 91% Precision figure represents this conservative configuration.

Recall will necessarily be lower — some documents will require human re-review. But from a financial risk standpoint, that's an acceptable tradeoff. The AI acts as a risk filter, not a full replacement for human judgment.

---

## ④ LLM-as-a-Judge for Evaluation

Generative information extraction introduces an evaluation challenge: outputs are natural language, not discrete labels.

"Maturity: January 2026" and "Maturity: Jan. 2026" are semantically identical but string-mismatched. Standard accuracy metrics penalize this.

The study proposes using an LLM as the evaluator itself — LLM-as-a-judge. The judge receives both the generated output and the ground truth and determines whether they are semantically equivalent.

This is a meaningful methodological contribution. Semantics-based evaluation gives a more accurate picture of real-world pipeline performance than token-level matching. It's also directly transferable to any financial NLP evaluation setting.

---

## ⑤ Implementation Implications for Japanese Financial Institutions

Mapping this case study to Japanese financial institutions reveals several concrete use cases.

Semi-automated collateral eligibility screening: Automatically extract required fields from prospectuses and securities reports to reduce the burden of initial screening on compliance staff. A 91% Precision benchmark provides a defensible target for internal PoC proposals.

Multilingual compliance checking: For cross-border transactions and foreign bond reviews involving Japanese-English mixed documents, this architecture's demonstrated bilingual capability is a directly relevant reference.

OCR noise resilience: For workflows that still involve scanning paper documents, the normalization stage's noise correction design is a non-negotiable design consideration.

Suggested KPIs: false acceptance rate as the primary metric; Precision ≥90% as the PoC acceptance threshold.

---

## "Conservative AI" as a Design Philosophy

Discussions about AI adoption in compliance often focus on accuracy. But in financial risk management, the more important question is: which errors are you minimizing?

A Precision-first, conservative design positions AI not as a replacement for human reviewers, but as a risk filter that eliminates serious errors while reducing reviewer workload on routine cases.

This reframes AI from "automation tool" to "risk management layer." For Japanese financial institutions designing compliance AI, this framing may be more useful than chasing raw accuracy numbers.

---

## Reference

1. Hamotskyi, S., Gautam, A. K., & Hänig, C. (2026). *LLM-Based Examination of Eligibility Criteria from Securities Prospectuses at the German Central Bank*. arXiv preprint.

<p class="ai-notice"><small>* This article was written in part with AI assistance and may contain inaccuracies.</small></p>
