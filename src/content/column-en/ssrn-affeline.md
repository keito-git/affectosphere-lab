---
title: "Can One Model Handle Fifteen Text Emotion Tasks?"
subtitle: "Affeline: A Late-Read Foundation Model for Transferable Text Emotion Understanding"
date: "2026-11-27"
excerpt: "We built Affeline, a model that learns fifteen text emotion tasks, from polarity and discrete emotions to sarcasm and intensity regression, with one set of weights. Overall it is on par with same-capacity specialists, and its representation transfers to tasks it was never trained on. A walk-through of our SSRN preprint."
readingMinutes: 13
showImage: false
image: "/column-images/ssrn-affeline/architecture.png"
imageAlt: "Affeline architecture. Fifteen tasks are sampled uniformly; the input places the channel and a [READ] token after the body text; a frozen Qwen3-8B-Base with LoRA processes it; the last-layer state at [READ] goes to per-task linear heads."
authors:
  - name: "Keito Inoshita"
    url: "/en/about/"
    affiliation: "Kansai University"
tldr: "Text emotion recognition has been split task by task, with polarity, discrete emotions, sarcasm and intensity regression each handled by a separate model. Affeline learns fifteen English and Japanese tasks with one set of weights. Its input places the task channel after the body text, so under causal masking the body representation is provably independent of the channel. Against same-capacity specialists it is on par overall (7 of 15 wins, sign test p = 1.0). It tends to gain on low-resource tasks and lose a little on high-resource ones, but the trend is not significant. On tasks held out of training, a linear head on the frozen representation far exceeds the base model. Given the label names, no task identifier is needed."
links:
  - label: "Preprint (SSRN)"
    url: "https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7685008"
  - label: "Model (Hugging Face)"
    url: "https://huggingface.co/Affectosphere-Group/Affeline-1-8B"
citation: |
  @misc{inoshita2026affeline,
    title        = {Affeline: A Late-Read Foundation Model for Transferable Text
                    Emotion Understanding},
    author       = {Inoshita, Keito},
    howpublished = {SSRN preprint, abstract id 7685008},
    year         = {2026}
  }
---

<div class="teaser">
<div>

Share

Fifteen tasks, one set of weights. Against same-capacity specialists it wins **7 of 15**: on par overall.

</div>
<div>

Late-Read

With the channel after the body, the body representation does not depend on it. **Performance is essentially unchanged** (6/15 wins, mean difference −0.0030).

</div>
<div>

Transfer

On a task never trained on, **1% of the labels** give a TweetEval-Emotion macro-F1 of 0.716 (base model: 0.233).

</div>
</div>

## Emotion tasks sit in separate drawers

Reading emotion from text is becoming a tool for interpreting data in psychology, education, medicine, economics and sociology. Researchers in these fields do not need the model with the top score on one benchmark. They need a tool that returns a stable judgment on their own text, whose output they can interpret, and that works in their language.

Emotion recognition, however, has grown task by task. Polarity classification, sarcasm detection and emotion-intensity regression each have their own models and their own input and output conventions. A user who wants to look at several facets must deploy and maintain several models. Recent work has started to treat several tasks with one model, but the targets concentrate on classification and intensity regression. Interpersonal tasks such as sarcasm and aggression, and aspect-level tasks, are rarely handled together, and evaluation is heavily skewed toward English.

So we did not just ask whether one model can solve the tasks. We asked four questions.

1. How far does a single model preserve per-task performance relative to a task-specific model?
2. Does the model need to be told which task it is solving?
3. Where do metric definitions silently break when many tasks are evaluated together?
4. Does the learned representation transfer to tasks that were never part of training?

## How Affeline works

<figure>
  <img src="/column-images/ssrn-affeline/architecture-1600.webp" alt="Affeline architecture" />
  <figcaption><strong>Figure 1.</strong> Affeline architecture (Figure 1 of the paper). Fifteen tasks are sampled uniformly, the Late-Read input is processed by a frozen Qwen3-8B-Base with LoRA, and the last-layer state at the [READ] position goes to a per-task linear head.</figcaption>
</figure>

Affeline has four parts.

