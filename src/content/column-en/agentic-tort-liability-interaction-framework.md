---
title: "When Your AI Agent Causes Harm, Who Is Legally Responsible?"
date: "2026-06-07"
excerpt: "Autonomous AI agents that execute tasks and use tools do not fit neatly into existing tort law. A new interaction-based framework proposes three liability patterns and a Reasonable Agent standard built around interaction logs — with direct implications for enterprise AI governance."
image: "/column-images/agentic-tort-liability-interaction-framework.png"
imageAlt: "An abstract flat illustration showing an AI agent's action log being preserved as a legal evidence trail"
readingMinutes: 5
basedOnPaper: "Acting with AI: An Interaction-Based Framework for Agentic Tort Liability"
basedOnPaperUrl: "https://arxiv.org/abs/2606.00518"
---

Hello. This is Keito Inoshita from Affectosphere Group.

Enterprise adoption of AI agents is accelerating.

Systems that autonomously send emails, call external APIs, and update databases are now showing up in everyday workflows. The practical benefits are clear.

But most organizations that have deployed these systems cannot answer a simple question: if the agent causes harm, who is legally responsible?

A study published on arXiv in May 2026 (Yiheng Yao; arXiv:2606.00518) tries to answer that question through a formal legal framework. It proposes a classification of agentic AI behavior into three interaction patterns, each with a distinct liability attribution rule, and introduces a "Reasonable Agent" standard built on interaction logs as legal evidence.

This is a legal theory paper, but its implications for enterprise AI governance are immediate.

---

## Three takeaways for today

1. Agentic AI behavior falls into three patterns — autonomous deviation, pure tool use, and collaborative planning — each with a different liability structure.
2. Interaction logs can function as legal evidence under a "Reasonable Agent" standard, making log design a governance issue.
3. Organizations deploying AI agents should start documenting system constraints and instruction-action correspondence now, not after an incident occurs.

---

## ① Three patterns, three liability structures

The core of this research is a three-way classification of how AI agents act.

The first pattern is autonomous deviation. This describes cases where the agent takes action that goes beyond or contradicts the user's instructions or the designer's specification. When harm results from deviation, liability shifts toward the developer or provider — the reasoning being that the agent's behavior originated from its design and training, not from the user's directive.

The second pattern is pure tool use. Here the agent acts exactly as instructed, functioning essentially as a sophisticated tool. This maps closely to the existing legal concept of tool-user liability: the person wielding the tool is primarily responsible for its effects.

The third pattern is collaborative planning. This is the most common scenario in practice — the user and the agent engage in back-and-forth interaction to develop and execute a plan. Responsibility is distributed across the interaction, and determining liability requires reconstructing which decisions were made by whom at each step.

The reason this classification matters is that the fact of "an AI caused harm" is not enough to assign responsibility. What matters is the pattern of interaction that led to the harm.

---

## ② The Reasonable Agent standard

The second major concept the research introduces is the Reasonable Agent standard.

In legal reasoning, the "reasonable person" standard is widely used: would a reasonable person in this situation have acted the same way? The paper adapts this to AI agents: would a reasonable AI agent with the same capabilities, constraints, and context have acted as this agent did?

Applying this standard requires knowing what the agent was designed to do, what constraints it was given, what instructions it received, and what it actually did. All of that is in the interaction logs.

This reframes interaction logs from operational data to potential legal evidence. If your system's logs cannot reconstruct the instruction-action correspondence that occurred when a harmful output was produced, that absence itself may become a legal problem.

---

## ③ What legal and compliance teams should do now

Taking the framework seriously means acting before an incident occurs.

The first priority is auditing log design.

Many current AI agent implementations capture what the agent did but not the full context of what instructions were given, what approval workflows were followed, and how the agent's proposed action was confirmed or modified. Under the Reasonable Agent standard, that context is exactly what would be scrutinized. Check whether your system can reconstruct the instruction-to-action chain.

The second priority is documenting system constraints.

When you set explicit limits on what an agent can and cannot do, those settings and their rationale should be preserved as documentation. If an autonomous deviation occurs, demonstrating that the designer imposed reasonable constraints is meaningful evidence that responsibility shifts toward the agent's learned behavior rather than negligent design.

The third is getting liability allocation into contracts.

Organizations selling AI agent platforms and organizations buying them both need common language for "which party is responsible for which class of behavior." The three-pattern classification in this research works as that shared vocabulary. Specifying "for autonomous deviation events, the provider bears liability; for pure tool use events, the deploying organization bears liability" is cleaner than generic "use at your own risk" clauses.

A governance KPI worth tracking: not just "number of agent-caused incidents" but "percentage of incidents where liability attribution was resolved within N days." Organizations that can answer the responsibility question quickly will have a structural advantage in an increasingly regulated environment.

---

## Logs are liability evidence

AI agents will cause more problems as they become more capable. That is a predictable side effect of expanding capability.

The important posture is not "fight the liability battle after the fact" but "know in advance who is responsible for what when something goes wrong."

This research provides a framework for building that clarity. The three-pattern classification and the log design implications should be part of any serious AI governance policy review.

That's it for today!

---

## Reference

1. Yiheng Yao (2026). *Acting with AI: An Interaction-Based Framework for Agentic Tort Liability*. arXiv preprint.

<p class="ai-notice"><small>* This article was written in part with AI assistance and may contain inaccuracies.</small></p>
