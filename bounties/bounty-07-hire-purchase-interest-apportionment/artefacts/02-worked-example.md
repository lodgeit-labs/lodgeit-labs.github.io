# Worked Example — Bounty #07

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
