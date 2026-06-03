---
title: "Before 'AI Governance' Lands on the CEO's Desk — Just 3 Things"
date: "2026-06-01"
excerpt: "LLMs are no longer an IT-only matter. They are quietly shaping the language used in politics, education, and the workplace. Three control points an executive should keep their hand on — data, model selection, output review. A 5-minute guide."
image: "/column-images/llm-governance.png"
imageAlt: "Abstract visual of a three-tier hierarchy diagram crossed vertically by an amber line of responsibility"
readingMinutes: 5
basedOnPaper: "大規模言語モデルの政治的影響とガバナンスの指針"
basedOnPaperUrl: "https://arxiv.org/"
---

> _This article is an English translation of the original Japanese column. Some phrasing has been adapted for English readers._

Hello, this is Inoshita from Affectosphere Group.

Recently, in conversations with executives, I keep hearing variations of this question:

"Apparently ChatGPT is being used quite a bit on our floor. Should we be doing something about that?"

It is a question that gives you a small shiver, isn't it?

And the truth is, nobody has the canonical answer to "where is the line of 'should be doing something.'" That is the current situation.

In a paper I wrote in 2025 [^1], I organized the situation in which large language models (LLMs) are quietly affecting three areas — politics, education, and the workplace — and laid out the control points companies should hold as governance.

Today I want to translate that into something practical for executives, compliance, and legal.

And just so we are clear: I am not going to land this on "let's set up an AI Governance Committee." You have probably all seen at least one or two cases where a committee gets formed and then nothing actually moves.

[^1]: Keito Inoshita (2025). Political Impact of Large Language Models and Principles for Their Governance, 44th Student Paper Showa Ikeda Prize.

---

## Today's takeaway in 3 lines

1. Value: a company that builds AI governance properly can lower its regulatory cost and confidently expand AI use.
2. Structure: the control points an executive should hold come down to three — data, model selection, output review. Try to be comprehensive and it always ossifies.
3. Caution: treat governance as "regulatory compliance" and it ossifies. Treat it as "trust building" and it pays off in ESG and recruiting too.

Let me go in order.

---

## ① First, why "a convenient AI" becomes an executive agenda item

ChatGPT, Claude, Gemini, in-house RAG — these have already exceeded the scale of "convenient IT tools."

For example:

- AI drafts the initial response to customer inquiries
- AI generates the first draft of evaluation comments in HR
- AI checks the summary of internal documents
- Marketing copy, job postings, apology letters — AI is somewhere in every "language output"

What is happening here is not just efficiency gains. It is that AI is starting to quietly shape the "language norms" the organization releases to the outside world.

And often the field flags "I had AI write this" upward — and just as often, it doesn't. The latter is overwhelmingly more common.

From an executive perspective, "what fraction of the language we publish has been AI-generated with no human review" has become unknowable.

Meanwhile the EU AI Act, the U.S. NIST AI RMF, and Japan's METI AI Business Operator Guidelines are all moving in the same direction: "the AI generated it" is not a defense.

We are already in the era where "the AI did it" no longer holds up.

---

## ② The three things an executive should hold

Here is the heart of it.

If you try to design governance "comprehensively," it always ossifies. Because the moment you go comprehensive, you produce "a thick policy document nobody on the floor ever reads."

The control points an executive should keep in their own head come down to three. That is enough.

### Control point 1: Data — what is being trained on, and what is being fed in

LLM behavior is, in the end, decided by data.