- **Base model**: Qwen3-8B-Base is frozen. LoRA (r = 32, α = 64) is applied to all seven linear projections of each block. The learned parameters amount to 88.7M, or 355 MB on disk.
- **Outputs**: each task has one linear head. Single-label classification uses cross-entropy, multi-label classification uses binary cross-entropy, and regression uses mean squared error.
- **Task mixing**: training sizes differ about 48-fold across tasks. To keep the large tasks from dominating, the fifteen tasks are sampled uniformly (temperature α = 0).
- **Late-Read input**: a channel listing the task's label names is placed after the body text, followed by a [READ] token. The last-layer hidden state at [READ] (4,096 dimensions) is the readout.

<figure>
  <img src="/column-images/ssrn-affeline/late-read-1600.webp" alt="Late-Read input format and causal mask" />
  <figcaption><strong>Figure 2.</strong> The Late-Read format and the causal mask (Figure 2 of the paper). (a) In the conventional format the channel comes before the body, so the body representation depends on it. Late-Read places the channel after the body. (b) Under the causal mask, body tokens cannot attend to the channel or [READ], while [READ] attends to everything.</figcaption>
</figure>

The key to Late-Read is the causal mask of a decoder-only Transformer. Each position can attend only to earlier positions, so body tokens never see the channel. Whatever channel is given, the body hidden states are therefore identical (Proposition 1 in the paper). This is a structural property that holds without any training. The final [READ] token, in contrast, attends to both the body and the channel, so the readout is still conditioned on the task.

Training uses three seeds. Each seed gets the same fixed budget, and the weights of the last three epochs are averaged. Early stopping on a 15-task development composite would be dragged by the noise of development sets that hold only tens of examples.

## Experiment 1: How does it compare with specialists?

<p class="experiment-label">Experiment 1</p>

<div class="setup">

**Setup**

- Tasks: 15 in total, 13 English and 2 Japanese (WRIME reader and writer). Training sizes range from 1,584 (FinancialPhraseBank) to 76,673 (EmpatheticDialogues)
- Reference: same-capacity specialists, i.e. the same Qwen3-8B-Base with LoRA trained separately per task. Convergence verified by update counts and development curves
- Evaluation: each task's official primary metric. The same three seeds on both sides, so each per-task gain has a 95% confidence interval
- Statistics: two-sided sign test with the task as unit; Mann–Whitney U test between low- and high-resource groups

</div>

<figure>
  <img src="/column-images/ssrn-affeline/per-task-gain-1600.webp" alt="Per-task gain over same-capacity specialists" />
  <figcaption><strong>Figure 3.</strong> Per-task difference (Affeline − specialist) with 95% CI; right means Affeline is better. Amber marks tasks with at most 4,000 training examples, blue the larger ones (Table 3 of the paper).</figcaption>
</figure>

Affeline is better on 7 of the 15 tasks. The sign test gives p = 1.0000, so neither side has an overall advantage.

Where the interval excludes zero, the specialist leads on high-resource tasks such as GoEmotions, WRIME reader and EI-reg, and Affeline leads on irony detection. The largest gap is on EI-reg, at −0.0539.

<figure>
  <img src="/column-images/ssrn-affeline/resource-groups-1600.webp" alt="Gain by resource group" />
  <figcaption><strong>Figure 4.</strong> Mean difference by resource group: +0.0064 on low-resource tasks (5 of 7 wins) and −0.0106 on high-resource tasks (2 of 8 wins). The separation is not significant.</figcaption>
</figure>

There is a pattern: a gain where data are scarce and a small cost where data are abundant. The Mann–Whitney U test gives p = 0.1325, however, so the paper reports this as a descriptive trend, not a demonstrated interaction.

The pattern also leans heavily on one task. The irony specialist does not train stably under the shared recipe and early-stops at a volatile optimum. Without irony, the low-resource tasks change by only −0.0001 on average (4 of 6 wins), and the group separation is p = 0.2453.

Treating training size as continuous gives the same picture. The Spearman correlation between the normalized gain and log training size is −0.136 (p = 0.6214): same direction, not significant. When each score is normalized so that the constant predictor is 0 and the best of the three models is 1, Affeline averages 0.9792 against 0.9849 for the specialists, and 13 of 15 tasks fall within a prespecified margin of δ = 0.05.

This comparison is itself a correction. An earlier version of the work compared against task-specific baselines that, under an exploratory budget, received very few updates (on the order of ten for stance detection). Smaller tasks received fewer updates, so under-training was correlated with training size and produced an apparently large low-resource gain. The paper retracts that estimate and uses specialists whose convergence has been checked.

## Experiment 2: Does it transfer to unseen tasks?

