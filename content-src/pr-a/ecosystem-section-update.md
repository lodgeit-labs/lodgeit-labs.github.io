# Ecosystem section update — copy + repo-description checklist

Purpose: the site currently surfaces 2 of 13 public repos (`brain-pattern`, `clawdog`). Seven public integration kits are invisible from the customer-facing site. This file supplies (A) replacement Ecosystem section copy grouping the real public surface, and (B) proposed one-line GitHub descriptions for repos that lack one, so the ecosystem page and the org page tell the same story.

---

## A. Ecosystem section copy (replaces the current two-card section)

### The reasoning substrate

**[Logical English](https://github.com/lodgeit-labs/LogicalEnglish)** — executable statute: legal and domain rules written in controlled natural language that compile to deterministic constraint logic. One text a lawyer can read and a machine can run. *(LodgeiT staging fork: [LogicalEnglish-LodgeiT](https://github.com/lodgeit-labs/LogicalEnglish-LodgeiT).)*

**[FOL_solvers](https://github.com/lodgeit-labs/FOL_solvers)** — research substrate: logic programming and knowledge-representation experiments underpinning the deterministic layer.

**[brain-pattern](https://github.com/lodgeit-labs/brain-pattern)** — the public methodology: how an AI agent's memory is kept honest with cryptographic integrity, append-only ledgers, coherence audits and receipts. The discipline behind everything else on this page.

### The agent surface

**[clawdog](https://github.com/lodgeit-labs/clawdog)** — the neurosemantic accounting engine: LLM flexibility in front, SWI-Prolog rigor behind, zero-hallucination outputs where it counts.

**[clawdog-mcp-server](https://github.com/lodgeit-labs/clawdog-mcp-server)** — MCP access to LodgeiT tools: point any MCP-capable agent at the calculator constellation.

**[clawdog-kit](https://github.com/lodgeit-labs/clawdog-kit)** — agent-driven AU tax and accounting calculator kit with CSV templates: the fastest way to run the calculators yourself.

### Integration kits

**[clawdog-calculator-api](https://github.com/lodgeit-labs/clawdog-calculator-api)** — the Calculator-Constellation REST API.

**[clawdog-calculator-api-integration-kit](https://github.com/lodgeit-labs/clawdog-calculator-api-integration-kit)** — client-side integration kit for the REST API.

**[clawdog-widget-renderer](https://github.com/lodgeit-labs/clawdog-widget-renderer)** — schema-driven HTML widget renderer for calculator surfaces.

**[fano-classifier-integration-kit](https://github.com/lodgeit-labs/fano-classifier-integration-kit)** — integration kit for the Fano classifier (account classification with a deterministic firewall).

**[report-generator-frs-105](https://github.com/lodgeit-labs/report-generator-frs-105)** — FRS 105 report generation kit (UK micro-entity accounts).

---

## B. Repo-description checklist (GitHub-side, PR-D or done in passing)

These are proposed one-liners for the org admin to set. Repos not listed already have adequate descriptions.

| Repo | Current description | Proposed |
|---|---|---|
| `clawdog` | *(none)* | Neurosemantic accounting engine — LLM front-end, SWI-Prolog deterministic core, zero-hallucination SBRM outputs |
| `LogicalEnglish` | *(none)* | Executable statute: controlled-natural-language rules that compile to deterministic constraint logic |
| `lodgeit-labs.github.io` | *(none)* | lodgeit.org — LodgeiT Labs: open-source financial infrastructure, scene protocol, bounty programme |

Note for reviewer (Andrew): descriptions are public metadata — one glance for accuracy is the whole review.
