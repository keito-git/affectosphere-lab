---
title: "Does Adding More LLM Judges Make an Evaluation Panel Identifiable?"
subtitle: "Adding Judges Is Not Enough: Free Anchors for Identifiable LLM Judge Panels"
date: "2026-11-27"
excerpt: "Does an LLM judge panel become more reliable as more judges are added? In theory and on two real panels, families added after the first gave no detected reduction in identification, while two unambiguous items already in the pool did. A walk-through of our WSDM 2027 paper."
readingMinutes: 13
showImage: false
image: "/column-images/wsdm2027-free-anchors/gauge-schematic.png"
imageAlt: "Schematic of the probability simplex. With true profiles at vertices only relabelling remains; with interior profiles a continuum of equally good explanations remains."
authors:
  - name: "Keito Inoshita"
    url: "/en/about/"
    affiliation: "Kansai University"
tldr: "LLM evaluation panels are usually assumed to become more reliable as judges are added. We model a panel as a family-level latent-class model and ask how far judge distortion can be separated from the true values. When true profiles sit at vertices of the probability simplex (one correct label), only label permutations remain. When they sit in the interior (a distribution over intents), a continuum of dimension L(L−1) remains for any number of judge families. On two real panels, families added after the first gave no detected reduction in the diameter of the identification set, while two gold-confirmed unambiguous items already in the pool reduced it by 18%. For binary labels, two likelihood ratios decide before procurement whether a candidate family can help, and this check predicted all 69 real cases tested."
links:
  - label: "Paper (WSDM 2027, accepted)"
    url: "https://lab.affectosphere.group/en/news/20261103-wsdm2027-free-anchors/"
  - label: "Code / Data"
    url: "https://github.com/keito-git/free-anchors-llm-judge-panels"
citation: |
  @inproceedings{inoshita2027freeanchors,
    title     = {Adding Judges Is Not Enough: Free Anchors for Identifiable
                 {LLM} Judge Panels},
    author    = {Inoshita, Keito},
    booktitle = {Proceedings of the Twentieth ACM International Conference on
                 Web Search and Data Mining (WSDM 2027)},
    year      = {2027},
    doi       = {10.1145/3862322.3863454},
    note      = {Accepted, to appear}
  }
---

<div class="teaser">
<div>

Gauge

With true profiles in the **interior**, a continuum of dimension **L(L−1)** remains for any number of families.

</div>
<div>

Panels

On two real panels, families after the first gave **no detected reduction** (on TREC-COVID, six more providers left the diameter at 1.1066).

</div>
<div>

Anchors

**Two** unambiguous items already in the pool cut the diameter by **18.03%**, with no new human labels.

</div>
</div>

## Do more judges make a panel trustworthy?

Using LLMs as judges is now a standard way to reduce the cost and latency of human evaluation. Because any single judge has its own biases, the common practice is to build a **panel** of models from different providers and training data, in the hope that their errors will not coincide. Panel size and diversity have become design parameters.

Whether these parameters help depends on what the panel is asked to estimate. Information retrieval evaluation has two notions of the true value.

| | Point contract | Distribution contract |
|---|---|---|
| True value | Label of one designated assessor | Label distribution marginalised over query intents |
| Location in the simplex | Vertex | Interior |
| Examples | Adhoc retrieval, TREC DL | TREC Web Track diversity, NTCIR INTENT-2 |
| Identifiability | Identified with 3 or more families (T1) | Not identified for any number of families (T3 b) |

One difficulty is that judge disagreement cannot tell which contract is in force. The paper shows that for any model with distributional true values there is a model with point true values that produces the same observations (Proposition P0). The contract has to come from the definition of the evaluation protocol, not from the data.

A second difficulty is that classical latent-class results stop at the emission columns, that is, what each latent class looks like to the judges. Panel design also needs to split each column into **judge distortion** and **true value**, and this does not follow from the classical results. The goal of this study was to state which expansions of a panel can improve identification and which cannot.

## Theory: the remaining freedom is a gauge group

