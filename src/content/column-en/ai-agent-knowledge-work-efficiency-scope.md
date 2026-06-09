---
title: "AI Agents Can Return 87% of Your Time — But That's Not Even the Main Story"
date: "2026-06-09"
excerpt: "Production data from Perplexity shows autonomous AI agents cut task time by 87% and costs by 94%. But the more important finding is what happens to workers after the time savings arrive."
image: "/column-images/ai-agent-knowledge-work-efficiency-scope.png"
imageAlt: "A flat illustration of an AI agent autonomously handling multiple knowledge work tasks across different domains"
readingMinutes: 5
basedOnPaper: "How AI Agents Reshape Knowledge Work: Autonomy, Efficiency, and Scope"
basedOnPaperUrl: "https://arxiv.org/abs/2606.07489"
---

Hello. This is Keito Inoshita from Affectosphere Group.

"AI will make us more efficient" is a familiar claim by now. What gets discussed less is what happens to knowledge workers after the efficiency gains arrive.

A study published on arXiv in June 2026 (Jeremy Yang, Kate Zyskowski, Noah Yonack, Jerry Ma; arXiv:2606.07489) is one of the first to answer that question using real production data. The researchers used actual usage logs from Perplexity's products — not a controlled experiment, but the behavior of real users across their daily work.

---

## Three takeaways for today

1. Autonomous AI agents cut task completion time by 87% and costs by 94% compared to search-based AI on the same tasks.
2. Agents reduced user dissatisfaction rates by 55%, improving quality and efficiency simultaneously.
3. After adopting agents, users took on more complex, cross-domain tasks — a "scope expansion effect" with direct implications for how organizations should frame AI deployment.

---

## ① What 87% time reduction actually means

Let's start with the numbers.

When comparing Perplexity Search (conversational AI with search) and Perplexity Computer (autonomous agent) on the same tasks, the differences were stark:

- Task completion time: 269 minutes → 36 minutes (87% reduction)
- Cost: 94% reduction
- User dissatisfaction rate: Computer showed 55% lower dissatisfaction than Search

The difference in autonomous operation time is also striking. Search operates for roughly 33 seconds per user session. Computer operates autonomously for 26 minutes per session — the user simply waits while the agent works through the task.

Those 26 minutes represent something specific: the agent decomposing a task into subtasks, executing each sequentially, verifying intermediate results, and producing a finished output. Not just retrieving information, but completing a workflow.

That's what drives the 87% time reduction.

For organizations evaluating AI adoption, this distinction matters. Most "efficiency improvement" estimates for enterprise AI are projections or limited pilots. This study demonstrates 87% reduction using live production data from a deployed product — which is a materially higher bar of evidence.

---

## ② Why dissatisfaction rates fell at the same time

The simultaneous improvement in efficiency and quality is one of the more interesting findings.

The typical trade-off in process optimization is speed versus quality: faster usually means rougher. But this study shows user dissatisfaction rates falling 55% relative to Search, at the same time as task time falls 87%.

The research attributes this to task decomposition and execution automation. With search-based AI, users must issue queries one at a time, receive partial results, and integrate the pieces themselves. With an autonomous agent, that synthesis happens internally. Users receive a completed output rather than components they need to assemble.

The cost that disappears isn't just time — it's the cognitive overhead of doing the integration work, managing partial results, and deciding what to search next. Removing that overhead appears to be what drives satisfaction upward.

For implementation planning, this has a practical implication: tracking time reduction alone as the primary KPI will miss half the story. The user experience data suggests that time, cost, and satisfaction can improve together — but you need to measure all three to see it.

---

## ③ The scope expansion effect — the most important finding

This is the part of the research I find most significant.

After adopting autonomous agents, users didn't simplify their behavior. They expanded it.

The study found that users of Computer increasingly directed it toward queries spanning multiple occupational domains — more complex, cross-functional tasks than they had previously attempted. The researchers describe this as a "scope expansion effect."

In practical terms: when an agent handles routine information-gathering and synthesis tasks, users shift toward work they previously couldn't get to. Tasks that required coordinating multiple people or multiple days started completing within a session. Users who experienced that possibility then set their sights on more complex problems.

This reframes the question of what AI agents are for. The story isn't "AI agents replace workers." The story is "AI agents expand the scope of what a knowledge worker can engage with."

A research analyst who previously spent half their time on data collection can now spend that time on interpretation, synthesis, and strategic framing. A business planner who avoided cross-domain analyses because they were too time-intensive can now run them routinely. The constraint that was shaping which problems were worth attempting — time — becomes less binding.

---

## How to try this in your organization

If you're thinking about how to bring these findings into practice, here's a suggested starting point.

First, identify tasks that consist primarily of repetitive information gathering and integration. Likely candidates:

- Corporate planning: market research reports, competitive landscape summaries, earnings analysis
- DX teams: cross-functional knowledge base searches, vendor comparison reports
- HR and recruitment: candidate research, industry salary benchmarking
- Operations: data collection, consolidation, and reporting across multiple sources

These are tasks where the current constraint is that a person must manually navigate multiple sources, integrate the results, and format the output. Autonomous agents have a structural advantage here.

For KPIs, I'd suggest tracking three metrics:

- Task completion time (measurable before and after deployment)
- Rate at which teams initiate previously-deferred complex tasks (to detect scope expansion)
- Output quality metrics (review pass rates, satisfaction scores)

The second metric — detecting scope expansion — is the critical one to add. If you only track time savings, you will miss the higher-order value. The right question to ask is: "Are teams now working on problems they weren't able to get to before?"

The answer to that question is what separates AI agent deployment that changes how work is done from AI agent deployment that just makes the same work faster.

---

## Investing in work that was previously out of reach

The most significant return on AI agent deployment may not be cost reduction.

It may be that teams finally get to tackle the cross-functional, analytically complex work they've been deferring for years — because time was the constraint and the constraint is now much weaker.

This study is one of the first to document that shift using production data rather than projections. When designing a pilot, build scope expansion into the evaluation criteria from the beginning — not just "how much time did we save?" but "what did we do with it?"

That's it for today!

---

## Reference

1. Jeremy Yang, Kate Zyskowski, Noah Yonack, Jerry Ma (2026). *How AI Agents Reshape Knowledge Work: Autonomy, Efficiency, and Scope*. arXiv preprint.

<p class="ai-notice"><small>* This article was written in part with AI assistance and may contain inaccuracies.</small></p>
