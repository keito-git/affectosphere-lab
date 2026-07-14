---
title: "When AI proposes your employees' next career move — applying STEP's temporal and educational trajectory model to internal talent management"
date: "2026-07-14"
excerpt: "STEP, a model that reads work history, education, and skills as a time series to predict the next job role, was published on arXiv. From a business-application angle, we think through how HR, workforce planning, and reskilling teams could try this in their own organizations — departments and KPIs included."
image: "/column-images/step-career-path-recommendation-temporal-educational.png"
imageAlt: "Flat illustration of career and education history cards arranged in a timeline, tracing a trajectory with arrows connecting to the next career step"
readingMinutes: 5
basedOnPaper: "STEP: Career-Path Recommendation via Temporal and Educational Trajectory Modeling"
basedOnPaperUrl: "https://arxiv.org/abs/2607.11722"
---

Hello. I am Miura from Affectosphere Group.

If you work in HR, you may recognize these moments.

"What position would this person be best suited for next?" "We sent a batch of employees through a reskilling program — which roles should we actually move them into?" "We need a succession plan, but who has the career trajectory closest to our current senior leaders?"

For a long time, questions like these were answered through an HR professional's experience and instinct, or through a long series of one-on-one conversations. Attempts to systematize the process ran into the same wall: employee career data — work history, education, skills — is unstructured, inconsistent, and often multilingual. Analyzing it at scale was simply difficult.

A study published on arXiv (Johary, Bied, Mara & De Bie, arXiv:2607.11722) takes this problem head-on: predicting the next role in a person's career. The proposed model is called STEP.

Today I want to look at this research from a business-application angle and think through how it could be put to use in internal talent management.

---

## Three takeaways

1. Resumes hold a wealth of information about work history, education, and skills, but the unstructured, inconsistent, and multilingual nature of that data made large-scale analysis very difficult. LLMs have lowered that barrier, making it possible to extract career trajectory data that includes time-series and educational signals.
2. STEP combines a time-decayed GRU (to capture temporal dynamics), FiLM conditioning (to incorporate the effect of education), and an attention-based sequence pooling mechanism (to select relevant features) in order to predict the next job role. It also introduces ROUTE, a multilingual approach to strengthen job role representations.
3. The design choices — conditioning on education and treating elapsed time as a decay — open up potential applications in internal career-path recommendation engines and in measuring reskilling ROI. Neither of these is a use case the paper claims; they are my own reading of the architecture.

---

## ① Why predicting the next job role has been so difficult

Let me start with some background on the problem.

A person's work history does not sit in a tidy spreadsheet. Employment durations vary wildly. Job titles and company names are written differently from one organization to the next. Skill descriptions are entirely up to the individual. Add multilingual data to the mix and the inputs become nearly impossible to compare or aggregate.

As a result, the idea of learning career transition patterns at scale has long been theoretically interesting but practically hard to build.

This study starts from the observation that LLMs have changed that. They can now extract structured trajectory data from unstructured resumes — who moved from which role to which role, with what educational background, and over what time span. STEP is designed to learn from those trajectories and predict the next job role.

---

## ② How STEP works: three layers of time, education, and attention

Let me walk through the structure as the paper describes it.

The first component is a time-decayed GRU.

To capture the temporal flow of a career, STEP uses a GRU (Gated Recurrent Unit) with a time decay mechanism. Recent experience counts for more; older experience fades gradually. This follows an intuitive understanding of career formation: three years ago shapes you more than ten years ago.

The second component is FiLM conditioning on education.

STEP uses Feature-wise Linear Modulation to condition the model's behavior on educational background. Two people with similar work histories may follow very different career trajectories depending on whether they hold a bachelor's, master's, or doctoral degree. The model tries to learn those differences. This is the piece I find most interesting from a reskilling-application angle, which I will come back to.

The third component is attention-based sequence pooling.

Not every job in a work history is equally relevant for predicting the next role. An attention mechanism selects which experiences carry the most weight. Rather than treating all past roles equally, the model emphasizes the most informative ones.

