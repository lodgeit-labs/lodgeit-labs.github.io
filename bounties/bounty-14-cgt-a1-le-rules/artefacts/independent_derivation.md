# Independent derivation — 12 CGT scenarios (worked by hand from the statute notes)

Sources used: `/home/claude/run/statute_notes.md` and `/home/claude/run/indep/facts_only.txt` only. No `.le` file, test file or reasoner was consulted. One extra provision (s 110-45(2)) was checked via Tax Genii because the notes only mention the deducted-amount rule for the *reduced* cost base (s 110-55(4)); see s13.

Conventions
- Income year Y = year ending 30 June Y. Time of CGT event A1 = contract date (s 104-10(3)); gain/loss made at that time (s 102-20) and returned in that year (TD 94/89).
- Capital proceeds = money + market value of property received (s 116-20(1)), subject to s 116-30.
- Cost base = sum of the five elements (s 110-25); only first element facts are given unless stated. Reduced cost base = same elements except the third, less amounts deducted/deductible (s 110-55(2),(4)).
- Gain if proceeds > cost base; loss if proceeds < reduced cost base (s 104-10(4)). If proceeds fall between RCB and CB (or equal both), neither.
- 12-month test (s 115-25(1), TD 2002/10): acquisition day and event day both excluded; at least 365 clear days must lie between them (366 where the clear period must include a 29 February to make a full year). Equivalently the event must fall strictly after the first anniversary of acquisition.
- Discount percentage: 50% individual (s 115-100(a)), unless s 115-105 applies (then s 115-115).
- Method statement s 102-5(1): Step 1 current-year losses v current-year gains (order chosen by taxpayer); Step 2 prior-year net capital losses (earliest first, s 102-15); Step 3 discount; Step 5 sum. Collectable losses only against collectable gains (s 108-10(1)); excess carried forward (s 108-10(4)).

---

## s7 — "ordering" (zeta, individual). All events in income year 2025.

**d1 land one** (contract 2024-12-01; acquired 2020-01-01)
- Proceeds 30,000 (s 116-20). Cost base 10,000; RCB 10,000 (s 110-25(2), s 110-55).
- Gain = 30,000 − 10,000 = **20,000** (s 104-10(4)).
- 12-month test: 2020-01-01 → 2024-12-01, well over a clear year → discount capital gain (ss 115-5, 115-10(a), 115-25). 50%.

**d2 shares three** (contract 2025-01-15; acquired 2024-09-01)
- Proceeds 9,000; CB 5,000. Gain = **4,000**. Clear days between 2024-09-01 and 2025-01-15 ≈ 135 → not a discount gain.

**d3 shares four** (contract 2025-02-01; acquired 2021-01-01)
- Proceeds 6,000; RCB 12,000. Loss = 12,000 − 6,000 = **6,000**.

**Net capital gain 2025** (s 102-5)
- Step 1, chosen order (loss against the non-discount gain first, which is the taxpayer-optimal choice): 6,000 loss → d2 gain 4,000 reduced to 0; remaining loss 2,000 → d1 gain 20,000 reduced to 18,000.
- Step 2: no prior-year losses.
- Step 3: 18,000 × 50% = 9,000.
- Step 5: **net capital gain = 9,000**.
- Alternative order (loss applied wholly against d1 first): d1 20,000 − 6,000 = 14,000 → discount → 7,000; d2 4,000 unreduced; total **11,000**. The Act leaves the choice to the taxpayer ("you choose the order", Step 1); 9,000 is the result under the optimal order.
- No net capital loss, nothing carried forward.

---

## s8 — "collectables" (eta, individual). All events in income year 2025.

**d1 painting** (collectable, s 108-10(2)(a); contract 2024-08-08; acquired 2019-03-03)
- First element 2,000 > 500, so s 118-10(1) does not disregard it.
- Proceeds 2,200; CB 2,000. Gain = **200** (collectable gain). Over 12 months → discount gain (50%).

**d2 coin** (collectable; contract 2024-09-09; acquired 2022-02-02)
- First element 1,000 > 500, not disregarded by s 118-10(1).
- Proceeds 600; RCB 1,000. Loss = **400** (collectable loss).

**d3 shares five** (contract 2024-10-10; acquired 2023-05-05)
- Proceeds 1,500; CB 1,000. Gain = **500**. Clear days between 2023-05-05 and 2024-10-10 = 523 ≥ 365 → discount gain (50%).

