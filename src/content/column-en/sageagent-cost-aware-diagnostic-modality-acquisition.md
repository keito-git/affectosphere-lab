---
title: "\"Do we really need this scan?\" — letting AI decide whether to go get the data cut acquisition burden by 55%"
date: "2026-07-13"
excerpt: "Multimodal AI research usually competes on accuracy assuming every modality is already there. SAGEAgent went the other way: an LLM agent that actively reasons, per patient, whether the next test is justified — cutting average acquisition burden by 55% while keeping survival prediction competitive. From hospital test-cost optimization to requesting extra documents in credit underwriting and extra inspections in asset maintenance, here is how the idea travels — departments and KPIs included."
image: "/column-images/sageagent-cost-aware-diagnostic-modality-acquisition.png"
imageAlt: "Flat illustration of a branching diagnostic decision flow where an AI agent looks at the tests already in hand and decides whether to acquire the next MRI or stop here, with unnecessary branches greyed out and closed"
readingMinutes: 5
basedOnPaper: "SAGEAgent: A Self-Evolving Agent for Cost-Aware Modality Acquisition in Multimodal Survival Prediction"
basedOnPaperUrl: "https://arxiv.org/abs/2607.09521"
---

Hello. I am Miura from Affectosphere Group.

Let me open with a question.

Does every cancer patient really need the full set of diagnostic tests?

Pathology, genomics, MRI. Read the multimodal AI literature and the story almost always proceeds on the assumption that every modality is already sitting there. When one is not, it gets treated as "missing" and passively imputed. But the clinic does not work that way. Tests cost money. They cost time. They cost the patient something physically. And there absolutely exist tests whose result would not have changed the conclusion either way.

A study published on arXiv (Qu, Cui, Lu et al., arXiv:2607.09521) goes straight at that gap. The proposal is SAGEAgent — the name stands for Sequential Acquisition Guided by Experience.

Put as simply as possible, here is what it does. For each individual patient, the AI actively reasons about whether the next modality is worth going out and acquiring.

Today I want to look at this from a business-application angle and ask how far the idea can travel.

---

## Three takeaways

1. Existing multimodal survival prediction either assumes all modalities are available or passively handles missing data. None of it actively reasons, per patient, about whether acquiring the next modality is justified. SAGEAgent formulates that "sequential acquisition of diagnostic modalities" as a problem in its own right.
2. Under the hood it is an LLM-based clinical agent that tracks how the diagnostic state changes, combining a tool that converts numerical predictions into text, an episodic memory that retrieves similar past cases, and a semantic memory that accumulates reusable decision patterns from experience.
3. On a glioma cohort combining TCGA-LGG, TCGA-GBM, and BraTS, it cut average acquisition burden by 55% while maintaining competitive survival prediction accuracy. To me this is a story about AI's job expanding from "make the prediction better" to "decide whether to go get the data at all."

---

## ① AI's job is not only to get the answer right

First, the pivot in this work that I find most interesting.

The main arena of applied AI has been, almost entirely, predictive accuracy. Gather all the data, throw it at the model, compete on how often it is right. Multimodal learning followed the same arc: the more you blend images, text, and numbers, the better the accuracy gets.

But there is always a prior question sitting upstream of that.

How much are you willing to pay to go get that data?

A test has a price, a wait, and a burden on the patient. And yet existing methods have kept the acquisition cost of a modality outside the problem. Everything is assumed present. What is absent is imputed. Whether to acquire is a human's call.

SAGEAgent pulls that call into AI's territory. If the diagnostic state is already settled by what is in hand, the next test is not needed. If it is still wavering, acquiring is worth it. The agent reasons, patient by patient, about whether one more move is justified.

Said differently: what the AI takes on is not the answer itself, but the choice of the next move toward the answer. That, I think, is a real reframing.

---

## ② It "self-evolves" because it banks experience

So how does it judge whether one more move is needed?

SAGEAgent is designed as an LLM-based clinical agent, and it combines three parts.

The first is a tool that converts numerical predictions into text. Rather than handling model outputs as raw numbers, it translates them into language the LLM can reason over. That is what lets the agent think, in words, about where the current state stands.

The second is episodic memory — machinery for pulling up similar past cases. It can look back at whether, in cases resembling this patient, an additional MRI changed the conclusion or left it untouched.

