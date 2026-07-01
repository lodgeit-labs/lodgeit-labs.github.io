# Bounty #05 — Public review brief: FBT Car — Statutory Formula vs Operating Cost

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
