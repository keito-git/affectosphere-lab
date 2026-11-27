---
title: "Can LLM-Generated Data Stand In for Human Disagreement?"
subtitle: "Generated Texts and Simulated LLM Readers Do Not Replace Human Disagreement in Emotion Recognition"
date: "2026-11-27"
excerpt: "Readers of the same post often choose different emotions. We tested whether texts written by an LLM, or persona-conditioned LLM readers, can supply the information this disagreement carries. Only human label distributions on real texts did. A walk-through of our SSRN preprint."
readingMinutes: 13
showImage: false
image: "/column-images/ssrn-generated-texts-llm-readers/flow.png"
imageAlt: "Analysis flow. The targets of real and generated texts are varied, and test texts are split into three levels of human disagreement to compare effects."
authors:
  - name: "Keito Inoshita"
    url: "/en/about/"
    affiliation: "Kansai University"
tldr: "LLMs are increasingly used both to write training data and to act as simulated annotators. For subjective judgments such as perceived emotion, people disagree, and the disagreement itself carries information. We split the test texts of a Japanese (WRIME) and an English (GoEmotions) emotion corpus into three levels of annotator disagreement and evaluated every training condition by the temperature-scaled cross-entropy against the human label distribution. Training real texts on human label distributions gave the largest gain, most on disagreed texts. Generated texts added about one-eighth of this gain, and it did not concentrate on these texts. Texts generated at the boundary between two emotions gave no additional gain. Ten persona-conditioned LLM readers disagreed less than humans (unanimous on 41.5% of texts against 21.6%), disagreed on different texts, and harmed the student even after entropy matching."
links:
  - label: "Preprint (SSRN)"
    url: "https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7686105"
citation: |
  @misc{inoshita2026generated,
    title        = {Generated Texts and Simulated {LLM} Readers Do Not Replace
                    Human Disagreement in Emotion Recognition},
    author       = {Inoshita, Keito},
    year         = {2026},
    howpublished = {SSRN preprint, abstract id 7686105}
  }
---

<div class="teaser">
<div>

Soft labels

Training real texts on human label distributions lowers CE by **0.060** (WRIME) and **0.100** (GoEmotions), most on disagreed texts.

</div>
<div>

Generated texts

Generated texts add only **0.007 / 0.012**, not concentrated on disagreed texts. Boundary texts add nothing more.

</div>
<div>

Simulated readers

LLM readers are unanimous on **41.5%** of texts (humans 21.6%). Disagreement correlates at only 0.185, and their labels harm the student.

</div>
</div>

## Can an LLM produce human disagreement?

LLMs are increasingly used as stand-ins for people. They are prompted to answer as survey respondents with given backgrounds, and they write labelled examples in place of texts written and annotated by humans. These uses assume that an LLM reproduces how people judge, not only what most people answer.

Emotion perception is a clear case in which judges vary. Readers of the same post often choose different emotions, and research on human label variation treats this disagreement as information rather than noise. The target of a text is then better described as a distribution over emotions than as a single label. Getting that distribution, however, needs several annotators per text.

Generated data could supply disagreement in two ways. **The texts** could be written to be ambiguous, or **the readers** could be a population of LLMs that disagree as humans do. Both assume that disagreement can be produced on one side alone.

Existing studies usually report averages over the whole test set and compare against a student trained on majority labels. Such a comparison cannot tell whether a gain comes from soft labels of any kind, from distilling a teacher that saw more real data, or from the generated texts themselves. This study **locates the information about human disagreement and tests whether generated texts or simulated readers can supply it**.

## How the analysis works

<figure>
  <img src="/column-images/ssrn-generated-texts-llm-readers/flow-1600.webp" alt="Flow of the disagreement-level analysis" />
  <figcaption><strong>Figure 1.</strong> Analysis flow (Figure 1 of the paper). (a) Targets of real texts, (b) four label sources for the same generated texts, (c) test texts split into three levels of human disagreement, with the effect reported per level.</figcaption>
</figure>

**Disagreement levels.** The disagreement of a text is D(x) = 1 − max p\*, where p\* is the human label distribution. It is zero when all annotators choose the same class. Test texts are split into low, mid and high levels by the tertiles of D.