<figure>
  <img src="/column-images/wsdm2027-free-anchors/gauge-schematic-1600.webp" alt="Schematic of the gauge theorem" />
  <figcaption><strong>Figure 1.</strong> Schematic of the gauge theorem (T3), not data. Left: with true profiles at vertices, only relabelling remains. Right: with interior profiles, a continuum of explanations that shift judge distortion against the true values fits the observations equally well.</figcaption>
</figure>

Judges from the same provider form a **family**. Judges within a family may depend on each other arbitrarily, and different families are conditionally independent given the truth. The response of family f is the product C_f p of a column-stochastic distortion matrix C_f and a true-value profile p.

Replacing the distortion by C_f A⁻¹ and the truth by A p leaves the product, and therefore the observations, unchanged. The set of such matrices A is the **gauge group**, and the paper's main results describe it.

1. **T1 (identification from three or more families)**: under the point contract, if the families can be split into three groups whose Kruskal ranks sum to at least 2K + 2, the parameters are identified up to label permutation. Two families can fail.
2. **T3 (gauge theorem)**: if all true profiles are vertices, the gauge group contains only permutations. If all lie in the interior and the distortions are entry-positive, it contains a continuum of dimension L(L−1), which no number of families, judges or items removes.
3. **C1 (limits of family diversity)**: a distortion shared by every family cannot be removed by any number of families (a diameter floor of 2η). A family whose errors lie in the cone spanned by the existing families (panel dominated) adds no identification power at any sample size.
4. **T2 and T4 (anchors)**: the gauge can be fixed only by information from outside the panel. Human anchors work only at the usual parametric rate n^(−1/2) (T2). Items at the vertex of every label already in the pool (structural anchors) collapse the gauge to permutations without human labels (T4).

For binary labels the C1 check is arithmetic. For a candidate family g, take α_g, the probability of answering 1 when the truth is 0, and β_g, the probability of answering 1 when the truth is 1, and compute r₁ = β/α and r₀ = (1−β)/(1−α). If r₁ exceeds the existing maximum or r₀ falls below the existing minimum, g can contribute. Otherwise it need not be bought for identification, whatever its accuracy or provider.

The experiments measure the **ℓ1 diameter of the identification set**: how far the true profiles can move while staying consistent with the observations. It is estimated by sampling many gauge directions and taking the largest admissible move, so every value is a lower bound.

## Experiment 1: synthetic data with known parameters

<p class="experiment-label">Experiment 1</p>

<div class="setup">

**Setup**

- Data: synthetic panels generated from known parameters (E1)
- Checks: T1 (two vs three families), T3 (vertex vs interior), T4 (collapse with 1% anchors)
- Compute: CPU only, no GPU

</div>

<figure>
  <img src="/column-images/wsdm2027-free-anchors/synthetic-1600.webp" alt="Synthetic checks" />
  <figcaption><strong>Figure 2.</strong> Checks on synthetic data. Left: going from two to three families lowers NRMSE from 0.560 to 0.310 (Welch t-test, p = 0.00036). Middle: with interior profiles, going from 3 to 20 families lowers the diameter only from 0.327 to 0.154. Right: 1% anchors take the diameter from 0.312 to 0.003.</figcaption>
</figure>

With vertex profiles the gauge orbit moved by 0.000000, so nothing beyond permutations remained. With interior profiles a diameter of 0.154 remained even at 20 families. The binary criterion also agreed with observation in all 60 synthetic configurations (E9a).

The comparison of one versus three families is not significant (p = 0.056). The paper explains that all 100 initialisations at one family converge to the same solution, so the meaningful comparison is two versus three.

## Experiment 2: do added families shrink the diameter?

<p class="experiment-label">Experiment 2</p>

<div class="setup">

**Setup**

- Panel 1: LLMJudge (33 judgment sets, three families GPT, Llama and T5, 4,423 items, four relevance levels)
- Panel 2: a panel we collected on BEIR TREC-COVID (294 items, nine judges from seven providers, three levels, temperature zero, one fixed prompt, 2,700 API requests)
- Family kernels are estimated from the human gold labels

</div>

We first checked that family boundaries exist in the data.

