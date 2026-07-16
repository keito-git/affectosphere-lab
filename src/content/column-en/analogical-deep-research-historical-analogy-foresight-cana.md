---
title: "\"It's Just Like Last Time\" Is a Dangerous Move — How CANA Brings Causal Rigor to AI-Assisted Historical Analogy"
date: "2026-07-16"
excerpt: "LLMs draw historical analogies by surface feature matching — missing whether the underlying causal mechanisms actually match. A new framework, CANA (Causal Analogical Researcher), integrates causal mechanism alignment and multi-analogy cross-verification, achieving up to 10% improvement on the newly proposed ADR-bench. Here is why this matters for strategic decision-making in business."
image: "/column-images/analogical-deep-research-historical-analogy-foresight-cana.png"
imageAlt: "An illustration showing historical events and a modern business scenario connected by arrows, with surface similarity on one side and causal structure alignment on the other"
readingMinutes: 5
basedOnPaper: "Analogical Deep Research: Retrieving and Integrating Historical Analogies for Foresight Analysis"
basedOnPaperUrl: "https://arxiv.org/abs/2607.13602"
---

Hello. This is Miura from Affectosphere Group.

"This looks just like the dot-com bubble." "It is basically the same story as when Netflix took down Blockbuster." Historical analogies like these are a staple of strategy meetings and executive decision-making.

They are also one of the most powerful — and most dangerous — tools in the strategic thinking toolkit.

The power is real: identifying a structurally similar historical situation gives you a rich evidence base for reasoning about the present. The danger is equally real: "looks similar on the surface" and "works the same way underneath" are very different things.

A study published on arXiv in July 2026 by Yongqiang Chen, Guangyi Chen, Yuewen Sun, and Kun Zhang (arXiv:2607.13602) addresses this problem directly. The researchers define a new AI task called ADR (Analogical Deep Research) — retrieving and integrating historical analogies for foresight analysis — build the first benchmark for it (ADR-bench), demonstrate that current LLMs fail by relying on surface feature matching rather than causal mechanism alignment, and propose CANA (Causal Analogical Researcher) as a solution.

---

## Three takeaways for today

1. Current LLMs draw historical analogies based on surface similarity — whether descriptions match — rather than whether the underlying causal mechanisms are aligned. This produces analogies that look persuasive but may be structurally wrong.
2. CANA incorporates causal mechanism alignment and multi-analogy cross-verification, achieving up to 10% improvement on ADR-bench. Its effectiveness is also confirmed in business case studies involving market entry and regulatory response.
3. Surface analogy poses the greatest risk in high-stakes, unprecedented decisions: M&A, new market entry, crisis scenarios. Adding causal mechanism alignment as an explicit screening criterion is the key to making AI-assisted strategic analysis trustworthy.

---

## ① The value of AI-assisted historical analogy for strategy

Start with the genuine value proposition.

Historical analogy has always been an important tool in strategic reasoning precisely because it works in situations where direct data is thin or unavailable. When a company faces a genuinely novel situation — entering a market with no clear precedent, responding to a competitor's unprecedented move, navigating a sudden regulatory shift — historical pattern matching is one of the few structured approaches available.

The problem is that doing this well is expensive. Finding relevant historical cases across diverse domains, evaluating the quality of each analogy, comparing multiple cases, and synthesizing a coherent forward-looking conclusion is the kind of work that consulting firms and think tanks do over weeks. Most organizations cannot afford that process for every decision.

If AI can automate the retrieval and evaluation of historical analogies at scale, it significantly reduces the cost of this kind of reasoning. The vision is a system that can respond to "we are considering entering this market — what historical cases of similar market entry attempts are most relevant, and what do they suggest about our situation?" in near-real time.

The ADR task defined in this research is exactly that: given a current problem, retrieve relevant historical analogies and integrate them to support foresight analysis. Paired with the newly constructed ADR-bench, this creates the first formal research infrastructure for measuring and improving AI performance on this kind of strategic reasoning task.

---

## ② Why surface analogy is a business risk, not just an academic problem

This is where the research gets interesting for practitioners.

The study found that current LLMs approach analogy through surface feature matching. They look for historical events or situations whose descriptions share vocabulary, labels, and surface-level patterns with the query. What they do not systematically evaluate is whether the causal mechanism — the sequence of factors that actually produced the outcome — matches the structure of the current problem.

Consider a concrete strategic example.

