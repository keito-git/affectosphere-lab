---
title: "How Do We Deploy LLMs When They Give Labels but Not Uncertainty?"
subtitle: "「LLMはラベルを出すが不確実性は出さない」という壁をどう越えるか -主観的判断タスクへの生成AI導入における実装・運用プラクティス-"
date: "2026-11-27"
excerpt: "Put an LLM on emotion classification or sarcasm detection and it returns plausible labels, but not whether humans would disagree on the case. From trial and error across four research projects, this paper distils seven practices and a checklist for getting past that wall. A walk-through of our paper accepted in the IPSJ Journal of Digital Practices (in Japanese)."
readingMinutes: 11
showImage: false
image: "/column-images/ipsj-dp-llm-uncertainty/overview.png"
imageAlt: "The LLM deployment pipeline for subjective tasks (data preparation, evaluation design, model operation, decision making, social acceptance) and where the seven practices sit."
authors:
  - name: "Keito Inoshita"
    url: "/en/about/"
    affiliation: "Kansai University"
tldr: "When LLMs are used for subjective judgement tasks such as emotion classification or sarcasm detection, they output plausible labels but do not show whether a case is one where humans disagree or one the model simply does not know. This Japanese-language practice paper organises the implementation and operational trial and error from four research projects and places seven practices along the deployment pipeline. The core ones: treat uncertainty as a distribution; know that label-oriented and distribution-oriented calibration are different things; estimate cost at design time; decide whether to let the LLM take over by the type of instance; and explain uncertainty in the receiver's terms. The paper claims no technical novelty; it is a record of field knowledge."
links:
  - label: "Paper (IPSJ Digital Practice, accepted)"
    url: "https://lab.affectosphere.group/en/news/20260916-ipsj-dp-uncertainty/"
citation: |
  @article{inoshita2027dp,
    title   = {「{LLM}はラベルを出すが不確実性は出さない」という壁をどう越えるか
               -主観的判断タスクへの生成{AI}導入における実装・運用プラクティス-},
    author  = {井下 敬翔},
    journal = {情報処理学会論文誌デジタルプラクティス},
    year    = {2027},
    note    = {採録決定，掲載予定}
  }
---

<div class="teaser">
<div>

Distribution

Cases where humans disagree carry the most information. Evaluate against **the distribution of judgements**, not the majority label.

</div>
<div>

Calibration

Temperature scaling improved ECE by **about 59%** but made the gap to the human distribution worse. Calibration means choosing which fit to improve.

</div>
<div>

Review

A feed that required human review stopped after **6 articles**. The bottleneck was neither accuracy nor price but keeping reviewers available.

</div>
</div>

## What is the "uncertainty wall"?

Generative AI is automating subjective judgements: emotion classification, sarcasm detection, stance and intent. In these tasks **human annotators themselves disagree**. A growing view, known as human label variation, holds that this disagreement is information inherent to the task, not noise to remove.

An LLM, however, returns one plausible label and has trouble expressing the uncertainty behind it: is this a case where humans split, or one the model does not know? The paper calls this the **uncertainty wall**, which appears at the technical, operational, decision-making and social-acceptance stages alike. No single technique removes it; it takes accumulated implementation and operational know-how.

## How the paper is built

<figure>
  <img src="/column-images/ipsj-dp-llm-uncertainty/overview-1600.webp" alt="Pipeline and seven practices" />
  <figcaption><strong>Figure 1.</strong> The LLM deployment pipeline for subjective tasks and the seven practices (Figure 1 of the paper, redrawn in English).</figcaption>
</figure>

The paper extracts seven practices along the deployment pipeline from four research projects the author worked on. Each practice is written in three parts: what we learned only by doing it, the generalised lesson, and implications for implementation and operation.

| ID | Project | Content |
|---|---|---|
| A1 | Affective computing survey | Organises the field as a six-layer pipeline, diagnoses cross-layer disconnections and proposes five design criteria |
| A2 | Human vs LLM emotion judgements | Compares the judgement distributions of four LLMs with humans over about 640,000 responses |
| A3 | MCMC uncertainty decomposition | Splits emotion-classification uncertainty into aleatoric (task ambiguity) and epistemic (model ignorance) |
| A4 | EDL sarcasm detection | Uses evidential deep learning to output predictions and uncertainty together |

