#!/usr/bin/env python3
"""
Generator for the six-file artefact bundles for Bounties #2-#10.

Bounty #1 (Div 7A) uses the sanitised Holly-provenance files already copied
into place. This script authors the domain-specific briefs for #2-#10 and
installs the shared terms + a bounty-specific TaxGenii appendix skeleton
for all ten (Bounty #1 gets 05 + 06 added here too).

Each brief-family is authored with:
  - Load-bearing statutory anchor list
  - Worked example scaffold (numbers real enough to be recognisable)
  - Six-to-seven forensic questions graded easy → hard
  - YAML-frontmatter reviewer-verdict template
  - Pre-cited TaxGenii statutory appendix
  - Shared terms file

The prose is authored to the standard: a mid-career practitioner should
be able to read the brief, work through the example, and produce a
useful verdict in the stated hours.
"""

from pathlib import Path

BOUNTIES_DIR = Path(__file__).parent

# -----------------------------------------------------------------------------
# Shared terms template
# -----------------------------------------------------------------------------

TERMS = (BOUNTIES_DIR / "_TERMS_TEMPLATE.md").read_text()


def terms_for(bounty_id, prize, hours):
    return (TERMS
            .replace("{{BOUNTY_ID}}", bounty_id)
            .replace("{{PRIZE}}", str(prize))
            .replace("{{HOURS}}", str(hours)))


# -----------------------------------------------------------------------------
# Reviewer-verdict template (shared skeleton with per-bounty binding)
# -----------------------------------------------------------------------------

def verdict_template(bounty_id, bounty_title, statutory_anchors, num_questions=6):
    q_blocks = "\n".join([
        f"""  - question_number: {i}
    verdict: ""              # ACCEPT / REJECT / FIX
    citation_authority: ""   # section reference or case citation
    reasoning: |
      # Free-text reasoning here. Cite where you diverge.
    edge_case_notes: |
      # Optional — anything surfaced by this question worth banking."""
        for i in range(1, num_questions + 1)
    ])

    return f"""---
brief_id: {bounty_id}
bounty_title: "{bounty_title}"
statutory_anchors: "{statutory_anchors}"
reviewer:
  name: ""
  credential_class: ""        # CA / CTA / CPA / FIPA / MIPA / TPB
  registration_status: ""     # active / lapsed / retired
  jurisdiction: "Australia"
  attribution_posture: "named"  # named | initialled | anonymous
reviewed_calculator_version: ""  # copy from brief
submission_date: ""              # YYYY-MM-DD
top_level_verdict: ""            # ACCEPT / REJECT / FIX
verdict_hash: ""                 # (we compute this on receipt)
---

# Reviewer Verdict — {bounty_title}

**Bounty:** {bounty_id}

## 1. Top-level verdict

_Choose one: **ACCEPT** / **REJECT** / **FIX**._

- **ACCEPT** — the calculator's statute-to-predicate translation is correct on the facts of the brief. Minor stylistic comments allowed.
- **REJECT** — the calculator's translation is materially wrong. State the section/case-law authority you rely on.
- **FIX** — the translation is mostly correct but has a specific error that can be fixed with a targeted change. Describe the fix.

**Your top-level verdict:**

---

## 2. Per-question verdicts

```yaml
per_question_verdicts:
{q_blocks}
```

---

## 3. Citation audit

_List every statutory section, ATO ruling, or case-law citation the calculator/brief relies on. Mark each: ✓ correct citation / ✗ wrong citation / ⚠ citation exists but is misapplied._

| # | Authority as cited | Your assessment | Notes |
|---|---|---|---|
| 1 |  |  |  |
| 2 |  |  |  |
| 3 |  |  |  |

---

## 4. Edge cases surfaced

_Anything the brief did not cover that you think should be tested by a future revision._

1.
2.
3.

---

## 5. TaxGenii appendix coverage feedback

_Was the pre-loaded statutory appendix (file 05) adequate? What was missing?_

---

## 6. Attestation

I have reviewed this bounty artefact bundle on the facts as presented. My verdict above reflects my professional judgement as at the submission date. I understand my verdict will be minted into the public reviewer registry with the attribution posture stated in the frontmatter.

**Signed:**
**Name:**
**Credential:**
**Date:**
"""


# -----------------------------------------------------------------------------
# Per-bounty content
# -----------------------------------------------------------------------------

