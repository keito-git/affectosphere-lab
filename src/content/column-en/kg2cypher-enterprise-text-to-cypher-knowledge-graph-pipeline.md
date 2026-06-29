---
title: "When Anyone in the Office Can Query the Knowledge Graph: What KG2Cypher Means for Enterprise Data Access"
date: "2026-06-29"
excerpt: "A data-centric pipeline that automatically generates Text-to-Cypher training data from the knowledge graph itself. KG2Cypher achieves 95.2% exact match execution accuracy and 99.9% execution rate — bringing self-service KG access within reach for non-engineers."
image: "/column-images/kg2cypher-enterprise-text-to-cypher-knowledge-graph-pipeline.png"
imageAlt: "Natural language questions being converted into Cypher query paths on a graph, returning structured answers"
readingMinutes: 5
basedOnPaper: "KG2Cypher: Data-Centric Pipeline for Building Enterprise Text-to-Cypher Systems"
basedOnPaperUrl: "https://arxiv.org/abs/2606.27742"
---

In many organizations, this situation is quietly playing out right now.

The data team has spent months building a knowledge graph — employee records, org structures, client relationships, product hierarchies, all modeled as nodes and edges in a graph database. Neo4j is running. The schema is clean. The data is there.

And the only people who can actually use it are the engineers who know how to write Cypher.

An HR manager who wants to find every employee who worked on a particular project over the past three years has to file a request with the data team and wait. A sales rep who wants to identify clients with overlapping touchpoints across two product lines faces the same bottleneck. The knowledge graph is, in practical terms, invisible to the people whose decisions it was built to inform.

This is not a data quality problem. It is an access layer problem. And it is more common than most organizations care to admit.

A June 2026 preprint from a research team at Korea presents a systematic approach to closing that gap — a pipeline called KG2Cypher that enables non-engineers to query a knowledge graph using natural language, with execution accuracy high enough to consider for real deployment.

---

## Three things this article covers

- What KG2Cypher's data-centric pipeline does and why automatically generating training data from the knowledge graph itself is the key design insight
- The numbers: 95.2% exact match execution accuracy, 99.9% execution rate, and F1 score of 0.964 across 11-class enterprise settings
- What HR teams, sales teams, and IT departments should take from this as a roadmap for self-service analytics on graph data

---

## ① The problem that Text-to-Cypher is actually solving

Graph databases like Neo4j are excellent at representing complex, interconnected enterprise data. The relationship between a client, the account manager who handles them, the products they have purchased, and the competitors they have also evaluated — all of that is naturally represented as a graph.

The query language for Neo4j is called Cypher. It is powerful and reasonably readable once you know it. But learning it requires time, and the population of people in most companies who have done so is small. That population is almost entirely in engineering or data roles.

The result is a structural inequality in data access. The knowledge graph holds answers. But the number of people who can ask it questions is artificially constrained by a language barrier.

Text-to-Cypher addresses this at the interface level. Rather than teaching non-engineers to write Cypher, it builds a system that translates natural language questions into valid Cypher queries automatically. The user types a question in plain English. The system converts it to Cypher, executes the query against the knowledge graph, and returns the result.

The idea is not new. What makes KG2Cypher notable is the approach it takes to a problem that has blocked practical deployment of Text-to-Cypher in enterprise settings: where do the training examples come from?

---

## ② The pipeline that works backward — generating training data from the graph itself

Building a Text-to-Cypher system requires a large set of examples pairing natural language questions with their correct Cypher queries. In research settings, these datasets are hand-crafted by domain experts. In enterprise settings, that is rarely feasible. Creating thousands of question-query pairs manually is expensive, time-consuming, and requires both domain knowledge and Cypher fluency simultaneously.

KG2Cypher solves this by inverting the process.

Instead of starting from questions and writing queries to match them, the pipeline starts from the knowledge graph itself. It works in four stages.

First, it traverses the knowledge graph and extracts graph facts — actual relationships between entities as they exist in the data. From these, it generates syntactically valid Cypher queries automatically. Each query is a real question the graph can answer because it was derived from the graph's own content.

