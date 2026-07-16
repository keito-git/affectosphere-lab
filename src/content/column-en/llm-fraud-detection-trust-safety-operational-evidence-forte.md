---
title: "What to check before deploying LLMs in fraud detection: the FORTE framework and the gap 49 papers left open"
date: "2026-07-16"
excerpt: "A review of 49 papers on LLM applications in fraud detection, content moderation, and Trust-and-Safety workflows found that zero papers simultaneously reported latency, cost, and trust calibration per decision. The FORTE framework organizes LLM operational roles into seven types and proposes a five-item pre-deployment checklist. Here is how to put it to work for your risk, compliance, or fintech team."
image: "/column-images/llm-fraud-detection-trust-safety-operational-evidence-forte.png"
imageAlt: "Flat illustration of a control room with seven instrument panels showing latency, cost, calibration, and robustness dials, a transparent checklist at the center lighting up row by row as each item is verified"
readingMinutes: 5
basedOnPaper: "Operational Evidence Gaps for LLMs in Fraud Detection and Trust-and-Safety Workflows"
basedOnPaperUrl: "https://arxiv.org/abs/2607.13078"
---

Hello. I am Miura from Affectosphere Group.

If you work in fraud risk, Trust-and-Safety, or compliance, you have probably run into something like this.

"We want to use LLMs for fraud detection, but we don't know what to evaluate." "Our PoC accuracy looked good, then production hit us with unexpected cost and latency." "We need to explain AI risk to leadership, but it gets too technical to land." — these are common blockers.

The movement toward LLMs in fraud detection and content moderation is real. But the tools for measuring whether that movement is working — and for knowing what to check before you commit to production — are not yet well established.

A paper by Keyur Gabani (arXiv:2607.13078), published on arXiv, takes aim at exactly that gap. It reviews 49 papers on LLM applications in fraud detection, content moderation, and T&S workflows, identifies a specific pattern of missing evidence, and proposes the FORTE framework as a pre-deployment evaluation structure.

Today I want to read this through from a risk management and compliance perspective.

---

## Three takeaways for today

1. A review of 49 papers on LLM use in fraud detection, content moderation, and T&S workflows found that zero papers simultaneously reported latency, cost, and trust calibration per decision — a significant operational evidence gap.
2. The FORTE framework organizes LLM operational roles into seven types (classifier, retrieval interface, explanation generator, review assistant, agent, feature extractor, escalation component) and proposes a five-item pre-deployment checklist: latency threshold, cost ceiling, calibration, explanation quality, and adversarial robustness.
3. FORTE's checklist and role taxonomy can be applied right now — as a PoC evaluation framework and as a tool for explaining scope and accountability to leadership and regulators.

---

## ① "Accuracy is reported — operations are not"

The first thing this research points out is a systematic gap in the existing literature.

Papers on LLM-based fraud detection and moderation already exist in quantity. When Gabani reviewed 49 of them, a pattern emerged. Accuracy metrics — detection rate, F1 score, AUC — are reported enthusiastically. The numbers that matter most for actual deployment are largely absent.

Specifically: latency per decision, cost per decision, and trust calibration. Zero papers reported all three simultaneously.

Calibration may need a brief explanation. In short, it refers to whether a model's confidence scores actually reflect its real-world accuracy. If a model says "90% confident," is it correct about 90% of the time? In fraud detection and moderation — where the model's confidence typically determines whether a case is auto-processed or escalated to a human reviewer — miscalibrated confidence scores cause downstream failures. If you cannot trust the confidence, you cannot set reliable escalation thresholds.

So the operational picture looks like this: practitioners who rely on the research literature to inform production deployment decisions cannot get what they need from 49 papers, because those papers did not measure what operations actually require.

In fraud detection, the stakes for each of these three metrics are concrete.

Latency: real-time payment fraud detection, transaction screening, and live content moderation have tight response requirements. Seconds of delay mean transactions slip through or legitimate traffic is blocked too long.

Cost: LLM API costs accumulate linearly with request volume. At high transaction rates, unit economics can fail even when accuracy is excellent.

Calibration: as described above, reliable confidence scoring is the prerequisite for any useful escalation or auto-decision threshold.

"Accuracy looked good in the PoC" does not tell you where you will land on these three. That is what Gabani calls the operational evidence gap — and it is the invisible failure mode for LLM deployments in fraud and T&S.

---

## ② FORTE: seven operational roles and a five-item checklist

The framework Gabani proposes in response is FORTE.

