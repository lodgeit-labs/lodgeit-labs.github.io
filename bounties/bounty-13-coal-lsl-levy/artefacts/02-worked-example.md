# Worked example — Coal LSL levy

One eligible employee, **base-rate branch**, reporting month **June 2026**, chosen so that
**Formula B wins** and the levy lands on a half-cent (so the final-step rounding actually bites).
This is fixture `F2-base-rate-formula-b-wins` from the contributor's suite.

## Request

```
POST /v1/calculators/urn:sbrm:calculator:coal-lsl:levy/urn:sbrm:period:coal-lsl-levy:2026-06
```

Against the contributor's base `https://coal-lsl-levy.coal-lsl-levy-service.workers.dev`:

```sh
curl -s -X POST \
  "https://coal-lsl-levy.coal-lsl-levy-service.workers.dev/v1/calculators/urn:sbrm:calculator:coal-lsl:levy/urn:sbrm:period:coal-lsl-levy:2026-06" \
  -H "Content-Type: application/json" \
  -d '{
    "reporting_month": "2026-06",
    "branch": "base_rate",
    "employee": { "eligible_employee": true },
    "pay": {
      "base_rate_of_pay": "6000.00",
      "salary_sacrificed": "0.00",
      "overtime_and_penalty_rates": "3000.00",
      "allowances": "500.00",
      "allowances_exclude_expense_reimbursements": true,
      "bonuses": []
    }
  }'
```

## Hand derivation (s 3B(1), base-rate branch)

- **Formula A** = base rate of pay including incentive payments and bonuses = **6000.00**.
- **Formula B** = 0.75 × (base rate + overtime/penalty rates + allowances other than expense
  reimbursements) = 0.75 × (6000.00 + 3000.00 + 500.00) = 0.75 × 9500.00 = **7125.00**.
- **Eligible wages** = greater of A and B = **7125.00** (Formula B wins).
- **Levy** = 7125.00 × **2.7%** = 7125.00 × 0.027 = **192.375**, rounded half up to cents →
  **192.38**.

## Expected live response (the engine must reproduce these)

```
branch.code              "s 3B(1)"
eligible_wages           "7125.0000"
workings.formula_a       "6000.00"
workings.formula_b       "7125.0000"
workings.winner          "formula_b"
rate.value_percent       "2.7000"
levy_before_rounding     "192.37500000"
levy                     "192.38"
rounding.differs         true
```

Note the scales: eligible wages and Formula B carry quarter cents at 4 dp; `levy_before_rounding`
is exact at 8 dp; the final `levy` is money at 2 dp after one half-up rounding. Each computed
response also carries rate/method content hashes, statutory citations, the engine source hash,
version and `code_revision`.

## Reviewer hooks (where to push)

- **The 2.7% rate** is reported from the contributor's pinned source (`methods.json`, record
  `s3b-from-2024-01`), **not** independently re-derived by LodgeiT. **Verify it** against the
  current levy regulations for June 2026, and for every served month (Jan 2024 – Aug 2026).
- **Formula B's 0.75 factor** and its component set (base + OT/penalty + non-reimbursement
  allowances) — confirm against s 3B(1)(b).
- **The single final half-up rounding** (192.375 → 192.38) is the contributor's documented choice.
  Is that the correct treatment for a levy return, or does the regulation prescribe otherwise?
- Compare a **Formula-A-wins** case (fixture `F1`: base 6000.00, nil else → levy 162.00 exactly)
  and the **exact-tie** case (fixture `F8`) to test the "greater of" tie-break.

*Not advice. Figures are reported from the contributor's pinned source at `53ba9b8`; the rate and
rounding treatment are exactly what this bounty asks you to ratify.*
