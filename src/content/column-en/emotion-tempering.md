---
title: "“Outrage Wins Clicks” Is Already Outdated — The AI That Tones Down Intensity Without Changing Meaning"
date: "2026-06-01"
excerpt: "What comes after a decade of media optimized for anger, anxiety, and outrage? An AI that preserves meaning while dialing down emotional intensity is quietly redrawing the competitive map for media, advertising, and content platforms. Five minutes."
image: "/column-images/emotion-tempering.png"
imageAlt: "An emotion-intensity meter shifting from red to yellow as a sensational headline is rewritten in a calmer tone"
readingMinutes: 5
basedOnPaper: "Multi-Agent Large Language Model Based Emotional Detoxification Through Personalized Intensity Control for Consumer Protection"
basedOnPaperUrl: "https://arxiv.org/"
---

> _This article is an English translation of the original Japanese column. Some phrasing has been adapted for English readers._

Hello — this is Inoshita from Affectosphere Group.

I was talking with the editorial lead of a news app the other day, and they said:

“Our click-through rates are growing nicely. But the churn rate is creeping up too. Which one should we be optimizing for?”

This is a surprisingly fundamental question.

The attention economy has run on a single answer for more than a decade: provoke strong emotions — anger, fear, outrage, anxiety — to keep eyeballs on the page.

But that same approach has been shown, again and again in medicine and psychology, to degrade users' mental state.

“Users get hooked, users don't get happier.”
That contradiction has been baked into the structure of ad-funded media and content platforms for years.

Now there's an interesting proposal coming from the technical side.
This is a short business-facing read on MALLET[^1], a framework we published in 2026.

[^1]: Keito Inoshita, "Multi-Agent Large Language Model Based Emotional Detoxification Through Personalized Intensity Control for Consumer Protection", IEEE ZINC 2026.

---

## Three-line takeaway

1. Value: rewriting content so the meaning is preserved but the emotional intensity is reduced has reached a workable level.
2. Competitive axis: this is not censorship. It's a design move that grows long-term LTV and brand equity. The next competitive axis sits here.
3. Affective AI lens: “delivering value without inflaming users” is a layer of value you cannot capture with accuracy or efficiency metrics. Businesses that ignore this layer will quietly sink.

Going through each in order.

---

## 1. What the technique actually does

MALLET orchestrates four LLM agents.

The division of labor roughly looks like this.

- Analysis: measures the emotional intensity of an input text
- Adjustment: rewrites it so the meaning is preserved while intensity drops
- Monitoring: tracks the user's emotional exposure over time
- Guide: produces personalized feedback

The interesting part is the adjustment step, which is what we call emotional detoxification.

A concrete rewrite looks like this.

- Before: “X goes rogue, industry rocked.”
- After: “X moves in an unexpected direction; industry weighs response.”

The factual content is the same.
But the first version makes you anxious and dependent on the feed; the second leaves you with energy to act.

In the study, on a news-article dataset, intensity scores went down while semantic similarity to the original stayed reasonably high.

“Tell the truth without inflaming” is becoming an automatable operation, not just artisanal editorial craft.

---

## 2. What this generates (the value side)

From a business angle, this lands on three layers.

First, long-term LTV.

Short-term clicks might dip a bit.
But you cut the silent attrition caused by emotional fatigue.
An app that used to be described as “exhausting to read” can become one that is described as “calm and readable.”

Second, regulatory get-ahead.

The EU Digital Services Act, the UK Online Safety Act, and a wave of minor-protection laws are all moving in the same direction: platforms that leave inflammatory content unchecked will be held responsible.

“We just rank what users post” is no longer a defense.
Whether you have an emotional-intensity adjustment option in your toolkit will change your regulatory cost by an order of magnitude.

Third, a story you can tell advertisers and investors.

Brand-safety requirements and ESG criteria keep tightening.
A platform that can credibly say “we have user mental health built into our design” lands at the same time with advertisers, with investors, and with talent.
One design decision, three stakeholder groups. The ROI math is unusually favorable.

---

## 3. The part I most want to convey as an affective-AI lab

This is where Affectosphere Group really wants to push.

“Provocation drives the numbers” is essentially the language of accuracy and efficiency optimization. Lift the model, lift the targeting, lift CTR.

But from an affective-AI standpoint, there's a layer missing in that framing.

The layer is: how a person feels after they finish reading.

That layer doesn't show up in CTR or dwell time.
“That made me uneasy,” “I wish I hadn't read that,” “I feel oddly tired” — none of this shows up on dashboards.

And those tiny feelings stack up until one day the user just deletes the app.
The exit survey says “no particular reason.”

Our lab's core stance is to treat emotion as ambiguous and many-sided, on purpose.
A system like MALLET is one implementation of that stance.

“Preserve meaning, change only intensity” means, technically, that we have started treating emotion as a thing whose strength is a separate axis — without crushing the underlying nuance.

An AI evaluated purely on accuracy and efficiency would never invent this design.
That's where bringing an affective-AI lens into management language earns its keep.

---

## So what do you do tomorrow?

If the field has been forced into provocation, that's a design problem, not a frontline-team problem.
Three moves you can actually run.

- Measure the emotional-intensity distribution of your current content once. Without a baseline, “tone it down” is meaningless to the people doing the work.
- Set up a single pilot channel. A newsletter or a specific segment. Try emotional adjustment and watch both engagement and churn.
- Add one line on emotional-intensity standards into your content policy. That line is what you'll quote in your advertiser and investor decks later.

You don't need all five-step checklists. The first one — just measure — already moves the conversation forward.

---

## Closing

Short-term attention competition is clearly saturated.
Regulators and users alike are pushing back on the provocation model.

The next competitive axis is the design discipline of delivering value without exhausting the user.
A system like MALLET is an early piece of equipment for making that axis technically real.

The businesses that don't inflame will be the ones still standing.

Slightly grand, but as a lab studying emotion and AI, that's the bet we want to make.

If this column makes someone ask, in the next editorial meeting, “is our content tiring our users out?” — that's enough for today.

That's it for now.

---

## References

1. Keito Inoshita (2026). *Multi-Agent Large Language Model Based Emotional Detoxification Through Personalized Intensity Control for Consumer Protection*. IEEE ZINC 2026.

<p class="ai-notice"><small>* This article was written in part with AI assistance and may contain inaccuracies.</small></p>
