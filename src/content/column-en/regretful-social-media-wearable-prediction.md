---
title: "Predicting the Scroll You'll Regret ── Wearables and Context Sensing for Social Media Regret Detection"
date: "2026-06-10"
excerpt: "Regret after doomscrolling isn't driven by time spent — it's driven by the gap between what you intended and what you actually did. An MIT–University of St. Gallen team ran a 7-day in-the-wild study with 21 participants to show wearable-plus-context sensing can predict regretful sessions before they fully unfold. Here's what that means for wellness app developers, HR teams, and platform wellbeing units."
image: "/column-images/regretful-social-media-wearable-prediction.png"
imageAlt: "Flat illustration of hands holding a smartwatch and smartphone, overlaid with an emotion waveform graph"
readingMinutes: 6
basedOnPaper: "Before You Scroll Again: Predicting Regretful Social Media Sessions from In-the-Wild Contextual and Wearable Sensing"
basedOnPaperUrl: "https://arxiv.org/abs/2606.08965"
---

Hi, I'm Keito Inoshita from Affectosphere Group.

"Ugh. I did it again."

The feeling of having mindlessly scrolled through social media is almost universal. And it doesn't track neatly with time: some 30-minute sessions feel fine; a 5-minute detour can leave a lingering sense of waste.

Current digital wellness tools can't distinguish between these cases. Screen time warnings monitor duration — they don't tell you whether a given session will become one you regret. Regret, by assumption, could only be observed after the fact. That assumption is what this research challenges.

A team at MIT Media Lab and the University of St. Gallen (Ahmed, Enkmann, Shimizu, Yip, Beermann, Alomar, Uebernickel, Maes) ran a 7-day in-the-wild study published in June 2026 on arXiv (arXiv:2606.08965), asking whether regretful social media sessions can be predicted before they complete — using wearable sensors and passively logged phone context.

Here's the breakdown for wellness app developers, HR/EAP practitioners, and platform wellbeing teams.

---

## 3 Points for Today

1. The strongest predictor of regret wasn't session length — it was the gap between intended and actual usage.
2. Regret clusters around nighttime use and sessions following productivity apps.
3. Contextual features generalize across users; physiological signals improve personalized prediction — pointing to a two-layer architecture.

---

## ① The Intent-Behavior Gap Outperforms Time as a Predictor

Start with the study design.

21 participants logged passive smartphone usage and physiological data from a Bangle.js 2 smartwatch (~$80) over 7 days of normal life. After each social media session, participants completed a brief survey. The dataset totals 1,445 session-level observations.

Collecting this scale of in-the-wild data with a low-cost wearable is itself notable. Prior work on physiological signals and social media use had been confined to lab settings. This is one of the first systematic in-the-wild attempts.

The headline finding: the strongest predictor of regret was not how long a session lasted. It was the gap between how long participants intended to use social media and how long they actually did. The intent-behavior discrepancy outperformed session duration as a predictor.

The implication: screen time limits are targeting the wrong variable. The problem isn't using social media for a long time — it's using it for longer than you meant to. Restriction-based tools that enforce time caps may be missing the underlying mechanism.

---

## ② When Regret Spikes: Nights and Post-Productivity Contexts

Beyond the intent gap, the research identified contextual patterns that amplify regret.

Nighttime social media use was associated with stronger regret. Late-night scrolling carries a high opportunity cost — it displaces sleep, a high-value alternative. The regret scales with how much of "something better" is being crowded out.

The second pattern: sessions that immediately follow productivity app use. Opening social media right after handling work email or documents raises regret risk. The likely cognitive mechanism is the sense of "I escaped from something I was supposed to be doing."

The structural finding: regret intensifies when social media use replaces a valued alternative — sleep, focused work, intentional rest. It's not the duration alone that triggers regret; it's the displacement cost.

For app designers, this opens concrete design directions. A prompt framed as "It's 11pm. You were just in email. Are you sure you want to open this?" is more information-dense than a flat screen time warning — and likely more effective.

---

## ③ A Two-Layer Architecture: Generalizable Context + Personal Physiology

The second major design insight concerns prediction model architecture.

Contextual features — time of day, previous app category, day of week, intent-behavior gap — generalized reasonably well across participants. A model trained on population-level patterns can start making useful predictions without extensive individual calibration.

Physiological signals (heart rate, accelerometer, and related wearable data) showed high inter-individual variability, making cross-user generalization harder. However, they contributed meaningfully to within-person prediction accuracy once enough personal data accumulated.

This suggests a two-layer design: a contextual baseline that works from day one, with physiological personalization layering in as individual data accumulates. The system is useful cold, and gets better with use.

That's a practically compelling architecture for consumer wellness products facing the cold-start problem.

---

## Business Implementation Use Cases

### Wellness App Development: Designing a "Digital Regret Score"

Rather than displaying screen time alone, apps could surface a real-time regret risk score derived from current time, preceding app usage, and intent-behavior gap patterns. The KPI to track isn't notification dismissal rate — it's reduction in user-reported regretful sessions. Intent capture (a lightweight pre-session prompt: "How long do you want to spend?") provides both the predictor signal and the intervention opportunity.

### HR / EAP Teams: Visualizing In-Work SNS Risk

Employee wellbeing programs can incorporate regret-oriented metrics without individual surveillance. Aggregating the frequency of social media sessions immediately following productivity app use — by hour and day of week — produces organization-level risk patterns without tracking individuals. This gives EAP program design an evidence base that goes beyond generic "digital wellness" messaging.

### Platform Wellbeing Units: Smarter Intervention Timing

Reducing regretful sessions is aligned with long-term platform trust. Wellbeing nudges triggered by context (time + preceding behavior + intent signal) rather than raw duration would be more targeted than current designs. This research provides the evidential grounding for that shift in trigger logic.

---

## Limitations and What Comes Next

21 participants over 7 days is meaningful as exploratory work, but generalizability at scale remains to be established. Regret measurement relies on self-report, and cultural variation in how regret is conceptualized is an open question.

The study also does not evaluate interventions. Predicting regret and reducing regret are different problems. Whether acting on these predictions actually changes behavior — and how — is the natural next step this work sets up.

Still, establishing in-the-wild baselines for when and why social media regret occurs is a meaningful advance for digital wellbeing research. It gives the field a more precise dependent variable than screen time, and an empirically grounded design target for the next generation of intervention tools.

That's all for today!

---

## References

1. Sally Ahmed, Jan Enkmann, Kye Shimizu, Ivy Yip, Vincent Beermann, Ayse Alomar, Falk Uebernickel, Pattie Maes (2026). *Before You Scroll Again: Predicting Regretful Social Media Sessions from In-the-Wild Contextual and Wearable Sensing*. arXiv:2606.08965.

<p class="ai-notice"><small>* This article was written in part with AI assistance and may contain inaccuracies.</small></p>