The third is semantic memory, a layer that accumulates reusable decision patterns from experience. It does not merely stockpile individual cases; it distills them into forms of judgment — "in a situation like this, no further test is needed" — and keeps those.

The "self-evolving" in the name comes from that third part. The more it is used, the more decision patterns pile up. It is built so that operating it, and accumulating data, makes it smarter.

The result: experiments on a glioma cohort combining TCGA-LGG, TCGA-GBM, and BraTS cut average acquisition burden by 55% while maintaining competitive survival prediction accuracy.

Roughly halve the testing without giving up accuracy. The health-economic weight of that one sentence is, frankly, large.

---

## ③ How a hospital could try it: departments and KPIs

So how would you actually try this? Here is my own rollout scenario.

The aim is to embed it into the diagnostic workflow of a university hospital or cancer center as a "first-pass test-necessity engine." Feed it the existing clinical information and it returns a prioritized suggestion: this patient already has enough to decide; this patient is one where an additional MRI would likely change the conclusion. The physician looks at that and makes the final call.

The departments I have in mind: first, hospital management, who can finally talk about test-cost optimization in numbers. Next, the diagnostic departments — radiology and pathology — who can steer scarce imaging slots and reading capacity toward the patients where it actually matters. Then the cancer center's clinical support office, which builds each patient's testing plan and is the most direct beneficiary. And the medical IT department, which owns the connection to the EHR and ordering systems.

For KPIs I would propose these. First, the reduction rate in average diagnostic test cost per patient. Second, a drop in the unnecessary-test rate (looking back, how many tests that did not change the conclusion were avoided). Third, shorter lead time to completing the diagnostic flow. And fourth, the retention rate of predictive accuracy — whether a survival metric like C-index still holds up after the cuts.

That fourth one matters most. Look at cost alone and the logic degenerates into "fewer tests is always better." Pairing it with an accuracy-retention KPI is what makes the system something a clinical team can actually accept.

On sequencing: do not put it into live operation on day one. Run it retrospectively on past cases first, and check whether the tests the AI deemed unnecessary really did fail to change the conclusion. Once those numbers convince people, move to prospective use as a suggestion to the physician. The final judgment always stays with a human. Medicine does not permit failure, so erring on the side of over-caution is exactly right here.

---

## Any job with a cost to going and getting information

And here, maybe, is the real point.

Is this idea only about medicine?

Take credit underwriting. You are constantly deciding whether to request one more document. If the information in hand will not move the conclusion, that request is pure loss — it only drives applicants to abandon the application. If AI can estimate whether one more page would actually flip the decision, underwriting lead time drops.

Take asset maintenance. Do you run an additional non-destructive inspection, or is the existing sensor data enough? Inspection carries downtime cost. If you can judge that a machine's condition is already sufficiently visible, you can steer inspection capacity toward the equipment that is genuinely at risk.

Take market research. Do you run more interviews, or can you decide on the data you have? How many users do you test with? Same structure, every time.

What they share is that acquiring information itself has a cost. And in most organizations, the decision of whether to acquire is made on experience and gut. Usually too much. Occasionally too little.

What SAGEAgent shows is that this decision can itself be treated as a learnable object. And with episodic and semantic memory, past judgments accumulate as an asset.

If you want to try it in your own company, I think there is one thing to do first. Count, from your past logs, the information you went and got that did not change the conclusion. The extra documents requested. The extra inspections run. The extra interviews held. What fraction of them actually moved a decision?

The moment that number exists, the room to cut becomes visible.

AI's place is not only in squeezing out another accuracy point. It is also in the move just before that — deciding whether to go get the data at all. This paper made me feel that quite strongly.

That is it for today!

---

## References

1. Qu, Chongyu, Cui, Can, Lu, Zhengyi, Zhu, Junchao, Yao, Tianyuan, Guo, Junlin, Xiong, Juming, Zhu, Yanfan, Yang, Yuechen, Landman, Bennett A., & Huo, Yuankai (2026). *SAGEAgent: A Self-Evolving Agent for Cost-Aware Modality Acquisition in Multimodal Survival Prediction*. arXiv preprint. https://arxiv.org/abs/2607.09521

<p class="ai-notice"><small>* This article was written in part with AI assistance and may contain inaccuracies.</small></p>
