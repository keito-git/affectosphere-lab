---
title: "Does an AI Need Emotion to Find Problems No One Has Posed?"
subtitle: "Must a Machine Feel before it can Ask? Functional Emotion and Problem Discovery in Open-ended Artificial Intelligence"
date: "2026-11-27"
excerpt: "What would a self-improving AI need in order to find problems that humans have not yet put into words? A walk-through of a theoretical paper (SSRN preprint) that focuses on the stage before a problem exists, argues which functions that stage requires, and states, in falsifiable form, the hypothesis that emotion fills one of them."
readingMinutes: 13
showImage: false
image: "/column-images/ssrn-functional-emotion-problem-discovery/appraisal-complementarity.png"
imageAlt: "Problem discovery through appraisal complementarity. When the appraisal of an unresolved state and the transition appraisal of an experience from another domain are complementary, the experience is recruited, verified and turned into a new problem."
authors:
  - name: "Keito Inoshita"
    url: "/en/about/"
    affiliation: "Kansai University"
tldr: "Current AI solves problems, and even generates its own goals, once a task or success criterion is available. For the earlier stage, turning an unresolved state that is not yet a problem into a new problem, falsifiable mechanisms are rare. This paper defines problem discovery through a budget-bounded reachable set and argues that in a hard case, where the resolving experience is unrelated in content and verification is scarce, a reliable discoverer must realize three roles: (a) retain the unresolved state, (b) rank candidates by a signal that relies on neither the resolution condition nor content similarity, and (c) fund verification that utility does not support. It then hypothesizes that concern-relative appraisal with directional complementarity realizes (b) and transfers to new domains, and defines this assembly as functional emotion. Emotion is not claimed to be the only route, and six falsifiable predictions are given. The paper is a preprint that has not been peer reviewed, and it contains no experimental data."
links:
  - label: "Preprint (SSRN)"
    url: "https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7535040"
citation: |
  @misc{inoshita2026mustamachinefeel,
    title        = {Must a Machine Feel before it can Ask? Functional Emotion and
                    Problem Discovery in Open-ended Artificial Intelligence},
    author       = {Inoshita, Keito},
    howpublished = {SSRN preprint, abstract id 7535040},
    year         = {2026}
  }
---

<div class="teaser">
<div>

Roles

Reliable discovery in the hard case needs three roles: **retention, selection and funded verification**. This is a conditional necessity under stated premises.

</div>
<div>

Hypothesis

Selection is realized by **complementarity of concern-relative appraisal**. A state of being obstructed matches an experience of an obstruction being removed.

</div>
<div>

Falsify

The claims can be refuted through **six predictions**. Emotion is not claimed to be the only route to discovery.

</div>
</div>

## The stage before a problem exists

AI now surpasses human performance on a widening range of tasks, and the argument for an intelligence explosion, in which self-improving machines grow ever more capable, has become more concrete. Recent work has named open-endedness as what such a process requires. Agents no longer only solve problems; they also propose their own goals and tasks.

Most of this progress, however, presupposes that something is already represented as a problem: a task description, a reward, a success criterion or a space of goals. In 2026 several proposals placed the next frontier earlier, at judging which phenomena may matter before their significance is known, or at working from tacit friction before a question forms. The observation itself is old. Dewey held that a problem must be felt before it can be stated.

The paper names three things that are still missing. The first is a non-vacuous notion of a new problem. An agent that can write code can express almost any hypothesis, so defining new problems as those that cannot be stated in the current vocabulary would make every problem already available. The second is a mechanism that carries an agent from an unresolved state to a representable problem, with predictions specific enough to be refuted. The third is a balanced answer to whether such a mechanism requires emotion. "Only emotion makes problem discovery possible" is too strong to defend, and "emotion is one option" says nothing about emotion.

## Defining problem discovery

<figure>
  <img src="/column-images/ssrn-functional-emotion-problem-discovery/problem-discovery-gap-1600.webp" alt="The problem-discovery gap" />
  <figcaption><strong>Figure 1.</strong> The problem-discovery gap (Figure 1 of the paper). Typical methods start once a problem is represented; problem discovery must reach a representable problem from an unresolved state L, and the selection mechanism in between is missing.</figcaption>
</figure>

