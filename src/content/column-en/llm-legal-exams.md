---
title: "Can GPT Pass the Real-Estate Bar? Where Legal AI Helps and Where It Must Stop"
date: "2026-05-31"
excerpt: "Feed Japan's real-estate-transactions exam to GPT and you see exactly where legal AI lands and where it falls short. A 5-minute decision framework for legal tech, compliance, real estate, and the regulated professions."
image: "/column-images/llm-legal-exams.svg"
imageAlt: "Abstract visual of a law book, an exam sheet, a balance scale, and a passing-score line"
readingMinutes: 6
basedOnPaper: "Assessing GPTs Legal Knowledge in Japanese Real Estate Transactions Exam"
basedOnPaperUrl: "https://arxiv.org/"
---

> _This article is an English translation of the original Japanese column. Some phrasing has been adapted for English readers._

## Why "can an LLM pass a national exam?" is a management question

Anyone evaluating legal-tech adoption — leadership, in-house counsel automating contract review, real-estate firms, or licensed professionals from CPAs to attorneys — runs into the same question sooner or later. "How far can we actually trust the LLM?"

The cleanest way to answer it is with a national licensing exam. The scope is defined, the passing score is public, and error patterns are easy to analyze. Recent research has used such exams again and again as venues where the "professional-substitution capacity" of AI can be argued in numbers rather than impressions.

A study released in 2024 [^1] takes ten past sittings of Japan's Real-Estate Transactions Specialist exam (RETSE), the so-called "takken," and compares the answer quality of GPT-3.5 and GPT-4. This column rereads that study not as a technical artifact, but as material for the management decision "how far should we embed an LLM in our own workflow?"

[^1]: "Assessing GPTs Legal Knowledge in Japanese Real Estate Transactions Exam", 2024.

---

## Three facts the research established

### 1. GPT-4 beats GPT-3.5, but neither reaches the passing bar

The study had GPT-3.5 and GPT-4 answer ten past exams and compared overall accuracy and the structure of errors. GPT-4 broadly outperforms GPT-3.5, but neither model reaches the passing threshold of the exam.

The business takeaway is the next sentence. The claim that "with the latest GPT, judgments at the level of a licensed professional are possible" does not currently hold, at least for national-license-grade legal judgment.

### 2. Errors cluster in the domain-specific small print

A striking pattern in the error analysis is that mistakes concentrate in tax law, the Real-Estate Transactions Business Act, and similar narrow regulatory detail. On general civil-code reasoning the model is reasonable; on special measures, transitional provisions, and exception-laden numerical thresholds — the parts professionals look up daily — it falls away.

This is less about "missing knowledge" than about "training-data frequency" and "rule-update velocity." Statutes are precisely the area where past correctness becomes present error with every amendment — a structure general-purpose LLMs are inherently poor at.

### 3. Auxiliary prompts lift accuracy on complex questions

A further finding: adding auxiliary prompts such as "take customary law into account" or "consider real-estate trade practice" measurably improves accuracy on complex case-style questions. In other words, the LLM does not simply lack the knowledge; in many cases it has the knowledge but cannot retrieve it without an appropriate reference frame.

That means the same model can express very different capability depending on prompt design and how domain knowledge is supplied. In LLM deployment, the gap is often in the surrounding design, not the model.

---

## What this research tells the business

Three points.

1. LLMs do not currently reach national-license-grade legal judgment. A design that treats them as the final decision maker is unacceptable on both regulatory and litigation grounds.
2. Errors cluster in domain-specific detail. A general-purpose LLM cannot be aimed at professional work as-is; connection to current statute databases and internal rules is a precondition.
3. Performance varies with prompt design and reference framing. With the same model, operational design quality decides the gap.

The realistic premise that follows is to position legal AI as an "assistive tool," not as a "final decision maker."

---

## Risk management: three areas to act on now

### Risk 1: Final-judgment liability — the legal weight of acting on an LLM's output

