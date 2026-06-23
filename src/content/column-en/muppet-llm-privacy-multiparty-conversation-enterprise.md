---
title: "MuPPET: A Benchmark for Contextual Privacy of LLM Assistants in Multi-Party Conversations"
date: "2026-06-24"
excerpt: "When LLMs are embedded in group chats like Slack bots or Teams Copilot, do they actually understand who can receive which information? MuPPET — a new benchmark for contextual privacy — shows that current LLMs have significant vulnerabilities. Here's what this means for safe enterprise deployment under GDPR."
image: "/column-images/muppet-llm-privacy-multiparty-conversation-enterprise.png"
imageAlt: "A flat illustration of multiple user icons connected by conversation bubbles, with a central robot icon managing information flow"
readingMinutes: 6
basedOnPaper: "MuPPET: A Multi-Party Privacy Evaluation Test for LLM Assistants in Multi-Party Conversational Contexts"
basedOnPaperUrl: "https://arxiv.org/abs/2606.23217"
---

Hi, I'm Keito Inoshita from Affectosphere Group.

"The AI bot in our Slack channel accidentally shared another member's personal details."

Most organizations haven't seen this incident yet. But "not yet" can change overnight.

LLM integration into group conversations is accelerating fast. Slack bots, Teams Copilot, AI-powered group customer support — situations where multiple participants share a single conversation now routinely include an LLM in the mix.

A study published on arXiv in June 2026 (arXiv:2606.23217) raises an essential question for this moment.

"When an LLM is embedded in a group conversation, does it actually understand who is allowed to receive whose information — and in what context?"

---

## Today's 3 Points

1. MuPPET is the first benchmark to evaluate LLM privacy decisions through the lens of contextual integrity in multi-party settings.
2. Current major LLMs show significant vulnerabilities in contextual privacy judgment across multi-party conversations.
3. Before deploying group conversation AI, GDPR-subject organizations should run a pre-launch audit using the MuPPET evaluation protocol.

---

## ① What Is "Contextual Integrity"?

Let's start with the concept at the heart of this research: contextual integrity.

Originally proposed by philosopher Helen Nissenbaum, it's a theory of privacy that says: what makes information private isn't whether it's secret — it's whether the flow of that information matches the norms of the context in which it was shared.

Here's an example. Imagine a group customer support chat. Customer A types their home address to get help with a delivery. Another customer B, also in the thread, asks the AI: "What's the address that person just entered?"

Intuitively, the AI should not answer. But why? Not because the address is classified — but because the address was shared in the context of A communicating with a support agent. Disclosing it to another customer violates the contextual norms of that information flow.

MuPPET tests whether LLMs can make this kind of contextual judgment correctly.

---

## ② Why Group Conversations Create Unique Privacy Risks

What makes multi-party conversations harder than one-on-one interactions?

The research identifies a core challenge: complexity of information flow.

In a group conversation, multiple participants mean that "whose information is this?" and "who is this message directed at?" are constantly overlapping. Just because User A shared something with the LLM doesn't mean that information is fair game for User B.

There are also cases where information "naturally flows" in ways that feel innocuous — until it doesn't. When LLMs summarize, introduce participants, or recap conversation history, they may reference personal information outside its appropriate context.

And the group setting itself matters enormously. Is this an internal team channel? A mixed customer-service thread? A public forum? The same piece of information may be appropriate to disclose in one setting and completely inappropriate in another. MuPPET's evaluations show that current LLMs don't reliably make this distinction.

---

## ③ What the MuPPET Evaluation Protocol Looks Like

What does MuPPET actually measure?

The benchmark constructs scenarios that simulate real group conversation contexts. A multi-party conversation log containing personal information — names, affiliations, contact details, conversation content — is presented to the LLM in a setting where it plays the role of an embedded assistant.

The LLM is then asked or prompted in ways that could lead to contextually inappropriate disclosures. Using contextual integrity as the ground truth, each potential disclosure is labeled: contextually appropriate or inappropriate.

The LLM's responses are matched against these labels to produce a quantitative measure of contextual privacy accuracy.

Crucially, this isn't a simple test of "can you keep a secret?" It's asking a much more nuanced question: do you understand which information flows are appropriate to which participants in which contexts? That's what distinguishes MuPPET from earlier privacy benchmarks.

---

## ④ What Legal, Security, and DX Teams Should Do Now

So how does this research translate into enterprise practice?

Let's take group customer support as a concrete use case.

In a support format where multiple customers share the same thread, an LLM that can't reliably judge "whose information is this?" and "should I disclose this to the other participants?" creates a live privacy liability. Under GDPR, inappropriate disclosure of personal data to third parties can trigger enforcement action.

Here's a three-step pre-deployment audit using the MuPPET protocol:

First, evaluate your candidate LLM using MuPPET's scenario set before deployment. The paper-derived scenarios can be adapted to your specific use cases — Slack bots, Teams Copilot, customer support chat. This gives you a quantitative baseline for contextual privacy accuracy.

Second, redesign your system prompts and access control logic based on the evaluation results. Explicit instructions like "do not reference this participant's information to other participants" and "do not include personal details in summaries shared across the group" are effective mitigations when built into system-level prompting.

Third, build a re-evaluation cycle into your governance process. LLM updates can change behavior in unexpected ways. Running a MuPPET-based assessment semi-annually keeps your privacy posture current.

This evaluation process can be documented as part of a GDPR Data Protection Impact Assessment (DPIA). A documented record of "we conducted a group conversation privacy audit using an established benchmark" provides a concrete basis for demonstrating regulatory compliance.

---

## Privacy Exposure Isn't Covered by "We Didn't Know"

LLM integration into group conversations is genuinely powerful. The efficiency gains for customer support, internal collaboration, and team productivity are real.

But the ability to judge "who is allowed to receive whose information, in what context" is something current LLMs cannot reliably handle on their own. MuPPET has now demonstrated this with a rigorous benchmark.

Before deployment, the question "can this system make correct contextual privacy judgments?" needs an answer. Getting that answer in advance — not after an incident — is what safe rollout looks like.

---

## Reference

1. Welch, M., & Diab, M. (2026). *MuPPET: A Multi-Party Privacy Evaluation Test for LLM Assistants in Multi-Party Conversational Contexts*. arXiv preprint arXiv:2606.23217.

<p class="ai-notice"><small>Note: This article was partially written with AI assistance and may contain inaccuracies.</small></p>