**Evaluation.** For each condition we report the difference Δ in cross-entropy (CE) between the student's prediction and the human label distribution, relative to a reference, at each level. A negative Δ is an improvement. To compare on equal confidence, a temperature is fitted on development data first (temperature scaling). Comparing the raw and calibrated effects separates harm from overconfidence from harm that changes the predicted class.

**Conditions compared.**

- Targets of real texts: a student trained on majority labels (one-hot) and a student trained on human label distributions (soft-real)
- Labels of generated texts: the class named in the prompt, a p\*-teacher trained on all real texts, a **same-data teacher trained only on the student's own real texts**, and the vote share of ten LLM readers
- Boundary-targeted generation: for pairs of emotions that annotators often confuse, the LLM writes a post with mixed feelings between them
- Entropy-matched control: the readers' labels are flattened with a temperature so that their mean entropy equals that of the teacher labels

The same-data teacher is the key. It has seen only the real texts the student already has, so any gain from its labels must come from **the generated texts as new inputs**.

| Item | WRIME | GoEmotions |
|---|---|---|
| Language | Japanese | English |
| Classes | 9 | 28 |
| Real training pool | 25,500 | 31,756 |
| Generated texts | 4,500 | 4,500 |
| Test texts (low / mid / high) | 541 / 479 / 1,480 | 1,222 / 1,766 / 1,602 |
| Generator | Qwen2.5-7B-Instruct | Llama-3.1-8B-Instruct |
| Student | BERT-base Japanese v3 | RoBERTa-base |

Boundary generation and the simulated readers were tested on WRIME only. The readers used Qwen2.5-7B-Instruct with ten Japanese personas, each described in one sentence by age, gender, occupation and a tendency in reading others' feelings. Each reader votes for the option whose number has the highest next-token probability.

## Experiment 1: Where do one-hot generated texts hurt?

<p class="experiment-label">Experiment 1</p>

<div class="setup">

**Setup**

- Comparison: add one-hot generated texts to the majority-label student
- Metrics: CE difference before (raw) and after (calibrated) temperature scaling; change in accuracy against the majority label
- Seeds: mean of 3 on WRIME and 2 on GoEmotions

</div>

<figure>
  <img src="/column-images/ssrn-generated-texts-llm-readers/harm-1600.webp" alt="Raw versus calibrated harm of one-hot generated data" />
  <figcaption><strong>Figure 2.</strong> Change in CE when one-hot generated texts are added (positive = harm). Before temperature scaling the harm is largest on disagreed texts; after scaling it almost disappears there.</figcaption>
</figure>

Before temperature scaling, the CE increase was largest at the high level on both corpora (+0.079 on WRIME, +0.095 on GoEmotions). After scaling, it shrank to +0.003 and +0.011.

The raw harm on disagreed texts was mainly **overconfidence**. On WRIME, the generated data raised the fitted temperature by 0.14 on average, and a single temperature removed most of the harm.

The calibrated harm that remained was **misclassification of texts on which annotators agreed**. On WRIME, accuracy dropped by 2.2 points at the low level, where the majority-label student reached 82.8%. On GoEmotions, the accuracy drop was largest at the mid level, which is also the level with the largest calibrated harm. This contradicts the expectation that one-hot generated data mainly harm texts on which humans disagree.

## Experiment 2: Changing the labels of generated texts

<p class="experiment-label">Experiment 2</p>

<figure>
  <img src="/column-images/ssrn-generated-texts-llm-readers/relabel-1600.webp" alt="Calibrated effect of label sources on the majority-label student" />
  <figcaption><strong>Figure 3.</strong> Calibrated change in CE when generated texts are added to the majority-label student on WRIME (negative = gain), by label source.</figcaption>
</figure>

Labels from a teacher trained on human label distributions (the p\*-teacher) turned the harm into a gain. On WRIME, the overall effect moved from +0.010 with one-hot labels to −0.026 with p\*-teacher labels, negative on all three seeds. On GoEmotions, p\*-teacher labels gave −0.038.

