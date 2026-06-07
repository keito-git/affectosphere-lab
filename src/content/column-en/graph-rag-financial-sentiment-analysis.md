---
title: "Reading One Company's News Is Not Enough to Understand That Company's Stock"
date: "2026-06-07"
excerpt: "Sentiment propagates across supply chains and partnerships in ways that vector search cannot capture. Graph-RAG improves entity recall by 6.4% and answer relevance by 11.7% on complex cross-entity queries — with only a 22.6% latency increase. Here is what this means for financial research automation."
image: "/column-images/graph-rag-financial-sentiment-analysis.png"
imageAlt: "An abstract flat illustration showing news nodes from multiple companies connected by sentiment-weighted edges in a knowledge graph"
readingMinutes: 5
basedOnPaper: "Graph-Augmented Retrieval for Cross-Entity Financial Sentiment Analysis: A Comparative Study"
basedOnPaperUrl: "https://arxiv.org/abs/2606.00062"
---

Hello. This is Keito Inoshita from Affectosphere Group.

One of the biggest challenges for equity analysts right now is signal extraction from information overload.

Hundreds of news articles every day. Earnings releases, regulatory filings, social media. Identifying what actually matters for a specific stock is already beyond what any individual analyst can do manually. The demand for AI-assisted research is real and growing.

But conventional vector-search-based RAG (Retrieval-Augmented Generation) has a structural blind spot. When you search for "news about Company A," you only retrieve text that directly mentions Company A. You miss the indirect effects.

Company B, A's major supplier, has a compliance scandal. Company C, B's major customer, revises guidance downward. These second-order signals are hard to surface through text similarity search alone.

A study published on arXiv in May 2026 (Rajan Bastakoti, Sagar Bhetwal, Nirajan Acharya, Gaurav Kumar Gupta; arXiv:2606.00062) addresses this with knowledge graph augmentation. The researchers built sentiment-weighted knowledge graphs from 255 news articles covering 10 stocks and ran a systematic comparison of Graph-RAG against conventional vector retrieval.

---

## Three takeaways for today

1. Graph-RAG improved entity recall by 6.4% and answer relevance by 11.7% on cross-entity queries compared to vector search.
2. The improvement is concentrated in complex, multi-entity questions; Graph-RAG shows little advantage over vector search for simple single-entity lookups.
3. The 22.6% latency increase is acceptable for daily research cycles even if it rules out real-time trading applications.

---

## ① What changes when you use a knowledge graph

Standard RAG converts documents into embedding vectors and retrieves based on cosine similarity to the query. This works well for factual lookups and single-entity information retrieval.

Graph-RAG extracts entities (companies, people, events) and their relationships from documents, building a structured knowledge graph. At retrieval time, instead of just ranking similar text chunks, the system traverses graph edges to collect information about related entities too.

In this study, the graph is constructed from 255 financial news articles covering 10 stocks. Each edge in the graph carries a sentiment weight — positive, negative, or neutral. This captures not just which companies are connected, but the emotional valence of their relationship in the news flow.

That sentiment-weighted structure is what enables better performance on questions like "what are Company A's supply chain risks" or "how has Company A's relationship with its customers shifted this quarter." Vector search retrieves text that mentions A. Graph-RAG also traverses to A's suppliers, customers, and partners and brings back their sentiment signals.

---

## ② What the numbers actually show

Three specific metrics stand out from this study.

Entity recall +6.4%. This measures whether the system retrieves information about all the relevant companies when a cross-entity question is asked. Graph-RAG outperforms vector search specifically on multi-entity queries.

Answer relevance +11.7%. This evaluates how well the LLM's generated answer matches the actual intent of the query. The gap is most pronounced for complex questions involving intercompany relationships — supply chain dependency analysis, competitive positioning, contagion risk.

Latency increase 22.6%. Graph traversal adds processing time. For real-time trading applications, this may be prohibitive. For daily research report generation, it is well within acceptable range.

The study also found that for simple, single-entity queries, Graph-RAG offers no meaningful advantage. This suggests the practical architecture is a hybrid: use Graph-RAG when cross-entity relationship analysis is needed, use vector search for straightforward factual lookups. The two approaches are complementary.

---

## ③ Thinking through deployment in a research team

Taking this research to its logical conclusion in a financial research context, the most accessible near-term use case is research report drafting support.

When an analyst wants to summarize supply chain risk for a sector, or map how sentiment about a key supplier is flowing through to an OEM's stock story, a Graph-RAG system provides substantially better source material than a vector-only retrieval pipeline.

The main engineering investment is in the knowledge graph construction and update pipeline. The study's 255-article, 10-stock graph was built manually, but production use requires automated ingestion and continuous updating. That is the primary build cost to estimate when evaluating this architecture.

Realistic KPIs for a pilot deployment: analyst time-to-draft reduction for a sector coverage report, or a coverage breadth score tracking how many directly and indirectly related companies the system's context window reached when answering a given query.

The right starting point is not a high-frequency trading desk but a research team operating on daily cycles — sell-side sector analysts, institutional investor research groups. Sufficient latency tolerance, sufficient query complexity.

---

## Sentiment does not stop at the company boundary

What I find interesting about this research from an affective AI perspective is that it treats financial sentiment not as a property of individual documents but as something that propagates through a network of relationships.

That framing matches how emotional signals actually work. The emotional valence attached to one entity spreads through its connections to adjacent entities, and understanding that propagation requires the structural knowledge the graph provides.

The application domain here is financial text, but the underlying principle — sentiment as a relational, propagating phenomenon rather than an isolated label — is relevant across much of affective AI.

That's it for today!

---

## Reference

1. Rajan Bastakoti, Sagar Bhetwal, Nirajan Acharya, Gaurav Kumar Gupta (2026). *Graph-Augmented Retrieval for Cross-Entity Financial Sentiment Analysis: A Comparative Study*. arXiv preprint.

<p class="ai-notice"><small>* This article was written in part with AI assistance and may contain inaccuracies.</small></p>
