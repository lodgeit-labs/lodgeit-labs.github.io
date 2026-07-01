# Bounty #01 — Public review brief: Division 7A Minimum Yearly Repayment

**Reviewer:** [Reviewer Name]
**Calculator under review:** `lodgeit-labs/Div7A_Calculator` (commit `main` HEAD, 2026-06-30 snapshot)
**Statute scope:** ITAA 1936 s 109D + s 109E + s 109N
**Income year:** 2024–25 (FY2025)
**Estimated reviewer time:** ~2 hours, one sitting
**Compensation:** discussed separately

---

## 1. What this calculator claims to do

The `Div7A_Calculator` is a deterministic Prolog microservice that takes:

- A private-company loan to a shareholder/associate (`loan_data`)
- The benchmark interest rate for the year of income (`context.benchmark_interest_rate`)
- The lodgement day of the company's tax return (`context.lodgment_date`)
- A ledger of repayments made during the year (`repayment_ledger`)

...and returns:

- The **amalgamated loan base amount** at lodgement day (`amalgamated_base_amount`) — the principal balance after crediting pre-lodgement-day repayments
- The **statutory minimum yearly repayment** (`statutory_myr`) — the amount the borrower must repay each subsequent year to keep the loan outside s 109D
- The **total interest** accrued on the loan over the income year (`total_interest_calculated`)

The engine's MYR formula is the Subdivision EB amortisation formula:

$$
\text{MYR} = \frac{\text{Amalgamated Loan Balance} \times \text{Benchmark Rate}}{1 - (1 + \text{Benchmark Rate})^{-\text{Remaining Term}}}
$$

This is the calculator's claim to encode s 109E(6) — the formula a private company must use to determine the minimum yearly repayment that prevents a loan being treated as a deemed dividend under s 109D.

## 2. Statutory anchors as encoded

| Statute | Engine claim | Where in the code |
|---|---|---|
| s 109D(1) | A private company loan unrepaid by lodgement day is a deemed dividend unless an exception applies | Implicit — the calculator computes MYR *because* the loan is otherwise within s 109D |
| s 109N(3) | Loan is excluded from s 109D if it meets minimum interest rate + maximum term + written agreement before lodgement day | `validate_term/2` enforces 7-year cap for unsecured, 25-year cap for secured |
| s 109E(6) | The MYR formula above | `evaluate_div7a/2`: `RawMYR is (BaseL * Rate) / Denominator` where `Denominator is 1 - (1 + Rate)**(-Term)` |
| s 109E(2) | "Amalgamated loan" — combining loans made in the same income year | The `amalgamated_loan_sum` input field assumes amalgamation already done upstream |
| ATO benchmark rate (TD 2024/X for FY2025: 8.77%) | Supplied as input `benchmark_interest_rate = 0.0877` | Not hard-coded; expected from caller |

## 3. Scope boundaries — what this calculator does NOT do

These are explicit non-claims. Please **don't** review against them; we have separate calculators (or backlog tickets) for each:

- **Distributable surplus calculation** (s 109Y) — separate calculator
- **Subdivision EA UPE flow-through** (Trust → Company → Shareholder cascade) — separate workstream
- **Interposed entity look-through** (s 109T) — separate workstream
- **Anti-avoidance re-borrow detection** (s 109R) — separate workstream
- **Pre-1997 / transitional loans** (s 109D(4A) and the pre-Div 7A grandfathering rules) — out of scope; engine assumes post-4-December-1997 loans
- **Loans to which s 109N exemption is being **claimed** without a written agreement on the calculator's evidence path** — engine assumes the s 109N written-agreement precondition has been satisfied by the time the loan reaches it

You are reviewing **only the s 109E(6) MYR computation and its immediate inputs**. The architecture deliberately isolates this calculator from the surrounding statutory machinery.

## 4. The worked example

See `02-worked-example.md` (companion file).

Read it. Run the maths in your head (or on paper). The engine's actual output is at the bottom of that file. Tell us whether the formula was applied correctly.

## 5. The forensic questions

See `03-forensic-questions.md` (companion file).

