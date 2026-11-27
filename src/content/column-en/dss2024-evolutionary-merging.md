---
title: "Can One Merged LLM Handle 15 Sentiment Tasks?"
subtitle: "Multi-Stage Evolutionary Model Merging with Meta Data Driven Curriculum Learning for Sentiment-Specialized Large Language Modeling"
date: "2026-11-27"
excerpt: "We merged 15 task-specific sentiment-analysis LLMs into one model with an evolutionary algorithm, then added an inference-time curriculum that shows tasks from easy to hard. A walk-through of our IEEE DSS 2024 paper, which received the Best Paper Award."
readingMinutes: 11
showImage: false
image: "/column-images/dss2024-evolutionary-merging/framework.png"
imageAlt: "MEM-MCL overview. Task-specific expert models are built in the SFT phase, merged in stages with an evolutionary algorithm in the MEM phase, and used for inference with a difficulty-ordered curriculum in the MCL phase."
authors:
  - name: "Keito Inoshita"
    url: "/en/about/"
    affiliation: "Kansai University"
  - name: "Xiaokang Zhou"
    affiliation: "Kansai University / RIKEN Center for AIP"
  - name: "Akira Kawai"
    affiliation: "Shiga University / Japan Safety Society Research Center"
tldr: "Sentiment analysis covers very different tasks, from positive/negative classification to aspect-level extraction and irony or hate detection. We instruction-tuned Llama 2 with LoRA into 15 task-specific experts and merged them in two evolutionary stages, first within three task groups and then across groups (MEM). Merge weights are selected by performance on 'weak data', the examples each expert got wrong. We then scored each task's difficulty from its meta data (number of classes, data diversity, task complexity, subjectivity) and prompted the merged model with tasks ordered from easy to hard (MCL). The single merged model beats the original Llama 2 on 10 of 15 tasks and beats the task-specific expert on 6. Adding MCL raises the score over MEM on 9 of 15 tasks. The effect is uneven, however: on the easiest SC tasks, MCL lowers the score."
links:
  - label: "Paper (IEEE DSS 2024)"
    url: "https://doi.org/10.1109/dss64273.2024.00018"
citation: |
  @inproceedings{inoshita2024memmcl,
    title     = {Multi-Stage Evolutionary Model Merging with Meta Data Driven
                 Curriculum Learning for Sentiment-Specialized Large Language Modeling},
    author    = {Inoshita, Keito and Zhou, Xiaokang and Kawai, Akira},
    booktitle = {Proceedings of the 10th IEEE DSS},
    pages     = {58--65},
    year      = {2024},
    doi       = {10.1109/dss64273.2024.00018}
  }
---

<div class="teaser">
<div>

Merge

15 experts **merged in two evolutionary stages**. One model beats the original Llama 2 on 10 of 15 tasks.

</div>
<div>

Order

A **difficulty score** from task meta data sets the order of in-context tasks. Over MEM, 9 of 15 tasks improve.

</div>
<div>

Limits

The gains are uneven. **MCL lowers the easiest SC tasks**, and tasks such as MAST-Hate stay below the original Llama 2.

</div>
</div>

This paper was presented at the 10th IEEE DSS in December 2024 and received the Best Paper Award.

## Sentiment analysis is not one task

"Sentiment analysis" covers many different tasks. Sentence-level polarity classification (Sentiment Classification, SC), aspect-based sentiment analysis that links sentiment to targets in the text (ABSA), and the multifaceted analysis of subjective text (MAST), which covers 11 or 28 fine-grained emotions as well as hate, offensiveness and irony, each require a different kind of reading.

Earlier methods usually specialise in one task. Real applications often need several tasks at once, and keeping a separate model for each is costly to operate. A single LLM can handle many tasks, but on sentiment analysis it often falls short of specialised models.

We therefore asked two questions.

1. Can task-specific models be **combined into one model without losing accuracy**?
2. Does **ordering tasks by their meta data** (number of classes, subjectivity and so on) improve accuracy?

## How MEM-MCL works

<figure>
  <img src="/column-images/dss2024-evolutionary-merging/framework-1600.webp" alt="MEM-MCL framework overview" />
  <figcaption><strong>Figure 1.</strong> MEM-MCL overview (Fig. 1 of the paper). From left: the SFT phase builds experts, the MEM phase merges them with an evolutionary algorithm, and the MCL phase runs inference with a difficulty-ordered curriculum.</figcaption>
</figure>

MEM-MCL runs in three phases.

