---
title: "The Workforce Speaks on Social Media — Can LLMs Detect Dangerous Attitude Shifts Before Accidents Happen?"
date: "2026-06-09"
excerpt: "A new study measures construction workers' safety attitudes across eight dimensions by analyzing Reddit posts with an LLM classifier achieving kappa 0.90. The approach opens a path to detecting 'pre-accident attitude deterioration' in real time — a tool safety managers, HR, and ESG teams can start building toward today."
image: "/column-images/workforce-safety-attitude-llm-social-media.png"
imageAlt: "Flat illustration of a construction site silhouette with social media text bubbles and an AI analytics dashboard overlaid"
readingMinutes: 5
basedOnPaper: "Listening to the Workforce: Measuring Construction Worker Safety Attitudes from Social Media Discourse Using LLMs"
basedOnPaperUrl: "https://arxiv.org/abs/2606.04450"
---

> _This article is an English translation of the original Japanese column. Some phrasing has been adapted for English readers._

Hello — this is Inoshita from Affectosphere Group.

I once asked a safety manager at a construction firm something that had been on my mind.

"You run annual safety training, you have a near-miss reporting system in place. Why don't the numbers move?"

The hint came back from an unexpected direction. Reddit.

In communities like r/Construction and r/Roofing, workers post anonymously every day — stories about a close call with a fall, complaints that "that rule is impossible to follow on a real site," arguments about whether a hard hat rule is worth enforcing. It is the unfiltered voice of the workforce. It never shows up on a formal survey.

A study published on arXiv in June 2026 (Farouq Sammour, Yuxin Zhang, Zhenyu Zhang; arXiv:2606.04450) uses LLMs to automatically measure safety attitudes from exactly this kind of social media discourse.

The classifier achieved Cohen's kappa = 0.90 — on par with trained human annotators.

---

## Three takeaways for today

1. CSAF framework: safety attitude is decomposed into eight measurable dimensions, making it possible to identify precisely which aspect is breaking down and where.
2. Classifier reliability: kappa 0.90 on the training community (r/Construction) generalizes to a different trade community (roofing workers) at kappa 0.89.
3. Business application: applying the same approach to internal channels — employee social media, incident reports, anonymous surveys — creates an early-warning system for attitude deterioration before accidents occur.

In order.

---

## 1. The CSAF framework: eight dimensions of safety attitude

The heart of the study is the Construction Safety Attitude Framework (CSAF).

Safety attitude tends to be treated as a single dial — either the workforce has it or they don't. But real sites are more nuanced than that.

Someone who follows the rules only under direct supervision needs a different intervention than someone who genuinely cannot see why the rule matters. Someone whose colleagues mock safety gear needs something different again. CSAF separates these cases.

The eight dimensions are:

1. Principle Integrity: does the worker prioritize safety over productivity, pay, and schedule?
2. Self-Efficacy: does the worker believe they can personally execute safe practices and control safety outcomes?
3. Compliance Orientation: does compliance come from internal conviction, or only when external enforcement is present?
4. Learning Orientation: is the worker open to adapting behavior based on their own accidents or others'?
5. Risk Perception: does the worker see workplace hazards as personally relevant, or dismiss them as exaggerated?
6. Benefit Perception: does the worker believe safety measures genuinely protect them, or see them as inadequate?
7. Social Norms: do colleagues support, obstruct, or remain indifferent to safe behavior?
8. Personal Agency: is the worker willing to intervene when they see unsafe behavior, and to participate in collective safety action?

Each dimension is coded as Favorable, Unfavorable, or Absent. The full codebook has 34 codes. It is designed to be applied without specialist training — a key requirement for operational deployment.

---

## 2. "The 2025 workforce is less safe than 2020" — what the longitudinal data shows

The most striking finding in the study comes from the time-series analysis.

Across 10,346 Reddit posts, the Favorable-to-Unfavorable ratio (F/UF ratio) dropped from 3.43 in 2020 to 1.43 in 2025.

In plain terms: measured across public construction discourse, safety attitudes deteriorated meaningfully over five years.

The four dimensions showing the sharpest decline are Benefit Perception (trust that safety measures actually work), Learning Orientation (willingness to change behavior after incidents), Risk Perception (seeing hazards as personally relevant), and Principle Integrity (prioritizing safety over schedule pressure).

Topic-level analysis adds further texture.

Fall Protection generates the highest volume of posts — it is the most-discussed safety topic in the community. Yet its F/UF ratio fell from 2.65 to 1.45 by 2025. The most talked-about topic is also where attitudes are deteriorating fastest.

Mental Health & Wellbeing is the only topic where unfavorable Social Norms and unfavorable Compliance Orientation converge simultaneously. When workers discuss mental health, peer pressure and external-only compliance both spike. This is a structural problem that conventional safety training is poorly equipped to address.

---

## 3. Business application: building a system that detects attitude shifts before accidents occur

This is the practical part.

The methodology is not limited to construction. Any industry employing a field workforce — manufacturing, logistics, facilities management, utilities — can apply the same approach.

The logic is straightforward.

Text from employee social media, internal chat, incident reports, or anonymous pulse surveys is passed through an LLM classifier. The output is coded against the eight CSAF dimensions. A dashboard tracks F/UF ratios by dimension, team, site, and time period. When a ratio drops sharply, a targeted intervention is triggered: a focused team meeting, a refreshed training module, a site walk with direct observation.

How each function can use this:

For safety management, the eight-dimension dashboard replaces the blunt instrument of an annual safety score. Instead of reacting after a recordable incident, the team acts when a dimension score moves. The trigger is attitude change, not injury.

For HR and labor relations, declining scores on Mental Health & Wellbeing — particularly in the Social Norms dimension — can serve as an early signal for engagement risk and potential attrition. This connects safety intelligence to workforce retention.

For ESG and investor relations, the framework provides a new quantitative input for the social pillar of ESG reporting. A monthly F/UF ratio by dimension is a trackable, reportable metric with a clear methodology behind it.

Suggested KPIs:

- Monthly F/UF ratio, overall and by dimension and team
- Alert count: number of dimensions or teams where the ratio dropped more than 10% month-on-month
- Intervention recovery rate: how much the F/UF ratio improves within 60 days of a targeted intervention
- Social Norms trajectory in the Mental Health & Wellbeing dimension

One design principle deserves emphasis here.

If the data source shifts from public social media to internal channels, transparency and consent are non-negotiable. The moment employees perceive safety attitude measurement as surveillance, honest expression disappears, data quality collapses, and the system defeats itself. The design default should be: measurement results are returned to the individual first; team-level reporting uses aggregates only. This is the same principle that governs responsible deployment of workplace emotion AI more broadly.

---

## Closing

The signal that a site is becoming dangerous often exists long before it appears in incident statistics.

A veteran who has started complaining about management. A new hire who has quietly decided that a particular safety rule makes no sense. A comment thread where "same at our site" gets twenty replies. None of these appear in formal reporting. But they are on Reddit.

Now that LLMs can read these signals at human-level reliability, the infrastructure to turn workforce voice into actionable safety intelligence has become technically available.

The question is no longer whether the tool works. It is whether safety management teams are ready to build the pipeline from text to insight to intervention — and to do it in a way that workers trust.

---

## Reference

- Farouq Sammour, Yuxin Zhang, Zhenyu Zhang, "Listening to the Workforce: Measuring Construction Worker Safety Attitudes from Social Media Discourse Using LLMs," arXiv:2606.04450, 2026.

<p class="ai-notice"><small>* This article was written in part with AI assistance and may contain inaccuracies.</small></p>
