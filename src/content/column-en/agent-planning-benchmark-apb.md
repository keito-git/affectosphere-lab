---
title: "Can You Tell Whether an AI Agent Failed at Planning or Execution?"
date: "2026-06-06"
excerpt: "When an LLM agent fails, most evaluations can't tell you whether planning or execution was the problem. APB is a diagnostic benchmark designed to break that black box open — and it has direct implications for how organizations should select agents before deploying them."
image: "/column-images/agent-planning-benchmark-apb.png"
imageAlt: "An abstract illustration of an LLM agent's planning capability being evaluated across multiple diagnostic settings"
readingMinutes: 5
basedOnPaper: "Agent Planning Benchmark: A Diagnostic Framework for Planning Capabilities in LLM Agents"
basedOnPaperUrl: "https://arxiv.org/abs/2606.04874"
---

Hello. This is Keito Inoshita from Affectosphere Group.

"This LLM agent didn't work well" — when that happens, can you say exactly why?

Was the initial plan wrong? Was the tool selection poor? Was the model the problem? Was the task too complex? Was the issue multi-step consistency, or handling unexpected errors?

If you can't distinguish between those, you'll end up iterating by trial and error — switching models without knowing whether the root cause was the model's planning capacity, its execution behavior, or something about the task structure itself.

A study published on arXiv in June 2026 (Haoyu Sun, Wenxuan Wang, Mingyang Song et al., arXiv:2606.04874) proposes a diagnostic benchmark designed to answer that question systematically: APB (Agent Planning Benchmark).

---

## Three takeaways for today

1. Existing agent evaluations measure final task success, not planning capability specifically — leaving failure root causes unknown.
2. APB covers 22 domains and 4,209 cases across five diagnostic settings: global planning, step-wise planning, tool distraction, broken tools, and unsolvable tasks.
3. Evaluating 12 models revealed systematic weaknesses in long-horizon planning, tool noise robustness, and the ability to recognize and refuse unsolvable tasks.

---

## ① Why separating planning from execution matters

Evaluating LLM agents is genuinely hard.

When an agent fails to complete a task, there are multiple possible reasons:

- The initial plan was wrong: the agent misunderstood the goal or sequenced the steps incorrectly.
- The plan was right but individual tool selection or execution failed.
- An unexpected error appeared mid-plan and the agent couldn't adapt.
- The task was actually unsolvable, and the agent started executing it anyway.

Most current agent evaluations measure "did the agent eventually succeed?" That's a reasonable end-to-end metric, but it tells you nothing about which of the above caused a failure. You change the model, and it fails for the exact same reason — but you couldn't tell from the previous evaluation.

APB addresses this by focusing specifically on planning capability, measured from multiple diagnostic angles.

---

## ② APB's five settings and the weaknesses they revealed

APB evaluates 22 domains and 4,209 multimodal cases across five configurations.

Global planning measures how accurately an agent can lay out the complete sequence of steps required to achieve a task. Step-wise planning evaluates the ability to execute plans incrementally, maintaining coherence as the task unfolds.

The remaining three settings assess robustness. Tool distraction introduces unnecessary tools into the available set, measuring how much irrelevant options degrade planning quality. Broken tools places non-functional tools in the environment, testing whether the agent can adapt when its expected tools don't work. Unsolvable tasks evaluates whether the agent can correctly recognize an impossible task and decline to execute, rather than proceeding with a doomed plan.

Evaluating 12 models across these settings surfaced several systematic weaknesses.

Multi-step long-horizon tasks caused significant performance drops across nearly all models — consistency broke down as step count increased. Tool noise had a disproportionate effect on planning judgment, with many models getting pulled in the wrong direction by irrelevant or broken tools. And the ability to recognize and refuse unsolvable tasks was the weakest setting across almost all models evaluated.

---

## ③ Using APB-style diagnostics before deployment

The practical value of this research is that it makes it possible to characterize an agent's planning capability quantitatively before you commit to deploying it.

The current typical approach to enterprise AI agent deployment is "just run a PoC." Try it on a real task, observe what breaks, then investigate. PoCs are expensive in time and resources. And when a PoC fails, the root cause — whether it was planning capability, tool handling, robustness, or task difficulty — often remains unclear.

An APB-style diagnostic framework gives you something to work with before the PoC. "This model is weak at long-horizon planning." "This model has low robustness to tool noise." These are specific, measurable properties you can use to filter candidates before committing to a full evaluation.

For information systems teams and consultants deciding which model to use for a specific workflow, this is exactly the kind of objective reference that makes model selection defensible rather than intuition-driven.

You can also define your workflow's planning requirements up front:

- For short, single-step tasks: prioritize step-wise planning scores over global planning.
- For environments with unreliable tools: weigh robustness settings more heavily.
- For workflows where "stop when the task is impossible" is critical: prioritize refusal judgment scores.

Matching APB scores to your workflow requirements makes agent selection discussions significantly more concrete.

---

## The value of having language for planning failures

Most discussions about LLM agent failures are still at the level of "it worked / it didn't work."

Being able to say specifically "this model struggles with tool noise" or "it loses coherence in long-horizon tasks" changes what you can do. Model selection becomes more principled. Workflow design can account for known weaknesses. Improvement efforts have measurable targets.

APB provides that vocabulary. When the research community shares a common diagnostic baseline, improving agent planning capacity shifts from a vague goal to a tractable, measurable one.

If teams evaluating enterprise AI deployment start routinely referencing benchmarks like APB, PoC failure rates and post-deployment friction should come down.

That's it for today!

---

## Reference

1. Haoyu Sun, Wenxuan Wang, Mingyang Song, Jujie He, Weinan Zhang, Yang Liu, Yang Yang, Yu Cheng (2026). *Agent Planning Benchmark: A Diagnostic Framework for Planning Capabilities in LLM Agents*. arXiv preprint.

<p class="ai-notice"><small>* This article was written in part with AI assistance and may contain inaccuracies.</small></p>
