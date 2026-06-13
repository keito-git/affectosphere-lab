---
title: "Why AI Contract Review Fails Across Borders ── 14,727 Clause Pairs Quantify the Gap"
date: "2026-06-14"
excerpt: "LAUKIN, a new dataset of 14,727 clause pairs extracted from 204 commercial contracts across Australia, the UK, and India, benchmarks how well AI models handle cross-jurisdictional legal equivalence. The best of 12 evaluated models reached an F1 of 65.11%. The findings spell out the limits of single-jurisdiction AI in global legal workflows — and where it can still add value today."
image: "/column-images/laukin-multijurisdictional-contract-dataset-legal-ai.png"
imageAlt: "National flags of Australia, the UK, and India overlaid on contract documents, with lines connecting to a central AI analysis engine"
readingMinutes: 5
basedOnPaper: "LAUKIN: A Multi-jurisdictional Common Law Contract Dataset"
basedOnPaperUrl: "https://arxiv.org/abs/2606.13184"
---

Hi, I'm Keito Inoshita from Affectosphere Group.

Here's a scenario that's become increasingly common: a legal AI tool performs well on domestic contracts, then gets deployed on an international deal — and the quality drops in ways that are hard to pin down.

The problem usually isn't the model's general capability. It's that contract drafting conventions differ meaningfully across jurisdictions, even within the same legal family. A non-disclosure clause in an English contract looks and reads very differently from the functionally equivalent clause in an Indian or Australian contract.

A 2026 paper (Amrita Singh, Aditya Joshi, Jiaojiao Jiang, Hye-young Paik, May Fong Cheong, arXiv:2606.13184) puts numbers on this problem. The researchers built LAUKIN — a dataset of 14,727 clause pairs from 204 commercial contracts across Australia, the UK, and India — and used it to evaluate 12 AI models on cross-jurisdictional legal equivalence.

The results are sobering, and directly actionable.

---

## 3 Points for Today

1. Discovery: Even within the common law family, drafting conventions across Australia, the UK, and India differ substantially enough that cross-jurisdictional equivalence judgment is a genuinely hard task for AI models.
2. Benchmark: The best of 12 evaluated models achieved an F1 of 65.11% — a significant gap from expert-level performance, which the paper makes explicit.
3. Practical takeaway: LAUKIN provides an immediately usable benchmark for evaluating legal AI tools on cross-border workflows, with concrete deployment architectures for M&A due diligence, compliance monitoring, and LegalTech product evaluation.

---

## ① What LAUKIN Is and Why It Matters

LAUKIN takes its name from the three jurisdictions it covers: Australia (AU), the United Kingdom (UK), and India (IN).

All three are common law systems — they share a legal heritage. But each has evolved its own drafting traditions, precedent systems, and regulatory requirements over centuries. The result is that the same legal concept can be expressed in strikingly different ways depending on where the contract was drafted.

The dataset was built through careful manual work: collecting 204 commercial contracts across the three jurisdictions, then extracting and labeling clause pairs at the level of legal equivalence. Not textual similarity — legal equivalence. Does this clause produce the same legal effect in its jurisdiction as that clause produces in another?

14,727 labeled clause pairs is the output. This scale puts LAUKIN into the range of serious benchmark datasets, not toy evaluations.

The legal equivalence framing is important because it tracks what practitioners actually need. When reviewing a cross-border acquisition, the question is not "are these clauses worded similarly?" It's "do these clauses do the same thing under their respective laws?"

---

## ② Why Same Legal Family Doesn't Mean Same Drafting

A natural assumption: if three countries share a common law tradition, their contracts should look broadly similar.

The research challenges that assumption.

Take a confidentiality clause. UK contracts tend to build elaborate definition provisions — defining "Confidential Information" with precision across multiple sub-clauses, hedged with specific carve-outs. Indian contracts frequently incorporate provisions responding to local regulatory requirements, including references to IT security rules. Australian contracts often absorb language from consumer law and competition law regimes that have no direct UK or Indian equivalent.