<p class="experiment-label">Experiment 2</p>

<div class="setup">

**Setup**

- Retrain on 12 tasks, holding out three: TweetEval-Emotion (discrete emotion), EmoBank (dimensional regression) and HateXplain (interpersonal)
- Using 1%, 5%, 10% or 100% of a held-out task's labels, train a single linear head on the frozen representation (Adam, fixed 300 steps, no early stopping)
- Baseline: the identical probe on the plain Qwen3-8B-Base representation, with LoRA disabled
- 3 seeds

</div>

<figure>
  <img src="/column-images/ssrn-affeline/transfer-1600.webp" alt="Few-shot transfer to held-out tasks" />
  <figcaption><strong>Figure 5.</strong> Transfer to three tasks held out of training. Amber is the frozen Affeline representation, grey the plain base model, and the dotted line the same-capacity specialist. EmoBank is MAE, so lower is better.</figcaption>
</figure>

At every data budget the Affeline representation beats the plain base model.

| Held-out task | Representation | 1% | 5% | 10% | 100% | Specialist |
|---|---|---|---|---|---|---|
| TweetEval-Emotion (macro-F1) | Affeline | 0.716 | 0.779 | 0.795 | 0.809 | 0.830 |
| | Qwen3-base | 0.233 | 0.264 | 0.310 | 0.430 | |
| EmoBank (MAE, lower is better) | Affeline | 0.447 | 0.297 | 0.264 | 0.208 | 0.152 |
| | Qwen3-base | 0.559 | 0.446 | 0.394 | 0.290 | |
| HateXplain (macro-F1) | Affeline | 0.564 | 0.586 | 0.596 | 0.656 | 0.694 |
| | Qwen3-base | 0.367 | 0.427 | 0.436 | 0.510 | |

On TweetEval-Emotion, 1% of the labels already gives 0.716, far above the plain representation (0.233). With all labels it reaches 0.809, close to the 0.830 of a specialist that adapts the whole backbone, while only a linear head is trained. The affective representation is learned once and carries to new tasks. The advantage is largest in the few-label regime, which is where a user cannot afford to train a specialist.

## Experiment 3: Does Late-Read cost performance?

<p class="experiment-label">Experiment 3</p>

Late-Read guarantees that the body representation is independent of the channel. We need to check that this does not cost performance. We compared it with the conventional early-channel format, which places the channel before the body, at the same configuration. The early-channel variant was trained with one seed.

<figure>
  <img src="/column-images/ssrn-affeline/late-vs-early-1600.webp" alt="Late-Read versus early-channel" />
  <figcaption><strong>Figure 6.</strong> Late-Read minus early-channel, computed from Table 4 of the paper. The sign is flipped for EmoBank (MAE), so right means Late-Read is better.</figcaption>
</figure>

Late-Read is ahead on 6 of 15 tasks, with a mean difference of −0.0030. Early-channel is ahead on GoEmotions (−0.0169) and EI-reg (−0.0259); Late-Read is ahead on, for example, FinancialPhraseBank (+0.0105). Overall the two are indistinguishable, and the paper concludes that moving the channel after the body costs essentially nothing. The value of Late-Read is not a performance gain but the proven guarantee that the body representation does not depend on the channel.

## Experiment 4: Is a task identifier needed?

<p class="experiment-label">Experiment 4</p>

We predicted in advance that writing a dataset identifier into the channel would reduce interference between tasks with different annotation conventions. We compared a condition with the identifier against one with label names only.

| Condition | Wins (of 15) | Dev composite | Sign-test p |
|---|---|---|---|
| With task identifier | 12 | 0.6669 | 0.0352 |
| Label names only (Affeline) | 3 | 0.6672 | |

Per task, the identifier is ahead on 12 tasks, a mean difference of +0.0054. The development composite used for model selection, however, is 0.6672 without the identifier and 0.6669 with it, so the identifier does not improve the quantity on which the model is chosen. Affeline therefore uses label names only.

For a user, this means that specifying the candidate output labels is enough; there is no need to declare which dataset the task comes from. The label set still selects the head, so the claim is not that the model runs entirely task-free. Two explanations fit: the set of label names may already identify the task almost uniquely, or the LLM may distinguish the task from the input distribution. The present design cannot separate them.

The readout depth and the sampling temperature were also chosen on the development set (one seed each).

