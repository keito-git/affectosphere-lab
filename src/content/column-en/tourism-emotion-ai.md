---
title: "A 4.5-Star and a 4.5-Star Are Not the Same — The Resolution Story for Emotion Data in Tourism"
date: "2026-06-01"
excerpt: "Reviews, social posts, photo captions. In an era where LLMs decode the fragments of emotion travelers leave behind, how do you act on a satisfaction structure that star ratings miss? Five minutes for tourism, municipal, and hospitality leaders."
image: "/column-images/tourism-emotion-ai.svg"
imageAlt: "Abstract visual of a travel map with destinations and emotion icons floating over each location"
readingMinutes: 5
basedOnPaper: "京都・滋賀・奈良3府県の観光拠点間における口コミの類似性に着目した観光候補地群の分析"
basedOnPaperUrl: "https://arxiv.org/"
---

> _This article is an English translation of the original Japanese column. Some phrasing has been adapted for English readers._

Hello — this is Inoshita from Affectosphere Group.

A municipal tourism officer asked me recently:

“Our destination has a 4.5-star rating, exactly the same as a nearby competitor. But our repeat-visit rate is completely different. Why do you think that is?”

If you stop and sit with this question, it goes pretty deep.

One 4.5-star destination, another 4.5-star destination.
On the surface, the same number.
But the experience behind those numbers might be entirely different.

One destination might score 4.5 because expectations were exceeded by surprise.
The other might score 4.5 because expectations were met, with small disappointments scattered throughout.
Same number. Very different repeat-visit intent. Very different word-of-mouth dynamics.

The tourism industry's experience evaluation has long run on single scores — repeat intent, overall satisfaction, NPS.
But today's traveler posts to social during the trip, writes a review after returning, and shares word-of-mouth with photos.
These unstructured texts carry an emotional texture — expectation, surprise, confusion, relief, gratitude — that no star count can hold.

In a study we published in 2025[^1], LLM-based analysis of reviews surfaced structurally distinct emotional profiles for each destination.

Today I want to translate that paper into the language of tourism, municipal, and hospitality work.

[^1]: Hironobu Ozaki, Keito Inoshita, "Analysis of candidate tourist destinations focused on the similarity of word-of-mouth across attractions in Kyoto, Shiga, and Nara prefectures" (in Japanese), Journal of the Japan Society for Information and Knowledge, vol. 35, issue 2, pp. 327-333, 2025.

---

## Three-line takeaway

1. Value: tourism experience is no longer a single aggregated score. It's a structure of an emotional flow. A 4.5 and a 4.5 are not the same.
2. Design: LLMs can extract emotion as a time series — “expectation at the entry,” “surprise on the ground,” “afterglow on the way home” — and improvement points become sharper by an order of magnitude.
3. Affective AI lens: but you need a design that doesn't get yanked around by the “loud minority.” Reading without crushing the calm majority is what gives this work its dignity.

In order.

---

## 1. What just became possible

Three shifts have lifted what tourism can do with emotion data in the past few years.

First, integrated analysis across multiple sources.

Traveler evaluation can't be captured by a single survey anymore.
Short social posts, travel-site reviews, blog articles, photo captions — they combine to reveal the full trip arc.

Each channel captures a different kind of emotion.

- Social — peaks of excitement, surprise in the moment
- Reviews — retrospective summary, more measured evaluation
- Blogs — narrative of the trip, memory in context

Reading these in parallel already lifts the resolution of destination branding meaningfully.

Second, time-series extraction of emotional dynamics.

Traditional sentiment analysis assigned one score to a whole text.
LLMs let you extract the temporal arc — expectation at entry, surprise on the ground, afterglow on the way home — as structure.

For tourism, this is a big shift.
You no longer flatten satisfaction into one number; you see emotion as a flow.
Root-cause analysis for repeat intent and word-of-mouth becomes a different kind of sharp.

Third, structural decomposition of satisfaction.

“I had a great time” hides multiple factors: access, price, service, scenery, cultural experience, interaction with locals, and more.
LLMs can decompose them.
You can talk quantitatively about strengths and weaknesses by site, by season, by facility.

