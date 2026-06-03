---
title: "Emotion-AI Projects Probably Die in the Gaps Between Layers"
date: "2026-06-01"
excerpt: "Most enterprise emotion-AI projects fail not because of technology, vendors, or the field, but because responsibility falls into the gaps between layers. A six-layer model, five design criteria, and the concept of emotional sovereignty — a 5-minute read for executives."
image: "/column-images/five-silos.png"
imageAlt: "Six-layer emotion-AI pipeline stacked vertically with amber bridges connecting the layers"
readingMinutes: 5
basedOnPaper: "Bridging the Silos in Affective AI: A Critical Perspective from Data to Society"
basedOnPaperUrl: "https://arxiv.org/"
---

> _This article is an English translation of the original Japanese column. Some phrasing has been adapted for English readers._

Hello, this is Inoshita from Affectosphere Group.

Over the last few years I've had more chances to talk with people at big enterprises who want to bring in emotion AI. The conversation usually starts like this.

"We want to deploy emotion AI too, but I'm afraid it's going to blow up on us."

That, I think, is a fairly correct instinct.

But when I ask what they are actually afraid of, the answer splits in interesting ways. Engineering says "we can't get the accuracy." UX says "users call it creepy." Legal says "we can't read the regulations." The C-suite says "we don't know who owns the risk."

In other words, emotion-AI projects don't die because "the tech is bad," "the vendor is bad," or "the field is bad." They die in the gap between layers.

The position paper [^1] we posted on SSRN in 2026 tackles this structure head-on.

The conclusion up front:

"See emotion AI as a six-layer pipeline. The ability to close the responsibility gaps between layers — that is the next competitive axis."

Today I want to write this for AI strategy leads, CTOs, and product owners.

[^1]: Keito Inoshita, "Bridging the Silos in Affective AI: A Critical Perspective from Data to Society", SSRN preprint, 2026.

---

## Today's takeaway in 3 lines

1. Value: see emotion AI as a six-layer stack and, for the first time, you can see where you are strong and where the holes are. Requirements get sharper fast.
2. Pitfall: most projects fail not on any single layer's technology, but in the gap between layers, where responsibility falls. Tech investment alone will not fix this.
3. Hidden point: "leave the final right to interpret your emotions with the user" — the idea of emotional sovereignty — can become a competitive message.

In order.

---

## ① The view: emotion AI as a six-layer pipeline

The paper's starting move is to stop treating emotion AI as a single technology and to see it as a stack of six layers.

- Theory layer: which emotion theory you adopt (Ekman's six basic emotions? Plutchik's wheel? PAD model?)
- Data layer: which labeled corpora you use
- Model layer: which ML design
- Dialogue layer: how output is presented to the user
- Social-application layer: which business context you deploy in
- Ethics / evaluation layer: who is accountable

The executive-level question is whether your organization can clearly say, for each of those six layers, "which parts do we own internally, which parts do we delegate to vendors, and which parts have quietly remained empty?"

In many organizations, operations launched while cross-layer responsibility was still ambiguous.

When something then goes wrong, you discover that nobody is the final owner. That is the typical emotion-AI blowup.

---

## ② What happens in the gaps between layers

The paper identifies four recurring disconnection patterns — "silo bridges" — between layers.

First, operationalization drift between theory and data.
What the chosen theory calls "joy" and what the data labels call "joy" do not match in definition. Looks small, but this is why "AI verdicts don't match the field" in operations.

Second, cognitive mismatch between model and dialogue.
The model's output (say "anger 0.87") and the user's interpretive frame fail to engage. A UI where you cannot tell "is 0.87 strong?" confuses users.

Third, dissipation of responsibility between technology and ethics.
When something goes wrong, accountability across layers becomes unclear. Vendor, UX agency, internal business unit, external auditor — everyone says "that is outside our scope."

Fourth, implicit representativeness assumption between data and social application.
Data collected from a specific population (English-language, younger, social-media text) is silently treated as universal truth. The model underperforms on older regional customers, but operations run on the vendor's quoted accuracy.

In business language: these are all topics that fall through the cracks of your contracts and become inevitable post-launch fires.

---

## ③ The emotion-AI angle: emotional sovereignty

This is the point Affectosphere Group most cares about.

The paper proposes five Design Criteria (DC1-5), and at the core sits DC5 — preservation of users' interpretive authority.

In plain language:

> The final right to interpret, record, and disclose one's own emotions belongs to the person experiencing them.

We call this emotional sovereignty.

Why it matters: when emotion AI says "you are angry," the design has to keep room for the user to say "no, that's not what I'm feeling." That room has to be built in at the design stage.

A relationship where a machine unilaterally declares "this is your emotion" creates an asymmetric power dynamic between humans and AI. The paper positions emotional sovereignty as an extension of the right to self-determination in medicine and the right to informational self-control in data protection — a new human-rights concept for the age of emotion AI.

And it works as a business move.

"Our emotion AI leaves the final right to interpret your emotions with you" — that message is a meaningful trust advantage against competitors who decide your customers' emotions inside a black box.

Especially in mental health, education, and HR — domains where you intervene in users at vulnerable moments — an explicit emotional-sovereignty stance becomes a brand asset.

---

## So what do you do starting tomorrow

Three things you can act on.

- Six-layer mapping: map your emotion-AI initiatives onto the six-layer model. Seeing "which layer is ours, which is vendor, which is empty" at a glance accelerates the first conversation dramatically.
- Two required disclosures from vendors: make the adopted emotion theory and the training-data composition (region, age, language, medium) mandatory disclosures. Those two alone go a long way toward defusing operationalization drift and the representativeness assumption.
- Turn DC1-5 into a governance checklist: "Is the chosen emotion theory documented? Are intervention boundaries defined? Is there a longitudinal-evaluation plan? Is deployment-specific accountability clear? Is user interpretive authority preserved?" Make these five questions standard review items for every emotion-AI initiative.

And if you sit anywhere near customer-facing messaging, try drafting an "emotional sovereignty statement" once. Writing it surfaces how unclear your stance on customers' emotions actually is.

---

## Closing

Competition in emotion AI is no longer competition on model accuracy.

Theory, data, model, dialogue, social application, ethics — the ability to design across these six layers, the ability to close the responsibility gaps between them, is what decides whether the product wins.

And at the core of that design should sit —

The final right to interpret a user's emotion stays with the user.

This is a technology argument and a business judgment at the same time, and ultimately it is a question about how to design the relationship between humans and AI in the age of emotion AI.

Our lab wants to answer this from the technology side.

So — that is it for today.

"Which of the six layers in our emotion AI has the hole?" If that question makes it onto the agenda of your next AI strategy meeting, this column has done its job.

---

## References

1. Keito Inoshita (2026). *Bridging the Silos in Affective AI: A Critical Perspective from Data to Society*. SSRN preprint.

<p class="ai-notice"><small>* This article was written in part with AI assistance and may contain inaccuracies.</small></p>
