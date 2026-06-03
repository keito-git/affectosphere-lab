---
title: "One Sentence About AI's Limitations Makes People Use It More Carefully"
date: "2026-06-04"
excerpt: "A randomized experiment with 252 students found that simply warning users about AI fallibility significantly increased help-seeking behavior. No system changes. No training program. Just a disclosure. Here's what this means for how organizations deploy AI tools."
image: "/column-images/ai-fallibility-warning-help-seeking.png"
imageAlt: "Abstract visualization of an AI tool interface with a fallibility disclaimer, showing users taking active verification steps rather than passive acceptance"
readingMinutes: 5
basedOnPaper: "Warning About AI Fallibility Increases Help-Seeking in an Intelligent Tutoring System"
basedOnPaperUrl: "https://arxiv.org/abs/2606.03822"
---

Hi, I'm Keito Inoshita from Affectosphere Group.

One of the persistent concerns about enterprise AI deployment: users will trust AI outputs more than they should.

They'll accept AI-generated responses without verification. They'll defer to AI recommendations even when their own judgment would catch the error. In high-stakes domains — healthcare, legal, financial — this isn't just a usability problem. It's a risk management problem.

The standard response is AI literacy training. Teach users to think critically about AI outputs, understand model limitations, verify before acting.

Training is real and valuable. But a paper published on arXiv in June 2026 (Tomohiro Nagashima, Mirella Hladký, Vera Rief, arXiv:2606.03822) demonstrates that a far lighter-weight intervention works: just telling people that the AI can make mistakes.

In a randomized experiment with 252 students using an intelligent tutoring system, pre-warning about AI fallibility significantly increased active help-seeking behavior. Nothing in the AI changed. Only the disclosure did.

---

## 3 Points for Today

1. Lightweight disclosure changes behavior: warning about AI fallibility increased help-seeking significantly with no changes to the underlying system — essentially a zero-infrastructure cost intervention.
2. The target isn't distrust — it's calibrated trust: the goal is not to make users avoid AI but to activate their own judgment alongside it. This paper shows a disclosure can move users toward that state.
3. Direct application to enterprise AI tools: a single sentence in the UI, or a standard section in AI onboarding materials, is a deployable version of this intervention today.

---

## ① What the Experiment Found

The research context is an intelligent tutoring system (ITS) — an AI-powered learning tool that provides students with hints and feedback as they work through problems. This is a setting where over-reliance is an active concern: if students always defer to the AI's hints without developing their own understanding, the system undermines the learning it's supposed to support.

The experimental design was simple. Students were randomly assigned to two conditions before a learning session:

Condition A: shown a brief statement that the AI in this system can make mistakes.

Condition B: no information about AI limitations.

The AI system itself was identical for both groups. The researchers measured how often students actively sought additional help (hints, clarifications, verification steps) during the session.

The result: students who received the fallibility warning showed significantly more help-seeking behavior than those who did not.

The intervention didn't make students distrust the AI or avoid using it. It made them more actively engaged with the material — more likely to verify, ask follow-up questions, and take ownership of their learning rather than deferring passively.

---

## ② The Concept: Trust Calibration

There are two failure modes in human-AI interaction.

The first, more discussed, is over-trust. The AI said it, so it must be right. This leads to unverified errors propagating into decisions.

The second, less discussed, is under-trust. The AI is unreliable, so I'll ignore it. This leaves legitimate AI value untapped.

The target state — what the research literature calls trust calibration — is understanding where the AI is reliable and where it isn't, and adjusting reliance accordingly.

What this paper shows is that a fallibility disclosure can shift users toward trust calibration without training, without system changes, and without extended intervention. The mechanism appears to be activation of the user's own agency: "the AI may be wrong, which means I'm part of the process."

That mental shift — from passive reception to active judgment — is what drives the help-seeking behavior. And it's achieved by a single piece of information provided before the session begins.

---

## ③ Applying This to Enterprise AI Tool Design

The intelligent tutoring system context translates directly to several enterprise use cases.

### Add a fallibility notice to AI copilot and assistant interfaces

The minimum viable intervention: a single-line disclosure in the UI where AI outputs are displayed.

"This AI can make mistakes. Please verify important information before acting on it."

Expected effect: users in this information state are less likely to accept AI outputs passively, more likely to flag uncertainty, and more likely to run verification steps before committing to AI-suggested decisions.

The team responsible: whoever owns the UI for the AI tool — product, IT, or UX design. A practical KPI to track is the AI output review rate: what proportion of AI-generated content does a human modify or supplement before using? If this rate goes up after adding the disclosure, that's evidence the intervention is working.

### High-risk domain AI tools: medical, legal, financial

Healthcare AI assistants used by clinicians during triage or differential diagnosis. Contract review AI used by legal teams. Financial data validation AI. These are the contexts where AI mistakes have the most direct consequences.

The argument from this research: the behavioral safety return on disclosing AI fallibility may be at least as large as the return on improving model accuracy — and the disclosure cost is near zero, while accuracy improvements require significant engineering and evaluation cycles.

This doesn't mean accuracy doesn't matter. It means that disclosure policy and model development are independent interventions, both of which affect safety outcomes.

### Standardize a fallibility section in AI onboarding materials

Employees who are new to an AI tool are in the highest-trust period. Onboarding is the natural moment to establish calibrated trust before passive reliance becomes habitual.

Adding a "what this AI gets wrong, and how to verify" section to standard AI tool onboarding materials is a scalable version of this intervention. It doesn't require a training program — it requires writing a few accurate paragraphs and including them in the documentation that already exists.

This sits naturally in the L&D (learning and development) function, as a standardized module in enterprise AI tool onboarding templates.

---

## Transparency Doesn't Reduce Trust — It Sharpens It

The intuitive concern from the AI vendor side: "telling users the AI makes mistakes will reduce adoption."

The evidence from this paper points the other direction. Disclosing fallibility activates user agency and increases active engagement. Passive over-reliance leads to disappointment when errors surface. Calibrated trust — where users understand both what the AI can do and where it needs checking — leads to sustained, productive use.

"This AI is powerful and capable" is a marketing framing. "Here's where this AI is reliable and where you should verify" is the framing that builds long-term trust.

That distinction matters for how organizations design their AI deployment communications, not just their AI systems.

That's all for today!

---

## References

1. Tomohiro Nagashima, Mirella Hladký, Vera Rief (2026). *Warning About AI Fallibility Increases Help-Seeking in an Intelligent Tutoring System*. arXiv preprint.

<p class="ai-notice"><small>* This article was written in part with AI assistance and may contain inaccuracies.</small></p>
