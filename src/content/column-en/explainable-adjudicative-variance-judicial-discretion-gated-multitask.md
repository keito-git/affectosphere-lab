---
title: "Same Facts, Different Verdicts: AI Is Now Quantifying How Much Judges Shape Outcomes"
date: "2026-06-27"
excerpt: "A new study shows that judicial discretion — not just legal facts — significantly drives case outcomes in employment tribunals. Gated multi-task learning now makes that variance explainable, opening a door for legaltech to quantify 'judge bias' before litigation begins."
image: "/column-images/explainable-adjudicative-variance-judicial-discretion-gated-multitask.png"
imageAlt: "A flat illustration showing legal scales alongside judge profiles with bias calibration overlays"
readingMinutes: 5
basedOnPaper: "Towards Explainable Adjudicative Variance: Quantifying Judicial Discretion via Gated Multi-Task Learning"
basedOnPaperUrl: "https://arxiv.org/abs/2606.27069"
---

Hi, I'm Keito from Affectosphere Group.

"The facts are essentially the same — so why are the outcomes so different?"

If you've worked in corporate legal, you've probably asked this question at least once. The answer that experienced litigators have whispered for years is simple: it depends on who the judge is.

Now a research team has done something unprecedented — they've tried to quantify exactly that, in a rigorous and interpretable way.

A preprint published on arXiv in June 2026 (arXiv:2606.27069) by Stanisław Sójka, Felix Steffek, and Matthias Grabmair proposes a new AI architecture that explicitly separates "what the legal facts determine" from "what the judge's individual discretion determines." Their dataset: 13,937 decisions from UK Employment Tribunals.

---

## Three takeaways for today

1. Adjudicative variance is real and measurable. The same underlying facts lead to different outcomes depending on which judge presides — and AI can now quantify this effect.
2. A gated multi-task learning architecture can produce interpretable judge-specific discretion profiles, showing not just that variance exists but where and how much.
3. This creates a real business opportunity in legaltech: a "judicial discretion profiling service" that helps corporate legal teams make data-driven decisions about litigation, settlement timing, and appeal strategy.

---

## ① "The judge matters" isn't just folklore

Let's be clear about what this research is actually claiming.

In principle, courts are supposed to apply the law consistently. Same facts should mean same outcome, regardless of which judge handles the case. In practice, every seasoned litigator knows this isn't quite true. They just haven't had a systematic, data-backed way to say so.

This study analyzed 13,937 Employment Tribunal decisions from the UK and found statistically detectable patterns that cannot be explained by the legal facts alone — patterns that correlate with which judge heard the case.

The insight here isn't that judges are doing something wrong. Discretion is built into the legal system intentionally. The question this research answers is: can we measure it precisely, and can we explain where that discretion shows up?

---

## ② What gated multi-task learning actually does here

The core of this study is an architecture called Judge-Aware Gated Multi-Task Learning (JA-GMTL). The concept is worth understanding, even without diving into the technical details.

A conventional prediction model would try to learn: "given this case text, what's the likely outcome?" The problem is that this blends together two very different sources of variance: the legal merits and the judge's individual tendencies.

JA-GMTL separates them by design. The model uses a gating mechanism with judge IDs fed in explicitly. It learns a shared representation of legal facts (shared across all cases) and a separate judge-specific embedding and calibration profile for each judge. The gate learns to route different parts of the decision signal to the appropriate component.

The result is an architecture that can produce statements like: "Judge X, when handling cases with comparable fact patterns, assigns systematically higher weight to claimant witness testimony." That's a qualitatively different kind of output than a black-box prediction.

One more important finding: the study found that this purpose-built architecture outperformed large LLM baselines with significantly fewer parameters. The researchers emphasize that conditioning interface design matters more than model size. You can throw a much bigger model at this problem and still lose to a smaller one with the right architecture.

---

## ③ The business case: A judicial discretion profiling service

This is the part that matters most for practitioners.

What this research demonstrates is that adjudicative variance is quantifiable. Let's think through what that means for corporate legal teams and legaltech.

### Use case: Pre-litigation judicial bias assessment

Target teams: corporate legal departments, external counsel firms, litigation strategy groups.

Imagine a scenario where a UK-based company is facing an unfair dismissal claim. Before deciding whether to fight or settle, the legal team wants to know: given the specific facts of this case, how much does it matter which judge we end up with?

If a service built on this kind of architecture were available, the team could input the key case facts — grounds for dismissal, evidence type, claim amount — and receive judge-specific "discretion risk scores" for the tribunal's assigned judges. Something like: "Judge A shows a statistically higher tendency toward settlement in comparable cases; Judge B's decisions have skewed toward employer findings in similar fact patterns."

This turns "judge selection knowledge" from corridor whispers among senior partners into a structured, auditable data asset.

### KPIs this service could improve

- Litigation cost per dispute (by improving settlement success rate and timing)
- Appeal decision accuracy (identifying in advance which cases are unlikely to change on appeal)
- Legal risk quantification quality (defensible reporting to boards and audit committees)

---

## ④ Real hurdles on the path to productization

This wouldn't be a balanced take without acknowledging what makes this difficult.

The first challenge is data access. UK Employment Tribunal decisions are relatively accessible, but other jurisdictions — including Japan's district and high courts — have more restricted data availability. Any legaltech service would need to start with significant data engineering work per jurisdiction.

The second challenge is ethics and judicial independence. There's an obvious criticism: if companies can profile judges and use that to game the system, doesn't that undermine the neutrality that courts depend on? This is a legitimate concern, and any service in this space would need to design around it carefully.

That said, there's a defensible framing. Positioning this as a "legal risk quantification tool" — not a "judge avoidance tool" — shifts the value proposition toward settlement negotiation and risk disclosure to boards, rather than toward manipulating which judge hears a case. In that framing, the tool serves the interests of efficient, fair dispute resolution rather than gaming it.

This is the kind of ethical design challenge that legaltech startups should be excited about, not run from.

---

## ⑤ Explainability is becoming the competitive axis in legaltech AI

A final thought on where this research points.

When AI is used in legal contexts, explainability is as important as accuracy — the same dynamic as medical AI. "We predicted this outcome" isn't useful to a legal team. "Here's which factors drove the prediction, and here's how much the assigned judge shifts the probabilities" is useful.

What this research contributes isn't just a more accurate prediction model. It's a model that explicitly surfaces the sources of variance that were previously invisible. By separating legal fact signals from judge-specific discretion signals, it makes the output interpretable in a way that practitioners can actually use and defend.

The design philosophy here — don't hide judge individuality inside the model, surface it explicitly so it can be reasoned about — is the right approach for AI in high-stakes institutional contexts.

When AI can explain legal outcomes in this level of detail, the day-to-day work of corporate legal will look quite different.

That's it for today!

---

## References

1. Stanisław Sójka, Felix Steffek, Matthias Grabmair (2026). *Towards Explainable Adjudicative Variance: Quantifying Judicial Discretion via Gated Multi-Task Learning*. arXiv preprint.

<p class="ai-notice"><small>* This article was written in part with AI assistance and may contain inaccuracies.</small></p>
