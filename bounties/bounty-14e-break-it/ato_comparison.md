# Divergences from ATO tools (brief §5 group 8, §9 item 6)

## Attempted: ATO "Capital gains tax record keeping tool" (website version), 25 Oct 2026

Facts entered (scenario s7 of `cgt_a1.le`): income year 2024-25; no prior losses; not a foreign/temporary resident since 8 May 2012; three "Other shares" assets:
- land one: acquired 01/01/2020, disposed 01/12/2024, proceeds 30,000, acquisition cost 10,000
- shares three: acquired 01/09/2024, disposed 15/01/2025, proceeds 9,000, cost 5,000
- shares four: acquired 01/01/2021, disposed 01/02/2025, proceeds 6,000, cost 12,000

Expected from the Act (and from the file): net capital gain 9,000 if the 6,000 loss is applied against the non-discount gain first; 11,000 if applied against the discount gain first. The ATO page states the tool "will apply the CGT calculation method that gives you the best result (the smallest net capital gain)", so the expected ATO figure is 9,000.

**Result: not obtained.** The three asset records saved (the tool listed them), but the per-asset "Gain/Loss", "Method" and "Status" fields stayed blank and the Calculate button produced no result page after the mandatory questions were answered. The tool is a single-page application whose field model did not reliably accept values set from the automation (the income-year select had to be re-set by keyboard; the proceeds field appeared filled but the records show no computed gain). I did not want to spend more of the session on driving the ATO form. **[run: attempted; no figure]**

Follow-up for a reviewer with a browser: enter the three assets above by hand and record the tool's net capital gain. A result of 9,000 agrees with the file; 11,000 would mean the tool applies losses in a different order than the one the file chose (open question Q2).

## Known points of difference to look for (from the statute, not yet measured against the tool)

1. **Rounding.** The tool takes whole dollars; the file keeps cents (s5: 6,000.00; s23: 7,263.27). Not a legal divergence.
2. **Order of losses across discount and non-discount gains.** The tool promises the smallest net capital gain; the file does the same for the 50%/non-discount split and refuses when discount percentages differ (s24). Expected to agree where the file answers.
3. **The 12-month test on the exact anniversary** (s2, s52). TD 2002/10 is the ATO's own view, so the tool should agree; worth a direct check since calculators often use "≥ 365 days".
4. **Personal use asset at exactly $10,000** (s11 boat one): the tool's PUA asset type should disregard the gain. The received LE file would not have.
5. **Deceased estates, main residence, foreign residents pre-2017**: the tool refuses or redirects, as the file refuses (s29, s32, s33, s34).