<figure>
  <img src="/column-images/wsdm2027-free-anchors/agreement-1600.webp" alt="Within- and cross-family agreement" />
  <figcaption><strong>Figure 3.</strong> Within- and cross-family agreement on LLMJudge (left) and leave-one-family-out Spearman ρ with 95% CI (right). Agreement is 0.095 higher within families, so the boundaries exist statistically.</figcaption>
</figure>

Mean Pearson φ is 0.589 within families and 0.494 across them, a gap of 0.095 (95% CI [0.068, 0.123], p = 1.8 × 10⁻¹¹). Predicting a held-out family from the others gives ρ = 0.80 to 0.87, indicating a common latent signal. The rank screen gives 4 for each family, so the grouped sum of 12 meets the required 10. LLMJudge therefore satisfies the condition of T1.

We then added families one at a time and measured the diameter.

<figure>
  <img src="/column-images/wsdm2027-free-anchors/diversification-1600.webp" alt="Diameter as families are added" />
  <figcaption><strong>Figure 4.</strong> Diameter of the identification set as families are added. The hatched bars (m = 0) are the kernel-free bound 2(1−η), not a baseline. Families after the first change the diameter little or not at all.</figcaption>
</figure>

On LLMJudge, the 26 judges of Llama and T5 added after GPT removed 0.30%, which is below the resolution of the search. On the TREC-COVID panel, the six families after GPT (Claude, Gemini, Llama, Qwen, Mistral, DeepSeek) left the diameter at 1.1066 to six decimals. The large drop at m = 1 starts from the kernel-free bound and says nothing about the value of that family.

The added families are not doing nothing. On LLMJudge no family was panel dominated, and the identification set itself shrank strictly (29 of 6,000 sampled directions showed a reduction). The directions that set the diameter did not move, however, so the diameter stayed the same. The paper treats shrinkage of the set and shrinkage of its diameter as separate quantities.

## Experiment 3: free anchors already in the pool

<p class="experiment-label">Experiment 3</p>

<div class="setup">

**Setup**

- Order all 4,423 items by the ℓ1 distance of their 33-judge profile to the nearest vertex; the top 10% (442 items) form the unambiguous pool
- Measure the diameter on 400 interior prototypes drawn from the most ambiguous 50%
- Anchors are selected by judge consensus, so they were checked against gold labels (E34 to E36)

</div>

Instead of families, we used items in the pool that are clear to every judge as anchors. No new human labels are needed.

<figure>
  <img src="/column-images/wsdm2027-free-anchors/anchor-sweep-1600.webp" alt="Anchor sweep" />
  <figcaption><strong>Figure 5.</strong> Interior diameter against the number of unambiguous items in the pool. On LLMJudge two items take it from 1.1233 to 0.9208 (−18.03%), and 80 items give the same value. On the TREC-COVID panel twelve or more items give 0.8451 (−5.0%).</figcaption>
</figure>

On LLMJudge two items (a 0.5% rate) reduced the diameter by 18.03%, and rates up to 20% left it there. On the TREC-COVID panel the reduction was 5.0%. That pool already reaches all three vertices at distance zero, so the paper notes that little is left to buy.

Consensus alone does not establish that an item is a true vertex, so we checked the pool against gold labels. Of the 442 items, 392 (88.7%) have gold label 0, and restricting the pool to these 392 reproduced every diameter to six decimals. On the second panel 23 of 29 pool items agree with gold, and the restricted sweep again reproduced every value.

The measurement needs care. If anchors stay in the set whose displacement is maximised, a permutation moves them onto another vertex and they become the largest move; that gives a diameter of 0.9777. The rule is to let anchors constrain and to measure on the interior prototypes.

<figure>
  <img src="/column-images/wsdm2027-free-anchors/interventions-1600.webp" alt="Three interventions compared" />
  <figcaption><strong>Figure 6.</strong> Three interventions on LLMJudge, each as diameter after divided by diameter before (optimised estimator). Adding 26 judges from two lineage families gives 0.997, splitting a family within one lineage gives 0.930, and two unambiguous items give 0.820. The sweeps use different prototype sets, so only ratios are compared.</figcaption>
