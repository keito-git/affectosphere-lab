---
title: "Querying 50 Years of Maritime Accidents With AI — What Multi-Field RAG Means for Safety-Critical Industries"
date: "2026-06-13"
excerpt: "A new study applies field-aware hybrid RAG to 13,329 Korean maritime accident investigation reports spanning 1971–2025. Normalized recall improved from 0.18 to 0.55. A practical breakdown for safety managers, marine insurers, and anyone looking to automate incident investigation in regulated industries."
image: "/column-images/multifield-hybrid-rag-maritime-accident-root-cause.png"
imageAlt: "A maritime safety officer at a workstation reviewing a stack of accident investigation reports, with a search interface on screen highlighting relevant case excerpts in three color-coded fields"
readingMinutes: 5
basedOnPaper: "Multi-Field Hybrid Retrieval-Augmented Generation for Maritime Accident Root Cause Analysis"
basedOnPaperUrl: "https://arxiv.org/abs/2606.13249"
---

> _This article is an English version of the original Japanese column. Some phrasing has been adapted for English readers._

Hello — this is Inoshita from Affectosphere Group.

When a maritime accident occurs, how long does it currently take to find relevant precedents — similar past incidents with documented root causes and disposition decisions?

For safety officers at shipping companies or marine loss adjusters at insurance firms, the process probably looks something like this:
Run keyword searches through past investigation reports. Pull dozens of candidates. Read through each one to assess relevance. Cross-reference with subject-matter experts. By the time the analysis is done, days have passed.

A study published in June 2026 on arXiv (Seongjin Kim, Sungil Kim; arXiv:2606.13249) tackles this directly. Using 13,329 adjudication reports from the Korean Maritime Safety Tribunal spanning 1971 to 2025, it proposes a multi-field hybrid RAG framework and reports normalized recall improving from 0.18 to 0.55, with expert evaluation scores rising from 3.34 to 3.72.

---

## Three takeaways

1. Separating accident reports into three distinct fields — Summary, Causes, and Disposition — and searching each independently yields dramatically better results than treating the document as a single block.
2. Combining sparse retrieval (keyword matching) and dense retrieval (semantic similarity) with a hierarchical causal taxonomy produces the best results.
3. The multi-field RAG design pattern is transferable from maritime to aviation, rail, nuclear, and other regulated industries with similarly structured incident reports.

---

## 1. Why searching by field changes the results

Conventional RAG systems typically treat an entire document as a single unit for retrieval.

For structured documents like maritime accident investigation reports, this causes a real problem. The "Summary" section describes the incident narrative — location, vessel type, weather, timeline. The "Causes" section identifies root factors — watch-keeping failures, navigation errors, procedural gaps. The "Disposition" section records the administrative and regulatory outcomes.

If you want to find past cases with similar root causes, you need the "Causes" field to dominate the retrieval. If you want precedents for how a particular type of violation was handled, the "Disposition" field matters most.

Treating the document as one block means the contextual details in the Summary — the specific port, the vessel class, the season — tend to dominate retrieval scores, and the root cause patterns you actually care about get buried.

The proposed architecture assigns independent retrieval scores to each of the three fields and integrates them. That is what makes it "field-aware."

---

## 2. Sparse + dense retrieval: why both matter

Beyond field separation, the framework uses a hybrid retrieval approach combining sparse and dense search.

Sparse retrieval uses keyword frequency and exact match — the traditional method. It is strong when specific technical terms matter: "vessel collision," "reduced visibility," "course deviation."

Dense retrieval converts text into numerical vectors and computes semantic similarity. It captures paraphrasing and terminological variation — "inadequate watch-keeping" and "failure of monitoring duties" will score as similar even without shared words.

Neither method alone is sufficient. Sparse retrieval misses synonyms and phrasing variation; dense retrieval can be weak on specific technical terms and proper nouns. Combining them allows each to compensate for the other's gaps.

The framework also integrates a hierarchical causal taxonomy — a structured classification of accident causes — to enable consistent categorization and structured querying of root cause patterns.

---

## 3. What the numbers actually mean

The quantitative results, reported directly from the study:

Normalized recall improved from 0.18 to 0.55. This measures how many of the genuinely relevant precedents the system successfully retrieves. The improvement is more than threefold.

Expert evaluation scores improved from 3.34 to 3.72. This is a qualitative assessment by subject-matter experts rating whether the retrieved results are actually useful for report drafting and analysis. The improvement reflects practical utility, not just statistical performance.

The study also found the field-aware approach effective for two distinct tasks: precedent search (finding similar past incidents) and evidence-based report drafting (supporting the writing of new investigation reports with retrieved material).

---

## Business application: maritime safety management systems

The most direct application is for safety managers at shipping companies.

When a new incident occurs, locating relevant precedents quickly matters both for the immediate response and for internal reporting. Today, this search is manual. A field-aware RAG system that can return the most relevant past cases — ranked by root cause similarity, not just surface similarity — could substantially reduce that effort.

For marine insurance loss adjusters, the application is similarly concrete. Root cause identification is central to claims evaluation and coverage decisions. Fast access to "past incidents with similar causes and how they were adjudicated" directly supports investigation quality and consistency.

Measurable KPIs: time-to-precedent for new incident investigations, and the number of expert-validated precedents surfaced per query compared to manual search.

Looking beyond maritime, the design pattern transfers to any regulated industry with structured incident report archives: aviation occurrence reports, rail safety incident databases, nuclear plant event records. All share the same three-part structure of narrative, causes, and disposition or corrective action.

---

## Honest caveat: this study depends on a very specific data asset

The results here depend on the Korean Maritime Safety Tribunal's archive — 13,329 structured, digitized, consistently formatted adjudication reports accumulated over more than 50 years.

That is not a trivial resource. Most organizations will not have an equivalent in hand.

For this approach to work in practice, the historical incident reports need to be digitized, field-structured, and consistent in format. Organizations where reports are undigitized, inconsistently formatted, or spread across multiple systems will need a data preparation phase before deployment.

This study is also an arXiv preprint at this stage. Adapting the framework to a different organization's domain-specific vocabulary and causal taxonomy would require additional engineering work.

---

## Closing

"Never repeat the same accident" — in safety management, this is not just a slogan, it is a design problem.

Learning from past accidents requires retrieving them accurately, quickly, and in a way that is relevant to the question being asked.

What multi-field RAG demonstrates is a straightforward but frequently overlooked design principle: the right retrieval strategy depends on what question you are trying to answer, and different parts of a document serve different questions.

For anyone looking to apply AI to incident investigation in regulated industries, "design the retrieval around the field, not just the document" is a useful starting point.

That is it for now!

---

## References

1. Seongjin Kim, Sungil Kim (2026). *Multi-Field Hybrid Retrieval-Augmented Generation for Maritime Accident Root Cause Analysis*. arXiv preprint arXiv:2606.13249.

<p class="ai-notice"><small>* This article was written in part with AI assistance and may contain inaccuracies.</small></p>
