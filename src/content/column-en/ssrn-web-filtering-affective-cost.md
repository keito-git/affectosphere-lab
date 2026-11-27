---
title: "What Does Web Quality Filtering Stop Teaching Language Models About Emotion?"
subtitle: "The Hidden Affective Cost of Web Quality Filtering"
date: "2026-11-27"
excerpt: "The language model trained on an educationally filtered Web corpus scored highest on knowledge benchmarks and had the weakest emotion structure of eight models. The filter dropped first-person narration far more than emotion words. A walk-through of our SSRN preprint."
readingMinutes: 13
showImage: false
image: "/column-images/ssrn-web-filtering-affective-cost/overview.png"
imageAlt: "Overview of the three analyses. A corpus comparison, a filter audit and vocabulary deletion during pretraining feed into a shared floor-gated emotion probing protocol."
authors:
  - name: "Keito Inoshita"
    url: "/en/about/"
    affiliation: "Kansai University"
tldr: "Web quality filters are judged by the capabilities they improve. But which human experiences do they remove from the training data? We compared eight compute-matched language models on how well emotion can be read from event descriptions that never name an emotion, counting only what exceeds a random network and a bag-of-words baseline. The model trained on the educationally filtered FineWeb-Edu beat its source FineWeb on knowledge benchmarks (0.455 vs. 0.395) and had the weakest emotion structure of the eight (macro-F1 0.456 vs. 0.493). In an audit of about 59,000 documents, one SD of first-person density cut the odds of being kept to 0.25; the association with emotion-word density was much weaker."
links:
  - label: "Preprint (SSRN)"
    url: "https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7647739"
citation: |
  @misc{inoshita2026hiddenaffective,
    title        = {The Hidden Affective Cost of Web Quality Filtering},
    author       = {Inoshita, Keito},
    year         = {2026},
    howpublished = {SSRN preprint, abstract id 7647739}
  }
---

<div class="teaser">
<div>

Contrast

The model trained on the educationally filtered corpus is **best on knowledge** and **weakest on emotion structure** of eight (0.456 vs. 0.493).

</div>
<div>

Audit

The filter strongly drops **first-person narration**: odds of passing 0.25× per SD of first-person density, 0.98× for emotion words.

</div>
<div>

Gate

Deleting every emotion word during pretraining shows no loss beyond controls at 124M, but the **measurability gate is not met, so no verdict**.

</div>
</div>

## What do filters stop teaching?

The Web is the main source from which language models learn about human life, and the Web that reaches a model is increasingly curated. Only pages that survive deduplication, heuristic rules and learned quality classifiers are used for pretraining.

Quality filters are judged by the capabilities they improve. The educational classifier behind FineWeb-Edu, for example, raises knowledge benchmarks such as MMLU and ARC. But quality is always quality for a purpose. A corpus optimized for one purpose need not preserve the range of human experience the Web records.

We use emotion as a test case. People convey emotion not only by naming it ("I was sad") but also by narrating what happened. If a filter removes first-person accounts of personal events, models may learn less of the emotion that situations imply, even when emotion words remain.

## Three analyses and a floor-gated measure

<figure>
  <img src="/column-images/ssrn-web-filtering-affective-cost/overview-1600.webp" alt="Overview of the three analyses" />
  <figcaption><strong>Figure 1.</strong> Overview figure from the paper. Q1 corpus comparison (observational), Q2 filter audit (document level), Q3 vocabulary deletion during pretraining (intervention). The models of Q1 and Q3 enter the shared measurement protocol on the right.</figcaption>
</figure>

We ask three questions.

- **Q1:** How does the emotion structure a model learns vary with how its Web corpus was curated?
- **Q2:** Which documents does the quality classifier keep, and which does it drop?
- **Q3:** Does removing emotion-naming words from the training data weaken that structure?

The measurement has two safeguards. The first is the stimuli. We use the 6,600 event descriptions of crowd-enVENT, each labeled by its writer with one of 13 emotions and rated on 21 appraisal dimensions. The official version already masks the emotion word; we further scrub any remaining emotion words with an extended lexicon. A model can then recover the category only by representing the situation, not by spotting a label word.

The second is the floor. Situation words alone carry emotion cues, so raw probe scores are not interpretable. The floor is the higher of a randomly initialized network of the same architecture and a TF-IDF bag-of-words (BoW) probe, and a model is credited only for what exceeds it. The main measure, M1, is the macro-F1 over 13 categories. M2 (discrimination within negative emotions), M3 (pleasantness regression) and M4 (representational similarity with humans) are also reported.

The stimuli were split into 3,281 discovery and 3,319 confirmation texts before any model was measured.

## Experiment 1: Eight Web corpora

<p class="experiment-label">Experiment 1</p>

<div class="setup">

**Setup**

