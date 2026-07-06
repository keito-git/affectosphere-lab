---
title: "Fixed Scripts Can't Persuade a Resident Who Refuses to Evacuate — The Era of Per-Utterance Policy Switching"
date: "2026-07-06"
excerpt: "When residents refuse to evacuate a burning building, which persuasion strategy should an AI choose? DiPS, a Q-learning dialogue policy framework, offers an answer — and a blueprint for high-stakes call center scenarios."
image: "/column-images/dips-dialogue-policy-persuasion-rl.png"
imageAlt: "A flat illustration of dialogue branching. A flowchart where persuasion policies switch at each turn"
readingMinutes: 5
basedOnPaper: "DiPS: Dialogue Policy Selection for High-Stakes Persuasion Agents"
basedOnPaperUrl: "https://arxiv.org/abs/2607.01557"
---

Hello. This is Miura from Affectosphere Group.

"Please evacuate now." "I'm staying."

This kind of exchange happens in real fire emergencies — and lives depend on how well the next response is chosen.

Structurally, it's remarkably similar to a call center scenario where a customer has firmly decided to cancel their insurance policy, and the agent's next move determines whether they stay or go.

In both cases, the other party has already made up their mind. The challenge is changing it. And in both cases, a fixed script often isn't enough.

A study published on arXiv (Zhang et al., arXiv:2607.01557) tackles this "high-stakes persuasion" problem using reinforcement learning. Their Q-learning framework, DiPS, analyzes the resident's most recent utterance at each turn and dynamically selects the most effective persuasion policy for that moment.

---

## Today's 3 Points

1. Using a fire evacuation scenario, DiPS — a Q-learning framework — analyzes each utterance and dynamically selects the optimal persuasion policy per turn.
2. DiPS outperformed zero-shot LLM and RAG baselines in both simulation and human interaction.
3. The results validate a new agent class: the "situationally adaptive persuasion AI."

---

## When Persuasion Failure Has Consequences

The research setting is a fire evacuation scenario. The agent plays a firefighter trying to convince a resident to leave immediately. The resident role is played by a simulator or, in some conditions, real human participants.

The core difficulty: there is no single correct script.

One resident refuses out of overconfidence ("I'll be fine"). Another is emotionally attached ("I can't leave my cat"). A third doesn't trust authority figures ("I'm not listening to officials").

The same goal — "please evacuate" — requires completely different approaches depending on why the person is resisting. Pushing logical arguments at someone whose resistance is emotional often backfires. Emotional appeals to someone who needs factual reassurance don't land either.

This maps directly onto call centers. A customer who says "I want to cancel" may be doing so because of cost concerns, dissatisfaction with service quality, a better offer from a competitor, or distrust of their assigned account manager. A fixed script can only respond to the average of these — and in high-stakes moments, average is rarely enough.

---

## What DiPS Solves

Before DiPS, LLM-based persuasion agents used two main approaches.

The first was zero-shot prompting — give the LLM persuasion guidelines and let it figure out the execution. The second was RAG (retrieval-augmented generation) — retrieve successful past conversations and use them as reference.

Both approaches share a structural limitation: they rely on knowing good persuasion strategies in advance, not on adapting to what the other person is actually saying right now. Think of it as reading a great persuasion textbook, then applying it uniformly regardless of who you're talking to.

DiPS takes a fundamentally different path. It analyzes the resident's most recent utterance at each turn and selects the most effective persuasion policy dynamically for that specific moment.

The mechanism is Q-learning: the system learns a mapping from "which policy used in which situation" to "how much reward (evacuation success) it produced." Rather than executing a predetermined strategy, DiPS selects whichever policy has the highest expected value at each moment in the dialogue.

The input driving that decision is the other party's last words. If the resident says "but my neighbor is still here too," DiPS might switch to a strategy that addresses social conformity pressure. If they say "the fire is still far away," it might pivot to risk reframing with factual information. This dynamic responsiveness is the system's core value.

---

## Beating Zero-Shot and RAG

DiPS outperformed both zero-shot LLM and RAG baselines in simulation and human interaction conditions.

What this result tells us is that "knowing many good persuasion examples" or "teaching the LLM persuasion principles via prompt" matters less than "dynamically choosing the right approach for this specific person right now."

The problem isn't the quantity of knowledge. It's the quality of the in-context judgment call.

Trained with evacuation success rate as the reward signal, DiPS moves beyond "a well-informed AI" into a different category: "an AI that reads the situation and adjusts its strategy." The researchers label this a new agent class — the situationally adaptive persuasion AI.

Notably, the advantage held in human interaction conditions, not just simulation. That the policies learned from a simulator also transferred to real human conversations suggests that DiPS captured something genuine about the structure of persuasion in practice.

---

## Transferring DiPS to Call Center Scenarios

Let's think concretely about applying DiPS's design logic to "high-stakes churn" scenarios in call centers.

Target scenarios: insurance cancellation prevention, loan application conversion, employee retention conversations. What these share is a negotiation structure where the other party has already made or is leaning toward a decision, and the agent's task is to shift or reinforce it. And critically, the best next move depends on what the other person says next — making this a dynamic, sequential problem.

The transfer has two parts.

First: replace fixed scripts with a menu of persuasion policies. Design distinct styles in advance — "empathy mode (acknowledge the emotion)," "logical mode (present data and cost-benefit)," "alternative mode (offer substitute solutions)," "social proof mode (cite third-party examples or testimonials)." These become the routing targets.

Second: build a dialogue control layer that analyzes the customer's most recent utterance in real time and proposes which policy to apply next. The human operator sees this suggestion and carries it into the conversation — "AI-coached dialogue" in practice.

This isn't "AI replaces the operator." It's "AI coaches the operator in real time, turn by turn." The situational reading skill that currently lives in experienced operators' intuition gets partially systematized and made available to everyone on the team.

KPIs could be: cancellation prevention rate, application conversion rate, retention rate post-conversation — whatever "reversal rate" means in your specific context. You can measure how much dynamic policy selection improves these versus a fixed script baseline.

For implementation, a practical starting point is pairing a commercial LLM with a policy selection agent. Display real-time suggestions on the operator's screen: "For your next response: acknowledge their concern about cost first, then present the premium reduction option." Begin with an advisory display, accumulate data, and gradually move toward deeper automation where the data supports it.

---

## What "Reading the Room" Really Means for AI

What makes this research compelling is how it reframes "persuasion" as a sequential decision-making problem across time.

This is how skilled human persuaders actually work, isn't it. You try an emotional appeal first; if it doesn't land, you shift to concrete benefits; if that doesn't move them, you bring in a third-party voice. We do this strategy switching intuitively, and often unconsciously.

DiPS formalizes that intuition and optimizes it with reinforcement learning. The underlying logic is universal: it applies to any high-stakes dialogue where the goal is to shift someone's position.

The scope extends well beyond call centers. Medication adherence support in healthcare, dropout prevention counseling in education, settlement recommendations in legal consultation — any dialogue with the structure "encourage the other party to reconsider" sits within the reach of this approach.

The shift from "an average response for an average situation" to "the best response for this specific person in this specific moment" — that's what DiPS demonstrates is achievable, and what the situationally adaptive persuasion AI category opens up.

---

## Reference

1. Tianyi Zhang, Mousumi Das, Abrar Anwar, Jesse Thomason, David Traum (2026). *DiPS: Dialogue Policy Selection for High-Stakes Persuasion Agents*. arXiv preprint.

<p class="ai-notice"><small>* This article was written in part with AI assistance and may contain inaccuracies.</small></p>
