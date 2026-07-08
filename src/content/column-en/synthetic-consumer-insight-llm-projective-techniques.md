---
title: "Can LLMs Serve as the Opening Act for Consumer Research? Projective Techniques, Synthetic Data, and What It Means for the Field"
date: "2026-07-08"
excerpt: "Can LLMs replace human respondents in projective techniques — the qualitative methods that surface consumers' hidden associations, emotions, and desires? A new study comparing LLM-generated and human responses across multiple models, prompting strategies, and temperature settings offers a nuanced answer."
image: "/column-images/synthetic-consumer-insight-llm-projective-techniques.png"
imageAlt: "A marketing researcher inputs a projective technique prompt into an LLM on a laptop screen, while a split panel on the right shows human response cards alongside AI-generated responses, with large overlap in broad themes but visible structural and stylistic differences"
readingMinutes: 5
basedOnPaper: "Synthetic Consumer Insight Generation with Large Language Models"
basedOnPaperUrl: "https://arxiv.org/abs/2607.05761"
---

Hello. I am Miura from Affectosphere Group.

If you've ever run consumer research, you know the drill.

Recruit participants. Book a venue. Hire a moderator. Run a focus group. Wait weeks for the analysis. Pay for all of it — and end up with insights from a few dozen people.

The desire to shortcut this process is entirely understandable. And with large language models becoming capable of generating human-like text at scale, an obvious question has emerged: could we use LLMs to generate synthetic consumer responses instead?

It sounds appealing. But there's a subtler version of the question that matters more: can LLMs actually replicate what happens in projective techniques — the qualitative methods specifically designed to surface what consumers won't or can't say in response to direct questions?

A study published on arXiv (France & Albinsson, arXiv:2607.05761) takes this question seriously. The researchers tested multiple LLM models, prompting strategies, and temperature settings to generate synthetic consumer responses to projective technique prompts, then compared those responses directly with primary human data collected in a study on urban tourism destination perceptions.

The findings are instructive — and the framing they land on has real implications for how marketing research teams should think about where LLMs fit.

---

## Three Things Worth Taking Away

1. LLMs can generate projective technique responses, and broad topical overlap with human responses is substantial. But meaningful stylistic and structural differences remain.
2. Model choice, prompting strategy, and temperature setting all affect synthetic data quality — and the study provides guidance on what that means in practice.
3. The core framing the research offers: LLMs are not a replacement for consumer research, but a useful hypothesis-generation tool for the front end of the research process.

---

## What Makes Projective Techniques Different

Before getting into the findings, it's worth being precise about what projective techniques are and why they're hard to replicate.

Standard survey and interview methods have a well-known limitation: when you ask consumers direct questions about their attitudes, you often get socially desirable answers, conscious evaluations, or post-hoc rationalizations — not the underlying emotions and associations that actually drive behavior.

Projective techniques get around this by using indirect stimuli. Instead of asking "What do you think of this city as a travel destination?", you might ask: "If this city were a person, what kind of person would it be?" Or: "What color does this city make you think of?" Or: "What animal comes to mind?"

The indirectness is the point. By creating some distance from the direct evaluation, you can surface associations, feelings, and needs that the consumer hasn't consciously articulated — which is where a lot of the most actionable insight lives.

These techniques have long been used in brand perception research, UX studies, and consumer insight work. But they're expensive to run at scale. Recruiting participants, facilitating sessions, and coding qualitative responses takes time and money that many research teams don't have for every project.

This is what makes the idea of LLM-generated synthetic responses attractive. If you could get comparable results from an LLM for a fraction of the cost, the implications for research design would be significant.

---

## What the Study Did

The research used urban tourism destination perception as the primary domain. Researchers collected actual human participant data through projective technique prompts, then generated synthetic responses from multiple LLMs using different prompting strategies and temperature settings, and compared the two.

The comparison wasn't just a qualitative read — it was a systematic analysis of where LLM responses converged with and diverged from human responses across dimensions like topical coverage, associative patterns, language style, and structural characteristics.

This design gives the research a practical character. Instead of asking the abstract question of whether LLMs "understand" consumer psychology, it asks the more useful question: when you sit down to run a projective technique study, what would you actually get if you used LLMs to generate responses?

---

## Where LLMs Do Well: Broad Topical Coverage

The first main finding is encouraging in a bounded way.

On the dimension of broad topical coverage and associative patterns, LLM-generated responses showed substantial overlap with human responses. When asked projective questions about an urban tourism destination, LLMs and human participants tended to surface similar themes and categories of association.

This matters because it tells us something about where LLMs can actually contribute. If you're trying to map the landscape of possible associations — to understand the territory of what people might think and feel about a destination or brand — LLMs can generate a usable draft of that map.

For hypothesis generation, brainstorming, and initial scoping of a research project, that overlap is meaningful. You can use LLMs to surface the broad thematic space before you invest in recruiting human participants to explore it in depth.

