---
title: "From 'Reading' to 'Parsing' Case Law — AI Starts Mapping the Logic of Courts"
date: "2026-06-09"
excerpt: "HKJudge — a 290,000-sentence corpus of Hong Kong criminal judgments annotated with 26 rhetorical roles — lays the foundation for AI that automatically decodes how courts find facts, reason through law, and deliver rulings. A 5-minute read on what this means for legal tech teams and in-house counsel."
image: "/column-images/hkjudge-legal-discourse-corpus-court-reasoning.png"
imageAlt: "Flat illustration of court documents, a text-structure analysis diagram, and a gavel arranged in an abstract layout"
readingMinutes: 6
basedOnPaper: "HKJudge: A Legal Discourse-Annotated Corpus for Interpreting What Courts Find, How They Reason, and What They Rule"
basedOnPaperUrl: "https://arxiv.org/abs/2606.06679"
---

> _This article is an English translation of the original Japanese column. Some phrasing has been adapted for English readers._

Hello, this is Inoshita from Affectosphere Group.

When I talk to legal tech teams and in-house counsel, a shared frustration comes up every time.

"Case law piles up endlessly. But grasping, quickly, what a court actually thought and why it ruled the way it did — that's the hard part."

A court judgment is a block of structured logic. Over dozens of pages, it records what facts the court found, what chain of reasoning it followed, and what it ultimately ordered. Having humans work through each judgment one by one is simply not scalable.

A paper posted to arXiv in June 2026 [^1] tackles this problem head-on. The team built HKJudge: an expert-annotated corpus of Hong Kong criminal judgments, designed to train AI models to parse legal discourse at the sentence level.

Today I want to unpack this research for legal tech companies, law firms, in-house legal teams, and compliance professionals — with a focus on what it means in practice.

[^1]: Xi Xuan, Wenxin Zhang, Yufei Zhou, King-kui Sin, Chunyu Kit (2026). HKJudge: A Legal Discourse-Annotated Corpus for Interpreting What Courts Find, How They Reason, and What They Rule. arXiv:2606.06679.

---

## Today's three takeaways

1. HKJudge is the first large-scale corpus that labels court judgments at the sentence level with rhetorical roles — 290,000 sentences, 6.5 million tokens.
2. BERT, GPT, and other models were benchmarked on two tasks: rhetorical role classification and legal element extraction.
3. This data foundation enables AI tools that help lawyers and legal teams quickly identify how courts reasoned through facts in large volumes of case law.

Let me go through each.

---

## ① What HKJudge built

The team collected criminal judgments from all five tiers of Hong Kong courts and assembled a corpus of 290,000 sentences and 6.5 million tokens.

The standout feature is the annotation design. Each sentence in the judgments was assigned one of 26 rhetorical roles.

A quick explanation of what that means. Inside a court judgment, different sentences play different functions: some establish facts, some evaluate evidence, some develop legal arguments, some issue sentencing orders. When a human reads a judgment, the role of each sentence is inferred from context. Rhetorical role annotation makes that implicit structure explicit — labeling, for every sentence, the function it is serving in the court's reasoning process.

Twenty-six roles is not a rough "majority opinion vs. dicta" split. It is a fine-grained capture of the court's full arc from fact-finding through reasoning to ruling. Alongside sentence-level labels, the corpus also supports span-level extraction of three key criminal-law elements: charge, sentence, and fine.

Annotation was done by ten legal linguistics experts. Inter-annotator agreement reached κ = 0.8, which is a strong reliability score for a corpus of this complexity.

---

## ② What is hard, and what becomes possible

Benchmark evaluations using BERT and GPT models showed that rhetorical role classification is tractable, while legal element extraction remains more challenging.

Why the difficulty? Legal language has properties that differ from general text. Sentences are long, logic is deeply nested, interpretation depends on broad context, and legal terms carry domain-specific meanings that diverge from ordinary usage. These are exactly the areas where general-purpose LLMs tend to struggle.

The flip side: there is clear demand for models fine-tuned on legal discourse. A corpus like HKJudge is the raw material for that fine-tuning.

From an implementation perspective, the key design choice is the two-layer task structure. Sentence-level rhetorical role classification combined with span-level legal element extraction means the system can, progressively, answer the question "what was the structure of this judgment, and what sentence did it impose?" — rather than returning a simple keyword hit.

---

## ③ Implementation hints for legal and legal-tech teams

Here is where the practical talk starts. Let me map out the use cases and example KPIs.

The first application is case research support for lawyers and legal counsel.

If you can quickly surface "judgments where a court made a similar factual finding" from a large corpus, the research burden drops significantly. Today, a full-text search in a case database returns text matches — but whether and how the court weighted that passage requires a human to read through the document.

With rhetorical role classification, you can run searches restricted to specific parts of the judgment structure: "search only the fact-finding sections," or "extract statutes cited as reasoning grounds." That is structure-aware retrieval. A measurable KPI: time-per-case-research engagement.

The second application is sentencing trend analysis for compliance teams.

When a company is assessing legal risk, it needs to understand how courts have typically ruled on comparable cases. Span-level extraction of sentence length and fine amounts enables statistical visualization of "sentencing distribution across similar charge types." KPIs here include reductions in risk-assessment report preparation time and decreases in blind-spot exposure.

For legal tech product design, HKJudge points toward a natural expansion path. Starting from Hong Kong criminal judgments, the same methodology can extend to other common-law jurisdictions — UK, Singapore, Australia, and beyond — toward a multi-jurisdiction case analysis platform.

One practical caution. The final responsibility for legal judgment always rests with a human. Even if an AI presents "here is the reasoning structure of this judgment," whether and how to use that analysis in a legal argument remains a decision for a lawyer or in-house counsel.

The design principle: AI shows structure, humans make judgments. Rhetorical role output is an aid to reading comprehension, not a substitute for expert interpretation. That division of labor is the realistic implementation for now.

---

## A note from an emotion-AI researcher

Let me shift the angle slightly.

Court documents can look like pure logic, untouched by emotion. But reading judgments closely, you find that emotional and psychological elements are woven into the reasoning structure: the defendant's motivation, the court's evaluation of a victim's testimony, mitigating factors in sentencing.

When a court decides to "recognize the defendant's remorse," that sentence, in rhetorical role terms, belongs to the category of sentencing mitigation. Being able to automatically parse the structure of sentences that carry emotional assessments like this opens up the possibility of studying emotion's role in legal discourse quantitatively.

From an emotion-AI research standpoint, HKJudge is also raw material for exploring the intersection of law and emotion. This is a thread we are actively pulling at in Affectosphere Group.

---

## Closing

The shift from "reading" to "parsing" case law has quietly begun.

HKJudge is specific to Hong Kong criminal judgments, but the design philosophy it demonstrates is general. Structure legal discourse with rhetorical roles; give AI a map of the logic.

The goal is to reduce the cost of lawyers and legal teams working through individual judgments, and redirect that freed capacity toward deeper consultation with clients.

If you are exploring implementation: start by deciding which phase of legal decision-making you want AI to assist with structurally. Not full automation — but structured support for the pre-reading step, before human judgment takes over. Lower risk, faster learning.

That is it for today.

---

## References

1. Xi Xuan, Wenxin Zhang, Yufei Zhou, King-kui Sin, Chunyu Kit (2026). *HKJudge: A Legal Discourse-Annotated Corpus for Interpreting What Courts Find, How They Reason, and What They Rule*. arXiv:2606.06679.

<p class="ai-notice"><small>* This article was written in part with AI assistance and may contain inaccuracies.</small></p>
