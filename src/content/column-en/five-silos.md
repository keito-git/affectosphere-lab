---
title: "The Five Silos of Emotion AI — A Design Strategy for Executives"
date: "2026-05-31"
excerpt: "Most enterprise emotion-AI projects stumble not on technology but on the responsibility gaps between layers. A new position paper offers a six-layer model and five design criteria — a 5-minute read for AI strategy leads, CTOs, and product owners."
image: "/column-images/five-silos.svg"
imageAlt: "Six-layer emotion-AI pipeline stacked vertically with amber bridges connecting the layers"
readingMinutes: 5
basedOnPaper: "Bridging the Silos in Affective AI"
basedOnPaperUrl: "https://arxiv.org/"
---

> _This article is an English translation of the original Japanese column. Some phrasing has been adapted for English readers._

## Why "the silos of emotion AI" is a management problem

You have probably seen the failure pattern. The engineering team ships a high-accuracy emotion model, UX wraps it in a clean interface, the business unit slots it into operations — and a few months later three different problems erupt in three different layers: "the emotion labels do not match what our front-line staff feels," "customers are complaining that this feels invasive," "the regulator is asking how we align with AI ethics guidelines."

This is not a project-level failure. It is the structural consequence of emotion AI having grown up as a collection of specialist silos. Six layers — theory, data, model, dialogue, social application, and ethics — each evolved inside a different academic community and a different industrial function. The result is responsibility gaps wherever two layers meet.

A 2026 position paper [^1] submitted to AI and Society confronts this structure head-on and offers four named "silo bridges" and five Design Criteria (DC1-5). This column re-reads it as decision material for AI strategy leads, CTOs, and product owners.

[^1]: Keito Inoshita, "Bridging the Silos in Affective AI", AI and Society (submitted), 2026.

---

## Three facts the research established

### 1. Emotion AI is a six-layer pipeline

The paper's starting move is to stop seeing emotion AI as a single technology and to see it instead as a stack of six layers: a theory layer (which emotion theory you adopt), a data layer (which labeled corpora you use), a model layer (which ML design), a dialogue layer (how output is presented to the user), a social-application layer (which business context you deploy in), and an ethics/evaluation layer (who is accountable).

The executive-level question is whether your organization can clearly say, for each of those six layers, which parts you own internally, which parts you delegate to vendors, and which parts have quietly remained empty inside the company. In many organizations, operations launched while responsibility ownership across layers was still ambiguous.

### 2. There are four recurring "silo bridges" between layers

The paper identifies four disconnection patterns that recur at the seams between layers.

First, operationalization drift between theory and data — what the chosen theory calls "joy" and what the data labels call "joy" do not match in definition. Second, cognitive mismatch between model and dialogue — the model's output interpretation and the user's interpretive frame fail to engage. Third, dissipation of responsibility between technology and ethics — when something goes wrong, accountability across layers becomes unclear. Fourth, an implicit representativeness assumption between data and social application — data collected from a specific population is silently treated as universal truth.

In business language: these are the topics that fall through the cracks in your contracts and become the inevitable post-launch fire.

### 3. Five Design Criteria (DC1-5) become a cross-cutting common language

The core contribution is a set of five criteria that cut across all the layers rather than optimizing within one.

DC1, theory disclosure, requires the adopted emotion theory to be explicit in both paper and implementation. DC2, intervention boundaries, requires the legitimate scope of emotion-AI intervention to be defined in advance and enforced by design. DC3, longitudinal evaluation, makes effects over time, not single-moment accuracy, essential. DC4, deployment-specific accountability, requires that "who is responsible for what" be stated separately for research prototypes, field trials, and commercial deployment. DC5, preservation of users' interpretive authority, retains the final right to interpret AI output with the user.

The five are designed not as independent rules but as a mutually reinforcing normative system. At the heart of DC5 sits the concept of "emotional sovereignty" — the final right to interpret, record, and disclose one's own emotions belongs to the person experiencing them.

---

## What this research tells the business leader

Three takeaways.

1. Emotion-AI deployments fail less because a particular layer's technology is weak, and more because responsibility falls into the gap between layers. Technology investment alone will not fix it.
2. Vendor selection, internal team design, and operational governance should be redesigned around "where is the hole in the six-layer stack?" as the framing question.
3. The five Design Criteria (DC1-5) work as-is as a checklist for internal AI governance.

From here, move in two registers: risk management and value creation.

---

