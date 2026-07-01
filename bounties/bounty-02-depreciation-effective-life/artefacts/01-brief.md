# Bounty #02 — Public review brief: Depreciation Effective-Life Lookup

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