1. **SFT phase.** For each of the 15 sentiment tasks, a prompt is built from the instruction and the input text (plus the aspect or category for ABSA), and Llama 2 with LoRA is instruction-tuned on it. This yields 15 task-specific experts.
2. **MEM phase (Multi-stage Evolutionary Model Merging).** The experts are split into three groups, SC, ABSA and MAST, and merged first within each group and then across groups. Each merge is a weighted sum whose weights are searched by an evolutionary algorithm.
3. **MCL phase (Meta data driven Curriculum Learning).** Each task's difficulty is computed from its meta data. The instruction, input and output of each task are placed in the prompt from easiest to hardest, and the merged model performs inference with this prompt.

### Choosing weights on weak data

<figure>
  <img src="/column-images/dss2024-evolutionary-merging/mem-mechanism-1600.webp" alt="Mechanism of MEM" />
  <figcaption><strong>Figure 2.</strong> The MEM mechanism (Fig. 4 of the paper). The 15 experts are grouped by meta data; the first evolutionary merge builds one model per group, and the second merges the group models into the final model.</figcaption>
</figure>

The key design choice in MEM is the data used to judge a set of weights. Each expert first runs inference on its own training data, and **the examples it gets wrong are kept as "weak data"**. The evolutionary algorithm keeps a population of weight vectors, varies them by crossover and mutation, merges the models with each candidate, and uses accuracy on the weak data as the fitness. The fittest individuals move on to the next generation. Selecting weights that do well on the hard examples is meant to let the experts cover each other's weaknesses.

The main hyperparameters are as follows.

| Phase | Setting | Value |
|---|---|---|
| SFT | Batch size / micro batch size | 64 / 4 |
| SFT | Learning rate / max epochs / weight decay | 3e-4 / 10 / 0.1 |
| SFT | LoRA r / α / dropout | 4 / 16 / 0.05 |
| Merge | Generations / initial population | 10 / 20 |
| Merge | Crossover point / mutation probability | Random / 0.1 |

### Scoring difficulty from meta data

MCL scores each task's difficulty as

**Score = 1.0 × C + 0.5 × V + 2.0 × Z + 5.0 × S**

where C is the number of classes, V the data diversity, Z the task complexity and S whether the task is subjective. The weights follow prior work; subjectivity (irony or hate detection, for example) receives the largest weight, 5.0.

<figure>
  <img src="/column-images/dss2024-evolutionary-merging/difficulty-1600.webp" alt="Task difficulty scores" />
  <figcaption><strong>Figure 3.</strong> Difficulty scores and ranks of the 15 tasks (Table III of the paper). Tasks are presented from the top down. 28-class emotion classification is the hardest; sentence-level binary classification is the easiest. Ranks are as given in Table III; in a few places they do not follow the score, e.g. SC-5class (8) comes before ABSA-TSD (6.5).</figcaption>
</figure>

## Experimental setup

<div class="setup">

**Setup**

- Base model: Llama 2 (7B), instruction-tuned with LoRA
- Tasks: 4 SC, 6 ABSA (ATSA, ACSA, TSD, ASD, ASTE, ASQP) and 5 MAST (11-class, 28-class, Hate, Offensive, Irony), 15 in total
- Test: up to 500 randomly sampled examples per task
- Metrics: Accuracy, Micro-F1 or Macro-F1 depending on the task (all in %)

</div>

| Group | Task | Train | Test | Metric |
|---|---|---|---|---|
| SC | 2class-sen / 2class-doc / 3class / 5class | 6000 / 3000 / 3000 / 15000 | 500 each | Accuracy |
| ABSA | ATSA / ACSA | 1600 / 3000 | 421 / 400 | Accuracy |
| ABSA | TSD / ASD / ASTE / ASQP | 1600 / 1500 / 1500 / 1500 | 421 / 400 / 500 / 500 | Micro-F1 |
| MAST | 11class / 28class | 5000 / 10000 | 500 each | Accuracy |
| MAST | Hate / Offensive / Irony | 9000 / 3000 / 3000 | 500 each | Macro-F1 |

Fig. 7 and Fig. 8 of the paper are bar charts without printed values. The figures in this post are redrawn from the authors' result sheet behind those bars.

## Experiment 1: Does one merged model keep the accuracy?

<p class="experiment-label">Experiment 1</p>

We compared the original Llama 2 (Base), the task-specific experts (Expert) and the single MEM-merged model (MEM) on all 15 tasks.

<figure>
  <img src="/column-images/dss2024-evolutionary-merging/mem-vs-base-expert-1600.webp" alt="Base vs expert vs MEM" />
  <figcaption><strong>Figure 4.</strong> Scores on the 15 tasks (corresponding to Fig. 7 of the paper). Grey is the original Llama 2, blue the task-specific experts and gold the single merged MEM model.</figcaption>
