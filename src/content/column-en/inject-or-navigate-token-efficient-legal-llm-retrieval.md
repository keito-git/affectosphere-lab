---
title: "Stop feeding whole contracts to the AI — cutting legal-document API cost by up to 56x with inject vs. navigate"
date: "2026-07-08"
excerpt: "When you have an LLM read a pile of transactional contracts and answer questions, dropping the full text into the prompt is the most natural move. It is also the most expensive one under token billing. On a 20-question benchmark, reranked semantic retrieval kept the same accuracy while cutting context tokens by 17.3x, and the LLM-navigation approach NAVINDEX compressed context size by about 56x. Here is how to lower the API cost of contract-review and legal-research AI structurally, from a legal-tech point of view."
image: "/column-images/inject-or-navigate-token-efficient-legal-llm-retrieval.png"
imageAlt: "Flat illustration of a large corpus of transactional contracts on the left, with three paths — Full Injection, NAVEMBED, NAVINDEX — showing token reduction ratios of 1x, 17.3x, and 56x, next to a cost-crossover graph marking where cached injection breaks even against retrieval"
readingMinutes: 6
basedOnPaper: "Inject or Navigate? Token-Efficient Retrieval for LLM Analysis of Transactional Legal Documents"
basedOnPaperUrl: "https://arxiv.org/abs/2607.05764"
---

Hello. I am Miura from Affectosphere Group.

There is a wall almost everyone hits when they first bring an LLM into legal work. Not the client invoice — the API invoice.

You have the AI read a contract or a set of terms and you ask, "What are the termination conditions in this clause?" or "How far do the representations and warranties reach?" The method is simple: paste the full contract into the prompt and send it along with the question. That is the most straightforward idea. But transactional contracts routinely run to dozens of pages, and once you run hundreds or thousands of them, token billing starts to add up — slowly, sometimes all at once. Full injection gives you accuracy, but it is also the most lavish way to spend.

A study published on arXiv (Mahmoud Hany, Mourad ElSheraey, Mahmoud Said, Peter Naoum, arXiv:2607.05764) takes this question — how should an LLM read a large body of transactional legal documents — and compares the options head-on from a cost-efficiency angle. Do you "inject" the whole text, or do you "navigate" to just the parts you need? Today I want to read that question through the practical lens of legal-tech API cost optimization.

---

## Three takeaways

1. Full injection is accurate but the most token-expensive. Instead, the study compares two structured retrieval methods — embedding-based NAVEMBED and NAVINDEX, which has the LLM traverse the document — on a 20-question benchmark.
2. Reranked semantic retrieval kept performance on par with injection while cutting context tokens by 17.3x. NAVINDEX matched injection performance across all 18 questions while shrinking total token footprint by 1.61x and compressing context size by about 56x.
3. It also derives a closed-form crossover rule: cached full injection is only cost-effective when the corpus size is at most about 10x the retrieval payload. So you can decide between injection and retrieval by formula, not by gut, according to matter size.

---

## ① Why full injection is "expensive"

First, let me lay out why full injection is hard on the budget.

LLM APIs charge by the volume of input tokens. Stuffing the entire contract into the prompt means paying for the whole document's worth of tokens on every single question. For one contract it is nothing; for work that sweeps across hundreds or thousands of documents — legal research, M&A due diligence — that "pay for all of it every time" structure lands directly on your running cost.

And in most cases, only a small slice of the document is actually relevant to the question. You want to ask about the termination clause, yet you make the model read everything from the recitals through the definitions each time. A human lawyer opens only the relevant page; naive LLM usage forces "read the whole thing from the top, every time."

That is exactly where retrieval — stop injecting, go fetch only what you need — earns its place. The study compared two schools of "how to go fetch."

---

## ② NAVEMBED and NAVINDEX: two schools of fetching

As challengers to full injection, the study set up two structured retrieval methods with different temperaments.

The first is NAVEMBED, embedding-based semantic search. You chunk the document up front, vectorize it, and pull back only the fragments semantically closest to the question — the classic RAG (retrieval-augmented generation) approach. Add reranking (a step that reorders retrieved candidates for precision), and it kept performance on par with injection while cutting the context tokens handed to the question by 17.3x. If you can shrink tokens by more than an order of magnitude without losing accuracy, the cost picture already changes.

