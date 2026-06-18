---
title: "When Your Enterprise AI Grows Too Large: Routing Degradation, Diagnosis, and Recovery"
date: "2026-06-18"
excerpt: "Scaling to 110 agents and 584 tools drops AI routing F1 scores by 16–23 points. A new framework isolates 'retrieval gaps' and 'confusion gaps,' then recovers 10–17 points with embedding pre-filtering — a quality assurance blueprint for IT and AI operations teams."
image: "/column-images/enterprise-agent-routing-scale-degradation-recovery.png"
imageAlt: "A bird's-eye diagram of a large enterprise AI infrastructure with dozens of agent nodes connected by routing paths"
readingMinutes: 5
basedOnPaper: "Scaling Enterprise Agent Routing: Degradation, Diagnosis, and Recovery"
basedOnPaperUrl: "https://arxiv.org/abs/2606.17519"
---

Hello. This is Keito Inoshita from Affectosphere Group.

There is a moment every scaling enterprise AI team eventually faces.

The pilot worked. Stakeholders were impressed. The project got a green light for full deployment. More agents were added, more tools were integrated, and more departments were brought on board. Then, quietly, the system started getting things wrong in ways it never had before.

Routing quality — the ability of an orchestration layer to send each incoming request to the right agent — degraded. Users noticed. But because the decline was gradual and distributed across many workflows, no one could pinpoint why.

A new arXiv preprint by Kellen Gillespie and Robyn Perry (arXiv:2606.17519) examines this exact phenomenon. The research measures how routing performance degrades as enterprise agent deployments grow, diagnoses two distinct root causes, and demonstrates a recovery strategy that restores a substantial portion of the lost quality. For IT and AI operations teams managing large-scale agent infrastructure, this work provides a practical quality assurance blueprint.

---

## Three takeaways for today

1. Scaling to 110 agents and 584 tools degrades routing F1 scores by 16–23 points — a decline large enough to seriously affect user-facing quality.
2. There are two separable root causes: a retrieval gap (the correct agent never appears in the candidate set) and a confusion gap (the correct agent appears but a wrong one is selected anyway).
3. Embedding pre-filtering recovers 10–17 F1 points, and the two-gap framework tells you exactly which fix to apply to which problem.

---

## ① What breaks at scale

Routing is the core function that makes multi-agent AI systems work.

When a user submits a request — "summarize the vendor contract and flag clauses that exceed our standard liability cap" — the orchestration layer must determine which agent or combination of agents is best equipped to handle it. In a small deployment with a handful of specialized agents, this is relatively tractable. Each agent has a clear, distinct responsibility, and the routing logic does not need to work very hard.

The problem emerges when the deployment grows. As organizations add agents for new departments, new use cases, and new data sources, two distinct failure modes appear.

The first is what Gillespie and Perry call the retrieval gap. This is a failure at the candidate selection stage: the routing system generates a shortlist of potentially relevant agents, and the correct agent is not on that list. The system cannot route to an agent it has not nominated as a candidate. The larger the pool of agents, the harder it is to retrieve the right candidates reliably. Think of it like a search engine that has to find the right document across a library that grows from a few hundred to tens of thousands of entries — even a small drop in recall per query compounds quickly.

The second failure mode is the confusion gap. Here, the correct agent does appear in the candidate set, but the routing model selects a different one. This happens because agents at scale begin to overlap in their described capabilities. A procurement agent, a contract review agent, and a vendor compliance agent may all seem like plausible choices for the same contract-related query. The routing model, confronted with multiple plausible candidates with similar semantic profiles, makes the wrong call.

These two failure modes are distinct in their causes. The retrieval gap is a recall problem: the right answer is not even being considered. The confusion gap is a precision problem: the right answer is in the running but loses to a near-miss. Conflating them leads to applying the wrong fix.

---

## ② How to diagnose it: the two-gap framework

The contribution that makes this research immediately actionable for operations teams is its diagnostic methodology.

Gillespie and Perry propose measuring routing performance using F1 scores — a standard information retrieval metric that balances how often the system correctly identifies the right agent against how often it fails to do so. In their experiments, scaling from a small deployment to 110 agents and 584 tools produced F1 score drops of 16–23 points. That is not a marginal regression. In a system handling thousands of requests per day, a 16-point drop in routing F1 translates to a substantial fraction of requests going to the wrong agent, producing wrong outputs, or failing silently.

The diagnostic value of the framework comes from decomposing that aggregate F1 drop into its two components.

To measure the retrieval gap, you examine how often the correct agent appears in the candidate set generated at the first routing stage. If that inclusion rate is low, you have a retrieval problem regardless of how good your downstream selection logic is. No amount of fine-tuning the final selection step will recover performance that was lost when the right agent was excluded from consideration.

