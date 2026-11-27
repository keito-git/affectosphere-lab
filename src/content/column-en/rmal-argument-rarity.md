---
title: "Are AI Essays Less Original, or Just More Alike?"
subtitle: "Argument Rarity as a Measure of Essay Originality in the Age of AI-Assisted Writing"
date: "2026-11-27"
excerpt: "We propose AROA, which measures how rare an essay's claims, evidence and argument structure are among student essays written for the same assignment. AI essays were not much more typical one by one, but they were strikingly alike as a group. A walk-through of our paper accepted in Research Methods in Applied Linguistics."
readingMinutes: 13
showImage: false
image: "/column-images/rmal-argument-rarity/framework.png"
imageAlt: "The AROA pipeline: an LLM extracts claims, reasons, evidence, counterarguments and rebuttals; structural, claim and evidence rarity and dialogic elaboration are computed and combined with a quality gate into a final score."
authors:
  - name: "Keito Inoshita"
    url: "/en/about/"
    affiliation: "Kansai University"
  - name: "Michiaki Omura"
    affiliation: "Arbege Corporation"
  - name: "Tsukasa Yamanaka"
    affiliation: "College of Life Sciences, Ritsumeikan University"
  - name: "Go Maeda"
    affiliation: "Office of General Education, Ritsumeikan University"
  - name: "Kentaro Tsuji"
    affiliation: "Office of General Education, Ritsumeikan University"
tldr: "Now that LLMs write fluent, well-organised text, quality alone no longer tells whether a student did the thinking. AROA measures how rare an essay's claims, evidence and argument structure are among student essays for the same assignment, as a measure of the novelty facet of originality. Applied to 1,354 student essays and 1,000 GPT-4.1-mini essays, it shows that AI essays are highly homogeneous as a group: their within-group claim diversity is about a third of the students'. Judged one by one against the student population, however, they are not much more typical. Which of the two a rarity score shows depends on the reference corpus. Fabricated evidence also earns high scores, so rarity cannot simply be called originality."
links:
  - label: "Paper (RMAL, accepted)"
    url: "https://lab.affectosphere.group/en/news/20261117-rmal-argument-rarity/"
  - label: "Data (AIDE, Kaggle)"
    url: "https://www.kaggle.com/datasets/lburleigh/tla-lab-ai-detection-for-essays-aide-dataset"
citation: |
  @article{inoshita2026aroa,
    title   = {Argument Rarity as a Measure of Essay Originality in the Age of
               {AI}-Assisted Writing},
    author  = {Inoshita, Keito and Omura, Michiaki and Yamanaka, Tsukasa and
               Maeda, Go and Tsuji, Kentaro},
    journal = {Research Methods in Applied Linguistics},
    year    = {2026},
    note    = {Accepted, to appear}
  }
---

<div class="teaser">
<div>

Separate

AI essays are homogeneous **as a group**: within-group claim diversity is 0.32–0.36 of the students'. One by one, they can be no more typical than students.

</div>
<div>

Corpus

Adding AI essays to the reference corpus widens the claim-rarity gap **from d = 0.47 to 1.58**. The corpus defines what the score means.

</div>
<div>

Limits

Fabricating evidence raises the final score by **+0.405**. Rarity is not validated originality.

</div>
</div>

## Quality no longer tells them apart

LLMs can now write logical, fluent text on almost any topic in seconds. Instructors can no longer reliably tell whether an essay reflects a student's own thinking or an AI reconstruction of typical patterns. As AI text approaches human quality, **quality stops being a signal of authorship or effort**.

Automated essay scoring (AES) has mostly predicted quality: coherence, grammar, organisation. But the purpose of an essay assignment is not good text as such. It is to engage students in critical thinking: forming a view, exploring evidence and answering counterarguments. **Originality at the level of argument components**, meaning which claims are made, which evidence is chosen and how they are structured, is not measured by current AES.

Human raters have limits too. Grading many essays under time pressure brings order effects and fatigue. And judging how rare a claim is across hundreds of essays exceeds human working memory.

## How AROA works

<figure>
  <img src="/column-images/rmal-argument-rarity/framework-1600.webp" alt="AROA framework" />
  <figcaption><strong>Figure 1.</strong> The AROA pipeline (Figure 1 of the paper). Argument elements are extracted on the left; structural and semantic rarity are computed in the middle and dialogic elaboration at top right; a quality adjustment yields the final score.</figcaption>
</figure>

AROA (Argument Rarity-based Originality Assessment) measures **how atypical an essay's argumentation is relative to a reference corpus of student essays for the same assignment**. Creativity research has long operationalised originality as the statistical infrequency of a response; AROA applies this to argument components. The paper states that this captures only the novelty facet of originality and is not, by itself, validated originality.

The steps are:

1. **Extraction.** An LLM (temperature 0) extracts five kinds of elements.

