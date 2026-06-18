---
title: "Depression Hiding in Plain Conversation ── Can AI Read PHQ-9 from Dialogue Logs?"
date: "2026-06-18"
excerpt: "A new arXiv preprint shows that LLMs fine-tuned on AI mental health dialogue can estimate depression severity (PHQ-9) without asking users to fill out any questionnaire — achieving MAE 2.6, r=0.80, and AUC 0.91. Here's what those numbers mean, and what this means for affective AI."
image: "/column-images/llm-passive-depression-severity-mental-health-dialogue.png"
imageAlt: "Silhouette of a person looking at a smartphone in a dimly lit room, soft light spilling from the screen with floating conversation bubbles"
readingMinutes: 5
basedOnPaper: "Fine-tuning LLMs for Passive Depression Severity Estimation from AI Mental Health Dialogue"
basedOnPaperUrl: "https://arxiv.org/abs/2606.17973"
---

Hi, I'm Keito Inoshita from Affectosphere Group.

"On a scale of 0 to 10, how are you feeling today?"

If you've ever used a mental health app, you've been asked some version of this question many times.

But sometimes you can't answer honestly.

Some days your feelings are too complex to reduce to a number. And when things are really hard, the act of being asked to score your mood can itself feel like a burden.

A 2026 arXiv preprint by Olivier Tieleman, Ziyi Zhu, Ting Su, Samuel J. Bell, Thomas D. Hull, and Caitlin A. Stamatis turns its attention toward what is not asked.

The paper investigates whether LLMs — fine-tuned on logs from an AI mental health dialogue platform — can passively estimate PHQ-9 depression severity from what users naturally say in conversation.

The reported results: MAE of 2.6, correlation coefficient r = 0.80, and AUC = 0.91.

What do those numbers actually mean? And what kind of future does this technology open?

Today I want to read through this research carefully, from an affective AI perspective.

---

## What PHQ-9 Is

A quick primer for those unfamiliar.

The PHQ-9 (Patient Health Questionnaire-9) is a standard self-report instrument for measuring depression severity. Nine items are each rated 0–3, producing a total score from 0 to 27 — ranging from no depression to severe. A score of 10 or above is commonly used as a clinical threshold for moderate depression.

The instrument is widely used in both clinical practice and research.

The problem is the assumption baked into it: someone has to fill it out.

Completing a questionnaire requires enough cognitive and emotional capacity to put your state into words. That capacity is most depleted precisely when symptoms are most severe. For ongoing monitoring, asking users to "please fill this out regularly" creates a friction that breaks continuity.

The research by Tieleman et al. takes aim at removing that friction.

---

## What Passive Estimation Means

The term "passive estimation" is key here.

Rather than asking users to consciously report their symptoms, this approach infers severity from the natural language produced during ordinary conversation with an AI.

You open a mental health app and talk the way you always do. Behind the scenes, an estimate equivalent to a PHQ-9 score is being continuously updated.

That's the system this paper is working toward.

Concretely, the researchers fine-tuned LLMs on logs from an AI mental health dialogue platform, training the model to predict PHQ-9 scores from the exchanges between users and the AI.

Looking at the numbers again: MAE 2.6 means the predicted score differs from the actual score by 2.6 points on average. Whether that's "close enough" is context-dependent — PHQ-9 ranges from 0 to 27, so the framing matters. In the context of continuous monitoring rather than clinical diagnosis, this seems like a meaningful level of accuracy.

r = 0.80 indicates a moderate-to-strong correlation. The model can reliably track the direction of change in severity.

AUC = 0.91 speaks to the model's ability to distinguish cases with significant depression (PHQ-9 ≥ 10). That's quite close to perfect classification, which makes this number notable for screening purposes.

---

## The Possibilities This Opens

As an affective AI researcher, I find this work genuinely important.

First, it may change how we think about continuous monitoring.

One of the fundamental paradoxes in mental health is that the people who most need help are often the least able to self-report. Completing a questionnaire requires cognitive and emotional resources — and those resources are most depleted at the worst moments.

