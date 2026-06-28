---
title: "Fixing the LLM Forecasting Blind Spot: Feature Steering Kills Lookahead Bias"
date: "2026-06-28"
excerpt: "When LLMs are used for demand forecasting or sales planning, lookahead bias — where the model implicitly references future knowledge — causes dangerously optimistic predictions. A new study uses Sparse Autoencoders to identify time-awareness features inside the LLM, then applies Activation Steering to causally correct the bias. Here's what it means for SCM and corporate planning teams."
image: "/column-images/llm-forecasting-feature-steering-generalization-time-aware.png"
imageAlt: "A flat illustration showing time-aware reasoning flowing from historical data toward future predictions with a corrective steering layer"
readingMinutes: 5
basedOnPaper: "Forecasting With LLMs: Improved Generalization Through Feature Steering"
basedOnPaperUrl: "https://arxiv.org/abs/2606.27199"
---

Hello. This is Keito Inoshita from Affectosphere Group.

When organizations try to use LLMs for demand forecasting or sales planning, one structural problem keeps surfacing: the model acts as if it already knows the future.

This is called lookahead bias. The LLM was pretrained on text that includes events from specific time periods, and when asked to forecast from past data, it silently references that future knowledge. The result is predictions that look accurate in testing but fail badly in production.

A June 2026 study (Merchant & Levy, arXiv:2606.27199) attacks this problem not through prompting, but through the model's internal representations — identifying time-awareness features with Sparse Autoencoders and then steering them with Activation Steering to causally shift the model toward historically grounded reasoning.

---

## Today's 3 Points

1. Sparse Autoencoders can distinguish "time-specific knowledge-dependent reasoning" from "generalizable pattern recognition" inside an LLM's internal representations.
2. Activation Steering on time-awareness features substantially reduces lookahead bias while maintaining general reasoning performance.
3. This approach causally shifts the model toward historically grounded inference — a deployable solution for SCM and corporate planning use cases where data leakage causes systematic over-optimism.

---

## ① The Lookahead Bias Problem

LLM-based forecasting pilots are proliferating across finance, retail, and manufacturing. But there is a structural trap.

LLMs trained on large corpora absorb knowledge about what happened at specific points in time. If the model learned about the 2022 inflation surge, and you ask it to forecast from 2021 data, it may unconsciously reference that knowledge. It appears to analyze the past, but it is effectively reasoning from the future.

Forecasts come out systematically optimistic. When deployed in real operations, the accuracy gap can be severe.

Merchant & Levy (2026) take a fundamentally different approach than prior work: instead of constraining the model with prompts, they go inside the model and correct the bias at the feature level.

---

## ② Sparse Autoencoders: Reading the Model's Internals

The first step is analyzing what features the LLM actually uses when solving forecasting tasks.

Sparse Autoencoders (SAEs) decompose the activation patterns in an LLM's intermediate layers into interpretable, sparse feature sets. This allows researchers to identify which features correspond to time-specific knowledge versus generalizable reasoning patterns.

The study applied SAEs to forecasting tasks and confirmed that "time-specific knowledge-dependent reasoning" and "generalizable pattern recognition" are distinguishable as internal representations. The former is the source of lookahead bias. The latter is what actually contributes to robust forecasting accuracy.

This finding matters because it shows that the model's "ability to reason from the past" and its "tendency to act as if it knows the future" are not inseparably entangled — they can be identified and addressed separately.

---

## ③ Activation Steering: Causally Correcting the Bias

Once the time-awareness features are identified, Activation Steering intervenes during inference.

Activation Steering amplifies or suppresses specific internal features while the model is generating its output. Rather than asking the model to "please reason only from historical data" in a prompt, Activation Steering changes the internal reasoning process itself.

In this study, amplifying the time-awareness features caused the model to more strongly account for its current temporal context when forecasting. Lookahead bias dropped substantially, and general reasoning performance was maintained.

The key distinction from prompting: prompting is a request. The model can still "cheat." Activation Steering modifies the inference process directly — it is a causal intervention.

---

## Implementation Hypotheses for SCM and Corporate Planning

Two primary use cases stand out.

The first is demand forecasting for new product launches. New products have thin historical data, so the model must reason from analogous products and market signals. Getting the temporal context exactly right — "we are at launch date, not six months after launch" — has a direct impact on accuracy. Time-awareness Activation Steering seems like a natural fit here.

The second is forecasting around external shocks: natural disasters, regulatory changes, competitor entries. These are precisely the moments when past averages break down and historical reasoning about similar events becomes critical. Ensuring the model does not misidentify its temporal context is a prerequisite for this reasoning to work correctly.

By team:
- SCM teams: integrate as a lookahead-bias removal layer in forecasting pipelines. KPI: reduction in Forecast Bias (systematic directional error).
- Corporate planning teams: deploy as an accuracy assurance layer in LLM-powered market analysis tools. KPI: gap between LLM analysis outputs and actuals.
- MLOps teams: implement as an Activation Steering layer added to the production inference pipeline.

---

## From Prompting the Outside to Fixing the Inside

Most LLM deployment work focuses on prompt engineering — crafting better instructions to steer model behavior from the outside.

This research points toward a different paradigm: identifying the internal features responsible for problematic behavior and correcting them directly.

If lookahead bias has been blocking your team from trusting LLM forecasts in production, the approach here — SAE-based feature identification combined with Activation Steering — represents a credible path toward deployment-grade reliability. This is still an arXiv preprint, and validation on real business data presumably lies ahead. But as a directional signal, it represents a meaningful step toward treating LLMs as controllable systems rather than black boxes you prompt and hope for the best.

---

## Reference

1. Merchant, H., & Levy, B. (2026). *Forecasting With LLMs: Improved Generalization Through Feature Steering*. arXiv preprint.

<p class="ai-notice"><small>* This article was written in part with AI assistance and may contain inaccuracies.</small></p>