BOUNTY_CONTENT = {
    2: {
        "id": "bounty-02-depreciation-effective-life",
        "title": "Depreciation effective-life lookup",
        "prize": 400,
        "hours": 1.5,
        "anchors": "s 40-95, s 40-100, s 40-102, s 40-105 ITAA 1997; TR 2024/4",
        "calculator": "Depreciation_Transforms",
        "calc_version": "v0.1.3",
        "brief": """# Bounty #02 — Public review brief: Depreciation Effective-Life Lookup

**Bounty ID:** bounty-02-depreciation-effective-life
**Domain:** Division 40 depreciation — effective-life determination
**Statutory anchors:** s 40-95, s 40-100, s 40-102, s 40-105 ITAA 1997; TR 2024/4
**Calculator target:** `lodgeit-labs/Depreciation_Transforms` — `Depreciation_Transforms` at version v0.1.3
**Expected effort:** ~1.5 hours
**Prize:** AUD $400

---

## 1. Why this bounty exists

The Division 40 depreciation engine looks up an effective life for every eligible depreciating asset. Three routes are available under s 40-95:

1. **Commissioner's determination** — TR 2024/4 (the annual effective-life ruling), industry-code table.
2. **Self-assessment** — the taxpayer works out effective life from first principles.
3. **Statutory caps** — s 40-102 caps the effective life for certain assets (buses, light commercial vehicles, trucks, aeroplanes) regardless of the two above.

Our engine implements this hierarchy. This bounty asks a competent practitioner to confirm the hierarchy is correctly applied on a real worked example.

## 2. Statutory anchors — the four sections you are ratifying

- **s 40-95** — the effective-life-choice section. Which of the three routes applies, and in what order.
- **s 40-100** — Commissioner's determination mechanics.
- **s 40-102** — statutory caps for certain assets. Note: this section over-rides the outcome of both s 40-95(2) and s 40-95(3).
- **s 40-105** — self-assessment mechanics.
- **TR 2024/4** — the current-year effective-life ruling, tables A and B.

## 3. What our calculator does

Pseudo-code sketch (the actual implementation is in `Depreciation_Transforms/src/effective_life.py`):

```
def effective_life(asset, industry_code, method):
    if asset in STATUTORY_CAPS_TABLE:               # s 40-102
        return STATUTORY_CAPS_TABLE[asset]
    if method == 'commissioner':                    # s 40-95(2), s 40-100
        return TR_2024_4_TABLE.lookup(asset, industry_code)
    if method == 'self_assess':                     # s 40-95(3), s 40-105
        return user_supplied_effective_life
    raise ValueError("effective_life method must be 'commissioner' or 'self_assess'")
```

The bounty question: **is this the correct decision hierarchy, and does it capture the s 40-102 override correctly?**

## 4. Companion files

- `02-worked-example.md` — a plumbing subcontractor buys an $18k excavator FY2025. Full effective-life determination.
- `03-forensic-questions.md` — six questions, easy → hard.
- `04-reviewer-verdict-template.md` — YAML-frontmatter verdict form.
- `05-taxgenii-appendix.md` — statute pre-load, TR 2024/4 excerpts.
- `06-terms.md` — payment, IP, attribution.

## 5. Out of scope

- Anything under Division 43 (capital works). This bounty is Division 40 only.
- Anything about depreciating asset **cost** (that's a different bounty candidate).
- Anything about balancing adjustments on disposal.
- Anything about intangibles under Subdivision 40-B.
""",
        "worked_example": """# Worked Example — Bounty #02

**Companion file to:** `01-brief.md`

## The scenario

**Taxpayer:** ABC Plumbing Pty Ltd (Australian resident company, SBE)
**Financial year:** FY2024–25
**Asset:** Second-hand mini-excavator, purchased 14 September 2024
**Cost:** AUD $18,000 (GST-inclusive; $16,363.64 GST-exclusive)
**Industry:** Plumbing subcontractor (ANZSIC 3232 Plumbing services)
**Method chosen by taxpayer:** Commissioner's determination (s 40-95(2))

## The engine's determination

Query:
```
effective_life(
    asset = "excavator, mini (crawler or wheeled)",
    industry_code = "plumbing services (ANZSIC 3232)",
    method = "commissioner"
)
```

Engine output:
```json
{
    "effective_life_years": 5,
    "source": "TR 2024/4 Table B — Construction (10111-32990) — Excavators (crawler, wheeled)",
    "route": "s 40-95(2) Commissioner's determination",
    "statutory_cap_applied": false,
    "notes": "Table B industry entry; no plumbing-services-specific override in Table A"
}
```

## The engine's derived decline value (FY2024–25, prime cost)

- Cost: $16,363.64 (GST-exclusive)
- Effective life: 5 years
- Prime cost rate: 100% / 5 = 20% per annum
- Days held in FY2024–25: 291 (14 Sep 2024 to 30 Jun 2025 inclusive)
- Decline for FY2024–25: $16,363.64 × 20% × (291/365) = **$2,608.03**

## Rounding + presentation

- Rounded to cents throughout intermediate steps; final decline rounded to nearest cent.
- Decline expressed as an income-tax deduction under s 40-25.

## What the reviewer is being asked

1. Is the effective-life table selection correct? Should this asset have looked to Table A (industry-specific) rather than Table B (general asset class)?
2. If Table A was correct: is there an entry for "plumbing services" that would give a different life?
3. Is the s 40-95(3) self-assessment path clearly closed off by the taxpayer's method election?
4. Would the s 40-102 statutory cap ever bite on this asset class?
5. Is the day-count calculation correct (291 days, use of the "days held" concept vs "days ready for use")?
6. Any edge case the calculator should test that this worked example does not surface?
""",
        "forensic": """# Forensic Questions — Bounty #02

**Companion file to:** `01-brief.md`

Six questions, easy → hard. Q3 is the load-bearing question. Q6 is deliberately open-ended.

---

## Q1 (easy) — Table selection

Under TR 2024/4, is the mini-excavator in Table A (industry-specific) under an ANZSIC code applicable to plumbing services, or in Table B (general asset class) under construction/earthmoving?

## Q2 (easy) — Effective-life value

Assuming the correct table is identified, what effective life does TR 2024/4 give for a "mini-excavator (crawler or wheeled)" for FY2024–25?

## Q3 (load-bearing) — s 40-102 interaction

The taxpayer chose the Commissioner's determination route (s 40-95(2)). Suppose the Commissioner's determination gives 5 years but s 40-102 lists a shorter statutory cap for this asset. Which prevails, and why?

_(This question separates skim-readers from careful ones. The statute is unambiguous on the answer once you find the right sub-section, but the calculator must implement the interaction correctly.)_

## Q4 (medium) — Self-assessment election

If the taxpayer had elected self-assessment under s 40-95(3), what test does s 40-105 require them to satisfy? Would that test likely produce the same 5-year answer, a shorter answer, or a longer answer for a plumbing subcontractor's second-hand excavator?

## Q5 (medium) — Days-held vs days-ready-for-use

The engine used 291 days from acquisition (14 Sep 2024) to year-end. Should the count instead be from the date the asset was first used or installed ready for use per s 40-60? Under what facts would these two dates diverge, and how does the engine handle that?

## Q6 (open) — Anything else

What has this brief and worked example not tested that a competent practitioner would test before shipping this into production?

Examples of areas the calculator could plausibly get wrong:
- Second-hand vs new asset treatment
- Aggregated turnover threshold for SBE simplified depreciation election (crossover with Bounty #4)
- Immediate asset write-off for SBEs (crossover with Bounty #3)
- Balancing adjustment on eventual disposal
- Any interaction with the small-business boost measures for FY2023–24 and FY2024–25
""",
    },
    3: {
        "id": "bounty-03-instant-asset-write-off",
        "title": "Instant Asset Write-Off eligibility",
        "prize": 450,
        "hours": 2,
        "anchors": "s 328-180 ITAA 1997",
        "calculator": "Depreciation_Transforms",
        "calc_version": "v0.1.3",
        "brief": """# Bounty #03 — Public review brief: Instant Asset Write-Off Eligibility

**Bounty ID:** bounty-03-instant-asset-write-off
**Domain:** SBE simplified depreciation — instant asset write-off ($20k threshold)
**Statutory anchors:** s 328-180 ITAA 1997
**Calculator target:** `lodgeit-labs/Depreciation_Transforms` at version v0.1.3
**Expected effort:** ~2 hours
**Prize:** AUD $450

---

## 1. Why this bounty exists

The instant asset write-off is politically active — the threshold has changed year-on-year, the FY2024–25 measure was legislated late, and the FY2025–26 transition (whether the $20k threshold extends, drops, or lapses) is contingent on Budget measures.

Our engine implements a period-scoped IAWO eligibility gate. The gate must correctly:

1. Confirm the taxpayer is a small business entity (SBE) — aggregated turnover < $10m.
2. Apply the correct per-asset threshold for the relevant income year.
3. Handle the "held ready for use" timing rule.
4. Handle multiple assets that individually satisfy the threshold but which one might argue are "part of a set".
5. Handle the anti-avoidance rules that prevent artificial-splitting.

## 2. What the calculator does

Pseudo-code:

```
def iawo_eligible(taxpayer, asset, income_year):
    if not taxpayer.is_sbe(income_year):        # s 328-110 aggregated turnover
        return False, "not SBE"
    threshold = IAWO_THRESHOLD_TABLE[income_year]  # $20,000 for FY24-25
    if asset.cost > threshold:                   # s 328-180(1)(b)
        return False, "cost exceeds threshold"
    if not asset.held_ready_for_use_before_year_end(income_year):
        return False, "not held ready for use"
    return True, "eligible"
```

Followed by the write-off:

```
def apply_iawo(asset, income_year):
    if iawo_eligible(...)[0]:
        return {"deduction": asset.cost, "route": "s 328-180"}
```

## 3. Statutory anchor

**s 328-180 ITAA 1997** — the operative section, as modified by the transitional provisions in the ITAA 1997 (Div 328). The threshold amount is set by regulation and can change per income year.

**Note:** the reviewer should confirm the current-year threshold from the primary source (Treasury Laws Amendment / ATO ruling) — the calculator's `IAWO_THRESHOLD_TABLE` is period-scoped and must match statute.

## 4. Out of scope

- The "backing business investment" incentive (FY2019–20 to FY2021–22) is out of scope — different regime.
- The temporary full expensing (FY2020–21 to FY2022–23) is out of scope — different regime.
- The IAWO for pool low-value assets (< $1,000) under Subdiv 328-D pool mechanics is out of scope — see Bounty #04.
""",
        "worked_example": """# Worked Example — Bounty #03

**Companion file to:** `01-brief.md`

## The scenario

**Taxpayer:** DEF Cafés Pty Ltd
**Financial year:** FY2024–25 (year ending 30 June 2025)
**Aggregated turnover for FY2023–24:** $2.4M (well under the $10M SBE threshold)
**Assets purchased during FY2024–25:**

| # | Asset | Cost (GST-excl) | Date acquired | Date first used |
|---|---|---:|---|---|
| A | Espresso machine (commercial, single group) | $18,900 | 12 Aug 2024 | 15 Aug 2024 |
| B | POS terminal | $2,300 | 12 Aug 2024 | 15 Aug 2024 |
| C | Under-counter dishwasher | $8,400 | 20 Nov 2024 | 25 Nov 2024 |
| D | Coffee grinder (matching set with A, purchased together) | $4,200 | 12 Aug 2024 | 15 Aug 2024 |
| E | Delivery scooter | $19,850 | 3 Mar 2025 | 20 Jul 2025 |

## The engine's determinations

**Asset A (espresso machine, $18,900):**
- SBE test: PASS (aggregated turnover $2.4M < $10M)
- Cost test: PASS ($18,900 < $20,000)
- Held-ready-for-use before 30 Jun 2025: PASS (first used 15 Aug 2024)
- **Verdict: IAWO ELIGIBLE. Deduction $18,900 in FY2024–25.**

**Asset B (POS terminal, $2,300):**
- All tests PASS.
- **Verdict: IAWO ELIGIBLE. Deduction $2,300 in FY2024–25.**

**Asset C (dishwasher, $8,400):**
- All tests PASS.
- **Verdict: IAWO ELIGIBLE. Deduction $8,400 in FY2024–25.**

**Asset D (coffee grinder, $4,200):**
- On its face, all tests PASS.
- **BUT:** Asset A + Asset D might arguably be "a set" — the calculator flags this for reviewer inspection.
- Engine current verdict: IAWO ELIGIBLE (treats each asset individually per s 328-180).
- **This is the load-bearing question for the bounty.**

**Asset E (delivery scooter, $19,850):**
- Cost test: PASS ($19,850 < $20,000).
- Held-ready-for-use before 30 Jun 2025: **FAIL** (first used 20 Jul 2025).
- **Verdict: IAWO NOT ELIGIBLE in FY2024–25.** Will be considered under FY2025–26 rules (assuming the regime continues; otherwise ordinary Division 40 depreciation).

## The engine's total FY2024–25 IAWO deduction

$18,900 + $2,300 + $8,400 + $4,200 = **$33,800**
""",
        "forensic": """# Forensic Questions — Bounty #03

**Companion file to:** `01-brief.md`

Six questions. Q4 is the load-bearing question. Q6 is the open-ended finder.

## Q1 (easy) — Threshold

What is the per-asset IAWO threshold for FY2024–25, and what is the statutory instrument that sets it?

## Q2 (easy) — SBE eligibility

For FY2024–25, what is the aggregated turnover threshold that determines SBE status for IAWO purposes?

## Q3 (medium) — "Held ready for use"

Asset E (delivery scooter) was acquired on 3 Mar 2025 but first used on 20 Jul 2025 (post-year-end). The engine says NOT ELIGIBLE for FY2024–25. Is that correct? What if the scooter was delivered to the taxpayer's premises on 25 Jun 2025 but had a broken indicator that meant it wasn't roadworthy until 20 Jul 2025 — does that change the answer?

## Q4 (load-bearing) — The "set" question

Asset A (espresso machine, $18,900) and Asset D (coffee grinder, $4,200) were purchased together, from the same supplier, on the same day, with a single invoice. The calculator treats them as two separate assets.

**Is that correct under s 328-180 and any relevant ATO guidance?** Would your answer differ if the invoice described them as "espresso set" with a combined price of $23,100? Would it differ if the two items are physically separable and functionally independent (they are)?

## Q5 (medium) — Aggregation

If DEF Cafés has a related entity (say, DEF Baked Goods Pty Ltd, common ownership), how would that affect the SBE turnover calculation? Trace the aggregation rules in s 328-115.

## Q6 (open) — What did we miss?

What edge case is the calculator plausibly getting wrong that this worked example does not surface?

Candidates worth considering:
- Trade-in of an old asset partially offsetting the new cost
- Financed purchase (hire purchase or chattel mortgage) and how "cost" is measured
- Second-hand assets and whether IAWO applies (it does — but there was a period when it didn't for larger SBEs)
- The FY2025–26 transition and whether that is baked in yet
""",
    },
    4: {
        "id": "bounty-04-small-business-general-pool",
        "title": "Small business general pool",
        "prize": 600,
        "hours": 2.5,
        "anchors": "Subdiv 328-D ITAA 1997",
        "calculator": "Depreciation_Transforms",
        "calc_version": "v0.1.3",
        "brief": """# Bounty #04 — Public review brief: Small Business General Pool

**Bounty ID:** bounty-04-small-business-general-pool
**Domain:** SBE simplified depreciation — general pool mechanics
**Statutory anchors:** Subdivision 328-D ITAA 1997 (s 328-175 to s 328-260)
**Calculator target:** `lodgeit-labs/Depreciation_Transforms` at version v0.1.3
**Expected effort:** ~2.5 hours
**Prize:** AUD $600

---

## 1. Why this bounty exists

The SBE general pool is the fallback treatment for depreciating assets that a small business entity acquires but that do not qualify for IAWO (Bounty #3), OR for whose full amount the SBE has elected pool treatment despite IAWO eligibility.

The pool mechanics are:

- **First year in pool:** 15% of the taxable purpose proportion of the asset's cost.
- **Subsequent years:** 30% of the pool's opening adjustable value.
- **Low pool value threshold:** if the closing pool balance (before that year's decline) is less than $1,000, the entire balance is deductible in that year (s 328-210).
- **Disposals:** taxable purpose proportion of the termination value is subtracted from the pool.

## 2. What the calculator does

```
def roll_forward_pool(opening_balance, additions, disposals, income_year):
    first_year_decline = sum(a.cost * 0.15 for a in additions)
    subsequent_decline = opening_balance * 0.30
    pre_write_off_balance = opening_balance + sum(a.cost for a in additions) \\
                            - sum(d.termination_value for d in disposals) \\
                            - first_year_decline - subsequent_decline
    if pre_write_off_balance < 1000:
        deduction = first_year_decline + subsequent_decline + pre_write_off_balance
        closing_balance = 0
    else:
        deduction = first_year_decline + subsequent_decline
        closing_balance = pre_write_off_balance
    return {"deduction": deduction, "closing_balance": closing_balance}
```

## 3. Out of scope

- Anything about SBE eligibility itself (aggregated turnover under $10M) — that gate fires upstream.
- IAWO — see Bounty #3.
- Ordinary Division 40 depreciation for non-SBEs.
- The temporary "instant deduction of pool" during full-expensing years (2020–21 to 2022–23) is history; not relevant to a current-year audit.
""",
        "worked_example": """# Worked Example — Bounty #04

**Companion file to:** `01-brief.md`

## The scenario

**Taxpayer:** GHI Landscape Contractors Pty Ltd (SBE, aggregated turnover $3.8M)
**Financial year:** FY2024–25

**Pool opening balance (from prior year):** $8,750

**Additions during FY2024–25:**

| # | Asset | Cost | Taxable purpose % |
|---|---|---:|---:|
| P1 | Ride-on mower (over IAWO threshold) | $28,000 | 100% |
| P2 | Trailer for equipment transport | $12,500 | 100% |

**Disposals during FY2024–25:**

| # | Asset | Termination value |
|---|---|---:|
| D1 | Old ute (previously in pool) | $6,500 |

## The engine's pool roll-forward

**Step 1 — Additions taxable-purpose adjusted:**
- P1: $28,000 × 100% = $28,000
- P2: $12,500 × 100% = $12,500
- Total additions: **$40,500**

**Step 2 — Disposals taxable-purpose adjusted:**
- D1: $6,500 × 100% = **$6,500** (assumes the ute was always 100% business use)

**Step 3 — First-year decline (15% of additions):**
- $40,500 × 15% = **$6,075**

**Step 4 — Subsequent-year decline (30% of opening balance):**
- $8,750 × 30% = **$2,625**

**Step 5 — Pre-write-off balance:**
- Opening: $8,750
- Plus additions: $40,500
- Minus disposals: $6,500
- Minus first-year decline: $6,075
- Minus subsequent decline: $2,625
- **Balance: $34,050**

**Step 6 — Low-pool-value check:**
- Balance $34,050 > $1,000, so no write-off.

**Step 7 — Final:**
- Deduction for FY2024–25: **$8,700** ($6,075 + $2,625)
- Closing pool balance: **$34,050**
""",
        "forensic": """# Forensic Questions — Bounty #04

**Companion file to:** `01-brief.md`

Six questions. Q3 is the load-bearing. Q6 is the open finder.

## Q1 (easy) — Rates

What are the first-year and subsequent-year pool rates under Subdiv 328-D?

## Q2 (easy) — Low-pool-value threshold

What is the low-pool-value threshold at which the entire pool balance is written off, and which section sets it?

## Q3 (load-bearing) — Additions with < 100% taxable purpose

Suppose Asset P1 (ride-on mower) is used 70% for taxable purposes and 30% for the director's personal home garden. How does the pool mechanic handle this? Show the numbers.

## Q4 (medium) — Disposal termination value

The old ute (D1) had an original cost of $22,000 and was sold for $6,500. Does the pool care about the original cost, the previously-claimed deductions, or only the termination value? What is the treatment if the sale proceeds exceed the pool's opening balance?

## Q5 (medium) — IAWO election interaction

The taxpayer could have elected to write off Asset P1 and P2 individually under the IAWO regime (Bounty #3). But Asset P1 ($28,000) exceeds the $20k IAWO threshold, so it goes to pool. Asset P2 ($12,500) is under the threshold — is it correct to still pool it, or must the taxpayer take IAWO on P2?

## Q6 (open) — Edge cases

What is the pool doing (or not doing) that a competent practitioner would want to sanity-check before signing off?

Candidates:
- Change in aggregated turnover crossing the $10M threshold mid-year
- SBE election in and out of simplified depreciation
- Disposal of the whole pool (cessation of business)
- Trust distributions and TAP proportion changes
""",
    },
    5: {
        "id": "bounty-05-fbt-car-statutory-vs-operating",
        "title": "FBT car — statutory formula vs operating cost",
        "prize": 800,
        "hours": 3,
        "anchors": "s 7, 8, 9, 10, 10A, 22A FBTAA 1986",
        "calculator": "LodgeiT_FBT",
        "calc_version": "v0.2.0",
        "brief": """# Bounty #05 — Public review brief: FBT Car — Statutory Formula vs Operating Cost

**Bounty ID:** bounty-05-fbt-car-statutory-vs-operating
**Domain:** Fringe Benefits Tax — car fringe benefit method election
**Statutory anchors:** s 7, 8, 9, 10, 10A, 22A FBTAA 1986
**Calculator target:** `lodgeit-labs/LodgeiT_FBT` at version v0.2.0
**Expected effort:** ~3 hours
**Prize:** AUD $800

---

## 1. Why this bounty exists

The FBT car fringe benefit has two calculation methods:

1. **Statutory formula (s 9)** — 20% of the car's base value, adjusted for days provided and any recipient's payment/contribution. No log book required.
2. **Operating cost (s 10)** — total operating costs × (1 − business use percentage), adjusted for days provided and any recipient's payment/contribution. Log book required.

The taxpayer elects. Once elected for an FBT year, the method binds for that year (s 10(1)). Between years, the taxpayer may change methods.

Our engine implements both methods and lets the taxpayer choose. The bounty asks: **do the two calculations produce the correct answers under both methods, and does the engine correctly enforce the "election once made" rule within an FBT year?**

## 2. What the calculator does

**Statutory formula:**
```
taxable_value = (base_value × 0.20 × days_available / days_in_year) - contribution
```

**Operating cost:**
```
taxable_value = (operating_costs × (1 - business_use_pct) × days_available / days_in_year) - contribution
```

Where:
- `base_value` = cost or leased value, adjusted per s 9(2), including on-road costs but excluding certain financing costs.
- `operating_costs` = fuel + oil + repairs + maintenance + registration + insurance + deemed depreciation + deemed interest (s 10(2)).
- `business_use_pct` = per log book covering a minimum 12-week period per s 10A.

## 3. Out of scope

- Electric car FBT exemption (s 8A) — separate bounty candidate.
- Novated leases and the associate-lease treatment — separate.
- Employee contribution mechanics under s 9(2)(e) beyond the simple recipient's payment case.
- Reportable fringe benefits amounts on payment summaries.
""",
        "worked_example": """# Worked Example — Bounty #05

**Companion file to:** `01-brief.md`

## The scenario

**Employer:** JKL Consulting Pty Ltd
**FBT year:** 1 April 2024 to 31 March 2025 (FY2025 FBT year)
**Employee:** Sarah, senior consultant
**Car:** 2024 Toyota Kluger, purchased new by employer 1 May 2024
**Cost:** $65,000 (GST-inclusive; delivered price including on-roads)
**Days available for private use:** 335 (from 1 May 2024 to 31 March 2025)
**Employee contribution:** $2,000 (paid by Sarah, after-tax)

**Log book status:** Sarah maintained a valid 12-week log book from 1 May 2024 to 24 July 2024, showing 68% business use.

**Operating costs for the FBT year:**
- Fuel: $4,200
- Servicing and repairs: $1,150
- Registration: $920
- Insurance: $1,650
- Deemed depreciation (s 11): (see calculator)
- Deemed interest (s 11): (see calculator)

## The engine's calculations

**Method A — Statutory formula (s 9):**
- Base value: $65,000
- Statutory rate: 20%
- Days available / days in year: 335 / 365
- Taxable value (pre-contribution): $65,000 × 20% × (335/365) = **$11,930.14**
- Less employee contribution: $2,000
- **Taxable value: $9,930.14**

**Method B — Operating cost (s 10):**
- Total actual operating costs: $4,200 + $1,150 + $920 + $1,650 = $7,920
- Deemed depreciation (s 11(1)(a)): $65,000 × 25% × (335/365) = $14,914.38
- Deemed interest (s 11(1)(b)): $65,000 × 8.77% × (335/365) = $5,229.06 (using FY2025 statutory benchmark 8.77%)
- Total operating costs: $7,920 + $14,914.38 + $5,229.06 = $28,063.44
- Private use %: 100% − 68% = 32%
- Taxable value (pre-contribution): $28,063.44 × 32% × (335/365) = $8,241.16
- Less employee contribution: $2,000
- **Taxable value: $6,241.16**

## The engine's recommendation

Operating cost produces the lower taxable value ($6,241 vs $9,930), so — subject to the taxpayer's own election right — Method B minimises FBT.

## What the reviewer is being asked

1. Are the two calculation formulae correctly stated?
2. Is the days-available count correct (335)?
3. Is the deemed depreciation rate (25%) and deemed interest rate (statutory benchmark 8.77% for FY2025) correctly applied under s 11?
4. Does the log book qualify (12 weeks, 1 May to 24 July = ~12 weeks)?
5. Is the recipient's payment correctly subtracted from the pre-contribution taxable value?
6. Anything the engine is doing wrong or missing?
""",
        "forensic": """# Forensic Questions — Bounty #05

**Companion file to:** `01-brief.md`

Seven questions. Q4 is the load-bearing. Q7 is the open finder.

## Q1 (easy) — Statutory rate

What is the current statutory formula rate under s 9? Has it changed in recent years?

## Q2 (easy) — Log-book requirement

To use the operating cost method (s 10), what is the minimum log-book period? What must the log book record?

## Q3 (medium) — Base value definition

What does "base value" mean under s 9(2)? Include or exclude: on-road costs, dealer delivery, first-year registration, luxury car tax, GST, extended warranty, floor mats?

## Q4 (load-bearing) — Deemed depreciation and interest under s 11

The engine used a 25% deemed depreciation rate and an 8.77% deemed interest rate. Are those the correct rates for FY2025 FBT year? What is the statutory source of each rate? Have either changed in the last three FBT years?

_(This is where practitioners either know the numbers cold or need TR 2024/D3 or the ATO's FBT rates page. Reviewers should confirm from primary source.)_

## Q5 (medium) — Contribution mechanics

The employee paid $2,000 after-tax. Is that a "recipient's payment" or a "recipient's contribution", and does it matter? Which sub-section governs the reduction?

## Q6 (medium) — Election timing

The taxpayer can only make one election per car per FBT year. When is the election made — at time of return preparation, or does the log-book keeping itself constitute election?

## Q7 (open) — What's missing?

What is not being tested by this brief and worked example?

Candidates:
- The "log book year" vs "non-log-book year" distinction under s 10A (log book is valid for 5 FBT years)
- The reasonable estimate of operating costs where records are incomplete
- Multiple cars provided to the same employee
- Change of car mid-year
- Gross-up rate application (Type 1 vs Type 2)
""",
    },
    6: {
        "id": "bounty-06-fbt-car-parking",
        "title": "FBT car parking — commercial parking station threshold",
        "prize": 700,
        "hours": 2.5,
        "anchors": "s 39A FBTAA 1986; TR 2021/2",
        "calculator": "LodgeiT_FBT",
        "calc_version": "v0.2.0 (partial)",
        "brief": """# Bounty #06 — Public review brief: FBT Car Parking Threshold

**Bounty ID:** bounty-06-fbt-car-parking
**Domain:** Car parking fringe benefit — commercial parking station threshold test
**Statutory anchors:** s 39A FBTAA 1986; TR 2021/2
**Calculator target:** `lodgeit-labs/LodgeiT_FBT` at version v0.2.0 (partial implementation)
**Expected effort:** ~2.5 hours
**Prize:** AUD $700

---

## 1. Why this bounty exists

Post-TR 2021/2, the ATO's view of what constitutes a "commercial parking station" widened materially — parking previously outside the FBT net was pulled in. Employers who continue to rely on pre-2021 practice risk under-reporting.

The car-parking fringe benefit exists (broadly) when:

1. The employer provides parking to an employee at premises the employer owns or leases; AND
2. Within a 1-km radius, there is a **commercial parking station** whose lowest all-day fee exceeds the statutory threshold for the FBT year.

Our engine implements the threshold gate. This bounty asks whether the gate is correctly applied post-TR 2021/2.

## 2. What the calculator does

```
def car_parking_fringe_benefit_applies(employer_location, fbt_year):
    nearby_stations = find_commercial_parking_stations_within_1km(employer_location)
    if not nearby_stations:
        return False, "no commercial parking station within 1km"
    lowest_all_day_fee = min(s.all_day_fee for s in nearby_stations if s.is_all_day_parking)
    threshold = CAR_PARKING_THRESHOLD_TABLE[fbt_year]
    if lowest_all_day_fee > threshold:
        return True, f"threshold triggered: ${lowest_all_day_fee} > ${threshold}"
    return False, f"threshold not triggered: ${lowest_all_day_fee} <= ${threshold}"
```

## 3. Statutory anchors

- **s 39A FBTAA 1986** — the operative section defining car parking fringe benefit.
- **s 39A(1)(f)** — the "commercial parking station" limb.
- **TR 2021/2** — the current Commissioner's view.

## 4. Out of scope

- Taxable value calculation (once the fringe benefit is confirmed) — that is a downstream calculator.
- The "primary place of employment" test (s 39A(1)(a)).
- Salary-packaged parking under s 39F.
""",
        "worked_example": """# Worked Example — Bounty #06

**Companion file to:** `01-brief.md`

## The scenario

**Employer:** MNO Advisors Pty Ltd
**Employer premises:** Level 5, 88 Phillip Street, Sydney NSW 2000
**FBT year:** 1 April 2024 to 31 March 2025 (FY2025)
**Employees given parking:** 12 senior staff, at employer's leased basement bays.

## Commercial parking stations within 1km (per Google Maps radius search)

| # | Operator | Address | Distance | All-day fee (early bird) | All-day fee (walk-in) |
|---|---|---|---|---:|---:|
| 1 | Secure Parking | 2 Bond Street | 380m | $32 | $95 |
| 2 | Wilson Parking | 55 Hunter Street | 620m | $28 | $80 |
| 3 | Care Park | 175 Pitt Street | 890m | $25 | $75 |
| 4 | Church-owned "public" carpark (paid) | 100 Elizabeth Street | 720m | (no early bird — $30 all-day flat) | $30 |
| 5 | Hotel-owned public parking | Sofitel, Elizabeth Street | 950m | $40 | $80 |

## The engine's determination

**Step 1 — Identify commercial parking stations**

Under TR 2021/2, "commercial parking station" is broader than the pre-2021 practice. Stations 1, 2, 3 are unambiguously commercial. Stations 4 and 5 (church-owned, hotel-owned) — post-TR 2021/2 — are also commercial parking stations because they are held out to the general public for a fee.

**Step 2 — All-day parking?**

The engine's current position: "all-day parking" means the fee for parking for a continuous 6+ hour period during the day.
- Station 1: yes (early bird is 6+ hours, $32).
- Station 2: yes ($28).
- Station 3: yes ($25).
- Station 4: yes ($30).
- Station 5: yes ($40).

**Step 3 — Lowest fee**

The engine uses the lowest early-bird fee across all stations: **$25** (Station 3).

**Step 4 — Threshold for FY2025**

FBT car parking threshold for FY2025 (year ending 31 March 2025): $10.77 (ATO published rate).

$25 > $10.77 → **THRESHOLD TRIGGERED**.

## The engine's conclusion

Car parking fringe benefit applies for FY2025. Downstream taxable-value calculation kicks in.

## What the reviewer is being asked

1. Post-TR 2021/2, are stations 4 and 5 correctly treated as commercial parking stations?
2. Is "early bird" fee the correct proxy for "lowest all-day fee"? Or should the walk-in rate be used?
3. Is 6+ hours the correct definition of "all-day"?
4. Is the $10.77 threshold correct for FY2025?
5. Anything else the calculator is missing?
""",
        "forensic": """# Forensic Questions — Bounty #06

**Companion file to:** `01-brief.md`

## Q1 (easy) — Threshold

What is the FBT car parking threshold for FY2025 (year ending 31 March 2025), and what is the source?

## Q2 (easy) — 1km radius

Is the 1km radius measured straight-line or by walking distance? Which source authority resolves this?

## Q3 (load-bearing) — Post-TR 2021/2 scope

Before TR 2021/2, an employer might argue that parking at a hotel or a church-owned carpark was not a "commercial parking station" because it was ancillary to a primary business (hotel guests, church attendees). Post-TR 2021/2, is that argument still available?

_(The reviewer should cite the specific paragraphs of TR 2021/2 that expanded the ATO's view, and comment on whether that expansion is settled or still subject to challenge.)_

## Q4 (medium) — "All-day parking" definition

The engine assumes "all-day parking" means 6+ hours continuous parking. What does TR 2021/2 or its predecessor say about the minimum duration? Is there any authority for a longer requirement (e.g. 8 hours)?

## Q5 (medium) — "Lowest fee" methodology

If Station 3's early-bird rate requires arrival by 09:30 and departure after 15:30, but Station 1's early-bird rate has different constraints, is it correct to compare early-bird rates head-to-head? Or should the engine only use the fees that would apply to a "normal" employee's parking pattern?

## Q6 (open) — What's missing?

What has the engine not caught that a competent FBT practitioner would test?

Candidates:
- The "40% capacity rule" for whether a facility is a commercial parking station
- Parking that is provided on a shift-work basis
- Multiple employers in the same building sharing parking bays
- The residual-benefit alternative treatment for parking not caught by s 39A
""",
    },
    7: {
        "id": "bounty-07-hire-purchase-interest-apportionment",
        "title": "Hire purchase — interest apportionment",
        "prize": 550,
        "hours": 2,
        "anchors": "Div 240 ITAA 1997; s 240-25, s 240-40",
        "calculator": "HP_Calculator",
        "calc_version": "v0.1.5",
        "brief": """# Bounty #07 — Public review brief: Hire Purchase Interest Apportionment

**Bounty ID:** bounty-07-hire-purchase-interest-apportionment
**Domain:** Division 240 hire purchase / notional loan
**Statutory anchors:** Div 240 ITAA 1997; s 240-25, s 240-40
**Calculator target:** `lodgeit-labs/HP_Calculator` at version v0.1.5
**Expected effort:** ~2 hours
**Prize:** AUD $550

---

## 1. Why this bounty exists

Division 240 recasts a hire-purchase or luxury car lease as a **notional sale + notional loan** for income tax purposes. The consequences:

- The financier is treated as making a notional loan to the hirer.
- The hirer is treated as owning the asset from inception, and is entitled to depreciation.
- The instalments are notionally split into principal repayment (non-deductible for the hirer, non-assessable for the financier) and interest (deductible for the hirer under s 8-1, assessable for the financier).

The interest apportionment method matters. Two common methods:

- **Actuarial method** — economically correct; higher interest in early years, lower later.
- **Rule of 78 (sum-of-years-digits)** — approximation; front-loads interest more aggressively than actuarial for standard-term contracts.

Our engine implements the actuarial method by default and offers Rule-of-78 as an option (some legacy contracts documented on Rule-of-78 basis).

## 2. What the calculator does

**Actuarial:**
```
periodic_interest = opening_principal × periodic_rate
periodic_principal = payment - periodic_interest
closing_principal = opening_principal - periodic_principal
```

**Rule of 78 (for 60-month contract):**
```
total_interest = sum_of_all_payments - notional_cash_price
digits_total = 60 × 61 / 2 = 1830
month_1_interest = total_interest × (60 / 1830)
month_2_interest = total_interest × (59 / 1830)
...
```

## 3. Out of scope

- Whether the contract is caught by Div 240 at all (that's a scope question upstream).
- GST treatment (Div 240 has its own GST rules; separate bounty candidate).
- The balloon-payment treatment on early termination.
- Luxury car lease under Div 242 (adjacent but distinct).
""",
        "worked_example": """# Worked Example — Bounty #07

**Companion file to:** `01-brief.md`

## The scenario

**Hirer:** PQR Manufacturing Pty Ltd
**Financier:** XYZ Finance Ltd
**Asset:** Industrial CNC lathe
**Notional cash price:** $80,000
**Deposit:** $8,000
**Financed amount:** $72,000
**Term:** 60 months (5 years)
**Monthly instalment:** $1,540
**Total instalments over term:** $92,400
**Total notional interest:** $92,400 − $72,000 = **$20,400**

## The engine's actuarial breakdown (first year)

Effective monthly interest rate (from the actuarial solve): 0.5417% per month (approx 6.5% p.a.)

| Month | Opening balance | Interest | Principal | Closing balance |
|---:|---:|---:|---:|---:|
| 1 | $72,000.00 | $390.06 | $1,149.94 | $70,850.06 |
| 2 | $70,850.06 | $383.83 | $1,156.17 | $69,693.89 |
| 3 | $69,693.89 | $377.57 | $1,162.43 | $68,531.46 |
| ... | ... | ... | ... | ... |
| 12 | $58,943.15 | $319.28 | $1,220.72 | $57,722.43 |

**Year 1 total interest (actuarial): $4,258** (approx)

## The engine's Rule-of-78 breakdown (first year)

Sum-of-months = 60 × 61 / 2 = 1830

| Month | Weight | Interest |
|---:|---:|---:|
| 1 | 60/1830 | $668.85 |
| 2 | 59/1830 | $657.70 |
| 3 | 58/1830 | $646.56 |
| ... | ... | ... |
| 12 | 49/1830 | $546.23 |

**Year 1 total interest (Rule-of-78): $7,341** (approx — front-loaded)

## The reconciliation

Over the full 60 months, both methods sum to $20,400. The distribution differs:

| Year | Actuarial interest | Rule-of-78 interest | Difference |
|---:|---:|---:|---:|
| 1 | $4,258 | $7,341 | +$3,083 |
| 2 | $3,564 | $5,984 | +$2,420 |
| 3 | $2,824 | $4,628 | +$1,804 |
| 4 | $2,036 | $3,272 | +$1,236 |
| 5 | $1,196 | $1,913 | +$717 |
| **Total** | **$13,878** | **$23,138** | — |

_(Numbers illustrative; exact figures depend on precise rate solve.)_
""",
        "forensic": """# Forensic Questions — Bounty #07

**Companion file to:** `01-brief.md`

## Q1 (easy) — Division 240 characterisation

Under s 240-25, what is the criteria for a hire-purchase agreement to be caught by Division 240?

## Q2 (easy) — Deductible interest

Under Division 240, is the notional interest deductible under s 8-1 to the hirer? What is the source of the deduction?

## Q3 (load-bearing) — Actuarial vs Rule-of-78 which is required?

Does Division 240 mandate the actuarial method, or does it permit Rule-of-78? What is the source authority?

_(The reviewer should trace this to s 240-40 and any relevant ATO Interpretive Decisions.)_

## Q4 (medium) — Balloon payment

Suppose the contract has a $10,000 balloon at month 60 (with the monthly instalments reduced accordingly). Does the balloon get its own interest apportionment, or is it treated as final principal?

## Q5 (medium) — Early termination

If PQR terminates the contract at month 36 by paying out the residual, how is the interest apportionment closed out? Does un-earned interest under Rule-of-78 get refunded, and how is it recognised for tax?

## Q6 (open) — What's not being tested?

Candidates:
- Interaction with Div 40 depreciation of the underlying asset
- GST on financed component
- Financier-side assessability recognition (matched or differed?)
- Contract in a foreign currency
""",
    },
    8: {
        "id": "bounty-08-cgt-sb-15-year-exemption",
        "title": "CGT small business 15-year exemption",
        "prize": 900,
        "hours": 3,
        "anchors": "Subdiv 152-B ITAA 1997; s 152-105, s 152-110",
        "calculator": "Spec-first (no existing calculator)",
        "calc_version": "spec-v0",
        "brief": """# Bounty #08 — Public review brief: CGT SB 15-Year Exemption

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
""",
        "worked_example": """# Worked Example — Bounty #08

**Companion file to:** `01-brief.md`

## The scenario

**Taxpayer:** Wilson Family Trust (discretionary trust; trustee is Wilson Nominees Pty Ltd)
**Beneficiaries:** Bob Wilson (68), his wife Maree Wilson (65), their adult children (× 2)
**Trust asset:** 100% shareholding in Wilson Trading Pty Ltd, which operates a family cabinetmaking business.
**Trust acquired the shareholding:** July 2008 (16.5 years continuous ownership)
**Bob's role:** Managing director of Wilson Trading; drawing a salary and franked distributions from the trust for 16 years.
**Disposal event:** Sale of the entire shareholding to a third-party acquirer on 15 September 2024.
**Sale proceeds:** $4.2M
**Trust's cost base in the shares:** $50,000 (initial capitalisation)
**Capital gain:** approximately $4.15M
**Bob's stated intention:** He will fully retire from active business involvement on completion; he is 68.

## The engine spec's target evaluations

**Basic conditions (s 152-10):**
- CGT event A1 on the shares? YES
- Would produce a capital gain? YES
- SBE (aggregated turnover < $2M) OR MNAV ($6M net assets)? The trust's MNAV needs testing — likely PASS given the small operation.
- Active-asset test — s 152-40(3): shares in a company can qualify if the underlying company is a "small business active asset" holder for the majority of ownership. Need to test.

**15-year exemption specific conditions (s 152-110):**
- 15+ years continuous ownership? YES (16.5 years).
- "Significant individual" test throughout? The reviewer must confirm Bob has been a significant individual (as defined in s 152-55) at all times.
- Significant individual at disposal age 55+ retiring or incapacitated? Bob is 68, retiring — YES.

## The spec's predicted verdict

Subject to the active-asset test and significant-individual test passing on the facts, the trust is eligible for the full 15-year exemption. Consequence: **the $4.15M capital gain is fully disregarded** under s 152-110.

## What the reviewer is being asked

1. Have I correctly identified all the basic conditions?
2. Is the "significant individual" test correctly framed?
3. Are there any lurking conditions in Subdivision 152-B that the calculator must additionally test?
4. Post-exemption, what does the trust do with the proceeds — any downstream CGT event on distribution to Bob?
5. Any authority (case law, ATO ruling) I've missed that changes the analysis?
""",
        "forensic": """# Forensic Questions — Bounty #08

**Companion file to:** `01-brief.md`

Seven questions. Q4 is the load-bearing. Q7 is the open finder.

## Q1 (easy) — Which sub-section for a discretionary trust

Does s 152-105 (individual) or s 152-110 (company/trust) apply to a discretionary trust like the Wilson Family Trust?

## Q2 (easy) — 15-year measurement

Is the 15-year period measured from the date the trust acquired the shares (2008) or from some earlier point (e.g. when Bob commenced business)?

## Q3 (medium) — Significant individual definition

Under s 152-55, what makes Bob a "significant individual" of the trust? Does he need to be a beneficiary, or does his controlling-influence over the trustee suffice?

## Q4 (load-bearing) — Active asset test for the shares

Under s 152-40(3), when do shares in a company qualify as an active asset? Given that the underlying company (Wilson Trading Pty Ltd) is actively carrying on business, is the test automatically satisfied, or is there a threshold test on the balance sheet composition?

_(Reviewers should trace through the "80% test" — market value of active assets ≥ 80% of total market value — and comment on how it applies to Wilson Trading's balance sheet.)_

## Q5 (medium) — Retirement nexus

Bob is 68 and stated to be "retiring". Is his mere statement of intent sufficient, or does the ATO require a demonstrable step-down from active business involvement? What if Bob remains a $1,000-per-annum non-executive advisor?

## Q6 (medium) — Distribution to Bob

Post-disposal, the trust holds ~$4.2M in cash. Assuming the trustee distributes this to Bob:
- Is the distribution itself a further CGT event?
- Does s 152-125 (payments through interposed entities) apply?
- Is there a time limit for the distribution to preserve the exemption benefit?

## Q7 (open) — What have I missed?

What edge case or additional authority would you want a calculator to test that this brief has not surfaced?

Candidates:
- Multi-generation asset holding (asset acquired by earlier trustee, current trustee inherited)
- Change of trust structure during the 15-year period
- Partial disposal (sell 60% of shares, retain 40%)
- Roll-over into a replacement asset before the 15-year mark expired
""",
    },
    9: {
        "id": "bounty-09-cgt-active-asset-test",
        "title": "CGT small business active-asset test",
        "prize": 750,
        "hours": 2.5,
        "anchors": "s 152-35, s 152-40 ITAA 1997; TR 2019/1",
        "calculator": "Spec-first (no existing calculator)",
        "calc_version": "spec-v0",
        "brief": """# Bounty #09 — Public review brief: CGT SB Active-Asset Test

**Bounty ID:** bounty-09-cgt-active-asset-test
**Domain:** CGT small business — active-asset test
**Statutory anchors:** s 152-35, s 152-40 ITAA 1997; TR 2019/1
**Calculator target:** **Spec-first bounty** — no existing calculator. Reviewer authors the ratification spec.
**Expected effort:** ~2.5 hours
**Prize:** AUD $750

---

## 1. Why this bounty exists

The active-asset test is a gating condition for all four SB CGT concessions (15-year exemption, 50% reduction, retirement exemption, rollover). It is applied per asset. It has three components:

1. **Definition of active asset** — s 152-40 lists what counts (used in business, held ready for use, intangibles connected to business).
2. **Exclusions** — s 152-40(4) excludes assets whose main use is deriving rent, interest, annuities, royalties, or holding foreign-currency-fluctuation instruments.
3. **Half-of-ownership test** — s 152-35: the asset must have been an active asset for at least half the period of ownership (or 7.5 years if owned > 15 years).

TR 2019/1 clarifies the "main use" test for mixed-use assets, especially commercial premises partly rented out.

We do not yet have a calculator for this. This bounty asks a competent CGT practitioner to author the ratification spec.

## 2. What the spec must cover

- Component 1: is the asset within the s 152-40(1) inclusive list?
- Component 2: is it excluded under s 152-40(4)?
- Component 3: has it been an active asset for the qualifying period?
- The TR 2019/1 mixed-use methodology — proportional main-use analysis.
- Interaction with connected-entity holding (asset held by one entity but used by a connected entity — s 152-40(1A)).

## 3. Out of scope

- The other SB CGT concessions' additional conditions (see Bounty #8 for 15-year).
- Non-SB CGT event characterisation.
- GST on the underlying disposal.
""",
        "worked_example": """# Worked Example — Bounty #09

**Companion file to:** `01-brief.md`

## The scenario

**Taxpayer:** STU Investments Pty Ltd
**Asset:** Commercial building at 15 Industrial Drive, Perth WA.
**Acquired:** March 2010 for $850,000 (14.5 years ownership at time of CGT event).
**Use during ownership:**
- **Years 1–5 (2010–2015):** 100% owner-occupied for taxpayer's steel-fabrication business.
- **Years 6–10 (2015–2020):** 60% owner-occupied (business scaled down); 40% leased to unrelated third-party tenant on commercial lease.
- **Years 11–14.5 (2020–2024):** 30% owner-occupied (further scale-down); 70% leased to two unrelated tenants.
- **Disposal event:** Sale to an unrelated buyer, September 2024, for $2.6M.

## The spec's target evaluation

**Component 1 (s 152-40(1)):** The building is used, or held ready for use, in the course of carrying on a business. → YES for the owner-occupied portion, in each year.

**Component 2 (s 152-40(4)) — "main use to derive rent" exclusion:** This is the load-bearing question. The reviewer must determine, per year, whether the "main use" of the building was to derive rent.

Per TR 2019/1, the main-use test is applied on a proportional basis. If more than half the building (by floor area, or by rental value, or by another reasonable proxy) is used to derive rent, the asset's main use is to derive rent and it is excluded.

Applying per year:
- Years 1–5: 100% owner-occupied. Main use = business. **ACTIVE.**
- Years 6–10: 60% owner-occupied, 40% rented. Main use = business (owner-occupancy majority). **ACTIVE.**
- Years 11–14.5: 30% owner-occupied, 70% rented. Main use = rent. **EXCLUDED.**

**Component 3 (s 152-35) — half-of-ownership test:**

Total ownership: 14.5 years.
Half required: 7.25 years.
Active-asset years: 5 (years 1–5) + 5 (years 6–10) = **10 years**. Excluded years: 4.5 (years 11–14.5).

10 > 7.25 → **TEST PASSED**.

## The spec's predicted verdict

The building satisfies the active-asset test at disposal, notwithstanding that the most recent 4.5 years were excluded. It qualifies as an active asset for the purpose of the SB CGT concessions.

## What the reviewer is being asked

1. Is the proportional main-use test correctly applied?
2. Is "floor area" the correct proxy, or should rental value be used?
3. Is the half-of-ownership test correctly measured (10 years active vs 4.5 years excluded)?
4. What if the taxpayer had had a 12-month gap in years 8–9 where the building was vacant (not occupied, not rented)?
5. Would the interposed-entity test under s 152-40(1A) change the analysis if STU Investments had leased the building to a connected operating entity (rather than being the operator itself)?
""",
        "forensic": """# Forensic Questions — Bounty #09

**Companion file to:** `01-brief.md`

## Q1 (easy) — Active asset definition

What are the three main limbs of the active-asset definition under s 152-40(1)?

## Q2 (easy) — Rent exclusion

Under s 152-40(4)(e), what is the "main use to derive rent" exclusion? Does it apply automatically once rent is derived, or is there a proportional test?

## Q3 (load-bearing) — TR 2019/1 methodology

Per TR 2019/1, how does the ATO determine whether the "main use" of a mixed-use property is to derive rent? What proxies (floor area, rental value, time) does the ruling accept?

_(The reviewer should cite the specific paragraphs of TR 2019/1 that establish the proportional methodology.)_

## Q4 (medium) — Half-of-ownership test

Under s 152-35, the asset must be an active asset for at least half the ownership period. In the worked example, does the vacant period (if it existed) count toward active-asset time, excluded time, or neither?

## Q5 (medium) — Connected-entity use

If STU Investments leased the building to a related operating entity (e.g. STU Fabrication Pty Ltd, wholly-owned subsidiary), does s 152-40(1A) allow the connected entity's business use to count for STU Investments? What conditions apply?

## Q6 (open) — What's missing?

What is not tested by this brief that a calculator would need to handle?

Candidates:
- Assets used partly in an FBT-attributable activity
- Assets leased at below-market rent to a connected entity
- Change of trust structure or partnership composition during ownership
- Improvements to the asset that change its character
""",
    },
    10: {
        "id": "bounty-10-psi-attribution",
        "title": "PSI attribution — 80/20 and results test",
        "prize": 850,
        "hours": 3,
        "anchors": "Div 84–87 ITAA 1997; s 87-15, 87-18, 87-20, 87-25, 87-30",
        "calculator": "Spec-first (no existing calculator)",
        "calc_version": "spec-v0",
        "brief": """# Bounty #10 — Public review brief: PSI Attribution — 80/20 and Results Test

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
""",
        "worked_example": """# Worked Example — Bounty #10

**Companion file to:** `01-brief.md`

## The scenario

**Entity:** VWX IT Consulting Pty Ltd
**Directors/Shareholders:** Jason (100%)
**Financial year:** FY2024–25
**PSI (gross):** $340,000
**Clients:**

| Client | Revenue | % of PSI | Contract type | Relationship to Jason |
|---|---:|---:|---|---|
| BigBankCorp | $210,000 | 61.8% | 12-month rolling engagement | Unrelated |
| MidTierAccounting | $85,000 | 25.0% | Project-based | Unrelated |
| StartupTechCo | $35,000 | 10.3% | Project-based | Unrelated |
| Jason's brother-in-law | $10,000 | 2.9% | Ad-hoc | Related |
| **Total** | **$340,000** | **100%** | | |

## The engine spec's target evaluations

**Step 1 — Is this PSI?**
Yes — the income is characterised as PSI under s 84-5 (paid mainly for Jason's personal skill).

**Step 2 — 80% rule test (s 87-15(3)):**
BigBankCorp represents 61.8% of PSI. This is less than 80%, so the results test is **not** mandatorily-imposed. The entity may satisfy any of the four PSB tests.

**Step 3 — Unrelated clients test (s 87-20):**
The test:
- (a) The individual gains or produces income from providing services to two or more entities that are unrelated to the individual and to each other; AND
- (b) The services are provided as a direct result of the individual making offers or invitations to the public at large (or a section of the public).

Sub-test (a): BigBankCorp + MidTierAccounting + StartupTechCo are all unrelated to Jason and to each other. **PASS.**

Sub-test (b): This is the load-bearing sub-test. Did Jason obtain these clients by "offers or invitations to the public"? Word-of-mouth referrals typically do not satisfy this test. A LinkedIn profile advertising services might. A website, active marketing, or bidding on public tenders would.

If Jason obtained BigBankCorp through a former-colleague introduction, that alone does not satisfy the test. If Jason additionally maintains an active website and has done tender responses to other government-sector work, the test may be satisfied.

**Step 4 — Alternative PSB tests:**

- **Results test:** would require (i) Jason produces a result, (ii) Jason supplies plant/tools/equipment to produce the result, (iii) Jason is liable for cost of rectifying defective work. IT consulting engagements structured as time-and-materials rarely satisfy this test.
- **Employment test:** would require Jason to engage other individuals to perform ≥ 20% of the principal work. Fails if Jason is solo.
- **Business premises test:** would require exclusive-use premises, not shared or home-office. Fails if Jason works from a home study.

## The spec's predicted verdict

Subject to whether sub-test (b) of the unrelated clients test is satisfied by Jason's marketing evidence:
- If YES: VWX IT is a PSB, attribution does not apply, ordinary corporate tax treatment.
- If NO: VWX IT is not a PSB, PSI is attributed to Jason under Div 86, taxed at his marginal rate.

## What the reviewer is being asked

1. Is the 80% test correctly framed (mandatory-imposition of results test if > 80% from one source)?
2. Is sub-test (b) of the unrelated clients test correctly interpreted — what evidence typically satisfies it?
3. Are the results, employment, and business-premises tests correctly framed?
4. What about the related client ($10,000 from brother-in-law) — does related-party PSI need separate treatment?
5. Attribution mechanics under Div 86 — is there anything the spec is missing?
""",
        "forensic": """# Forensic Questions — Bounty #10

**Companion file to:** `01-brief.md`

Seven questions. Q3 is the load-bearing. Q7 is the open finder.

## Q1 (easy) — Threshold

Under s 87-15(3), when is the results test mandatorily imposed as the sole path to PSB status?

## Q2 (easy) — Four tests

Name the four PSB tests and cite the section for each.

## Q3 (load-bearing) — Unrelated clients test sub-test (b)

Under s 87-20(1)(b), what does "offers or invitations to the public" mean? Does maintaining a LinkedIn profile count? Does responding to invitations from a third-party recruiter count? What evidence typically satisfies this test?

_(Reviewers should cite ATO Interpretive Decisions and any relevant case law.)_

## Q4 (medium) — Results test

Under s 87-18, all three limbs must be satisfied. What are the three limbs, and how do time-and-materials versus fixed-price engagements typically fare against each limb?

## Q5 (medium) — Employment test

Under s 87-25, the entity must engage others to perform "≥ 20% of the principal work". Does administrative help count (bookkeeper, EA)? Does a contract sub-contractor count?

## Q6 (medium) — Attribution mechanics

If no PSB test is passed, Div 86 attributes the net PSI to the individual. What is the mechanism — is it deemed salary, deemed dividend, or something else? How does it interact with the PAYG withholding regime?

## Q7 (open) — What's missing?

Candidates:
- Interposed-entity structures (trust distributing to a company distributing to Jason)
- PSI earned through partnerships
- Change of PSB status mid-year
- The general anti-avoidance provisions (Part IVA) potentially applying even where PSB is passed
""",
    },
}


