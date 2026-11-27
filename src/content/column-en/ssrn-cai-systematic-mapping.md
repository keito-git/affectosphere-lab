---
title: "Do Affective Computing Papers Say Who Supplied Their Emotion Labels?"
subtitle: "Computational Affective Intelligence: A Systematic Literature Mapping, Taxonomy, and Research Agenda for Affective Competence"
date: "2026-11-27"
excerpt: "Who supplied the emotion labels, and what was done when raters disagreed? A walk-through of a systematic literature mapping (SSRN preprint) that places 250 affective AI papers in a research space of six competences and four processes and counts how often these questions go unreported."
readingMinutes: 14
showImage: false
image: "/column-images/ssrn-cai-systematic-mapping/cai-conceptual.png"
imageAlt: "The three layers of CAI. Affective (phenomena), Intelligence (six competences) and Computational (four processes) span a 6 x 4 research space; the affective host and the source of ground truth cut across every cell."
authors:
  - name: "Keito Inoshita"
    url: "/en/about/"
    affiliation: "Kansai University"
tldr: "In affective AI evaluation, a person's own report of an emotion routinely differs from what third-party observers assign. Yet who supplied the labels and how rater disagreement was handled are not standard reporting items. This paper defines Computational Affective Intelligence (CAI) as a research space of six competences (perception, representation, reasoning, generation, interaction, regulation) and four processes (specification, construction, mechanism, evaluation). It codes 60 papers from IEEE Transactions on Affective Computing verbatim from full text and places 190 further records from four other sources into the space. Among the 44 papers in which disagreement could arise, 27 (61.4%, Wilson 95% CI 46.6%–74.3%) say nothing about how it was handled, and the absence is concentrated in dataset reuse (79.2%) rather than original collection (22.2%). In the external sample, 150 of 163 eligible papers (92.0%) could be placed. An illustrative analysis on one dataset shows that the gap between model and human accuracy changes by +0.154 depending on whether self-report or observer consensus supplies the ground truth. The paper is a preprint that has not been peer reviewed."
links:
  - label: "Preprint (SSRN)"
    url: "https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7501718"
citation: |
  @misc{inoshita2026cai,
    title        = {Computational Affective Intelligence: A Systematic Literature
                    Mapping, Taxonomy, and Research Agenda for Affective Competence},
    author       = {Inoshita, Keito},
    howpublished = {SSRN preprint, abstract id 7501718},
    year         = {2026}
  }
---

<div class="teaser">
<div>

Report

Of the 44 papers where raters could disagree, **61.4%** say nothing about how disagreement was handled: **79.2%** under dataset reuse, **22.2%** under original collection.

</div>
<div>

Map

In the single-journal sample, **48 of 60** papers fall in perception × construction. Across 150 papers from four other venues, mechanism is still only **1.4%** of placements.

</div>
<div>

Key

Switching the ground truth from self-report to observer consensus moves the model–human gap from **+0.187** to **+0.033**.

</div>
</div>

## Emotion labels do not always have one right answer

Evaluating affective AI has a difficulty that most other areas do not. In many datasets, the emotion a writer reports and the emotion a reader assigns differ systematically, and several observers often fail to converge. This divergence is increasingly understood not only as poor annotation quality but as a sign that emotion can legitimately be interpreted in more than one way (the perspectivist view).

At the same time, the intersection of emotion and computation has split into many names and frameworks: affective computing, Artificial Emotional Intelligence, Affective AI, Computational Affective Science and others, each built around its own questions. The paper argues that these frameworks complement each other, but none of them makes the following questions central.

- How far does an evaluation score move with the scoring convention, that is, with whose judgment counts as correct?
- When humans and AI are compared on the same task, does the scale measure the same latent variable for both?
- On items whose labels legitimately diverge, can abstention based on the model's own uncertainty stand in for abstention based on the plurality of human interpretation?

The paper therefore defines **Computational Affective Intelligence (CAI)** as a research space that engages these questions, and measures from the literature how far the field currently occupies it.

