---
title: "Where Does LLM Context Actually Help Emotion Recognition?"
subtitle: "ACE-Net: Diagnosing Learned Deep Prior Injection for Fine-Grained Emotion Recognition in Under-Determined Texts"
date: "2026-11-27"
excerpt: "We injected LLM-distilled context into the middle of an emotion classifier to help with short texts that contain no emotion words. What mattered was not the content of the context but the depth at which it was injected. A walk-through of our Knowledge-Based Systems paper."
readingMinutes: 15
showImage: false
image: "/column-images/ace-net/architecture.png"
imageAlt: "ACE-Net architecture. Offline, LLM-written context descriptions are clustered into a frozen dictionary of 32 prototypes; at run time a context vector is added to an intermediate layer."
authors:
  - name: "Keito Inoshita"
    url: "/en/about/"
    affiliation: "Kansai University"
tldr: "88.8% of the GoEmotions test texts contain no emotion word. ACE-Net clusters LLM-written context descriptions into 32 frozen prototypes and injects them into an intermediate Transformer layer, improving macro-F1 by +0.041. When we took it apart, however, none of the dictionary content, the discrete selection or the adaptive temperature mattered on its own. The gain is almost fully explained by a single learned vector placed in a middle layer. We also identify where it helps (middle layers), which inputs it helps (context-deficient ones), and introduce FORGE-Ω, a signal that flags those inputs before deployment."
links:
  - label: "Paper (KBS, accepted)"
    url: "https://lab.affectosphere.group/en/news/20261124-kbs-ace-net/"
  - label: "Code"
    url: "https://github.com/keito-git/ace-net"
  - label: "Data"
    url: "https://doi.org/10.5281/zenodo.23415199"
citation: |
  @article{inoshita2026acenet,
    title   = {{ACE-Net}: Diagnosing Learned Deep Prior Injection for Fine-Grained
               Emotion Recognition in Under-Determined Texts},
    author  = {Inoshita, Keito},
    journal = {Knowledge-Based Systems},
    year    = {2026},
    note    = {Accepted, to appear}
  }
---

<div class="teaser">
<div>

Diagnose

The gain is **one learned vector**. The full model scores 0.4965; a single vector alone scores 0.4960.

</div>
<div>

Locate

It works in the **middle layers (L5–L8)**. Injected near the top, it falls below the baseline.

</div>
<div>

Select

It helps **only context-deficient text**: +0.041 on GoEmotions, −0.001 (n.s.) on ISEAR, where context is in the text.

</div>
</div>

## Reading text that has no emotion words

Emotion recognition from short social-media posts has moved to fine-grained label sets such as the 28 emotions of GoEmotions. A basic difficulty is text that **contains no emotion word at all**. Of the 5,427 GoEmotions test texts, 4,817 (88.8%) have no explicit emotion word. Missing context is the normal case, not the exception.

The obvious fix is to ask an LLM for background and append it to the input. When we appended GPT-4o-mini context, however, macro-F1 went from 0.4559 to 0.4552: no improvement. A RAG variant that retrieves TF-IDF neighbours reached 0.452.

So we changed the question. Instead of asking whether to add context, we asked **when, where and in what form adding it helps**.

## How ACE-Net works

<figure>
  <img src="/column-images/ace-net/architecture-1600.webp" alt="ACE-Net architecture" />
  <figcaption><strong>Figure 1.</strong> ACE-Net. Top: the offline dictionary construction. Bottom: injection at run time. No LLM is called at inference.</figcaption>
</figure>

ACE-Net runs in two stages.

1. **Offline, once.** We sample 3,500 training texts and ask GPT-4o-mini for background that would help interpret each one's emotion. The descriptions are embedded with DeBERTa and clustered by K-means into 32 prototypes, which are then frozen. No emotion labels are used.
2. **At run time.** A small head decides, per input, how to mix the 32 prototypes (Gumbel-Softmax), and the resulting context vector is added to every token of the ninth layer (L = 8, 0-based). The sharpness of the mixing (the temperature) also adapts to how ambiguous the input is.

The module adds 25,377 trainable parameters, about 50k including the frozen dictionary, or +0.06% of the backbone. Inference is a single forward pass.

