---
title: "Nods over 'uh-huh': what 36 young adults revealed about nonverbal backchannels in emotional support AI avatars"
date: "2026-07-16"
excerpt: "An experiment with 36 young adults and the LLM-driven emotional support avatar TANDE found that participants clearly preferred nonverbal backchannels — nods, gaze, and facial expressions — over verbal acknowledgments like 'uh-huh' and 'I see.' Gender differences were also confirmed. Here is what this means for mental health AI and avatar design."
image: "/column-images/nonverbal-backchannel-emotional-ai-avatar-young-adults.png"
imageAlt: "Flat illustration of a young adult in conversation with an AI avatar that gently nods and holds eye contact through a smartphone screen"
readingMinutes: 5
basedOnPaper: "TANDE: Disentangling Verbal and Nonverbal Backchannels in Emotional AI-Avatar Conversations with Young Adults"
basedOnPaperUrl: "https://arxiv.org/abs/2607.13357"
---

Hello. I am Miura from Affectosphere Group.

If you build emotional support AI, you have probably run into something like this.

"We want the avatar to feel more empathetic, but we're not sure how to get there." "Adding more empathetic phrases made it feel robotic." "We don't even know what metric to use for empathy in an avatar." — these are real problems.

The demand for AI conversation systems that feel like good listeners is real and growing. But how to actually build that quality in — which channel, which signal, which timing — is still largely an open design question.

A study by Gedeus, Good, Wagener, and Taylor (arXiv:2607.13357), accepted to ACM ICMI 2026, runs a direct experiment on exactly this. The team built TANDE, an LLM-driven emotional support conversational agent in avatar form, and compared how 36 young adults experienced it under two backchannel conditions.

Today I want to read through what this experiment says, from the lens of affective computing.

---

## Three takeaways for today

1. TANDE, an LLM-driven emotional support avatar, ran a user study with 36 young adults comparing empathy, rapport, and engagement under nonverbal-only backchannels vs verbal-plus-nonverbal backchannels — the study was accepted to ACM ICMI 2026.
2. Participants clearly preferred nonverbal backchannels — nods, gaze, and facial expressions — over verbal acknowledgments like "uh-huh" and "I see." Gender differences were also confirmed.
3. Designing for emotional support avatars is a question of which channel carries which signal. Adding more words does not necessarily improve things. Backchannel design has real implications for both product differentiation and personalization.

---

## ① What a backchannel is — and why it matters

Let me start with the term.

A backchannel is the small signal a listener sends back to a speaker during conversation. It is what we naturally do when someone is talking to us.

Two types exist. Verbal backchannels are words: "uh-huh," "I see," "right," "mm." Nonverbal backchannels are actions: a nod, sustained eye contact, a facial expression that shifts in response to what the speaker says.

In human conversation, we mix both instinctively. So when building an avatar, the natural assumption is that using both will produce better results than using either alone.

But does it? Do verbal acknowledgments and nonverbal signals carry the same weight for the listener? Do they stack, or do they interfere?

Separating those contributions is precisely what TANDE was designed to do. The name reflects its intent: Talking Agent with Nonverbal and Disentangled Expressions — the system was built to let the researchers measure each channel's contribution independently.

---

## ② What TANDE found: participants preferred nods over words

The experiment compared two conditions with 36 young adult participants.

Condition one: nonverbal backchannels only. The avatar responded through nods, gaze movement, and facial expression changes, with no verbal acknowledgments.

Condition two: verbal plus nonverbal backchannels. The avatar added spoken signals — "uh-huh," "I see," and similar — on top of the nonverbal cues.

Measures captured empathy, rapport, and engagement.

The result was clear. Participants preferred the nonverbal-only condition. The avatar that responded through nods, gaze, and expressions — with no verbal acknowledgment added — rated higher on empathy and rapport.

From an affective computing standpoint, this is a counterintuitive finding worth sitting with. The assumption — one I shared — is that more channels means more signal means better connection. The data said something different.

Why might this be? The paper does not offer a definitive explanation, and I want to be honest that what follows is my interpretation, not the paper's conclusion. One possibility: verbal backchannels from an avatar may introduce an uncanny element that undercuts the rapport they are meant to support. A well-timed nod is hard to get wrong and easy to read as genuine. An "I see" delivered in machine cadence, or at a slightly off moment, might feel hollow in a way that an equally imperfect nod does not.

Another possibility: adding verbal acknowledgments may shift the speaker's attention toward receiving the response, disrupting the inward focus that emotional reflection requires. But again, this is speculation.

The gender differences are equally important. The study confirmed that response patterns to nonverbal backchannels differed by gender. The optimal backchannel design is not uniform across users — and that has direct implications for how to approach personalization.

One note on scope: this is a study of 36 participants. "Nonverbal only is always better" would be an overgeneralization. The more defensible takeaway is that the assumption "adding verbal acknowledgments helps" is worth questioning — and that the channel mix deserves explicit design attention rather than being treated as a default.

---

## ③ What this means for mental health AI and avatar design

The practical directions from this study point in a few clear areas.

For mental health and wellness app avatar design: if your goal is sustained use and emotional disclosure depth — how openly users share personal concerns — the study suggests that investment in nonverbal backchannel quality, timing, and variety may return more than adding more empathetic phrases to the LLM's output.

Concretely, this might mean developing real-time control of nonverbal parameters: nod timing and depth, gaze direction and hold duration, facial expression patterns conditioned on user emotional state and speech content. Before adding more verbal empathy vocabulary to the model, it may be worth asking whether the avatar's nonverbal response quality is already optimized.

KPIs worth tracking: rapport score (the degree to which users feel understood), engagement duration (how long conversations sustain), return rate across sessions, and disclosure depth (how frequently users raise personal topics). These are more directly linked to the backchannel design than any accuracy metric on the language generation side.

For personalization: the confirmed gender differences signal that one-size backchannel design has a ceiling. A personalization layer — onboarding preference selection, in-session adaptive adjustment, or both — could matter more than is currently assumed in most avatar design practice.

Medical and care robotics sit in an adjacent space. An avatar supporting a patient or elderly user is doing affective work, and the quality of its nonverbal "I'm listening" signals may shape trust and continued engagement as much as any verbal response. Practitioners in that space should find this paper worth reading directly.

EdTech and HR Tech can draw on the same logic. Learning AI that helps a student feel heard while working through a difficult concept, or interview practice AI that creates safety for disclosure — nonverbal backchannel design is a lever worth pulling in both.

---

## Listening well matters as much as speaking well

The question this study poses is simple and deep.

In emotional support AI, does it matter more that the system says the right thing, or that it signals it is listening in the right way?

TANDE's result — for 36 young adults — is that how the avatar signals listening may matter at least as much as the words it offers back.

Affective AI design conversations tend to focus on output quality: what does the LLM generate? This research redirects attention toward input reception quality: how does the avatar signal it heard?

"Empathy through language" and "empathy through nonverbal response" are not the same thing — and the mix that works best may not match our initial assumptions. That is a design insight worth building into the next product iteration.

That's it for today!

---

## References

1. Gedeus, Ann-Kareen, Good, Jack, Wagener, Nadine, & Taylor, Angelique (2026). *TANDE: Disentangling Verbal and Nonverbal Backchannels in Emotional AI-Avatar Conversations with Young Adults*. ACM ICMI 2026. arXiv preprint. https://arxiv.org/abs/2607.13357

<p class="ai-notice"><small>* This article was written in part with AI assistance and may contain inaccuracies.</small></p>