| Element | Content |
|---|---|
| Claims | Central conclusions or assertions |
| Reasons | Arguments that support the claims |
| Evidence | Examples, data or citations backing the reasons |
| Counterarguments | Anticipated opposing views |
| Rebuttals | Responses to counterarguments |

2. **Embedding.** Each element is placed by Sentence-BERT in a space where similar meanings lie close together.
3. **Four sub-scores.** Structural rarity (how unusual a profile of 12 features such as element counts and ratios is), claim rarity and evidence rarity (the complement of mean similarity to the five nearest elements in the reference corpus), and dialogic elaboration (the amount and coverage of counterargument–rebuttal exchange). An essay is never compared with itself or with the example essays shown to the model during AI generation.
4. **Quality gate.** An LLM rates coherence and logical validity on three levels. The four sub-scores are combined, converted to a percentile within the reference corpus, and multiplied by quality. **Lower quality can never raise the score.**

## Experiment 1: Are AI essays more typical than student essays?

<p class="experiment-label">Experiment 1</p>

<div class="setup">

**Setup**

- Student essays: two assignments from the AIDE dataset (Car-free cities 686, Electoral College 668; 1,354 scored). Both are source-based argumentative tasks
- AI essays: 500 per assignment from GPT-4.1-mini, 1,000 in total. The prompt contained the instructions, the source material and three student essays as examples
- Primary protocol: the reference corpus for each assignment is its student essays; both student and AI essays are scored against it

</div>