We built it so that **the dictionary content, the selection, the temperature and the injection layer can each be isolated**. The goal was to find out which part does the work, not to top a leaderboard.

## Experiment 1: Does it help at all?

<p class="experiment-label">Experiment 1</p>

<div class="setup">

**Setup**

- Data: GoEmotions (58,009 Reddit comments, 28 emotions, multi-label)
- Backbone: DeBERTa-v3-base for every condition
- Metric: macro-F1, mean and std over five seeds (42 / 123 / 456 / 789 / 1024)
- Compared with: no context (A1), RAG (A2), concatenated LLM context (A3), self-training (A4), one-token prefix-tuning (A6)

</div>

<figure>
  <img src="/column-images/ace-net/main-results-1600.webp" alt="Main results on GoEmotions" />
  <figcaption><strong>Figure 2.</strong> GoEmotions macro-F1. The dashed line is the no-context baseline (A1). The three grey bars are existing ways of adding context, and all sit at the baseline. Zero-shot CoT with GPT-4o-mini (A5) scores 0.3099 and is left off the axis.</figcaption>
</figure>

ACE-Net reaches 0.4965, +0.041 over the baseline. Concatenating the context as text (A3) does not help, so **the same LLM context helps once it is distilled and injected into a middle layer**.

The blue bar is the interesting one. Prefix-tuning with a single learnable token (A6) reaches 0.5037, with no significant difference from ACE-Net (Welch p = 0.14). A method with no dictionary and no LLM lands in the same place. That observation set up the next experiment.

## Experiment 2: What carries the gain?

<p class="experiment-label">Experiment 2</p>

We removed the components one at a time and measured macro-F1.

<figure>
  <img src="/column-images/ace-net/ablation-1600.webp" alt="Core-mechanism ablation" />
  <figcaption><strong>Figure 3.</strong> macro-F1 with components removed. Amber is the full model. Blue drops the dictionary and the selection and simply adds one learned vector at L = 8. Only late fusion (adding at the final CLS) clearly drops.</figcaption>
</figure>

Fixing the temperature, removing Gumbel noise or removing the diversity loss changes almost nothing. Even **dropping the whole dictionary and adding one learned vector at L = 8 (C_freevec) gives 0.4960**, only 0.0005 below the full model.

A non-significant difference does not by itself prove equivalence, so we tested it directly. The per-input context vectors on the test set are nearly identical: cosine 1.000 to their mean, relative dispersion 0.0001. Feeding the single mean vector to every input leaves macro-F1 at 0.4964 and **reproduces every test prediction**. By convergence the input-adaptive selection is inert, and ACE-Net works as a constant learned deep prior.

This also explains why prefix-tuning lands in the same band. The internal ablation and the external baseline point to the same conclusion.

## Experiment 3: Which layer?

<p class="experiment-label">Experiment 3</p>

If one vector explains the gain, the remaining variable is where it goes. We injected at each of the twelve layers.

<figure>
  <img src="/column-images/ace-net/layer-sweep-1600.webp" alt="Injection-layer sweep" />
  <figcaption><strong>Figure 4.</strong> macro-F1 by injection layer (band = std over five seeds). Layers L5–L8 cluster at 0.49–0.50; L10 and L11 fall below the baseline.</figcaption>
</figure>

L5 to L8 sit together at 0.49 to 0.50. L6 has the highest mean (0.5004), but its 0.0017 lead over L8 is within seed noise, so we do not claim L8 is uniquely necessary. We use L8 because it has the smallest seed variance in the band (std 0.0043).

Near the top, macro-F1 drops to 0.4382 at L10 and 0.3728 at L11, **worse than adding nothing**. A control that rescales the injected vector leaves the middle-layer result unchanged and never rescues the degraded layer. Depth, not magnitude, governs the effect.

## Experiment 4: Which texts does it help?

<p class="experiment-label">Experiment 4</p>

We repeated the comparison on three datasets of different character. ISEAR consists of self-narratives of the form "When I ... I felt ...", so the context is in the text. It is included as a negative control.

<figure>
  <img src="/column-images/ace-net/selectivity-1600.webp" alt="Selectivity across datasets" />
  <figcaption><strong>Figure 5.</strong> Improvement by dataset. The less context the text carries, the more the injection helps; on ISEAR it does not help.</figcaption>