**Net capital gain 2025**
- s 108-10(1): the 400 collectable loss can only reduce the 200 collectable gain: 200 − 400 → collectable gain 0; unapplied collectable loss 200.
- Step 1 (other gains): 500, no other losses available (the collectable loss is quarantined).
- Step 2: none. Step 3: 500 × 50% = 250.
- **Net capital gain = 250.**
- **Net capital loss from collectables carried forward = 200** (s 108-10(4)); applied in a later year in which collectable gains exceed collectable losses. (This mirrors the example in s 108-10 itself.)
- No general net capital loss.

---

## s10 — "prior losses exceed" (theta, individual). Income year 2025.

**d1 land one** (contract 2024-12-01; acquired 2020-01-01)
- Proceeds 30,000; CB 10,000. Gain = **20,000**; discount-eligible (over 12 months).

**Net capital gain 2025**
- Step 1: no current-year losses → 20,000.
- Step 2: prior-year net capital loss 25,000 (income year 2022) applied: 20,000 − 20,000 = 0. Only 20,000 of the 25,000 is utilised (s 960-20(1) / s 102-15).
- Step 3: nothing remains to discount (the discount is applied *after* losses, so it is lost).
- **Net capital gain = 0.** No net capital loss for 2025 (current-year losses 0 do not exceed gains).
- **Unapplied prior-year loss remaining: 5,000 from income year 2022**, carried forward.

---

## s11 — "personal use assets" (iota, individual). All contract 2025-03-01, acquired 2024-09-01 → income year 2025; no disposal meets the 12-month test (≈180 clear days), so no discount anywhere.

**d1 boat one** (PUA): proceeds 15,000; CB 10,000; gain 5,000. First element 10,000 is "$10,000 or less" → gain **disregarded** (s 118-10(3)). (Boundary: equality counts.)

**d2 boat two** (PUA): proceeds 15,001; CB 10,001; gain = **5,000**. First element 10,001 > 10,000 → not disregarded. Not a discount gain.

**d3 boat three** (PUA): proceeds 15,000; RCB 20,000; loss 5,000 → **disregarded** (s 108-20(1)).

**Net capital gain 2025 = 5,000.** No net capital loss; nothing carried forward.

---

## s13 — "nil and one dollar" (lambda, individual). All contract 2025-03-01, acquired 2024-09-01 → income year 2025; no discount (≈180 clear days).

**d1 shares six**: proceeds 1,000; CB 1,000; RCB 1,000. Proceeds neither exceed CB nor fall short of RCB → **no capital gain and no capital loss** (s 104-10(4)).

**d2 shares seven**: proceeds 1,001; CB 1,000. Gain = **1**. Not discount.

**d3 building one**: proceeds 100; first element 120; deducted amounts 30.
- Reduced cost base = 120 − 30 = 90 (s 110-55(4)).
- Cost base: on the statute notes as given (which attach the deducted-amount rule only to the reduced cost base), CB = 120 → proceeds 100 < 120 so no gain, and 100 > RCB 90 so no loss → **no gain, no loss**.
- However s 110-45(2) (checked via Tax Genii; asset acquired after 7.30 pm 13 May 1997) also excludes from the *cost base* expenditure "to the extent that you have deducted or can deduct it". On that reading CB = 120 − 30 = 90 and the disposal yields a **gain of 10**.
- I treat this as an open point for the rule file: the notes' vocabulary ("deducted amounts" = s 110-55(4)) gives the nil result; the full Act gives a gain of 10.

**Net capital gain 2025 = 1** (per the notes); **= 11** if s 110-45(2) is applied to d3. No net capital loss either way.

---

## s14 — "otherwise assessable" (mu, individual). Contract 2025-03-01, acquired 2024-09-01 → income year 2025; no discount.

**d1 lot one**: proceeds 130,000; CB 100,000; gain 30,000. s 118-20: amount included in assessable income under another provision = 40,000 ≥ 30,000 → gain **reduced to zero**.

**d2 lot two**: proceeds 150,000; CB 100,000; gain 50,000. s 118-20: 20,000 included elsewhere < 50,000 → gain reduced to 50,000 − 20,000 = **30,000**. Not a discount gain.

