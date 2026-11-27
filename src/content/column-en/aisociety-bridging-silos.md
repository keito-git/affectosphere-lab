---
title: "Why Do Emotion Labels Break Down Between Data and Society?"
subtitle: "Bridging the Silos in Affective AI: A Critical Perspective from Data to Society"
date: "2026-11-27"
excerpt: "A position paper that rereads affective AI as a six-layer chain from theory to data, models, interaction, applications and ethics, identifies four disconnections that recur at the layer boundaries, and proposes five design criteria in response. A walk-through of our AI & Society paper."
readingMinutes: 12
showImage: false
image: "/column-images/aisociety-bridging-silos/pipeline.png"
imageAlt: "The six-layer pipeline of affective AI, from L1 theory to L6 ethics and evaluation, with the four silo-bridge patterns at the layer boundaries."
authors:
  - name: "Keito Inoshita"
    url: "/en/about/"
    affiliation: "Kansai University"
tldr: "Most surveys of affective AI cover one or two layers, such as data or models. This paper rereads the field as a six-layer chain of dependencies and diagnoses four disconnections that recur at the layer boundaries: theory and data, modeling and interaction, technology and ethics, and data and social application. The four are not independent. Upstream disconnections enable downstream ones, forming a cascade. In response, the paper proposes five design criteria (DC1–DC5) that must be met together, plus four action items, and argues that the cascade carries social consequences: a threat to people's authority over their own emotions, pressure toward machine-legible expression, and a shift of power to institutions. The paper introduces no new experimental data."
links:
  - label: "Paper (AI & Society)"
    url: "https://doi.org/10.1007/s00146-026-03324-y"
citation: |
  @article{inoshita2026bridging,
    title   = {Bridging the Silos in Affective {AI}: A Critical Perspective
               from Data to Society},
    author  = {Inoshita, Keito},
    journal = {AI \& Society},
    volume  = {41},
    number  = {11},
    pages   = {11179--11225},
    year    = {2026},
    doi     = {10.1007/s00146-026-03324-y}
  }
---

<div class="teaser">
<div>

Diagnose

**Four disconnections** recur at the layer boundaries: theory–data, modeling–interaction, technology–ethics, data–application.

</div>
<div>

Cascade

The four are linked. **Upstream gaps enable downstream ones**, so fixing one spot only moves the problem.

</div>
<div>

Prescribe

**Five design criteria (DC1–DC5)**, met together. The last one, DC5, keeps the person as the final interpreter of their own emotion.

</div>
</div>

## Do emotion labels keep their meaning across layers?

Affective computing now spans emotion theory, multimodal data, models, human–AI interaction, applications such as healthcare and education, and ethics and regulation. One assumption has gone largely unexamined throughout: that **emotion labels and scores produced in one layer can be passed downstream** into dialogue generation, intervention, decision support and deployment without friction.

The paper argues that this assumption no longer holds, for three reasons.

- LLMs and multimodal foundation models are changing annotation, recognition and generation at the same time.
- Emotion recognition has left the lab. It is embedded in education, healthcare, employment and dialogue agents, where its outputs shape user experience and institutional decisions.
- Regulation is tightening. The 2024 final text of the EU AI Act prohibits emotion recognition in workplaces and education and classifies related uses as high-risk.

Existing surveys mostly organise the field within one layer or task, such as recognition, multimodality or conversation. Of the 11 representative surveys the paper compares, none treats inter-layer dependence as its central object (one does so partly), and two take a prescriptive stance toward the field.

<figure>
  <img src="/column-images/aisociety-bridging-silos/prior-surveys-1600.webp" alt="Positioning against 11 prior surveys" />
  <figcaption><strong>Figure 1.</strong> Positioning of 11 prior surveys, from Table 1 of the paper. Top: does the survey treat cross-layer dependence as central? Bottom: does it propose a prescriptive program? The scoring rubric is published in the paper's appendix.</figcaption>
</figure>

The paper does not aim to be another comprehensive survey. It is a position paper that **diagnoses a structural problem of the field and derives design-level responses** from that diagnosis.

## How the argument is built: a six-layer chain

<figure>
  <img src="/column-images/aisociety-bridging-silos/pipeline-1600.webp" alt="Six-layer pipeline model" />
  <figcaption><strong>Figure 2.</strong> The six-layer pipeline model (Figure 1 of the paper). The left arrows show the flow from L1 to L6; the red dotted brackets on the right mark the structurally weak connections, i.e. the four patterns.</figcaption>
</figure>

The paper splits the field into six layers. It treats them not as a flat taxonomy but as **a chain in which upstream choices propagate downstream**.