<figure>
  <img src="/column-images/ssrn-cai-systematic-mapping/cai-conceptual-1600.webp" alt="The three layers of CAI and the 6 x 4 research space" />
  <figcaption><strong>Figure 1.</strong> The three layers of CAI and the 6 × 4 research space (the paper's figure). Each word of the name corresponds to one layer. The affective host and the source of ground truth are not a fourth layer; they cut across every cell.</figcaption>
</figure>

The three words of the name correspond to three layers. **Affective** refers to affective phenomena such as emotions, moods, appraisals and preferences; CAI takes them as its subject without choosing between discrete, dimensional, appraisal and constructionist accounts. **Intelligence** refers to six competences a system shows with respect to these phenomena: perception, representation, reasoning, generation, interaction and regulation. **Computational** refers to four processes: formally describing a competence (specification), building it through learning or design (construction), analyzing and intervening on how it is realized internally (mechanism), and measuring it validly against an identifiable ground-truth source (evaluation).

The primary object of CAI is affective competence realized in artificial systems. Human affect remains essential as a source of ground truth, a reference for comparison and a counterpart in interaction. The paper also introduces the **affective host**, the entity to which states or competences are attributed: an individual, a human collective, an artificial agent or a multi-agent system. For a model that recognizes emotion from human faces, the host of the state is an individual and the host of the competence is an artificial agent.

Membership in the space is decided by two conditions: (i) the study makes a claim about a competence related to a host's affective state, and (ii) that claim can be evaluated by a computationally implementable procedure against an identifiable ground-truth source or criterion. A recommender that uses affective features only as auxiliary input fails (i); a psychology experiment without a computational evaluation criterion fails (ii).

## Two samples and the coding scheme

Because different claims need different evidence, the paper uses two tiers of sample.

<figure>
  <img src="/column-images/ssrn-cai-systematic-mapping/selection-flow-1600.webp" alt="Selection flow for the two samples" />
  <figcaption><strong>Figure 2.</strong> Selection flow for the two samples (the paper's figure). The core sample is read in full and supports the reporting claims; the external validation sample is placed from titles and abstracts and supports the coverage claims.</figcaption>
</figure>

The **core sample** is IEEE Transactions on Affective Computing, 2020–2025 (population 891 papers). A year-stratified systematic sample of 300 was drawn, 19 were excluded by publication type (surveys, editorials and the like), and 60 of the remaining 281 were randomly selected and coded verbatim from full text. The target was 300 papers; coding stopped at the 60 with verbatim-accessible full text, and the paper states plainly that the planned precision (about ±4.6 points) was not reached.

The **external validation sample** checks the bias of restricting the core to one journal.

| Tier | Venue | Candidates | Selected |
|---|---|---|---|
| Core | IEEE TAFFC 2020–2025 | 281 | 60 |
| External | ACL Anthology 2020–2026 | 779 | 63 |
| External | arXiv cs.CL / cs.AI / cs.HC 2023–2026 | 379 | 60 |
| External | ICMI 2020, 2022, 2023 | 52 | 27 |
| External | ACII 2021–2024 | 87 | 40 |
| | Total | | 250 |

(From the paper's table "Sample composition and extraction process". Some years of ICMI and ACII are missing because of index coverage.)

The inclusion criterion for the external sample was revised after a pilot. The first criterion took any paper with an emotion-related term in its title or abstract, and 57 of 192 papers (29.7%) could not be placed anywhere in the space. On inspection, papers on grammatical error correction or backdoor defense had been retrieved because they used sentiment analysis as one evaluation task. The non-placement rate ranged from 2.5% in ACII to 53.3% in arXiv, and the paper reads this as an extraction failure, not a taxonomy failure. The criterion was changed to "a term in the title, or a term in the first 400 characters of the abstract and at least twice in the abstract as a whole", and 21 papers retrieved only by the verb *affect* (to influence) were removed.

<div class="setup">

**Coding axes (core sample)**

- Axis B, ground-truth source: B1 third-party consensus, B2 expert, B3 self-report, B4 physiological measure, B5 designed stimulus intent, B6 not applicable, B7 multiple sources, B? not determinable from the text
- Axis C, disagreement handling: C1 aggregated, C2 agreement statistics only, C3 preserved or leveraged (C3a perspectives, C3b uncertainty), C4 not applicable (single source), C_none no statement in the text
- Ruling §7.1: information from the source paper of a reused dataset is not imported; only the text of the paper under review counts
- Axes A, D and E (purpose, evaluation paradigm, host) have only automated-coder output without verbatim checking and are not reported
- External sample: placed into the 24 cells from verbatim evidence in the title or abstract; a paper spanning several cells counts as several placements

</div>

The coding axes were derived from prior literature, not from the CAI definition, so that the results could not circularly confirm the definition. The correspondence to the CAI questions was mapped only after all axes had been coded.

The paper is explicit about two transparency issues. First, the C_none code was added after the data had been inspected. The original rules converted "no statement" into C1 or C4, so silence was treated as a positive description. The central finding comes from this code, and the risk of post hoc bias is concentrated in this one change. Second, the author coded alone. The reference rule-based coder works from titles and abstracts and is not independent, so no inter-rater agreement is reported.

## Analysis 1: Are the ground-truth source and disagreement handling reported?

<p class="experiment-label">Analysis 1</p>

The C-axis denominator includes only papers where disagreement is a meaningful question. Sixteen of the 60 were verbatim-confirmed to use single-source labels, which structurally rules out disagreement, leaving 44.

<figure>
  <img src="/column-images/ssrn-cai-systematic-mapping/reporting-1600.webp" alt="B-axis and C-axis distributions in the core sample" />
  <figcaption><strong>Figure 3.</strong> B-axis (60 papers) and C-axis (44 papers) distributions in the core sample (drawn from the paper's B-axis and C-axis tables). Amber marks "not determinable" and "no statement".</figcaption>
</figure>

The most frequent code is C_none: 27 of 44 papers (61.4%, Wilson 95% CI 46.6%–74.3%). The point estimate exceeds 50%, but the lower bound is 46.6%. Next is C1 (aggregated) with 10 papers (22.7%); C3a and C3b, which preserve or use disagreement, total 5. All three C3a papers make annotator disagreement itself the subject of the study.

On axis B, third-party consensus (B1), not determinable (B?) and self-report (B3) each account for 14 papers (23.3%). In nearly one paper in four, the text does not say who supplied the labels. Thirteen of the 14 B? papers are also C_none, so in 13 of 60 papers (21.7%, CI 13.1%–33.6%) neither the source nor the handling of disagreement can be determined. The paper notes that the B and C findings point to almost the same papers and describe one phenomenon from two angles, not two independent observations.

<figure>
  <img src="/column-images/ssrn-cai-systematic-mapping/reuse-strata-1600.webp" alt="C_none rate by dataset reuse status" />
  <figcaption><strong>Figure 4.</strong> C_none rate by dataset reuse status, with Wilson 95% confidence intervals (drawn from the paper's stratified table).</figcaption>
</figure>

The absence is not uniform. Among 24 papers that reuse existing datasets, 19 (79.2%) are C_none; among 9 that collected their own labels, 2 (22.2%) are. The difference is significant under Fisher's exact test (two-sided p = 0.005, odds ratio 13.3), as is the test across all three strata including unknown reuse status (χ²(2) = 9.24, p = 0.010). The overall 61.4% averages three quite different strata. The paper reads this as a structure in which **the ground-truth source becomes invisible at the point of label inheritance**, and explains that ruling §7.1 makes this asymmetry observable at the paper level rather than creating it.

Sensitivity analyses are reported. Restricted to the 30 papers with a determinable source, C_none falls to 46.7% (CI 30.2%–63.9%); with the 16 single-source papers added back, it is 45.0% (27/60). What holds under every denominator is that 13 of 60 papers leave both the source and the disagreement handling undeterminable.

Examples suggest the gap is not about missing resources. Three papers outside the 60 that used datasets distributing per-item votes, such as FERPlus with 10 raters per image, were checked verbatim. One acknowledged the 10 votes and reported majority-vote accuracy only; one repeatedly mentioned inconsistent annotations yet discarded the vote distributions and injected synthetic label noise; one did not mention majority, votes, soft labels or label distributions at all.

## Analysis 2: Which parts of the research space are filled, and which are empty?

<p class="experiment-label">Analysis 2</p>

The 60 core papers yield 124 placements (2.07 cells per paper on average). Forty-eight of the 60 papers sit in the perception × construction cell, so about 80% of papers fall in one of 24 cells. Eight cells are empty, five of them on the output side (generation, interaction, regulation). Representation × evaluation is also empty: no paper whose main subject is the validity of internal affective representations was found from titles and abstracts.

<figure>
  <img src="/column-images/ssrn-cai-systematic-mapping/core-vs-external-1600.webp" alt="Core sample versus external sample in the research space" />
  <figcaption><strong>Figure 5.</strong> Placements from the single-journal core sample (top, 60 papers) and the four-venue external sample (bottom, 150 papers) (the paper's figure). Hatched cells hold no paper; numbers are placements.</figcaption>
</figure>

In the external sample, 169 papers remained under the revised criterion. Excluding 6 that do not study emotion (extraction failures), 163 were eligible and 150 of them (92.0%) could be placed. The 19 that could not be placed break down as follows.

| Category | Count | % |
|---|---|---|
| Does not study emotion as a subject | 6 | 3.6 |
| Not primary research (e.g., workshop announcements) | 3 | 1.8 |
| Verbatim evidence unavailable | 4 | 2.4 |
| No computationally evaluable claim | 5 | 3.0 |
| Does not fit 6 competences × 4 processes | 1 | 0.6 |

(From the paper's table "Breakdown of the 19 papers that could not be placed". Denominator 169.)

Only the last row counts against the coverage of the taxonomy, and that paper was a workshop announcement stating its theme. The five papers with no computationally evaluable claim study emotion without an artificial system (for example, measuring how arousal affects taste perception in human participants); they are cases where inclusion condition (ii) worked as grounds for exclusion. The paper adds that five cases show the condition can be applied, not how well it discriminates.

The paper separates three kinds of validity and says that 92.0% primarily establishes **coverage validity**: a place exists for the papers examined. Discriminative validity (separating CAI work from non-CAI work) has only initial evidence, and structural validity (whether the two axes capture the real organization of the field) is not tested.

The perception concentration holds in the external sample too: 239 of 417 placements (57.3%). The difference is in empty cells. Only generation × mechanism and interaction × mechanism are empty in the external sample, and representation × evaluation, empty in the core, has 23 placements. The paper revises its reading accordingly: most of the core sample's empty cells reflect one journal, not gaps in the field. Its methodological lesson is that evaluating a taxonomy's coverage from a single venue risks over-reading empty cells as questions the field does not ask.

## Analysis 3: Why is mechanism work so rare?

<p class="experiment-label">Analysis 3</p>

The one process that is sparse in both samples is mechanism. In the external sample it accounts for 6 of 417 placements (1.4%), and the 53 ACL Anthology papers and 17 ICMI papers have none at all. The paper reads this as a field that has studied extensively what models do with affect, but rarely how they do it. Probing, causal tracing, activation patching, concept erasure and circuit-level analysis have been developed mainly on linguistic and factual targets, and their systematic application to affective competence remains sparse.

Mechanistic analysis may not appear in an abstract, however, so placement from titles and abstracts could undercount it. The paper tests this alternative against full texts.

<figure>
  <img src="/column-images/ssrn-cai-systematic-mapping/mechanism-check-1600.webp" alt="Full-text check of the Mechanism placement" />
  <figcaption><strong>Figure 6.</strong> The full-text check of the Mechanism placement (drawn from the numbers in Section 5.6 of the paper). The vocabulary was fixed before retrieval, and bodies were searched excluding reference lists.</figcaption>
</figure>

Of the 123 open-access records from ACL Anthology and arXiv, 58 full texts were retrieved. A deliberately generous vocabulary (probing, causal tracing, activation patching, model editing, concept erasure, circuit, neuron and others) matched at least one term in 17 of them. Reading the surrounding sentences, 15 used the term in an unrelated sense (a question that "probes" a respondent, a circuit in an alarm-clock illustration), and only 2 used it in the mechanistic sense. Both of those had already been placed in Mechanism from their abstracts.

The conclusion is cautious. Within the subset examined, there is no evidence that abstract-level placement systematically missed mechanistic work, which weakens the explanation that the sparsity is an artifact of the placement basis. But the subscription venues ICMI and ACII were not checked, so the check covers 58 of the 190 external papers, and a keyword sweep cannot rule out mechanistic papers that use none of the terms.

## Analysis 4: Did large language models change the distribution?

<p class="experiment-label">Analysis 4</p>

The temporal comparison uses the ACL Anthology subsample only, because it is the one subsample with 9 papers drawn per year from 2020 through 2026, so year is not confounded with venue. The 53 placed papers were split into 2020–2022 (22 papers) and 2023–2026 (31 papers).

<figure>
  <img src="/column-images/ssrn-cai-systematic-mapping/temporal-1600.webp" alt="Placement distributions before and after the emergence of LLMs" />
  <figcaption><strong>Figure 7.</strong> Placement distributions in the ACL Anthology subsample before and after the emergence of large language models (the paper's figure). Dots are shares of papers; lines are Wilson 95% intervals.</figcaption>
</figure>

For none of the six competences or four processes does the difference between periods reach significance under Fisher's exact test. The smallest p-value is 0.277 (reasoning and specification), before correction for 10 comparisons. Perception accounts for 86.4% in the early period and 87.1% in the late period, and mechanism has no placements in either.

The paper records this not as proof of no change but as a negative finding at this sample size: with 22 and 31 papers, the comparison may lack the power to detect a moderate shift.

## Analysis 5: How does changing the ground-truth source move a human–model comparison?

<p class="experiment-label">Analysis 5</p>

The mapping shows that the ground-truth source is often unreported. To show what that leaves hidden, the paper runs an illustrative analysis confined to one dataset and one family of models.

<div class="setup">

**Setup**

- Data: the validation portion of crowd-enVent. Writers describe an event that caused an emotion and label it themselves; five readers label each text independently
- Self-report key: the writer's own label is the ground truth
- Observer key: the majority of four readers, formed over each of the five leave-one-out subsets; a reader is scored against the subset excluding that reader, and a model against all five subsets and averaged, so the design is symmetric
- Scored parties: 11 configurations (prompt and temperature) of four commercial language models from a single provider, and the individual human reader
- Intervals: bootstrap over items, B = 2000

</div>

<figure>
  <img src="/column-images/ssrn-cai-systematic-mapping/scoring-key-1600.webp" alt="Accuracy under the two scoring keys" />
  <figcaption><strong>Figure 8.</strong> Accuracy under the two scoring keys (drawn from the paper's scoring-key sensitivity table). Amber is the self-report key and blue the observer key; the number on the right is the difference Δkey.</figcaption>
</figure>

Three results follow. First, the models are almost insensitive to the key: the mean Δkey over 11 configurations is +0.019, with an interval [−0.009, +0.047] that includes zero. Second, the human reader is not: 0.638 against the consensus of other readers but 0.504 against the writer's own label, a Δkey of −0.134 in the opposite direction. Third, the human–model comparison therefore depends almost entirely on the key. The gap is +0.187 under the self-report key and +0.033 under the observer key, and the difference between the two gaps is +0.154 [+0.120, +0.187].

The paper stresses why the gap changes. It is not that the models behave differently under the two keys; it is that what counts as human competence changes. Against what other readers agreed on, the individual reader looks competent; against what the writer said they felt, the same reader looks much less so, while the models barely move. Model rankings are largely preserved (Spearman correlation between the two key-specific rankings 0.882, interval [0.718, 0.964]; 8 of 55 model pairs swap order), so a benchmark that reports only the top model would give nearly the same answer under either key. A benchmark that reports how far models stand from human performance would give two very different answers.

The analysis does not show that scoring keys reverse comparisons in general. An earlier version used reversal of direction as its criterion, and that criterion was not met: models scored above the individual reader under every key. What is reported is the weaker, more general result that the size of a comparison depends on the source of the ground truth, and that the dependence falls almost entirely on the human side. There is one dataset, one language and one elicitation protocol; the models come from one provider; and the human side is a single reader. The paper notes that aggregating readers into a panel raises the human score under the self-report key and narrows the gap.

## Analysis 6: A research agenda and minimum reporting items

<p class="experiment-label">Analysis 6</p>

From the research space and the gaps in the mapping, the paper derives eight research questions.

| Research question | Question | What this review observed |
|---|---|---|
| RQ1 representation | How should affective states, distributions and uncertainty be represented inside AI? | Representation × evaluation empty in the core, 23 placements in the external sample |
| RQ2 reasoning | How should agents reason about affect given context, culture and individual differences? | Mechanism cells empty in the ACL Anthology and ICMI samples |
| RQ3 generation | Under what conditions should AI generate and adjust affective expressions? | Five of eight empty core cells are on output-side competences |
| RQ4 ground truth | Which ground-truth sources does evaluating affective competence require? | 61.4% of the C-axis denominator report no disagreement handling; 23.3% undeterminable source |
| RQ5 measurement | Does the scale measure the same latent variable for humans and AI? | Model–human gap changes by +0.154 with the scoring key |
| RQ6 uncertainty | How should AI represent uncertainty and abstain when interpretations legitimately diverge? | Human–model label-distribution divergence is measurable; link to abstention design not tested |
| RQ7 interaction | How should affective intelligence be evaluated in human–AI interaction? | Interaction cells sparse; mechanism empty in both samples |
| RQ8 governance | How should affective AI be designed under cultural, ethical, privacy and manipulation constraints? | Regulatory frameworks constrain which ground-truth sources are accessible |

(Summarized from the paper's table "Eight research questions of CAI mapped to the 6 × 4 research space".)

Priority follows whether the prerequisites for a question are in place. The short term is RQ4, which needs a reporting convention rather than a new method, starting with restating the annotation procedure in papers that inherit labels; if dataset distributors shipped a machine-readable summary of their annotation procedures, the cost of restating it downstream would drop. The medium term is RQ1, RQ5 and RQ6, and the long term is RQ2, RQ3, RQ7 and RQ8, for which evaluation criteria are not yet established. The paper itself only formulates the three measurement questions corresponding to RQ4–6 and does not claim to have resolved them.

The practical form of the agenda is a set of minimum reporting items, **CAI-MR**.

| # | Item | Basis |
|---|---|---|
| 1 | Ground-truth source (self-report, third-party, expert, physiological, designed stimulus intent, artificial agent, or a combination) | Absence observed in the survey |
| 2 | Disagreement handling (aggregated, agreement reported, perspectives preserved, uncertainty retained) | Absence observed in the survey |
| 3 | Inherited annotation protocol (restated in the text, not only cited) | Absence observed in the survey |
| 4 | Affective host | Derived from the definition |
| 5 | Targeted competence and process | Derived from the definition |
| 6 | Aggregation rule | Derived from the definition |
| 7 | Uncertainty representation | Derived from the definition |
| 8 | Evaluation criterion (what was measured, against which source) | Derived from the definition |

(Summarized from the paper's table "CAI-MR".)

The paper states that the list is not proposed as a pass/fail criterion for peer review. What it showed is an absence of reporting in the text, not that studies lacking it reach wrong conclusions. The aim is comparability across studies, achieved not by mandating one measurement procedure but by each study stating what it measured against which source.

## What we found, and what remains open

The study yields four results.

- Within this survey, the ground-truth source and the handling of rater disagreement are not standard reporting items, and the absence is concentrated in papers that inherit labels from existing datasets (79.2% vs. 22.2%).
- The 6 × 4 research space can place the papers examined (92.0% of the external sample). Most cells left empty by the single journal filled once other venues were included.
- Mechanism stayed sparse in both samples, and a full-text check of the open-access records found no evidence that abstract-level placement missed mechanistic work. No change in the distribution was detected before and after the rise of large language models.
- On one dataset, switching the ground truth between self-report and observer consensus changed the human–model gap by +0.154, and almost all of that change came from the human side.

The paper lists four limitations. The author coded alone, with no double coding by an independent second coder, and makes no claim about coding reliability. Placement of the external sample rests on titles and abstracts, and the full-text mechanism check did not reach the subscription venues. The inclusion criterion and vocabulary were revised after a pilot, so correspondence with the initial time-stamped design is not exact, and ICMI and ACII do not cover every year of the target period. And the scoring-key analysis is confined to one dataset, one provider's models and a single reader on the human side. In addition, the core sample of 60 limits precision, and the paper itself notes that the C_none code was added after inspecting the data and needs re-examination by an independent coder.

The paper says the coding records, codebook, sampling records and scripts are to be deposited in a public repository; this version of the manuscript gives no public URL. The paper is available on SSRN as a preprint that has not been peer reviewed.