</figure>

MEM beats Base on 10 of 15 tasks. The largest gains are on ATSA (18.76 → 67.22), SC-2class-doc (47.4 → 94.8) and SC-3class (36.8 → 87.6).

Against the experts, MEM is higher on six tasks: ATSA (61.52 → 67.22), ACSA, ASQP, SC-3class, MAST-Hate and MAST-Irony. On several others the gap is very small, such as SC-2class-doc (95.2 vs 94.8) and ASTE (25.2 vs 24.8). A model that covers all 15 tasks stays close to models built for each single task on many of them.

MEM also falls below Base on some tasks: MAST-Hate (38.04 → 25.34), MAST-Irony (63.29 → 59.94), ABSA-TSD, SC-5class and SC-2class-sen. On MAST-Hate the expert itself scores 19.13, below Base, so the task was already difficult at the instruction-tuning stage.

## Experiment 2: Does an easy-to-hard order help?

<p class="experiment-label">Experiment 2</p>

To measure the effect of MCL we compared three conditions: MEM alone (MEM), MEM shown task examples in no particular order (Unstructured), and MEM shown them in order of difficulty (MEM-MCL).

<figure>
  <img src="/column-images/dss2024-evolutionary-merging/mcl-comparison-1600.webp" alt="MEM vs unstructured vs MEM-MCL" />
  <figcaption><strong>Figure 5.</strong> Scores on the 15 tasks (corresponding to Fig. 8 of the paper). Grey is MEM, light is the unordered condition and gold the difficulty-ordered MEM-MCL.</figcaption>
</figure>

MEM-MCL beats MEM on 9 of 15 tasks. The largest gains are on ACSA (9.25 → 19.5), ASD (20.5 → 28.75), MAST-Hate (25.34 → 38.04) and MAST-Offensive (22.29 → 41.73). Against the unordered condition MEM-MCL is higher on 9 tasks, with clear gaps on ATSA (55.34 → 67.93) and MAST-Irony (52.3 → 60.17).

It does not help everywhere. On ASD the unordered condition (31.5) scores higher than MEM-MCL (28.75), and on MAST-Hate the two are tied at 38.04.

## Experiment 3: Where it helps and where it hurts

<p class="experiment-label">Experiment 3</p>

We re-sorted the change from MEM to MEM-MCL by curriculum order, from easiest to hardest.

<figure>
  <img src="/column-images/dss2024-evolutionary-merging/mcl-delta-1600.webp" alt="Change from MEM to MEM-MCL" />
  <figcaption><strong>Figure 6.</strong> Difference between MEM-MCL and MEM (points). Tasks are sorted by difficulty rank, easiest at the top. All three of the easiest SC tasks go down.</figcaption>
</figure>

On the three easiest tasks (SC-2class-sen, SC-2class-doc and SC-3class), MCL lowers the score by 3.2 to 7.4 points. The paper also notes that MEM beats MEM-MCL on some SC tasks and that the effect of MCL may be limited for certain tasks. The gains come mainly from the mid-ranked ABSA tasks and from MAST-Hate and MAST-Offensive.

Finally, the win counts over the 15 tasks.

<figure>
  <img src="/column-images/dss2024-evolutionary-merging/win-counts-1600.webp" alt="Win counts over 15 tasks" />
  <figcaption><strong>Figure 7.</strong> Number of tasks, out of 15, on which the first model scores higher. The MAST-Hate tie (38.04) is not counted as a win.</figcaption>
</figure>

## What we know and what we don't

The study shows two things.

- Merging 15 task-specific experts into one model by evolutionary merging on weak data beats the original LLM on most tasks and stays close to the experts.
- An inference-time curriculum that orders tasks by a meta-data difficulty score improves accuracy on 9 of 15 tasks.

The paper also lists open problems.

- On tasks with strong label imbalance such as MAST-Hate, the small 7B model sometimes failed to follow the output format, likely due to both model size and task complexity.
- The merging effect is not uniform, and some tasks remain below the base model. The weighting or the algorithm may not be tuned well enough for complex or subjective tasks.
- The difficulty weights (1.0, 0.5, 2.0, 5.0) are set heuristically from prior work and are not optimised.

In addition, each task is tested on at most 500 examples, and the paper does not report variance over seeds or statistical tests. Wins and losses on tasks with small gaps should be read with care.

Next, we plan to optimise the evolutionary algorithm and to set the curriculum weights automatically from per-task performance.