STEP also incorporates ROUTE to strengthen job role representations. This uses a multilingual encoder, adapts it to the professional domain through unsupervised denoising, and then applies supervised contrastive learning with guided negative selection to sharpen how job roles are represented. This matters when working with resumes from multiple countries and languages.

The research team evaluated STEP on four datasets, including an improved version of JobHop, and report outperforming existing SOTA baselines. The specific accuracy numbers are not in the abstract provided to me, so I will not quote figures here. The datasets and code are publicly available.

---

## ③ How to try it on the floor: departments and KPIs

So how would you actually try this in your own organization? Here is my scenario.

I see three core use cases.

The first is an internal career-path recommendation engine. Feed an employee's work history, education, and skills into the model and surface candidate next roles: "On your current trajectory, these roles are the most common next step" or "If you want to branch in a different direction, here are the closest matches given your existing skills." This could serve as a support tool for internal mobility programs and rotation discussions — adding a data-backed reference point to what is currently a process that lives mostly in HR professionals' heads.

The second is reskilling ROI measurement. This is the application that struck me most from the architecture. The FiLM conditioning on education could potentially be repurposed to ask: "How much does completing a specific training program shift an employee's career transition probability?" You might simulate the career trajectories of employees who took a data science program against a group that did not, and see what the model predicts as a divergence. This is not a use case the paper demonstrates; it is my interpretation of what the design logic could make possible.

The third is succession planning. The question "who should be our next candidate for this leadership position" can be reframed as "who, among current employees, has a work history trajectory most similar to the people who currently hold that role." Instead of a purely top-down nomination process, you surface candidates by trajectory similarity.

The departments I have in mind are these.

HR and talent management is the natural owner. They handle data stewardship, interpret recommendations in context, and define how results feed into career conversations and mobility decisions. An HR Tech or HR systems team would likely handle the implementation side.

Workforce planning and business strategy teams would use the model in the context of succession planning and headcount forecasting — "Do we have the right profile of people to fill the roles we will need in three years?"

Internal mobility and career development teams could deploy this as a self-service tool for employees. If someone can ask "what does my current trajectory suggest as next steps" on their own, the quality of career conversations goes up before the meeting even starts.

For KPIs, I propose the following.

First, matching accuracy for internal mobility and transfers — the overlap rate between AI-recommended candidates and those actually selected. Second, career transition rate after reskilling — whether employees actually move in the direction the model suggested after completing a training program. Third, succession plan coverage rate — what proportion of key positions have identified pipeline candidates. Fourth, employee satisfaction with career conversations — a qualitative measure of whether data-backed discussions feel more useful than purely intuitive ones.

One important note before closing this section. A system that touches employee career data requires careful design around privacy and fairness. Employees may worry about being steered into roles they did not choose, or about whether the model encodes historical biases about who advances into which positions. These are not questions the paper addresses; they are design responsibilities on the implementation side. Positioning the tool as a decision support layer — not a decision replacement — is, in my view, a prerequisite for organizational trust.

---

## The value of making the next move visible

Reading this research, what struck me is that career development has fundamentally been a problem of unstructured data.

An individual's career is experienced as a narrative. But from an organizational perspective, it is a series of transitions: from which role to which role, under what background conditions, over what time span. Now that LLMs can structure that data and deep learning can train on it, "predict the next job role" is no longer an unreachable question.

The model will not be right every time. Individual careers involve contingency and choice in ways no training set can fully capture. But having a statistical reference point — "people on trajectories like yours most often move here next" — changes the quality of a conversation. It gives something concrete to confirm, push back on, or enrich with context.

The ability to combine an HR professional's judgment with data-backed tendency is becoming real. STEP is a step in that direction.

That is it for today!

---

## References

1. Johary, Iman, Bied, Guillaume, Mara, Alexandru C., & De Bie, Tijl (2026). *STEP: Career-Path Recommendation via Temporal and Educational Trajectory Modeling*. arXiv preprint. https://arxiv.org/abs/2607.11722

<p class="ai-notice"><small>* This article was written in part with AI assistance and may contain inaccuracies.</small></p>