</figure>

## Experiment 4: the 18% is not full identification

<p class="experiment-label">Experiment 4</p>

Collapsing the gauge to permutations under T4 requires vertex items for **every** label. LLMJudge does not meet this.

<figure>
  <img src="/column-images/wsdm2027-free-anchors/vertex-coverage-1600.webp" alt="Vertex coverage of the LLMJudge pool" />
  <figcaption><strong>Figure 7.</strong> Minimum ℓ1 distance from any of the 4,423 LLMJudge items to each label vertex. Only label 0 has items on its vertex.</figcaption>
</figure>

Label 0 has items at distance zero, but the closest items for labels 1 to 3 are 0.4848, 0.3030 and 0.6061 away. In every pool slice (top 5%, 10% or 20%) all items sit at the label-0 vertex. The sweep saturates at two items because both constrain the same vertex.

The paper therefore reports this result as **a reduction by anchors at a single vertex**, not as complete identification under T4. The anchors are still effective: under kernel constraints alone the diameter is 2.5118, against 0.3674 with anchors under the same estimator. Anchors for the remaining labels require human effort unless the pool covers every grade.

## Experiment 5: screening before procurement, and estimator checks

<p class="experiment-label">Experiment 5</p>

We tested the binary criterion (two likelihood ratios) on real data after binarising both panels. Across every family subset of LLMJudge and a seeded sample of sixty cases from the second panel, **all 69 predictions matched observation**.

The paper also reports checks on the model and the estimator.

| Expt. | Check | Result |
|---|---|---|
| E5 | Conditional independence across families | In the reference band only at K = 8 |
| E10 | EM prototypes, K = 4, 5, 6, 8 | Diameter invariant for m ≥ 2 |
| E16 | Sampled diameter vs direction budget | Stable from 12,000 to 96,000 |
| E19 | Optimised vs sampled estimate | Optimised about 40% larger |
| E17 | Four family partitions | A later family binds in 2 of 4 (6.96%, 7.34%) |
| E11 | Error vs number of human anchors | Slope −0.581 [−0.660, −0.501] |
| E33 | Binary criterion on real panels | 69/69 correct |

The partitions in E17 that bind are distinctions within one lineage, not new providers. The E11 slope is steeper than −1/2, which the paper attributes to T2 bounding the worst case rather than a particular estimator. A synthetic population (E8) also shows that the negative result of Vossler et al. on the number of score levels and our T1 hold at the same time, so the two results do not contradict each other.

## What we found and what remains open

The study establishes three points.

- Identification is set by **pool composition and the evaluation contract**, not by the number of judges. Under the distribution contract no number of families removes the gauge continuum or the common-confusion floor.
- On two real panels, families after the first gave no reduction above the search resolution, while gold-confirmed unambiguous items reduced the interior diameter by 18.03% (two items) and 5.0% (twelve or more).
- For binary labels, two likelihood ratios decide before procurement whether a candidate family can add identification power (69/69 on real data).

This is not a claim that adding judges is useless. Further judges can reduce the sampling error of finite data even when the identification set does not change; the paper did not measure this. The practical suggestions are to audit the pool and the contract before paying for labels, to screen each candidate family before buying it, and to report the rank screen, the vertex coverage of the pool and the assumed contract next to agreement.

There are limitations. Every diameter is a lower bound from a search, and differences below one percent are not resolved. Absolute diameters depend on how prototypes are built, so only reductions within one construction are comparable. Conditional independence across families is not rejected only at K = 8, while the main measurements use K = 4. Both judge panels follow the point contract, and the distribution contract is tested only on NTCIR-10 INTENT-2, which has no judge panel. On LLMJudge, unambiguous items exist only for label 0, and confirming that a consensus item is a true vertex needs reference labels (50 of the 442 consensus items had a different gold label). The results are therefore no basis for removing human evaluation. Certifying the diameter, rather than bounding it from below, is the next step.

The code, the collected judge labels and the result files behind every number are available at [github.com/keito-git/free-anchors-llm-judge-panels](https://github.com/keito-git/free-anchors-llm-judge-panels).
