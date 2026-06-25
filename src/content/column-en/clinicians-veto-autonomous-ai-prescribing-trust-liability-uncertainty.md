---
title: "When AI Prescribes, Who Gets the Veto? Designing for Trust in Autonomous Clinical AI"
date: "2026-06-26"
excerpt: "As autonomous AI moves from recommending to deciding on prescriptions, how should clinicians retain meaningful authority? A framework that distinguishes types of uncertainty and triggers human escalation offers a path to trust and clear accountability."
image: "/column-images/clinicians-veto-autonomous-ai-prescribing-trust-liability-uncertainty.png"
imageAlt: "Flat illustration of a clinician and an AI panel side by side in an examination room, with an arrow returning control to the human at a high-risk decision point"
readingMinutes: 5
basedOnPaper: "The Clinician's Veto: Navigating Trust, Liability, and Uncertainty in Autonomous AI Prescribing"
basedOnPaperUrl: "https://arxiv.org/abs/2606.25108"
---

Hello. This is Inoshita from Affectosphere Group.

A quiet but important shift is underway in healthcare AI.

Early clinical decision support tools offered suggestions — a ranked list of drugs, a flag for potential contraindications. Clinicians could take it or leave it. Now a new generation of systems is moving toward autonomous decisions: the AI determines the drug, the dose, the timing.

That raises an uncomfortable question. If an autonomous AI prescribes and something goes wrong, who is responsible?

A paper published on arXiv in June 2026 by LaRocco et al. (arXiv:2606.25108) tackles this directly. Their answer centers on a deceptively simple idea: clinicians need a veto, and the system needs to know when to ask for one.

---

## Three takeaways for today

1. AI uncertainty comes in two distinct forms — one fixable with more data, one not — and conflating them leaves clinicians with no useful guidance.
2. Communicating the type of uncertainty, not just its magnitude, enables precise human intervention at the right moments.
3. Designing an explicit escalation trigger — when uncertainty crosses a threshold, the human takes the wheel — can simultaneously raise trust, clarify liability, and improve real-world adoption.

---

## ① Two kinds of uncertainty that matter differently

When a clinical AI says it is "60% confident," what does that number actually mean?

LaRocco et al. argue this number hides two fundamentally different situations.

The first is epistemic uncertainty. The model is unsure because it lacks data. The patient's profile — age, comorbidities, lab value combination — is underrepresented in training data. Critically, this kind of uncertainty is improvable. Add more data, retrain, consult a specialist, order another test — and the picture can get clearer.

The second is aleatoric uncertainty. The model is unsure because the patient is genuinely hard to predict. Individual biological variation means that even with perfect data, some patients will respond idiosyncratically to a drug. No amount of additional data resolves this. It is irreducible uncertainty, inherent to the patient.

If a system collapses both into a single score, clinicians lose their compass. When should I order more tests? When should I simply proceed cautiously? Those two situations call for very different responses.

---

## ② The design principle: show the type, not just the level

The framework LaRocco et al. propose is straightforward: when AI presents a prescription recommendation, it should surface which kind of uncertainty is driving the confidence level.

If epistemic uncertainty is high — "this case type is underrepresented in my training data" — the clinician gets a clear signal to gather more information. Request an additional lab panel. Consult a pharmacogeneticist. Run a chart review of similar cases.

If aleatoric uncertainty is high — "this patient's biological profile makes outcomes inherently variable" — the clinician knows that more data will not help much. The right move might be a lower starting dose with close monitoring, or a shared decision-making conversation where the patient's own risk preferences guide the call.

This is not just a UI improvement. It changes the nature of the human-AI collaboration. Instead of the clinician second-guessing an opaque score, they are receiving actionable information about where the AI's limitations lie.

---

## ③ The veto as a structural accountability mechanism

The research goes further than uncertainty communication. It argues that autonomous prescribing systems must explicitly preserve the clinician's veto.

The word "veto" here is doing real work. It is not just a technical override button — it is an accountability record. When a clinician exercises the veto, the system logs: who intervened, at what time, on what AI recommendation, and what alternative was chosen. That log becomes critical evidence in the event of an adverse outcome or a liability investigation.

Without an explicit veto mechanism, accountability becomes murky. Did the AI decide? Did the clinician tacitly endorse it by not intervening? The law and hospital governance committees will want answers that the system needs to be able to provide.

The escalation design follows directly from this. When either form of uncertainty crosses a pre-defined threshold, the system automatically flags the case for mandatory human review before any action is taken. This is not a workaround for weak AI — it is the core design. In clinical environments, LaRocco et al. suggest, this kind of structured hand-off is what makes autonomous AI practically viable.

---

## Practical application: what HIS and clinical AI teams can do now

The target audience for this section is hospital IT departments managing electronic health record (EHR) systems, and medical device procurement teams evaluating AI-assisted prescribing tools.

The first concrete step is an audit of your current clinical AI products. Do they output uncertainty scores? If yes, do they distinguish between epistemic and aleatoric sources? Most tools today report a single confidence value. Products that go further are worth prioritizing in evaluations.

The second step is operational: start logging the cases where AI confidence is below a threshold and track what clinicians actually do with those cases. Build a monthly review routine around the question: in cases where the AI flagged low confidence and no physician intervened, what was the outcome?

A practical KPI pair to track would be (a) the rate at which physicians override AI recommendations in high-uncertainty cases, and (b) the concentration of adverse events in high-uncertainty / no-intervention cases. If adverse events are clustering there, the escalation thresholds need tightening.

For teams developing or procuring new prescribing AI, the research suggests making uncertainty-type disclosure a functional requirement, not a nice-to-have. Build it into the vendor evaluation rubric.

---

## "Can your AI tell you when it doesn't know?"

Healthcare institutions have been asking "can we trust this AI?" That is the right question. But the more precise version of it is this: can the AI tell you what it doesn't know, and show you why?

A clinical AI that surfaces the type of its uncertainty — epistemic versus aleatoric — and automatically escalates when that uncertainty is high gives clinicians a basis for trust that a single confidence score never can.

The clinician's veto is not a sign of distrust in AI. It is the design feature that makes autonomous prescribing safe enough to use.

---

## Reference

1. Eileanor LaRocco, Sarah Tan, Adarsh Subbaswamy, et al. (2026). *The Clinician's Veto: Navigating Trust, Liability, and Uncertainty in Autonomous AI Prescribing*. arXiv preprint.

<p class="ai-notice"><small>* This article was written in part with AI assistance and may contain inaccuracies.</small></p>
