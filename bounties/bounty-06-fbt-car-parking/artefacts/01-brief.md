# Bounty #06 — Public review brief: FBT Car Parking Threshold

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
