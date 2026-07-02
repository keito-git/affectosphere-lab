---
title: "What Happens When You Connect All Your Business Tools to an LLM: Five MCP Server Patterns and the Tool Explosion Trap"
date: "2026-06-30"
excerpt: "A study analyzing 15 MCP server implementations extracts five architecture patterns — and quantitatively shows that tool selection accuracy drops significantly once the number of tools crosses a certain threshold. Here's what this means for enterprise AI design."
image: "/column-images/mcp-server-architecture-patterns-llm-integrated-applications.png"
imageAlt: "Flat illustration showing multiple business systems connecting to an LLM through MCP servers"
readingMinutes: 5
basedOnPaper: "MCP Server Architecture Patterns for LLM-Integrated Applications"
basedOnPaperUrl: "https://arxiv.org/abs/2606.30317"
---

Hello. This is Keito Inoshita from Affectosphere Group.

"Let's just connect everything." You've probably heard this in a planning meeting.

ERP, CRM, document management, communication tools — if the LLM can reach all of them, natural language should handle every workflow. Organizations moving toward this vision are running into the same wall: how do you actually structure these connections?

MCP (Model Context Protocol), standardized by Anthropic, provides a common way to link LLMs with external tools. But until now, there was no organized body of knowledge on how to architect those connections well.

A June 2026 study (Rodrigues & Vas, arXiv:2606.30317) addresses exactly this. Analyzing 15 independently developed MCP server implementations, the authors identify and systematize five architecture patterns — derived inductively from real-world code, not prescribed in advance.

And along the way, they uncover something that should reshape enterprise AI design: what happens when you add too many tools.

---

## Three things this article covers

- MCP server implementations fall into five architecture patterns, each with its own appropriate use cases and design pitfalls
- Tool selection accuracy in Claude models drops notably once the number of available tools crosses a threshold — shown quantitatively
- Cross-cutting concerns like authentication and observability are what make or break production stability

---

## ① The Five Patterns

The study identifies five distinct MCP server architecture patterns.

Resource Gateway mediates access to data and documents. File systems, databases, cloud storage — any "source of information" that needs to be surfaced to an LLM.

Tool Orchestrator controls complex workflows that combine multiple tools. It appears when a single request requires multiple actions executed in sequence.

Stateful Session Server maintains session state. Browser automation and multi-step interactions that need to remember context across turns fit here.

Proxy Aggregator consolidates multiple underlying MCP servers behind a single interface. When an organization has many MCP servers running independently, this pattern provides a unified management layer.

Domain-Specific Adapter translates a particular business domain into LLM-friendly representations. ERP APIs and CRM data structures get converted into tool definitions the model can reason about.

---

## ② Why Pattern Classification Matters

The instinct is to register every available API as a tool and let the model figure it out. In practice, this causes a specific and measurable problem.

One of the most significant findings in this study is the relationship between tool count and accuracy. Once the number of tools exceeds a certain threshold, Claude's tool selection accuracy drops in a way that is quantitatively observable.

Intuitively, this makes sense. Present a person with twenty buttons labeled in similar ways and decision quality degrades. LLMs behave similarly — too many options raises the probability of calling the wrong tool.

This is precisely why pattern classification is useful. A Proxy Aggregator lets you bundle many underlying tools while limiting what the LLM actually sees. A Domain-Specific Adapter partitions tool sets by business domain, keeping any single context window manageable.

---

## ③ The Anti-Pattern Perspective

Beyond the five positive patterns, the study also catalogs common anti-patterns — designs that are frequently implemented but cause problems down the line.

One recurring issue is tool granularity. A single multipurpose "do anything" tool seems convenient, but it degrades the model's ability to select correctly. Small, single-purpose tools perform better — until you have so many of them that you hit the tool count problem again. Managing this tension is central to MCP server design.

Inconsistent authentication is another anti-pattern. When each tool handles its own credentials independently, error handling becomes a tangle. Consolidating authentication at the MCP server layer keeps individual tools simple and the system consistent.

---

## ④ Cross-Cutting Concerns: Authentication and Observability

The study places particular emphasis on concerns that cut across all five patterns rather than belonging to any single one.

For authentication, a unified approach at the MCP server layer is recommended. Individual tool-level credential management does not scale.

Observability becomes critical in production. Without tracking which tools were called, what the response times looked like, and where errors occurred, debugging becomes guesswork.

LLM-based systems behave probabilistically — the same input may invoke different tools across runs. That non-determinism makes rich logging essential, not optional. "What is actually happening" needs to be answerable from logs, not inferred.

---

## ⑤ An Implementation Proposal for Enterprise Contexts

Consider a mid-size IT company running multiple SaaS products — ERP, CRM, project management, and document management — that wants to connect all four to an LLM agent.

Start with Domain-Specific Adapters for each system. ERP business logic and CRM data structures are fundamentally different, so each deserves its own translation layer that maps domain vocabulary into tool definitions the model can use.

On top of those, deploy a Proxy Aggregator. This is where you control what the LLM sees. Focus the exposed tool set on the workflows you actually expect to run: inventory queries from ERP, customer lookups from CRM, document search. The goal is to keep the visible tool count within the range where selection accuracy stays high.

For KPIs, track two things: tool selection accuracy rate (did the model call the tool that matched the user's intent?) and task completion rate. Monitor how these shift as you adjust the tool set, and tune the configuration weekly.

---

## Conclusion

As MCP adoption grows, the question of how to structure connections between LLMs and business tools is becoming a first-class design concern.

This study's message is that connection is not a technical task to be executed — it is an architecture decision to be made. Choosing among five patterns based on context, respecting the tool count ceiling, and handling cross-cutting concerns deliberately: these design choices determine whether LLM agents work at production-grade accuracy or frustrate users with wrong-tool invocations.

The shift is from "connect everything" to "design the connection." That distinction is what this research makes concrete.

---

## Reference

1. Rodrigues, Carson, & Vas, Oysturn. (2026). *MCP Server Architecture Patterns for LLM-Integrated Applications*. arXiv preprint (2026).

<p class="ai-notice"><small>* This article was written in part with AI assistance and may contain inaccuracies.</small></p>
