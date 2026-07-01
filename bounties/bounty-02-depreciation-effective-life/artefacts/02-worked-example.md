# Worked Example — Bounty #02

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
