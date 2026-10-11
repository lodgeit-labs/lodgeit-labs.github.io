---
brief_id: bounty-13-coal-lsl-levy
bounty_title: "Coal LSL levy — statute-to-calculator review"
statutory_anchors: "s 3B Coal Mining Industry (Long Service Leave) Payroll Levy Collection Act 1992; Coal Mining Industry (LSL) levy regulations"
reviewer:
  name: ""
  credential_class: ""        # CA / CTA / CPA / FIPA / MIPA / TPB
  registration_status: ""     # active / lapsed / retired
  jurisdiction: "Australia"
  attribution_posture: "named"  # named | initialled | anonymous
reviewed_calculator_version: ""  # copy from brief — e.g. source 53ba9b8 (v0.4.0), code_revision from a live response
submission_date: ""              # YYYY-MM-DD
top_level_verdict: ""            # ACCEPT / REJECT / FIX
verdict_hash: ""                 # (we compute this on receipt)
---

# Reviewer Verdict — Coal LSL levy — statute-to-calculator review

**Bounty:** bounty-13-coal-lsl-levy
**Target:** `urn:sbrm:calculator:coal-lsl:levy` — external contributor (Ryan Duguid,
<https://duguid.com.au/>), hosted at
`https://coal-lsl-levy.coal-lsl-levy-service.workers.dev`, source pinned at `53ba9b8` (v0.4.0).

## 1. Top-level verdict

_Choose one: **ACCEPT** / **REJECT** / **FIX**._

- **ACCEPT** — the calculator's statute-to-predicate translation is correct on the facts of the brief. A passing verdict lifts the attestation tier from `conformance-passed` to `practitioner-attested`.
- **REJECT** — the calculator's translation is materially wrong. State the section/regulation authority you rely on.
- **FIX** — the translation is mostly correct but has a specific error that can be fixed with a targeted change. Describe the fix.

**Your top-level verdict:**

---

## 2. Per-question verdicts

```yaml
per_question_verdicts:
  - question_number: 1   # levy rate (verify 2.7%)
    verdict: ""              # ACCEPT / REJECT / FIX
    citation_authority: ""   # levy regulation + rate for the period(s)
    reasoning: |
      # Confirm or correct the 2.7% rate for Jan 2024 – Aug 2026. Cite the instrument.
    edge_case_notes: |
  - question_number: 2   # Formula A vs Formula B, greater-of
    verdict: ""              # ACCEPT / REJECT / FIX
    citation_authority: ""   # s 3B(1)
    reasoning: |
    edge_case_notes: |
  - question_number: 3   # allowances / expense-reimbursement carve-out
    verdict: ""              # ACCEPT / REJECT / FIX
    citation_authority: ""   # s 3B(1)(b)
    reasoning: |
    edge_case_notes: |
  - question_number: 4   # salary sacrifice + bonus frequency
    verdict: ""              # ACCEPT / REJECT / FIX
    citation_authority: ""   # s 3B(4)(a),(aa),(b),(c),(d)
    reasoning: |
    edge_case_notes: |
  - question_number: 5   # rounding choice (LOAD-BEARING)
    verdict: ""              # ACCEPT / REJECT / FIX
    citation_authority: ""   # Act / regulation / return practice
    reasoning: |
      # Is a single final half-up rounding correct for a levy return? If not, state the prescribed treatment and the divergence.
    edge_case_notes: |
  - question_number: 6   # scope + monthly boundaries (OPEN-ENDED)
    verdict: ""              # ACCEPT / REJECT / FIX
    citation_authority: ""
    reasoning: |
    edge_case_notes: |
```

---

## 3. Citation audit

_List every statutory section or regulation the calculator/brief relies on. Mark each:
✓ correct citation / ✗ wrong citation / ⚠ citation exists but is misapplied._

| # | Authority as cited | Your assessment | Notes |
|---|---|---|---|
| 1 | s 3B(1) — Formula A / Formula B |  |  |
| 2 | s 3B(2) — annual salary branch |  |  |
| 3 | s 3B(3) — casual branch |  |  |
| 4 | s 3B(4) — salary sacrifice / bonus frequency |  |  |
| 5 | Levy rate (2.7%) — levy regulation |  |  |

---

## 4. Edge cases surfaced

_Anything the brief did not cover that you think should be tested by a future revision._

1.
2.
3.

---

## 5. Attestation

I have reviewed this bounty artefact bundle on the facts as presented. My verdict above reflects my
professional judgement as at the submission date. I understand my verdict will be minted into the
public reviewer registry with the attribution posture stated in the frontmatter, and that an ACCEPT
verdict lifts this external-contributor calculator to the `practitioner-attested` tier bound to the
version I ratified.

**Signed:**
**Name:**
**Credential:**
**Date:**
