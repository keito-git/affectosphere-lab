---
title: "AI in the Courtroom: Simulating Civil Trials to Forecast Litigation Outcomes"
date: "2026-06-10"
excerpt: "A multi-agent framework assigns LLMs the roles of judge, plaintiff, and defendant, then runs the full five-stage civil trial procedure to generate structured verdicts. The result is a practical pre-litigation tool that lets legal teams stress-test arguments and estimate damage ranges before committing to a court battle."
image: "/column-images/civil-court-simulation-llm.png"
imageAlt: "A flat illustration showing AI agents engaging in a structured legal debate as judge, plaintiff, and defendant in a virtual courtroom"
readingMinutes: 5
basedOnPaper: "Civil Court Simulation with Large Language Models"
basedOnPaperUrl: "https://arxiv.org/abs/2606.09632"
---

Hello. This is Keito Inoshita from Affectosphere Group.

A new class of legal AI tools is emerging — one that does not just answer legal questions but re-enacts the entire trial process.

The question "if this contract dispute went to court, would we win?" is one that enterprise legal teams face constantly. Getting a credible preliminary answer typically requires expensive attorney time or waiting until the situation has already escalated. A study published on arXiv in June 2026 (Yifan Chen et al., Tsinghua University; arXiv:2606.09632) proposes an alternative: run the trial in simulation first.

The paper introduces a multi-agent framework in which large language models play the roles of judge, plaintiff, and defendant, proceed through all five stages of civil court procedure, and generate a structured verdict. This is a meaningful departure from prior LLM-based legal tools that focus on document summarization or question answering. Here, the trial process itself becomes the computation.

---

## Three takeaways for today

1. Five-stage civil court procedure is fully reproduced by three LLM agents — judge, plaintiff, and defendant — each operating with role-specific strategies.
2. A two-layer memory module preserves evidentiary consistency across the full trial, and memory quality directly drives verdict quality.
3. The framework can serve as a pre-litigation stress test: input your evidence, observe the simulated outcome, and make a more informed settle-or-sue decision.

---

## ① A trial with three agents and five stages

The framework's architecture mirrors actual civil court procedure.

Stage one is preparation. The judge agent opens the session, verifies party identities, and handles procedural questions such as recusal challenges.

Stage two is court investigation. The plaintiff agent presents claims and factual assertions; the defendant agent responds. Both parties submit and examine evidence at this stage.

Stage three is court debate. This is the most adversarial phase. Both sides argue over liability, applicable law, and the scope of relief sought.

Stage four is final statement. Each party delivers a closing argument before the verdict.

Stage five is judgment. The judge agent synthesizes the accumulated record — both the in-session dialogue and the structured memory built across prior stages — alongside retrieved statutory references, and produces a structured verdict.

The three agents are designed with distinct strategic orientations. The judge is tasked with fact-finding, issue identification, and evidence review. The plaintiff is built to justify claims and counter defense arguments. The defendant is configured to challenge liability and present mitigating facts. Role-specific prompts encode these orientations in the same way that actual courtroom participants operate from different strategic positions.

---

## ② Memory as the backbone of legal consistency

Maintaining consistency across a long trial is one of the harder problems for LLMs. The framework addresses this with a two-layer memory design.

Short-term memory retains the dialogue history within the current stage. It ensures that agents respond coherently to what was just said.

Long-term memory is generated after the court investigation and debate stages conclude. It stores structured summaries of key issues, evidence findings, disagreements between parties, liability relationships, and the numerical figures that will matter for the damages calculation.

This long-term memory feeds directly into the verdict stage. The experiment confirms the causal relationship: when memory quality was degraded, the overall score dropped from 5.47 to 5.00. The cleaner the intermediate memory, the better the final judgment.

A statutory retrieval module is also integrated. Just as attorneys pull relevant case law and statutes from a legal database, the judge agent queries legal references in context during deliberation.

---

## ③ The pre-litigation simulation as a business tool

Translating the research into enterprise legal practice, the most direct application is a pre-litigation stress test.

Consider a payment dispute with a supplier, a contested termination of a service agreement, or a product liability claim. In each case, the legal team needs to form a preliminary view of the litigation risk before deciding whether to escalate, negotiate, or settle.

A civil court simulator allows the legal team to feed in their evidence, generate a simulated opposing argument, and observe how a neutral judge agent resolves the dispute. The output is not a legal opinion — it is structured information that helps calibrate the risk range before calling outside counsel.

The quantitative results support this framing. Liability allocation scores improved from 5.44 (direct generation) to 5.86 (simulation), a 7.7 percent gain. Simulating the adversarial process, rather than just asking an LLM to produce a verdict directly, produces better liability reasoning. This is consistent with what human attorneys know from experience: the process of constructing and stress-testing arguments surface issues that a first-draft answer misses.

Concrete use cases by function:

Law firms can use the simulator for pre-engagement screening. Before committing attorney hours, run a simulation against the client's evidence and get an early read on case strength.

In-house legal teams can use it to structure the settle-or-sue decision. Simulate the best-case and worst-case trial outcomes, then set negotiation parameters for settlement discussions accordingly.

Contract teams can build the simulation into pre-signing risk assessment for clauses with high dispute potential, particularly around liability caps, indemnification, and termination for cause.

A clean KPI to track is time-to-decision for litigation escalation: how many days from incident identification to "sue / settle / drop" decision. A pre-litigation simulation layer shortens that timeline by giving the team structured information early, before the situation has escalated into urgency.

---

## Limitations, stated plainly

The researchers are candid about where the system falls short.

Quantitative judgment precision — the accuracy of numerical damage estimates — remains the weakest dimension across all experimental configurations, ranging from 3.77 to 4.90 on a 10-point scale. For use cases that require reliable damage figures, the current system should not be treated as a forecasting tool.

Verdict quality varies substantially with the choice of underlying model. The spread between the best-performing and worst-performing model configurations is nearly a full point (4.54 to 5.47). Model selection matters.

The evaluation also relies on an LLM-based reviewer rather than legal experts, which is a meaningful gap for a domain where ground truth is defined by professional judgment.

These limitations define the appropriate scope: the simulator is a decision support tool for pre-litigation information gathering, not a replacement for legal counsel. The human-AI division of labor that makes sense here is to let the system surface the key arguments and risk range, then bring attorneys in for the judgment calls that require legal expertise.

---

## Running the rehearsal before the real thing

Courts are adversarial systems where the side with stronger evidence and sharper argument tends to win. If you can rehearse that adversarial process before the actual filing — stress-testing your evidence, identifying weak points in your argument, and seeing how a neutral party is likely to rule — that preparation has obvious value.

The framework's code and dataset are set for public release, which means the technical barrier to adapting this for jurisdiction-specific use cases will drop. For legaltech companies, this is a product architecture reference. For enterprise legal departments, this is the shape of a tool that is coming in the next few years.

Worth watching closely.

That's it for today!

---

## Reference

1. Yifan Chen, Haitao Li, Kaiyuan Zhang, Yueyue Wu, Qingyao Ai, Yiqun Liu (2026). *Civil Court Simulation with Large Language Models*. arXiv preprint arXiv:2606.09632.

<p class="ai-notice"><small>* This article was written in part with AI assistance and may contain inaccuracies.</small></p>