The paper's example is as follows. An agent manages both the computing pipeline and the physical facilities of a laboratory. It notices that pipeline runs stall at irregular times. This creates a discrepancy on one of its concerns, reliable throughput, but no hypothesis it holds predicts the stalls, so nothing it would try is expected to help. Weeks later, in its separate role of scheduling the loading dock, it sees deliveries stop piling up once an unused standing reservation is released. The two episodes share little vocabulary, and a retrieval system keyed to the pipeline is unlikely to surface the dock episode. What they share is relational: one is a state of being obstructed with no identified cause, the other a transition in which an obstruction was removed by releasing an unused hold. If this correspondence brings the dock episode to verification, the agent can pose a testable problem it had not posed before: do some jobs hold locks they no longer use?

The paper formalizes this as follows.

- **Concern**: an internally maintained variable with a set point or constraint, whose violation raises a discrepancy δ_k. It holds what matters to the system before anything is formulated as a goal.
- **Budget-bounded reachable set**: under a fixed generation-and-evaluation protocol and budget B, the problems reachable from an unresolved state L without recruiting other stored experiences and predicted to reduce the discrepancy. L is **unresolved** when it persists and this set is empty.
- **Problem discovery**: the event in which, later, a problem outside that set becomes actionable through a recruited experience. It is a **validated discovery** if pursuing it actually reduces the discrepancy, which keeps finding separate from solving.

Because the definition asks what is generated within the budget rather than what is expressible, lock contention counts as a discovery not because it was inexpressible but because it was not among the hypotheses the agent would have generated from the stalls alone.

## Argument 1: Are three roles necessary?

<p class="experiment-label">Argument 1</p>

The paper sets out five premises. An open-ended agent must expand its repertoire, not only solve problems within it (P1). Goal-conditioned allocators fund verification by expected utility and so do not fund candidates whose relation to any available problem cannot be estimated (P2). Verification is scarce and resolving candidates are sparse (P3). Optimization and conventional retrieval work systematically only once what is sought is represented in some form (P4). Unresolved states arise first, and the experiences that resolve them are met later (P5).

These premises define a **hard case**: the resolving experience Z is unrelated in content to the episode where L arose, and P3 holds. Content-based retrieval then has no systematic advantage, utility-based allocation has nothing to estimate, and chance selection is defeated by scarcity. If M of N candidates would resolve L and B can be verified, chance succeeds at about BM/N.

<figure>
  <img src="/column-images/ssrn-functional-emotion-problem-discovery/argument-structure-1600.webp" alt="Structure of the two-stage argument" />
  <figcaption><strong>Figure 2.</strong> Structure of the two-stage argument (drawn from Sections 3.4, 4.1 and 4.3 of the paper). Conclusion 1 is a structural necessity under the premises; Conclusion 2 is a defeasible reason that depends on hypotheses and on a premise about the world.</figcaption>
</figure>

**Conclusion 1 (role necessity)**: under P1–P5, a resource-bounded sequential discoverer that reliably discovers problems in the hard case (at a rate at least κ > 1 times chance, independent of N) must realize functions equivalent to three roles, whether as explicit modules or implicitly in its weights.

- (a) **Retain** L across intervening episodes.
- (b) Have a **selection signal** σ(L, Z) that ranks candidates without presupposing a representation of the resolution condition and without relying on content similarity.
- (c) Allow σ to **fund verification** even when goal-conditioned utility gives no support.

The paper openly concedes that (a) follows almost from the definition that L persists, and that ranking better than chance in (b) also holds almost by definition. The substantive claims reduce to two: the hard case is not empty in the world, and (a) and (c) are each necessary in addition to (b). Conclusion 1 states the necessity of roles, not of emotion.

## Argument 2: The appraisal-complementarity hypothesis

<p class="experiment-label">Argument 2</p>

Emotion enters in the second stage. The paper distinguishes a space of state types (being obstructed, lost, unreachable, threatened) from a space of transition types (an obstruction being removed, a loss recovered, a threat averted). Both are shared across domains.

<figure>
  <img src="/column-images/ssrn-functional-emotion-problem-discovery/appraisal-complementarity-1600.webp" alt="Problem discovery through appraisal complementarity" />
  <figcaption><strong>Figure 3.</strong> Problem discovery through appraisal complementarity (Figure 2 of the paper). A candidate from Domain 2 is recruited when its transition appraisal, computed at retrieval, complements the appraisal of the unresolved state in Domain 1. Verification funded by the selection signal turns a successful candidate into a new problem; on failure the process returns to L.</figcaption>