Second, it passes each Cypher query to an LLM with a prompt that asks the model to generate a natural language question that the query would answer. This is the step that produces the human-language side of each training pair.

Third, the generated pairs are validated — the Cypher is executed against the graph to confirm it produces correct results, and the natural language is checked for quality. Pairs that fail validation are discarded.

Fourth, the validated pairs become training data. A Text-to-Cypher model is fine-tuned on this corpus, learning to convert natural language into Cypher for the specific schema and entity vocabulary of that organization's knowledge graph.

The elegance of this approach is that the training data is automatically grounded in the organization's actual data. There is no need to import an external benchmark dataset that uses a different schema. The system learns the vocabulary, the relationship types, and the naming conventions of the specific graph it will query.

This data-centric design is what makes enterprise deployment tractable. The pipeline is largely automated, and the quality of the training data scales with the quality of the underlying knowledge graph rather than with the time investment of domain experts.

Several additional technical components strengthen the accuracy of the final system. Schema prompting provides the LLM with structural information about the knowledge graph — node types, relationship types, property names — so the model has the context it needs to generate valid Cypher. Entity linking maps surface forms in the user's question to the canonical entity names in the graph, handling the common situation where the same entity is referred to in multiple ways. Specialized reasoning strategies address the structural complexity of multi-hop queries that require traversing several relationships to reach the answer.

---

## ③ What the numbers show

The evaluation in the paper covers 11 enterprise settings — a level of diversity that reflects the range of schema designs and data characteristics organizations actually encounter, rather than a single clean benchmark.

Across these settings, the system achieves 95.2% exact match execution accuracy. This measures the proportion of generated Cypher queries that produce exactly the correct result set, matching the ground truth answer. Reaching this level across 11 distinct enterprise configurations is the figure that most directly reflects real-world deployment potential.

The execution rate is 99.9%. This measures the proportion of generated Cypher queries that execute without errors. A query that is syntactically invalid or refers to entity names that do not exist in the graph will fail at execution time, returning no result rather than a wrong result. An execution rate this close to 100% means the system is reliable enough to present to non-engineers who would not know how to interpret or debug a query error.

The F1 score across the evaluation is 0.964. This measures the balance between precision and recall in retrieving the correct entities and relationships from the graph in response to a query.

Taken together, these figures suggest a system that has moved past the level where accuracy is the limiting factor. A 95% correct execution rate means roughly one in twenty queries returns an incorrect answer. Whether that is acceptable depends on the use case — but for self-service exploration and reporting tasks where results can be spot-checked, it is within the range that practical systems operate.

The more significant figure for enterprise adoption may be the 99.9% execution rate. When a non-engineer uses a system like this, their primary experience of failure is not a wrong answer — it is a system that does nothing, returns an error, and offers no explanation. A near-perfect execution rate means the system responds meaningfully to nearly every query, even when the answer requires refinement.

---

## ④ How this changes work for HR and sales teams

The practical implications of these accuracy levels become clearer when mapped to specific use cases.

For HR teams managing a people knowledge graph, the change is substantial. Consider the queries that currently require data team involvement: finding employees with specific combinations of skills, tenure, and project history; identifying candidates for internal mobility based on experience profiles; mapping reporting structures and team compositions across organizational changes. These are pattern-matching queries on structured data — precisely what a knowledge graph and a Text-to-Cypher interface are designed to handle.

With a system like KG2Cypher deployed, an HR business partner could type: "Show me people in the engineering division with at least four years of experience who have worked on client-facing projects in the last two years and speak Japanese." The system converts this to Cypher, executes it against the people graph, and returns the matching records — without a data team in the loop.

The time implications are significant. Requests that currently take days to fulfill, through the cycle of submitting a data request, waiting for queue position, receiving results, and iterating if the query was not quite right, compress to seconds. The HR team can iterate the question in real time rather than waiting for each revision to complete.

For sales teams working with a CRM or client relationship knowledge graph, the same dynamic applies to a different class of queries. Multi-condition searches — clients in a particular industry segment, above a certain revenue threshold, with active contracts expiring within six months, who have not yet been introduced to a new product line — are cumbersome to construct in most CRM interfaces. They are natural to express in free-form language.