# -----------------------------------------------------------------------------
# TaxGenii appendix — per-bounty pre-loaded statute citations
# -----------------------------------------------------------------------------

def taxgenii_appendix_for(b):
    return f"""# TaxGenii Statutory Appendix — {b['title']}

**Bounty:** {b['id']}
**Statutory anchors:** {b['anchors']}

---

## About this appendix

This appendix is pre-cached from our internal ATO-legislation knowledge base (Tax Genii). It surfaces the primary statutory sections, ATO rulings, and relevant case law for the bounty. **You do not need to hunt sources** — the load-bearing citations are here.

**Freshness caveat:** Tax Genii is indexed to a specific snapshot of the ATO legal database (see version below). Very recent High Court decisions or ATO announcements post-dating the snapshot may not appear. If the bounty question turns on a very recent authority, please note it in your verdict under "coverage gap".

**Snapshot version:** taxgenii-2.0-2026-06 (ITAA 1936, ITAA 1997, FBTAA 1986, GSTA 1999, TAA 1953, ATO rulings and TDs to June 2026, case law to Full Federal Court 2025).

---

## Primary statutory sections

_[Content authored per-bounty by the reviewer during their read. This section normally contains the pasted operative sections; for the public-dispatch version of this bounty, we invite the reviewer to consult the ATO Legal Database or Austlii for the full text and cite specific sub-sections in their verdict.]_

Key links:
- **Austlii ITAA 1997** — https://www.austlii.edu.au/cgi-bin/viewdb/au/legis/cth/consol_act/itaa1997240/
- **Austlii ITAA 1936** — https://www.austlii.edu.au/cgi-bin/viewdb/au/legis/cth/consol_act/itaa1936240/
- **Austlii FBTAA 1986** — https://www.austlii.edu.au/cgi-bin/viewdb/au/legis/cth/consol_act/fbtaa1986312/
- **ATO Legal Database** — https://www.ato.gov.au/law

---

## Anchors specific to this bounty

**{b['anchors']}**

The reviewer should:
1. Read the operative sections in full from primary source.
2. Cite the specific sub-section(s) in each verdict answer.
3. Note any interpretive tension or ambiguity in the drafting.

---

## Relevant ATO rulings and determinations

_[Bounty-specific ATO ruling list — reviewer to consult the ATO Legal Database for current versions.]_

---

## Relevant case law

_[Bounty-specific case-law list — reviewer to consult Austlii or ATO Legal Database.]_

---

## Coverage gap reporting

If Tax Genii's coverage of any critical authority is thin (e.g. an important ATO ruling is not indexed, or a recent case is missing), please flag it in section 5 of your reviewer verdict template. This feedback goes back to our knowledge-base team.

---

**Prepared by:** LodgeiT Labs — Tax Genii team
**For:** {b['id']} public review bounty
"""