**Net capital gain 2025 = 30,000.** No losses.

---

## s15 — "market value substitution" (nu, individual). Contract 2025-03-01; acquired 2015-06-01 → income year 2025.

**d1 house one**
- First element: acquired for no consideration → replaced by market value at acquisition, 300,000 (s 112-20(1)(a)). (Assumes the acquisition was not from a non-CGT-event source caught by s 112-20(2); the facts do not say, so this is an assumption.) CB = RCB = 300,000.
- Capital proceeds: money 100,000; parties not at arm's length and proceeds (100,000) are less than market value (450,000) → proceeds replaced by market value **450,000** (s 116-30(2)(b)(i)).
- Gain = 450,000 − 300,000 = **150,000**.
- Discount: 2015-06-01 → 2025-03-01, far more than a clear year → discount gain, 50%.
- (No main-residence exemption is in the facts or the notes, so none is applied.)

**Net capital gain 2025** = 150,000 × 50% = **75,000**. No losses.

---

## s23 — "foreign resident part period" (upsilon, individual). Contract 2024-12-31; acquired 2020-01-01 → income year 2025.

**d1 flat one**: proceeds 60,000; CB 50,000. Gain = **10,000**. 12-month test easily met.

**Discount percentage**
- Discount testing period = acquisition day to event day inclusive: 2020-01-01 … 2024-12-31 = 366 (2020) + 365 + 365 + 365 + 366 (2024) = **1,827 days**.
- s 115-105 applies: individual; period ends after 8 May 2012; foreign/temporary resident during part of the period. The period starts after 8 May 2012 → s 115-115(2).
- Percentage = resident days / (2 × period days) = 1,000 / (2 × 1,827) = 1,000 / 3,654 = **27.3673%** (0.27367268…).
- Discount amount = 10,000 × 1,000 / 3,654 = 2,736.7268… ≈ **2,736.73**.

**Net capital gain 2025** = 10,000 − 2,736.73 = **7,263.27** (exact 7,263.2731…). No losses.

---

## s28 — "net loss with prior loss" (omega, individual). Contract 2025-03-01, acquired 2024-09-01 → income year 2025; no discount.

**d1 shares thirteen**: proceeds 2,000; CB 1,000; gain **1,000**.
**d2 shares fourteen**: proceeds 1,000; RCB 5,000; loss **4,000**.

**Income year 2025**
- Step 1: 1,000 − 4,000 → losses exceed gains by 3,000 → **net capital loss 2025 = 3,000** (s 102-10). Net capital gain = **0**.
- Step 2 cannot operate (nothing remains after Step 1), so the prior-year loss of 2,000 (income year 2023) stays **unapplied**.
- Carried forward: 2,000 (from 2023) and 3,000 (from 2025); in a future year they are applied earliest first (s 102-15).

---

## s52 — "leap year anniversary" (b3, individual). Each gain = 300 − 100 = **200**. Day counts (both end days excluded):

| disposal | acquired | event | clear days between | first anniversary | discount? |
|---|---|---|---|---|---|
| d1 parcel p | 2024-02-29 | 2025-02-28 | 364 | not yet reached | **No** |
| d2 parcel q | 2024-02-29 | 2025-03-01 | 365 | passed | **Yes** |
| d3 parcel r | 2023-03-01 | 2024-03-01 | 365, but the span includes 29 Feb 2024 so a full year needs 366; event is *on* the anniversary (cf. TD 2002/10: 2 Feb 2001 → 2 Feb 2002 is not discount) | on anniversary | **No** |
| d4 parcel s | 2023-03-01 | 2024-03-02 | 366 | passed | **Yes** |

**Income year 2024** (d3 2024-03-01, d4 2024-03-02): d3 200 (no discount) + d4 200 × 50% = 100 → **net capital gain 2024 = 300**.
**Income year 2025** (d1 2025-02-28, d2 2025-03-01): d1 200 + d2 100 → **net capital gain 2025 = 300**.
No losses.

---

## s54 — "loss year strictness" (b5, individual).

**d1 parcel t** (contract 2025-03-01; acquired 2024-09-01) → income year 2025. Proceeds 2,000; CB 1,000; gain **1,000**; not discount.
**d2 parcel u** (contract 2026-03-01; acquired 2025-09-01) → income year 2026. Gain **1,000**; not discount (≈180 clear days).

