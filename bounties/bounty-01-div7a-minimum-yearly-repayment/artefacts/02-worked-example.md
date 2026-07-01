# Worked Example — Div 7A MYR Calculator

**Companion file to:** `bounty-01-div7a-myr.md`

---

## The scenario

**MHPL** (a private company, Australian-resident) advanced a loan to **David** (a shareholder of MHPL).

| Variable | Value |
|---|---|
| Lender | MHPL — private company |
| Borrower | David — shareholder of MHPL |
| Loan amount | $100,000 |
| Loan date | 15 July 2024 |
| Loan type | Unsecured |
| Original term | 7 years (the maximum permitted by s 109N(3)(b) for unsecured loans) |
| Written agreement in place before lodgement day | Yes — assumed |
| Income year | 1 July 2024 – 30 June 2025 (FY2025) |
| Lodgement day of MHPL's tax return | 15 May 2026 |
| ATO benchmark interest rate FY2025 | 8.77% (TD 2024/X — *please verify this citation*) |

**Repayments made during FY2025:**

| Date | Amount | Reference |
|---|---|---|
| 1 July 2024 | $30,000 | "Initial Repayment" (a partial repayment of the original advance, made the same income year but before lodgement day) |

No other repayments. No further drawings. No interposed entities. No UPE in the chain. (Those are out of scope per the brief §3.)

## The engine's intermediate working

**Step 1 — Compute the amalgamated loan balance at lodgement day:**

```
amalgamated_loan_sum = $100,000     (the original advance)
pre_lodgement_repayments = $30,000  (only the 1 July 2024 repayment is before 15 May 2026)
BaseL = $100,000 − $30,000 = $70,000
```

The engine carries `$70,000` as the principal on which the MYR is computed.

**Step 2 — Apply the s 109E(6) formula:**

$$
\text{MYR} = \frac{\text{BaseL} \times \text{Rate}}{1 - (1 + \text{Rate})^{-\text{Term}}}
$$

With the numbers:

$$
\text{MYR} = \frac{70{,}000 \times 0.0877}{1 - (1.0877)^{-7}}
$$

Computing the denominator:

$$
(1.0877)^{-7} = 0.55557
$$

$$
1 - 0.55557 = 0.44443
$$

So:

$$
\text{MYR} = \frac{6{,}139.00}{0.44443} = 13{,}815.65
$$

**Step 3 — Compute the interest accrued over the income year** (a separate output the engine produces; not the MYR itself):

The engine walks the ledger day-by-day:

- From 1 July 2024 (income-year-start) to 1 July 2024 (first repayment): 0 days at $100,000
- From 1 July 2024 to 30 June 2025 (income-year-end): 365 days at $70,000

```
Period interest = $70,000 × 0.0877 × (365 / 365)
                = $6,139.00
total_interest_calculated = $6,139.00
```

## The engine's actual output (returned by the Prolog server)

```json
{
  "loan_id": "L001",
  "amalgamated_base_amount": 70000.0,
  "statutory_myr": 13815.65,
  "total_interest_calculated": 6139.00
}
```

## Your task

Three things to mentally verify:

1. **Is the formula in Step 2 the correct encoding of s 109E(6)?** Specifically:
   - Is the denominator `1 − (1 + Rate)^(−Term)` the right denominator? (The legislation expresses this differently in the actual statute — verify the algebraic equivalence.)
   - Should `Term` here be the *original* 7-year term, or the *remaining* term as at the start of the FY2025 income year? The engine uses the original term as supplied. Is that correct for the very first year of the loan?

2. **Is the treatment of the $30,000 pre-lodgement-day repayment correct?**
   - s 109E(3) deals with how repayments interact with the MYR calculation. Does crediting the $30,000 against the principal *before* applying the formula match the statute's instructions? Or should the $30,000 instead count toward the MYR requirement for FY2025 (which is what s 109E suggests, but possibly not what the engine is doing)?
   - Specifically: should the engine output have been:
     - **Option A (what the engine does):** MYR is computed on the reduced balance of $70k → MYR = $13,815.65
     - **Option B (what the statute might require):** MYR is computed on the original $100k balance → MYR ≈ $19,736.65; then the $30k pre-lodgement repayment is credited against the MYR; net obligation $0 satisfied for this year
   - This is the single most important question in this brief. If A is wrong and B is right, the engine systematically under-states the MYR by amortising over a reducing balance prematurely.

3. **Does 8.77% match the ATO published benchmark interest rate for FY2025?**
   - The benchmark rate is published annually in a Taxation Determination. The engine accepts whatever the caller passes — but the caller (LodgeiT) needs to look this up correctly. Verify the rate and pin the TD citation.

The forensic questions file (`-forensic-questions.md`) goes deeper. This worked example is the "is the basic maths right?" gate.
