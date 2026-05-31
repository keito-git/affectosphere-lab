---
title: "Your Company's AI Is Quietly Guessing 'Whose Name This Is'"
date: "2026-05-31"
excerpt: "Global CRM, hiring AI, credit scoring — processes that infer nationality from a customer's name are quietly spreading. What is going on behind the convenience? A 5-minute take from the latest research and an emotion-AI lens."
image: "/column-images/nationality-llm-bias.svg"
imageAlt: "Abstract visual of a world map overlaid with personal names in multiple scripts"
readingMinutes: 5
basedOnPaper: "Nationality and Region Prediction from Names: A Comparative Study of Neural Models and Large Language Models"
basedOnPaperUrl: "https://arxiv.org/"
---

> _This article is an English translation of the original Japanese column. Some phrasing has been adapted for English readers._

Hello, this is Inoshita from Affectosphere Group.

The other day I was talking with someone in charge of AI at a company, and they said this.

"Our CRM automatically switches the display language based on the customer's name. It's convenient, but... is it actually fine?"

Convenient — yes, it really is convenient.

And probably, many companies are already doing it without realizing it. Anywhere you have a global CRM, hiring AI, credit scoring, or ad targeting, there is almost certainly some process where the customer's "name" is the starting point.

In a study we published in 2026 [^1], we compared this kind of "name → nationality / region" prediction task between classical neural models and large language models (LLMs).

What came out of it, put simply, is this:

"The moment you bake an LLM into your operations, you also get nationality inference for free."

But there is a real value here, and a risk that is easy to miss. Today I want to write about both, from a business angle.

[^1]: Keito Inoshita, "Nationality and Region Prediction from Names: A Comparative Study of Neural Models and Large Language Models", arXiv preprint, 2026.

---

## Today's takeaway in 3 lines

1. Value: an AI that can infer nationality from a name makes global CX localization dramatically easier.
2. Cost: but "an LLM covers everything" is a lie — in many cases a lightweight model wins on ROI.
3. Hidden cost: and the "uneasy feeling" of the people who get missed never shows up in revenue data. The companies that ignore this layer pay for it in the long run.

Let me go in order.

---

## ① First, what this generates for the business (the value side)

Imagine you are the head of a SaaS business with customers in 50 countries.

The moment a new user enters their name into the signup form, what if the AI quietly did this in the background — wouldn't that be useful?

- Set the default display language to match the customer's home region
- Switch recommended plans to ones that fit their cultural context
- Automatically optimize currency notation, date format, and the order of the address fields

If you try to actually build this with databases and if-statements, it becomes a nightmare. But put an LLM in between, and it just reasons "Yamada Taro → Japan," "O'Brien → Irish heritage" on its own. The implementation cost drops by an order of magnitude.

Our research also confirmed that GPT-class and Llama-class LLMs — without being specifically trained for the task — get name-to-nationality "reasonably right." And because names are relatively short strings, lightweight models with low compute cost are often sufficient. That was another key point of the work.

In other words — you do not have to throw GPT-4 at everything. If the task is well-scoped, you can keep quality with a lightweight model and drop your API costs by an order of magnitude. ROI-wise, it is a tasty story.

That is the value side. For anyone looking to sharpen global CX, this is a tailwind.

---

## ② But riding it as-is will sink you (the risk side)

Here is the part I want to communicate from the lab.

The accuracy with which LLMs infer nationality from names is severely uneven across regions.

- Anglophone, Western European, and major East Asian countries (well-represented in training data) → often correct
- Many African countries, Central Asia, Pacific islands (sparse in training data) → wildly off

Translated into business:

> Which region's customers your AI is misclassifying — the answer is not your choice as a business, but is decided automatically by the bias in the training data.

"We don't discriminate, of course" — but the moment AI mediates, customers in specific regions consistently receive a wrong service. And the structure is invisible from your side.

On top of that, GDPR in Europe, Title VII in the U.S., and the EU AI Act in force from 2024 — regulators are moving to treat "AI inferred it" and "a human decided it" as legally equivalent. "But we only collect names" is no longer a defense.

---

## ③ The emotion-AI angle is the part I most want to convey

This is the point Affectosphere Group, as a research lab, wants to underline.

Suppose a customer from an African country is misclassified by your AI and lands on a service displayed in the wrong language.

- A small sense of friction
- A bit of irritation
- Not enough to file a support ticket, though
- Quietly... they churn

What stays in the CRM is one data point: "churned." Why they churned, how they felt — none of that is recorded.

In business terms, this is "loss that does not show up in the numbers." And from the perspective of emotion-AI research, it is a deeper problem.

Our lab's core stance is to handle emotion "as ambiguous and polysemous as it actually is." The reason is simple: human feelings are not the kind of thing that survives being collapsed into averages or majority votes.

The same logic applies to nationality inference. When an AI says "mostly correct," the minority who fall outside that "mostly" quietly lose trust in the entire service. By the time the business notices, it is already too late.

If you evaluate AI only on "accuracy, efficiency, cost," this layer stays invisible forever. Bringing in an emotion-AI lens means, in a way, equipping yourself with a tool that visualizes losses that revenue dashboards cannot show.

---

## So what do you do starting tomorrow

It would be unfair to only fan the risk side, so here are three things you can act on at the field level.

- Inventory: list every process inside your products that takes a name as input and produces some attribute (country, language, cultural background) as output. A lot of companies have never done this.
- Region-level accuracy audit: measure the accuracy of your main AI features by region and attribute. Aim for an internal dashboard that always shows "Top 5 most-misclassified regions."
- A channel for explanation and appeal: it is hard to fully explain "why we judged this way," but you can place a human-review path and an appeals channel. That alone becomes an entry point for EU AI Act readiness and significantly defuses reputational landmines.

The value is big. The risk is big. Look at both — that is the ask from someone who studies AI and emotion together.

---

## Closing

For an AI, a name is easy to handle. It is short, structured, and you can collect it everywhere in the world.

Which is exactly why AI tries to infer "all kinds of things" from names on its own.

Make the most of the convenience, but keep asking whether someone is quietly leaving with a small sense of unease — that is a technology question and at the same time a business judgment question.

And our lab wants to answer that question from the technology side, by building "tech that handles emotion while keeping it ambiguous."

So — that is it for today.

If anyone reading this thought "wait, is our AI's global readiness actually okay?", please take this chance to inventory your own products once.

---

## References

1. Keito Inoshita (2026). *Nationality and Region Prediction from Names: A Comparative Study of Neural Models and Large Language Models*. arXiv preprint.

<p class="ai-notice"><small>* This article was written in part with AI assistance and may contain inaccuracies.</small></p>
