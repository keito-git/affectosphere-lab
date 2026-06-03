---
title: "I Made GPT Take the Real-Estate Exam, and Saw the Shape of the Future of Licensed Professions"
date: "2026-06-01"
excerpt: "What happens when GPT-3.5 and GPT-4 take Japan's licensed real-estate broker exam. A 5-minute take, for legal tech, in-house legal, and licensed professionals, on how to turn an 'AI that can't pass' into a tool that makes pass-holders 1.5× more productive."
image: "/column-images/llm-legal-exams.png"
imageAlt: "Abstract visual of a law book, an exam sheet, a scale of justice, and a pass line"
readingMinutes: 6
basedOnPaper: "Assessing GPT's Legal Knowledge in Japanese Real Estate Transactions Exam"
basedOnPaperUrl: "https://arxiv.org/"
---

> _This article is an English translation of the original Japanese column. Some phrasing has been adapted for English readers._

Hello, this is Inoshita from Affectosphere Group.

I have been talking with companies evaluating legal tech a lot recently, and the same question always comes up:

"So — how far can we actually trust an LLM?"

It is, honestly, a very fair question.

"It hits 90% accuracy" — fine, but if the missing 10% lands on a key contract clause, the deal is over. The other way around: "It hits 60%" — fine, depending on the use case that is more than enough.

The best material for answering this question quantitatively is the past papers of national licensing exams.

The scope is clear, the passing line is publicly defined, the error patterns are easy to analyze. It is a rare arena where the "ability to substitute for the job" can be discussed in numbers.

In a paper I wrote in 2024 [^1], I had GPT-3.5 and GPT-4 take ten years of past papers from Japan's Licensed Real Estate Broker (hereafter "takken") exam.

Today I want to unpack the results, not as a technical paper, but as material for the question "how far should we integrate an LLM into our own business?"

[^1]: Keito Inoshita (2024). Assessing GPT's Legal Knowledge in Japanese Real Estate Transactions Exam, 3ICT 2024, pp. 149-155.

---

## Today's takeaway in 3 lines

1. Value: even an "AI that can't pass" can compress the working hours of someone who can. That is where the ROI of legal tech sits.
2. Structure: the weak spots of general-purpose LLMs are "domain-specific small print" and "keeping up with the latest law." Conversely, plug those with RAG and the thing transforms.
3. Caution: a design that hands "final judgment" to the LLM is — legally and litigation-wise — unacceptable today. Use it as a draft engine.

Let me go in order.

---

## ① First, what we found

The study had GPT-3.5 and GPT-4 take ten years of takken past papers and compared accuracy and error patterns.

Roughly:

- GPT-4 outperformed GPT-3.5 across the board
- Neither model reached the takken pass line
- Errors concentrated on domain-specific small print such as tax law and the Real Estate Brokerage Act
- Auxiliary prompts like "consider customary law" and "consider real-estate transaction practice" improved accuracy on complex case items

"With the latest GPT you get judgment on par with a license holder" — at the level of national licensing, at least, this does not hold today.

But stopping here would not be fair.

"Cannot pass" and "cannot be used in business" are two different things.

---

## ② Why an "AI that can't pass" is still usable in practice

The working hours of a takken-licensed broker are not, in fact, spent solving exam-style problems.

The bulk of the work is things like:

- Reading property documents and pulling out the issues
- Surveying similar past cases and comparing structure
- Drafting the Important Matters Explanation document
- Pulling and organizing the relevant statutes in response to customer questions
- Getting a final check from a senior or a license holder

The LLM's role here is not "final judge" — it is "draft engine," "issue-extractor," "first-pass surveyor."

That layer is exactly where GPT-4 shines. Even at the "below pass line" accuracy seen in the study, it is plenty usable.

For example, when a broker is asked "is this property eligible for the housing-loan tax deduction?"

- First, have the LLM do a first-pass survey of the relevant statutes
- A license holder then verifies the surfaced statutes against current law
- If needed, the question is escalated to a certified tax accountant

In this design, the risk that the LLM "gets a tax-law detail wrong" is absorbed by the license holder's final check.

And the license holder's working time can probably be compressed by something like 50%.

That is the "turn an AI that can't pass into a tool that makes the pass-holder 1.5× more productive" idea.