<figure>
  <img src="/column-images/ipsj-dp-llm-uncertainty/projects-1600.webp" alt="Projects and practices" />
  <figcaption><strong>Figure 2.</strong> Which project grounds which practice, from Section 2 of the paper.</figcaption>
</figure>

The paper focuses on P1, P2, P3, P6 and P7, where field knowledge is richest, and only outlines P4 (dataset selection) and P5 (metric design). The five main practices follow.

## P1: Treat uncertainty as a distribution, not label agreement

<p class="experiment-label">Practice 1</p>

Early in A2, evaluation rested on accuracy, F1 and Cohen's κ: if the LLM matched the human majority label, that seemed good enough. An interim tally showed the problem: **the cases where humans split were exactly the ones the table could not show**. If annotators were divided and the LLM piled onto one category, it still counted as correct as long as it matched the majority.

Evaluation was switched to Jensen–Shannon divergence (JSD) and distribution entropy. In A2, LLMs approached humans on majority-label agreement but deviated systematically in distribution (JSD of 0.45 or more), and scaling the model did not close the gap. A RoBERTa model fine-tuned on the target data brought JSD down to about 0.10 on cases where all annotators agreed.

Another finding: the model that looked best on the aggregate metric was earning its score by conservatively leaning toward the neutral category. Selecting on the aggregate alone would have put that behaviour into production.

**Generalised lesson.** Do not make majority-label agreement the main criterion. Keep per-annotator labels from the start, because majority-aggregated data cannot be turned back into distributions. Use aggregate metrics together with per-category profiles. Where possible, split uncertainty into aleatoric and epistemic: high-aleatoric cases will not improve with more training, while high-epistemic ones may improve with more data, so the remedies differ.

## P2: Label-oriented and distribution-oriented calibration are different

<p class="experiment-label">Practice 2</p>

A2 tried three post-hoc calibration methods (temperature scaling, bias correction, isotonic regression). The best reduced JSD by only 12–14% in three models and made it worse in another. None came close to the fine-tuned model.

The decisive observation came from A3. The expectation was that better calibration against correct labels would also bring the model closer to the human distribution. Instead, **temperature scaling improved ECE by about 59% while making JSD to the human distribution worse**. Suspecting a bug, the experiment was re-run with several seeds; the conclusion held.

<figure>
  <img src="/column-images/ipsj-dp-llm-uncertainty/calibration-1600.webp" alt="Two calibration targets" />
  <figcaption><strong>Figure 3.</strong> The direction of calibration observed in A3. The paper reports the ECE improvement (about 59%) but not the size of the JSD deterioration, so only its direction is shown.</figcaption>
</figure>

**Generalised lesson.** Calibration is not post-processing that tidies probabilities; it is **a design choice about which fit to improve**. Decide first whether the application needs confident labels or faithful distributions. Do not apply one calibration method uniformly to all models. Compare at least two methods side by side and check for per-category degradation. Trusting ECE alone gives a false sense of safety in distribution-oriented use.

## P3: Estimate cost at design time

<p class="experiment-label">Practice 3</p>

The A2 experiments took about a week, but at the planning stage the API cost estimate was decisive. A rough calculation showed that the initial number of samples per temperature would not fit the budget, so the number was cut and a bootstrap check confirmed that it was still statistically sufficient. Mixing commercial APIs with open-source models showed that open-source models win on unit price but add work in inference speed, output-format variance and batching. Retry with backoff and centralised logging were added after the fact, which affected reproducibility; they should have been in place before the experiment.

**Generalised lesson.** Start by estimating total calls × unit price; samples, temperatures, models and data size multiply quickly. Compare APIs on total cost including implementation effort, not unit price alone. Set sample sizes against statistical power. Treat retry, rate-limit handling and logging as prerequisites for reproducibility and recovery in high-volume use, not as conveniences.

## P6: Decide what the LLM takes over by the type of instance

<p class="experiment-label">Practice 6</p>

Early in A2, substitution was judged by a single accuracy level. By category, however, the LLM matched humans almost perfectly on some and was nearly uncorrelated on others. A measure of how explicitly an emotion category shows up in vocabulary (the Lexical Transparency Score) was developed; it predicts per-category human–LLM agreement with a rank correlation of 0.51.

| Lexical transparency | Example categories | Recommended use |
|---|---|---|
| High | Joy, gratitude, remorse, sadness | LLM can take over; calibrate afterwards if needed |
| Low | Neutral, approval, realisation, relief | No LLM-only use; human verification required |