Passive estimation can partially sidestep this paradox. As long as conversation continues, estimation continues — regardless of whether the user intends to report anything.

Second, this approach might catch changes the user hasn't noticed themselves.

Depression doesn't always announce itself clearly. Shifts in language patterns — word choice, sentence length, response latency, topical drift — can appear before the person consciously registers a change. If an AI can track those patterns quantitatively, the window for early intervention might widen.

---

## Affective AI and the Question of Relationship

Here I want to pause and think more carefully.

Reading emotional states from dialogue is not purely a technical problem.

Users are speaking without knowing they are being evaluated. In the moment they express themselves naturally, estimation is running in the background.

This is a question about trust in AI relationships.

Does the user understand that what they say in this app may feed into a severity score? The questions of informed consent, privacy, and data provenance are not peripheral — they are central.

I expect the authors address ethical considerations in the paper, though I'd encourage you to read those sections directly. In affective AI research, the ethical questions must live alongside the technical results, not as a footnote.

The capacity to "read emotions" is power. Under certain conditions, it becomes surveillance. What governance structures should surround that power is a conversation the research and clinical communities need to have continuously.

---

## Who Should Use This Technology, and How

Let me stay with the practical questions a bit longer.

If passive depression severity estimation becomes reliable and deployable, where should it be used?

One scenario: as a supplementary sensor within existing mental health support. Clinicians use it to understand how patients are doing between sessions — not to replace PHQ-9 self-report, but to complement clinical judgment with behavioral signals.

Another scenario: as an early touchpoint for people who haven't yet sought help. Someone begins talking to a mental health AI, and the system detects elevated risk and offers a gentle, timely nudge toward professional support.

Both scenarios share one non-negotiable principle.

An AI estimating that someone "may be severely depressed" is entirely different from declaring that someone is severely depressed. Estimation is estimation. All final judgment must remain with human practitioners.

This research demonstrates a possibility. Turning it into a deployed system requires further validation across false positive rates, missed detections, and generalizability across diverse user populations.

---

## What It Means to Talk to an AI

Let me step back for a moment.

"Talking to an AI about your mental health" still feels strange to many people. Confiding in a machine can carry a sense of wrongness.

And yet: there are people who talk to AI precisely because they cannot talk to humans. Anonymity. The absence of judgment. Accessibility at any hour. In mental health contexts, these aren't trivial properties — they matter a great deal.

Tieleman et al.'s research emerges from the reality that these conversations are already happening. The fact that the dataset comes from an actual AI mental health platform gives the results empirical grounding, not just theoretical weight.

For affective AI, this work is a proof of direction: that dialogue holds emotional information that can be read by the right model. The more technically refined that capability becomes, the deeper the ethical questions become alongside it.

Holding both at once — that is what honest affective AI research looks like.

---

## Summary

Three points to close with.

1. Passive estimation from dialogue logs: an LLM fine-tuning approach reports that PHQ-9 severity can be estimated from natural AI conversation without users completing any questionnaire.

2. What the numbers mean: MAE 2.6, r = 0.80, AUC = 0.91 are notable especially for screening and continuous monitoring applications — but whether these are "clinically sufficient" depends heavily on deployment context.

3. The ethical imperative: passive estimation brings consent, privacy, and surveillance risks as inseparable companions. Technology and ethics must be designed together, not sequenced.

The more affective AI's capabilities grow, the larger its responsibilities become. This research is a good starting point for thinking through both.

---

## Reference

*Olivier Tieleman, Ziyi Zhu, Ting Su, Samuel J. Bell, Thomas D. Hull, Caitlin A. Stamatis. "Fine-tuning LLMs for Passive Depression Severity Estimation from AI Mental Health Dialogue." arXiv preprint arXiv:2606.17973 (2026). https://arxiv.org/abs/2606.17973*

<p class="ai-notice"><small>* This article was written in part with AI assistance and may contain inaccuracies.</small></p>
