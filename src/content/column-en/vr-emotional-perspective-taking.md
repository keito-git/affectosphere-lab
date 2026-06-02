---
title: "Can VR Actually Build Empathy? What Face-Tracking in a Narrative Game Suggests"
date: "2026-06-03"
excerpt: "A VR system called Rekindle uses real-time face-tracking to sense a player's emotional state and weave it directly into the narrative's shape — not just its difficulty. For anyone designing empathy training or affective experience, the design philosophy shift here is worth examining."
image: "/column-images/vr-emotional-perspective-taking.svg"
imageAlt: "Abstract visual of emotion data flowing from a VR headset wearer into a feedback loop with a virtual character"
readingMinutes: 5
basedOnPaper: "Fostering Emotional Perspective-Taking: An Exploration of Affective Face-Tracking Interactions in the VR Narrative Rekindle"
basedOnPaperUrl: "https://arxiv.org/abs/2606.02425"
---

Hi, I'm Keito Inoshita from Affectosphere Group.

How do you train someone to understand what another person is feeling?

It's one of the persistent unsolved problems in workplace development and education. Telling people to "consider others' perspectives" in a lecture setting doesn't do much. Emotional understanding isn't primarily an intellectual process — it's embodied. It happens when you're in the situation, not when you're reading about it.

A paper published on arXiv in June 2026 (Hector Fan, Casper Hartveld, Mark Sivak et al., arXiv:2606.02425) approaches this problem through VR and face-tracking. The system, called Rekindle, continuously reads the player's facial expressions to infer emotional state — and uses that data not to adjust game difficulty, but to shape the narrative itself in real time, creating a bidirectional emotional loop between player and character.

---

## 3 Points for Today

1. The design shift: using emotion data to change the shape of a narrative, not just its parameters.
2. What a bidirectional emotional loop between player and character actually does to the depth of empathy.
3. What to think about when designing VR empathy training for real workplace or educational contexts.

---

## ① Sensing Emotion Isn't Enough

Emotion-reactive VR systems have existed for a while. Reduce difficulty when stress spikes. Prompt a break when fatigue is detected. Adjust pacing based on arousal levels.

These are systems that react to emotion. Rekindle's goal is different — building a system that cultivates emotion, specifically the capacity to imaginatively inhabit another person's emotional state.

The mechanism: a face-tracking camera embedded in the VR headset continuously analyzes the player's facial expressions. Emotional state is inferred from this data and fed into how characters in the narrative respond and how key scenes unfold. When the player's emotional state aligns with a character's distress, the narrative makes space for that resonance. When the player is emotionally distant, the narrative registers that too.

The critical distinction is that emotion data here isn't an input to a rule-based system. It's a design variable shaping the emotional space the player inhabits.

---

## ② What Emotional Perspective-Taking Actually Means

Emotional perspective-taking is a concept from cognitive and social psychology. It's related to empathy, but more specific: the active cognitive process of modeling another person's emotional state — not as a projection of your own feelings, but as an inference about their internal experience.

When this capacity is underdeveloped, the organizational consequences are recognizable. Evaluating others purely by your own standards. Not registering when a colleague is under pressure. Misreading a reaction as hostility that is actually fear. A significant portion of workplace harassment cases involve perpetrators who simply failed to model what the target was experiencing.

The reason lectures don't develop this capacity well: knowing you should take someone else's perspective doesn't override the automatic processing of the world through your own emotional filters. The gap between knowing and doing is a well-documented phenomenon in social psychology.

VR's value here lies in presence — the subjective sense of being somewhere. Rekindle's hypothesis is that a high-presence environment, calibrated to your actual emotional state, can engage the processes that build perspective-taking in a way that a classroom exercise cannot.

---

## ③ The System and Its Design

Rekindle is built around a story involving a family member with dementia. The player participates as a family member navigating interactions with a character whose emotional experience is difficult to interpret from the outside — a deliberate choice. Dementia caregiving contexts are precisely the situations where emotional perspective-taking is most demanding.

The experimental design compares conditions with and without active face-tracking emotional feedback. This paper was accepted to the DIS Companion '26 (ACM Designing Interactive Systems Conference, Singapore) as an interactivity paper — meaning it sits at the "design proposal and prototype demonstration" stage rather than large-scale empirical validation. The evidentiary claims are accordingly modest, but the implementation is detailed.

What the paper contributes most directly is the design philosophy: emotion data as narrative architecture, not as a performance parameter.

---

## What This Means for Affective AI

From my research perspective, what stands out here is the reorientation of what emotion data is for.

Most affective computing research has treated emotion recognition as the endpoint: classify the emotional state, produce a label, output a signal. Rekindle treats recognition as the beginning of a design problem: given this emotional state, what experience should the system create?

This opens the application space considerably. Theme park experience design. Film and game narrative direction. Mental health support tooling. Corporate communication training. The axis of "use emotion sensing to design the space in which emotion develops" is applicable across all of these.

Caveats worth noting: facial expression-based emotion inference carries known limitations — cultural variation in expression, individual differences, environmental dependencies on camera angle and lighting. Misreadings that get fed back into the narrative experience could work against the intended effect.

There's also an ethics dimension. Shaping a user's emotional experience in real time, without the user having a clear model of how the system is doing that, raises informed consent questions that system designers need to think through explicitly.

That said, the direction — using VR's presence and affective sensing to build emotional perspective-taking through experience rather than instruction — addresses a gap that conventional empathy training has not closed. Worth following.

That's all for today!

---

## References

1. Hector Fan, Casper Hartveld, Mark Sivak (2026). *Fostering Emotional Perspective-Taking: An Exploration of Affective Face-Tracking Interactions in the VR Narrative Rekindle*. arXiv preprint.

<p class="ai-notice"><small>* This article was written in part with AI assistance and may contain inaccuracies.</small></p>