| Sampling temperature α | Normalized composite | Low-resource | High-resource |
|---|---|---|---|
| 0.0 (adopted) | 0.9825 | 0.9942 | 0.9722 |
| 0.25 | 0.9810 | 0.9925 | 0.9710 |
| 0.5 | 0.9802 | 0.9942 | 0.9680 |
| 0.75 | 0.9696 | 0.9847 | 0.9565 |
| 1.0 | 0.9698 | 0.9836 | 0.9577 |

Reading only the last layer (0.9825) was also better than concatenating several depths (0.9676–0.9726).

## Experiment 5: Where does the error come from?

<p class="experiment-label">Experiment 5</p>

WRIME labels each sentence twice: with the writer's own emotion and with the emotion a reader perceived. The gap between the two is a per-sentence measure of annotation disagreement. We related the model's error to this gap on the 2,500 test sentences.

<figure>
  <img src="/column-images/ssrn-affeline/wrime-disagreement-1600.webp" alt="Error versus reader-writer disagreement on WRIME" />
  <figcaption><strong>Figure 7.</strong> Mean per-sentence error on the least- and most-disagreeing thirds of the WRIME test sentences. The more the reader and writer disagree, the larger the error.</figcaption>
</figure>

The Spearman correlation between per-sentence error and the reader–writer gap is +0.307 on the reader task and +0.621 on the writer task (p < 0.001 for both). On the writer task, the mean error rises from 0.3372 on the least-disagreeing third to 0.6262 on the most-disagreeing third. Part of what looks like model error is the variation that the annotation itself carries.

## Experiment 6: The metric can change the conclusion

<p class="experiment-label">Experiment 6</p>

While evaluating fifteen tasks, we repeatedly found the definition and the implementation of a metric diverging in ways that could reverse a conclusion. The paper treats this as a structural weakness of cross-task evaluation, not as isolated bugs.

| Case | What happened |
|---|---|
| Zero-inflated regression (WRIME) | Over 70% of labels are zero, so shrinking predictions toward zero improves the MAE. On the writer task, both models look nearly identical to an all-zero predictor under MAE, but under Pearson correlation both are clearly learning |
| Stance detection | The official metric is the mean of the FAVOR and AGAINST F1, but one implementation returned a 3-class macro-F1. The config named the right metric, but no code computed it, so it fell back silently to a default |
| SemEval-2025 Track B | A 0–3 intensity regression had been implemented as a binary classification |

The paper gives three checks. Verify at run time that the registered primary metric is the one actually computed, and never allow a silent fallback. Report a constant-predictor score for every task. Before comparing with a published value, confirm the metric definition and the test split against the primary source. Applying these checks cut the number of published values we could claim to exceed from four to one. Against external values, Affeline stays below the 13B EmoLLMs on EI-reg and is competitive with the best published TweetEval-Emotion result.

## What we found and what remains open

What this study shows:

- Learning fifteen text emotion tasks with one set of weights is on par overall with same-capacity specialists. There is a tendency to gain on low-resource tasks, but it is not significant and leans heavily on irony detection.
- The frozen representation transfers to tasks held out of training and beats the plain base model by a wide margin even with 1% of the labels.
- The Late-Read format guarantees that the body representation is independent of the channel at almost no cost in performance.
- Given the label names, no task identifier is needed.
- Cross-task evaluation has at least three routes by which a metric silently breaks, and each has a check.

There are limits. The main comparison uses three seeds, which gives limited power for per-task tests, so the paper argues from confidence intervals. The overall result is parity, not uniform improvement. The readout-depth and temperature ablations use one seed. Evaluation covers English and Japanese only, so multilingual performance is not established. The identifier result is shown at the 8B scale only. Primary-source values matching both metric and split could be confirmed for only a few tasks, so external calibration is narrow. The run records lack a commit hash, so the exact training code cannot be pinned.

Next steps are to characterize whether the model is reliable enough to be a research instrument (calibration, out-of-distribution behavior, robustness), to adapt the frozen representation to new tasks with parameter-efficient few-shot learning, to add seeds, and to release a lightweight, commercially licensed variant together with the evaluation suite.

The model (adapter weights, per-task heads, [READ] embedding delta, inference package and per-task scoring code) is available for research use on [Hugging Face](https://huggingface.co/Affectosphere-Group/Affeline-1-8B) under CC BY-NC 4.0. No training text is redistributed. The training and evaluation code is available from the author on request.