- Models: the eight ablation models released with FineWeb (Llama-style, 24 layers, 1.71B parameters, 350B tokens), differing only in their corpus
- Corpora: FineWeb, FineWeb-Edu, C4, Dolma, RefinedWeb, SlimPajama, the Pile, RedPajama-V2
- FineWeb-Edu is the part of FineWeb that passes the educational classifier, so this pair differs only in that filter
- Predictions fixed in advance: P1 FineWeb-Edu has less floor-exceeding structure than FineWeb; P2 the relative drop exceeds the drop in emotion-word density; P3 structure correlates more with first-person and narrative density than with emotion-word density

</div>

<figure>
  <img src="/column-images/ssrn-web-filtering-affective-cost/corpora-1600.webp" alt="Held-out M1 of eight corpora" />
  <figcaption><strong>Figure 2.</strong> M1 on the held-out set. The dashed line is the BoW floor (0.362). All eight models exceed it; FineWeb-Edu is lowest.</figcaption>
</figure>

Every model exceeded the floor, so emotion categories are linearly recoverable from situations that never name them. FineWeb-Edu had the smallest floor-exceeding M1 on both splits: 0.097 on discovery (FineWeb 0.125) and 0.094 on held-out (FineWeb 0.131), a 22% to 28% reduction. It was also lowest on M2 to M4 on the held-out set.

We also compared what the corpora contain.

<figure>
  <img src="/column-images/ssrn-web-filtering-affective-cost/densities-1600.webp" alt="Corpus densities" />
  <figcaption><strong>Figure 3.</strong> Densities per 1,000 words. FineWeb-Edu loses far more first-person pronouns and narrative clauses than emotion words.</figcaption>
</figure>

Relative to FineWeb, FineWeb-Edu has 27% fewer emotion words but 74% fewer first-person pronouns and 70% fewer narrative clauses. The relative loss of structure, however, is of the same order as the loss of emotion words, so P2 is not supported. Structure correlates most strongly with first-person density, as P3 predicts, but with eight corpora and densities correlated at 0.86 to 0.98, the three correlations cannot be distinguished. Corpora outside the FineWeb pair are less stable across splits, so the paper interprets only this pair.

## Experiment 2: Is the contrast robust?

<p class="experiment-label">Experiment 2</p>

<figure>
  <img src="/column-images/ssrn-web-filtering-affective-cost/robustness-1600.webp" alt="Robustness of the FineWeb contrast" />
  <figcaption><strong>Figure 4.</strong> M1 difference between FineWeb and FineWeb-Edu (95% CI). Every representation-level check is positive; only the zero-shot behavioral test crosses zero.</figcaption>
</figure>

On the held-out set, with layers fixed in advance, the difference equals the discovery estimate of 0.029. It remains with writer-grouped folds, with other probes (an MLP, logistic regression without PCA, a nearest-centroid classifier) and on the external EmpatheticDialogues set, and FineWeb-Edu ranks last of eight each time. These robustness analyses were specified before execution but after the original plan, so the paper reports them as post hoc.

Each corpus has only one public training run. Across six intermediate checkpoints from 101B to 348B tokens, the gap stays between 0.029 and 0.036, which does not substitute for independent seeds. A zero-shot behavioral test, in which each model completes a held-out situation with an emotion label, shows the predicted sign, but its CI includes zero.

## Experiment 3: More knowledge, weaker emotion structure

<p class="experiment-label">Experiment 3</p>

<figure>
  <img src="/column-images/ssrn-web-filtering-affective-cost/knowledge-1600.webp" alt="Knowledge vs emotion structure" />
  <figcaption><strong>Figure 5.</strong> Published benchmark scores of the same checkpoints (mean of MMLU, ARC and OpenBookQA) next to held-out M1.</figcaption>
</figure>

FineWeb-Edu has the highest knowledge score of the eight corpora, 0.455 against 0.395 for FineWeb, and the lowest emotion structure.

Across all eight corpora, however, knowledge and emotion scores are unrelated (ρ = −0.05). The paper does not claim a general trade-off. The claim is specific to the educational filter: its gain on knowledge benchmarks hides a weakening those benchmarks do not measure.

## Experiment 4: What does the filter select?

<p class="experiment-label">Experiment 4</p>

<div class="setup">

**Setup**

- 29,716 and 29,697 documents sampled from two FineWeb shards, scored with the public FineWeb-Edu classifier (kept if the rounded score is at least 3)
- Logistic regression of the keep decision on standardized emotion-word, first-person and narrative densities plus log length
- Robustness: topic-cluster fixed effects, domain bootstrap, the second shard, a parser-based narrative proxy, other thresholds

</div>

<figure>
  <img src="/column-images/ssrn-web-filtering-affective-cost/audit-1600.webp" alt="Odds ratios for passing the filter" />
  <figcaption><strong>Figure 6.</strong> Odds ratio per SD for passing the filter (95% CI). First person sits consistently near 0.25; emotion words stay close to 1.</figcaption>
</figure>

In the first shard, 6.0% of documents pass. One SD of first-person density reduces the odds of passing to 0.25 of their value, and one SD of narrative density to 0.73. The OR for emotion-word density is 0.98, with a CI that includes 1. Documents with any narrative clause pass at 4.2% against 7.0% for those without, so their share falls from 36% of all documents to 25% of kept documents.

