---
title: "Governing AI Agents at Runtime: What Deontic Policies Can Do That Access Control Cannot"
date: "2026-06-21"
excerpt: "Authentication and access control are not enough to govern autonomous AI agents once they start acting. A study published on arXiv proposes AgenticRei, a framework that applies permission, prohibition, and obligation constraints in real time — with concrete implications for CISOs, legal teams, and GRC functions designing AI governance."
image: "/column-images/deontic-policies-runtime-governance-agentic-ai.png"
imageAlt: "An abstract flat illustration showing deontic policy rules dynamically applied to AI agent actions at runtime"
readingMinutes: 5
basedOnPaper: "Deontic Policies for Runtime Governance of Agentic AI Systems"
basedOnPaperUrl: "https://arxiv.org/abs/2606.19464"
---

Hello. This is Keito Inoshita from Affectosphere Group.

"Once an AI agent has been granted access, how do you control what it actually does?" That question is becoming urgent for enterprise security and compliance teams.

AI agents that send emails, call APIs, and update internal systems are no longer experimental. They are operating in production environments. And the governance challenge that comes with them is not primarily about authentication — it is about everything that happens after an agent clears the security gate.

A study published on arXiv in June 2026 (Anupam Joshi, Tim Finin, Karuna Pande Joshi, Lalana Kagal; arXiv:2606.19464) addresses this problem through the lens of deontic policies: constraints expressed as permission (what an agent may do), prohibition (what it must not do), and obligation (what it must do). The paper proposes AgenticRei, a system for applying these constraints to LLM-based agents at runtime.

The core argument is that existing access control tools were designed for a different problem, and applying them to autonomous AI agents leaves a significant governance gap.

---

## Three takeaways for today

1. Authentication and access control cannot govern the real-time behavior of autonomous AI agents once they start acting.
2. AgenticRei applies permission, prohibition, and obligation constraints through an external reasoning engine — not through the LLM itself.
3. The framework's approach to obligation lifecycle management, conflict resolution, and dispensation maps directly to EU AI Act compliance, SOC 2 audits, and enterprise GRC design.

---

## ① The governance gap that opens after authentication

Traditional enterprise security focuses on "who gets in."

Tools like XACML (eXtensible Access Control Markup Language), Rego, and Cedar are widely deployed for access control in enterprise systems. They define which identities may access which resources under which conditions — and they do that job well.

But access control is a gate-time mechanism. It is not designed to evaluate, moment by moment, whether a specific action an agent is about to take is permissible, prohibited, or obligated. Once an LLM-based agent passes authentication, it may chain tool calls, coordinate with other agents, and take sequences of actions that were never individually evaluated against policy.

This research identifies that gap explicitly. The paper argues that XACML, Rego, and Cedar lack four capabilities that autonomous agent governance requires: obligation lifecycle management (when an obligation arises and when it expires), policy conflict resolution, dispensation (granting exceptions to prohibitions under specific conditions), and ontology-based reasoning. Each of these is familiar territory in compliance and legal practice — but is absent from the standard access control toolbox.

---

## ② What AgenticRei actually does

The proposed solution, AgenticRei, is built on the OWL (Web Ontology Language) Rei framework. Its key architectural choice is to place a high-performance logic reasoning engine outside the LLM.

Rather than embedding governance rules into prompts and relying on the LLM to interpret them, AgenticRei evaluates policy formally before an agent takes action — whether the action is a tool call or inter-agent communication. The result is a runtime check: "Is this action permitted? Is it prohibited? Is there an obligation that applies here?"

Obligation lifecycle management is worth unpacking. Consider a rule like: "If personal data is processed, an audit log must be submitted within 24 hours of completion." This obligation is triggered by an event (processing personal data), persists through a time window, and is discharged by a subsequent action (submitting the log). Managing the birth, persistence, and expiration of obligations is not something access control systems are designed for. AgenticRei handles it explicitly.

Dispensation is the formal mechanism for exceptions. Standard governance practice often includes rules like "customer data access is prohibited, except for security personnel during an active incident response." The ability to represent and evaluate exceptions in a principled way — without simply punching holes in the policy — is what dispensation provides.

Policy conflict resolution addresses a routine compliance tension: what happens when "privacy policy prohibits sending customer data externally" and "regulatory obligation requires reporting that data to a supervisory authority" are both active? AgenticRei uses ontology-based reasoning to resolve such conflicts.

---

## ③ How CISOs, legal teams, and GRC functions can apply this

Let me make the practical connections concrete.

For EU AI Act compliance, AgenticRei's architecture is a strong fit.

The EU AI Act (entering its main enforcement phase in 2026) requires high-risk AI systems to implement risk management, maintain logs, and support transparency. A framework that formally defines what an AI agent may, must not, and must do — and evaluates those constraints in real time with a logic engine external to the LLM — addresses those requirements structurally.

Critically, the external reasoning engine approach means "AI governance is not delegated to the AI itself." Compliance teams and regulators can audit the policy definitions independently of the LLM's behavior. That separation of concerns is significant for explainability in regulatory contexts.

For SOC 2 audits, the same logic applies. SOC 2 requires audit trails for access control, change management, and monitoring. An AgenticRei-style system produces exactly those trails: records of which policies were evaluated, which were applied, when obligations arose, when dispensations were granted. That evidence quality is meaningfully higher than logs that only record "the agent did X."

A concrete use case: an enterprise document generation agent.

- Permission policy: access to internal knowledge base documents
- Prohibition policy: transmitting documents containing customer personal data outside the organization
- Obligation policy: if an external API is called, a call log must be recorded

Managing these three policy types through an external logic engine means the agent's behavior is constrained by formal rules, not by how well the system prompt was written. This structurally reduces the risk of prompt injection attacks bypassing prohibition policies.

KPIs worth tracking: both "policy violations caused by agents" and "incidents prevented by policy enforcement." Tracking only violations misses the value that runtime governance generates by blocking actions before they cause harm.

---

## The security problem is shifting from authentication to action control

AI agent security is moving from "who do you trust" to "what do you let trusted agents do."

For CISOs, this represents a genuine shift in attack surface. Prompt injection, tool call misuse, and exploitation of inter-agent communication channels are not stopped by authentication controls. They require runtime behavioral governance.

The architecture AgenticRei proposes — a high-performance logic engine outside the LLM that evaluates permission, prohibition, and obligation constraints in real time — is one principled answer to that challenge.

This is research-level work, not a production product. But the thinking framework it offers is immediately useful for GRC teams designing AI agent governance policies. The key question to ask: "Can we articulate, right now, what our agents are permitted to do, prohibited from doing, and obligated to do — and can we demonstrate that those rules are enforced at runtime?"

If the answer is no, that's the gap this research is pointing at.

That's it for today!

---

## References

1. Anupam Joshi, Tim Finin, Karuna Pande Joshi, Lalana Kagal (2026). *Deontic Policies for Runtime Governance of Agentic AI Systems*. arXiv preprint.

<p class="ai-notice"><small>* This article was written in part with AI assistance and may contain inaccuracies.</small></p>
