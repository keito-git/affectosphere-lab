---
title: "Automating KPI Extraction from Annual Reports — What LEDGER Tells IR and Finance Teams"
date: "2026-06-14"
excerpt: "LEDGER is a large-scale benchmark of approximately 5,000 corporate annual reports, annotated with 31 KPIs linked to market reactions at earnings disclosure. It reveals where LLMs fall short on dense financial documents — and provides a precise map for designing workflows where human review fills the gaps."
image: "/column-images/ledger-benchmark-corporate-annual-report-financial-extraction.png"
imageAlt: "Corporate annual report pages connected by lines to extracted KPI values, representing automated financial data extraction"
readingMinutes: 5
basedOnPaper: "LEDGER: A Long-Context Benchmark of Corporate Annual Reports for Grounded Financial Retrieval and Extraction"
basedOnPaperUrl: "https://arxiv.org/abs/2606.13100"
---

Hi, I'm Keito Inoshita from Affectosphere Group.

Here's a scenario most finance and IR professionals have tried at least once: paste an annual report PDF into a chat interface and ask it to pull out revenue, EBITDA, and EPS.

Something comes back. It looks plausible. But is it right? Can you cite the source page? Can you repeat this for fifty companies and get consistent results? When you push past surface-level use, the limitations of current LLMs on dense financial documents come into focus fast.

A 2026 paper by Charles Moslonka, Amaury de Vitry, Arthur Garnier, Hicham Randrianarivo, and Emmanuel Malherbe (arXiv:2606.13100) addresses this systematically. LEDGER is a benchmark built specifically to measure how well LLMs handle KPI extraction from corporate annual reports — at scale, with grounding requirements, and with annotation that connects KPIs to actual market reactions at earnings disclosure.

---

## 3 Points for Today

1. LEDGER is the first large-scale benchmark for evaluating LLM performance on KPI extraction from corporate annual reports — covering approximately 5,000 reports and 31 KPIs linked to market reactions.
2. Its three evaluation tasks directly model what IR teams, finance departments, and analysts actually do with these documents: page-level KPI retrieval, interactive numerical reference, and long-context KPI extraction.
3. The benchmark surfaces where current LLMs break down on financial text — dense numerical content, multi-page cross-references, table structure recovery — giving practitioners a clear map for designing human-in-the-loop workflows.

---

## ① What LEDGER Is and Why the Design Matters

Annual reports are hard documents. A large-cap company's annual report can run to two hundred pages: financial statements, MD&A, segment-by-segment breakdowns, footnotes referencing other footnotes, and dense tables where rows and columns carry structured meaning that OCR doesn't always preserve cleanly.

LEDGER's dataset covers approximately 5,000 of these documents, annotated with 31 key performance indicators — revenue, operating income, EPS, debt ratios, and others — linked to market reaction data at the point of earnings disclosure. The market linkage is not decorative: it means the benchmark can distinguish between KPIs that markets treated as signal versus those that passed without reaction.

The OCR quality annotations are also significant for practitioners. A recurring practical problem with financial document processing is that failures are hard to attribute. When an LLM gives the wrong number, was it because OCR mangled the source text, or because the model misread a correctly transcribed table? LEDGER's quality annotations let researchers and practitioners separate these failure modes — which changes how you design your remediation.

---

## ② Three Tasks That Mirror Real Workflows

The three evaluation tasks in LEDGER weren't designed abstractly. They model what finance professionals actually do with annual reports.

The first task is page-level KPI retrieval: given a KPI and a document, identify the page where it appears. In practice, this is the "find me where the revenue figure is disclosed" query. Getting this right with citation matters for compliance and audit trail purposes — you can't just surface a number, you need to point to where it came from.

The second task is interactive numerical reference: extract a specific figure from a document with a source citation. This is closer to the analyst workflow — "give me the 2023 EBITDA and tell me where you found it." The grounding requirement makes this task directly sensitive to hallucination: fabricating a number with a wrong or invented page reference is a failure mode that surfaces immediately.

The third task is long-context KPI extraction: extract all instances of a given financial metric across a full document. This models the IR team's cross-company aggregation work — "pull every segment-level operating profit figure from this report." It's the task most exposed to the long-context limitations of current LLMs, where information in the second half of a two-hundred-page document can fall out of effective context.

---

## ③ Where LLMs Break Down on Financial Documents

