# Open questions for practitioners

Numbered so a reviewer can answer inline. Each records either a judgement the statute leaves open or a design choice the file had to make. "File does" states the current behaviour of `cgt_a1.le`.

**Q1. Is the thing a CGT asset at all?** The file takes "d1 is a disposal of ASSET by TAXPAYER" as given. Whether the thing is property or a legal/equitable right (s 108-5), whether it is one asset or several (Subdiv 108-D separate assets, s 108-7 joint tenants), and whether the dealing is a "disposal" (change of ownership, s 104-10(2)) are left to the practitioner. Should the file carry an explicit "ASSET is a CGT asset" input and refuse without it?

**Q2. Order of applying losses (s 102-5 step 1 note 1, step 2 note 2; s 108-10(1) note).** The Act leaves the order to the taxpayer. File does: losses against non-discount gains first, then discount gains, which minimises the net capital gain. (S7 shows the alternative order gives 11,000 instead of 9,000.) Is encoding the optimal choice acceptable, or should the order be an input?

**Q3. Mixed discount percentages with losses.** Where a year has a discount gain with a reduced percentage (s 115-115 apportionment) and losses to apply, the file refuses the year rather than choosing. Should it instead apply losses in ascending order of discount percentage (lowest percentage first), which is the minimising choice?

**Q4. Prior year losses are inputs.** The file applies "unapplied net capital loss of L from the income year Y" facts to later years only (earliest first by sum; the file outputs the total remaining, not the per-year split). It does not carry a net capital loss it computes for 2025 into 2026 within the same scenario. Should it? (That needs a year-ordered recursion and a convention for which year's losses remain.)

**Q5. Fourth element for collectables and personal use assets.** The ATO text of s 110-25 shows a note "This element does not apply to personal use assets or collectables: see sections 108-17 and 108-30" at the boundary of subsections (4) and (5); the EM says ss 108-17 and 108-30 exclude *non-capital costs of ownership* (the third element). File does: excludes the third element only. Please confirm whether the fourth element (capital improvements) is also excluded for these assets.

**Q6. Section 118-300 coverage.** File does: items 3 (original owner) and 4 (acquired for no consideration) for life policies and annuities, for taxpayers that are not complying superannuation entities. Not modelled: item 2 (general insurance where the insured property's own gain/loss would be disregarded), items 1, 5–7 (insurers, complying super entities, illness/injury policies). Is item 2 wanted in a first file?

**Q7. Exemptions not modelled at all** (no marker, so a scenario cannot even be refused): shares in a PDF (s 118-13), venture capital (Subdiv 118-F), granny flat interests (Subdiv 137-A), superannuation-agreement rights, relationship-breakdown roll-overs (Subdiv 126-A), the affordable housing discount (s 115-125), Subdiv 118-I earnouts, ESS interests, Div 775 foreign currency, Div 149 and s 104-230 for pre-CGT interests, sets of collectables/personal use assets (ss 108-15, 108-25), integrity rules ss 115-40 and 115-45. Which of these should become refusals (an input marker plus a refusal rule) in the next version?

**Q8. Norfolk Island.** File does: disregards if the taxpayer was a Norfolk Island resident when the asset was acquired, the acquisition was before 24 Oct 2015, and the practitioner asserts the asset "would have been exempt under the Norfolk Island law as it applied before 1 July 2016" (the EM's carve-out for, e.g., mainland assets). Is that assertion the right input, or should the file instead ask where the asset was situated?

**Q9. Nil proceeds (s 116-30(1)).** File does: a disposal with no money and no property proceeds takes the asset's market value at the time of the event as proceeds and reports "cannot be assessed" without it. The text of s 116-30(1) itself was not retrieved verbatim this session (s 116-30(3), which lists its exceptions, was). Please confirm the wording.

**Q10. Trading stock (s 118-25(1)).** The disregard rule was written from the note to s 118-25 and general knowledge; the subsection text was not retrieved verbatim. Please confirm: "a capital gain or loss you make from a CGT asset is disregarded if, at the time of the CGT event, the asset is your trading stock".

**Q11. Personal use assets that are land.** s 108-20(3) says a personal use asset does not include land or a stratum unit or a building treated as a separate asset. The file trusts the "is a personal use asset" input; it does not detect a block of land marked as a PUA. Should there be an "is land" input to guard this?

**Q12. Foreign-residency apportionment inputs.** s 115-115(2) needs the number of Australian-resident (non-temporary) days in the discount testing period. The file asks for that number directly rather than for residency periods. Is a day count the input practitioners can supply, or should the file compute it from dated residency periods (and apply s 115-105(3) changed-residency rules)?

**Q13. 11.45 am on 21 September 1999 (s 115-15).** An event dated 21 Sep 1999 is refused because the time of day is needed. Acceptable, or should a time input be added?

**Q14. Decimal output.** Discount results with thirds (33 1/3%) and apportioned percentages are floats; the file does not round. Should net capital gains be rounded to the cent, or to whole dollars (the ATO return takes whole dollars)?

**Q15. Collectable loss carry-forward per year.** s 108-10(5) says two or more unapplied net capital losses from collectables are applied in the order made. The file applies the total and reports the total remaining; it does not say which year's loss remains. Is the total enough for a return, or is the per-year split needed?

**Q16 (from external review). Cost base keyed on the asset, not the disposal.** `the cost base of an asset`, `the reduced cost base of an asset` and `the first element …` take only the asset; a scenario with two disposals (e.g. a part disposal) of the same asset identifier would cross-talk. All v1 scenarios have one disposal per asset. v2: key these on the disposal.

*Status after external review (25 Oct 2026): Q5, Q9, Q10 closed by retrieved statute/rulings; Q11 implemented (s59); Q2 and Q7 await a practitioner; the rest stay as designed for v1. See `review_response.md`.*

**Q17 (v1.2). Residency and asset character are now required inputs.** A disposal with neither a residency statement nor an asset-character statement returns "cannot be assessed". This makes every scenario two lines longer but stops a silently-omitted "foreign resident" or "collectable" fact producing a resident/ordinary-asset figure. Practitioners: is "was an Australian resident and not a temporary resident throughout the ownership of the asset" the right single fact, or should residency be stated per income year?
