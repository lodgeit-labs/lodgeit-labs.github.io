# Bounty #04 — Public review brief: Small Business General Pool

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
    pre_write_off_balance = opening_balance + sum(a.cost for a in additions) \
                            - sum(d.termination_value for d in disposals) \
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
