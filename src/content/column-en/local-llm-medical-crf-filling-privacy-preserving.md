---
title: "Automate CRF Entry Without Sending Hospital Data Anywhere ── How Local LLMs Enable Privacy-Preserving Clinical Trial Support"
date: "2026-06-14"
excerpt: "A fully local two-stage LLM pipeline using MedGemma-27B achieved second place (macro F1 = 0.55) on an English clinical CRF-filling benchmark — zero external API calls, zero fine-tuning. If local on-premise deployment can reach competitive performance on this task, pharmaceutical companies, CROs, and hospitals have a concrete path to privacy-compliant AI-assisted data entry."
image: "/column-images/local-llm-medical-crf-filling-privacy-preserving.png"
imageAlt: "Illustration of an EHR screen and a local server, with data processing contained entirely within the hospital network and no external cloud connections"
readingMinutes: 5
basedOnPaper: "sebis at CRF Filling 2026: A Two-Stage Local LLM Pipeline for Medical CRF Filling"
basedOnPaperUrl: "https://arxiv.org/abs/2606.13082"
---

Hi, I'm Keito Inoshita from Affectosphere Group.

Talk to anyone running clinical data management and you'll hear the same thing: CRF entry is still mostly manual.

The patient information is right there in the electronic health record. But moving it into the Case Report Form — field by field, visit by visit — still requires a human. Transcription errors, missing entries, the sheer volume of review work: this is a well-known operational burden across pharma, CROs, and hospitals alike.

"Why not use AI?" is a question that's been asked for years. The problem is that sending medical data to an external cloud API is legally and ethically fraught. GDPR, HIPAA, domestic privacy regulations, sponsor agreements, ethics committees — the barriers to using cloud LLMs on clinical trial data are significant.

A 2026 study (Katharina Sommer, Tristan Till, Florian Matthes, arXiv:2606.13082) took this constraint seriously. They built a fully local two-stage LLM pipeline using MedGemma-27B — no external API, no fine-tuning, few-shot in-context learning only — and achieved second place on the English test track of a clinical CRF-filling benchmark, with a macro F1 score of 0.55.

---

## 3 Points for Today

1. Discovery: A fully local LLM pipeline, using only few-shot in-context learning with no external API calls, reached competitive performance on a clinical CRF-filling benchmark.
2. Design: A two-stage architecture — binary classification of field-level information presence, followed by value extraction — enables safe, structured clinical information extraction with deterministic output constraints.
3. Business application: This is a working design template for pharmaceutical companies, CROs, and hospitals that want to build on-premise CRF automation while remaining GDPR- and HIPAA-compliant.

---

## ① Why CRF Entry Is Still a Problem

A Case Report Form (CRF) is the standardized data collection instrument for clinical trials. Each trial has dozens or hundreds of fields. Each patient, each visit, each event — someone has to pull that information from the EHR and enter it into the CRF.

Beyond the volume, the problem is structural. EHR notes are unstructured text. Extracting "adverse event present: yes/no," "severity grade," and "outcome" from a clinical note like "patient's condition remains stable, mild fatigue reported" is a natural language processing challenge. The surface form varies across clinicians, institutions, and documentation styles.