A Text-to-Cypher interface lets a sales rep explore their territory as they think about it, in the language they use to describe their accounts, without having to translate their mental model into filter dropdowns and boolean toggles. The knowledge graph holds the answer. The interface removes the translation burden.

---

## ⑤ Measuring the impact and navigating the implementation conditions

When planning a deployment of a system like this, two KPIs are particularly useful for tracking whether the intended value is materializing.

The first is the rate of self-service data access by non-technical staff. A practical proxy: count the number of data requests submitted to the engineering or data team per month before deployment, then track how that number changes after the Text-to-Cypher interface goes live. If the interface is working as intended, the volume of intermediated requests should decrease as users handle more queries themselves. The delta between those two numbers is a measure of the access gap the system is closing.

The second is time-to-answer for ad hoc queries. Before deployment, the cycle time from "I have a question about the data" to "I have the answer" includes queue time, specification time, and iteration time. After deployment, it should be close to the execution time of the query itself. The reduction is a concrete productivity figure that can be mapped to specific business functions.

Implementation requires attending to a few conditions that the system depends on.

Knowledge graph quality is foundational. The training data pipeline works by generating query-question pairs from the graph's own content. If the graph contains inconsistent entity names, stale data, or structural irregularities, the training data will reflect those inconsistencies, and accuracy will suffer. Before deploying KG2Cypher, the organization needs a clear picture of the current state of its knowledge graph and a plan for the data quality work that may be needed to make it a reliable training source.

Entity normalization deserves particular attention. In enterprise knowledge graphs, the same real-world entity — a person, a company, a product — often appears under multiple names. An employee might be represented as "Kenji Watanabe," "K. Watanabe," and "Watanabe Kenji" in different systems that fed data into the graph. The entity linking component of KG2Cypher can help with this, but only up to a point. Systematic deduplication and normalization before deployment will directly improve the system's ability to match natural language references to graph entities.

The choice of LLM backend carries governance implications that IT and legal teams need to weigh in on. If the Text-to-Cypher system routes queries — which contain references to internal entities, employee names, client names, and product identifiers — through an external LLM API, then those queries are subject to the privacy policies of the API provider. For many organizations, this is a blocker. The alternative is running the LLM component on infrastructure the organization controls — either on-premises or in a private cloud environment. This adds operational complexity but removes the data residency concern. The right answer depends on the sensitivity of the data in the knowledge graph and the organization's existing policies on external AI services.

---

## The reframe worth taking away

Most of the public conversation about LLMs in enterprise settings focuses on chatbots and content generation. These are real use cases, but they sit at the surface of what the technology can do.

What KG2Cypher points toward is something more structural: LLMs as translation layers that make existing data infrastructure accessible to people who currently cannot use it. The knowledge graph already exists. The data is already there. The accuracy needed to make the interface reliable is now within reach. What changes is who can ask questions.

This is what data democratization actually means in practice — not the aspiration, but the mechanism. It is not about building new data pipelines or democratizing access to raw data lakes. It is about removing the language barrier between the people who have questions and the systems that hold the answers.

The 95.2% execution accuracy figure is not the ceiling. It is a floor — a demonstration that the problem is tractable at enterprise scale with current techniques. The direction from here is more coverage, better entity handling, and tighter integration with specific knowledge graph schemas.

For data teams who have invested in knowledge graph infrastructure and are looking for the next step, Text-to-Cypher is a concrete path from "we have the data" to "everyone who needs it can use it." That shift is worth taking seriously.

---

## Reference

1. Minjun Choi, Yerin Kim, Junghyuk Seo, Sujin Mo, Hyemin Lee, Youngjoong Ko (2026). *KG2Cypher: Data-Centric Pipeline for Building Enterprise Text-to-Cypher Systems*. arXiv preprint. https://arxiv.org/abs/2606.27742

<p class="ai-notice"><small>* This article was written in part with AI assistance and may contain inaccuracies.</small></p>