The gain grew with the amount of human-label information in the target: −0.008 for the hard-teacher mix, −0.015 for the p\*-teacher mix and −0.026 for the p\*-teacher alone. These targets differ in mean entropy (0.59, 0.73 and 0.86), so this comparison is not entropy-matched.

Again, the gain did not concentrate on disagreed texts: it was largest at the mid level on WRIME and nearly uniform on GoEmotions. This comparison alone cannot tell whether the labels carry disagreement information or simply distil a teacher that saw the full real pool.

## Experiment 3: Separating the sources of gain

<p class="experiment-label">Experiment 3</p>

<figure>
  <img src="/column-images/ssrn-generated-texts-llm-readers/decomposition-1600.webp" alt="Decomposition of the calibrated effect by disagreement level" />
  <figcaption><strong>Figure 4.</strong> Decomposition of the calibrated effect (mean of three seeds). Amber: training real texts on human label distributions. Blue: adding generated texts with same-data teacher labels. Grey: adding generated texts with full-data teacher labels.</figcaption>
</figure>

**Training real texts on human label distributions was the largest source of gain.** The soft-real student lowered overall CE by 0.060 on WRIME and 0.100 on GoEmotions. The gain was larger on disagreed texts: on WRIME it grew from −0.029 at the low level to −0.075 at the high level, and on GoEmotions from −0.059 to −0.119 and −0.112 at the mid and high levels.

**Generated texts added a smaller gain that did not concentrate on disagreed texts.** With same-data teacher labels, generated texts lowered the soft-real student's CE by 0.007 on WRIME and 0.012 on GoEmotions, negative on all three seeds on both corpora. Because this teacher saw no extra real data, the gain comes from the generated texts as new inputs. It was smallest at the high level on WRIME and nearly uniform on GoEmotions.

Switching to the full-data teacher added a further 0.005 on WRIME and 0.010 on GoEmotions; this is the distillation share. The two teachers agreed more as the real data grew, with argmax agreement rising from 0.88 to 0.94 on WRIME and from 0.79 to 0.89 on GoEmotions.

## Experiment 4: Do boundary-targeted texts help?

<p class="experiment-label">Experiment 4</p>

To create disagreement on the text side, the LLM wrote posts with mixed feelings between two emotions that annotators often confuse. Results on the majority-label student of WRIME (calibrated, negative = gain):

| Generated texts and label | Low | Mid | High | All | Neg. seeds |
|---|---|---|---|---|---|
| Standard, one-hot | +0.022 | +0.020 | +0.003 | +0.010 | 0/3 |
| Boundary, one-hot | +0.040 | +0.030 | 0.000 | +0.014 | 0/3 |
| Boundary, pair (0.5 each) | +0.013 | −0.001 | −0.011 | −0.004 | 3/3 |
| Standard, p\*-teacher | −0.022 | −0.037 | −0.024 | −0.026 | 3/3 |
| Boundary, p\*-teacher | −0.022 | −0.035 | −0.024 | −0.026 | 3/3 |

With p\*-teacher labels, standard and boundary texts gave the same overall effect, −0.026. The boundary texts were more ambiguous to the teacher (predictive entropy 0.95 against 0.86), and the teacher's argmax fell inside the targeted pair for 77% of them, so the texts did express the requested emotions. Their gain on disagreed texts was nevertheless no larger than that of standard texts.

**A text can be ambiguous to a model without being read differently by people.** What decided the value of a boundary text was its label: the pair label removed most of the one-hot harm. These differences were small, and the interaction between text type and label type was not consistent across seeds.

## Experiment 5: Do LLM readers disagree like humans?

<p class="experiment-label">Experiment 5</p>

To create disagreement on the reader side, ten persona-conditioned LLM readers labelled the WRIME test texts.

<figure>
  <img src="/column-images/ssrn-generated-texts-llm-readers/reader-disagreement-1600.webp" alt="Disagreement of humans and simulated readers" />
  <figcaption><strong>Figure 5.</strong> Left: mean disagreement of humans and simulated readers at each level of human disagreement. Right: share of test texts on which all judges agreed.</figcaption>
</figure>

