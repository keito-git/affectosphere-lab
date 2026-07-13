---
title: "Is it really true that people will not talk about their minds to an AI? What drove disclosure was not the topic, but perceived risk and benefit"
date: "2026-07-13"
excerpt: "In an experiment with a Dutch representative sample of N=1,388, what determined willingness to self-disclose health information to an AI chatbot was not whether the topic was physical or psychological, but the benefits and risks users perceived — and their individual characteristics. For anyone designing affective AI, that lands hard."
image: "/column-images/health-chatbot-self-disclosure-perceived-risk-benefit.png"
imageAlt: "Flat illustration of a person holding a physical-symptom card and a mental-worry card in front of a chatbot screen, hesitating as a scale weighs benefit on one side and risk on the other"
readingMinutes: 5
basedOnPaper: "LLMs for health: Perceived benefits, risks, intention to use AI chatbots, and willingness to self-disclose across sensitive health topics"
basedOnPaperUrl: "https://arxiv.org/abs/2607.09253"
---

Hello. I am Miura from Affectosphere Group.

Whenever I talk about affective AI, there is one line I hear again and again.

"I would ask an AI about a physical symptom, sure. But talk to it about my mental health? That is a different story."

I get the feeling. Matters of the mind are special, and not something you hand to a machine. I carried that assumption around for a long time without questioning it.

Then a study posted to arXiv in July 2026 (Beets, Jansen, Hommes, Vromans, Westerbeek, Sankaran, van Weert, Krahmer & Bol, arXiv:2607.09253) walked straight up to that assumption and poured cold water on it.

A Dutch representative sample, N=1,388. A mixed-design online experiment measuring perceived benefits, perceived risks, intention to use an AI chatbot, and willingness to self-disclose health information. And the conclusion: whether people disclose health information to an AI chatbot is driven mainly by perceived benefits, perceived risks, and individual characteristics — rather than by the type of topic.

From where I sit, working on affective AI, that lands hard. So let me dig in.

---

## Three takeaways

1. Topic type — physical versus psychological — was not as dominant as you would expect. What mainly drove disclosure were the benefits and risks users perceived, plus their individual characteristics.
2. Perceived benefits were positively associated with intention to use and willingness to disclose; perceived risks were negatively associated. The topic-side factor that did matter was sensitivity: intention to use was higher for low-sensitivity topics than for high-sensitivity ones.
3. The thing affective AI quietly assumes — that people will hand over their emotional expression as data — turns out to be a variable designers can move. Before you push accuracy, there is work to do on lowering perceived risk and raising perceived benefit.

---

## ① The "matters of the mind are special" assumption did not hold up well

First, let me lay out the question the study puts on the table.

Two axes were examined. One is topic type: is the subject physical, or psychological? The other is topic sensitivity: is it low, or high? The study looks at how these two axes affect perceived benefits, perceived risks, intention to use, and willingness to self-disclose.

The naive prediction goes like this. Psychological topics are special, so risk should spike there and willingness to disclose should collapse.

The results were not that simple. What the paper reports is that disclosure of health information to AI chatbots was determined mainly by perceived benefits, perceived risks, and individual characteristics — rather than by topic type.

In other words, how a person sees the chatbot mattered more for disclosure than the label of "is this about the mind or not."

I think that is a quietly big deal.

If you treat "psychological content will not be disclosed to AI" as a fixed wall, affective AI design drifts toward one of two options: give up, or pry the content out anyway. But if what is actually doing the work is perceived risk and perceived benefit, then that can be moved by design. It is not a wall. It is a dial.

---

## ② What mattered was sensitivity, and the scale between benefit and risk

So what did the work?

One part comes out clearly. Perceived benefits were positively associated with intention to use and willingness to disclose; perceived risks were negatively associated. Which is to say: users are weighing things on a scale.

"If I say this, does anything good come back to me?"
"If I say this, does anything bad happen to me?"

They compare the two and decide whether to disclose. It sounds obvious — but the point is that the obvious thing actually showed up in a large sample.

There was a topic-side factor that mattered too: sensitivity. Intention to use was higher for low-sensitivity topics than for high-sensitivity ones. So it is not the category of physical versus psychological, but the degree of how sensitive the subject is, that moves intention to use.

And honestly, that fits. There are psychological topics that are light (I have been sleeping a little badly) and physical topics that are very heavy. Slice by category and you erase those gradations. Slicing by sensitivity is closer to how it actually feels.

On top of that, the study reports that perceptions, intentions, and willingness to disclose varied by individual characteristics. Users are not one homogeneous block. Looking at the same chatbot, different people perceive different benefits and different risks.

Line all that up and the picture gets fairly sharp. What decides disclosure is not "what kind of topic this is," but "how this person, in this situation, estimated the benefit and the risk."

---

## ③ What this means for designing affective AI

When we build affective AI, we make one assumption without saying it out loud. We assume the user will put their emotional and psychological content into the system.

Neither emotion recognition nor empathic response works without that. If the data never comes out, no model, however accurate, can run. Which means the very first gate in affective AI is not accuracy and not architecture. It is disclosure.

This paper suggests that the key to that gate sits more on the design side than I had assumed.

If so, I think the work sorts into three pieces.

First, show the benefit. If perceived benefit pushes positively, then the question is whether the user understands what comes back to them when they say this thing. Leave that vague and just drop an emotion input field on the screen, and the scale will not tip.

Second, lower the risk. Since perceived risk pushes negatively, this is where the leverage is. Where does what I said go, who sees it, and when does it disappear? Giving people that visibility may do far more for disclosure rates than another feature. Emotional data is, by its nature, the kind of data people are most anxious about handing over.

Third, design for individual differences. If perceptions, intentions, and willingness all vary by individual characteristics, then serving everyone the same front door is poor design. Do not demand deep disclosure straight away from the hesitant. Build a path that earns trust in stages. There is a lot of room for craft here.

Incidentally, the finding that topic sensitivity moved intention to use also hints at an implementation order. Do not open with the heaviest subject. Let people feel the usefulness somewhere low-sensitivity first. Put weight on the benefit side of the scale, and only then approach the heavy topics. That order simply feels more natural.

---

## Disclosure comes before accuracy

What I found most interesting reading this study is that the intuition "psychological topics are special" was not strongly supported by the data.

We tend to treat the heaviness of the subject matter as a fixed constraint. But what users were actually looking at was not the category of the content — it was what happens to them once they hand it over.

For affective AI, I find that quite hopeful.

Content does not go undisclosed because emotion as a subject is cursed. It may be that the benefit was never communicated, or the risk was never lowered, or no front door was built for that particular person. And if so, all of that is inside our job description.

Before you push model accuracy up by one point, think about whether the user can type the first sentence at all. In affective AI, I suspect that pays off sooner.

That is it for today!

---

## References

1. Beets, Gwenn, Jansen, Anniek, Hommes, Saar, Vromans, Ruben D., Westerbeek, Leonie, Sankaran, Supraja, van Weert, Julia C.M., Krahmer, Emiel J., & Bol, Nadine (2026). *LLMs for health: Perceived benefits, risks, intention to use AI chatbots, and willingness to self-disclose across sensitive health topics*. arXiv preprint. https://arxiv.org/abs/2607.09253

<p class="ai-notice"><small>* This article was written in part with AI assistance and may contain inaccuracies.</small></p>
