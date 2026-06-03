---
title: "Chat UI vs. Dashboard: What 134 Managers' Data Actually Says"
date: "2026-06-02"
excerpt: "An experiment with 134 manufacturing managers compared LLM-based conversational interfaces against graphical dashboards across tasks of varying complexity. The results offer a clearer picture of when to use which — and why neither is a replacement for the other. A 5-minute read for DX, ERP, and BI tool teams."
image: "/column-images/llm-conversational-vs-graphical-decision-support.png"
imageAlt: "Chat UI bubbles on the left, graphical dashboard on the right, with a central balance scale tipping based on task complexity"
readingMinutes: 5
basedOnPaper: "Neither Replacement nor Panacea: Comparing LLM-Based Conversational and Graphical Decision Support in Industrial Tasks"
basedOnPaperUrl: "https://arxiv.org/abs/2605.31287"
---

Hi, I'm Keito Inoshita from Affectosphere Group.

If you're evaluating whether to add an LLM chat feature to your ERP or production management system, you're probably sitting with two conflicting intuitions.

The optimistic case: "If managers can just ask questions in natural language, they won't have to navigate complex screens." The skeptical case: "Dashboards work fine. Chat interfaces tend to get abandoned after the first month."

Both intuitions have some truth to them. A study published on arXiv in May 2026 (Roberto Figliè, Simone Caputo, Alan Serrano et al., arXiv:2605.31287) provides experimental data to ground the debate. The researchers ran 134 manufacturing managers through a set of decision support tasks — at low, medium, and high complexity — using both an LLM conversational interface and a traditional graphical dashboard, and measured what actually happened.

The headline finding: conversational AI is neither a replacement for dashboards, nor a panacea. Which one performs better depends on the task.

---

## 3 Points for Today

1. Value: Conversational AI consistently reduced cognitive load and improved completion speed on simple tasks.
2. Limits: On complex tasks, the speed advantage disappeared — and decision accuracy was equal across both interfaces.
3. Design implications: a framework for deciding which tasks get conversational UI and which retain the dashboard.

---

## ① The Experiment Setup

A quick look at the design.

134 manufacturing managers completed three types of decision support tasks (low, medium, and high complexity) using both a conversational LLM interface and a conventional graphical dashboard. The study measured:

- Task completion time
- Decision accuracy (alignment with a defined correct answer)
- Cognitive load (via subjective scales including NASA-TLX)

The "conversational LLM" interface was a natural language chat system — managers could ask questions like "What were the main production issues this week?" and receive answers. The "graphical dashboard" was a conventional operational screen displaying KPIs, charts, and tables.

---

## ② What the Results Actually Showed

### Cognitive load was lower with conversational AI across the board

Across all task complexity levels, the conversational interface group reported lower cognitive load. This is intuitive: instead of visually scanning charts to extract information, you ask. The barrier to information access goes down.

This suggests conversational AI has particular value for users who are less comfortable with complex systems, and for high-frequency decision environments where cognitive fatigue accumulates.

### Simple tasks: conversational AI was faster

On low-complexity tasks, the conversational group completed tasks faster.

Simple information retrieval — "What's today's production count?" "What's the current inventory level for this part?" — turns out to be faster to ask than to navigate, click, and read. For this category of task, the ROI case for conversational UI is clear.

### Complex tasks: the speed advantage disappeared

On high-complexity tasks, completion times were statistically equivalent between both interfaces.

The reason makes sense in retrospect. Complex decisions require holding multiple variables in mind simultaneously — forming a gestalt of the situation before deciding. Graphical dashboards are built for this: parallel KPI displays allow visual comparison in a way that a sequential text-based conversation doesn't naturally support. When you ask a chat interface to "show me everything relevant," it produces a text list — which is harder to survey at a glance than a well-designed chart layout.

### Decision accuracy was equal regardless of interface

Neither interface produced better or worse decisions in terms of accuracy.

The concern that "AI chat will make people less analytical" or "decision quality will degrade" was not supported by this experiment. For the decision quality dimension, the interface choice didn't matter.

---

## ③ How DX Teams Can Use This

Reading the findings straightforwardly, a design framework emerges.

### Tasks where conversational AI fits

- Single-question information lookups (simple queries)
- Quick situational checks where deep analysis isn't needed
- Reducing learning overhead for users unfamiliar with the system
- Mobile and floor-level environments where navigating dashboards is impractical

### Tasks where dashboards fit

- Simultaneous multi-variable comparison and overview
- Trend detection and anomaly spotting (time-series charts)
- Deep analysis and decision documentation
- Routine reporting workflows

### The hybrid design principle

The real opportunity isn't "conversational AI OR dashboard" — it's designing the workflow so they complement each other. Conversational AI as the navigation layer: managers ask quick questions to get oriented, then move into the dashboard for deeper analysis when needed.

A concrete example for a manufacturing context: shop floor manager asks AI chat "Any alerts this morning?" → gets a summary → clicks through to the dashboard for the details → uses AI chat to log an action item. Conversational AI as the entry point; dashboard as the workspace for analysis.

---

## Let Go of the Replacement Framing

The core argument of this paper — visible in its title — is that neither "replacement" nor "panacea" is the right frame for conversational AI in industrial settings.

The DX field tends to oscillate between two poles: "AI will make legacy tools obsolete" and "AI is overhyped and won't get adopted." This research pushes back on both. Conversational AI won't replace dashboards. But it demonstrably reduces cognitive load and improves access to information for appropriate task types.

For organizations considering AI feature additions to ERP or operations platforms, this study argues for doing the pre-work: mapping your task inventory by complexity, and designing UI assignment accordingly. That's where ROI gets maximized — not by defaulting to one interface over the other, but by being deliberate about when each one earns its place.

That's all for today!

---

## References

1. Roberto Figliè, Simone Caputo, Alan Serrano, Daria Mikhaylova, Tommaso Turchi, Daniele Mazzei (2026). *Neither Replacement nor Panacea: Comparing LLM-Based Conversational and Graphical Decision Support in Industrial Tasks*. arXiv preprint.

<p class="ai-notice"><small>* This article was written in part with AI assistance and may contain inaccuracies.</small></p>
