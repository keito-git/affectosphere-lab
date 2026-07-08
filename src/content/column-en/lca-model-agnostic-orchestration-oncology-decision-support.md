---
title: "Cutting oncology AI's vendor lock-in by design — LCA, a decision-support framework where you keep swapping the model"
date: "2026-07-08"
excerpt: "When a hospital brings in AI-assisted diagnosis, many people worry: what if we get chained to this vendor and cannot switch in a few years? LCA separates data ingestion, clinical routing, and inference into three layers so you can freely swap only the AI model that does the reasoning. Here is a concrete proposal for how a cancer hospital's health informatics team could bake it into AI procurement criteria."
image: "/column-images/lca-model-agnostic-orchestration-oncology-decision-support.png"
imageAlt: "Flat illustration of a hospital oncology decision-support system with three layers — patient-data standardization, clinical routing, and interchangeable AI models — connected by clean modular pipelines"
readingMinutes: 6
basedOnPaper: "The Large Cancer Assistant (LCA): A Model-Agnostic Orchestration Framework for Scalable Clinical Decision Support in Oncology"
basedOnPaperUrl: "https://arxiv.org/abs/2607.06531"
---

Hello. I am Miura from Affectosphere Group.

Whenever a hospital talks about bringing in AI-assisted diagnosis, one worry always tags along. "Won't we get chained to this vendor's model and be unable to switch a few years from now?"

Medical AI moves fast. This year's best model may not be next year's. Yet in many deployments, a specific vendor's model and the hospital's IT system end up tightly coupled, so when you later try to swap in a different AI, the data integration and even the screens have to be rebuilt — the classic vendor lock-in.

A study published on arXiv (Marrakchi & Matei, arXiv:2607.06531) takes this problem head-on for oncology clinical decision support. It proposes LCA (Large Cancer Assistant), a model-agnostic orchestration framework designed so that any AI model can be swapped in interchangeably. Today I want to think, from a business-application angle, about how your hospital or company could actually try it.

---

## Three takeaways

1. LCA dissolves oncology AI's biggest headache — dependence on a specific model (vendor lock-in) — by separating processing into three layers: data ingestion, clinical routing, and inference. Splitting the layers lets you freely swap only the AI model that does the reasoning.
2. It defines the relationship among the three layers as a formal 7-tuple mathematical architecture. Entry Theory uses geometric deep learning to standardize multimodal patient data, and the Cancer Switching Module generates a structured intermediate payload that fully isolates AI inference from the hospital IT system.
3. Orchestration overhead is zero, and data-anomaly detection recall reaches 100%. It is designed as next-generation oncology clinical-decision-support infrastructure with electronic medical record (EMR) interoperability.

---

## ① Why vendor lock-in is so painful on the ground

First, let me lay out why vendor lock-in is so disliked.

Medical AI, and oncology especially, advances quickly. Imaging diagnosis, genomic analysis, treatment-plan suggestion — the models get updated almost every year. Ideally, a hospital wants to move to "the best model available right now" at any time.

But in real deployments, the AI model and the hospital's IT systems — the EMR, lab data, image servers — become tightly coupled. Once you wire the data integration to fit one vendor's model, switching to a different AI means rebuilding that integration too. This "rebuild cost" is so high that the hospital ends up chained to the first vendor. That is what lock-in really is.

On top of that, clinical settings handle patient data — extremely sensitive information. Every time you swap the model, you have to re-verify where that data flows and how. When that is heavy, the very decision to switch grinds to a halt.

---

## ② What LCA actually does: three-layer separation and full isolation

What LCA does is sever this tight coupling through layer separation.

The paper splits processing into three layers. The first is the data-ingestion layer. The second is the clinical-routing layer. The third is inference — the layer where the AI model actually makes the call. A defining feature is that it defines the relationship among these three layers properly, as a formal 7-tuple mathematical architecture.

In the ingestion layer, a geometric deep learning approach called Entry Theory standardizes multimodal patient data that arrives in disparate formats — images, lab values, records. In other words, it aligns the shapes right at the entrance.

The crux is the Cancer Switching Module. It generates a "structured intermediate payload" that fully isolates AI inference from the hospital IT system. Between the hospital's data and the AI model's input, it inserts one clean intermediate format. Because of that single layer, the AI model never touches the hospital's systems directly, and conversely, swapping the model leaves the hospital side unaffected.

And the paper reports that this separation carries zero orchestration overhead. Adding an intermediate layer would normally slow things down, but here that price is not paid. It also reports data-anomaly detection recall of 100% — catching oddities in incoming data without letting any slip through. In a field like medicine, where input data quality is directly tied to lives, a design that does not miss here is welcome.

---

## ③ How to try it on the ground: departments and KPIs

So how would you put this to use in your own hospital or company? As a business application, here is my own take on where it fits.

The most realistic move is for a cancer hospital's or university hospital's health informatics team to bake model-agnostic orchestration into the procurement criteria for AI-assisted diagnosis. That is, stop selecting on the performance of an individual AI model alone, and add a requirement: "Is it separated into three layers like LCA, with the inference model replaceable?" This way, whichever vendor you pick first, you secure from the start the room to periodically move to the latest model later.

By department, the lead is the health informatics or information systems department that owns in-hospital AI adoption. It writes an operating rule — "re-evaluate and swap the model every few years" — into the contract at the procurement stage. Oncology AI vendors, too, can align with this separation design and sell "the reassurance that you can switch later." The same "infrastructure that does not lock the model in" mindset also works for oncology risk assessment at health insurers and for patient selection in pharma clinical trials.

For KPIs, so you can tell the impact in numbers, I propose the following. First, the labor and time a model swap takes — how many person-days or weeks to move to a new AI model. With a separated design, this should shrink dramatically. Second, the re-verification cost of data integration at swap time — because the intermediate payload isolates things, the scope that must be re-verified narrows. Third, the cost of regulatory compliance such as HIPAA and GDPR. With hospital IT and AI fully separated, there are fewer paths by which patient data touches the AI side directly, so you can tighten both the compliance cost and the audit scope.

As a path forward, I think it is good to start small with a single cancer type and a single model, and run one experiment: "swap in a different model while keeping the same framework." Confirm with your own hands, before adoption, whether swapping is truly light. If it feels solid here, that becomes firm grounds for elevating it into a procurement standard.

---

## Building a vessel that swaps in intelligence, not the intelligence itself

What I found good reading this work is a design philosophy that separates "the performance race" from "ease of switching."

Which model is smartest keeps changing with the times. So instead of fixing the smartness itself, you fix the foundation on which a smart model can be swapped in at any time. This, I think, is an idea that pays off more the faster a field moves.

Affective AI actually carries the same challenge. Emotion-recognition models get replaced almost every year, yet if the system is tightly coupled to one model, a better evaluation model can appear and you still cannot slot it in. LCA's model-agnostic idea, I felt, is a prior example you can reference directly when designing an evaluation foundation for affective AI too.

Rather than chasing intelligence, build a vessel that lets you swap intelligence in and out. It is not flashy — but the more a setting has lives on the line and heavy regulation, like medicine, the more this kind of design pays off.

That is it for today!

---

## References

1. Marrakchi, Ghassen, & Matei, Basarab (2026). *The Large Cancer Assistant (LCA): A Model-Agnostic Orchestration Framework for Scalable Clinical Decision Support in Oncology*. arXiv preprint. https://arxiv.org/abs/2607.06531

<p class="ai-notice"><small>* This article was written in part with AI assistance and may contain inaccuracies.</small></p>