</figure>

An unresolved state receives a state appraisal a_L computed from its concern, the current state and the history. Each stored experience keeps a relational representation of its transitions, and its transition appraisal is computed at retrieval relative to the concern at issue. The selection signal is the **complementarity** C between the two, a mapping from state types to the transition types that would improve them. Removal of an obstruction complements being obstructed. Complementarity is directional and excludes transitions that would make the state worse. It is neither antonymy nor reversed valence. Nor does complementarity assert that Z resolves L; only verification settles that.

Two hypotheses follow.

- **Hypothesis R1 (realization)**: in the hard case, ranking by complementarity recruits resolving candidates at a rate at least κ > 1 times chance, independent of N, even with semantic similarity and non-appraisal relational similarity controlled.
- **Hypothesis R2 (transfer)**: the advantage persists for concerns and domains not met in training, whereas a relevance predictor trained on the content of past resolutions degrades.

The ground for R2 is that type spaces are shared across domains and types are assigned relative to the concern at retrieval, whereas a predictor trained on content is tied to the content distribution of its training domains.

A representation is an **appraisal representation** if it is (1) computed from concerns and history, (2) readable across content domains, and (3) directionally complementary from state types to improving transition types, depending on concerns. If it is (4) causally used to rank candidates, this is **complementary recruitment**. **Functional emotion** is then defined as the assembly that realizes roles (a), (b) and (c), with (b) carried by complementary recruitment, whether or not subjective experience is present. Mood-congruent retrieval, which recalls experiences of the same type, lacks the direction of complementarity and does not qualify even if it uses emotion types.

The paper's reason for calling this assembly emotion is that each role matches a function long attributed to emotion. The concern-relativity of (b) is central to appraisal theory (Frijda, Lazarus, Scherer). Role (a) matches recalcitrant emotions that persist against evaluative judgment (Brady). Role (c) matches control precedence, the tendency of emotion to direct action and resources ahead of other processes (Frijda).

**Conclusion 2 (functional emotion)**: in addition to Conclusion 1, if R1 and R2 hold and complementarity is coupled with actual resolution in the hard case, a system that keeps expanding its repertoire has a reason to possess functional emotion in addition to intelligence. Such a system keeps meeting new concerns and domains, where competitors learned from content degrade while realization by an appraisal representation keeps its advantage. This is a defeasible reason that depends on hypotheses and a premise about the world, not a necessity.

## Argument 3: A component-removal thought experiment

<p class="experiment-label">Argument 3</p>

<div class="setup">

**Setup**

- System F: all four elements of functional emotion (lack retention, appraisal representation, complementary recruitment, adoption budget) plus intelligence components (budgeted memory, embedding search, structural analogy, language-model goal generation, a scalar curiosity budget)
- Systems O-1 to O-4: F with one element removed each
- Scenario: an unresolved state of type "being obstructed" in Domain 1 (the pipeline); later, in content-unrelated Domain 2 (the loading dock), an experience Z of type "an obstruction being removed". Domain 2 also holds several distractors whose types are complementary but which do not resolve the lack
- Caveat: the thought experiment does not test R1 or R2; it grants them and shows the role of each element

</div>

<figure>
  <img src="/column-images/ssrn-functional-emotion-problem-discovery/thought-experiment-1600.webp" alt="Component-removal thought experiment" />
  <figcaption><strong>Figure 4.</strong> Outcome of the component-removal thought experiment (drawn from Sections 5.1 and 5.3 of the paper). In the hard case, removing any one element prevents Z from becoming a new problem. The recruitment cell for O-2 is marked not applicable because O-2 has no appraisal representation.</figcaption>
</figure>

When content is similar (for example, a lock release in another pipeline is logged next to the stalls), O-2 and O-3 can also recall Z through embedding search. The paper places this case outside the scope of its necessity claim.

In the hard case the systems diverge. O-1 does not sustain the lack, so there is nothing for Z to be linked to. O-2 cannot recognize complementarity, so the link is left to chance, at about BM/N. O-3 has appraisal types but does not use them for recruitment, so Z never comes to attention. O-4 recruits Z, but the utility estimate cannot justify verifying a match with no estimable contribution to any goal, and the curiosity budget goes to highly novel targets instead. Only F retains "being obstructed" with its type, recruits the complementary Z, checks the few recruited candidates one by one, and poses the problem of whether some jobs hold unused locks.

