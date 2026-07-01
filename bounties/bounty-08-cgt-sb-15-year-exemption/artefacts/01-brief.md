# Bounty #08 — Public review brief: CGT SB 15-Year Exemption

**Bounty ID:** bounty-08-cgt-sb-15-year-exemption
**Domain:** CGT small business concessions — 15-year exemption
**Statutory anchors:** Subdivision 152-B ITAA 1997; s 152-105 (individual), s 152-110 (company/trust)
**Calculator target:** **Spec-first bounty** — no existing calculator. Reviewer authors the ratification spec.
**Expected effort:** ~3 hours
**Prize:** AUD $900

---

## 1. Why this bounty exists

The CGT small-business 15-year exemption (Subdiv 152-B) is the most valuable of the four SB CGT concessions — a full exemption of the capital gain, no cap, on top of the retirement exemption cap being unaffected.

We do not yet have a calculator for this. This bounty asks a competent CGT practitioner to author the ratification spec — the set of predicates that a future calculator must satisfy to correctly determine 15-year exemption eligibility on a real disposal.

## 2. What the spec must cover

**Basic conditions (s 152-10):**
- CGT event applies to a CGT asset.
- CGT event would result in a capital gain.
- The taxpayer satisfies one of: SBE test, MNAV test ($6M net assets), or partner-in-partnership tests.
- Active-asset test (s 152-35 to s 152-40).

**Additional conditions for 15-year exemption (s 152-105 / 152-110):**
- **Individual (s 152-105):** continuous ownership of the asset for at least 15 years; taxpayer is 55+ AND retiring, OR permanently incapacitated at time of disposal.
- **Company or trust (s 152-110):** the entity has owned the asset for at least 15 years continuously; the "significant individual" test at all times during the ownership; a "significant individual" at time of disposal is 55+ retiring or incapacitated.

## 3. Spec deliverable

The reviewer produces a numbered list of predicates in plain English, ordered by test-precedence, that a calculator must evaluate to determine eligibility. Example:

```
predicate 1: cgt_asset(X)                       [s 152-10(1)(a)]
predicate 2: cgt_event_gives_capital_gain(X)    [s 152-10(1)(b)]
predicate 3: taxpayer_satisfies_sbe_or_mnav()   [s 152-10(1)(c)]
predicate 4: active_asset_test(X)               [s 152-35]
predicate 5: continuous_ownership_15_years(X)   [s 152-105(1)(a) OR s 152-110(1)(a)]
...
```

Plus: the reviewer surfaces edge cases the spec must anticipate.

## 4. Companion files

- `02-worked-example.md` — family trading trust, 68-year-old sole operator, disposal of business.
- `03-forensic-questions.md` — seven questions.
- `04-reviewer-verdict-template.md` — YAML-frontmatter form.
- `05-taxgenii-appendix.md` — statute pre-load.
- `06-terms.md` — payment, IP, attribution.

## 5. Out of scope

- The 50% active-asset reduction (Subdiv 152-C) — separate concession.
- The retirement exemption (Subdiv 152-D) — separate concession.
- The rollover (Subdiv 152-E) — separate concession.
- Non-SB CGT discount (Div 115) — unrelated.
