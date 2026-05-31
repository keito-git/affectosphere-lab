---
title: "ChatGPT Quietly Changes Its Tone Depending on the Country Name"
date: "2026-06-01"
excerpt: "'Russia,' 'Ukraine,' 'Iran,' 'the U.S.' — swap a country name and an LLM's output sentiment quietly tilts. A 5-minute take, for global PR, compliance, and government relations, on how to face geopolitical bias."
image: "/column-images/llm-political-bias.svg"
imageAlt: "Abstract visual of a world map overlaid with sentiment scores, with certain regions highlighted in amber bias"
readingMinutes: 6
basedOnPaper: "Multifaceted Exploration of Perceptions on the Ukraine-Russia War in the Japanese Twitter Space"
basedOnPaperUrl: "https://arxiv.org/"
---

> _This article is an English translation of the original Japanese column. Some phrasing has been adapted for English readers._

Hello, this is Inoshita from Affectosphere Group.

Talking with someone at a globally-operating company the other day, I had a small shiver moment.

"Our overseas PR uses ChatGPT to draft things, and sometimes the tone comes out slightly negative for certain countries. Why is that?"

A lot of companies are starting to half-notice this, but nobody has been willing to face it head-on.

LLMs quietly tilt the sentiment of their outputs depending on which country name you put in.

And the direction of the tilt is not chosen by the business — it is decided automatically by the bias in the training data.

In a sequence of five papers published in 2024 [^1] [^2] [^3] [^4] [^5] with Professor Zhou, we measured this "geopolitical bias of LLMs" from multiple angles. Using the Ukraine-Russia war as a case, the work spans analysis of about 200,000 Japanese tweets, a new metric called EICR, the bias of Japanese-continued-pretraining LLMs, and finally the bias in the major training corpora themselves.

Today I want to unpack these five papers, not as technical works, but as material for international PR, compliance, and government-relations decisions.

[^1]: Keito Inoshita (2024). Multifaceted Exploration of Perceptions on the Ukraine-Russia War in the Japanese Twitter Space, IEEE IoTaIS 2024, pp. 58-64.
[^2]: Keito Inoshita (2024). Sentiment Analysis of Japanese Twitter Users Regarding the Ukraine-Russia War and Its Implications for Security Policy, ICITACEE 2024, pp. 338-343.
[^3]: Keito Inoshita (2024). Assessment of Conflict Structure Recognition and Bias Impact in Japanese LLMs, TIMES-iCON 2024.
[^4]: Keito Inoshita (2024). The Efficient Development of Conflict Structure Datasets for Evaluating Sentiment Recognition Bias in Large Language Models, ICELTICs 2024, pp. 7-12.
[^5]: Keito Inoshita, Xiaokang Zhou (2024). Sentiment Bias and Security Analysis in Training Datasets of Large Language Models, IEEE BDCloud 2024, pp. 1-8.

---

## Today's takeaway in 3 lines

1. Value: a company that can make bias visible can lead on both regulatory compliance and region-level optimization.
2. Structure: bias is embedded not in individual models but in the "training-data ecosystem." Swapping the model does not erase it.
3. Caution: localization into Japanese (or any language) does not guarantee neutrality. In fact, it can amplify region-specific discourse bias.

Let me go in order.

---

## ① First, what came into view

Using the Ukraine-Russia war as the case study, we analyzed about 200,000 Japanese tweets with BERT-class models aligned to Plutchik-style basic emotion categories. Why Japanese data? Because Japanese companies using Japanese LLMs need to understand the geopolitical bias embedded in their own language space — as the parties directly affected.

Four main findings emerged.

- The phenomenon that sentiment prediction flips when the country name is swapped can be quantified (we proposed a new metric called EICR)
- Japanese-continued-pretraining LLMs show a stronger negative bias toward Russia and Eastern Europe than the base Llama2
- In the major training corpora (C4, RedPajama, OSCAR, RefinedWeb), negative sentiment toward Russia and Iran and over-exposure of the U.S. are already embedded
- That is, the bias was not produced by individual-model fine-tuning. It is embedded in the training-data ecosystem itself

The conclusion is simple:

> Swapping the model does not fundamentally fix this.

Because the leading model families are largely trained on the same lineage of corpora. Switching Llama to Mistral, Mistral to Qwen — you inherit the same contamination as you start.

For a global company, this is, frankly, a small-shiver moment.

---

## ② Why "an AI that looks neutral" is a business risk

LLM outputs are, on the surface, fluent and look neutral.

If you use them assuming you "just swapped 'Russia' for 'Ukraine' for 'Iran' for 'the U.S.'," the sentiment polarity of the output tilts one way.

Concretely, where does this become a problem?

- The auto-reply on an overseas subsidiary's SNS responds in a slightly negative tone to a specific region
- Multilingual customer support returns subtly cooler responses to customers in a specific region
- AI translation replaces adjectives in a press release with nuances more negative than the original
- An auto-generated job ad treats the culture of applicants from a specific region "a little lightly"

Individually, each of these is a small piece of unease.

But the moment one of them blows up in local media or on social media, it amplifies within days and reaches brand damage.

And regulators are starting to look at exactly this. The EU AI Act, foreign-interference laws in various countries, election-related laws — regulators have a high level of interest in "AI amplifying biased discourse against specific regions."

