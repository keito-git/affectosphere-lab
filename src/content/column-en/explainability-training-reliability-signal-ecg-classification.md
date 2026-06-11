---
title: "Using Explainability as a Quality Filter During Training ── The ERTS Flip in ECG AI"
date: "2026-06-12"
excerpt: "Explainability doesn't have to be a post-hoc regulatory checkbox. ERTS uses Grad-CAM focus scores as a training-time reliability filter — dynamically excluding low-quality samples — and achieves lower training cost and higher accuracy at the same time. Here's what that means for medical device developers and regulatory teams."
image: "/column-images/explainability-training-reliability-signal-ecg-classification.png"
imageAlt: "Flat illustration of ECG waveforms in the background with an AI heatmap overlay highlighting diagnostic regions"
readingMinutes: 5
basedOnPaper: "Using Explainability as a Training-Time Reliability Signal for Efficient ECG Classification"
basedOnPaperUrl: "https://arxiv.org/abs/2606.12252"
---

Hi, I'm Keito Inoshita from Affectosphere Group.

If you work on medical AI development, you've probably run into this wall more than once.

"The model's accuracy looks good, but we can't tell what it's actually focusing on."

"Regulators are asking for explainability documentation, but retrofitting that onto a trained model is painful."

"There's too much noise in the data — the model might be learning the wrong features."

For a long time, improving accuracy and making predictions explainable were treated as separate phases. Build the model, then run XAI tools on top to visualize decisions, then fix problems if they show up. That's been the standard flow.

A 2026 arXiv preprint (Veerendhra Kumar Dangeti, Xiao Gu, Ying Weng, Shreyank N Gowda, arXiv:2606.12252) reverses this sequence. Instead of generating explanations after training, ERTS uses an explainability tool as a quality filter during training itself — and shows that this simultaneously reduces training cost and improves classification accuracy.

Today I'll break down the research for medical device development teams, regulatory affairs staff, and AI quality assurance leads.

---

## 3 Points for Today

1. Value: Using Grad-CAM focus scores as a training-time quality metric allows noisy samples to be automatically excluded, improving both efficiency and accuracy at once.
2. How ERTS works: why removing "low-explainability samples" actually improves training quality.
3. Business applications: concrete use cases for wearable manufacturers, regulatory submissions, and hospital ECG monitoring systems.

---

## ① The Conceptual Flip — Using Explainability During Training

Let me start with a quick explanation of Grad-CAM.

Grad-CAM (Gradient-weighted Class Activation Mapping) is a technique that visualizes which parts of an input an AI model focused on when making a prediction. For ECG classification, it can show something like: "this model identified atrial fibrillation by focusing on the morphology of the QRS complex" — displayed as a heatmap over the waveform. It's typically used as a post-hoc interpretability tool: train first, then explain.

ERTS (Explainability-based Reliability Training Signal) uses Grad-CAM for a completely different purpose. During training, it evaluates each sample by asking: "is the model currently attending to diagnostically relevant regions?" Samples with low focus scores — where the model is looking at noise, artifacts, or irrelevant areas — are excluded from the training batch.

The core idea is disarmingly simple.

"If the model is learning from samples where it's paying attention to the wrong regions, it will learn the wrong features. So don't train on those samples."

Traditional training assumes that if a sample is correctly annotated, it should be used. ERTS breaks that assumption. Even with a correct label, a sample with a low Grad-CAM focus score is flagged as unreliable and dynamically excluded.

---

## ② How ERTS Works — What Is a Focus Score?

ERTS operates in three steps.

### Step 1: Compute Grad-CAM Focus Scores

For each training sample, Grad-CAM heatmaps are computed. For ECG data, this quantifies how much the model's attention concentrates on diagnostically meaningful waveform components — P waves, QRS complexes, T waves — versus irrelevant regions. The resulting number is the focus score.

High score = the model is attending to diagnostically important regions.
Low score = the model is attending to noise, motion artifacts, poor electrode contact, or other irrelevant signal.

### Step 2: Dynamic Sample Exclusion

At each epoch, focus scores are computed and samples falling below a threshold are excluded from training. The "dynamic" aspect matters: as training progresses, scores shift, and the set of excluded samples updates accordingly. A sample that passes the filter early in training may be excluded later.

