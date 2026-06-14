---
title: "The Era of Emotion-Driven Image Generation Is Here ── How valence × arousal Makes Ads 'Yours'"
date: "2026-06-15"
excerpt: "What if the visual you see changes based on how you feel right now? EPIG — a training-free framework — is making emotion-driven personalised image generation a reality for advertising, UX, and creative tools."
image: "/column-images/epig-emotion-prompting-personalised-image-generation.png"
imageAlt: "Abstract visual of a 2D emotion map (valence × arousal) with images of different moods arranged across the grid"
readingMinutes: 5
basedOnPaper: "EPIG: Emotion-Based Prompting for Personalised Image Generation"
basedOnPaperUrl: "https://arxiv.org/abs/2606.13247"
---

Hi, I'm Keito Inoshita from Affectosphere Group.

Image generation AI is evolving at an incredible pace. But so far, the basic interaction model has stayed the same: you enter a prompt, and an image comes out. The output depends on the words you typed — not on how you feel right now.

A paper published on arXiv by Emna Othmen, Mohamed Yassine Landolsi, and Lotfi Ben Romdhane proposes a framework called EPIG that flips this premise.

EPIG captures a user's emotional state in two dimensions — valence and arousal — converts that into a prompt, and generates an image tuned to that emotional state. No additional training required. It runs on top of existing image generation models as-is.

Today I want to unpack what makes this interesting and what it means for advertising, UX, and the creative industry.

---

## 3 Points for Today

1. Value: EPIG converts emotional states into prompts, enabling personalised image generation without any model retraining.
2. Results: Arousal prediction error reduced by 12–14%. Emotional accuracy improves in measurable, concrete terms.
3. Implications: If you can auto-generate "the visual that fits how you feel right now," the way dynamic banners and personalised ads work changes fundamentally.

---

## ① What Are Valence and Arousal?

In emotion research, a two-dimensional model for representing emotional states is widely used.

The horizontal axis is valence — positive versus negative, pleasant versus unpleasant.
The vertical axis is arousal — activated versus calm, energised versus relaxed.

So "excitement and joy" sits high valence, high arousal.
"Relaxation" is high valence, low arousal.
"Anger" is low valence, high arousal.
"Sadness and depression" is low valence, low arousal.

This two-axis combination is thought to cover human emotional states with reasonable comprehensiveness.

EPIG uses this 2D model as the input to image generation. From "the emotional coordinate where you are right now," it builds a prompt and outputs an image.

That sounds straightforward — but it's actually a significant conceptual shift.

---

## ② How EPIG Works ── "Translating" Emotion into Prompts

The core of EPIG is an idea called structured prompt expansion.

When it receives an emotional state (the valence and arousal values), it applies rules to translate that state into a description of what the image should look like.

For instance, high arousal tends to select for high colour saturation, strong contrast, and dynamic composition. High valence (positive) tends to select for bright tones, natural light, and open spaces. Something like that.

This translation requires no additional training. You simply pass emotionally-informed prompts to existing image generation models — diffusion models like Stable Diffusion, for example — and it works.

In experiments, this approach reportedly reduced arousal error by 12–14%. The precision of generating images that match an emotional state improved in concrete numerical terms.

---

## ③ What This Means for Advertising, UX, and Creatives

This is where it gets interesting from a business perspective.

### Emotion-Driven Dynamic Banner Ads

Digital advertising today achieves remarkably granular targeting. But the visual of the banner itself is essentially static.

With EPIG's approach, you could potentially use estimated emotional states — from wearable devices or behavioural logs — to serve the same product with a visual tuned to "how the user feels right now."

Someone in an excited state sees a vivid, dynamic banner. Someone in a relaxed state sees a calm, low-key version. Same product, different emotional context.

My intuition is that the effect on conversion rates could be substantial.

### Personalised UI ── Interfaces That Shift With Your Mood

E-commerce sites and media apps don't yet change their visual tone based on how a user is feeling. But technically, a pipeline of emotion estimation + EPIG makes this achievable.

A morning news app that softens its image tones based on your current stress level. A music app whose suggestion visuals sync to your mood right now. This kind of experience design is becoming plausible.

### Creative Support ── Eliminating the "Translate Your Vibe Into Prompt" Burden

This is interesting for creators too.

"Something like this feeling." "A bit more calm." Turning that vague sense into a precise prompt that produces the right image is actually non-trivial work if you're not practiced at it.

If you can just specify "roughly this area of the emotional map," the overhead of prompt design could drop significantly. Image generation with emotion as the interface — that's the direction here.

---

## "Training-Free" Is the Most Important Feature

Among EPIG's characteristics, I think the most practically significant is that no additional training on existing models is required.

Fine-tuning image generation models is computationally expensive. And every time a base model updates, you need to retrain. EPIG converts emotional information into the prompt space, achieving emotion-responsiveness without touching the model weights. When the model changes, the prompt translation logic still works.

From a product development and maintenance cost perspective, this is a realistic, usable option.

---

## Emotion Is Now a Dimension in Image Generation

A broader thought to close with.

Until now, image generation's primary input axes have been what to depict (content) and how to depict it (style).

EPIG adds a third axis: who is viewing, and in what emotional state (emotional context).

When this becomes normal, my sense is that the experience of visual content will shift from "something static" to "something that responds to how I feel at this moment."

Advertising, UI design, creative production — I'll keep tracking how this change gets applied across these fields.

That's all for today!

---

## References

1. Emna Othmen, Mohamed Yassine Landolsi, Lotfi Ben Romdhane (2026). *EPIG: Emotion-Based Prompting for Personalised Image Generation*. arXiv preprint.

<p class="ai-notice"><small>* This article was written in part with AI assistance and may contain inaccuracies.</small></p>