There's also a three-way distinction that matters a great deal for regulatory compliance: "No" (the condition did not occur), "Unknown" (we don't know whether it occurred), and "Not mentioned" (the record doesn't address it). Conflating these in a CRF can create data quality issues that surface in regulatory review.

The paper addresses all of these challenges in a single pipeline.

---

## ② The Two-Stage Pipeline Design

The architecture has two stages.

Stage 1 is binary classification: for each CRF field, the model determines whether the EHR text contains relevant information to fill it. If not, the field is left empty. No guessing, no confabulation.

Stage 2 is value extraction: for fields where Stage 1 detected relevant information, the model extracts the specific value.

Separating these stages matters. A common failure mode in AI-assisted data entry is over-completion: the model tries to fill every field even when the information isn't there, producing implausible or contradictory values that create downstream data quality problems. Explicit Stage 1 control — "if no information is present, do not fill" — structurally prevents this.

The pipeline also enforces deterministic output constraints for handling ambiguous clinical states. The three-way distinction between "not mentioned," "unknown," and "negative" is handled explicitly, preserving the semantic distinctions that matter for regulatory data quality.

The base model is MedGemma-27B — a medically pre-trained open-weight model that runs on local hardware. No fine-tuning on the target dataset. Few-shot in-context learning only: a small number of input-output examples in the prompt is all the task-specific adaptation the system uses.

---

## ③ What "Competitive Performance Without External APIs" Actually Means

The macro F1 of 0.55 and second-place ranking on the English test track are meaningful not because 0.55 is a high absolute number — it isn't — but because of what was not used to achieve it.

No OpenAI API. No Google API. No proprietary cloud endpoint. No fine-tuning on labeled training data. The model runs on hardware inside the institution, and patient data never leaves.

This is the constraint that had previously seemed to require a trade-off: you can have privacy or you can have good performance, but not both. This paper shows the trade-off is less severe than assumed, at least for this task and this model.

MedGemma-27B is an open-weight model pre-trained on medical text and medical imaging. It can be downloaded and run on on-premise GPU infrastructure. Combined with few-shot prompting, it achieves performance in the competitive range of systems that use external APIs.

That's the baseline that matters for any organization evaluating whether local deployment is worth attempting.

---

## ④ Concrete Application Scenarios

Here is how pharmaceutical companies, CROs, and hospitals can translate this research into practice.

### For pharmaceutical data management teams and CROs

The most immediate application is a pilot for "EHR → CRF draft auto-generation" on a defined subset of fields.

Start with the more structured fields — vital signs, lab values, adverse event flag, severity grade. Run Stage 1 (information presence detection) and Stage 2 (value extraction) on local GPU infrastructure. The output is a pre-filled CRF draft that a human data manager reviews and approves.

Design your KPIs around two metrics: draft generation rate (what percentage of fields the system proposes a value for) and draft accuracy (what percentage of those proposals are correct). This framing makes it easy to explain the value to internal stakeholders and to track improvement over time.

For GDPR and HIPAA compliance, the key documentation is straightforward: patient data does not leave the institution's infrastructure, and the system maintains processing records as required. This pipeline satisfies both requirements structurally, not by policy exception.

### For hospital clinical trial management units

Academic medical centers and university hospitals running their own trials can directly target transcription error reduction and missing data rates as the measurable business outcome.

The three-way "unknown / not mentioned / negative" distinction the pipeline explicitly handles is particularly valuable here. Automating that disambiguation reduces the human review burden on data entry and the data cleaning burden downstream.

If the EHR system is HL7 FHIR-compliant, the pre-processing pipeline for extracting unstructured text from structured records is easier to standardize — lowering the integration cost.

### For medical AI software vendors

For vendors offering CRF management SaaS, this research provides a technical foundation for an on-premise AI module that reaches competitive performance parity with cloud-based offerings.

The traditional challenge for on-premise AI features has been the performance gap versus cloud API-based systems. This paper shows the gap is closable for CRF tasks using open-weight models — which is a genuine product differentiation opportunity for vendors whose customers cannot use cloud AI due to regulatory or contractual constraints.

---

## The Regulatory Alignment

The design of this pipeline aligns with the requirements of major privacy frameworks.

Under GDPR, personal data processing requires purpose limitation, data minimization, and restrictions on third-party transfers. A fully local pipeline satisfies the third-party transfer constraint structurally — there is no transfer to an external processor.

Under HIPAA, sending PHI (Protected Health Information) to an external API requires a Business Associate Agreement. Local deployment avoids this requirement entirely.

In Japan, the Act on the Protection of Personal Information and the Next Generation Medical Infrastructure Act impose similar constraints on the handling of medical information as a category of sensitive personal data. Keeping processing on-premise simplifies ethics committee approval and institutional review board submissions significantly.

---

## What This Research Does Not Yet Solve

To be direct: macro F1 of 0.55 is not production-ready for unassisted entry.

At this performance level, the practical deployment model is human-in-the-loop: the system generates a draft, a human data manager reviews and corrects it. The value is in reducing the time the human spends generating the draft from scratch — not in replacing the human review step.

Open challenges remain. Multilingual support (Japanese EHRs, for instance, are a different NLP problem). Cross-visit context tracking — where a finding in visit 3 refers back to a condition documented in visit 1. Field-level performance variance — some CRF fields are likely much easier to extract than others, and aggregate F1 masks that heterogeneity.

These are research and engineering problems that the paper doesn't claim to solve. What it does establish is that the privacy-preserving local deployment constraint, which many organizations assumed would preclude competitive AI performance on this task, is not the blocking factor it appeared to be.

That's all for today!

---

## References

1. Katharina Sommer, Tristan Till, Florian Matthes (2026). *sebis at CRF Filling 2026: A Two-Stage Local LLM Pipeline for Medical CRF Filling*. arXiv preprint arXiv:2606.13082.

<p class="ai-notice"><small>* This article was written in part with AI assistance and may contain inaccuracies.</small></p>
