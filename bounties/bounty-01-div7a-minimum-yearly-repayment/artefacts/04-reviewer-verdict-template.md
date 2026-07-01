---
artefact_kind: reviewer-verdict
artefact_schema_version: 1
brief_id: bounty-01-div7a-myr
calculator_under_review: lodgeit-labs/Div7A_Calculator
calculator_commit: <fill in: short SHA of the engine version you reviewed, e.g. 4a1f2c8>
statute_scope:
  - ITAA_1936_s_109D
  - ITAA_1936_s_109E
  - ITAA_1936_s_109N
income_year: FY2025
reviewer:
  name: [Reviewer Name]
  role: AU statute-grade reviewer (candidate Tier-1 AU tax-authority ratifier per LE trust-tier system)
  affiliation: <fill in: Big-4 firm name, or "independent">
  reviewer_id: <leave blank — we'll assign one>
review_session:
  received_date: <YYYY-MM-DD>
  started_date: <YYYY-MM-DD>
  completed_date: <YYYY-MM-DD>
  time_spent_hours: <decimal>
verdict: <ACCEPT | REJECT | FIX_THEN_RE_REVIEW>
verdict_confidence: <HIGH | MEDIUM | LOW>
---

# Reviewer Verdict — Div 7A MYR Calculator, FY2025

## 1. Headline verdict

<One paragraph. ACCEPT means "ship it." REJECT means "the encoding of the law is fundamentally wrong; do not ship." FIX_THEN_RE_REVIEW means "the maths is broadly right but there are concerns the calculator must address before going to production." Be plain. No hedging in this paragraph — the hedges go below.>

## 2. Statute-citation audit

For each section the brief claimed the engine encodes, confirm or correct:

| Statute claimed | Correctly cited? | If wrong, the correct citation |
|---|---|---|
| ITAA 1936 s 109D(1) | <YES \| NO> | <citation> |
| ITAA 1936 s 109N(3) | <YES \| NO> | <citation> |
| ITAA 1936 s 109E(6) | <YES \| NO> | <citation> |
| ITAA 1936 s 109E(2) | <YES \| NO> | <citation> |
| TD 2024/X (FY2025 benchmark) | <YES \| NO> | <correct TD number + actual rate> |

Additional statute references the engine *should* cite but doesn't:

- <bullet list, or "none">

## 3. Formula-fidelity verdict

The engine encodes the s 109E(6) MYR as:

```
MYR = (Amalgamated_Loan_Balance × Benchmark_Rate)
      / (1 − (1 + Benchmark_Rate)^(−Remaining_Term))
```

**Is this algebraically equivalent to the statute?**

- [ ] Yes, identical to s 109E(6)
- [ ] Yes, but expressed in a different but equivalent form. Statutory form: <fill in>
- [ ] No, deviates from the statute. Deviation: <fill in>

**Is the engine's interpretation of "Remaining Term" correct?**

- [ ] Yes — using the original term is correct in the first year and re-computed for subsequent years
- [ ] No — should be the term remaining as at the start of the current income year
- [ ] Ambiguous — the statute is silent on this; see open questions below

## 4. Forensic question answers

### Q1 — s 109E(6) statute pin
<your answer>

### Q2 — timing-of-repayments (the load-bearing question)

**Engine's behaviour:** reduces the principal by pre-lodgement-day repayments *before* applying the MYR formula.

**Correct treatment per the statute:**

- [ ] Engine is correct (Option A in the worked example)
- [ ] Engine is wrong; Option B (compute MYR on opening balance, then credit repayments toward MYR) is correct
- [ ] Both interpretations are defensible; the ATO has published guidance preferring one. Citation: <fill in>
- [ ] Other: <fill in>

**Detail / reasoning:**
<your answer>

### Q3 — FY2025 benchmark interest rate citation
- TD number: <fill in>
- Rate: <fill in %>
- Publication date: <fill in>
- Notes: <any caveats>

### Q4 — secured-loan 25-year term requirements
<your answer>

### Q5 — s 109N(3) precondition validation gaps
<your answer>

### Q6 — multi-loan amalgamation under s 109E(2)
<your answer>

## 5. Edge cases the calculator should disclaim or handle

List edge cases you identified that the calculator does not currently handle but a real practitioner would encounter. For each, indicate severity:

- **CRITICAL** — engine will produce a materially wrong number in this case
- **WARNING** — engine will produce a defensible number but it's not the only correct interpretation; calculator should disclose this
- **NOTE** — calculator should mention this but it doesn't change the output

Format:

```
- [SEVERITY] <edge case description>
  Why it matters: <one sentence>
  Suggested remedy: <one sentence — could be "disclaim in docs", "add input validation", "block calculation with a meaningful error", or "needs separate calculator">
```

<your list>

## 6. Open questions

Questions you encountered that you can't resolve from current law / public guidance. These become **the calculator's known-unknowns disclosure** — published alongside its output.

```
- <question>
  Why this matters: <one sentence>
  How you'd resolve it if you had unlimited time: <one sentence — "check with a partner", "wait for a TR", "test with the ATO directly", etc.>
```

<your list>

## 7. If you said FIX_THEN_RE_REVIEW — what needs to change

For each fix required, give:

- The defect (in plain English)
- The proposed remedy
- Whether you'd want to re-review after the fix, or whether you trust us to implement it correctly without a second look

<your list>

## 8. Reviewer attestation

By signing below, you attest that:

1. You read the brief, the worked example, and the forensic questions
2. The verdict above reflects your good-faith professional judgement based on the materials provided
3. You agree that this verdict, signed and hashed, may be bound into the calculator's permanent provenance trail and visible to future auditors, regulators, or counterparties who need to verify the calculator's review history
4. You retain no proprietary interest in this verdict and grant LodgeiT Labs the right to publish it (in full or in summary form) under the LodgeiT Labs open-source licence

Reviewer signature:

```
Name:         [Reviewer Name]
Date:         <YYYY-MM-DD>
Signature:    <free-form — typed name is sufficient; we'll hash the file>
```

---

*This verdict file, once signed, will be SHA-256-hashed and the hash bound into the `Div7A_Calculator` provenance ledger under `helm_mutations` per the Zero-Hallucination Law (LodgeiT Labs Brain Standing Rule #3).*

*Reviewer attribution will appear in the LE corpus trust-tier metadata for `le-au-corpus` under §15 D3 / D5 of the LE Trust Tier System.*