<figure>
  <img src="/column-images/rmal-argument-rarity/student-vs-ai-1600.webp" alt="Student vs AI effect sizes" />
  <figcaption><strong>Figure 2.</strong> Student–AI differences (Cohen's d; positive means student essays are more atypical). Direction and size depend on the assignment.</figcaption>
</figure>

The clearest difference is quality: AI essays reach 0.998, students average 0.609. Rarity differs much less and depends on the assignment.

- AI claims are more typical than student claims for Car-free cities (d = 0.99) but not for Electoral College (d = −0.01, p = 0.79).
- AI evidence is not consistently more typical (d = −0.38 and 0.12).
- AI argument structures are somewhat more typical in both (d = 0.34 and 0.51).
- Counterargument–rebuttal exchanges appear in 2.6% of AI vs 51.2% of student essays for Car-free cities, but in 100% of AI vs 74.0% of student essays for Electoral College.

Because the gate multiplies by quality, the near-ceiling AI quality carries into the final score, and AI essays score higher overall (d = −0.57). **The final score is not an authorship indicator**; group comparisons must be read alongside the components.

## Experiment 2: Group homogeneity and the reference corpus

<p class="experiment-label">Experiment 2</p>

While individual differences are modest, AI essays are very similar to one another. Computing rarity within each population at matched size (500), AI claim rarity is 0.32 and 0.36 times the student value, and evidence rarity 0.58 and 0.64 times.

<figure>
  <img src="/column-images/rmal-argument-rarity/homogeneity-1600.webp" alt="Within-population homogeneity" />
  <figcaption><strong>Figure 3.</strong> Within-population rarity, AI divided by students (1 = as diverse as students). The main AI essays' claims are about a third as diverse. The two right-hand groups are generation conditions from Experiment 4 (250 each).</figcaption>
</figure>

When AI essays are added to the reference corpus, this homogeneity leaks into individual scores, because AI claims sit close to other AI claims. The mean similarity of an AI claim to its five nearest AI claims is 0.961 and 0.966, against 0.884 and 0.909 for students.

<figure>
  <img src="/column-images/rmal-argument-rarity/composition-1600.webp" alt="Reference-corpus composition" />
  <figcaption><strong>Figure 4.</strong> How the student–AI difference changes with the reference corpus. Mixing in AI essays widens the gap for both claims and evidence.</figcaption>
</figure>

A mixed-corpus rarity score therefore conflates two phenomena: **the homogeneity of the AI population** and **the typicality of an individual argument relative to students**. In a corpus full of AI-assisted submissions, each one is penalised for the homogeneity of the others. That is why the student-only corpus is the primary protocol. The paper recommends reporting the corpus composition, assignment and version with every score, as norm-referenced tests report their norming sample.

## Experiment 3: Can new essays be scored stably?

<p class="experiment-label">Experiment 3</p>

In class, a student's score should not change because later classmates submitted similar arguments. We split the student essays 20 times into a frozen reference half and a held-out half and scored the held-out essays against the frozen half only. Scores matched those obtained inside the corpus (mean Spearman ρ = 0.99 for the final score), and mean percentiles were 0.49 and 0.50, showing no drift.

<figure>
  <img src="/column-images/rmal-argument-rarity/reference-size-1600.webp" alt="Reference corpus size" />
  <figcaption><strong>Figure 5.</strong> Rank agreement of the final score with a smaller reference corpus, compared with a larger corpus from the same cohort.</figcaption>
</figure>

Even with 50 reference essays, rank agreement is 0.91. The paper cautions that this is agreement with a larger corpus from the same cohort, not a general minimum size.

Other robustness checks:

| Check | Result |
|---|---|
| Neighbourhood size (3–50) | Claim rankings ρ ≥ 0.97; the evidence difference changes sign, so it is not interpreted |
| Integration weights (1,000 random sets) | Median rank correlation 0.91 with equal weights |
| Second encoder (all-MiniLM-L6-v2) | Rankings kept (ρ = 0.91–0.93), but the claim gap shrinks to d = 0.25 |
| Other extractors (Gemini, Claude) | Moderate agreement on the final score (mean r = 0.34; 0.56 with quality held fixed) |

## Experiment 4: What if the model is told to be unusual?

<p class="experiment-label">Experiment 4</p>

To check whether AI typicality comes from the imitation prompt, we compared three conditions: C0 repeats the main prompt; C1 tells the model to avoid typical arguments and use uncommon perspectives and evidence; C2 assigns one of 25 student personas.

<figure>
  <img src="/column-images/rmal-argument-rarity/generation-strategy-1600.webp" alt="Generation strategy" />
  <figcaption><strong>Figure 6.</strong> Difference from student essays by generation condition (negative means AI is more atypical). Under novelty-seeking C1, individual essays become rarer than students'.</figcaption>
</figure>

C0 reproduces the main result. Under C1, individual essays become more atypical than students', especially in evidence (d = −1.94). Yet within-group diversity for C1 is still 0.62 and 0.56 of the student level: **the essays converge on a smaller set of unusual arguments**.

Was the rare evidence fabricated? Only 2.7% of C1 evidence consisted of specific facts absent from the source (30.0% for students); 41.7% was general or hypothetical examples. This classification is itself model-based and detects unsourced specificity, not factual error.

## Experiment 5: Is rarity originality?

<p class="experiment-label">Experiment 5</p>

We applied four edits to 100 student essays and measured the change in scores.

<figure>
  <img src="/column-images/rmal-argument-rarity/perturbation-1600.webp" alt="Perturbation test" />
  <figcaption><strong>Figure 7.</strong> Mean change in final score per edit (Wilcoxon signed-rank; * p < .05, ** p < .01, *** p < .001). Fabricated evidence earned the largest gain.</figcaption>
</figure>

- **Paraphrase.** Rarity barely moves, as intended for a meaning-based measure. But any LLM rewrite raises the quality score (+0.243), so the final score rises although no argument changed.
- **Fabricated evidence.** Evidence rarity rises by 0.113, the quality gate does not penalise it, and the final score rises by 0.405.
- **Irrelevant claim vs relevant uncommon argument.** Both raise the score only slightly, and the two are not distinguished.

Other validity checks:

| Check | Result |
|---|---|
| Agreement with counts of equivalent claims | Higher claim rarity, fewer judged equivalents (ρ = −0.32, p < .01) |
| One experienced instructor rating 120 essays for originality | Final score ρ = 0.33, carried mainly by dialogic elaboration (ρ = 0.38); no significant link for the three rarity components |
| Same rater, retest after more than three months | Originality ρ = 0.42, quality ρ = 0.64 |

<figure>
  <img src="/column-images/rmal-argument-rarity/expert-1600.webp" alt="Expert ratings" />
  <figcaption><strong>Figure 8.</strong> Rank correlations with one instructor's originality ratings. Within-strata values remove the range extension caused by stratified sampling and are the conservative estimates.</figcaption>
</figure>

The rater responded to the elaboration of the argument visible within an essay rather than to its rarity across the corpus. The paper does not take this as evidence that humans cannot perceive rarity; it limits the conclusion to what a single rater of limited reliability can show.

## What we know and what we don't

The paper establishes three points.

- AI essays differ from student essays **far more as a group than one by one**. Individual typicality relative to students can vanish for an assignment, while within-group claim diversity is about a third of the students'.
- The composition of the reference corpus decides what a rarity score means. A frozen student-only corpus supports stable scoring of new essays.
- Rarity is robust to paraphrase, but it rewards fabricated evidence and does not separate relevant from irrelevant novelty. **It is a promising exploratory measure, not a validated measure of originality.**

Many limits remain. The expert evaluation has one rater, so inter-rater reliability is unknown. Extraction was not validated by independent annotation, and rebuttals are not checked for actually answering their counterarguments. The quality score is an LLM judgement; relevance, factual accuracy and source use need separate checks. The data are two English assignments from one dataset, and the AI essays come from one model, not from students writing with AI assistance.

The paper proposes using the component percentiles as feedback on which argumentative move is most conventional relative to earlier students, paired with relevance and sourcing checks and instructor review, and not for grading or authorship decisions.

Data: the student essays come from the public AIDE dataset ([Kaggle](https://www.kaggle.com/datasets/lburleigh/tla-lab-ai-detection-for-essays-aide-dataset)).
