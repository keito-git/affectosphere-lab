---
title: "You trust the AI's explanation. But who audited the explanation? — ConceptSMILE and the accountability of explanations"
date: "2026-07-13"
excerpt: "We hand regulators and customers explanations like \"the AI decided this because of X.\" But has anyone inspected whether the explanation itself is correct? ConceptSMILE is a model-agnostic, perturbation-based framework for auditing the trustworthiness of concept-based XAI. On retinal fundus images, MedSAM-derived visual concepts reached a surrogate fidelity of R^2=0.8503. Here is how an AI governance team could try it — departments and KPIs included."
image: "/column-images/conceptsmile-auditing-concept-based-explainable-ai.png"
imageAlt: "Flat illustration of an inspector examining AI-generated explanation cards one by one with a magnifying glass and perturbation tests, scoring each for trustworthiness and compiling them into an audit report"
readingMinutes: 5
basedOnPaper: "ConceptSMILE: Auditing the Trustworthiness of Concept-Based Explainable AI"
basedOnPaperUrl: "https://arxiv.org/abs/2607.09649"
---

Hello. I am Miura from Affectosphere Group.

Something has been nagging at me lately whenever AI governance comes up.

Plenty of companies have adopted explainable AI (XAI) by now. A loan-screening model outputs a score, and along with it a reason: "repayment history and debt ratio drove this decision." A diagnostic-support model says, "I focused on this lesion region." As regulatory practice, and as customer communication, this is the right direction.

But here is the thought I keep having. Is that explanation actually correct?

Suppose the model was really looking somewhere else entirely, while the explanation plausibly told us "repayment history mattered." We would not catch it. The explanation gets treated as true the moment it is produced, and it goes straight into the audit file.

We do not really have a mechanism to hold explanations accountable.

A study published on arXiv (Mollapour, Aslansefat, Dehghani, Mishra, Shah & Mian, arXiv:2607.09649) aims exactly there. It proposes ConceptSMILE, a framework for auditing the trustworthiness of concept-based XAI.

Today I want to look at this from a business-application angle and think about how a company could fold it into its own AI governance.

---

## Three takeaways

