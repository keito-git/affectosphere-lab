---
title: "Autonomous Driving Got Both Rules and Intuition ── ADRD's Case for Interpretable LLM Control"
date: "2026-06-01"
excerpt: "The wall that pure reinforcement learning and standalone LLMs couldn't break through in autonomous driving has been tackled by combining rule-based decision systems with LLM reasoning. ADRD achieves interpretability, response speed, and driving performance simultaneously — here's what that means for automotive and mobility teams."
image: "/column-images/adrd-llm-driving.svg"
imageAlt: "Abstract bird's-eye view of a car in motion, with a rule flowchart on the left and LLM reasoning bubbles on the right, merging at center"
readingMinutes: 5
basedOnPaper: "ADRD: LLM-Driven Autonomous Driving Based on Rule-based Decision Systems"
basedOnPaperUrl: "https://arxiv.org/abs/2506.14299"
---

Hi, I'm Keito Inoshita from Affectosphere Group.

Conversations with autonomous driving teams tend to hit the same wall.

"Adding an LLM makes the system more flexible. But we can't explain what it's basing its decisions on."

"Our RL model is stable, but it does strange things in unusual scenarios."

"The safety team can't sign off if they can't explain the AI's decisions."

Autonomous driving AI has long been pinned between a tradeoff: flexibility vs. explainability. Lean toward LLMs and decisions become opaque. Lean toward rule-based systems and edge case handling suffers. This has been the industry's basic structural constraint.

A 2026 arXiv paper (Fanzhi Zeng, Siqi Wang, Chuzhao Zhu, Li Li, arXiv:2506.14299) reports an attempt to break through this constraint. The ADRD framework — integrating LLM reasoning with a rule-based decision system — demonstrated advantages over reinforcement learning and standalone LLM approaches on all three dimensions: interpretability, response speed, and driving performance.

Today I'll break down the research for automotive, mobility, and safety engineers.

---

## 3 Points for Today

1. Value: Combining rule-based "certainty" with LLM "flexibility" achieves interpretability, speed, and performance simultaneously.
2. ADRD's 3 components: why the division of labor between the Information, Agent, and Test modules works.
3. What's different from LLM-only: what breaks when you rely on LLM alone, and what ADRD fills in.

---

## ① The Hybrid Idea: Rules + LLM

A quick framing of the landscape.

Autonomous driving decision systems have evolved through several major approaches:

Rule-based (classical): humans write explicit "in situation X, do action Y" logic. High transparency, but brittle when encountering situations the rules didn't anticipate (edge cases).

Reinforcement learning: learns optimal actions through environmental interaction. Better at edge cases, but "why did it make that decision?" is hard to answer.

Standalone LLM: strong at natural language understanding and contextual reasoning. Handles complex intent interpretation well, but real-time response latency and consistency guarantees are difficult.

ADRD (Zeng et al., 2026) is a hybrid of these. The paper positions it as "the first integration of LLM with rule-based systems" in this domain, emphasizing real-world deployability.

---

## ② ADRD's Three Components

ADRD is built around three modules.

### Information Module

This module collects and structures driving context. Sensor data, movements of surrounding vehicles and pedestrians, road conditions, applicable traffic regulations — all the information needed for decision-making is organized and formatted.

Its job is converting raw context into something the LLM can reason about effectively. Passing raw sensor streams to an LLM produces poor reasoning. Passing structured, contextual descriptions produces useful judgment.

### Agent Module

This is the core module where the LLM generates tactical decisions. Drawing on the structured context from the Information Module, the LLM handles judgments like "should we change lanes here?" or "is that pedestrian about to cross?"

The critical design point: the LLM generates tactics; a rule-based system handles execution. LLM outputs pass through rule-based filters that automatically exclude legally non-compliant actions, physically impossible maneuvers, and dangerous behaviors.

### Test Module

This module handles iterative improvement. Decisions from the Agent Module are tested in simulation environments, with feedback returned. Edge cases that failed are accumulated to improve future decision quality.

This is structurally difficult for standalone LLMs. Because LLM outputs vary for the same input, safety-critical contexts require a baked-in "test and improve" loop — which is what the Test Module provides.

---

## ③ Comparison With Existing Approaches

The paper benchmarks ADRD against RL-based systems and existing LLM approaches, reporting advantages on three dimensions.

Interpretability: By combining with a rule-based system, the reasoning behind each decision can be traced after the fact. The explainability that was difficult with standalone LLMs is preserved through the rule layer.

Response speed: By constraining LLM involvement to scenarios requiring complex contextual reasoning, overall processing speed improves. Simple rule-application cases are handled immediately by the rule-based component.

Driving performance: Edge case handling improves. The LLM produces flexible tactical judgments; the rule-based system guarantees their safety. This division of labor raises performance in unexpected scenarios.

"Improving interpretability, speed, and performance simultaneously" was a difficult claim to make under previous approaches. The fact that it's supported experimentally here is the core contribution.

---

## The Evaluation Axis for Autonomous Driving AI Is Shifting

The direction this framework points to aligns with a broader shift in how autonomous driving AI gets evaluated.

Evaluating AI on model accuracy alone is increasingly insufficient. As safety and explainability enter regulatory requirements, "can you explain why this decision was made?" and "if something goes wrong, can you tell which component failed?" are becoming selection criteria.

ADRD directly addresses this direction. "Combining LLM intelligence with rule-based explainability" as a design philosophy is a generalizable reference point for deploying AI in high-safety-requirement industrial contexts.

The next competitive axis in autonomous driving may be moving from "how smart is it?" to "how explainable is its intelligence?"

That's all for today!

---

## References

1. Fanzhi Zeng, Siqi Wang, Chuzhao Zhu, Li Li (2026). *ADRD: LLM-Driven Autonomous Driving Based on Rule-based Decision Systems*. arXiv preprint.

<p class="ai-notice"><small>* This article was written in part with AI assistance and may contain inaccuracies.</small></p>