| Layer | Content | Passed to the next layer |
|---|---|---|
| L1 Theory | Discrete, dimensional, appraisal, constructionist | The emotion vocabulary that data collection uses |
| L2 Data | Corpora, labeling schemes, ecological validity | The training and evaluation target of models |
| L3 Modeling | Feature extraction, multimodal fusion, LLMs | Recognition and generation systems |
| L4 Interaction | Affective dialogue, user acceptance, long-term relationships | The form in which systems are used |
| L5 Applications | Healthcare, education, public sector and others | Real-world impact |
| L6 Ethics and evaluation | Bias, regulation, societal risk | Auditing and feedback to upstream layers (cross-cutting) |

The four patterns were identified in three steps. First, the paper mapped the translation points at which one layer's output becomes the next layer's input. Second, for each layer pair, it checked in the literature whether the upstream output format, metric or theoretical assumption fits what the downstream layer needs. Third, it grouped misalignments that share the same mechanism into four patterns. Boundaries with only sporadic or resolved misalignment were not made into patterns.

## Argument 1: Four silo-bridge patterns

<p class="experiment-label">Argument 1</p>

Each pattern is written in the same format: definition, evidence, the mechanism that enables the next pattern, and counter-arguments with rebuttals. The goal is to make the diagnosis falsifiable rather than rhetorical.

| Pattern | What is misaligned | How it enables the next pattern |
|---|---|---|
| P1 Theory ↔ Data | A label scheme is an implicit commitment to an emotion theory, and it enters the corpus unexamined | No theoretically coherent objective can be defined, so models fall back on proxy metrics such as accuracy and F1 |
| P2 Modeling ↔ Interaction | Models are optimised on aggregate metrics; interaction is judged by satisfaction, trust, behaviour change and well-being. The units differ | Effects that do not map onto the proxy (dependence, manipulation, loss of autonomy) become invisible, and ethics is pushed into post-hoc auditing |
| P3 Technology ↔ Ethics | Ethics is post-processing, not a design constraint. The issue is not only misclassification but influence and control when inference is accurate | Harm is found only after deployment, and fixes there cannot reach upstream commitments |
| P4 Data ↔ Application | Evaluation assumptions at data collection (classification accuracy) differ structurally from deployment outcomes (symptom improvement, learning, safety) | The end of the cascade, where P1–P3 show up together |

<figure>
  <img src="/column-images/aisociety-bridging-silos/cascade-1600.webp" alt="Cascade among the four patterns" />
  <figcaption><strong>Figure 3.</strong> The cascade among the four patterns (figure from the paper). Solid arrows: an upstream pattern structurally enables the next. Dashed arrows: P1–P3 manifest together in P4.</figcaption>
</figure>

For P1, the paper points to datasets such as AffectNet that attach discrete labels and continuous valence–arousal values at the same time. The two rest on different ontologies, so a model learns several incompatible representations rather than one coherent concept of emotion. The paper calls this state **unreconciled coexistence**.

The paper also answers objections. To "theoretical pluralism is healthy", it replies that pluralism is healthy only when the data-level commitments are stated and reconciled. To "large-scale LLM annotation will dissolve the problem", it replies that scale captures labels but not the distributional structure of human judgements.

The conclusion is that **closing a downstream pattern while its upstream cause remains only relocates the problem**. This is why the paper asks for an interlocking set of design criteria rather than point fixes.

## Argument 2: Existing bridging attempts and their limits

<p class="experiment-label">Argument 2</p>

The paper does not claim that the field has done nothing. There are many partial bridging attempts. The question is whether any of them closes the cascade as a whole.

| Attempt | Mainly reaches | What remains |
|---|---|---|
| Datasheets, data statements, model cards | P1, part of P3 | Declaring a theoretical commitment stays optional; the unit mismatch of P2 is untouched |
| Emotion-AI ethics sheets and ethics-by-design | P3 | Does not reach the upstream theory that licenses the labels |
| Data-cascade analysis | P4, part of P1 | Not tied to theory (L1) or interaction (L4); no integrated design response |
| Foundation-model integration | Several, unaudited | Merging functions without merging theory, evaluation units and accountability moves the silos inside the model, where they are harder to audit |
| Empathic-dialogue corpora and benchmarks | P2 | Rated empathy is still a proxy for the user-side outcome |

Each attempt closes part of one pattern; none closes the cascade. The paper positions its contribution not as a new bridging artifact but as **the structural argument that fragmented bridging cannot succeed, and the program that follows from it**.

## Argument 3: The social stakes of the cascade