If an LLM produces an incorrect legal interpretation and a contract, transaction, or filing is made on that basis, who is liable? Service provider, deploying company, or the responsible practitioner — every interpretation has takers. The most practical defensive line is an operational principle that "the LLM's answer is never the final basis for action."

What to do: Document an LLM-usage policy for legal, contracts, and filings. Codify in internal rules a clear line: drafting, issue-spotting, and reference opinions may use the LLM; final judgment and signature stay with a licensed person.

### Risk 2: Keeping up with statute changes — training-data lag becomes a business risk

LLMs have a hard training-data cutoff, so there is always a window during which they cannot reflect the latest amendment. The higher the amendment frequency — Real-Estate Transactions Business Act, tax law, labor law, data-protection law — the more dangerous it becomes to take a general-purpose LLM's answer at face value.

What to do: List the statutes referenced in your workflow with their amendment cadence, and mark the domains that "must not be completed by LLM alone." Move to a Retrieval-Augmented Generation (RAG) design that references the live statute database.

### Risk 3: Audit trail — can you reconstruct which provision the LLM relied on?

Whether facing a regulator, an internal audit, or litigation, accountability for "why this conclusion was reached" is unavoidable. If LLM output flows straight into work, the chain back to source provisions becomes hard to recover, and judgments that cannot be reproduced under audit accumulate.

What to do: Build into the workflow system a mechanism that stores the LLM's output, the referenced provisions and rules, and the practitioner's final judgment together. Aim for a state in which you can always say "AI assisted, a human decided, and here is the underlying provision."

---

## Value creation: three ways legal AI earns its keep as an assistant

The flip side of those risks is concrete productivity gain.

### Opportunity 1: Front-end of legal research and contract review

Issue extraction, first-pass surveys of related provisions, structural sanity checks of contracts, diff detection on standard clauses — these are areas where LLMs are comparatively strong. With final judgment still resting with counsel, halving the time of the upstream work materially shortens overall lead time.

### Opportunity 2: Training content for legal staff and the regulated professions

If the research is right that "how you frame the prompt changes performance," then "how to frame the right question" itself becomes training content. Case discussions in onboarding, instant feedback on past-exam practice, natural-language access to internal knowledge bases — there is wide scope to lift the productivity of training spend.

### Opportunity 3: First-line response for customers

Real-estate customer inquiries, first-touch consultations at administrative-law offices, internal legal helpdesks — designs that have an LLM handle routine questions while routing complex cases to a human improve both cost and customer experience. The key is an explicit design of "scope the AI may close out" and "threshold for human escalation."

---

## A 5-item action checklist for business leaders

Things you can move on tomorrow.

- [ ] Drawing the line: document an LLM-usage policy for legal and contracts (drafting yes, final judgment no)
- [ ] Trace: build a mechanism that stores LLM output, referenced provisions, and the human's final judgment together as logs
- [ ] Statute connection: in high-amendment domains, migrate to a configuration that references the live statute database via RAG
- [ ] Training design: bake "how to write the right prompt" into onboarding and internal knowledge bases
- [ ] Front-line design: codify the threshold between "AI handles" and "human escalates" in customer-facing channels

---

## Closing — turn an LLM that cannot pass into a tool that boosts the people who can

An LLM that cannot pass the takken exam cannot replace a licensed takken specialist. It can, however, compress the share of their time spent on research, organization, and drafting. The same structure applies across legal, contracts, and filings.

While remaining cautious about the "LLM replaces the licensed professional" scenario, the "LLM makes the licensed professional 1.5x more productive" scenario is already in range. Companies that do not conflate the two — and that invest in designs treating the LLM as an assistant — will lead in legal-domain AI deployment.

Next time you are asked "should we adopt legal tech?", I hope this checklist is what you reach for.

---

> This article is a business-oriented rewrite of a 2024 study evaluating GPT models on the Japanese Real-Estate Transactions Specialist exam.

<p class="ai-notice"><small>* This article was written in part with AI assistance and may contain inaccuracies.</small></p>
