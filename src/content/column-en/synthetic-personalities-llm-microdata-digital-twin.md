---
title: "Can an LLM Reproduce Your Customer? What Synthetic Personalities Mean for Market Research"
date: "2026-06-21"
excerpt: "A study feeding individual response histories into LLMs achieved 78.8% accuracy in mimicking real survey respondents. With over 2.1 million synthetic responses analyzed, the findings point toward a concrete shift in how consumer insight work gets done."
image: "/column-images/synthetic-personalities-llm-microdata-digital-twin.png"
imageAlt: "A flat illustration showing silhouettes of individuals standing alongside semi-transparent digital twins, with data flowing between them"
readingMinutes: 5
basedOnPaper: "Synthetic Personalities: How Well Can LLMs Mimic Individual Respondents Using Socio-Economic Microdata?"
basedOnPaperUrl: "https://arxiv.org/abs/2606.04592"
---

Hello. This is Keito Inoshita from Affectosphere Group.

"Will this product resonate with our target audience?"

It is the question every marketer most wants answered — and the hardest one to answer well. Designing a survey, recruiting respondents, collecting and cleaning data can take weeks and cost significant budget, even before analysis begins.

What if the customer data you already have could tell you how those same people would respond to new questions?

A study published on arXiv in June 2026 (Leonard Kinzinger, Jochen Hartmann; arXiv:2606.04592) attacks this problem directly. Using individual-level data from the German Socio-Economic Panel (SOEP), the researchers built personal-level digital twins with LLMs and conducted a rigorous evaluation of how accurately these synthetic personalities replicate real respondents.

The results were more interesting than expected.

---

## Three takeaways for today

1. Fed with individual response histories, LLMs can replicate real-person answers at 78.8% accuracy and Fisher-z correlation r=0.590.
2. Feeding raw conversation histories directly outperforms text summaries across all models tested.
3. The binding constraint on synthetic market research is not survey design — it is the amount of individual-level data you hold, the model you choose, and how you build the twin.

---

## ① What 2.1 million responses revealed

The scale of this study is worth noting first.

The SOEP is a longitudinal survey spanning decades of individual-level data on lifestyle, attitudes, and behavior. The researchers used this data to construct personal digital twins and ran an experiment combining three LLMs, five levels of information depth, two embedding approaches, and two inference modes.

The result: over 2.1 million synthetic responses. No prior study had evaluated LLM mimicry of individual respondents at anything close to this scale.

The best conditions produced 78.8% accuracy and a Fisher-z correlation of r=0.590. Not perfect — but firmly within the range that makes the approach worth taking seriously for applied work.

Why does this matter? Because mimicking an individual is fundamentally different from surveying a segment. The conventional insight question is: how does the average 40-something female consumer feel about this? The synthetic personality question is: how would this specific person respond? That shift in granularity is what makes the technology interesting.

---

## ② More information helps — up to a point

The relationship between input depth and mimicry accuracy follows an intuitive pattern, with an important qualification.

Providing only demographic basics — age, gender, occupation — produces lower accuracy than providing detailed response histories. The study operationalized this as five levels of information depth and confirmed that accuracy improves as depth increases.

But the gain is not linear indefinitely. Accuracy improvements taper off above the 75th percentile of information depth. After a certain threshold, adding more data yields diminishing returns.

For market research practitioners, this has a practical implication. There is a point of sufficient data beyond which additional investment in data enrichment does not meaningfully improve synthetic personality performance. Knowing where that threshold lies allows for much more targeted ROI calculations when evaluating data collection investments.

---

## ③ Raw histories beat summaries — across every model

This is one of the most operationally useful findings in the study.

Two approaches to embedding conversation histories were compared. The first was text summarization: condensing a person's response history into a summary before passing it to the LLM. The second was direct injection: feeding the raw history straight into the prompt.

The result was consistent across all models tested. Direct injection of conversation histories outperformed text summaries on mimicry accuracy.