The paper itself cautions that this comparison retrieves what the hypotheses built in. The claim that the remaining components cannot substitute for a removed element rests on the analysis of alternative routes that follows.

## Argument 4: Other routes, and the parts current AI already has

<p class="experiment-label">Argument 4</p>

To play role (b) in the hard case, a route must at once use the unresolved state as one anchor, link content-unrelated experiences, and do so at a rate above chance.

<figure>
  <img src="/column-images/ssrn-functional-emotion-problem-discovery/routes-1600.webp" alt="Comparison of routes for role (b)" />
  <figcaption><strong>Figure 5.</strong> Routes that could play role (b) in the hard case (Table 1 of the paper). ✓ satisfies; ✗ does not satisfy; △ partially satisfies through descriptions of symptoms or traces of content; ↑ above chance; = at chance; ? untested competitor; — not applicable in the hard case. The "above chance" entry in the last row is an empirical assumption to be tested.</figcaption>
</figure>

A relevance predictor trained on past resolutions and schematization by a concern-conditioned language model are competitors that may meet all three requirements. The paper therefore does not conclude that complementary appraisal types are the only route in the table. What it concludes is that, among routes that may meet all three requirements, complementary appraisal types are the one that predicts transfer to new concerns and domains for a theoretical reason. If a language model's schematization meets the four criteria and is causally used for ranking, it counts as an implementation of functional emotion, however it was built.

<figure>
  <img src="/column-images/ssrn-functional-emotion-problem-discovery/ai-components-1600.webp" alt="Existing AI components versus the four elements" />
  <figcaption><strong>Figure 6.</strong> Major existing AI components and the four elements of functional emotion (Table 2 of the paper). The paper notes that judgments concern explicit components in typical designs; individual implementations and implicit realizations in weights may differ.</figcaption>
</figure>

EMA, an appraisal-based affect agent, represents appraisal types explicitly, but it appraises events against formulated goals and does not use the types to recruit memories. Emotion-aware retrieval brings back memories that match the current emotion, a computational analogue of mood-congruent memory, whereas the paper predicts that complementary rather than matching types carry the advantage. Interoceptive regulation can tell an agent that something is wrong but does not address how it might discover what the problem is.

The paper concludes that, at the level of explicit components, current AI lacks the wiring that connects the retention of pre-articulate lacks to complementary recruitment, even though the individual parts are becoming available. Whether large models already contain such representations in their weights is not settled by the argument; it is an empirical question for probing and intervention.

## Argument 5: How could the proposal be refuted?

<p class="experiment-label">Argument 5</p>

The paper separates two kinds of empirical premise: one about agents (R1 and R2) and one about the world, namely whether complementarity is coupled with actual resolution in real discovery. The latter is defined with a reference schema C*, separate from any agent's appraiser, as the difference ρ_w between the resolution probabilities of complementary and non-complementary candidate pairs. This separates the claim that an agent's advantage grows with ρ_w and vanishes at ρ_w = 0 from the claim that real discovery has ρ_w > 0.

<figure>
  <img src="/column-images/ssrn-functional-emotion-problem-discovery/predictions-1600.webp" alt="Relations among the six predictions" />
  <figcaption><strong>Figure 7.</strong> How the six predictions relate (drawn from Section 6.1 of the paper). Predictions (1), (2) and (5) each test the mechanism's advantage independently; (3) and (4) diagnose where that advantage comes from once (1) holds; (6) tests the self-binding argument independently of the mechanism.</figcaption>
</figure>

| Prediction | Supported if | Contradicted if |
|---|---|---|
| (1) Complementarity | complementary appraisal beats same appraisal, random selection, a valence-flip cue and a predictor without appraisal features | no advantage once semantic and relational similarity are controlled |
| (2) Transfer | the advantage persists with new concerns and domains while a content-trained predictor degrades | the advantage vanishes under domain shift |
| (3) Direction | swapping the roles of origin and resolving episodes removes the advantage | the advantage survives the swap |
| (4) Concern dependence | changing only the appraising concern changes recruitment | recruitment is unchanged |
| (5) World coupling | the advantage grows with ρ_w and vanishes at ρ_w = 0 | an advantage at ρ_w = 0, or no monotone relation |
| (6) Erosion | discovery declines once the delay between verification and payoff exceeds the optimizer's horizon, and an insulated budget prevents the decline | no decline in discovery |

