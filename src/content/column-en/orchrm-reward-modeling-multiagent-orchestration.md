---
title: "Can an AI Orchestrator Get Better Without Human Feedback?"
date: "2026-06-15"
excerpt: "A new approach called OrchRM lets multi-agent orchestrators improve themselves by learning from intermediate outputs — reducing token costs by up to 10x while lifting accuracy by around 8%. Here is what that means for enterprise back-office automation."
image: "/column-images/orchrm-reward-modeling-multiagent-orchestration.png"
imageAlt: "A flat illustration of multiple AI agents collaborating on business tasks while a central orchestrator continuously self-improves its routing decisions"
readingMinutes: 5
basedOnPaper: "Reward Modeling for Multi-Agent Orchestration"
basedOnPaperUrl: "https://arxiv.org/abs/2606.13598"
---

Hello. This is Keito Inoshita from Affectosphere Group.

One of the most common concerns I hear from organizations exploring AI automation is this: "We want to delegate tasks to agents, but we're not confident in the output quality."

Invoice processing, contract review, HR document handling — these are all multi-step workflows. Chaining specialized agents into a pipeline tends to outperform a single generalist model. But when the orchestrator — the component that decides which agent gets the task at each step — makes poor routing decisions, the final output collapses no matter how capable the individual agents are.

And improving the orchestrator traditionally means collecting a lot of human-labeled feedback data. That is expensive, slow, and hard to scale.

A study published on arXiv in June 2026 (King Yeung Tsang et al.; arXiv:2606.13598) proposes a way around this. The approach, called OrchRM, automatically constructs learning pairs from intermediate outputs and uses them to continuously improve orchestrator quality — without requiring human annotation at each step.

---

## Three takeaways for today

1. The orchestrator's routing quality is the biggest performance bottleneck in multi-agent systems deployed for back-office work.
2. OrchRM generates training signal from intermediate pipeline outputs automatically, removing the dependency on human-labeled data.
3. Reported results include up to 10x reduction in token usage and around 8% accuracy improvement — a combination that changes the ROI picture for enterprise automation.

---

## ① What does an orchestrator actually do?

A quick framing first.

In a multi-agent system, the orchestrator is the decision layer that routes tasks. It receives a high-level instruction and decides: send this to the document reading agent first, then to the amount verification agent, then to the approval routing agent. Each step produces an intermediate output, which the orchestrator uses to decide what happens next.

When the orchestrator gets those routing decisions right, the pipeline hums. When it routes incorrectly — sending an unverified document to the approval agent, for example — even a well-tuned downstream agent cannot rescue the output.

This is why improving the orchestrator matters more than fine-tuning individual agents. A 5% improvement in orchestrator routing quality propagates through every downstream step.

---

## ② How OrchRM generates its own training data

The conventional approach to improving orchestrators relies on humans labeling decisions as "good" or "bad" after the fact. Build enough labeled pairs, run reinforcement learning from human feedback, repeat. Feasible for research demos; rarely feasible at enterprise scale.

OrchRM bypasses this by looking at the intermediate outputs that the pipeline already generates.

The core idea is to use task completion rates and final output quality as retrospective signals. When a pipeline run produces a good final result, the orchestrator decisions along the way get labeled as positive examples. When the final output is poor, those decisions become negative examples. The system automatically constructs the comparison pairs (sometimes called preference pairs) that drive the learning update.

No human in the loop for each labeling decision. The data generation scales with pipeline usage.

The paper reports that this approach lifts orchestrator accuracy by around 8% while reducing token consumption by up to 10x. Both directions simultaneously — lower cost and higher quality. That is the unusual part.

---

## ③ Where to start in back-office automation

The more interesting question is where to actually deploy this.

Three back-office functions stand out.

Finance and accounts payable is the most natural starting point. Invoice receipt, amount matching, approval routing, journal entry — this is a high-repetition, multi-step workflow where orchestration errors have downstream financial consequences. OrchRM's self-improvement loop is well-suited here because the pipeline runs repeatedly, giving it more signal to learn from faster. The right KPIs to track: processing volume per person-day and rejection rate (documents returned for correction).

Legal contract review is more complex but potentially high-value. Different contract types — NDAs, service agreements, purchase contracts — have different review priorities. An orchestrated pipeline might use a contract classification agent, a risk clause detection agent, and a regulatory cross-check agent in sequence. The orchestrator's job is to route dynamically based on document characteristics. What makes OrchRM applicable: post-signature issues (clauses that caused disputes after signing) can be fed back as quality signals to refine the orchestrator's routing logic over time. Measuring "issues discovered post-review" as a lagging quality indicator makes the self-improvement loop operational.

HR document processing is the third candidate. Resume screening, interview scheduling, onboarding document verification — all high-repetition, multi-step. The more interesting long-term possibility: if downstream outcomes (retention rates, performance ratings) are linked back to the screening pipeline's intermediate outputs, the orchestrator can learn what "good early-stage routing" actually looks like for this organization's specific hiring context.

---

## ④ Practical implementation sequence

OrchRM is not a drop-in upgrade. A few things need to be in place first.

Intermediate output design matters. The system needs clearly defined checkpoints whose quality can be evaluated retrospectively. Which pipeline stage output serves as the quality anchor? This is a domain question — finance teams need to define it for accounts payable, legal teams for contract review. Getting this right before the learning loop starts is important.

Baseline orchestrator quality sets the floor. OrchRM is a refinement method, not a bootstrap. If the starting orchestrator makes essentially random routing decisions, the automatic labeling will just reinforce noise. A reasonable starting point is to use an existing LLM as the initial orchestrator and treat OrchRM as the continuous improvement layer.

KPIs worth tracking weekly: task completion rate trend, orchestrator routing agreement with human expert review (sampled), and API cost per processed document. All three together give a picture of whether the self-improvement loop is working.

---

## The shift from "build perfect" to "improve continuously"

The most common back-office automation failure pattern is: the system doesn't perform well enough out of the box, so humans end up reviewing everything anyway, and the automation ROI never materializes.

What OrchRM suggests is a different design philosophy — build a system that gets better with use rather than a system that needs to be perfect at launch. If the accuracy gap at deployment closes automatically over weeks of operation, the pressure on the initial configuration is lower, and the path to positive ROI is clearer.

Whether that plays out in practice at your organization's scale and with your specific workflows is still an open question, and I'd encourage reading the original paper (arXiv:2606.13598) for the detailed experimental conditions. But the direction seems right for enterprise back-office automation.

That's it for today!

---

## Reference

1. King Yeung Tsang et al. (2026). *Reward Modeling for Multi-Agent Orchestration*. arXiv preprint. https://arxiv.org/abs/2606.13598

<p class="ai-notice"><small>* This article was written in part with AI assistance and may contain inaccuracies.</small></p>
