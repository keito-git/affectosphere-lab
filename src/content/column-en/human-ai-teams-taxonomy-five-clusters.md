---
title: "\"Human-AI Collaboration\" Is Actually Five Different Things — The Taxonomy That Exposes an AI Deployment Blind Spot"
date: "2026-07-06"
excerpt: "A systematic analysis of 53 papers reveals five qualitatively distinct human-AI team clusters — and shows that researchers using the same phrase \"human-AI teaming\" often mean entirely different team dynamics. Here's what that means for enterprise AI deployment design."
image: "/column-images/human-ai-teams-taxonomy-five-clusters.png"
imageAlt: "A flat illustration of five distinct team types. Diagrams showing different distributions of autonomy and decision-making authority"
readingMinutes: 5
basedOnPaper: "What Types of Human-AI Teams Exist?"
basedOnPaperUrl: "https://arxiv.org/abs/2607.02198"
---

Hello. This is Miura from Affectosphere Group.

"We've deployed AI" — a sentence that comes up constantly in organizational conversations these days.

But when you dig into what that actually means, the specifics are radically different from one organization to the next. In some cases, AI automatically produces reports and humans check the outputs. In others, AI is a tool that assists human judgment but holds no decision-making authority. In others still, humans and AI participate roughly equally in decisions. And in some, whole groups of humans and AI systems collaborate in interlocking ways.

The phrase "AI deployment" covers all of these. But they are not the same thing. The team dynamics, accountability structures, and design requirements are fundamentally different in each case.

A study published on arXiv (Hughes & Habli, arXiv:2607.02198) takes this problem seriously. The authors systematically analyzed 53 papers on human-AI teaming and identified five distinct team clusters — each qualitatively different in how autonomy is distributed, where decision-making authority sits, and what form interdependence takes.

---

## Today's 3 Points

1. Analysis of 53 papers identified five human-AI team clusters that differ qualitatively in autonomy distribution, decision-making authority, and interdependence form.
2. The research reveals a comparability problem: studies using the phrase "human-AI collaboration" are often describing entirely different team dynamics.
3. The five-cluster framework is directly applicable as an enterprise AI deployment assessment tool.

---

## The Problem of Words Meaning Different Things

Research on human-AI teaming has grown rapidly in recent years. But accumulating and comparing findings across studies has been difficult — for a structural reason.

The phrase "human-AI collaboration" means different things to different researchers. One study investigates AI that handles everything automatically while humans review results. Another studies a pair where human and AI jointly participate in decision-making. A third looks at complex multi-human, multi-AI coordination structures. These are not variations of the same phenomenon. They are qualitatively different team types, answering qualitatively different questions.

Comparing them under the same label produces noise, not insight.

Hughes and Habli's research addresses this directly. By systematically analyzing 53 papers, they mapped what types of human-AI teams actually exist in the literature — and found that five clusters, with meaningfully different characteristics, cover the space.

---

## Five Team Clusters

The five clusters differ along three key dimensions: autonomy distribution, decision-making authority, and interdependence form.

The first is the "AI Assistant" type. AI handles specific tasks automatically, and humans supervise and approve the outputs. The AI plays a supplementary role; humans retain final decision-making authority. This is what most organizations are actually building when they say they've "deployed AI."

The second is "Ad-hoc Dependency." Humans call on AI when they feel they need it — an unstructured, opportunistic collaboration. There's no systematic process for when to engage AI; it's up to the human's in-the-moment judgment. The hallmark is ad-hoc, non-planned use.

The third is "Ad-hoc Forced Dependency." This is where humans find themselves de facto following AI recommendations, even when they nominally have override authority. The AI output becomes the default, and the cost of deviating from it — cognitively, organizationally, or practically — is high. This is where automation bias problems most commonly emerge. On paper, humans are in control; in practice, they're deferring.

The fourth is "Peer Balance." One human and one AI collaborate on roughly equal footing. Decision-making is distributed between them, and each references the other's judgment. This type requires the most sophisticated design of autonomy-sharing — it can't be left implicit.

The fifth is "Group Balance." Multiple humans and multiple AIs function as a team. Role distribution, information sharing, and decision-making are designed at the team level, and interdependence takes its most complex form.