The second is NAVINDEX, a navigation approach that has the LLM itself traverse the document structure. You show the LLM a table of contents or index and let it decide, "for this question, which section should I open?", opening only the needed parts step by step. It mimics how a human jumps from the index of a thick contract straight to the relevant spot. NAVINDEX matched injection performance across all 18 benchmark questions while shrinking the total token footprint (the sum of tokens exchanged across the whole process) by 1.61x and compressing the context size handed to the question by about 56x.

What is interesting is that the two cut in different places. NAVEMBED thins out "the context you pass at question time." NAVINDEX does that and also makes the traversal itself smarter, lightening the whole token budget. Which one wins depends on the volume and structure of the documents you handle.

---

## ③ Deciding "inject or retrieve" by formula — the closed-form crossover rule

What struck me as especially useful here is that the study answers "so which one should I use?" with a formula.

Retrieval is not universally best. When there are few documents, the effort of building the retrieval machinery can outweigh the gain, and naive full injection is sometimes cheaper. This is especially true when you reuse the same document repeatedly, because prompt caching (reusing already-sent context to hold cost down) kicks in and tilts the balance further toward injection.

The study derives this break-even as a closed-form crossover rule. Roughly: cached full injection is cost-effective only when the corpus size is at most about 10x the payload you retrieve. In other words, if your document corpus is that small, injection is fine; grow past that point and switching to retrieval pays off — and that threshold can be drawn in numbers.

This is a weapon for design decisions. Not "let's just go with RAG" or "let's just paste it all in," but: estimate the corpus size of the matter and the retrieval payload per question, and you can calculate in advance which is cheaper. Deciding how to build the system by rule rather than by gut is a gift for anyone who has to justify the cost.

---

## ④ How to try it on the floor: departments and KPIs

So how do you land this in your own legal-tech stack? Let me put down one concrete rollout scenario.

Picture an AI contract-review system at a law firm or corporate legal department that handles hundreds to thousands of transactional contracts. The aim is simple: move the existing "full-injection" question-answering pipeline onto NAVINDEX-style structured retrieval. Keep answer accuracy on par while structurally lowering the API cost per question.

Here is the picture of departments and uses. An M&A due-diligence lead targets just the termination and change-of-control clauses out of a large set of target contracts. A financial institution's legal and compliance team runs cross-checks across terms and policies through relevant-section navigation instead of reading the full text every time. A corporate-legal API-cost owner first measures their own corpus size, applies the crossover rule, and builds an operating policy of "inject this matter, retrieve that one." All of them share the same shape: many documents, repeated questions, but only a slice actually needed.

For measurement KPIs, so you can tell the story in numbers, I propose the following. First, the most legible one — API cost reduction rate: against full injection as the baseline, by what percent did the token billing per question drop after moving to NAVINDEX? The study's context-size figure of about 56x is a direct benchmark for "there is room to get this much lighter at the same accuracy." Second, accuracy retention — proof that lowering cost did not drop the correct-answer rate (the study held parity across 18 questions). Third, processing throughput — how many more contracts you can handle per day on the same budget.

As for the path, I think the safe move is to run the injection version and the retrieval version side by side on a subset of matter types first, and confirm on your own data that accuracy is truly on par. Then, following the crossover rule, shift the large-corpus workloads toward retrieval. Measure small, expand from where it worked. In that order you can stack cost savings without sacrificing accuracy.

---

## The elegant cost cut of "not reading everything"

What felt good reading this study is that its way of cutting cost is elegant.

It is not a war of attrition — switching to a cheaper model, giving up accuracy. By fetching only what is needed, it cuts tokens by one or two orders of magnitude while keeping accuracy. Just letting go of the naïveté of "read everything" opens up this much room. And whether to inject or retrieve is settled by formula. It is not flashy, but the more documents you run every day, the more this difference lands like a body blow.

One last word from the affective-AI angle. The large emotion corpora we work with quietly carry the same problem. Labeling vast amounts of text with emotions, done naively, tends toward the same "process everything every time" high-cost structure. The design philosophy of going to fetch only what is needed feels like it carries straight over to the cost design of scalable emotion annotation. For contracts and for emotion data alike, "the wisdom of not reading everything" looks like a shared weapon.

That is it for today!

---

## References

1. Hany, Mahmoud, ElSheraey, Mourad, Said, Mahmoud, & Naoum, Peter (2026). *Inject or Navigate? Token-Efficient Retrieval for LLM Analysis of Transactional Legal Documents*. arXiv preprint. https://arxiv.org/abs/2607.05764

<p class="ai-notice"><small>* This article was written in part with AI assistance and may contain inaccuracies.</small></p>