Six questions, graded from easy to hard. Answer in your own time. You don't have to get every question "right" — the questions where you say "I don't know, this is ambiguous" or "the law is unclear on this" are **the most valuable answers**, because they're the edge cases the calculator's documentation needs to explicitly disclaim.

## 6. The reviewer-verdict template

See `04-reviewer-verdict-template.md` (companion file).

This is the structured template you'd fill in. Three top-level verdicts (`ACCEPT` / `REJECT` / `FIX_THEN_RE_REVIEW`), plus structured fields for citations, edge cases, and open questions.

Your filled-in verdict becomes a **hash-anchored review artefact**. The hash + your name + the date get baked into the calculator's permanent provenance trail. If anyone ever audits a Div 7A computation that came from this calculator in this year, the chain of reasoning leads back to your review.

## 7. What we'd like from you, structurally

1. **A statute-citation audit** — are the section references in §2 above pinned to the right paragraphs? If the engine says "s 109N(3)" but actually means "s 109N(1)(c)", we want to know.

2. **A predicate-translation fidelity check** — the MYR formula as encoded in the Prolog engine reads:

   ```
   MYR = (Amalgamated_Loan_Balance × Benchmark_Rate) / (1 − (1 + Benchmark_Rate)^(−Remaining_Term))
   ```

   Does that faithfully translate s 109E(6)? Anything missing? Anything added that shouldn't be?

3. **Edge-case discovery** — what real-world Div 7A scenarios would break this calculator's assumptions? (We expect to find at least two. The most useful answer is "your engine doesn't account for X, but the law requires X — here's the section.")

4. **A verdict** — ACCEPT means "ship it"; REJECT means "the formula or its statutory anchor is fundamentally wrong"; FIX_THEN_RE_REVIEW means "the formula is right but the calculator is missing safeguards / disclaimers / edge-case handling that a real practitioner would require".

## 8. How your verdict travels through the system

```
   Your filled-in verdict template (markdown)
                  │
                  ▼
   SHA-256 hash of the file
                  │
                  ▼
   Bound into the calculator's provenance ledger
   (visible alongside every future computation
    that uses the version of Div7A you reviewed)
                  │
                  ▼
   If the calculator ever gets pulled into evidence
   (audit, dispute, regulator query), the chain
   from the disputed number → the engine version →
   your review → your name is recoverable.
```

You're not just reviewing code. You're **stamping the law's encoding**.

## 9. Practical mechanics

- **You work in markdown.** Open the four companion files in any editor (VS Code, Obsidian, plain notepad — doesn't matter). Read them. Fill in the verdict template. Send it back.
- **You don't run code.** We've already run the engine for you. The worked example shows the engine's actual output. You're judging whether the output reflects the law.
- **You don't need to know Prolog.** The formula is in §1 in maths notation; the engine's expression of it is in §2 only as a transparency exhibit.
- **You can spend 90 minutes or 4 hours.** The brief is sized for ~2 hours of focused reading. If you find a rabbit-hole worth going down, log it as an edge case and stop — we don't expect exhaustive review.
- **Open questions are gold.** "The law is unclear here" / "I'd want a partner to sign this off" / "This depends on a TR I'd need to check" — log them. They become the calculator's published-disclaimer surface.

## 10. What happens after

If you ACCEPT: the calculator's `s109E_myr` predicate gets stamped with your verdict hash + your name + 2026-06-30 + the brief reference. The calculator continues into production.

If you FIX_THEN_RE_REVIEW: we author a fix-up branch addressing your concerns, and a second brief comes back to you in ~2 weeks. (No pressure on cadence — driven by our engineering, not your calendar.)

If you REJECT: we pause the calculator. The engine doesn't ship. We schedule a conversation about what's actually required.

In all three cases: **your name is in the audit trail.** That's the deal. The work is real and it's permanently attributable to you.

---

## Reviewer signoff

```yaml
brief_id: bounty-01-div7a-myr
reviewer_name: [Reviewer Name]
reviewer_received_date: <fill in when you start>
estimated_time_spent_hours: <fill in when you finish>
verdict: <ACCEPT | REJECT | FIX_THEN_RE_REVIEW>
verdict_artefact_filename: 04-reviewer-verdict-template.md
```

— Dad ∮