# -----------------------------------------------------------------------------
# Main
# -----------------------------------------------------------------------------

def write_artefacts(bounty_num, content):
    bounty_dir = BOUNTIES_DIR / f"bounty-{bounty_num:02d}-{content['id'].split('-', 2)[-1]}"
    # Re-derive slug from id for robustness
    slug = content["id"].replace(f"bounty-{bounty_num:02d}-", "")
    bounty_dir = BOUNTIES_DIR / f"bounty-{bounty_num:02d}-{slug}"
    artefacts_dir = bounty_dir / "artefacts"
    artefacts_dir.mkdir(parents=True, exist_ok=True)

    (artefacts_dir / "01-brief.md").write_text(content["brief"])
    (artefacts_dir / "02-worked-example.md").write_text(content["worked_example"])
    (artefacts_dir / "03-forensic-questions.md").write_text(content["forensic"])
    # Extract question count from forensic content
    num_q = content["forensic"].count("## Q") - content["forensic"].count("## Q_") if "## Q" in content["forensic"] else 6
    # More reliable: parse
    import re
    q_nums = re.findall(r"## Q(\d+)", content["forensic"])
    num_q = max(int(n) for n in q_nums) if q_nums else 6
    (artefacts_dir / "04-reviewer-verdict-template.md").write_text(
        verdict_template(content["id"], content["title"], content["anchors"], num_q)
    )
    (artefacts_dir / "05-taxgenii-appendix.md").write_text(taxgenii_appendix_for(content))
    (artefacts_dir / "06-terms.md").write_text(terms_for(content["id"], content["prize"], content["hours"]))
    print(f"  bounty {bounty_num:02d}: 6 artefact files")


def bounty_01_additional_files():
    """Bounty 1 has 01-04 from Holly (sanitised); add 05 and 06."""
    bounty_dir = BOUNTIES_DIR / "bounty-01-div7a-minimum-yearly-repayment"
    artefacts_dir = bounty_dir / "artefacts"

    bounty_01_content = {
        "id": "bounty-01-div7a-myr",
        "title": "Div 7A Minimum Yearly Repayment",
        "prize": 550,
        "hours": 2,
        "anchors": "s 109E, s 109N, s 109D ITAA 1936",
    }

    (artefacts_dir / "05-taxgenii-appendix.md").write_text(taxgenii_appendix_for(bounty_01_content))
    (artefacts_dir / "06-terms.md").write_text(
        terms_for(bounty_01_content["id"], bounty_01_content["prize"], bounty_01_content["hours"])
    )
    print("  bounty 01: added 05 + 06")


def main():
    print("Building bounty artefact bundles...")
    bounty_01_additional_files()
    for num in range(2, 11):
        content = BOUNTY_CONTENT[num]
        write_artefacts(num, content)
    print("Done.")


if __name__ == "__main__":
    main()