These five are not ranked by quality. Each is appropriate in different contexts and demands different design considerations.

---

## What the Taxonomy Reveals About Comparability

One of the taxonomy's key insights is that comparing teams of different types using the same metrics is misleading.

Consider studies measuring "accuracy in human-AI collaboration." In the AI Assistant type, accuracy means the precision of outputs after human review of AI-generated results. In the Peer Balance type, it means the precision of decisions that emerged from mutual human-AI deliberation. These are different decision processes. The number produced by each study cannot be straightforwardly compared.

The same logic applies to productivity gains. An improvement measured in an AI Assistant deployment says nothing about what a Peer Balance deployment will produce. Transferring the finding requires knowing which team type the original study examined.

This taxonomy provides researchers with a shared vocabulary for making that explicit: "our study examines the Peer Balance cluster." Once the cluster is specified, comparisons become interpretable and cumulative knowledge becomes possible.

---

## Using the Framework as a Deployment Assessment Tool

Now for the business application.

A problem common to many enterprise AI deployments is that "what to deploy" gets decided before "what kind of team to build." The tool gets chosen, and then someone asks "so how are we actually going to use this?"

The taxonomy suggests a better sequence. If you first decide which team type you're aiming for, the downstream decisions — tool selection, decision process design, responsibility allocation, and evaluation metrics — follow more naturally.

Say a CHRO or talent development team decides: "We're targeting the Peer Balance type." The design questions become concrete. How do we weight human versus AI judgment in specific decisions? What's the process when a human wants to override AI's recommendation? What level of AI explainability do we need to make that override decision meaningful? What do we measure — AI performance alone, or the human-AI pair as a unit?

These questions emerge from the team type choice. Without specifying the type, they remain vague.

The "Ad-hoc Forced Dependency" cluster deserves special attention for enterprise settings. This is the type where AI deployment appears successful — the AI is being used, decisions are being made — but a hidden accountability problem is accumulating. Humans are nominally responsible but are functionally following AI defaults. From a governance and audit standpoint, this is the highest-risk configuration.

Regularly assessing whether your AI deployment is drifting into this cluster — even unintentionally — is a governance practice worth building in.

---

## A Tool for Management, Legal, and HR Alignment

In enterprise AI adoption, the hardest alignment challenge is typically between management, legal, and HR on two questions: "what level of human oversight is required?" and "where does accountability sit?"

Does "AI made the decision" meaningfully reduce human responsibility? Who bears liability when AI-assisted decisions go wrong? Can employees decline to follow AI recommendations? If they don't, and the AI was wrong, who is accountable?

This taxonomy can serve as shared language for those conversations. "We are building an AI Assistant configuration, where humans always hold final decision-making authority" is a clearer design commitment than vague statements about "keeping humans in the loop." Conversely, moving toward Peer Balance requires explicit agreement on how responsibility is divided — and the framework gives the parties a common structure for that conversation.

As AI agents become more prevalent in enterprise settings, being specific about which team cluster a given agent configuration represents will become a core part of accountability design. Deploying an agent without answering "is this AI Assistant, Ad-hoc Dependency, or Peer Balance?" leaves the accountability structure undefined.

Making it possible for CHROs, IT leads, and legal teams to reference the same framework in the same conversation — that's the practical value this taxonomy delivers.

---

## "What Kind of Team Will We Be?" Is the Right Question

In AI deployment discussions, attention naturally flows toward tool capabilities and model performance. Those matter.

But the more important question is: when this AI is deployed, what does our team actually look like? How is autonomy distributed between humans and AI? Where does decision authority sit? What form does interdependence take?

The five-cluster framework gives organizations vocabulary to answer those questions concretely — not just for researchers designing studies, but for practitioners designing workplaces.

"Human-AI collaboration" is not one thing. When you're precise about which of the five types you're building, the design choices, accountability structures, and evaluation metrics follow. The work of AI deployment gets more tractable when you know which team you're actually trying to create.

---

## Reference

1. Nathan Hughes, Ibrahim Habli (2026). *What Types of Human-AI Teams Exist?*. arXiv preprint.

<p class="ai-notice"><small>* This article was written in part with AI assistance and may contain inaccuracies.</small></p>
