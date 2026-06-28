---
title: "Add AI Agents Without Replacing Legacy Workflows: The Process Harness Approach"
date: "2026-06-28"
excerpt: "The number one barrier to AI agent adoption in regulated enterprises is the existing workflow infrastructure you cannot simply replace. A new study proposes a Process Harness — a policy-controlled agent layer that wraps around legacy workflow engines rather than replacing them. Demonstrated in a loan screening workflow on CUGA FLO, here is what it means for DX teams and IT departments in regulated industries."
image: "/column-images/agentic-bpm-process-harness-legacy-workflow-uplift-cuga-flo.png"
imageAlt: "A flat illustration showing an agent layer wrapping around a legacy workflow engine, with TaskAgent, DecisionAgent, and FlowAgent operating in parallel"
readingMinutes: 5
basedOnPaper: "A Process Harness for Uplifting Legacy Workflows to Agentic BPM: Design and Realization in CUGA FLO"
basedOnPaperUrl: "https://arxiv.org/abs/2606.27188"
---

Hello. This is Keito Inoshita from Affectosphere Group.

"We want to automate knowledge-intensive tasks with LLM agents, but we have existing workflow systems that we simply cannot replace."

This is one of the most consistently recurring constraints faced by DX teams and IT departments. Workflow engines in finance, insurance, healthcare, and public administration are deeply entangled with compliance controls, audit logs, and approval frameworks. A full system replacement is not an option.

A June 2026 study (Fournier & Limonad, arXiv:2606.27188) proposes a way out of this bind: the Process Harness, a mechanism that places a policy-controlled agent layer around the legacy workflow engine rather than replacing it. The design is realized in CUGA FLO using a loan screening workflow as the demonstration case.

---

## Today's 3 Points

1. A Process Harness places three agent types — TaskAgent, DecisionAgent, and FlowAgent — around an existing workflow engine in a Task-Decision-Flow (TDF) model, enabling gradual uplift to agentic BPM without system replacement.
2. The design structurally separates mandatory requirements (compliance, legal constraints) from normative requirements (adaptive, context-sensitive judgment), maintaining deterministic control where it is required.
3. Existing IT governance — audit logs, approval records, compliance trails — is preserved throughout, making this design specifically suited for large-enterprise DX in regulated industries.

---

## ① Why "Not Replacing" Is the Strategic Advantage

When organizations consider deploying AI agents, the most common blocker is coexistence with legacy systems.

Workflow engines in regulated industries are not just software. They are the implementation of legal obligations, audit requirements, and organizational accountability structures. "Migrating to a new AI agent system" means migrating all of that — at enormous cost, risk, and regulatory exposure.

The Process Harness escapes the replace-or-do-nothing binary. The legacy system stays exactly where it is. A new layer of judgment capability is added around it. The new architecture does not replace the old system; it wraps it.

This framing is practically important. DX leadership can pursue agent-driven improvement without having to win the argument for a full system overhaul. The first step is an overlay, not a replacement.

---

## ② The Task-Decision-Flow (TDF) Model

The research proposes a design framework called the Task-Decision-Flow (TDF) model, assigning each of three agent types a distinct role.

TaskAgent handles individual tasks within the workflow — document verification, data entry, external system lookups. These are the manual execution steps that humans historically performed. TaskAgent takes over their execution.

DecisionAgent handles judgment points. In loan screening, this includes questions like "how should this applicant's credit risk be assessed?" or "does this case require exception handling?" — the kind of knowledge-intensive judgments that rule-based systems cannot adequately handle. DecisionAgent applies LLM reasoning here.

FlowAgent monitors the overall process flow. It manages sequencing: "what should happen next after this task completes?" and "which route should this exception take?" It serves as the orchestration layer.

Critically, all three agents are placed outside the existing workflow engine. The engine itself is unchanged. The agents subscribe to the engine's events and triggers, providing judgment and execution where the engine alone falls short.

---

## ③ Separating Mandatory and Normative Requirements

The most distinctive aspect of the Process Harness design is its structural separation of what must be done deterministically from what can be handled adaptively.

Mandatory requirements are legally or contractually non-negotiable procedures. In loan screening: identity document verification, anti-money-laundering checks, compliance with lending limits. These cannot be delegated to agent judgment. They must execute deterministically.

Normative requirements are where contextual adaptation improves outcomes. "Assess creditworthiness given this applicant's employment context." "Generate a review comment that accounts for similar historical cases." These are knowledge-intensive, context-dependent judgments that uniform rules cannot handle well.

The Process Harness assigns each category to its proper layer. The workflow engine enforces mandatory requirements. The agent layer handles normative requirements adaptively. This separation means compliance teams retain certainty about rule adherence while business users gain access to more intelligent judgment.

---

## Implementation Hypotheses for DX and IT Departments

The target deployment context is large enterprises in regulated industries with existing BPM tools or workflow engines.

Beyond loan screening, the same structure applies to:

- Procurement approval workflows: DecisionAgent evaluates amount, category, and supplier context; FlowAgent dynamically routes exceptions. KPI: approval lead time reduction.
- Contract management and renewal decisions: DecisionAgent handles renewal condition evaluation and negotiation priority. KPI: missed renewal rate reduction and review cost savings.
- Compliance report drafting: TaskAgent collects logs across systems; DecisionAgent scores risk and structures the report. KPI: reduction in reviewer hours.

A phased rollout approach makes sense. Phase one: deploy the harness in observation mode, where agents generate recommendations but humans make final decisions. This phase validates agent judgment quality and builds organizational trust.

Phase two: expand autonomous execution to lower-risk tasks incrementally. Start with TaskAgent automating data collection and document sorting. Expand DecisionAgent autonomy to tasks where confidence scores consistently exceed defined thresholds.

---

## Designing Around Constraints Rather Than Against Them

AI adoption discussions in large enterprises almost always end up at the same wall: how do we integrate with existing systems without destabilizing what already works?

The Process Harness reframes that question. Instead of trying to minimize or overcome legacy infrastructure, it treats legacy infrastructure as the stable foundation and adds intelligence around it.

Nothing is replaced. Something is added.

This is still an arXiv preprint, and validation across different industries and workflow scales presumably lies ahead. But as a design pattern for organizations that need to introduce AI autonomy without sacrificing existing IT governance, the Process Harness offers a credible and practically deployable framework — one that may be particularly well-suited to the DX context in Japan, where legacy system preservation constraints are especially strong.

---

## Reference

1. Fournier, F., & Limonad, L. (2026). *A Process Harness for Uplifting Legacy Workflows to Agentic BPM: Design and Realization in CUGA FLO*. arXiv preprint.

<p class="ai-notice"><small>* This article was written in part with AI assistance and may contain inaccuracies.</small></p>
