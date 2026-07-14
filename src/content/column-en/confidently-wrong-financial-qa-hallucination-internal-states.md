---
title: "How to handle an AI that is confidently wrong — triaging financial QA errors with an internal-state probe"
date: "2026-07-14"
excerpt: "In financial LLMs, the most damaging error is not an uncertain answer — it is a confident wrong one. A study by Wang (arXiv:2607.11414) shows that 15–23% of 'confident' answers on the FinQA benchmark are actually incorrect, and that a linear probe on the residual stream detects them far better than token log-probabilities or self-reported confidence. Here is how a triage layer based on internal states could be built into a financial QA pipeline."
image: "/column-images/confidently-wrong-financial-qa-hallucination-internal-states.png"
imageAlt: "Flat illustration of a triage flow where an AI system processing financial disclosure documents uses an internal-state sensor to detect error risk and automatically routes high-risk answers to a human review lane"
readingMinutes: 5
basedOnPaper: "Confidently Wrong: Detecting Hallucinations in Financial Question Answering from LLM Internal States"
basedOnPaperUrl: "https://arxiv.org/abs/2607.11414"
---

Hello. I am Miura from Affectosphere Group.

"The AI got something wrong. But it sounded a bit uncertain, so we double-checked." That kind of story is becoming routine in business settings.

The dangerous version is the opposite.

An AI states a revenue figure and operating profit with complete confidence — and turns out to be entirely wrong.

People notice when an AI seems hesitant. When an AI sounds certain, we tend not to question it. In financial decision-making, that confident-but-wrong answer is by far the most damaging type of failure.

A study by Wang (arXiv:2607.11414) addresses exactly this problem. Today I want to think about how organizations running financial QA systems can structure a response, taking cues from this research.

---

## Three takeaways

1. In financial LLMs, the most damaging failure is the "confident hallucination" — wrong answers delivered with certainty. Ambiguous answers attract scrutiny; certain-sounding wrong answers flow downstream unchecked.
2. In the FinQA benchmark, built from actual disclosure documents, 15–23% of answers that were "confident" — identical across 8 resamplings of the same question — turned out to be wrong.
3. A linear probe on the residual stream achieved AUROC 0.68–0.77 across three models (Qwen3-8B, Llama-3.1-8B, Gemma-2-9B), well above token log-probability and self-reported True/False baselines of 0.55–0.63.

---

## ① Why the "confident wrong answer" is in a different danger class

Let me start with the setup.

AI making mistakes is already being factored into many workplaces. "Always verify before acting on AI output" is a norm that is gradually taking hold.

But verification does not happen evenly.

Answers that feel uncertain get checked. Answers that sound authoritative tend to pass straight through.

The problem this paper raises is that a substantial share of those "confident answers" turn out to be wrong.

The study defined a "confident answer" as one where all 8 resamplings of the same question returned the same response. Against benchmarks built from actual disclosure documents — FinQA and TAT-QA — FinQA showed that 15–23% of these confident answers were incorrect.

In other words, an AI sounding certain and an AI being correct are quite different things.

In finance, this gap is especially costly. Querying an LLM about figures in securities reports, earnings releases, or prospectuses, then basing investment decisions or credit reviews on the response — that is a real workflow. When a confident wrong answer enters that flow, catching it afterward is very hard.

---

## ② Looking beyond the output: the linear probe approach

So what can you do?

The most obvious approaches are either asking the AI how confident it is, or looking at token log-probabilities on the output side. This study tested both as baselines and found AUROC scores of 0.55–0.63. Neither gives you enough signal to detect wrong answers reliably from the output alone.

What the paper proposes instead is training a linear probe on the LLM's residual stream.

The residual stream is the internal intermediate representation that an LLM maintains as it processes a query — the model's state while it is "thinking," before anything appears in the output.

Training a linear classifier (a probe) on that representation, across Qwen3-8B, Llama-3.1-8B, and Gemma-2-9B, produced AUROC of 0.68–0.77. The internal representation carries information that does not show up in the output, and that information turns out to be useful for distinguishing correct from incorrect answers.

My read of this result is that models may, in some sense, already "know" whether they are right before they produce an answer — but that knowledge does not get translated into an honest confidence signal in the output. That is a striking implication for any approach that relies on an AI's self-report of certainty.

---

## ③ How to try this on the floor: departments and KPIs

Here is my implementation scenario for putting these findings to work.

The goal is to add an "internal-state triage layer" to the financial QA system your organization is already running.

Concretely: when the LLM generates a response, you also capture the intermediate representation from the residual stream. A probe scores that representation for error risk. Answers that exceed the risk threshold are automatically routed to a human review queue.

Reviewing every single response is too expensive. Reviewing nothing is too risky. "Route the high-risk ones to humans" is a way to allocate human-in-the-loop costs where they matter most.

Here are the departments I have in mind.

First, risk management and internal audit. Measure what fraction of your AI's "confident" answers on disclosure document queries are actually wrong. Tune the probe threshold to determine the review scope. In the early phase, a practical target is whether the approach reduces total review effort compared to checking everything manually.

Second, compliance and legal. For financial institutions using generative AI, "how is human oversight maintained" is a regulatory accountability question. Triage logs based on internal states could serve as documentation material for that question. To be clear, this is my own interpretation — not a claim that the research validates compliance with any specific regulation — but the evidentiary value of such logs strikes me as real.

Third, DX and AI product teams. These are the people building and operating financial QA in-house, and they would be the ones inserting a probe layer into the existing pipeline. Starting with internal tooling rather than a customer-facing API makes the first iteration considerably easier.

For KPIs, I would propose three.

First, human review rate — what share of all responses get routed for human check. Too low and you miss errors; too high and the cost savings disappear. Where the right level lands will depend on your organization's actual error distribution, so use your own data rather than any number from the paper.

Second, error rate within routed responses — a check that the probe is actually surfacing the wrong answers rather than sampling randomly. Compare it to a random sample of non-routed answers to see how much better the probe is doing.

Third, downstream cost of errors — incident count, correction effort hours. Ultimately this is the number that needs to move to justify the investment.

On sequencing: I would start with the task types closest to FinQA and TAT-QA — numerical extraction, comparison, calculation — where the distinction between correct and wrong is clear. Build confidence and reduce costs there before expanding to more open-ended query types.

Probe accuracy is likely to vary by task type. Starting narrow, building trust, then widening — that order matters.

---

## Toward a world where you look inside the AI before you trust it

The suggestion from this research is simple and a little unsettling.

An AI answering with complete confidence does not mean the answer is correct. And confident wrong answers are hard to detect by looking at the output alone.

The flip side: looking at the internal state may give you signal that the output does not contain.

In a domain like finance, where the cost of a wrong answer is high, that gap is not small.

Even if you are not ready to implement a probe, dropping the assumption that "AI confidence equals trustworthiness" already changes how you design governance policies, audit log requirements, and review workflows for generative AI use in your organization.

That is it for today!

---

## References

1. Wang, Richard Zhe (2026). *Confidently Wrong: Detecting Hallucinations in Financial Question Answering from LLM Internal States*. arXiv preprint. https://arxiv.org/abs/2607.11414

<p class="ai-notice"><small>* This article was written in part with AI assistance and may contain inaccuracies.</small></p>
