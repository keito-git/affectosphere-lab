---
title: "Stop Making Users Re-Explain Everything: A Knowledge Architecture for Financial AI"
date: "2026-06-03"
excerpt: "InKH, an interaction-native knowledge harness for financial LLM agents, absorbs session context passively and retrieves it via temporal graph memory — achieving task quality 0.815, latency under 900ms, and 96% reduction in stale knowledge use. The design principle is broadly applicable wherever users are currently paying the complexity cost that systems should absorb."
image: "/column-images/financial-llm-interaction-native-knowledge.svg"
imageAlt: "Abstract visualization of conversation history being absorbed into a graph memory and automatically restored in the next financial AI interaction"
readingMinutes: 5
basedOnPaper: "Absorbing Complexity: An Interaction-Native Knowledge Harness for Financial LLM Agents"
basedOnPaperUrl: "https://arxiv.org/abs/2606.01886"
---

Hi, I'm Keito Inoshita from Affectosphere Group.

If you've had more than one conversation with a financial adviser, you've likely experienced this.

The second session begins with: "So, just to recap my situation — I mentioned last time that..." And you spend the first ten minutes re-establishing context that the previous conversation covered.

With AI chatbots, it's often worse. A new session starts fresh. The system has no memory of what you discussed before. The prior conversation — the portfolio details, the concerns you raised, the options you were considering — is simply gone.

This is a design problem before it's a technology problem. Complexity is being transferred to the user. The memory cost that the system should carry, the user is paying at the beginning of every interaction.

A paper published on arXiv in June 2026 (Ailiya Borjigin, Igor Stadnyk, Ben Bilski et al., arXiv:2606.01886) proposes InKH — an Interaction-Native Knowledge Harness for financial LLM agents — as an architectural solution to this. The core design principle: absorb complexity on the system side, not the user side.

---

## 3 Points for Today

1. Value: Automatically carrying session context forward eliminates the re-explanation cost for users and enables continuous advisory relationships.
2. How it works: Passive knowledge injection builds a working context buffer; temporal graph memory enables low-latency retrieval of the right context at the right time.
3. Application: Customer retention, adviser handover efficiency, and compliance traceability in financial services — and beyond.

---

## ① The Structural Problem: Complexity Transferred to Users

Most AI assistants in financial services today operate in session-isolated mode. What the user said last week, what portfolio changes were discussed, what concerns were raised and partially resolved — none of this transfers automatically to the next session.

The workaround is that the user explains it again. Every time. This is friction that accumulates. At low frequency it's tolerable. At higher frequency it becomes a reason to stop using the product.

The research frames this as a "complexity absorption" problem. There is inherent complexity in a continuing financial relationship: evolving portfolio state, personal circumstances, ongoing decisions in progress, regulatory constraints. Someone has to hold that complexity. Currently, users hold it. InKH proposes moving that burden to the system.

---

## ② How InKH Works

Two mechanisms combine in InKH.

### Passive Knowledge Injection

A working context buffer is built automatically from user interactions — without the user explicitly tagging, saving, or registering information. As the conversation unfolds, the system identifies and organizes contextually relevant information in the background.

The key word is "passive." No user action required. The context accumulates through ordinary use.

### Temporal Graph Memory

Accumulated information is organized in a graph structure that tracks the temporal dimension: what was true three months ago, what changed last week, what the current portfolio state is. When the system needs to retrieve context for a response, it queries this graph — pulling the right time-indexed information quickly.

Reported outcomes: 96.58% reduction in stale knowledge usage, average task quality score of 0.815, and average response latency of 900ms.

The 900ms figure matters for practical deployment. Complex context retrieval in under one second is a workable response time for an advisory interaction. This isn't a research demo that sacrifices usability for capability.

---

## ③ Applications in Financial Services

Where does this translate into real product or service design?

### Customer-facing AI assistants: "continuing the conversation" as a default

In wealth management apps, insurance consultation chats, and brokerage support interfaces, InKH-type architecture eliminates the re-entry burden. The system greets the user with context that's already current.

"Building on what we discussed last time" becomes the system's default posture, not a feature users have to manually invoke.

The business hypothesis: reducing re-explanation friction improves the perceived quality of the relationship, which improves retention. Measurable KPIs: retention rate, session frequency, and NPS scores compared pre/post InKH deployment.

### Adviser handover: eliminating context loss between representatives

When a client's relationship manager changes, the new adviser inherits a gap: they know the account data, but not the conversation history — the client's priorities, the options that were discussed, the reasons certain decisions were made.

With InKH-type memory, the temporal graph becomes a handover artifact. The new adviser can orient themselves from the system's accumulated context before the first meeting. Client experience continuity is preserved even when the human relationship breaks.

This addresses both efficiency (fewer catch-up conversations) and client satisfaction (not feeling like you're starting over again).

### Compliance and auditability

The temporal graph is also a record. "What information was available at the time of this recommendation" is a question financial services firms routinely face from regulators. A system that tracks what was known when, and what knowledge informed which response, has built-in traceability.

Efficiency and compliance auditability as joint outputs of the same architecture.

---

## A Design Principle With Broader Reach

"The system absorbs complexity instead of transferring it to the user" is not a principle specific to finance.

Healthcare record continuity. Legal matter management. HR interview histories. Anywhere that users are currently re-explaining context that a system should already hold — the same principle applies, and the same architectural pattern can be explored.

The important caveat: passively accumulating and automatically referencing personal information about users raises data privacy and security questions that are proportional to the sensitivity of the domain. In financial services, what gets stored, how it's secured, and when it gets deleted need to be designed with the same rigor as the retrieval architecture.

Building trust and building capability need to be designed together.

That's all for today!

---

## References

1. Ailiya Borjigin, Igor Stadnyk, Ben Bilski, Maksym Chikita, Dmytro Kyrylenko, Sofiia Pidturkina, Julia Stadnyk (2026). *Absorbing Complexity: An Interaction-Native Knowledge Harness for Financial LLM Agents*. arXiv preprint.

<p class="ai-notice"><small>* This article was written in part with AI assistance and may contain inaccuracies.</small></p>