The simulated readers disagreed less than humans and on different texts. Mean disagreement was 0.158 for the readers against 0.301 for humans, and the readers were unanimous on 41.5% of the test texts against 21.6% for humans. Across the low, mid and high levels, human disagreement rose from 0.000 to 0.174 to 0.453, while the readers stayed at 0.121, 0.118 and 0.184. The readers disagreed on texts where all annotators agreed as much as on mid-level texts, and the Spearman correlation between the two was only 0.185.

<figure>
  <img src="/column-images/ssrn-generated-texts-llm-readers/jsd-1600.webp" alt="JSD from the human label distribution" />
  <figcaption><strong>Figure 6.</strong> Distance from the human label distribution (Jensen–Shannon divergence, 0–1, lower is closer). On disagreed texts, the readers' vote share (0.487) is farther from humans than the training class prior, which ignores the text (0.448).</figcaption>
</figure>

The readers' label distributions were far from the human distributions of the same texts. Overall JSD was 0.413 for the vote share and 0.386 for the entropy-matched label, whereas the soft-real student, which never saw the test texts, reached 0.252. On high-level texts, the vote share (0.487) was farther from humans than the class prior of the training texts (0.448).

The readers still responded to each text. Their vote share was closer to the human distribution of the same text than to that of another text at the same level (JSD 0.413 against 0.753 over 200 random pairings), and closer for 69.6% of the pairs. Their argmax agreed with the majority label on 48.5% of the test texts. **They respond to the text, but not the way humans read it.**

## Experiment 6: Training on the readers' labels

<p class="experiment-label">Experiment 6</p>

<figure>
  <img src="/column-images/ssrn-generated-texts-llm-readers/reader-labels-1600.webp" alt="Simulated reader labels on the soft-real student" />
  <figcaption><strong>Figure 7.</strong> Calibrated change in CE when the same generated texts are added to the soft-real student on WRIME with four kinds of labels (positive = harm).</figcaption>
</figure>

The readers' labels harmed the soft-real student. With the vote share, the overall effect was +0.009, positive on all three seeds, and the harm peaked at the mid level (+0.027). With same-data teacher labels, the same texts gave −0.007, negative on all three seeds.

The harm did not come from the confidence of the labels. The vote share had a mean entropy of 0.16 against 0.86 for the teacher labels. Averaging the readers' option probabilities and flattening them with τ = 4.68 raised the mean entropy to 0.86, yet the overall effect was still +0.008, positive on all three seeds. **The harm came from which classes the readers put probability on, not from how much.**

## What we found and what remains open

The study shows three things:

- Among the sources tested, only human label distributions of real texts, and teachers trained on them, improved predictions on disagreed texts. Generated texts added about one-eighth of that gain, not concentrated on disagreed texts.
- Boundary texts were ambiguous to a model but added no gain, and LLM readers disagreed on different texts from humans, with labels that harmed the student even at matched entropy. From this, the paper hypothesises that human disagreement is a property of **the relation between a text and a population of readers**, not of the text alone.
- The value of generated data should be measured against a student that already learns human label distributions, after temperature scaling. Against the majority-label student, p\*-teacher labels look like a 0.026 / 0.038 gain; against the soft-real student, generated texts add 0.007 / 0.012.

The paper proposes three checks before replacing human annotators with LLM readers: compare the readers' disagreement with human disagreement on the same texts, not only its average amount; compare their label distribution with a simple reference such as the training class prior; and test their labels as training targets against a model that already learns human label distributions. The readers here failed all three, although their argmax matched the majority label on about half of the texts.

There are limits. The study uses two corpora with one student architecture each, and p\* for each text rests on a few annotators. Boundary generation and the simulated readers were tested only on WRIME, with one LLM, ten fixed personas and deterministic votes; larger LLMs or personas drawn from the actual annotators may reproduce human disagreement better. The label comparison on the majority-label student is not entropy-matched, and only CE and accuracy were evaluated.

Next steps are to condition generation on distributions of human judgments, that is, to synthesise texts paired with the human judgments they elicit rather than texts of a class, and to test other subjective tasks such as natural language inference and offensive language detection.
