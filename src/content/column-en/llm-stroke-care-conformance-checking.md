---
title: "No CIG Required ── LLMs Are Now Auditing Clinical Records Straight from the PDF"
date: "2026-06-10"
excerpt: "Verifying whether patients received guideline-compliant care has long required costly conversion of clinical guidelines into computer-interpretable formats. A pilot at an Italian hospital now shows that a six-stage LLM pipeline can audit 463 stroke patient records against 50 extracted rules — using nothing but the original PDF guideline and discharge summaries."
image: "/column-images/llm-stroke-care-conformance-checking.png"
imageAlt: "Flat illustration of an LLM pipeline connecting electronic medical record screens to a clinical guideline document"
readingMinutes: 6
basedOnPaper: "LLM-Orchestrated Conformance Checking in Stroke Care Without Computer-Interpretable Guidelines"
basedOnPaperUrl: "https://arxiv.org/abs/2606.09489"
---

Hi, I'm Keito Inoshita from Affectosphere Group.

Anyone working in hospital quality management or healthcare information systems will recognize these situations.

"We want to regularly check whether treatments are following the guidelines. But extracting data from charts manually doesn't scale at all."

"We looked into an audit tool, but it required converting our guidelines into a proprietary format — the cost and effort didn't add up."

"We need documented evidence of compliance for reimbursement reviews and litigation risk, but generating that report still takes enormous manual work."

Clinical conformance checking — verifying that patient care aligns with evidence-based guidelines — is critical for both patient safety and institutional risk management. Yet it has remained stubbornly difficult to automate. The core barrier: guidelines are written in natural language for human readers, not in formats that computers can directly interpret.

A paper published on arXiv in June 2026 (Giorgio Leonardi, Stefania Montani, Manuel Striani, Alessandro Canessa, Delfina Ferrandi, arXiv:2606.09489) reports a system that breaks through this barrier using multi-stage LLM orchestration. A pilot deployment at the Neurology Ward of Alessandria Hospital in Italy — using 463 anonymized stroke patient records — demonstrated that a PDF guideline and discharge summaries are sufficient inputs to automate clinical conformance auditing.

Today I'll walk through the research for hospital administrators, quality managers, and healthtech engineers.

---

## 3 Points for Today

1. Core value: The original PDF guideline works as-is. No conversion to a specialized format is required.
2. The six-stage LLM pipeline: from structured discharge record extraction to rule derivation, Python script generation, and compliance scoring.
3. Implementation lens: which departments can use this for which KPIs, and what limitations to know upfront.

---

## ① What "No CIG" Actually Means

Let me unpack the phrase "Computer-Interpretable Guidelines (CIG)" first.

Traditional automated audit tools assumed that clinical guidelines had already been converted into a machine-readable format such as GLIF, ASBRU, or PROforma. These specialized CIG formats have been studied for decades, but they have not penetrated routine clinical practice — because the conversion process requires specialized expertise, is expensive, and must be repeated every time the guideline is updated.

The vast majority of clinical guidelines worldwide are still distributed as PDF or Word documents. This is what blocks automation.

The key idea from Leonardi et al. is that you can skip CIG creation entirely. With LLMs capable of natural language understanding, a pipeline can extract rules directly from the original PDF text and convert them into executable code.

---

## ② The Six-Stage LLM Pipeline

The system operates in six stages, each with a distinct model and role.

Stage 1 — Trace extraction from discharge records (Gemini 2.5 Flash). The discharge summary is the input. The model generates a timestamped event log (XES format) of what procedures the patient received and when. For 463 Alessandria patients, the average trace contained 47 events over an average 10-day stay.

Stage 2 — Rule extraction from the guideline (NotebookLM). The PDF of the Italian Stroke Association guideline goes in, and IF-THEN clinical rules come out. This stage produced 161 rule candidates organized across 9 clinical categories.

Stage 3 — Filtering applicable rules (Gemini 2.5 Flash). Out of 161, rules covering outpatient prevention (outside the hospital stay window) and those requiring data not collected in the EMR are removed. The result: 50 applicable rules.

Stage 4 — Conversion to Python scripts (Gemini 2.5 Flash). Each of the 50 rules is automatically translated into an executable Python script. Each script reads the event log and returns one of three labels: CONFORMANT, NOT CONFORMANT, or NOT APPLICABLE.