The interpretation is that the summarization process loses information. The raw record of how a person answered specific questions at specific moments carries more signal than a generalized characterization of their tendencies.

The practical implication: when building LLM-based customer analysis tools, passing structured raw logs may yield better results than passing cleaned and summarized profiles. This runs counter to the usual data preparation instinct, but the empirical evidence here is clear.

---

## ④ Where the real constraints are

The most important finding from this research may be the reframe it offers on where the limits of synthetic market research actually lie.

The constraint is not survey design.

How you write questions, how you sequence a questionnaire, what scale you use — these are not the bottleneck. The binding constraints are: how much individual-level data you have on each person, which model you use, and how you construct the twin.

This represents a meaningful shift in what market research investment should target.

For decades, a large share of research budget has gone into survey instrument design — developing the questionnaire, testing it, refining it. In the framework this study implies, the more important investment is in the depth and quality of longitudinal customer data. CRM records, purchase histories, support ticket logs, prior survey responses — all of these are raw material for synthetic personalities.

Organizations with rich individual-level data are in a structurally better position to apply this technology than those relying on aggregate segment data alone.

---

## Can synthetic personalities substantially cut research costs?

The clearest appeal of synthetic personalities is cost reduction.

Fielding a consumer survey — designing it, recruiting participants, collecting and analyzing responses — carries substantial cost when done rigorously. If synthetic personalities can substitute for some of that work, the savings could be significant.

But it is important to be clear about where the technology currently stands. The 78.8% accuracy figure is from a specific set of conditions and a specific survey instrument. It does not automatically transfer to all research contexts.

The most realistic near-term use cases are in pre-research phases rather than as direct replacements for primary research.

For early-stage concept screening, synthetic personalities can simulate target respondents before a full study is fielded. If you have three product concepts and want to know which has the most potential, a synthetic simulation can help prioritize which concepts to test more rigorously — and may allow you to reduce the sample size needed in the actual study.

For stimulus pre-screening in A/B testing, the same logic applies. Narrowing down from many variants to a shortlist using synthetic responses before fielding to real panels can substantially reduce the cost of the primary study.

The technology is not ready to replace rigorous primary research. But as a complement that reduces the scale of the primary work needed, it is closer to practical than many assume.

---

## What to do with this today

If you work in marketing research or UX research, there are concrete steps this study points toward.

The first is auditing your individual-level data assets. Synthetic personality accuracy depends on the quantity and quality of per-person data. Mapping what you hold — which customers, what types of records, over what time horizon — clarifies how ready your organization is to use this technology. Purchase histories, support interactions, past survey responses: the richer and more longitudinal, the better.

The second is testing direct raw-log injection in any LLM-based customer analysis you already do. Rather than summarizing customer profiles before passing them to a model, try passing structured raw records and compare results. The evidence from this study suggests the raw approach is likely to outperform.

The third is positioning synthetic personalities as hypothesis-generation tools rather than primary research replacements. At current accuracy levels, they are well-suited to the pre-study phase: generating hypotheses, screening concepts, reducing the scope of the primary research needed. That framing makes the current capability immediately useful without overstating what it can do.

---

## Summary

Can an LLM reproduce a real person's survey responses? The answer is: yes, under the right conditions, and with meaningful accuracy.

78.8% accuracy and r=0.590 correlation are not perfect numbers, but they are close to practical for hypothesis testing and concept screening work.

More importantly, this research clarifies what actually determines that accuracy. It is not how the survey is designed. It is how much you know about the individual, which model you use, and how you build the twin. That shifts the strategic question for market research from "what should we ask?" to "who do we know, and how well?"

---

## References

1. Leonard Kinzinger, Jochen Hartmann (2026). *Synthetic Personalities: How Well Can LLMs Mimic Individual Respondents Using Socio-Economic Microdata?*. arXiv preprint.

<p class="ai-notice"><small>* This article was written in part with AI assistance and may contain inaccuracies.</small></p>