- What was used in training (the model provider's responsibility)
- What was used in additional training (your responsibility)
- What the field is feeding in as input (the operator's responsibility)

The last one is a complete blind spot at many companies.

People paste confidential documents into ChatGPT for summaries. Customer personal information gets routed through it for translation. Contract drafts get handed to external APIs.

In an enormous number of cases, this happens without anyone having read the external API's terms of use or retention policy.

What the executive should do is hold a three-stage picture of the company's data flow: "what we trained on / what we feed in / where it goes." The actual operation can be left to IT and legal, but whether that three-stage picture is in the executive's head changes the speed of judgment dramatically when something happens.

### Control point 2: Model selection — the discipline of not using GPT-4 for everything

I wrote about this in the previous Nationality column, but the "always reach for the strongest model" reflex is wrong both on governance grounds and on cost grounds.

- External-facing (customer text, PR copy) → optimize for explainability
- Internal brainstorming, ideation → optimize for creativity
- Confidential documents, legal, HR → on-prem or strict data-protection contracts

This split is the main job of any AI governance committee. If a committee tries to enforce "we use Claude" across the entire company, operations will not hold, so the policy should be cut by business category.

It is also easy to forget that vendor terms change. LLM vendors silently flip "we do not train on your data" and "we do" — and an extraordinary number of companies have no one tracking that.

### Control point 3: Output review — who confirms what, by what standard

LLM output is fluent. Too fluent: errors arrive at customers and regulators wearing a respectable face.

What matters here is varying the granularity of human review according to usage risk.

- Internal brainstorming summaries → no review
- Internal materials → casual sign-off by the author
- Customer-facing documents → manager review required
- Regulatory reports, contracts, HR evaluations → final review by a qualified person

Write this matrix out by business category and share it across the company. That alone tightens output accountability significantly.

"Anything through AI requires review" kills the field, "no review anywhere" causes incidents. The gradient in between has to live in the executive's head.

---

## ③ The angle I want to add as an emotion-AI researcher

This is the point unique to Affectosphere Group.

When LLMs enter an organization, most companies first worry about "accuracy," "cost," and "information leakage."

But from an emotion-AI researcher's perspective, there is one more scary phenomenon:

When employees read "AI-written language" daily, employees' own emotional expression starts to be pulled toward AI-generated text.

AI drafts evaluation comments. AI drafts apology letters. AI gives example feedback for 1-on-1s.

Run this for a year, two years, and the emotional range of the language coming out of the organization converges on the AI's signature style.

Concretely: the words that become the organization's standard register are the ones AI is good at — "moderate, polite, hurts no one, lands on no one."

In compliance terms this even looks desirable.

But as an emotion researcher, I have to say: an organization in which everyone writes at the same temperature with the same cadence stagnates badly, psychologically. When the diversity of emotional expression dies, the diversity of decision-making dies with it.

Our lab's core stance is to handle emotion "as ambiguous and polysemous as it actually is." The language coming out of an organization should, by rights, also be allowed to remain more ambiguous and polysemous.

The last topic in LLM governance, I think, is this quiet but decisive one: "protect the organization's emotional range from being flattened by AI."

Regulation will never cover this. It is a question of the executive's aesthetic.

---

## So what do you do starting tomorrow

It would be unfair to only stack up risks, so three things you can act on at the field level.

- Three-stage data picture: write down on one page where your company stands on "trained on / fed in / sent to." Rough is fine at first.
- Output-review matrix: a one-page sheet of the required review level and the final reviewer, by business category. Operations tighten just from this.
- Periodic vendor-terms check: once a quarter, have legal review the terms and training-policy changes of every LLM vendor in use. Astonishingly few companies have made this a habit.

The value is big. The risk is big. Both belong on the executive agenda — that is the ask from the lab.

---

## Closing

Treat AI governance as a chore and you lose every bit of trust-building it could have produced.

The companies that can confidently show, internally and externally, "we have our AI under control" will gain a real edge over the next three years.

Data, model selection, output review — keep these three in the executive's hand. Don't stop at forming a committee. And as a matter of aesthetic, protect the "emotional range" of the language your organization produces from collapsing into AI's voice.

If "is our AI actually under control?" crossed your mind, just ask yourself those three points first.

So — that is it for today.

---

## References

1. 井下敬翔 (2025). *大規模言語モデルの政治的影響とガバナンスの指針*. 第44回学生論文昭和池田賞.

<p class="ai-notice"><small>* This article was written in part with AI assistance and may contain inaccuracies.</small></p>