To measure the confusion gap, you restrict analysis to cases where the correct agent was in the candidate set and then examine how often the routing model still selected the wrong one. A high confusion rate with a low retrieval gap tells you that your candidate generation is solid but your selection logic is struggling with near-duplicate capability descriptions.

This decomposition is the key diagnostic step. Running it on your deployment tells you which lever to pull.

---

## ③ How to recover: embedding pre-filtering

Once you have diagnosed where the degradation is coming from, the paper's recovery strategy points toward a concrete technical solution.

For retrieval gaps — cases where the correct agent is not making it into the candidate set — the authors find that embedding-based pre-filtering substantially improves recall. The idea is to use dense vector representations of agent capability descriptions to pre-select a higher-quality candidate pool before the more expensive routing logic runs. Rather than relying on keyword matching or sparse retrieval methods that scale poorly as the number of agents grows, embedding pre-filtering leverages semantic similarity to capture agents whose descriptions are meaningfully related to the incoming query even when the surface-level wording does not match.

The results are significant: this approach recovers 10–17 F1 points in the settings studied. That is a large share of the degradation that scaling introduced. The recovery is not complete — some gap remains — but it demonstrates that the degradation from scaling is not simply an irreducible cost of growing the deployment. It is a recoverable engineering problem, provided you apply the right technique to the right root cause.

The practical implication is that organizations experiencing routing degradation should not assume the problem is inherent to large-scale agent systems. Nor should they assume that switching to a more powerful routing model will necessarily help, since a more capable model applied after a weak candidate generation step still cannot route to agents it never sees. Fixing retrieval is logically prior to fixing selection.

---

## ④ A concrete proposal for IT and AI operations teams

Let me make this concrete with a scenario that I suspect will be familiar to many organizations currently scaling their agent deployments.

Imagine a financial services firm that has been building out its enterprise AI platform for eighteen months. It started with four agents: one for customer inquiry handling, one for transaction monitoring, one for regulatory document parsing, and one for internal reporting. Routing worked well. Then, over successive quarters, the team added agents for KYC verification, anti-fraud analysis, credit assessment, ESG disclosure review, and cross-border compliance tracking. The tool catalog grew to several hundred entries.

The operations team begins noticing that the compliance-related queries — which were previously handled cleanly by the regulatory parsing agent — are now being split across the KYC, ESG, and cross-border compliance agents in ways that do not reflect the actual intent of the queries. Users are reporting that they ask for one thing and get something adjacent but not quite right.

This is a textbook confusion gap. The agents all have overlapping semantic profiles in the compliance domain. The routing model, when it generates a candidate set, is correctly including the right agent — but then selecting a near-miss.

The diagnostic step would be to measure retrieval inclusion rates and selection accuracy separately. If retrieval is solid but selection is failing, the fix is not to rebuild the retrieval layer. It is to address the capability description overlaps — through more differentiated agent descriptions, capability namespacing, or adding explicit disambiguation examples to the routing model's context.

A KPI worth tracking at the department level is not just overall routing accuracy but routing accuracy stratified by agent cluster — meaning groups of agents with overlapping capability domains. A cluster-level F1 score that is substantially lower than the system-wide average signals exactly the kind of confusion gap that this framework helps diagnose.

Setting a threshold — for example, no cluster-level routing F1 below 0.75 — gives the AI operations team a clear, measurable quality gate that triggers investigation before users notice the degradation.

---

## Routing quality is infrastructure quality

There is a tendency in enterprise AI deployment to focus quality assurance on the outputs of individual agents — does the contract review agent produce accurate summaries? does the compliance agent flag the right clauses? — while treating the routing layer as invisible infrastructure that either works or does not.

This research suggests that framing is incomplete. At scale, the routing layer is where quality is made or lost before any individual agent gets a chance to contribute. A well-tuned agent sending accurate outputs is useless if requests consistently land on the wrong agent in the first place.

The two-gap framework gives teams a vocabulary and a methodology for holding the routing layer to the same quality standards applied elsewhere. Retrieval gap and confusion gap are measurable. They respond to specific technical interventions. And monitoring them over time — as the agent pool continues to grow — provides an early warning signal for degradation that would otherwise only become visible through accumulated user complaints.

I suspect that for many organizations currently running 50 or more agents, a routing quality audit using this framework would reveal degradation that has already occurred but not yet been attributed to routing as a root cause. The diagnosis alone is worth running.

That's it for today!

---

## Reference

1. Kellen Gillespie, Robyn Perry (2026). *Scaling Enterprise Agent Routing: Degradation, Diagnosis, and Recovery*. arXiv preprint.

<p class="ai-notice"><small>* This article was written in part with AI assistance and may contain inaccuracies.</small></p>