</figure>

The order is GoEmotions (+0.041) > SemEval-2018 (+0.013) > ISEAR (−0.001, n.s.). The datasets also differ in label count and source, so we do not rest the conclusion on this ordering alone. Within GoEmotions, we split the test set by type of context deficiency.

| Stratum | Description | n | Δ | p |
|---|---|---|---|---|
| S1 | no emotion word | 4,817 | +0.025 | < 0.01 |
| S2 | short text | 1,991 | +0.044 | < 0.001 |
| S3 | implicit premise | 89 | n.s. | 0.936 |
| S4 | irony / sarcasm | 16 | n.s. | 0.692 |

Inside one dataset, the gain is significant on texts with no emotion word (S1) and on short texts (S2). S3 and S4 are too small to decide, and we report them as they are.

By class, the gain is **concentrated on the three rarest classes**.

<figure>
  <img src="/column-images/ace-net/tail3-1600.webp" alt="Tail-3 decomposition" />
  <figcaption><strong>Figure 6.</strong> The gain split by class frequency. Without the three rarest classes the gain is +0.008 (n.s.); on those three alone it is +0.315.</figcaption>
</figure>

83.3% of the macro-F1 gain comes from the three rarest classes. On pride and relief the baseline scores F1 0, while ACE-Net reaches 0.411 and 0.230. The baseline's zero comes from never predicting these classes at the 0.5 threshold, not from a total absence of signal.

## Experiment 5: Isn't class rebalancing enough?

<p class="experiment-label">Experiment 5</p>

If the gain is on rare classes, standard long-tail fixes (logit adjustment, class-balanced loss) might do the same job. We compared them under the same protocol.

<figure>
  <img src="/column-images/ace-net/rebalancing-1600.webp" alt="Comparison with long-tail rebalancing" />
  <figcaption><strong>Figure 7.</strong> Improvement over the baseline. Standard rebalancing reaches 40–50% of the ACE-Net gain.</figcaption>
</figure>

The stronger rebalancer, class-balanced loss, gains +0.0207, about 51% of the ACE-Net gain. The remaining half (around +0.020) lies beyond what frequency correction reaches. Rebalancing and deep prior injection complement each other rather than substitute for each other.

## Experiment 6: Flagging the inputs that will benefit

<p class="experiment-label">Experiment 6</p>

Before moving to a new domain, it helps to know which inputs the injection will help. FORGE-Ω takes a small labeled sample, computes for each example the change in classification loss between the injected and non-injected models (ΔL), and uses it as the indicator.

<figure>
  <img src="/column-images/ace-net/forge-omega-1600.webp" alt="FORGE-Omega correlations" />
  <figcaption><strong>Figure 8.</strong> Correlation of each signal with per-example improvement (frequency-controlled subset, n = 444). The loss change ΔL correlates positively on two backbones; the label-free surrogate does not.</figcaption>
</figure>

The loss change tracks the benefit: r = 0.345 on DeBERTa and r = 0.477 on a second backbone, BERT-base. The label-free surrogate ΔL_mask gives r = 0.066 (n.s.) and was set aside. Baseline confidence and the top-two margin barely correlate with the improvement either. FORGE-Ω is therefore a **pre-deployment screen** that needs a small labeled sample.

## What we know and what we don't

The study establishes three things.

- Injecting LLM context into a middle layer helps on context-deficient text, but what does the work is **a learned prior placed at an intermediate depth**, not the dictionary content.
- It works in a band of middle layers and hurts near the top.
- It helps context-deficient texts and very rare classes, and does nothing when the context is already in the text.

There are limits. Building the dictionary needs one-time access to the GPT-4o-mini API, so the method is not fully LLM-free. All three datasets are single-utterance tasks; documents are untested. The irony and implicit-premise strata are too small for a conclusion. A label-free signal for spotting where the injection helps remains open.

Next, we plan to remove the LLM dependence with self-supervised dictionary updates and to build a fully label-free monitoring signal.

Code: [github.com/keito-git/ace-net](https://github.com/keito-git/ace-net). Data (dictionary, generated context descriptions, layer-sweep results and more): [Zenodo](https://doi.org/10.5281/zenodo.23415199).