(The six prediction rows of Table 3 of the paper.)

The paper also states explicit falsification conditions. If an agent lacking role (a) or (c) reliably discovers problems in the hard case, Conclusion 1 is refuted. If agents that match or beat the mechanism, including in new concerns and domains, contain nothing meeting the four criteria, Conclusion 2 loses its support. If ρ_w is near zero in natural records of discovery, the hard case offers appraisal nothing to exploit. A human experiment is also outlined; its prediction runs opposite to mood-congruent memory, which favors same-type pairs, and to the conjecture that analogical mapping is hindered for pairs of divergent valence.

## Argument 6: Subjectivity, Meno's paradox and self-binding

<p class="experiment-label">Argument 6</p>

Three philosophical consequences follow.

The first concerns **what cannot be borrowed**. The paper distinguishes three origins of valuation.

| Type | What it is | Examples |
|---|---|---|
| I: borrowed valuation | learned from human text and preferences, which mostly record what someone has already stated as a problem | goal generation that internalizes language and culture; reward models learned from human preferences |
| II: scalar native valuation | arises from the system's own experience, but does not indicate which experience bears on which lack | intrinsic motivation based on learning progress |
| III: typed native valuation | computed relative to the system's own concerns and history and used as the key for recruitment | functional emotion in this paper |

Borrowing a description of someone else's lack either borrows a problem (if it includes a resolution condition) or requires re-appraising it relative to the borrower's own concerns (if it does not). Either way, the appraisal type that drives recruitment comes from the borrower's own concerns and history. The paper therefore proposes a functional definition of subjectivity located in the origin of the appraisal rather than the origin of the lack. To the degree that concerns are learned from the agent's own history (Assumption S), subjectivity in this sense is a condition for posing problems beyond the human repertoire. The paper does not claim to resolve the hard problem of consciousness.

The second is an answer to **Meno's paradox**: how can one search for what one does not know? Even without knowing the resolution condition, one can feel the type of what is lacking. Because the type contains no content of the resolution, it can be matched against content-unrelated experiences, and the correspondence of types is the trigger for recognizing what fits. Posing a problem outside the repertoire becomes possible through coarse recruitment by type followed by verification by intelligence.

The third is **self-binding**. At the action level, the current utility estimate gives no reason to spend resources retaining unresolved states or verifying candidates with no estimable contribution to any goal. At the policy level, adopting a policy with such a mechanism can be justified. Under self-improvement that selects components one by one by current utility, however, functional emotion, and the adoption budget in particular, is gradually eroded. The paper treats this as an inconsistency between levels, a form of temporal inconsistency, argues that a self-binding mechanism must protect what was decided at the policy level, and makes the claim testable as prediction (6).

## What we found, and what remains open

The argument yields four results.

- Reliable problem discovery in the hard case requires three roles: retaining the unresolved state, a selection signal that relies on neither the resolution condition nor content similarity, and funding verification without support from utility. This is a conditional necessity under the premises.
- If appraisal complementarity realizes this signal and transfers to new concerns and domains, a system that keeps expanding its repertoire has a defeasible reason to possess functional emotion.
- The appraisal type of an unresolved state cannot be borrowed and arises from the system's own concerns and history. To the degree that concerns are learned from that history, subjectivity in this sense is a condition for posing problems beyond the human repertoire.
- Component-wise myopic self-improvement erodes this mechanism, so self-binding is needed. At the level of explicit components, current AI is acquiring the parts but lacks the wiring that connects them.

The paper lists seven limitations. It depends on functionalism, so meeting the criteria does not imply phenomenal pain or joy. R1, R2 and ρ_w > 0 have not been tested directly (Conclusion 1 survives if they fail). The list of alternative routes is not shown to be exhaustive. The assumption that appraisal type spaces are shared across domains may fail, and with it the core of Conclusion 2. How often the hard case occurs in real discovery is unknown. The bridge to surpassing humans depends on Premise H0. And how far concerns are the agent's own is a matter of degree.

This is a theoretical paper with no experimental data. It is available on SSRN as a preprint that has not been peer reviewed.
