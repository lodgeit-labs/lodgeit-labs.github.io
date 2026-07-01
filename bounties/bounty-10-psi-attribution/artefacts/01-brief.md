# Bounty #10 — Public review brief: PSI Attribution — 80/20 and Results Test

**Bounty ID:** bounty-10-psi-attribution
**Domain:** Personal services income — attribution and PSB eligibility
**Statutory anchors:** Div 84–87 ITAA 1997; s 87-15 (personal services business), s 87-18 (results test), s 87-20 (unrelated clients test), s 87-25 (employment test), s 87-30 (business premises test)
**Calculator target:** **Spec-first bounty** — no existing calculator. Reviewer authors the ratification spec.
**Expected effort:** ~3 hours
**Prize:** AUD $850

---

## 1. Why this bounty exists

PSI is the tax regime that stops individuals from routing personal-services income through interposed entities (companies, trusts) to reduce their marginal-tax exposure. The regime attributes the net PSI back to the individual **unless** the entity qualifies as a **personal services business (PSB)**.

Four PSB tests. If any one is satisfied, the entity is a PSB and attribution does not apply:

1. **Results test (s 87-18)** — the strongest test.
2. **Unrelated clients test (s 87-20)** — includes the 80/20 rule.
3. **Employment test (s 87-25).**
4. **Business premises test (s 87-30).**

We do not yet have a calculator for this. This bounty asks a competent PSI practitioner to author the ratification spec.

## 2. What the spec must cover

- Threshold gates: is the income PSI at all? (s 84-5 characterisation.)
- Four PSB tests, ordered by ease-of-satisfaction from taxpayer's perspective.
- The 80% rule under s 87-20: if 80%+ of PSI comes from one source, results test **must** be satisfied.
- Attribution mechanics under Div 86 if no PSB test is passed.

## 3. Out of scope

- Personal services *income* (Div 84) definitional questions — assume this has been passed.
- GST treatment of PSI.
- Payroll tax implications.
- Superannuation guarantee treatment.