The benchmark findings point to specific failure patterns that practitioners need to know.

Numerical density is the first challenge. Financial documents pack numbers close together. Revenue, operating income, net income, and EBITDA may appear within lines of each other in the same table. When LLMs encounter this density, they can misattribute numbers to the wrong metric — especially when table structure was imperfectly recovered by OCR and the row-column alignment that humans read visually isn't preserved in the text representation.

Multi-location cross-referencing is the second. Annual reports routinely defer detail to footnotes. "See Note 14 for a breakdown of revenue by segment" means the model needs to follow that reference, find Note 14 across potentially many pages, extract the relevant figures, and integrate them back with the main text. This kind of multi-hop retrieval is a documented weak point for current LLMs.

Long-context degradation is the third. Documents over a hundred pages stress LLM context windows. Information near the end of a very long document is less reliably processed than information at the beginning. For companies with extensive annual reports, this creates a systematic bias toward under-extracting information from later sections.

Knowing these three failure modes is the starting point for designing workflows that work.

---

## ④ Practical Applications for IR Teams and Finance Departments

The research findings translate directly into workflow design. Here's a concrete application.

One of the most time-consuming tasks in competitive intelligence work is extracting financial metrics from peer company annual reports. An IR team tracking fifteen to twenty comparable companies through earnings season does this repeatedly — pulling revenue, margin figures, and guidance language from each company's filings and aggregating them into a comparison table. This is currently done mostly by hand.

A semi-automated pipeline built on LEDGER's task design would look like this:

1. Ingest PDFs and flag documents with low OCR quality scores for additional preprocessing.
2. Run page-level KPI retrieval to identify which pages contain each target metric.
3. Run interactive numerical reference to extract KPI values with source page citations.
4. Route flagged outputs — anything from tables, footnote references, or documents with OCR issues — to human review before finalizing.

In this design, steps 1 through 3 are handled by the LLM; step 4 is human. The LEDGER findings tell you exactly what to route to step 4: table-sourced values, footnote-referenced figures, and information extracted from late pages in long documents. That's not guesswork — it's precision about where the LLM is most likely to err.

For finance departments and audit firms, the application is evaluation before deployment. Before adopting a vendor LLM tool for financial document processing, run an internal benchmark modeled on LEDGER's three tasks against a representative sample of your actual documents. That tells you where the tool is reliable and where it needs human oversight — a much better basis for deployment decisions than vendor-provided accuracy metrics on generic text.

---

## ⑤ CEO Communication and Market Reaction Analysis

LEDGER's market linkage opens a second line of application that goes beyond KPI extraction.

Annual reports contain qualitative text: CEO letters, management discussion and analysis, forward-looking statements. LEDGER connects these texts to market reactions at earnings disclosure. That connection enables analysis of what in CEO communication predicts market response — tone, language about uncertainty, forward guidance specificity, references to particular business lines.

For analysts, this is the foundation of pre-earnings tone analysis. If patterns emerge in how market-moving disclosures are written versus how non-moving disclosures are written, those patterns can be incorporated into earnings monitoring workflows.

For IR teams, the application runs in the opposite direction. Analyzing how your own CEO letters read against the patterns associated with positive or neutral market reception — using LEDGER's structure as a reference frame — is an input to optimizing disclosure communication. Not gaming the market, but understanding how language choices land with sophisticated readers.

---

## Use What's Available Now, Calibrated to Its Actual Limits

LEDGER's contribution isn't to declare that LLMs are ready for financial document processing. It's to characterize exactly where they are ready and where they aren't.

Dense tables, multi-page cross-references, long-document context degradation — these are the known weak points. Design around them with targeted human review, and the LLM handles the high-volume retrieval work that would otherwise consume analyst hours. Ignore them, and errors propagate into the numbers that decisions get made on.

The map is here. The practical question for IR teams and finance departments is how to use it.

That's all for today!

---

## References

1. Charles Moslonka, Amaury de Vitry, Arthur Garnier, Hicham Randrianarivo, Emmanuel Malherbe (2026). *LEDGER: A Long-Context Benchmark of Corporate Annual Reports for Grounded Financial Retrieval and Extraction*. arXiv preprint arXiv:2606.13100.

<p class="ai-notice"><small>* This article was written in part with AI assistance and may contain inaccuracies.</small></p>