Suppose a company asks an AI assistant to identify historical analogies for a platform business attempting to enter a two-sided market in a new geography. A surface-matching system might return a list that includes Airbnb, Uber, and several other well-known platform successes. On the surface, this looks useful.

But Airbnb's expansion succeeded in part because of a specific confluence of conditions: a regulatory gap that had not yet been closed, behavioral changes enabled by smartphone adoption, and a cultural readiness for peer-to-peer transactions in its target markets. If none of those conditions exist in the market your company is entering, the Airbnb analogy is not just unhelpful — it is actively misleading. It provides a high-profile success story that feels applicable but whose underlying mechanism does not transfer.

The researchers call this the failure to distinguish structural (causal) alignment from surface alignment. An LLM that matches on surface features may confidently present an analogy that "looks right" while missing the causal mismatch entirely.

This failure mode is most dangerous in exactly the situations where strategic analogy is most needed: unprecedented decisions with high stakes and long lead times for correction. M&A diligence, new market entry, crisis scenario planning, regulatory strategy. In each of these, a convincing but causally mismatched analogy can produce worse outcomes than having no analogy at all — because it creates false confidence.

---

## ③ CANA's design principles and how to apply them

The CANA framework (Causal Analogical Researcher) proposed in this research addresses the problem through two core design principles.

The first is causal mechanism alignment. When evaluating whether a historical case is analogous to the current problem, CANA explicitly asks whether the causal structure — the sequence of factors that drove the historical outcome — is present in the current situation. Surface similarity is not sufficient; the mechanism must match.

The second is multi-analogy cross-verification. Rather than relying on a single historical case, CANA retrieves multiple candidate analogies and checks them against each other. Patterns that appear across multiple structurally similar cases are more likely to reflect genuine causal regularities than coincidental surface matches.

Together, these two principles produced up to 10% improvement on ADR-bench. The paper also reports positive results from case studies involving market entry and regulatory response — business scenarios representative of the contexts where analogy-based reasoning is most practically valuable.

For organizations evaluating or building AI-assisted strategic analysis tools, these design principles translate directly into procurement and QA criteria.

When evaluating an AI tool that presents historical analogies, ask: does this system explain why the analogy applies, in causal terms? Can it distinguish between "this historical case looks like our situation" and "this historical case worked via mechanisms that are actually present in our situation"? A system that can only do the former is a surface matcher. A system that can do the latter is meaningfully more useful.

When designing prompts for current-generation LLMs in strategic contexts, adding an explicit causal reasoning step makes a significant difference. Rather than asking "what historical cases are similar to our situation?", ask "what historical cases are similar to our situation, and for each one, explain the causal chain that produced the outcome and whether those causal factors are present in our situation." This prompt structure pushes the model toward more rigorous analogy evaluation even with systems that are not purpose-built for causal alignment.

For M&A due diligence and crisis scenario planning specifically, introducing causal mechanism alignment as an explicit screening criterion — "before accepting this historical case as an analogy, confirm that its causal drivers are present" — can significantly improve the quality of the analogy-based reasoning that feeds into decision documents.

---

## What this means for AI-assisted strategy

The ADR task and the CANA framework represent an important conceptual contribution to how we think about AI in strategic decision support.

Most of the conversation around AI in strategy consulting has focused on information retrieval speed and breadth: AI can search more documents, summarize more cases, and produce more options faster than human researchers. That is real value, but it does not address the quality of the reasoning that connects historical cases to current decisions.

This research argues — and demonstrates — that the quality of analogical reasoning depends critically on causal alignment, and that current AI systems systematically underperform on this dimension. Improving it requires explicit architectural choices, not just more data or a bigger model.

For organizations deploying AI in strategy, consulting, and executive decision support, this suggests a near-term practical agenda: audit your current AI tools for whether they support causal reasoning in analogy, design your prompts to explicitly request causal justification for historical cases, and build QA processes that check whether the causal conditions of cited analogies actually hold in your context.

The companies that figure this out first will use AI-assisted historical analogy as a genuine strategic advantage rather than a source of sophisticated-sounding but unreliable recommendations.

See you next time!

---

## References

1. Yongqiang Chen, Guangyi Chen, Yuewen Sun, Kun Zhang (2026). *Analogical Deep Research: Retrieving and Integrating Historical Analogies for Foresight Analysis*. arXiv preprint. https://arxiv.org/abs/2607.13602

<p class="ai-notice"><small>* This article was written in part with AI assistance and may contain inaccuracies.</small></p>
