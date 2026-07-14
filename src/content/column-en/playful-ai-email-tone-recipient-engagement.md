---
title: "Does AI email rewriting actually raise reply rates? A field experiment with 16,880 real emails points to emotional positivity as the real driver"
date: "2026-07-14"
excerpt: "AI tone rewriting of business emails had zero direct effect on open rate, reply rate, or response speed. But playful rewriting did raise senders' emotional positivity scores, and that positivity strongly predicted replies. Here is what a three-week field experiment across six companies and 16,880 real emails found — and what it means for how you design and measure email-support AI."
image: "/column-images/playful-ai-email-tone-recipient-engagement.png"
imageAlt: "Flat illustration of a business email passing through an emotional temperature meter and arriving in an inbox suffused with a warm, positive tone"
readingMinutes: 5
basedOnPaper: "Playful AI in Professional Email: A Field Experiment on Tone and Recipient Engagement"
basedOnPaperUrl: "https://arxiv.org/abs/2607.11749"
---

Hello. I am Miura from Affectosphere Group.

You may recognize this kind of conversation.

"We rolled out an AI email-rewriting tool for the sales team and the reply rate barely moved." "After the AI tidied everything up to sound professional, responses actually felt thinner." "Honestly, we still are not sure where to measure the impact of email-support AI at all."

The expectation that AI-rewritten emails will move the needle is spreading fast, but the numbers are slow to follow. This gap is real in a lot of organizations.

A study published on arXiv (Ben-Zion & Lazebnik, arXiv:2607.11749) tests that very question in a live business setting — a three-week field experiment with 121 employees across six companies sending 16,880 actual work emails.

Today I want to read through what this experiment found from the lens of affective computing — emotional AI.

---

## Three takeaways

1. 121 employees across six companies participated in a three-week randomized crossover design. They sent 16,880 real business emails under three conditions: unedited writing, GPT-5 rewriting toward a playful tone, and GPT-5 rewriting toward a professional tone. Open rate, reply rate, response speed, and emotional tone were measured.
2. AI tone rewriting had zero direct effect on open rate, reply rate, or response speed. But the playful rewrite significantly raised the sender's emotional positivity (B=+0.068, p<0.001), and that positivity strongly predicted both opens (OR=2.05) and replies (OR=3.32, p<0.001).
3. AI rewriting does not change recipient behavior directly. It works only through an indirect path: it shapes the emotional tone of the language, and that tone is what moves the reader. Both where you measure KPIs and how you design tone need to be rethought.

---

## ① What actually happened across 16,880 real emails

Let me start with the experimental design.

The participants were 121 employees across six companies. The study ran for three weeks using a randomized crossover design, meaning the same individuals rotated through all three conditions at different points. The conditions were: unedited writing, GPT-5 rewriting toward a playful tone, and GPT-5 rewriting toward a professional tone.

The emails were real work emails — 16,880 in total. This is not a laboratory roleplay or simulated correspondence. It was measured inside actual work communication, which is the study's primary strength.

What they measured: open rate, reply rate, response speed, and the emotional positivity embedded in the sender's language.

The result that came back was quite clear.

The direct effect of AI tone rewriting on open rate, reply rate, and response speed was zero. The intuition that "rewrite the email with AI and recipient behavior will shift right away" was not supported by this experiment.

The story does not end there, though.

---

## ② The invisible path: emotional positivity

So what was moving? This is the part that is interesting from an affective computing perspective.

AI rewriting was changing the emotional tone of the language. The playful rewrite significantly raised the emotional positivity in the sender's writing (B=+0.068, p<0.001). The professional rewrite did the opposite — it lowered positivity (B=-0.041, p<0.001).

And that emotional positivity strongly predicted open rate and reply rate. The odds ratio for opens was OR=2.05. For replies it was OR=3.32 (p<0.001).

Laid out as a structure, the finding looks like this.

The path "AI rewriting → change in emotional positivity → change in recipient behavior" was real. The path "AI rewriting → direct change in recipient behavior" did not exist.

From an affective computing standpoint, that is a finding close to the core of the field. People do not process the semantic content of a message separately from its emotional temperature. However accurate and formal the content, a message with lower emotional warmth is less likely to pull the reader into action. That is what 16,880 real emails showed.

The professional-tone condition also stands out. It actively lowered emotional positivity. "I made it more professional — and the temperature dropped" is the story the data is telling. If you assume that professional-izing an email is always an improvement, this risk stays invisible. My own reading is that AI writing tools calibrated toward formal polish may be quietly eroding positivity in ways the teams using them cannot see.

---

## ③ How to try this on the floor: departments and KPIs

How would you actually use this in your organization? Here is my implementation scenario.

The most consequential shift is moving your email-support AI's KPI from "did the team use AI or not" to "what was the emotional positivity score of the emails they sent." The unit of measurement changes from adoption to output quality.

Concretely, you embed a tone-score visualization inside the email client or writing-support tool. Every email gets an emotional score before it is sent, and only emails falling below a threshold get a rewrite suggestion. Not "run everything through AI automatically," but "gate only the low-temperature drafts." I would call this an emotional tone gate.

Here are the departments I have in mind, and what they would measure.

Inside sales and field sales are the natural first target. These teams send large volumes of emails daily. Surface a positivity score in the compose window before send. Track each sender's score trend weekly, and offer rewrite prompts when the trend is dropping. The KPI to track is the correlation between average positivity score per sender and actual reply rate. The question is not whether AI was used — it is whether the tone was warm enough.

Customer success is another strong candidate. Emails around churn prevention and escalation handling are places where emotional tone likely affects more than just reply rate — it shapes how the customer feels about the company. Building a pre-send tone check into CS workflows and measuring the correlation between positivity score and post-interaction customer satisfaction gives you a direct line between tone design and business outcome.

Internal communications and HR also have a use here. Company-wide announcements, release notes, and policy updates sent to large internal audiences are exactly the kind of emails that often get "professionalized" before they go out. Monitoring the tone of these sends over time — looking for the signature of positivity quietly declining — is a concrete way to catch the pattern before it becomes a problem. Track open and reaction rates as your baseline metric.

One thing worth flagging before you go implement: this study does not say "make every email playful and replies will increase." It found that emotional positivity mediated the effect of tone rewriting on recipient behavior. The right level of positivity varies by context, industry, relationship, and message type. Treat tone as a parameter, run A/B comparisons with your own data, and calibrate what positivity level actually moves responses in your specific context.

---

## "Did we deploy AI?" is the wrong question. "What tone did we design?" is the right one.

The thing this paper left with me most clearly is that whether AI was used is not the meaningful question.

AI is a tool for adjusting the emotional tone of language, and emotional tone is what moves people. The question worth asking is not "have we adopted AI email rewriting" but "what emotional tone are we intentionally designing into the messages we send."

"We deployed AI and reply rates did not change" is, I suspect, usually a story about tone being pushed too far in the professional direction and positivity being stripped out in the process.

Affective computing has pointed at this for a long time: human communication cannot be separated from its emotional temperature. This field experiment confirmed that it holds for business email reply rates — a very concrete, measurable outcome — across 16,880 real emails.

That is it for today!

---

## References

1. Ben-Zion, Ziv, & Lazebnik, Teddy (2026). *Playful AI in Professional Email: A Field Experiment on Tone and Recipient Engagement*. arXiv preprint. https://arxiv.org/abs/2607.11749

<p class="ai-notice"><small>* This article was written in part with AI assistance and may contain inaccuracies.</small></p>