<p class="experiment-label">Argument 3</p>

At the end of the chain are systems that infer and act on human emotion. The same disconnections that reduce accuracy therefore also change the social conditions under which people feel, express and are recognised in their emotions. The paper names three axes.

- **Emotional agency.** When an upstream label fixes what a person "really" feels and downstream systems act on it, the person loses their standing as the interpreter of their own emotion. This is not reducible to privacy; it is about who may say what a feeling is.
- **Algorithmic conformity.** When only machine-legible affect is registered and rewarded, the range of expression a society makes visible shrinks. This is a cultural harm distinct from any single misclassification.
- **Institutional power.** The authority to define and respond to emotion moves from persons to the employers, platforms, schools, clinics and states that operate these systems. The paper treats this as a structural consequence of the cascade, not an incidental abuse.

<figure>
  <img src="/column-images/aisociety-bridging-silos/stakes-1600.webp" alt="Socio-philosophical stakes and design criteria" />
  <figcaption><strong>Figure 4.</strong> The three stakes and the design criteria that answer them, drawn from Section 8.6 and Section 9 of the paper. DC5 answers emotional agency directly and is described as also holding the other two stakes in check.</figcaption>
</figure>

## Argument 4: Five design criteria and four action items

<p class="experiment-label">Argument 4</p>

As the prescription, the paper proposes five design criteria. They are not options to pick from but requirements to be met together.

| Criterion | Idea | Example requirements |
|---|---|---|
| DC1 Theory-explicit affective representation | Declare the emotion theory a dataset or model adopts | Declare the theory; document when a label holds; under a constructionist stance, keep annotator distributions, uncertainty, context and cultural background |
| DC2 Affective reasoning with bounded intervention | Treat emotion as an intermediate representation in reasoning, not an output label | Make explicit how an inference is reached and which intervention it feeds; for personalisation, fix at design time what is stored, for how long and for what |
| DC3 Longitudinal interaction-in-the-loop evaluation | Do not evaluate on single-session accuracy alone | Measure experience, trust, dependence risk and behaviour change; evaluate over periods that match the use (e.g. weeks to months for mental-health support) |
| DC4 Deployment-specific affective accountability | State for whom, in which institution and toward which outcomes a system is used | In high-risk domains: pre-registered protocols, population representativeness, follow-up, connection to human support, responsibility on failure |
| DC5 User-retained interpretive authority | Design systems to support a person's own interpretation, not to fix their emotion | Present inferred emotions so users can correct, reject or reinterpret them; audit how long-term affective data shape a person's self-image |

<figure>
  <img src="/column-images/aisociety-bridging-silos/dc-matrix-1600.webp" alt="Mapping between design criteria and patterns" />
  <figcaption><strong>Figure 5.</strong> Mapping between design criteria and patterns, redrawn from the paper's table. "primary" is the pattern each criterion was formulated for, "secondary" the downstream support stated in Section 9, "indirect" a contribution only through the cascade. No criterion is sufficient alone; closing all four patterns needs the full set.</figcaption>
</figure>

Four action items translate the criteria into research practice.

1. **Theory-grounded dataset design (DC1).** When choosing a label scheme, declare which theory it instantiates and why that theory fits the population and deployment context. Record annotator confidence and label ambiguity.
2. **Deployment evaluation in benchmarks (DC2, DC3).** Alongside offline accuracy, report at least one of: user-felt empathy, turn-level satisfaction, ecological validity in a simulated deployment, or longitudinal outcomes.
3. **Ethical auditing in the development pipeline (DC1, DC5).** Make demographic bias audits standard, place ethical checkpoints before data collection, and give users a way to correct or reject inferred emotions.
4. **Field evaluation protocols (DC4).** In healthcare, education and public safety, fix in advance the outcome metrics, population, period, minimum sample size, and recourse and responsibility on failure.

The paper frames these not as endpoints to be met at once but as directions to be advanced step by step.

## What we know and what we don't

The paper establishes three points.

- Many problems in affective AI are better described not as defects of individual layers but as **four disconnections that recur at layer boundaries**.
- The four form a chain from upstream to downstream, so **a single local fix only moves the problem**.
- The response needs five criteria met together, anchored by the principle that **a person remains the final interpreter of their own emotion** (DC5).

There are limits. This is an argument built on published literature; it introduces no new data or models. The comparison with prior surveys was scored by the author with the appendix rubric and without an independent second coder, so inter-rater reliability was not measured. The 11 surveys were chosen as representative, not exhaustive. The paper also presents the five criteria not as a finished solution but as directions that future work should advance incrementally.
