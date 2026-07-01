# Bounty #03 — Public review brief: Instant Asset Write-Off Eligibility

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