Stage 5 — Code quality improvement (Gemini 2.5 Pro Preview). A separate model reviews the generated code for bugs, redundancy, and readability issues.

Stage 6 — Compliance scoring (Python module). For each rule, a "Trace Conformance Indicator (TCI)" is calculated: the percentage of patients for whom the rule applied who were judged compliant. The metric is intentionally simple and interpretable.

---

## ③ Results and What the Numbers Revealed

Across all 50 rules and 463 patient traces, overall compliance exceeded 86%.

But looking at individual rules surfaced meaningful insights.

For the antihypertensive therapy rule in hemorrhagic stroke patients, TCI was 62%. Investigation showed that blood pressure treatment was being initiated in the neurology ward after transfer — not in the emergency department where guidelines specify it should begin. A cross-department coordination gap, now visible as a number.

For the antipyretic therapy rule, TCI was only 6%. At first glance this looks alarming. But drilling down showed that 69% of "non-compliant" cases had bacterial infections being treated with antibiotics, and 6% had COVID-19 managed with antivirals. These are clinically appropriate responses to the underlying cause — antipyretics weren't the right intervention. The data point illustrates that TCI scores require clinical interpretation; the number alone is not a verdict.

For validation, physicians manually reviewed a random 20% sample (approximately 93 traces). All reviewed traces were judged accurate and usable.

---

## ④ Implementation View: Who Uses This for What

Quality management and patient safety departments

The most direct application is automating periodic chart audits. What has typically been done as monthly or quarterly sampling with manual review could shift to weekly or continuous full-cohort monitoring. KPIs like "TCI trend per rule over time" and "non-compliant case counts by ward" make it possible to track compliance patterns by department, season, or care team.

Risk management and legal teams

In clinical negligence disputes or regulatory inquiries, documented evidence that treatment followed established guidelines can matter. Automatically generated TCI scores and the underlying event logs create a continuous compliance record that can be surfaced on request.

Reimbursement and insurance review teams

As payers increasingly require quantitative evidence of guideline adherence, a system that captures not just whether a procedure occurred but when, where, and in what sequence relative to other interventions goes beyond what manual checks typically produce.

Healthtech companies and EMR vendors

The "no CIG required" property dramatically lowers integration barriers. There is no proprietary format conversion module to build and maintain. This makes the architecture viable for smaller hospitals, regional facilities, and healthcare systems in settings where CIG tooling has never been adopted.

---

## ⑤ Current Limitations and the Road Ahead

The paper is transparent about what the system cannot yet do.

It can only check what the discharge summary records. Verbal physician orders, bedside nursing observations, and anything not captured in the formal written record are outside the scope of the audit.

Rule extraction from the guideline was not perfect. Of the 161 rule candidates, 3 were found to be incomplete when compared to the source guideline, and the secondary prevention category was rated lower quality. The system is not infallible.

The system also assumes that the recorded facts are accurate. It cannot detect errors or omissions in the documentation itself.

The authors identify several directions for future work: integrating additional hospital data sources beyond discharge summaries, systematic comparison across different LLM models, and extension toward real-time monitoring. Crucially, because the pipeline is triggered by the guideline text, updating a guideline only requires re-running the pipeline — a significant operational advantage over maintaining hand-crafted CIG representations.

---

## Takeaway

What Leonardi et al. demonstrated is that the raw materials already present in most hospitals — a PDF guideline and electronic discharge summaries — are sufficient, when processed through a multi-stage LLM pipeline, to automate clinical conformance auditing.

A 463-patient, 50-rule pilot is still early-stage. But the architecture is extensible, and the core proposition — no CIG conversion needed — removes the single largest barrier that has kept automated audit tools out of routine clinical practice.

"AI for patient safety" can sound like a grand claim. What this system actually does is more grounded: extract rules from text, match them against event logs, and report percentages. The simplicity is the point. Deployable tools tend to be simple ones.

For those working on hospital quality or health IT strategy, the research is less a ready-to-deploy product than a design template worth understanding.

---

## Reference

Leonardi, G., Montani, S., Striani, M., Canessa, A., & Ferrandi, D. (2026). LLM-Orchestrated Conformance Checking in Stroke Care Without Computer-Interpretable Guidelines. arXiv:2606.09489. https://arxiv.org/abs/2606.09489

<p class="ai-notice"><small>* This article was written in part with AI assistance and may contain inaccuracies.</small></p>