### Step 3: Simultaneous Cost Reduction and Accuracy Gain

Excluded samples aren't processed, which reduces computation. At the same time, not training on noisy samples makes it easier for the model to learn correct features, improving accuracy.

The paper reports experiments on public ECG datasets (including PhysioNet) demonstrating both reduced training cost and improved classification accuracy simultaneously. The counterintuitive result — "using less data improved performance" — is explained mechanistically by the filtering logic, which is what makes this research worth paying attention to.

---

## ③ Business Applications by Use Case

Here's where this becomes directly relevant to practitioners.

### Use Case 1: Smartwatch Atrial Fibrillation Detection AI (Wearable Manufacturers)

ECG signals captured by smartwatch optical or electrical sensors are inherently noisy — motion artifacts, poor skin contact, electromagnetic interference. Signal quality is fundamentally different from hospital-grade 12-lead ECG.

Applying ERTS to wearable AI training automatically filters out noise-dominated samples. Signals corrupted by motion during exercise, sweat-induced electrode drift, or handling artifacts don't need to be explicitly labeled as bad data — low focus scores handle the exclusion automatically.

Teams: AI development, wearable algorithm engineering.
KPIs: reduction in atrial fibrillation false-positive rates, accuracy stability under noisy real-world conditions.

### Use Case 2: FDA and CE Mark Regulatory Submissions (Regulatory Affairs)

FDA's AI/ML guidance and the EU AI Act effectively require explainability for medical AI. Many organizations respond by generating post-hoc explanations after the model is built — which tends to invite scrutiny in audits because the explanation is disconnected from the training process.

With ERTS, explainability is embedded in the training pipeline from the start. "Our model was trained using diagnostically meaningful attention as a quality criterion" is a fundamentally different regulatory posture from "we applied an explainability tool to a pre-trained model." The former is a design property; the latter is documentation.

This framing gives regulatory submissions a stronger basis. As FDA and EU AI Act guidance matures, the distinction between explainability as a design property versus as a documentation exercise will likely affect approval timelines and audit outcomes.

Teams: regulatory affairs, quality assurance.
KPIs: reduction in response cost to regulatory explainability queries, improvement in submission approval rates.

### Use Case 3: In-Hospital ECG Monitoring Systems (Medical Device Manufacturers)

Hospital ECG monitoring AI increasingly involves continual learning — periodic retraining as patient data accumulates. In these pipelines, incoming data quality is a persistent problem.

Integrating ERTS into a continual learning pipeline means that low-quality samples don't accumulate and degrade model performance over time. Device-to-device variation, patient population shifts, and sensor characteristic differences that cause distribution drift are partially handled by the focus-score filter — the model continues to prioritize diagnostically coherent signal.

Teams: medical device software engineering, MLOps.
KPIs: reduction in post-update model performance degradation, automation rate of data quality management.

---

## When Explainability Requirements Become Competitive Advantage

Explainability has mostly been framed as a regulatory burden: something you have to demonstrate after building the model. ERTS suggests the framing can be inverted.

When explainability is embedded in the training process, it becomes a mechanism for improving accuracy — not a cost center. The model gets better because it's being trained on higher-quality signal, and the explainability comes naturally because it was built in from the start.

In regulatory terms, "a model trained with diagnostically meaningful attention as a design criterion" is a categorically different product from "a model with XAI documentation attached." As AI Act enforcement develops and FDA guidance becomes more prescriptive, this distinction will increasingly separate fast-tracking submissions from protracted review cycles.

Medical device AI teams that treat explainability as a first-class design property — rather than a compliance checkbox — may find that it becomes a durable competitive advantage. This research offers one concrete technical path toward that outcome.

That's all for today!

---

## References

1. Veerendhra Kumar Dangeti, Xiao Gu, Ying Weng, Shreyank N Gowda (2026). *Using Explainability as a Training-Time Reliability Signal for Efficient ECG Classification*. arXiv:2606.12252.

<p class="ai-notice"><small>* This article was written in part with AI assistance and may contain inaccuracies.</small></p>
