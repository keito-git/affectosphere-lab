---
title: "Why Personalizing for New Users Is So Hard — And How an LLM Solved the Long-Tail Problem"
date: "2026-06-19"
excerpt: "Personalization for users with sparse behavioral data has always been the blind spot of collaborative filtering. ProfiLLM, an LLM-based user profiling system deployed on the DiDi platform, improved AUC by up to 6.14% and lifted online GMV by +0.47%. Here is what it means for e-commerce, finance, and delivery platforms."
image: "/column-images/profillm-agentic-user-profiling-ride-hailing-dispatch.png"
imageAlt: "A city map with user icons and a personalized recommendation network overlay"
readingMinutes: 5
basedOnPaper: "ProfiLLM: Utility-Aligned Agentic User Profiling for Industrial Ride-Hailing Dispatch"
basedOnPaperUrl: "https://arxiv.org/abs/2606.18803"
---

Hello — this is Inoshita from Affectosphere Group.

"How do we personalize for users we don't know yet?"

That question sits at the center of every platform business.
Collaborative filtering works well once a user has accumulated history.
But new users, or users who visit once a month, have almost no behavioral data.
There is no similar-user cluster to fall back on.

This is the cold-start problem.
It is also the long-tail user problem.

A research team at DiDi tackled this head-on and published a solution on arXiv:
ProfiLLM, an LLM-based agentic user profiling system for industrial ride-hailing dispatch.

Today I want to explain what they built — and what the architecture means for e-commerce, financial services, and delivery platforms.

---

## Three takeaways

1. LLMs can generate semantically rich user profiles even from sparse behavioral logs
2. ProfiLLM improved AUC by up to 6.14% and achieved GMV +0.47% in an online A/B test
3. The architecture is transferable to e-commerce, fintech, and food delivery contexts

---

## The three walls ProfiLLM had to break through

Tengfei Lyu, Zirui Yuan, Xu Liu, and their co-authors designed ProfiLLM to solve not one but three simultaneous constraints.

The first constraint was the context window limit.
Ride-hailing platforms accumulate vast behavioral logs.
But the number of tokens you can feed an LLM in a single call is capped.
You cannot pass years of trip history all at once.

The second constraint was sparse interaction data.
New users or infrequent riders may have only a handful of trips.
Building a reliable profile from five data points is a fundamentally different challenge than building one from five hundred.

The third constraint was prediction utility.
A semantically rich profile that does not actually improve dispatch accuracy is worthless in production.
"Accurate description" and "useful for downstream prediction" are separate objectives that must both be satisfied.

ProfiLLM addresses all three through a two-component design.

The first component is tool-augmented knowledge mining, integrating 27 analytics tools.
Rather than feeding raw logs to the LLM, the system uses these tools to extract semantically meaningful signals from the behavioral data — working around the context window limit through intelligent selection and summarization.

The second component is utility-aligned profile exploration with candidate evaluation.
After generating profile candidates, the system evaluates each one against the downstream prediction task and keeps only the profiles that improve actual prediction performance.
This closes the gap between semantic richness and practical utility.

---

## Results in numbers

The reported results are concrete.

AUC improved by up to 6.14%.
Simulation experiments showed GMV improvement of up to 4.35%.
An online A/B test achieved GMV +0.47%.

The critical finding for practitioners is the long-tail result:
the system maintained accuracy even for users with minimal behavioral history.

This is the biggest gap from traditional collaborative filtering.
When behavioral data is thin, collaborative filtering performance degrades sharply.
LLM-based profiling compensates through semantic inference — reasoning about what a sparse history implies, rather than relying solely on statistical patterns.

---

## Business applications — which industries can transfer this?

ProfiLLM was implemented for ride-hailing dispatch.
But the architectural principles are general.

### E-commerce platforms

Recommendations for new members immediately after sign-up are a known failure point for collaborative filtering.
With near-zero behavioral data, an LLM can instead read registration details, early browsing behavior, and search terms to construct a semantic profile.

The relevant KPIs here are: CVR (conversion rate) in the first seven days post-registration, and time-to-first-purchase.
Lifting these numbers for new-user cohorts directly improves CAC payback period.

### Financial services and fintech

Thin-file customers — young adults or new customers with limited credit history — are exactly the long-tail problem in a different domain.
An LLM trained to read transaction patterns, transfer behavior, and app usage could generate semantic profiles that enable personalized offers beyond what traditional credit scoring can reach.

### Delivery and food tech

A user who orders once or twice a month has sparse behavioral data by definition.
If an LLM can infer from past order content, timing, and contextual signals when that user is likely to order again, the result is more precisely timed push notifications and better content targeting.

For long-tail users, a modest improvement in order frequency creates outsized revenue impact — because there are many such users.

---

## Notes for MLOps and data science teams

For teams evaluating whether to build something like this, a few structural observations.

The 27-tool integration is a statement about modularity.
The system does not ingest raw logs into the LLM directly.
It routes specific analytical queries to specific tools.
This maps cleanly onto existing data pipelines — you connect existing analytics as tool calls rather than rebuilding from scratch.

The separation between profile generation and utility evaluation is also notable.
This two-phase design is consistent with standard MLOps principles of separating feature generation from model evaluation.
It should be possible to integrate into existing ML pipelines without requiring a complete rebuild.

KPIs that are measurable in a production deployment:
recommendation CTR for long-tail user segments (e.g., fewer than 5 behavioral events);
time from onboarding to first transaction;
GMV change rate by user segment.

---

## Implementation cautions

Two things to verify before building anything similar.

First, inference cost.
A system integrating 27 tools and generating profiles via LLM calls is not cheap at scale.
For large user bases, separating batch profile generation (for known users) from real-time generation (for truly new users) is likely necessary for cost control.

Second, privacy architecture.
Passing behavioral logs to an LLM requires clear decisions about anonymization and data minimization.
Compliance with GDPR, local data protection law, and platform privacy policies must be designed in from the start — not added later.
Specifically, the decision about which granularity of behavioral data enters the LLM call needs to be documented and reviewed.

---

## Closing

What ProfiLLM demonstrates is a concrete methodology for a problem that has resisted solution for years:
how to personalize for users who have not yet generated enough data to personalize from.

The system validated in ride-hailing dispatch carries a design philosophy that data science teams in e-commerce, fintech, and delivery can map onto their own use cases.

If long-tail user monetization is a live challenge for your platform,
the ProfiLLM architecture is worth evaluating against your own data environment.

---

## References

Tengfei Lyu, Zirui Yuan, Xu Liu, Kai Wan, Zihao Lu, Li Ma, Hao Liu (2026). *ProfiLLM: Utility-Aligned Agentic User Profiling for Industrial Ride-Hailing Dispatch*. arXiv:2606.18803.

<p class="ai-notice"><small>* This article was written in part with AI assistance and may contain inaccuracies.</small></p>