---

## 2. What this generates for business

Three opportunities.

First, emotion maps for destination branding.
Pair emotion data with geography, and you can visualize where in a destination which emotions arise most strongly.
That becomes the basis for which sites to make centerpieces and which flows to strengthen.
The qualitative structure of the stay experience — invisible in star aggregates — comes into view.

Second, raising the cultural resolution of inbound strategy.
Parallel analysis across multiple languages tells you, for each source-culture, what is the draw and where are the friction points.
Western and East Asian visitors really do value different things.
Designing experiences by source-culture lifts both satisfaction and repeat rate simultaneously.

Third, sharper product and stay design.
Emotional-dynamics data informs both new product creation and improvement of existing offerings.
“Build expectation in the first third, design surprise in the middle third, leave afterglow in the final third” — we are starting to be able to do this on data, not just intuition.

---

## 3. The part I most want to convey as an affective-AI lab

This is what I most want to push from the lab.

LLM-based emotional analysis has a quiet tendency to over-amplify “loud emotional voices.”

Sharp complaints, excessive praise, chilling failure stories — these posts carry intense vocabulary, and naturally stand out to the analyzer.

For tourism, that's a structurally awkward situation.

A single design slip leads to this.

A handful of outlier complaint posts skew the facility's improvement priorities.
Genuine improvements that would lift the bulk of guests get deprioritized.
And the quietly-satisfied majority, never made visible, drifts to a different destination next time.

From an affective-AI standpoint, this connects to a question I think a lot about: is your technology accidentally crushing the calm and ambiguous emotions?

Our lab's stance is to treat emotion as ambiguous and many-sided.
A person's feeling can't be summarized by the extremes alone.
If you only look at “very satisfied” and “very dissatisfied,” the gray zone of “pretty good, but not sure if I'd come again” — which is where most guests actually live — disappears.

And in tourism, the gray zone is almost always what determines repeat rate.

The dignity of emotion-data work in this industry comes from the discipline of reading the loud minority and the calm majority separately.
Before swallowing a score the LLM returns, ask: “is this being pulled by a small intense minority?”
That habit matters.

There's also the ethics of social-media data.
A social post is technically public, but the poster didn't write it imagining a corporate analyst.
Checking against GDPR, revised APPI, and local municipal ordinances together with legal is the modern floor.

---

## So what do you do tomorrow?

Three concrete moves.

- Map which channels hold how much traveler-text data for your destination. Surprisingly few people have actually inventoried this.
- Use an LLM to extract an emotional profile per major site and put it on a map. Just having one “emotion map” changes the quality of destination-strategy conversations.
- Write down the rule for reading “loud minority voices” and “calm majority voices” separately. This alone dramatically reduces the skew in improvement priorities.

Back to that municipal officer: answering “why are repeat rates different at the same 4.5 stars?” needs both emotional flow and culture-segment resolution.
Read those two layers carefully, and the difference becomes explainable.

---

## Closing

Tourism has long been called “the industry that sells memories.”
But memories are vague, hard to quantify, and resistant to becoming usable improvement data.

LLM-based emotion analysis opens a path to treating those vague memories with structure.

But never forget the basic: the data was not written by travelers for operators.
Respecting the data, refusing to drop cultural diversity, and reading without being yanked around by the loud minority — that's what gives this work its dignity.

If you ever wonder, “does our tourism offering hold up to the emotional flow?” — start by drawing an emotion map.
Unexpected feelings will turn up in unexpected places.

That's it for now.

---

## References

1. Hironobu Ozaki, Keito Inoshita (2025). *Analysis of candidate tourist destinations focused on the similarity of word-of-mouth across attractions in Kyoto, Shiga, and Nara prefectures* (in Japanese). Journal of the Japan Society for Information and Knowledge, vol. 35, issue 2, pp. 327-333.

<p class="ai-notice"><small>* This article was written in part with AI assistance and may contain inaccuracies.</small></p>