---

## Where the Differences Show Up: Style and Structure

But the research doesn't stop there, and the second finding is equally important.

In terms of style and structure, meaningful differences between LLM-generated and human responses exist.

Human responses tend to be grounded in personal memory, emotional texture, and culturally specific context. They're idiosyncratic in ways that reflect real experience. The way a person describes their associations with a city often carries traces of a specific visit, a memory of a restaurant, a feeling about a neighborhood at a particular time of day.

LLM responses tend to be more systematic, more comprehensive, and — for lack of a better word — more textbook-like. They cover the conceptual ground efficiently, but they don't carry the same embedded particularity.

The topical content overlaps; the voice and structure differ.

For many research purposes, this distinction matters a great deal. If you're trying to understand what vocabulary and associations consumers use when they talk about a destination — the emotional and linguistic texture of their experience — LLM responses may not capture it. If you're trying to map what themes are likely to come up, they might get you most of the way there.

---

## Model and Prompt Choices Are Not Interchangeable

The study's third contribution is practical guidance on the variable inputs.

Different LLM models, different prompting strategies, and different temperature settings produce meaningfully different synthetic data. Higher temperature settings increase response variability but may affect the alignment with human response patterns in ways that matter for specific use cases. Prompting strategy shapes vocabulary, structure, and the range of associations generated.

The implication is that treating LLM-generated synthetic data as a commodity — "just use whatever model is available" — is a mistake. The quality and character of the synthetic data you get depends on deliberate choices about setup, and those choices should be made in light of what you're trying to learn.

The research provides guidance on these choices. That guidance is the practical layer that makes the findings useful rather than just informative.

---

## How to Apply This: The Hybrid Research Design

So what does this mean for a marketing research team, a CMO's office, or a brand manager thinking about where LLMs fit in the research workflow?

The framing the research lands on is the most useful thing to take away: LLMs as a front-end hypothesis-generation tool, not a replacement for human research.

Here's what a hybrid research design might look like in practice.

Phase 1: Use LLM-generated synthetic responses to projective technique prompts to map the broad thematic space — the range of associations, emotions, and framings that are likely to come up in human research. This phase is fast and cheap.

Phase 2: Use that map to design more targeted human research. Instead of asking open-ended projective questions and waiting to see what comes up, you go in with specific hypotheses about which associations matter and which framings resonate. You run smaller focus groups or targeted surveys to test and refine those hypotheses.

The practical effect is that the expensive, time-consuming parts of the research process — recruiting human participants, running facilitated sessions, coding qualitative data — become more focused and efficient because you've already scoped the landscape before you start.

For teams under pressure to deliver faster and cheaper, this is a meaningful workflow change. The total cost and timeline for the research project can be substantially reduced without abandoning the primacy of human response data for final conclusions.

For tourism and hospitality brands specifically — given the research domain — the application is direct. Destination marketing organizations, urban tourism boards, and hospitality brands can use LLM-generated projective data to inform preliminary brand perception hypotheses before investing in visitor surveys or ethnographic research.

---

## What to Watch Out For

One important caveat follows directly from the findings.

The stylistic and structural differences between LLM and human responses are not bugs to be engineered away — they're features of what LLMs are. LLMs generate language based on patterns in training data, not personal experience. In projective techniques, where the goal is often to surface the emotionally and culturally specific texture of consumer experience, that distinction carries weight.

Using LLM-generated synthetic data to draw final conclusions about consumer psychology — without validating against actual human responses — risks systematically missing what's most distinctive and actionable about real consumer insight.

The research is clear about this. The limits it identifies are real, and the positioning of LLMs as hypothesis-generation tools rather than replacements is not a hedge — it's a genuine constraint that follows from what the comparison showed.

---

## Conclusion

This study on arXiv offers one of the more practically grounded assessments of where LLM-generated synthetic consumer data stands today.

The headline finding — substantial topical overlap with human responses, alongside meaningful stylistic and structural differences — gives research teams something they can actually work with. It's not a blanket endorsement of synthetic data, and it's not a dismissal. It's a calibrated map of where LLMs can contribute and where they can't.

The hybrid research design framework — LLMs for hypothesis generation at the front end, human research for validation and depth — is the model worth experimenting with. For teams doing brand perception work, UX research, or consumer insight at scale, this positioning gives LLMs a genuine and useful role without overstating what they can do.

The question isn't whether to use LLMs in consumer research. It's how to fit them into a research process in a way that actually improves the output. This study offers a starting point for that conversation.

---

## Reference

1. France, Stephen L. & Albinsson, Pia A. (2026). *Synthetic Consumer Insight Generation with Large Language Models*. arXiv preprint. https://arxiv.org/abs/2607.05761

<p class="ai-notice"><small>* This article was written in part with AI assistance and may contain inaccuracies.</small></p>