Combined with methods such as the EDL model in A4, which give a confidence per instance, one can stratify in advance and route individual cases afterwards. The basic form is a **hybrid design**: the LLM makes a first pass, and only uncertain cases go to human review.

The paper also records one operational experience outside the four projects: a pipeline the author runs to produce and publish daily content with generative AI.

<figure>
  <img src="/column-images/ipsj-dp-llm-uncertainty/review-bottleneck-1600.webp" alt="Human-review bottleneck" />
  <figcaption><strong>Figure 4.</strong> Articles published by two feeds run in parallel. The children's feed involves a subjective judgement of appropriateness, so every article had to be reviewed by a person before publication; reviewers could not be kept available, and it stopped after its first 6 articles.</figcaption>
</figure>

The lesson is that **the bottleneck of a hybrid design is neither model accuracy nor price per call, but whether human review can be sustained**. If the P3 cost estimate leaves out review effort, the problem appears after launch as a stoppage. When human review is mandatory, estimate the number of cases and the time per case at design time, and set the routing threshold so the load stays sustainable.

## P7: Explain uncertainty in the receiver's terms

<p class="experiment-label">Practice 7</p>

When results were shown to co-authors and colleagues in neighbouring fields, technical descriptions of uncertainty repeatedly drew the same response: what does this number mean, and can I trust it? Adding more explanation did not help.

What worked was showing it per instance ("the model is unsure about this case"), simplifying to three levels (high, medium, low), and saying **"humans disagree on this case"** rather than "the model might be wrong". With that last framing, the discussion moved from "can we trust this model?" to "how should we handle this case?".

**Generalised lesson.** Translate uncertainty metrics into the receiver's words. Keep technical detail in a separate expert view. Present uncertainty as a property of the task rather than a defect of the model, so the receiver keeps the authority to judge. Build the presentation in from the start, since it affects output formats, data structures and the UI.

## A checklist for practitioners

Each practice has a fixed point in time at which it must be checked. "Did the metrics include a distribution distance?" cannot be fixed once data collection is over.

<figure>
  <img src="/column-images/ipsj-dp-llm-uncertainty/checklist-1600.webp" alt="Stage-by-stage checklist" />
  <figcaption><strong>Figure 5.</strong> The stage-by-stage checklist for LLM deployment (the paper's table, redrawn in English). The label at bottom right of each item is the corresponding practice.</figcaption>
</figure>

The paper also considers how the practices would apply in business (sentiment analysis of customer reviews), education (monitoring learners' emotions) and healthcare (supporting self-monitoring of mood logs). These are **conceptual scenarios**, not tested deployments.

<figure>
  <img src="/column-images/ipsj-dp-llm-uncertainty/scenarios-1600.webp" alt="Application scenarios" />
  <figcaption><strong>Figure 6.</strong> Practices used in the three scenarios, from the paper's table. Blue marks institutional and ethical prerequisites that the seven practices cannot cover. All effects are expected, not observed.</figcaption>
</figure>

All three scenarios follow the same order: evaluation design (P1, P2, P5) makes gaps visible, division of labour (P6) routes the remaining risk to people, and explanation (P7) keeps the decision with people. The tolerable severity of errors differs, though: business can correct afterwards, while healthcare leaves little room to defer human judgement, so the level of implementation should follow the domain's risk tolerance. For education and healthcare, the paper notes prerequisites that technology cannot solve, such as consent, data minimisation, medical-device regulation and the handling of sensitive personal data, which must be designed in from the start.

## What we know and what we don't

The paper's central lessons are:

- In subjective tasks, handle uncertainty as **the distribution of human judgements**, not agreement with the majority label.
- **Aggregate and distributional metrics are independent**, and improving one can worsen the other. Decide which one to calibrate for before calibrating.
- Decide what the LLM takes over **by instance type**, not by overall accuracy, and design for sustainable human review.

The limits are stated. The knowledge comes mainly from emotion classification and sarcasm detection, and generalisation to other subjective tasks is untested. The underlying studies use mostly English data; Japanese and multilingual settings, including the lexical-transparency measure, need re-validation. The three-domain scenarios are thought experiments without real-world validation. The operational experience in P6 is a real observation but a single one, not a systematic test of the seven practices. And the paper reflects one perspective; other settings may prioritise other practices.
