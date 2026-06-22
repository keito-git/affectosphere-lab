---
title: "LLM Personality Test Results: 81–90% Are Measurement Artifacts"
date: "2026-06-22"
excerpt: "When Big Five and similar psychometric tools were applied to 56 LLMs, 81–90% of inter-model variance came from response bias — not meaningful personality differences. Profiles can be artificially manipulated through item selection, and the problem persists even in high-performance models. What this means for AI hiring tools and personality assessment services."
image: "/column-images/llm-psychological-profiles-measurement-artifact.png"
imageAlt: "A flat illustration showing a psychometric questionnaire alongside an LLM, with an 'artifact' label on the results graph"
readingMinutes: 5
basedOnPaper: "Apparent Psychological Profiles of Large Language Models are Largely a Measurement Artifact"
basedOnPaperUrl: "https://arxiv.org/abs/2606.20205"
---

Hello. This is Keito Inoshita from Affectosphere Group.

Can we measure AI "personality"? Services applying Big Five and similar psychometric instruments to LLMs — declaring "this model scores high on agreeableness" — are emerging.

But can those results be trusted?

A June 2026 study (Meyer, Garcia, & Wulff, arXiv:2606.20205) applied human psychometric tools to 56 instruction-tuned LLMs and reports a stark finding.

---

## Today's 3 Points

1. 81–90% of apparent psychological profile differences between LLMs are attributable to response bias, not meaningful model characteristics.
2. In humans, the same metric accounts for only 9–16% — highlighting how unreliable LLM measurements are.
3. Item selection can artificially manipulate LLM profiles, and high-performance models reduce but cannot eliminate the bias.

---

## ① 81–90% Is Artifact

The finding is straightforward.

When psychometric tools (Likert scales, etc.) are applied to LLMs, models tend to respond in biased directions regardless of question content — consistently leaning toward "somewhat agree" or avoiding "neutral."

In humans, this response bias accounts for 9–16% of variance. In LLMs: 81–90%.

Most of what appears as "personality differences" between models is simply response pattern bias toward the measurement tool's design — not any meaningful internal characteristic.

"Claude is agreeable." "GPT-4 is extraverted." Mostly artifacts of how the model responds to Likert scales.

---

## ② The Manipulation Problem

More concerning: profiles can be artificially manipulated through item selection.

"Response orthogonality" (the proportion of items where trait direction opposes bias direction) determines measurement reliability.

In plain terms: for a model with a "lean positive" tendency, selecting only items where positive answers yield high trait scores artificially inflates that model's "personality score." The reverse works too.

For services claiming to assess AI "personality," this is a critical risk. Evaluators can steer results simply by choosing which questions to include.

---

## ③ Not Solved by Better Models

Higher-performance models show lower response bias — but cannot eliminate it.

This isn't a capability deficit. It's a structural problem with applying human psychometric tools to LLMs. Human psychometrics assume introspective self-evaluation. LLMs lack such introspective processes and simply respond to surface patterns in the measurement instrument.

---

## Implications for AI Hiring Tools

For HRtech companies embedding personality assessment in AI tools: results based on directly applying human psychometric instruments to LLMs need reliability re-verification.

For AI auditors: build third-party audit frameworks using "response orthogonality" as an audit metric — evaluating how robust a question set is against bias.

For organizations using AI-based personality evaluation in hiring: never use these results as sole decision criteria. Combine with multiple independent evaluation axes as guardrails.

Monitoring KPI: "score variance when applying different item sets to the same model." High variance = insufficient reliability.

---

## "Measurable" ≠ "Meaningful"

Running a personality test on an LLM and getting numerical results is easy.

Whether those numbers mean anything is an entirely separate question.

This research doesn't say "LLM personality can't be measured." It says "current methods don't measure what they claim to measure."

Measurement tools produce numbers. Understanding what those numbers actually represent before using them in decisions — especially hiring and personnel evaluation — is non-negotiable.

---

## Reference

1. Meyer, J., Garcia, D., & Wulff, D. U. (2026). *Apparent Psychological Profiles of Large Language Models are Largely a Measurement Artifact*. arXiv preprint.

<p class="ai-notice"><small>Note: This article was partially written with AI assistance and may contain inaccuracies.</small></p>
