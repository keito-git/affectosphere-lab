---
title: "Your Typing Tells the Truth — Using Keystroke Dynamics to Surface Where LLM Tools Are Actually Failing Workers"
date: "2026-07-01"
excerpt: "A 36-person experiment confirms that how people type while prompting an LLM reveals their cognitive load. Here is how companies can turn that signal into a workplace analytics layer that finally shows whether AI tools are helping or just adding friction."
image: "/column-images/keystroke-dynamics-cognitive-effort-human-llm-prompting.png"
imageAlt: "Flat illustration of a keyboard with typing patterns overlaid on a cognitive load graph"
readingMinutes: 5
basedOnPaper: "Typing Behavior in Human-LLM Interaction: Keystroke Dynamics Reveal Cognitive Effort During Prompting"
basedOnPaperUrl: "https://arxiv.org/abs/2606.28090"
---

Hello. I am Miura from Affectosphere Group.

Ask a knowledge worker "do you use your company's LLM tool?" and most will say yes.

Ask "is it actually making your work easier?" and you will hear a lot more hesitation.

One reason AI adoption ROI is hard to prove is that "how hard it is to use" leaves almost no trace in standard usage logs. You can count sessions and prompts. You cannot see the cognitive effort behind each one.

A paper published on arXiv in June 2026 (Schütz et al., arXiv:2606.28090) offers a practical entry point. The way someone types while writing a prompt turns out to be a passive sensor for their cognitive load. No surveys. No interruptions. The signal is already in the keystroke metadata.

---

## Three takeaways

1. Keystroke dynamics during LLM prompting — typing speed, pause frequency, backspace rate — are reliable passive indicators of cognitive effort, confirmed in a 36-participant experiment.
2. High-difficulty tasks produced significantly more keystrokes, slower input, and longer pauses. These patterns aligned with subjective workload ratings.
3. Keystroke metrics did not predict the usefulness of the LLM's response. They measure user-side effort independently of tool-side output quality — a distinct and separately trackable dimension.

---

## ① What are keystroke dynamics?

Keystroke dynamics refers to the temporal patterns in typing behavior: the time between key presses, the duration of pauses mid-input, backspace usage rate, and overall characters-per-minute.

The field has a history in security — keystroke patterns have been used for biometric authentication. This research extends that tradition into a new context: using these signals to passively measure cognitive effort during human-LLM interaction.

"Passive" is the key word here. Unlike think-aloud protocols or post-session questionnaires, keystroke logging requires nothing extra from the user. As long as they are typing, the data stream exists.

---

## ② Study design

Thirty-six participants completed tasks of varying cognitive difficulty while typing prompts to an LLM. The design contrasted low-load conditions (clear, simple inputs) with high-load conditions (complex problem setups requiring the user to formulate what to ask while already engaged in reasoning).

Measured keystroke metrics included total keystroke count, mean input speed (characters per minute), pause frequency and duration, backspace rate, and total time from first keystroke to submission. Participants also completed subjective workload assessments analogous to the NASA-TLX scale.

---

## ③ Cognitive difficulty shows up in how you type

Results were consistent across participants. High-load tasks produced measurable changes in all major keystroke metrics.

Keystroke count increased. Users typed and rewrote more as they worked through what to say. Input speed slowed. Cognitive interruptions between thoughts reduced fluency. Pauses became longer and more frequent. The "what do I write next" moments left visible gaps in the timing data.

These patterns correlated significantly with subjective workload scores. Participants who rated a task as difficult also showed the clearest keystroke disruption patterns.

The negative finding is equally important. The same metrics did not predict whether the LLM returned a useful answer. A user who struggled to write a prompt might get an excellent response. A user who typed fluently might get a useless one. The two dimensions — user effort and output quality — are independent.

---

## Why this matters for workplace analytics

Many organizations have now rolled out Microsoft Copilot, internal LLM chat tools, or AI-assisted writing environments at scale.

Usage logs tell you who is using the tool and how often. They do not tell you whether using the tool is effortful or smooth for different users across different task types.

Keystroke dynamics can fill that gap.

Analyzing the timing metadata from prompt inputs — without reading prompt content — makes it possible to estimate where cognitive load is highest by task category, department, or role. That is the missing dimension in most current AI adoption dashboards.

---

## Implementation proposal: a keystroke-based cognitive load monitoring layer

The target audience is the IT or UX team, the HR analytics function, or the L&D team at any organization running LLM tools at scale.

First, add keystroke timing metadata collection at the browser or application layer. You do not need to capture what users type — only the temporal patterns (inter-key intervals, pause durations, backspace rates). This makes the privacy surface relatively narrow compared to content logging.

Second, compute a monthly cognitive load index by business function and department. Visualize this as a matrix: which task categories, in which organizational units, are generating consistently high estimated effort. This is where AI support is creating friction rather than relief.

Third, target high-load segments with prompt training, template libraries, or workflow redesign. Measure impact by tracking average input speed improvement and pause frequency reduction over the following quarter. The framework lets you quantify training ROI in terms that go beyond session counts.

For a large enterprise, running this analysis quarterly can produce a clear prioritization map for where AI capability-building investment will have the highest return.

---

## The distance between "using AI" and "benefiting from AI"

One reason AI deployment results disappoint is that adoption metrics stop at usage volume. Sessions are up. But cognitive load may be up too. Workers are spending effort to engage with a tool that was supposed to reduce effort.

Keystroke dynamics offer a low-cost, non-intrusive signal to start measuring that gap. The 36-person study is modest in scale, but the direction is clear enough to act on.

For product managers building LLM-adjacent tools, and for HR teams responsible for workforce capability, adding a cognitive load dimension to your AI usage analytics is a practical next step that this research now provides a methodology for.

See you next time!

---

## References

1. Schütz, Laura, Cherif, Yousri, Sayffaerth, Clara, Weber, Thomas, & Chiossi, Francesco (2026). *Typing Behavior in Human-LLM Interaction: Keystroke Dynamics Reveal Cognitive Effort During Prompting*. arXiv preprint.

<p class="ai-notice"><small>* This article was written in part with AI assistance and may contain inaccuracies.</small></p>
