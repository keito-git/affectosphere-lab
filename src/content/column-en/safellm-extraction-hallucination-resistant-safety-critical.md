---
title: "Can You Trust What AI Says About a Medical Guideline? — The Case for Extraction-Based RAG in Safety-Critical Settings"
date: "2026-06-13"
excerpt: "In high-stakes settings like healthcare, legal, and compliance, standard RAG's 'rewriting' approach introduces hallucination risk. A study on NHS guidelines found that extraction-based approaches — especially line-number selection — outperformed rewriting on precision, recall, and source fidelity. A five-minute brief for healthcare IT and compliance teams on rethinking RAG design."
image: "/column-images/safellm-extraction-hallucination-resistant-safety-critical.png"
imageAlt: "A medical professional's hand holding a printed NHS guideline document, with a magnifying glass hovering over a highlighted line of text, and a green checkmark shield icon beside it"
readingMinutes: 5
basedOnPaper: "SafeLLM: Extraction as a Hallucination-Resistant Alternative to Rewriting in Safety-Critical Settings"
basedOnPaperUrl: "https://arxiv.org/abs/2606.12897"
---

> _This article is an English version of the original Japanese column. Some phrasing has been adapted for English readers._

Hello — this is Inoshita from Affectosphere Group.

When a physician asks an AI system "what is the correct dosage for this patient?", and the system retrieves the relevant guideline to answer — how confident can you be that the answer matches what the document actually says?

Healthcare organizations are rapidly deploying RAG-based systems that reference internal documents and guidelines. But there is a design choice baked into most of these systems that deserves much more scrutiny: the AI rewrites the source material before returning it.

A study published in June 2026 on arXiv (Julia Ive, Felix Jozsa, Evridiki Georgaki, Nabeel Sheikh, Emma Cattell, Nick Jackson, Paulina Bondaronek, Ciaran Scott Hill, Richard Dobson; arXiv:2606.12897) addresses this directly. Using NHS acute care, oncology, and NICE guidelines as test cases, it compares rewriting-based and extraction-based RAG approaches, and finds that extraction-based methods are more reliable in safety-critical settings.

---

## Three takeaways

1. Standard RAG's "rewriting" approach increases hallucination risk for safety-critical documents.
2. Extraction-based approaches — particularly line-number-based selection — achieved the best precision, recall, and source fidelity.
3. Healthcare IT and compliance teams now have a concrete evidential basis to reconsider their RAG design choices.

---

## 1. Why rewriting-based RAG is a safety problem

RAG (Retrieval-Augmented Generation) works by retrieving relevant documents and passing them as context to an LLM, which then generates an answer.

For general business documents, this works well enough. A slight rephrasing is rarely consequential.

But medical guidelines are different.

"Administer 200mg orally, twice daily" becoming "200mg may be administered orally or intravenously, twice daily" is a material change — one that introduces a route of administration not found in the original. That is a hallucination, and in clinical use, it is potentially dangerous.

The NHS documents targeted by this study are exactly the kind of material where this matters: oncology treatment protocols, acute care guidelines, NICE recommendations. Rewriting these to produce a fluent answer introduces a fidelity gap that specialists cannot easily accept.

---

## 2. How extraction-based approaches work — and why line selection stands out

The proposed alternative is conceptually simple: instead of generating new text, the system returns verbatim excerpts from the source.

Several extraction strategies were compared, and line-number-based selection performed best. The idea is to have the LLM identify relevant line numbers in the source document and return those lines unchanged.

This works because it separates the judgment task from the generation task. The LLM decides which parts of the document are relevant — but it is not asked to rephrase or synthesize anything. The step that introduces hallucination is eliminated.

Results showed that this approach maintained source fidelity while achieving the best precision and recall scores across the strategies tested.

---

## 3. Why auditability matters as much as accuracy

"LLMs can be wrong, but so can humans" — this is sometimes offered as a reason not to worry too much.

In healthcare and legal contexts, though, the question is not just whether the answer is correct. It is whether the source of the answer can be traced and verified.

A rewritten answer is the LLM's interpretation. To audit it, you would need to compare the output against the source, reconstruct which parts were paraphrased, and check whether any additions were made. That is a high monitoring cost.

An extracted answer with a line number is inherently auditable. "This answer is based on Section 3, line 12 of the NICE guideline" is a format that supports clinical documentation standards, regulatory review, and accountability chains.

For compliance and governance teams, this is less a question of software engineering and more a question of institutional risk management.

---

## Business application: the RAG design checklist for healthcare IT

The most direct implication of this research is a design question that healthcare IT departments should be asking:

"Is our current RAG system rewriting-based or extraction-based?"

Organizations that have already deployed RAG for internal document access have a concrete reason to review their architecture.

Practical scenarios:

A nurse on an acute care ward queries a care protocol before a procedure. An oncologist checks a chemotherapy regimen for a specific diagnosis. A pharmacist looks up contraindications. In all of these scenarios, returning the relevant lines from the original document is more defensible than returning a fluent paraphrase.

The same logic applies to compliance departments working with regulatory texts — financial regulation, pharmaceutical labeling, labor law. Extraction-based design reduces interpretive drift.

Measurable KPIs: "source match rate" between RAG responses and source documents, and "audit trace completeness" — the proportion of answers where a specific source line can be cited.

---

## Honest caveat: extraction has limits too

Extraction-based approaches have weaknesses worth acknowledging.

When a question requires synthesizing information across multiple documents or sections, simple line extraction may not produce a coherent answer. There is also a version-control risk: if guidelines are updated, outdated line references may persist in logs or cached responses.

The research establishes extraction as the better design choice for safety-critical document retrieval — not as a universal solution for all query types.

A thoughtful design would route queries to extraction or rewriting depending on the nature of the question and the risk level of the source document. That kind of task-sensitive routing is likely where the field is heading.

---

## Closing

In healthcare and law, precision is not a nice-to-have — it is the point.

The tradeoff between the convenience of AI-generated answers and the fidelity of those answers to source material is a real design decision that RAG architects are making right now, often without fully articulating it.

Extraction-based RAG is not a radical idea. It is what happens when you take seriously the question: "What should we stop asking the LLM to do?"

For teams building AI access to safety-critical documents, this research offers a principled starting point for that conversation.

That is it for now!

---

## References

1. Julia Ive, Felix Jozsa, Evridiki Georgaki, Nabeel Sheikh, Emma Cattell, Nick Jackson, Paulina Bondaronek, Ciaran Scott Hill, Richard Dobson (2026). *SafeLLM: Extraction as a Hallucination-Resistant Alternative to Rewriting in Safety-Critical Settings*. arXiv preprint arXiv:2606.12897.

<p class="ai-notice"><small>* This article was written in part with AI assistance and may contain inaccuracies.</small></p>