The research team describes this as a "cross-jurisdictional context deficit": models trained primarily on one jurisdiction's contract data encounter systematic blind spots when applied to others. The model may interpret jurisdictional drafting variation as substantive legal difference when it isn't, or miss genuine legal differences hidden behind superficially similar language.

This isn't a marginal issue for global legal AI. If a model's training data skews toward UK contracts (which is plausible given the volume of English-language UK legal text available), its performance on Australian and Indian contracts will be structurally degraded in ways that are hard to detect without a benchmark like LAUKIN.

---

## ③ Best F1 of 65.11%: What the Number Means

Evaluating 12 models on the LAUKIN benchmark, the best achieved F1 of 65.11%.

That number deserves unpacking for anyone thinking about deploying legal AI on cross-border workflows.

Expert practitioners working on cross-jurisdictional contract analysis operate at higher accuracy than this — the paper makes the gap explicit. That means current best-in-class models cannot replace specialist legal review for cross-jurisdictional equivalence judgment.

But "can't replace" doesn't mean "can't be used."

An F1 of 65% is still useful for first-pass triage. A model that reliably identifies the clearly equivalent and clearly non-equivalent clause pairs allows practitioners to focus their time on the ambiguous middle — the cases where human judgment genuinely adds value. That's a different and more defensible use case than attempting full automation.

The number also tells you something about where to invest in model improvement. Cross-jurisdictional legal AI needs training data that explicitly spans multiple jurisdictions — LAUKIN is exactly that kind of resource. Building evaluation protocols into procurement and development processes, rather than treating single-jurisdiction benchmarks as sufficient, becomes a concrete requirement.

---

## ④ Application Proposals for Legal, M&A, and LegalTech Teams

Here's how to put this research to work.

For LegalTech companies and in-house teams building legal AI: LAUKIN is immediately usable as a benchmark dataset. If you're evaluating vendor claims about cross-border contract review performance, ask whether they've been tested against a multi-jurisdictional benchmark. LAUKIN gives you a concrete standard to reference.

For M&A legal and due diligence teams: cross-border acquisitions require reviewing large volumes of target company contracts — NDAs, supplier agreements, employment contracts — under time pressure. A jurisdiction-aware clause equivalence model can function as a screening layer.

The architecture: AI handles first-pass classification, flagging clauses as likely-equivalent, likely-different, or ambiguous. The ambiguous set goes to specialist lawyers. The likely-equivalent set gets a lighter-touch spot-check. The KPI is reduction in specialist lawyer hours during DD without increasing the rate of missed legal inconsistencies. That's measurable from deal to deal.

For compliance and legal operations teams at multinationals: the same approach applies to monitoring whether group-wide standard contract terms are being reflected appropriately in local-entity contracts across jurisdictions. Flagging deviations from the standard template in jurisdictionally-aware terms is a more defensible compliance process than manual sampling.

---

## What to Ask Your Legal AI Vendor Today

The research's core message is a warning about single-jurisdiction AI deployed in global contexts. A model that performs well on UK contracts may fail on Indian or Australian contracts in ways that are invisible without explicit cross-jurisdictional evaluation.

The practical implication: when evaluating or procuring legal AI tools, ask two questions. What jurisdictions are represented in the training data? Has the model been evaluated on cross-jurisdictional tasks, and with what results?

LAUKIN provides a concrete benchmark to anchor those conversations. And as multi-jurisdictional datasets like this become more available, training legal AI models with explicit jurisdiction as a variable becomes increasingly achievable. That's the direction the field needs to move.

That's all for today!

---

## References

1. Amrita Singh, Aditya Joshi, Jiaojiao Jiang, Hye-young Paik, May Fong Cheong (2026). *LAUKIN: A Multi-jurisdictional Common Law Contract Dataset*. arXiv preprint arXiv:2606.13184.

<p class="ai-notice"><small>* This article was written in part with AI assistance and may contain inaccuracies.</small></p>
