---
title: "Can You Package a Veteran's Expertise Before They Retire? COLLEAGUE.SKILL Says Yes"
date: "2026-06-02"
excerpt: "A framework called COLLEAGUE.SKILL automatically converts experts' tacit knowledge — procedural know-how, mental models, decision heuristics — into structured AI skill packages that can be edited, versioned, and transferred to other agents. For L&D, knowledge management, and AI implementation teams, this is one of the more practically grounded ideas in tacit knowledge transfer."
image: "/column-images/colleague-skill-expert-knowledge-distillation.svg"
imageAlt: "Abstract flow showing knowledge extracted from a senior employee's mind, structured into a package, and transferred to an AI agent"
readingMinutes: 5
basedOnPaper: "COLLEAGUE.SKILL: Automated AI Skill Generation via Expert Knowledge Distillation"
basedOnPaperUrl: "https://arxiv.org/abs/2605.31264"
---

Hi, I'm Keito Inoshita from Affectosphere Group.

Here's a version of a conversation many organizations have had.

"Our most experienced engineer retires next year. We ran a three-month handoff. We captured everything in the procedures manual. But what really mattered — the reasoning behind the decisions, the judgment calls in edge cases — none of that made it into the document. It couldn't."

"A consultant we trained left for another firm. The knowledge they built while here walked out the door with them."

"We wrote the manual. But nobody operates by the manual. How the work actually gets done requires watching someone do it."

This is the tacit knowledge inheritance problem — and it affects virtually every organization at some scale. Knowledge that can't be systematized. Judgment that can't be rule-coded. Intuitions that don't survive the translation to text.

A paper published on arXiv in May 2026 (Tianyi Zhou, Dongrui Liu, Leitao Yuan et al., arXiv:2605.31264) comes at this problem from the direction of AI agents. The COLLEAGUE.SKILL framework proposes automatically converting experts' practical knowledge, mental models, and decision heuristics into structured "skill packages" that AI agents can execute — and that humans can inspect, edit, version, and transfer.

---

## 3 Points for Today

1. Value: Converting tacit knowledge into structured, executable packages makes it inheritable, transferable, and improvable — instead of just lost.
2. How skill packages work: natural-language-editable, version-controlled, rollbackable, and transferable to other agents.
3. Business application: designing a knowledge preservation program for retiring veterans and AI-agent-based onboarding.

---

## ① Why Tacit Knowledge Doesn't Get Passed On

A quick framing of the structural problem.

Knowledge comes in two broad types. Explicit knowledge can be written down — procedures, checklists, technical specifications. Tacit knowledge is the kind that resists documentation: the sense of when to apply a rule and when to bend it, the pattern recognition that experts develop after years of exposure, the judgment that gets called "experience."

The reason tacit knowledge doesn't transfer well is that the act of formalizing it strips out context-dependent nuance. A veteran can write "in situation X, do Y" — but what they're actually doing is applying a decision model that depends on dozens of contextual signals they no longer consciously notice. The manual captures the output of the model, not the model itself.

This problem has a parallel in AI work. The prompts that experienced practitioners build for LLMs often encode tacit knowledge: why this prompt works is opaque even to the person who wrote it. The prompt can't be improved or adapted by someone else because the underlying logic isn't visible.

---

## ② What COLLEAGUE.SKILL Does

COLLEAGUE.SKILL aims to convert tacit knowledge into transparent packages.

The framework collects and structures expert knowledge at three levels.

### Procedural Knowledge

The "what to do, in what order" knowledge. This is the most codifiable type, but COLLEAGUE.SKILL stores it not as a static document but as a structured, agent-executable sequence — something an AI agent can actually run.

### Mental Models

The interpretive frameworks experts use to make sense of situations — the "what kind of problem is this?" judgment that happens before any procedure begins. This is the hardest knowledge to capture, and arguably the most valuable.

### Decision Heuristics

The "in situations like this, here's how I decide" rules. "The only time I override this protocol is when X." "This metric crossing this threshold means stop and escalate." The judgment patterns that come from accumulated experience.

These three layers are combined into a single skill package, written in natural language — readable and editable by non-engineers.

### Package Management Features

The key distinguishing features of COLLEAGUE.SKILL packages:

- Natural language readable/editable (domain experts, not just engineers, can verify and modify the content)
- Version control (full change history; roll back to a previous state if a change causes problems)
- Cross-agent transfer (a skill package built for one agent can be applied to another)
- Community sharing (open-source; access to 215 community-contributed skill packages at time of writing)

The project has reportedly accumulated more than 18,500 GitHub stars and an active community of skill contributors.

---

## ③ How L&D and Knowledge Management Teams Can Use This

What does this actually look like in an organizational context?

### A "Knowledge Preservation Program" for Retiring Experts

Running COLLEAGUE.SKILL sessions with veterans before they exit — structured interviews and workflow observation focused on extracting practical knowledge, mental models, and decision heuristics — creates a transferable organizational asset, not just an archive.

The critical difference from traditional handoff documentation: skill packages are executable, not just readable. A new employee or AI agent can run them and observe the output. They're designed to be a live tool, not a reference document that sits on a shelf.

Applicable contexts: senior traders' decision rules, product quality inspection criteria, client escalation judgment, grant writing expertise, regulatory compliance reasoning — any domain where "you learn it by watching someone experienced" has been the dominant transfer method.

### An AI Coach That Thinks Like Your Best People

Skill packages applied to an AI agent create a coach that operates according to the captured judgment model. New team members can query it during cases. The agent responds with reasoning aligned to the patterns the organization considers best practice.

This scales in a way direct mentorship cannot. One veteran's skill package, once created, can support parallel interactions with multiple new employees simultaneously — without requiring the veteran's time.

### Auditable Improvement Cycles

Because changes to skill packages are version-controlled, the question "did updating this judgment rule improve outcomes?" becomes tractable. You can track whether a revised heuristic performs better, and roll back if it doesn't.

Traditional tacit knowledge transfer has no such audit trail. The knowledge exists in people's heads, and whether it's working is inferred from outcomes. Packaging it introduces the possibility of systematic organizational learning.

---

## Moving Beyond the Opaque Prompt

The broader direction this research points toward is the structuring and transparency of "how we instruct AI."

Today, AI proficiency in most organizations is unevenly distributed and individually held. The people with the best prompts are effective. Others aren't, and the gap is hard to close because the knowledge is personal, not organizational.

COLLEAGUE.SKILL's design philosophy treats skill knowledge as an organizational asset — something that can be edited, managed, versioned, and inherited — rather than something that disappears when the person who holds it moves on.

Caveats: not all tacit knowledge can be packaged. Embodied skills and sensory judgment have limits that language can't overcome. The quality of automated extraction also depends on expert cooperation and the nature of the knowledge domain. And whether the approach generalizes across industries and knowledge types is still an empirical question.

But the direction — making the implicit explicit, and making the explicit manageable — is one of the more practically grounded approaches to tacit knowledge transfer that AI research has produced. Worth watching.

That's all for today!

---

## References

1. Tianyi Zhou, Dongrui Liu, Leitao Yuan, Jing Shao, Xia Hu (2026). *COLLEAGUE.SKILL: Automated AI Skill Generation via Expert Knowledge Distillation*. arXiv preprint.

<p class="ai-notice"><small>* This article was written in part with AI assistance and may contain inaccuracies.</small></p>
