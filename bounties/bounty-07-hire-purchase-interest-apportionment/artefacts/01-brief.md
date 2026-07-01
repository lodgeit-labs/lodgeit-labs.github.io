# Bounty #07 — Public review brief: Hire Purchase Interest Apportionment

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