1. The premise: concept-based XAI (explaining a model's reasoning in human-understandable "concepts") is easy to read, but concept-level outputs are not automatically trustworthy just because they are legible.
2. ConceptSMILE is a model-agnostic, perturbation-based auditing framework that extends SMILE's perturbation logic from the feature and region level up to the auditing of concept explanations. It combines perturbation of input regions, measurement of concept response shifts, locality weighting, and XGBoost surrogate fitting, and evaluates trustworthiness through attribution accuracy, surrogate fidelity, faithfulness, stability, and consistency.
3. On retinal fundus images, MedSAM-derived visual concepts showed higher spatial attribution accuracy and surrogate fidelity (R^2=0.8503), while VLM-based semantic concepts showed stronger vessel faithfulness and stability. In other words, how you define your concepts changes the quality of the trust you get.

---

## ① The blank space called "accountability of explanations"

Let me first lay out where the gap sits.

XAI adoption projects usually end at "now we can produce explanations." The tool is installed, heatmaps or concept attributions come out. Goal met, on to the next phase.

But one question never gets asked. Does that explanation reflect what the model actually does?

Concept-based XAI makes this especially hard to see. When you are told "the concept of vessel abnormality is strongly present in this image," it lands beautifully for a human. And precisely because it lands, it is hard to doubt. Yet an explanation being human-friendly and an explanation being accurate are two entirely different things.

That is the paper's starting point. Concept-level outputs are easy for humans to understand — that is all. Legibility does not confer trustworthiness. Hence the need for an auditing framework.

I think this lands squarely on corporate AI governance as it stands. We validate model accuracy. We inspect data bias. But a step that validates the quality of the explanation itself simply does not exist in most internal processes.

---

## ② Shaking the input to measure trust

So what does ConceptSMILE actually do?

Crudely put, it shakes the input. It perturbs regions of the input, then measures how the concept responses shift. It applies locality weighting so that nearer perturbations count more heavily, and fits a surrogate model with XGBoost. Through that chain, it quantifies whether the explanation is genuinely coupled to the model's behavior.

What I find interesting is that it lifts SMILE's perturbation-based logic from the feature and region level up to the layer of concept explanations. The object of audit is no longer "which pixels mattered" but "which concepts mattered."

And trustworthiness is not collapsed into a single number. It is measured along several axes: attribution accuracy, surrogate fidelity, faithfulness, stability, and consistency. For practitioners this matters, because it encodes a design stance — whether an explanation can be trusted is not a question you round off into one score.

The experiments use retinal fundus images, comparing MedSAM-derived visual concepts against VLM-based semantic concepts. The results split cleanly. MedSAM delivered higher spatial attribution accuracy and surrogate fidelity (R^2=0.8503), while the VLM side showed stronger vessel faithfulness and stability.

Neither swept the board — and that is the part I lingered on. How you define your concepts shapes the trustworthiness profile of your explanations. And you only find that out by auditing.

---

## ③ How to try it on the floor: departments and KPIs

Here is the business-application core.

My proposal is to place a ConceptSMILE-style capability inside the company as an "XAI audit engine." Lay an independent verification layer over your existing XAI output. Separate the team that produces explanations from the team that inspects them. Accounting has external auditors; explanations should have an audit step too.

Three departments come to mind. First, AI governance — periodically auditing explanation quality and monitoring how trustworthiness scores move over time. Second, risk screening and compliance — a verification step before a loan-screening or insurance-underwriting model's explanation is handed to a regulator or a customer. Third, quality assurance for medical AI — a pre-release gate that checks whether the "region of interest" a diagnostic-support model highlights is truly its basis.

The KPIs I would set. First, the level of explanation fidelity scores (how high surrogate fidelity actually runs; you can fix a threshold per audited model and decline to submit explanations externally when it falls below). Second, the reduction in effort spent on XAI auditing (what share of the "this explanation looks plausible" eyeballing experts do today can be replaced by a quantitative indicator). Third, the regulatory accountability compliance rate (of the models whose explanations you submit, what fraction have had their trustworthiness verified).

A realistic small start, too. You cannot cover every model at once. Begin with the single highest-risk line of explanation — the stated reason for a loan denial, say, or the lesion a diagnostic-support model points to. Run the existing XAI output through a perturbation audit there and see what trustworthiness scores come out. If they are low, change the concept definition and measure again. As this study shows, how you build the concepts changes the result.

Then document the thresholds you learned as an internal XAI quality standard. That, I think, is the first step toward being able to tell a regulator: we independently verify the trustworthiness of our explanations.

---

## Inspect the explanation before you believe it

What I liked most about this work is the stance itself.

XAI has been sold as the technology that lets us trust AI. But we have been trusting what that technology outputs without any check of our own. Something got called an explanation, and by that name alone it was exempted from inspection. ConceptSMILE brings the audit in.

Regulation is certainly going to say "explain yourself." When it does, a company that merely produces explanations and a company that can show the trustworthiness of those explanations in numbers will be standing in very different places.

Incidentally, this is continuous with the affective AI we work on. "This text is anger, and here is the phrase that shows it" — is that phrase really what the model was looking at? With something as ambiguous as emotion, plausible-sounding explanations come cheap, which if anything raises the need for auditing.

Inspect the explanation before you believe it. It is not flashy, but I think this is the next move in AI governance.

That is it for today!

---

## References

1. Mollapour, Mohadeseh, Aslansefat, Koorosh, Dehghani, Zeinab, Mishra, Bhupesh Kumar, Shah, Tejal, & Mian, Zhibao (2026). *ConceptSMILE: Auditing the Trustworthiness of Concept-Based Explainable AI*. arXiv preprint. https://arxiv.org/abs/2607.09649

<p class="ai-notice"><small>* This article was written in part with AI assistance and may contain inaccuracies.</small></p>