## Risk management: three areas to act on now

### Risk 1: Responsibility gaps — fires that fall through the contract

A typical emotion-AI deployment involves four to six parties: technology vendor, UX agency, internal business unit, external audit, and so on. When something goes wrong, everyone says "that is outside our scope." What the paper calls "responsibility dissipation" plays out in everyday contracts and operations.

What to do: Map every emotion-AI-related contract you hold onto the six-layer model and write into the contract — and into the runbook — who is the first responder when a problem in each layer surfaces. For any layer that comes up empty, assign an internal owner.

### Risk 2: Operationalization drift — when "emotion labels" do not match the field

Every vendor's emotion AI is built on some specific theory (Ekman's six basic emotions, Plutchik's wheel, the PAD model, and so on) and inherits the ontology that comes with it. But your operational context may critically distinguish "dissatisfaction" from "disappointment," or live with culturally ambiguous expressions (Japanese "kekkō desu" being a classic). Left unmanaged, the operationalization drift the paper names erodes front-line trust in the AI quickly.

What to do: Make "the adopted emotion theory" and "the label definition document" mandatory disclosures from your emotion-AI vendor. Document the gap between the categories your business needs and the label system the vendor ships.

### Risk 3: Representativeness assumption — your customers are not their data

Emotion-AI training data is often skewed toward English-language, younger, social-media text. If your customer base is older, regional, or in a specific vertical, the vendor model will underperform its quoted accuracy. The paper's "representativeness assumption" is something to verify whenever you onboard a vendor model.

What to do: At vendor-selection time, require disclosure of training-data composition (region, age, language, medium). Where the distribution diverges significantly from your customer base, restrict deployment to fine-tuned variants or scoped pilots.

---

## Value creation: three opportunities hidden in the same research

### Opportunity 1: Use the six-layer model as a product-requirements template

At the requirements-definition stage of a new emotion-AI product, simply naming "which of the six layers we intend to make our core competence" sharpens the spec dramatically. Theory? Dialogue-layer UX? Domain knowledge at the social-application layer? Once that is explicit, what should be outsourced is also explicit, and wasted in-house build effort drops.

### Opportunity 2: Operationalize DC1-5 as your AI governance checklist

DC1-5 functions as-is as a checklist for the internal AI ethics committee and product reviews. "Is the chosen emotion theory documented? Are intervention boundaries defined? Is there a longitudinal-evaluation plan? Is deployment-specific accountability clear? Is user interpretive authority preserved?" — asking these five questions on every emotion-AI initiative meaningfully reduces downstream incidents.

### Opportunity 3: Make "emotional sovereignty" a customer message

The DC5 concept of emotional sovereignty also works as a competitive message. "Our emotion AI leaves the final right to interpret your emotions with you" is a meaningful trust signal against competitors who decide your customers' emotions inside a black box. In mental health, education, and HR especially, an explicit emotional-sovereignty stance becomes a brand asset.

---

## A 5-item action checklist for business leaders

Things you can move on tomorrow.

- [ ] Six-layer mapping: map every emotion-AI initiative onto the six-layer model and surface responsibility gaps
- [ ] Operationalization review: document the gap between vendor label definitions and your business's required categories
- [ ] Representativeness audit: measure the divergence between training-data composition and your customer distribution, and re-scope deployment accordingly
- [ ] DC1-5 governance: embed the five Design Criteria as standard review items in your AI governance process
- [ ] Emotional sovereignty statement: draft and publish a user-facing policy that "the right to interpret your emotions stays with you"

---

## Closing — cross-layer design decides the winners

Competition in emotion AI is no longer competition on model accuracy. The ability to design across the six layers of theory, data, model, dialogue, social application, and ethics — the ability, in other words, to close the responsibility gaps between layers — is what decides whether the product succeeds.

Mismanage the risk and technology investment spins in place inside the gaps, surfacing as inevitable post-launch fires. Manage it well and three values appear: sharper requirements, stronger governance, and emotional sovereignty as a new axis of differentiation.

"Which of the six layers in our emotion AI has the hole?" If that question makes it onto the agenda of your next AI strategy meeting, this column has done its job.

---

> This article is a business-oriented rewrite of _"Bridging the Silos in Affective AI"_ (AI and Society, submitted 2026), authored by Keito Inoshita (Affectosphere Group, Kansai University).

<p class="ai-notice"><small>* This article was written in part with AI assistance and may contain inaccuracies.</small></p>
