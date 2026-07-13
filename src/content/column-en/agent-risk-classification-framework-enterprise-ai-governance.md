---
title: "Stop debating from scratch how hard to review each AI agent — risk-tiering internal agents with a 12-dimension score"
date: "2026-07-13"
excerpt: "The more AI agents your teams build in-house, the more the line between 'light review' and 'escalate to the board' comes down to one person's gut. The TrustX Agent Risk Classification Framework (ARC) scores seven types of agentic systems across 12 dimensions, folds in a five-level autonomy model, and returns a three-tier governance output with mapped controls. Here is how risk, legal, and IT-control teams could try it — departments and KPIs included."
image: "/column-images/agent-risk-classification-framework-enterprise-ai-governance.png"
imageAlt: "Flat illustration of a governance review line where internally built AI agents pass through a 12-item scorecard and are sorted automatically into low, medium, and high risk-tier trays"
readingMinutes: 5
basedOnPaper: "TrustX Agent Risk Classification Framework (ARC): Risk-Tiering Internally Created Agentic AI Systems"
basedOnPaperUrl: "https://arxiv.org/abs/2607.09586"
---

Hello. I am Miura from Affectosphere Group.

If your company is building AI agents in-house, you may recognize this conversation.

"That meeting-notes agent the sales team built — does it need a review?" "What about the invoice-processing agent in finance? I hear it updates the system on its own." "And coding assistants — are those even in scope for AI governance?"

Agents keep sprouting all over the company, and the line between what gets scrutinized and what gets waved through rests on someone's instinct. Worse, the reasoning is never recorded. So the next similar case comes along, and the same debate starts over from zero.

A study published on arXiv (Liu, Saxena & Asthana, arXiv:2607.09586) goes straight at turning this agent risk-tiering into a system. What they propose is the TrustX Agent Risk Classification Framework — ARC for short.

Today I want to look at this from a business-application angle and think about how you could bolt it onto your own review process.

---

## Three takeaways

1. Agentic AI has proliferated so fast across enterprise and public-sector settings that general-purpose AI risk frameworks can no longer classify or govern it. ARC is proposed as a purpose-built tool to close that gap.
2. ARC is a structured, repeatable assessment tool applicable to seven types of agentic AI systems. It quantifies risk with a 12-dimension scoring rubric, combines classification models called GPA and IAT with a five-level autonomy framework, and returns a three-tier governance output with mapped control recommendations.
3. It gives you a base for standardizing which agent gets which level of review and oversight — a real seed for a pre-build assessment gate in risk management, legal, and IT control workflows.

---

## ① Why general AI risk frameworks cannot judge agents

Let me start with why the existing frameworks fall short.

AI risk assessment so far has, roughly, looked at what a model outputs. Is the prediction biased? What happens if it misclassifies?

But an agent does not stop at output. It calls tools, hits APIs, and rewrites the state of other systems. Sometimes it decides its own next action without a human in the loop.

The substance of the risk has moved from what it says to what it does. Two agents can return the same sentence, but if one writes it to an internal wiki and the other updates a production database, the weight of oversight they need is not remotely the same.

What this study flags is exactly that: the classification and governance capacity of general frameworks has been outpaced by the proliferation of agentic systems. Hence the case for an assessment tool that is agent-specific, structured, and repeatable.

Repeatable is the quietly important word here. A different reviewer should reach the same conclusion. That is the minimum bar for anything you want to call a system.

---

## ② What ARC actually does: 7 categories, 12 dimensions, 5 autonomy levels

Let me walk through the structure as the paper describes it.

First, scope. It is designed to apply to seven types of agentic AI systems. The entry step is placing each of your internal agents into a type.

Next, assessment. A 12-dimension scoring rubric quantifies the risk. Instead of saying "this one feels dangerous," you score it along fixed axes. This is the part that kills the reliance on personal judgment.

Layered onto that are classification models called GPA and IAT, plus a five-level autonomy framework. Treating autonomy as a graded scale strikes me as a very practical instinct. Does a human approve every action, only check afterward, or hand over the wheel entirely? For the same feature set, the fear factor jumps sharply as that level climbs.

Then the output. ARC returns a three-tier governance output along with mapped control recommendations. You get a verdict and a set of moves together: this agent lands in the middle tier, therefore apply these controls.

A framework that hands you a verdict and leaves the rest to the field tends to stall. Returning mapped control recommendations is, from an implementer's seat, the generous design choice.

The framework also includes a specialized extension for Coding Assistants. Given that coding assistants are usually the first agents to multiply inside a company, that targeted coverage feels grounded in reality.

---

## ③ How to try it on the floor: departments and KPIs

So how would you try this in your own organization? Here is my rollout scenario.

The aim is to embed ARC as a mandatory pre-build risk assessment gate. Any team that wants to build or adopt an AI agent in-house runs it through the ARC sheet before they start. Which of the seven categories is it? What is the score across the 12 dimensions? What autonomy level? That determines which of the three tiers it falls into, and the required review and controls attach automatically.

Low tier clears with a team-internal review. Middle tier goes through risk management. High tier escalates to a joint review by legal, information security, and the AI office. Once it becomes that mechanical, review gets faster.

The departments I have in mind are these. First, risk management — the owner of the assessment and the tier definitions, running them as an internal standard. Second, legal and compliance, who can use "how did we classify this system, and why" as material for accountability under regulation such as the EU AI Act. To be precise: this paper does not claim to have validated compliance with the EU AI Act. That the internal classification records could serve as a base for regulatory response is my own reading.

Third, IT control and information security — the team that decides which technical controls actually get applied to agents landing in the high tier. And finally, the AI office, which drives in-house agent building and can hand teams the design patterns that clear the gate easily.

For measurement KPIs, so you can tell the story in numbers, I propose the following.

First, AI incident count — how agent-caused incidents move before and after tiering. Second, regulatory audit pass rate and finding count — how much lighter audit response gets once classification records exist. Third, AI risk review lead time. How many days a review takes is the quietly decisive metric, because it determines whether teams route around governance. Fourth, efficiency against compliance cost — how many agents you can clear per unit of review effort.

On sequencing, I would not make it company-wide mandatory on day one. Start with coding assistants only, using the framework's extension for them. Watch whether the verdicts match what the teams themselves find reasonable. Where they diverge, tune the rubric weights for your organization. Widen the categories once trust has accumulated.

Governance systems get quietly routed around unless the people inside them believe they are fair. Whether you can build that belief on the first lap is the whole game.

---

## Toward governance that exists to let things through faster

What I found interesting in this paper is that risk-tiering is not really a mechanism for stopping development. It is a mechanism for letting things through faster.

Review everything with the same weight and the review board clogs, the teams wait, and waiting teams eventually learn to avoid review altogether. That is the truly dangerous outcome.

But if a team knows up front that "this is low tier, so it clears in two days," they walk through the gate willingly. And you get to concentrate review resources on the agents that genuinely scare you — the ones autonomously rewriting production systems.

The number of agents is almost certainly going to grow. If so, the case-by-case debate model will break at some point. Build the vocabulary of classification and tiers inside the company now. As a starting draft, ARC looks like a distinctly practical shape.

That is it for today!

---

## References

1. Liu, Hannah M., Saxena, Rhea, & Asthana, Shiv (2026). *TrustX Agent Risk Classification Framework (ARC): Risk-Tiering Internally Created Agentic AI Systems*. arXiv preprint. https://arxiv.org/abs/2607.09586

<p class="ai-notice"><small>* This article was written in part with AI assistance and may contain inaccuracies.</small></p>
