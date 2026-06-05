---
title: "How to Use External LLM APIs Without Sending Your Sensitive Data"
date: "2026-06-05"
excerpt: "For GDPR-constrained organizations, the barrier to using cloud LLMs is not cost — it's the risk of sending confidential data externally. SharedRequest solves this with a batch-mixing approach that achieves 20%+ better utility than differential privacy while cutting query costs by up to 5x."
image: "/column-images/llm-privacy-preserving-shared-request.png"
imageAlt: "An abstract illustration of multiple prompts being mixed and sent to a cloud API with results returned securely"
readingMinutes: 5
basedOnPaper: "SharedRequest: Privacy-Preserving Model-Agnostic Inference for Large Language Models"
basedOnPaperUrl: "https://arxiv.org/abs/2606.05004"
---

Hello. This is Keito Inoshita from Affectosphere Group.

"We want to use ChatGPT or Claude for this workflow, but we cannot send customer data to an external server."

This constraint shows up constantly in conversations with enterprises in finance, healthcare, and legal services. The LLM capability is compelling. The use case is real. But GDPR, HIPAA, local privacy laws, or internal data governance policies make it impossible to route confidential data through cloud APIs.

A paper accepted at ACL 2026 (Peihua Mai, Xuanrong Gao, Youlong Ding, Xianglong Du, Wei Liu, Yan Pang et al., arXiv:2606.05004) offers a practical answer to this problem.

SharedRequest achieves 20%+ higher utility than differential privacy baselines while reducing query costs by up to 5x. And it requires no access to model parameters — meaning it works with any external LLM API, including OpenAI, Anthropic, and Google.

---

## Three takeaways for today

1. SharedRequest protects prompt privacy by mixing real and noise prompts in batches, making it impossible for the server to identify which request is genuine.
2. It outperforms differential privacy baselines by 20%+ on utility while cutting query costs by up to 5x.
3. It requires no model parameter access — so it applies to any external LLM API without modifications to the provider's system.

---

## ① The core idea: hide the real request in a batch

Standard LLM API usage is transparent from the provider's side. "Summarize this patient record: [full record text]" reveals exactly whose data is being processed and why.

SharedRequest reframes the problem. Instead of sending one real request and hoping the provider's privacy policies are sufficient, it sends a batch: the actual prompt mixed with semantically similar noise prompts. The server cannot determine which prompt in the batch is the real request.

This is batch-level anonymization, not per-prompt obfuscation. The individual prompt is not modified or degraded — it is hidden within a group. The utility of the response is preserved because the real prompt reaches the model intact. The privacy protection comes from indistinguishability within the batch.

A secondary benefit emerges from grouping semantically equivalent instructions: query costs are distributed across the batch, delivering the 5x cost reduction reported in the paper.

---

## ② Why this outperforms differential privacy

Differential privacy is the most studied approach to privacy-preserving data analysis. It works by adding carefully calibrated noise to data, making it statistically impossible to identify any individual.

The trade-off is fundamental: stronger privacy requires more noise, which degrades accuracy. Weaker noise preserves accuracy but provides weaker privacy. For language tasks, where the signal is subtle and semantic precision matters, this trade-off is particularly painful.

SharedRequest sidesteps this trade-off. Rather than degrading the quality of individual prompts, it introduces uncertainty at the level of attribution — "which prompt belongs to which user" — without touching the content of any individual prompt.

The 20%+ utility improvement over differential privacy baselines reflects this structural advantage. Higher quality outputs from the same privacy protection budget.

---

## ③ Where enterprises can use this now

The "model-agnostic, no parameter access required" property is the most important implementation detail.

Organizations do not need to run their own infrastructure or negotiate special access with LLM providers. SharedRequest sits as a middleware layer between internal systems and external APIs. The interface to existing workflows does not change. The provider API call is the same. The privacy protection is in the preprocessing step.

Three concrete scenarios where this matters:

Law firms reviewing client contracts with AI assistance. Client names and matter details cannot be sent to external cloud systems under most confidentiality obligations. A SharedRequest layer that mixes the real contract review prompt with noise prompts of similar structure could allow LLM-assisted review without identifiable client data reaching the provider's servers.

Healthcare systems generating clinical documentation. Physician note summarization and clinical documentation assistance are high-value LLM use cases. Patient identifiers in the input make these workflows legally complex. Batch anonymization that removes the attribution link while preserving input quality opens these workflows up.

Financial institutions analyzing customer interaction data. Customer service logs containing account information, transaction history, and advisory conversations hold significant analytical value for CX improvement. Privacy-preserving inference enables that analysis with lower regulatory risk.

The 5x cost reduction also matters in high-volume scenarios. If an organization is routing thousands of queries per day through an external API, reducing that to one-fifth of the cost while maintaining quality and adding privacy protection is a strong operational argument.

---

## A design principle for LLM workflows under privacy constraints

SharedRequest is currently a research contribution rather than a packaged enterprise product. Operational deployment would require implementation work.

But the underlying design principle applies today. When building any LLM workflow that touches sensitive data, explicitly designing the "what goes into the prompt" question — minimizing PII, introducing pre-processing anonymization, separating identifiers from content — significantly reduces legal and reputational risk at low engineering cost.

SharedRequest extends this principle to a more rigorous level. As the regulatory environment around AI and personal data continues to tighten, organizations that have already designed privacy-aware LLM pipelines will have a meaningful operational advantage.

That's it for today!

---

## Reference

1. Peihua Mai, Xuanrong Gao, Youlong Ding, Xianglong Du, Wei Liu, Yan Pang (2026). *SharedRequest: Privacy-Preserving Model-Agnostic Inference for Large Language Models*. ACL 2026.

<p class="ai-notice"><small>* This article was written in part with AI assistance and may contain inaccuracies.</small></p>