---

## ③ Plug the weak spots structurally — the (obvious) RAG story

Another thing the study found is: "auxiliary prompts improve accuracy on complex problems."

In other words, there are cases where the LLM does not "lack the knowledge" but "cannot retrieve it without an appropriate reference frame."

The conclusion that falls out naturally is: use RAG (Retrieval-Augmented Generation).

The biggest weak spot of general-purpose LLMs is the training-data cutoff — they cannot keep up with the latest amendments. The Real Estate Brokerage Act, tax law, labor law, the Act on the Protection of Personal Information — the more frequently a domain is amended, the more dangerous it is to use a general-purpose LLM as-is.

The fix is a design that lets the LLM "reference" the latest statute database.

Use the LLM not in isolation but as "LLM + latest-statute DB + internal rules + license holder's final check."

The standard answer for legal-tech architecture is going to be this four-piece set for a while, I think.

---

## ④ The angle I want to add, as an emotion-AI researcher

This is the perspective unique to Affectosphere Group.

When designing legal tech, most companies think about "accuracy," "cost," and "audit trail."

That is right. But there is one more thing you cannot afford to miss.

The "feelings" of the customer and of the license holder.

Real-estate transactions are not procedures people go through many times in life. Buying a house, moving, inheritance — in nearly all of these moments, the customer is tense, full of things they don't understand, anxious.

When you put an AI at the front desk for those customers, one design slip away you get responses that are "neutral, accurate, but cold."

Returning a technically correct but emotionally inappropriate answer to an anxious customer — this is not a regulatory violation, but it reliably erodes trust in the service.

And it does not show up in the numbers.

Our lab's core stance is to handle emotion "as ambiguous and polysemous as it actually is." When a customer says "I don't get it," behind it there may be anxiety, confusion, or distrust of professionals.

If you compress all of that down to "the content of the question" and hand it to the LLM, the AI can only return "an answer to the question."

What the front desk of a legal-tech service really needs is a design that "stops for a second, senses what the customer is anxious about, and only then answers."

The same is true on the license holder's side.

When the LLM drafts for them, the holder's time gets freed up. Whether they spend that freed time on "handling more cases" or "deepening the conversation with each customer" will, five years out, completely separate good practices from average ones.

The proposal from an emotion-AI researcher is simple:

> Put one line — "resolution of the customer's feelings" — into the design metrics of legal tech.

Just that has a real chance of nudging the industry from a "accuracy and efficiency" race to an "accuracy, efficiency, and feeling-resolution" race.

---

## So what do you do starting tomorrow

It would be unfair to only stack risks, so three things you can act on at the field level.

- Document the boundary: write down the LLM use policy for legal and contract work as "drafting yes, final judgment no." That alone unblocks the field.
- Logs stored together: store LLM output, referenced statutes, and the license holder's final judgment in one record inside the business system. Pays off every audit.
- Front-desk design: explicitly define "the range AI can answer" and "the threshold for escalating to a human." Put a "this customer seems anxious" signal into the escalation logic.

The value is big. The risk is big. Look at both — that is the ask from someone studying both AI and emotion.

---

## Closing

An LLM that cannot pass the takken cannot replace a takken-licensed broker.

But it can compress the share of the broker's working hours spent on research, organizing, and drafting.

And the practices that can redirect that freed time into "the quality of conversation with each customer" will, over the next five years, reliably win.

While being wary of the "LLM replaces the license holder" scenario, the "LLM makes the license holder 1.5× more productive" scenario is already within reach.

Do not conflate the two. Invest in the design as an assistive tool — that is the realistic answer in the legal-tech area.

And if I can add one thing from the emotion-AI side: put "resolution of the customer's feelings" into the design metrics, as one line. That, I suspect, will shift the competitive axis of the industry by a notch.

If you are thinking "should we adopt legal tech too?" — start from positioning it as a draft engine.

So — that is it for today.

---

## References

1. Keito Inoshita (2024). *Assessing GPT's Legal Knowledge in Japanese Real Estate Transactions Exam*. 3ICT 2024, pp. 149-155.

<p class="ai-notice"><small>* This article was written in part with AI assistance and may contain inaccuracies.</small></p>