Prior loss: "unapplied net capital loss of 400 from the income year 2025".
- Step 2 applies net capital losses from *earlier* income years only. A loss "from 2025" is not from an earlier year relative to 2025, so it cannot be applied against the 2025 gain. (The fact is also internally odd — a year with a 1,000 gain and no losses cannot itself produce a net capital loss — but the test is evidently about strictness of the year comparison.)
- **Net capital gain 2025 = 1,000.**
- **Income year 2026**: Step 2: 1,000 − 400 = 600; no discount. **Net capital gain 2026 = 600.** Prior loss fully utilised, nothing remaining.

---

## s58 — "collectable no consideration" (b8, individual). Contract 2025-03-01; acquired 2020-01-01 → income year 2025.

**d1 brooch** (jewellery = collectable, s 108-10(2)(a))
- First element: acquired for no consideration → market value at acquisition, 400 (s 112-20(1)(a)). CB = RCB = 400.
- Proceeds 900; gain would be 500 and would be discount-eligible.
- s 118-10(1): first element of the cost base (400) is $500 or less → the capital gain is **disregarded**.

**Net capital gain 2025 = 0.** Nothing carried forward.

---

## Summary table

| scenario | disposal | result | discount? | net capital gain per year | other carried amounts / notes |
|---|---|---|---|---|---|
| s7 | d1 land one | gain 20,000 | yes 50% | 2025: **9,000** (optimal order; 11,000 if loss applied to d1 first) | none |
| s7 | d2 shares three | gain 4,000 | no | | |
| s7 | d3 shares four | loss 6,000 | – | | |
| s8 | d1 painting | collectable gain 200 | yes 50% (but fully absorbed) | 2025: **250** | net capital loss from collectables c/f **200** |
| s8 | d2 coin | collectable loss 400 | – | | |
| s8 | d3 shares five | gain 500 | yes 50% | | |
| s10 | d1 land one | gain 20,000 | yes (but nothing left to discount) | 2025: **0** | prior-year loss (2022) remaining **5,000** |
| s11 | d1 boat one | gain 5,000 disregarded (s 118-10(3), first element = 10,000) | – | 2025: **5,000** | none |
| s11 | d2 boat two | gain 5,000 | no | | |
| s11 | d3 boat three | loss 5,000 disregarded (s 108-20(1)) | – | | |
| s13 | d1 shares six | nil (proceeds = CB = RCB) | – | 2025: **1** on the notes; **11** if s 110-45(2) reduces d3's cost base | open point flagged |
| s13 | d2 shares seven | gain 1 | no | | |
| s13 | d3 building one | nil on notes (CB 120, RCB 90, proceeds 100); gain 10 under s 110-45(2) | no | | |
| s14 | d1 lot one | gain 30,000 reduced to 0 (s 118-20) | no | 2025: **30,000** | none |
| s14 | d2 lot two | gain 50,000 reduced to 30,000 (s 118-20) | no | | |
| s15 | d1 house one | gain 150,000 (proceeds 450,000 MV; CB 300,000 MV) | yes 50% | 2025: **75,000** | assumes s 112-20(2) not engaged |
| s23 | d1 flat one | gain 10,000 | yes, 1,000/3,654 = 27.3673% (1,827-day period) | 2025: **7,263.27** | none |
| s28 | d1 shares thirteen | gain 1,000 | no | 2025: **0** | net capital loss 2025 **3,000**; prior loss 2023 **2,000** still unapplied |
| s28 | d2 shares fourteen | loss 4,000 | – | | |
| s52 | d1 parcel p | gain 200 | no (364 clear days) | 2024: **300**; 2025: **300** | none |
| s52 | d2 parcel q | gain 200 | yes 50% | | |
| s52 | d3 parcel r | gain 200 | no (event on anniversary) | | |
| s52 | d4 parcel s | gain 200 | yes 50% | | |
| s54 | d1 parcel t | gain 1,000 | no | 2025: **1,000**; 2026: **600** | 2025 loss of 400 not applicable in 2025; fully used in 2026, 0 remaining |
| s54 | d2 parcel u | gain 1,000 | no | | |
| s58 | d1 brooch | gain 500 disregarded (s 118-10(1), MV first element 400 ≤ 500) | – | 2025: **0** | none |
