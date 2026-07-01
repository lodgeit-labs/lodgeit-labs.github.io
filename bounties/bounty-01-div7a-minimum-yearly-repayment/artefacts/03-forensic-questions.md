# Six Forensic Questions — Div 7A MYR Calculator

**Companion file to:** `bounty-01-div7a-myr.md`

Graded from easy (verification) to hard (edge case the engine probably gets wrong). Answer in your own words — bullet points are fine, citations preferred where you have them, "I don't know but I'd check X" is a perfectly valid answer.

---

## Q1 (warm-up — statute pin)

The engine claims to encode the s 109E(6) MYR formula.

**Pull up s 109E(6) ITAA 1936.** Is the formula in the brief's §1:

$$
\text{MYR} = \frac{\text{Amalgamated Loan Balance} \times \text{Benchmark Rate}}{1 - (1 + \text{Benchmark Rate})^{-\text{Remaining Term}}}
$$

algebraically equivalent to what the statute actually says? The statute expresses it in a slightly different form. Confirm equivalence (or flag deviation).

**Bonus:** what does the statute call each variable? Match the engine's variable names against the statutory labels.

---

## Q2 (the timing-of-repayments question — the load-bearing one)

The worked example shows the engine treating a $30,000 pre-lodgement-day repayment by **reducing the principal before applying the MYR formula**, giving:

- Amalgamated balance: $70,000 (not $100,000)
- MYR on $70,000: $13,815.65

**Question:** is this the correct interpretation of s 109E? Or should s 109E require the MYR be computed on the original $100,000, with the $30,000 then being credited toward satisfying the FY2025 MYR obligation (so net obligation for FY2025 = max(0, $19,736.65 − $30,000) = $0)?

There's a real legal distinction here:

- **Engine's approach:** repayments amortise the principal early; future-year MYRs are calculated off a lower base
- **Statute's approach (we suspect):** the MYR is fixed at the start of the income year based on the opening balance; repayments during the year count *toward* satisfying that MYR, not toward reducing the base on which it's computed

What does the ATO's published guidance say? (PCG 2017/13? An older TR?) What's the practical impact across the 7-year amortisation schedule of the loan?

This is the question I most want a real answer to.

---

## Q3 (the benchmark interest rate citation)

The engine accepts an externally-supplied benchmark interest rate (`0.0877` in the worked example, claimed to be the FY2025 rate).

**Question:** is 8.77% the correct ATO benchmark rate for FY2025 (income year 1 July 2024 – 30 June 2025)? What's the published citation (which Taxation Determination)? Is it published in advance of the income year, or does it get backdated? If the calculator is run mid-year, what should it do if the rate isn't published yet?

We need:
- The TD number
- The actual rate (verify our 8.77%)
- The publication date

So we can pin it as a hash-anchored fact in the statutory-rate table.

---

## Q4 (the 7-year unsecured cap — edge case)

The engine's `validate_term/2` predicate hard-codes:

- 7 years for unsecured loans
- 25 years for secured loans

**Question:** is the 25-year secured-loan term governed by s 109N(3)(b), and what are the requirements for a loan to *qualify* as "secured" for this purpose? Specifically:

- What kind of security is required? (Real property only? Or also chattel mortgages, charges over shares, guarantees?)
- What's the loan-to-value ratio requirement, if any?
- Can a partially-secured loan claim the 25-year term, or does it need to be fully secured?
- Does refinancing a 7-year unsecured loan as a secured loan reset the term clock?

The engine currently has no validation of the "is this loan actually secured?" predicate — it trusts the caller's `loan_type` field. Where would real-world auditors push back on that?

---

## Q5 (the pre-Subdivision-EB exception — what the engine doesn't model)

The s 109N(3) exemption requires three preconditions, all of which the engine **assumes** rather than validates:

1. A written agreement in place before the lodgement day
2. The interest rate for each year of the loan equal to or exceeds the benchmark rate
3. The term doesn't exceed the maximum (7 or 25 years)

**Question:** which of these three preconditions, if not met, would cause the engine's output to be misleading or actively wrong? Specifically:

- If there's **no written agreement** by lodgement day, what does s 109D actually do to the loan? Is the engine's MYR computation even relevant?
- If the **interest charged on the loan** in the prior year was less than the benchmark rate for that prior year, what is the engine's MYR computation supposed to do?

The brief explicitly disclaims that the calculator assumes the s 109N preconditions are met. But in practice, what's the failure mode if a careless practitioner runs the calculator on a loan that doesn't actually qualify?

---

## Q6 (the hardest one — multi-loan amalgamation under s 109E(2))

s 109E(2) defines an "amalgamated loan" as the combination of all loans the company makes to a particular borrower **in the same income year** that have the same maximum term and the same written-agreement date.

The engine accepts `amalgamated_loan_sum` as a single input field — it does **not** do the amalgamation itself. It trusts the caller to have already done it.

**Question:** what's the correct algorithm for amalgamation, and where can it go wrong?

Specifically:
- If MHPL makes three loans to David in FY2025 — $40k on 15 July 2024, $35k on 1 December 2024, and $25k on 1 May 2025 — should these be one amalgamated loan of $100k, or three separate Div 7A loans?
- Do they need to share the same loan type (all unsecured / all secured) to amalgamate?
- What if one of them has a 7-year term and another has a 5-year term — can they amalgamate?
- What's the relevant date for "income year" — the loan date, the agreement date, or the year in which it became a Div 7A loan (i.e. unrepaid by lodgement day)?

This is the question where, if you give us a clean answer, we'd put it directly into the calculator's documentation as a worked example with your name attached.

---

## Format for your answers

Free-form is fine. A markdown bullet under each question header is sufficient. If you find that the answer is "the law is genuinely ambiguous here," **say that and stop** — that's a publishable finding in its own right.

If you cite a TR / PCG / TD / court case, please include the citation (Austlii URL is welcome but not required).

Total time we expect this to take: ~90 minutes if you're warm on Div 7A, ~2.5 hours if you have to look things up. Spend longer if Q2 or Q6 turn into a rabbit hole worth exploring.