The first-person and narrative ORs persist with topic adjustment and domain bootstrap, on the second shard and with the parser-based proxy. The first-person OR strengthens as the threshold rises (0.55 at threshold 2, 0.05 at threshold 4). Emotion words show only a weak negative association in some fits.

| Fit | First person | Narrative | Emotion words |
|---|---|---|---|
| Shard 1, base | 0.25 | 0.73 | 0.98 |
| Shard 1, topic + domains | 0.26 | 0.74 | 0.91 |
| Shard 2, base | 0.24 | 0.72 | 0.88 |
| Shard 2, topic + domains | 0.28 | 0.71 | 0.87 |

To separate grammatical person from content, 500 first-person documents were rewritten into the third person by a rule-based parser and rescored. The rewrites score 0.12 higher on average (CI [0.11, 0.13]), and 91% score higher. Because first-person documents start far below the threshold, only 2 of 500 cross it. These are not human annotations, so the rewrite is treated as exploratory evidence of sensitivity to person. The audit describes the filter; on its own it does not establish an effect on models.

## Experiment 5: Deleting emotion words during pretraining

<p class="experiment-label">Experiment 5</p>

<div class="setup">

**Setup**

- 124M-parameter Llama-architecture models trained from scratch on 3.3B FineWeb tokens; 5 conditions × 3 seeds = 15 runs
- Conditions: full (no deletion), emo-core (deletes the 393-word emotion lexicon), emo-strict (extended lexicon plus emoji), freq-matched (non-affective words matched in part of speech and frequency), class-matched (cognition and perception verbs)
- Token share: 0.343% for the emotion lexicon, 0.336% and 0.345% for the controls
- Measurability gate: the full models' floor-exceeding M1 must be at least 0.03 with a 95% CI excluding 0; otherwise no verdict

</div>

The full models exceeded the floor by 0.0279 (seed-bootstrap CI [0.021, 0.033]), just short of 0.03. As fixed in advance, no verdict is issued on H1, the hypothesis that emotion words are not necessary.

<figure>
  <img src="/column-images/ssrn-web-filtering-affective-cost/deletion-1600.webp" alt="Retention after deletion" />
  <figcaption><strong>Figure 7.</strong> Retention relative to full at 124M (95% CI). The gate is not met, so these are exploratory. Every interval overlaps every other.</figcaption>
</figure>

As exploratory estimates, emotion-word and control deletions do not differ. Emo-core retains 78% of the category structure, between the two controls at 83% and 72%. Within-negative discrimination, which constructionist accounts expect to depend most on words, is retained at 81%. The direct contrast between emo-core and freq-matched is −0.001 in M1 (Welch interval [−0.014, 0.012]). That interval is still compatible with an emotion-word-specific loss of up to about half of the full models' floor-exceeding structure, so precision is limited at this scale. The developmental curves of full and emo-core also overlap throughout training.

## Experiment 6: At what scale can this be measured?

<p class="experiment-label">Experiment 6</p>

<figure>
  <img src="/column-images/ssrn-web-filtering-affective-cost/scale-1600.webp" alt="Measurability across scales" />
  <figcaption><strong>Figure 8.</strong> Floor-exceeding M1 on the held-out set by model size. The dashed line is the 0.03 gate. 124M falls short; 360M meets it. The 1.71B point is the FineWeb ablation model (no seed interval).</figcaption>
</figure>

With every threshold unchanged, a 360M-parameter model trained on 7.2B tokens exceeded the floor by 0.053 at layer 17 (CI [0.051, 0.055]), and every layer from 11 to 24 exceeded 0.03. At this scale the deletion experiment has enough sensitivity to test H1. The decision rules require all 15 runs, however, so the 360M result is reported only as a gate outcome.

## What we found, and what remains open

Three findings stand out.

- The model trained on the educationally filtered corpus, which leads on knowledge benchmarks, had the weakest linearly recoverable emotion structure of eight. The contrast replicated on held-out stimuli, other probes and an external dataset.
- That classifier dropped first-person narration far more than emotion vocabulary. Keeping the words of emotion does not necessarily keep the experiential contexts from which emotion is inferred.
- Whether emotion words themselves are necessary is still open: the gate failed at 124M, and the deletion runs at 360M, where the gate is met, have not been done.

The paper proposes that data cards report an experiential-coverage pair before and after each filter: the share of documents with a first-person narrative clause and the first-person singular density. For the educational filter these fall from 0.36 to 0.25 and from 12.1 to 3.1.

There are limitations. Each ablation corpus has a single public training run, so the intervals do not capture pretraining-seed variation. The corpus comparison has eight points with collinear densities, and only one quality filter is examined. The audit is observational and cannot exclude unmeasured document properties. The narrative proxy records first-person event accounts, not subjective experience. All stimuli are English first-person accounts, so a loss of emotion information is not separated from weaker adaptation to first-person style. Whether narration causes the corpus differences requires an intervention during pretraining.

Next steps are to train the deletion models at 360M and to test the role of narration causally during pretraining. This post describes a preprint that has not been peer reviewed.
