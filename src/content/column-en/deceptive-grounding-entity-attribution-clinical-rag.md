---
title: "What if an answer that passed every hallucination check was actually about a different drug? — deceptive grounding in clinical RAG"
date: "2026-07-13"
excerpt: "The citation is real. Faithfulness is high. Hallucinations: zero. And yet you asked about drug X and got back clinical evidence for drug Y. Standard metrics cannot see this failure. Across 13 models, deceptive-grounding rates hit 8-87% under adversarial conditions, and 86.7% for a domain-specialized model. Here is how pharmacovigilance and medical information teams could add an entity-attribution audit layer — departments and KPIs included."
image: "/column-images/deceptive-grounding-entity-attribution-clinical-rag.png"
imageAlt: "Flat illustration of a drug information RAG answer screen where hallucination, faithfulness, and citation-existence checks all show green, while the cited evidence belongs to a different drug than the one queried"
readingMinutes: 5
basedOnPaper: "Deceptive Grounding: Entity Attribution Failure in Clinical Retrieval-Augmented Generation"
basedOnPaperUrl: "https://arxiv.org/abs/2607.09349"
---

Hello. I am Miura from Affectosphere Group.

If you run a RAG system in-house, let me ask you to imagine something unpleasant.

You ask about the side effects of drug X. The answer comes back with a citation attached. The cited document really exists. The content is faithful to that document. Run it through your hallucination detector and you get zero warnings. Every check is green.

But the evidence was about drug Y.

A study published on arXiv (Caruzzo, Yoo & Kim, arXiv:2607.09349) gives this failure mode a name: deceptive grounding, or DG. The frightening part is that existing evaluation metrics cannot detect it at all.

Today I want to look at this from a business-application angle and think about how a real team could fold it into an audit pipeline. And I think this matters far beyond medicine — it touches every company running RAG internally.

---

## Three takeaways

1. RAG evaluation checks whether a claim is grounded in the retrieved documents, but not whether that evidence is attributed to the right entity. So evidence about drug Y, presented as evidence for drug X, sails straight through the zero-hallucination, high-faithfulness, real-citation checks.
2. In a controlled benchmark across 13 models, DG rates under adversarial conditions ran from 8% to 87% — including 86.7% for a domain-specialized model. A model tuned for medicine is not automatically the safer one.
3. On the other hand, entity attribution verification detected it with 97.0% precision and 98.7% recall. It is a detectable failure — which means it is worth building as an audit layer.

---

## ① "Grounded" and "grounded in the right entity's evidence" are different things

First, let me lay out the structure of the problem.

What RAG evaluation looks at today is roughly three things. Is the model's claim actually stated in the retrieved document (faithfulness)? Did it invent a document that does not exist (citation existence)? Did it add content the document never contained (hallucination)?

All three matter. But look closely and they only ever examine the space between the document and the answer. Nobody verifies whether that document is about the entity the user actually asked about.

That is the hole. Take genuine clinical data written about drug Y, and present it as the answer for drug X. The document exists. The content is faithful to it. Nothing was fabricated. Every check passes. And the answer is completely wrong.

Hence "deceptive." The model is not lying. It is pasting correct information onto the wrong subject — and nothing anywhere in the evaluation pipeline is watching for the swap.

What chilled me most on reading this is that going undetected is, in effect, built into the design. The harder you work on hallucination defenses, the more you accumulate a false sense of safety: everything is green, so we must be fine.

---

## ② What a range of 8% to 87% really tells you

The paper builds a controlled benchmark across 13 models. Under adversarial conditions, DG rates ranged from 8% to 87%.

The sheer width of that range is unsettling. Depending on the model, you get anything from almost never tripping to being wrong nearly nine times out of ten. Which means your model choice maps directly onto how large your drug-mix-up risk is — and existing metrics render that difference invisible.

More troubling still is the 86.7% figure for a domain-specialized model. A model trained specifically for the medical domain showed a high DG rate. Intuitively you want to believe that medical specialization means safety. It does not necessarily.

This next part is my own speculation, but a domain-specialized model is strongly adapted to the phrasing of clinical text, and so it is also very good at integrating retrieved clinical evidence in a way that reads plausibly. I suspect that very smoothness may work in the direction of papering over the entity mismatch.

Either way, the practical implication is simple. "It is a medical-specialized model, so we are safe" does not survive this paper as a vendor selection criterion. Unless you explicitly measure entity attribution, you have no idea which model is how dangerous.

---

## ③ How to try it on the floor: an entity-attribution layer, departments and KPIs

So how do you handle this in your own organization? From here on, this is my own rollout proposal.

There is one thing to do: add an entity attribution verification layer to your existing RAG audit pipeline.

Most in-house RAG systems today look like this: retrieve, generate, hallucination check, output. What you insert — alongside the hallucination check, not instead of it — is a step that asks whether the evidence this answer pulled belongs to the entity the user queried. The paper shows this verification detects the failure at 97.0% precision and 98.7% recall. That is a solid enough level to implement as an audit layer.

Here are the departments I have in mind. First, pharmacovigilance. If you use an internal RAG to field adverse-event queries, a drug mix-up leads straight to a patient safety incident. Next, drug safety evaluation and medical information teams — the desks that return drug information to clinicians, where mechanically guaranteeing who the evidence belongs to carries real weight. And hospital information systems departments: if you operate a drug information RAG inside a hospital, this verification layer is going to become effectively mandatory.

For KPIs, so you can tell the story in numbers, I propose the following. First, the rate of incorrect drug information served — the DG rate itself. Measure how far your own pipeline's DG rate falls before and after adoption. Second, the automation rate of safety audits (the share the machine can triage without escalating to human review). Third, reporting accuracy to regulators, and the count of patient safety incidents. For the first one especially, you can take this paper's benchmark approach straight into your own internal evaluation and get a pre-adoption baseline.

And here is the real point: this is not only about medicine.

In finance, you ask for company A's earnings figures and get company B's. In legal, you ask about a clause in contract C and the clause cited comes from contract D. In HR, you ask about the scope of policy E and out comes the scope of policy F. Every one of these passes hallucination detection — because the document exists and the content is faithful to it.

If you have deployed RAG, I would urge you to revisit your audit checklist. "It passed hallucination detection" does not mean "the evidence belonged to the right entity." Those are two different checks.

---

## Sometimes "all green" is the most dangerous state

What I took from this study is that an evaluation metric only protects what it measures.

Measure hallucination and hallucination goes down. But whatever you are not measuring quietly stays — and because every check is green, it gets harder, not easier, to notice. This paper names that blind spot and shows it can be measured properly. A failure with a name is a failure you can defend against.

Incidentally, this question of "is it attributed to the right subject" is continuous with the affective AI we work on. Whose emotion is it, and in which context — an emotion estimate attributed to the wrong subject is meaningless no matter how sound its content. Verifying attribution is, I feel, an unavoidable question in affective AI too.

Take another look at your RAG audit checklist. All green does not mean it was about the one you asked about.

That is it for today!

---

## References

1. Caruzzo, Cedric, Yoo, Donggeun, & Kim, Tae Soo (2026). *Deceptive Grounding: Entity Attribution Failure in Clinical Retrieval-Augmented Generation*. arXiv preprint. https://arxiv.org/abs/2607.09349

<p class="ai-notice"><small>* This article was written in part with AI assistance and may contain inaccuracies.</small></p>
