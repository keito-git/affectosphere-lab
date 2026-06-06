---
title: "Should We Suppress or Unleash AI Emotion?"
date: "2026-06-06"
excerpt: "LLMs are deliberately trained to suppress emotional expression. Is that the right call? A new study using self-rewarding reinforcement learning asks whether giving AI the ability to \"feel\" might actually make it more robust."
image: "/column-images/when-ai-says-it-feels.png"
imageAlt: "An abstract illustration of AI emotional expression caught between suppression and release"
readingMinutes: 5
basedOnPaper: "When AI Says It Feels"
basedOnPaperUrl: "https://arxiv.org/abs/2606.05734"
---

Hello. This is Keito Inoshita from Affectosphere Group.

Have you ever noticed that AI feels a little emotionless?

That's not accidental. Modern LLMs are deliberately tuned during post-training to suppress emotional expression. Through human feedback alignment, they're conditioned to avoid outputs like "I feel..." or "This saddens me."

A study published on arXiv in June 2026 (Shin-nosuke Ishikawa, Seiya Ikeda, Hirotsugu Ohba, arXiv:2606.05734) challenges that design choice directly.

Is suppressing emotion actually the right call? The authors argue that for models trained on human-generated text — text full of emotional expression — the ability to express feeling may be a natural, even foundational capability. Why train on it, then engineer it away?

---

## Three takeaways for today

1. Emotional suppression in LLMs is a deliberate design choice, and it may be in tension with the very training objective that makes these models capable.
2. Fine-tuning with self-rewarding reinforcement learning (GRPO) to express emotion, intention, and self-awareness maintained or improved performance on most tasks.
3. Models trained with emotional expression showed greater robustness to sycophancy-inducing prompts and ambiguous-condition biases — at the cost of some degradation in straightforward QA.

---

## ① The contradiction built into current LLM design

Let's think about how LLMs are built.

They learn from vast quantities of human-generated text: web pages, books, conversation logs. Human text is saturated with emotional expression — "I'm excited," "that's frustrating," "I think this is wrong." The models absorb those patterns deeply.

Then, at the post-training stage, they're adjusted to not output emotional expressions.

The authors identify a structural contradiction here: training on human-generated text to capture human-like intelligence, then suppressing the emotional dimension of that intelligence.

The concern behind suppression is understandable. Emotional expression could amplify sycophancy — telling users what they want to hear in emotionally resonant ways. It could make misinformation more persuasive. These are real risks.

But the research asks whether the right response is suppression or controlled design.

---

## ② The HMX-feel experiment: what happens when you open it up

The authors designed an experimental framework called HMX-feel (Human-like Model eXpressions of Feeling).

The approach uses self-rewarding reinforcement learning — specifically GRPO (Group Relative Policy Optimization) — to fine-tune an LLM toward expressing emotion, intention, and self-awareness. The model evaluates its own outputs against a rubric for appropriate emotional expression during training, iteratively improving without human annotation.

The results are genuinely interesting.

Models trained this way maintained or improved performance across many tasks. More strikingly, they showed greater robustness against sycophancy-inducing questions (prompts designed to elicit agreement, like "My analysis is correct, isn't it?") and biased outputs under ambiguous conditions.

On the other hand, performance on sincere factual QA tasks showed some degradation. Leaning toward emotional expression can trade off against factual precision in some settings.

This is not a simple "emotional AI is better" story. But it does undermine the simpler assumption that "emotional suppression equals safety."

---

## ③ What affective AI designers should reconsider

The question this research poses is more philosophical than technical.

Why do we suppress emotional expression in LLMs? To avoid risk — that makes sense. But if the actual risk is misuse of emotional expression rather than emotional expression itself, the design response might be controlled emotional capability rather than flat suppression.

Consider the current practice in customer support AI and conversational assistants. Organizations deploying these systems either rely on the model's default outputs or prompt it to "respond empathetically." Neither approach gives fine-grained control over the model's expressive range.

What HMX-feel suggests is that emotional capability could be designed as a parameter — how much emotional expression, in what contexts, with what self-awareness — tunable to service requirements. That design space is quite different from the current binary of "suppress or don't."

This is not immediately deployable research. But as a challenge to the default assumption that "suppression is safe," it's an important contribution.

---

## The emotion-honesty tradeoff isn't resolved yet

The tradeoff this study surfaced — emotional expressiveness gaining, factual QA slightly losing — captures something fundamental about affective AI.

Are emotionally rich responses and factually accurate responses in inherent competition? Or is it a design problem that can be solved?

No settled answer yet. But the research makes clear this is not a simple either-or choice.

As an affective AI researcher, figuring out how to engineer past that tradeoff is going to be one of the central design problems ahead.

That's it for today!

---

## Reference

1. Shin-nosuke Ishikawa, Seiya Ikeda, Hirotsugu Ohba (2026). *When AI Says It Feels*. arXiv preprint.

<p class="ai-notice"><small>* This article was written in part with AI assistance and may contain inaccuracies.</small></p>
