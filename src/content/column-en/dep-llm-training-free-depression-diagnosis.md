---
title: "Can LLMs Detect Depression Without Any Training? What Dep-LLM Means for Mental Health Screening"
date: "2026-06-11"
excerpt: "Clinics and occupational health teams have long faced the same three-way squeeze: risk of missed cases, shortage of resources, and high AI deployment costs. A training-free LLM framework called Dep-LLM is starting to answer all three at once."
image: "/column-images/dep-llm-training-free-depression-diagnosis.png"
imageAlt: "An overhead illustration of a clinical interview, with evidence text extracted from conversation bubbles flowing into an LLM that outputs a diagnostic score"
readingMinutes: 5
basedOnPaper: "Dep-LLM: Training-Free Depression Diagnosis via Evidence-Guided Structured Multi-factor with Reliable LLM Reasoning"
basedOnPaperUrl: "https://arxiv.org/abs/2606.10796"
---

Hi, I'm Keito Inoshita from Affectosphere Group.

Talk to occupational physicians long enough and the same frustrations come up.

"Patient questionnaires only go so far. But we don't have the resources to do long interviews with everyone."

"I don't want to miss depression signals. But relying too much on individual judgment creates inconsistency."

"We'd like to try an AI tool, but we don't have the capacity or budget to train it on our own data."

Mental health screening has long been caught in exactly this three-way bind — risk of missed cases, resource constraints, and high deployment costs. The "you need your own training data" problem has been a persistent barrier to medical AI adoption.

A paper published on arXiv (Yiqing Lyu, Xianbing Zhao, Buzhou Tang, Ronghuan Jiang, arXiv:2606.10796) takes this problem head-on. The Dep-LLM framework detects depression indicators from long clinical interview transcripts — without any fine-tuning or domain-specific training.

Today I'll break this down for occupational physicians, EAP providers, healthcare IT vendors, and insurance companies.

---

## 3 Points for Today

1. Why Dep-LLM works without training: how structured prompting beats fine-tuning.
2. Three modules: how Chain-of-Thought, reliability scoring, and multi-factor prediction divide the work.
3. Business applications: how to pilot this in occupational health, EAP, and insurance settings.

---

## ① Why "Zero Additional Training" Works

Let me start with the framing.

The conventional wisdom in medical AI is "you need a domain-specific model." Clinical language in psychiatry is nuanced, so general-purpose LLMs need fine-tuning to work. That's been the standard argument.

Dep-LLM takes a different stance.

"LLMs already have enough language understanding. The problem is we haven't been giving them the right questions and evidence in the right structure."

That's the core idea. The reason fine-tuning has seemed necessary, in many cases, comes down to a structural gap between raw LLM capability and how the problem was being framed. Dep-LLM addresses that gap directly.

---

## ② How the Three Modules Work

Dep-LLM is built around three components.

### Chain-of-Thought Evidence Extraction Module

This module extracts depression-relevant utterances and behavioral patterns from long clinical interviews as structured "evidence."

The kinds of signals it pulls: "I haven't felt motivated to do anything lately," "my sleep has been disrupted," "things I used to enjoy don't feel enjoyable anymore." These are lifted from across the full interview and organized.

Chain-of-Thought (CoT) prompting asks the LLM to reason through why something is evidence — not just flag it as suspicious, but explain step by step why it signals depression. This improves both accuracy and interpretability.

Think of it as giving the AI the same requirement we'd give a human clinician: don't just notice a concerning statement, explain why it's concerning.

### Reliability Analysis Module

This module scores the confidence level of each piece of extracted evidence.

Depression language is often ambiguous. "I'm tired" could be physical fatigue or depressive exhaustion. This module quantifies that ambiguity and weights higher-confidence evidence more heavily in the final prediction.

Treating all utterances as equal actually hurts performance. Distinguishing which evidence is more reliable is a meaningful part of what makes this framework work.

### Multi-Factor Coordination Prediction Module

This module evaluates multiple diagnostic factors — corresponding to DSM-style criteria — independently, then integrates them.

Depression indicators like sleep disturbance, loss of interest, fatigue, and difficulty concentrating are assessed separately, then combined into a final diagnostic score. Looking at the combination pattern across multiple factors is more stable than relying on any single one. If a patient doesn't respond to a particular question, other factors can compensate.

---

## ③ How to Read the Results

The paper runs experiments on two clinical depression audio datasets: DAIC-WOZ and E-DAIC.

Dep-LLM is compared against 21 baseline models — including fine-tuned depression-specific LLMs, commercial LLMs, and conventional ML — across 9 evaluation metrics. The reported result is that Dep-LLM outperforms all of them.

The critical point is that this is achieved with zero additional training. Most of the comparison models were specifically trained on depression data. Holding your own against fine-tuned specialists in a zero-shot setting speaks to the quality of the framework design.

That said, these are research dataset results. In real clinical environments, language, culture, individual variation, and audio quality all add complexity. The practical framing should be "screening support tool for clinicians," not "automated diagnosis system."

---

## How to Pilot This in Practice

Here's what this could look like in three concrete settings.

### Occupational Health and Mental Health Interviews

Current state: annual check-ups plus self-reported stress questionnaires. High risk of missing early signals.

Application: transcribe interview audio and run Dep-LLM to generate evidence and confidence scores. Use the output as a checklist for occupational physicians to catch statements they might otherwise overlook. Not AI diagnosis — AI-assisted oversight.

KPIs: early detection rate for high-risk individuals, increase in post-interview follow-up actions.

### EAP (Employee Assistance Program) Providers

Current state: initial counseling triage takes time, and consistency varies between counselors.

Application: process first-session online call transcripts with Dep-LLM to standardize initial triage. Use scores as reference to reduce inter-counselor variability in early assessment.

KPIs: triage accuracy improvement, reduction in judgment variance between counselors.

### Life and Health Insurance Companies

Current state: periodic health checks focus on physical indicators. Mental health is captured only through self-reported questionnaires.

Application: analyze health check phone calls or chat logs with Dep-LLM to generate proactive intervention flags for high-risk policyholders. Intervening before escalation can reduce treatment costs, absence costs, and policy cancellations.

KPIs: early intervention rate for high-risk individuals, reduction in escalation to severe cases.

---

## What Makes This Significant Going Forward

The value of Dep-LLM running without fine-tuning isn't just low deployment cost.

"No retraining required when the base LLM is updated" is a real operational advantage. When the underlying foundation model improves, the Dep-LLM framework carries over without rebuilding. That's an architectural answer to the ongoing maintenance cost problem in medical AI.

Depression screening AI has been splitting into two directions: fully autonomous diagnosis, and physician-support tools used in an assistive role. Given the regulatory and risk management landscape, the latter is the more practical path for now. Dep-LLM is well-suited to that direction.

How far can AI help us stop missing depression cases? The answers are taking shape.

See you next time!

---

## Reference

1. Yiqing Lyu, Xianbing Zhao, Buzhou Tang, Ronghuan Jiang (2025). *Dep-LLM: Training-Free Depression Diagnosis via Evidence-Guided Structured Multi-factor with Reliable LLM Reasoning*. arXiv preprint.

<p class="ai-notice"><small>* This article was written in part with AI assistance and may contain inaccuracies.</small></p>