The position "we're just using AI for translation" is no longer holding up.

---

## ③ Value: what a company that makes bias visible gains

Stacking only risks would be unfair, so this one I want to write head-on.

A company that can quantify geopolitical bias can actually stand in a fairly strong competitive position.

There are three reasons.

First, regional localization gets sharper. The ability to quantify bias is the ability to apply "region-specific tuning" that corrects for it. Middle East, Eastern Europe, East Asia — they can each get output that does not feel off. Bias is a flaw to remove and, at the same time, an entry point to region-level optimization.

Second, it becomes a strong differentiator for trust-building. "We audit regional bias of our AI every quarter and publish the results internally and externally" — companies that can say this gain an advantage on commercial terms in government procurement, international organizations, and regulated industries (finance, pharma, telecom).

Third, it attracts talent. People who can audit AI bias are, at present, in heavily under-supplied demand. Setting up an internal audit function is itself a magnet for excellent talent in ESG, compliance, and government-relations.

That is the value side for companies that make the bias problem visible.

---

## ④ As an emotion-AI researcher, I want to pause here

Here is the angle unique to Affectosphere Group.

Read the geopolitical-bias story as "regulatory compliance" and it ends up being a story about tools and processes. Bias-measurement KPIs, quarterly audits, disclosure templates — important, of course.

But as an emotion-AI researcher, I want to write one layer deeper.

What our research is ultimately trying to measure is: "when an LLM reads a sentence containing a country name, what emotion does it return?"

When you compress "emotion" here into a single label (positive / negative / neutral), things get lost.

For example, given the same sentence containing the word "Russia," one person feels "wariness," another feels "sympathy," yet another feels "indifference." That is the natural diversity on the human side.

The LLM, however, averages over the majority opinion in the training data and returns one "roughly this emotion."

What happens then is that the minority's emotional interpretation gets structurally erased — from the LLM's output, and from the services of any company using that LLM.

Our lab's core stance is to handle emotion "as ambiguous and polysemous as it actually is." The reason is simple: human feelings do not survive being collapsed into averages or majority votes.

The geopolitical-bias problem, at the surface, is about "tilted sentiment polarity." One level below, it is about "the polysemy of emotion being crushed."

This is, in the real sense, dangerous for a global company.

Because customers in a given region pick up the scent that a "single-coded emotion label" toward their region has been baked somewhere into the service.

Not bad enough to file an inquiry. Not bad enough to raise a complaint. But trust quietly drains.

This is structurally the same as the "loss that does not show up in the numbers" I wrote about in the previous Nationality column.

What the emotion-AI side can propose is to pull LLM design toward "outputting an emotion distribution" rather than "a single emotion label." That is what our lab is working on for the mid-to-long term.

In international PR terms: shift the evaluation axis from "the sentiment toward this text is X" to "for this text, fraction A of people feel X, fraction B feel Y, fraction C feel Z." That shift, I suspect, will happen over the next five years.

---

## So what do you do starting tomorrow

I have laid out both risk and value, so three things you can act on at the field level.

- Inventory: list every LLM used in customer-facing or generation tasks at your company. Surprisingly many companies have not mapped this.
- Audit KPI: define a KPI that quantifies the sentiment-polarity shift across sample outputs that include the names of your target countries and regions. Rough is fine at first.
- Disclosure template: prepare a format that lets AI bias-audit results be embedded in your ESG or sustainability report. You can be ready for the next reporting cycle.

The value is big. The risk is big. Look at both — that is the ask from someone who has crossed emotion AI and geopolitical bias in their research.

---

## Closing

LLMs look like "neutral tools" but in fact inherit the political tilt of their training data.

As long as the leading models are trained on the same lineage of corpora, swapping the model does not fundamentally solve it.

But this is not a hopeless situation for global companies.

A company that makes bias visible and audits it quantitatively can lead on both regulatory compliance and differentiation. Trust will quietly drain away from companies that give up on transparency — that structure will become visible over the next five years.

And from the emotion-AI side, we will propose designs that look at the world through "emotion distributions" instead of "single emotion labels."

If "wait, is our AI actually geopolitically okay?" crossed your mind, please start with an inventory of your generation tasks.

So — that is it for today.

---

## References

1. Keito Inoshita (2024). *Multifaceted Exploration of Perceptions on the Ukraine-Russia War in the Japanese Twitter Space*. IEEE IoTaIS 2024, pp. 58-64.
2. Keito Inoshita (2024). *Sentiment Analysis of Japanese Twitter Users Regarding the Ukraine-Russia War and Its Implications for Security Policy*. ICITACEE 2024, pp. 338-343.
3. Keito Inoshita (2024). *Assessment of Conflict Structure Recognition and Bias Impact in Japanese LLMs*. TIMES-iCON 2024.
4. Keito Inoshita (2024). *The Efficient Development of Conflict Structure Datasets for Evaluating Sentiment Recognition Bias in Large Language Models*. ICELTICs 2024, pp. 7-12.
5. Keito Inoshita, Xiaokang Zhou (2024). *Sentiment Bias and Security Analysis in Training Datasets of Large Language Models*. IEEE BDCloud 2024, pp. 1-8.

<p class="ai-notice"><small>* This article was written in part with AI assistance and may contain inaccuracies.</small></p>