FORTE first organizes the roles LLMs can actually play in fraud detection and T&S operations into seven types: classifier, retrieval interface, explanation generator, review assistant, agent, feature extractor, and escalation component.

The role taxonomy matters because the required evaluation criteria differ by role. If the LLM is the classifier — making the actual detection judgment — then accuracy, calibration, and latency per decision are all on the table. If it is an explanation generator — producing human-readable rationale for a decision made by a separate system — then explanation quality and the risk of misleading output are the primary evaluation axes. If it operates as an agent with autonomous action capability, adversarial robustness becomes critical.

"Evaluating our LLM fraud detection system" is too broad to be actionable. Fixing the role first makes the evaluation design tractable.

The five-item pre-deployment checklist FORTE proposes:

1. Latency threshold — Does the LLM's decision speed meet the operational response requirement for this specific role in this workflow?
2. Cost ceiling — At expected request volume, does the per-decision API cost fit within acceptable margins?
3. Calibration — Do the LLM's confidence scores correlate with real-world accuracy in a way that makes confidence-based escalation thresholds reliable?
4. Explanation quality — Are the LLM's decision rationales adequate for audit, compliance review, and human escalation purposes?
5. Adversarial robustness — Does the LLM's judgment hold under adversarial inputs such as prompt injection or deliberately constructed evasion attempts?

These five are what the 49 reviewed papers largely did not test. They are also what production failure modes in fraud and T&S tend to trace back to.

---

## ③ Bringing FORTE to your team

Here is how this translates into practical action for different teams.

For financial risk and fraud teams: the most immediate change is adding FORTE's five criteria to your PoC evaluation design. Most PoCs for LLM fraud detection currently measure detection rate (F1, AUC) only. Building in latency measurement, per-decision cost tracking, and calibration assessment from the start means you have a production readiness gate, not just an accuracy number. Suggested KPIs to track in parallel: calibration error (the gap between stated confidence and actual accuracy), 95th-percentile latency, and cost per thousand decisions. If any of these land outside acceptable range, you have a pre-production signal before the investment compounds.

For fintech product and platform teams: FORTE's role taxonomy is the right place to start before writing any code. Deciding whether the LLM is a classifier, a review assistant, or an escalation component changes everything downstream — required latency, cost structure, calibration requirements, and human-in-the-loop design. Locking the role first, then designing around that role's specific constraints, avoids the costly rework that comes from discovering the mismatch at integration time.

For compliance and internal audit: explanation quality and adversarial robustness are the two checklist items most directly relevant to your work. Building pre-deployment test documentation for both — can the LLM's reasoning be shown to an auditor? does it hold under adversarial input? — creates the evidentiary record that regulators and internal committees typically ask for after the fact. Having it ready before deployment changes the conversation.

For RegTech and risk governance: the seven-role taxonomy is useful in board and regulator-facing materials. "Our LLM is deployed in the role of review assistant, within these boundaries, evaluated against these five criteria" is a cleaner and more defensible framing than "we use AI for fraud detection." It makes scope, accountability, and oversight structure legible to non-technical audiences.

For Trust-and-Safety platform teams: adversarial robustness is worth treating as a hard gate, not a nice-to-have. Content moderation LLMs are a natural target for prompt injection and carefully crafted evasion. Pre-deployment robustness testing against adversarial inputs should be built into the evaluation protocol from the start, not added after incidents surface.

---

## "Accuracy looked good" is not a deployment decision

Forty-nine papers. Zero simultaneous reports of latency, cost, and calibration.

That is a strong finding — and it is not an indictment of researchers. It reflects a structural mismatch between what academic evaluation rewards (accuracy, reproducibility, novelty) and what practitioners need to make deployment decisions (latency, cost, and calibration together, for a specific operational role).

FORTE's value is in naming that gap explicitly and giving practitioners a structure to fill it themselves, at the PoC stage, before the gap becomes an expensive production incident.

If your organization is evaluating LLMs for fraud detection, content moderation, or any T&S workflow, FORTE's five-item checklist is worth adding to your PoC evaluation template now — not as extra overhead, but as the gate that turns a promising experiment into a production-ready judgment.

That's it for today!

---

## References

1. Gabani, Keyur (2026). *Operational Evidence Gaps for LLMs in Fraud Detection and Trust-and-Safety Workflows*. arXiv preprint. https://arxiv.org/abs/2607.13078

<p class="ai-notice"><small>* This article was written in part with AI assistance and may contain inaccuracies.</small></p>
