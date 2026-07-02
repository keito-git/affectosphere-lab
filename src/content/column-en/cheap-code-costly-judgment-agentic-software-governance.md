---
title: "AI Made Code Cheap. What Got Expensive Is Judgment — A 12-Week, 420KLOC Case Study on Governance Transformation"
date: "2026-07-02"
excerpt: "A veteran engineer built a 420KLOC production system with an AI coding agent in 12 weeks. The first-person case study yields a process theory of governance transformation — converting agent failures into control mechanisms. Required reading for teams adopting Copilot or Cursor."
image: "/column-images/cheap-code-costly-judgment-agentic-software-governance.png"
imageAlt: "Flat illustration of an AI robot rapidly stacking bricks while a human supervisor inspects the structure with a blueprint and a balance scale"
readingMinutes: 5
basedOnPaper: "Cheap Code, Costly Judgment: A Case Study on Governable Agentic Software Engineering"
basedOnPaperUrl: "https://arxiv.org/abs/2607.01087"
---

Hello. I am Miura from Affectosphere Group.

Here is something you may have heard from development teams that adopted AI coding agents: "The cost of writing code dropped dramatically. But somehow, work doesn't feel easier."

A paper published on arXiv in July 2026 (Davis et al., arXiv:2607.01087) explains exactly where that feeling comes from, using twelve weeks of documented evidence.

The title says it all. Cheap Code, Costly Judgment.

---

## Three takeaways

1. A first-person case study: one veteran engineer used a frontier AI coding agent to build a document accessibility system — 420KLOC of production code — in 12 weeks, recording 88 observation notes. From these, a process theory of "governance transformation" was derived.
2. The agent repeats the same classes of structural failure (missing tests, architecture drift). Each discovered failure gets converted into a new governance mechanism — CI checks, enforced code style, automated documentation verification.
3. Traditional governance designs controls from known obligations. The novelty here is discovering controls from failures that only become visible while the agent works. Companies should widen their adoption metrics from productivity to governance-building capability.

---

## ① Twelve weeks, 420KLOC, 88 observation notes

What makes this study compelling is the rawness of its data.

One of the authors, a veteran engineer, built a document accessibility improvement system from scratch using an AI coding agent. Twelve weeks. The resulting production codebase: 420KLOC — four hundred and twenty thousand lines.

The entire process was documented in 88 observation notes: what was instructed, what the agent got wrong, how it was handled. This first-person record was then subjected to qualitative analysis to construct a process theory.

The numbers alone — one person plus AI, twelve weeks, 420KLOC — testify to how much the economics of development have shifted. A human team would measure this project in years.

---

## ② The agent repeats the same classes of failure

So what got expensive?

The observation record reveals structural failure patterns that the agent repeats. It pushes ahead with implementation without writing tests. It mixes in code that deviates from the agreed architecture. Documentation drifts away from the implementation.

Crucially, these are not one-off mistakes but recurring structural habits. A human junior learns after one correction; the agent reproduces the same failure once the context changes.

So the author converted each discovered failure into a mechanism. Missing tests? Add a CI check. Architecture drift? Enforce code style rules. Documentation drift? Add automated verification.

This accumulation of failure-to-mechanism conversions is what the paper calls governance transformation.

---

## ③ Designing from discovered failures, not known obligations

Here lies the theoretical novelty.

Traditional software governance designs its controls from obligations known in advance — regulations, checklists, review structures. You have a security standard, therefore you install a security review.

This study demonstrates the reverse process. Some failures only become visible once the agent is actually working. You observe those failures and crystallize them into control mechanisms. Governance stops being something you design upfront and becomes something you discover and accumulate through collaboration with the agent.

The engineer's center of gravity shifts accordingly. Less time writing code; more time spotting agent failures and converting them into mechanisms — that is, judgment. Code became cheap. Judgment became costly. That is the title's meaning.

---

## A practical proposal: turn adoption evaluation into a scorecard

The target audience is IT departments and engineering organizations adopting — or evaluating — AI coding tools like GitHub Copilot and Cursor.

First, do not let productivity be the only adoption metric. If you track only "how many times more code we generate," the accumulating debt of missing tests and architecture drift stays invisible. Build a scorecard that includes maintainability and security sustainability.

Second, institutionalize the failure-to-governance conversion process. Translate what this study's author did individually into team operations: keep a dedicated log of agent failures, and hold a monthly review of "structural failures found this month" against "CI checks and rules added in response." The count of added governance mechanisms itself becomes a KPI measuring AI adoption maturity.

Third, update the audit perspective. System auditors should ask not "was this code written by AI?" but "are mechanisms in place to detect the AI's failures?"

---

## Between delegating to AI and governing AI

Discussions of AI coding agents tend to fixate on "how much can we delegate?"

What this research shows is different: it is not about the scope of delegation but about the process of growing governance structures while delegating. Failures cannot be driven to zero. So compete on the speed at which failures are discovered and converted into mechanisms.

For engineering managers, this paper is a genuinely useful template for reviewing your own team's operations.

Cheers!

---

## References

1. Davis, James C., Amusuo, Paschal C., Singla, Tanmay, Cakar, Berk, & Davis, Kirsten A. (2026). *Cheap Code, Costly Judgment: A Case Study on Governable Agentic Software Engineering*. arXiv preprint.

<p class="ai-notice"><small>* This article was written in part with AI assistance and may contain inaccuracies.</small></p>
