# Division 36 revision 3: findings log

**File:** `div36_rev3.le`, SHA-256 `ace4a35200ed0887471e87cccf5b37c4ea9de6e36c985a2ba36b9b6681da5dc7`
**Supersedes:** revision 2, `div36_rev2.le`, SHA-256 `aa97844c777b9b46b38aa69b83fe5a6f151f13ac303b2bea3883ae20a5bc6b8d` (Bounty #12)
**Source of findings:** reviewer D.M. (CPA), Bounty #12 verdict **FIX**, received 9 Nov 2026
**Built and measured by:** Fable, 9 Nov 2026
**Status:** draft for the reviewer's confirmation. **Not yet accepted.**

---

## Measured results

| | Revision 2 | Revision 3 |
|---|---|---|
| Rule clauses (all with a comment directly above) | 51 | 61 |
| Scenarios / test cases | 36 / 205 | 48 / 321 |
| Full suite | 205/205 pass | **321/321 pass, 23 s** |
| Verifier issues (incl. untested predicates) | 0 | **0** |

All runs used LogicalContractsOrg/LogicalEnglish2 @ `a4c314b` (main, 7 Nov 2026) and SWI-Prolog 9.0.4.

**Counting method:**
- tests: `grep -c 'expects answers'`
- scenarios: `grep -c '^scenario '`
- rule clauses: non-indented lowercase lines between the knowledge-base line and the first scenario

**Mutation check:** changing an expected figure in R3-F1a, and in R3-F2b, made those tests fail with the rules' real answer. The new tests are live, not vacuous.

---

## Findings and disposition

| # | Finding (D.M.) | Severity | Reproduced on rev 2 | Disposition in rev 3 | Proving scenario(s) |
|---|---|---|---|---|---|
| F1 | Outgoings and foreign tax on a **split** receipt never reduce net exempt income | high | **Yes**: NEI 6,000 and taxable income 2,000 (correct: 5,100 and 1,100) | New inputs: outgoings and foreign tax **attributable to the exempt part** of a split receipt, added to the s 36-20(1) sums. Amounts stated against the whole split receipt are **refused**; the rules don't apportion. | R3-F1a, R3-F1b, R3-F1c, R3-F1d |
| F2 | Two loss rows from the **same year** each take the full available amount | high | **Yes**: 7,000 applied against 5,000 available; carry-forward of **−1,000** | **Refused**, with the reason "combine them into one". A combined single amount computes correctly. | R3-F2a, R3-F2b |
| F3 | An uncharacterised receipt (G4) still gives figures | medium | Yes (G4 proved deducted 0, taxable income 0) | Refused as a **missing input**, naming the receipt's character; no figures. | G4 (rewritten) |
| F4 | A split receipt's assessable part left out of assessable income passes as proven | medium | per D.M. (taxable income 1,892, proven) | **Required confirmation** that assessable income includes every split receipt's assessable part (D.M.'s QD); without it, a missing input. | R3-F4a, R3-F4b, R3-F4c |
| F5 | A missing core input gives silence | medium | per D.M. | Missing assessable income, other deductions or limited deductions is named as a **missing input**. | R3-F5a, R3-F5b, R3-F5c |
| F6 | Comment on the NEI-nil rule claims it covers a no-receipt year | low | — | Comment corrected. | — |
| F7 | s 36-15(4) comment says "equal or exceed"; the Act says "exceed" | low | — | Comments now state the Act, and record the equality placement as a reading (same figure, Test B). | Test B |
| F8 | DM-2 has no foreign tax, so it passes for the wrong reason | low | — | DM-2 kept as a plain loss year and annotated; foreign tax on exempt income is now exercised by R3-F1a and Test C. | R3-F1a, Test C |
| Q1 | The split-receipt sum counts the exempt part without checking the split marker | — | — | Marker check added to the sum. | DM-3 and the R3-F4 scenarios |
| Q1 | Build history long in the header | — | — | Moved to the end of the file. | — |
| Q5 | Unstated assumptions | — | — | Stated in the header: residency for the full year; one loss amount per year; labels sort by date; PP and non-PP combined (no s 393-5); not a partnership; outgoings exclude capital, nexus left to the preparer; foreign tax "paid or payable". | — |

### Answers to the reviewer questions in `04-questions`, as adopted

- **QA** (missing input): named. Missing limited deductions is **refused naming it ("enter 0 if none")**, not treated as nil with a listed assumption as D.M. suggested. **A design difference for D.M. to confirm.**
- **QD** (assessable income asserted): adopted D.M.'s required declaration.
- **QF** (wrong fact): refuse. Adopted for whole-receipt amounts on a split receipt and for same-year loss rows.
- **QC** (PP/non-PP): out of scope; combined amounts only, stated in the header.

---

## Behaviour changes a caller must know about (Tax Genii)

1. **New refusal reasons beginning `missing input:`.** These mean "ask the user for this", not "out of scope". Show them as a clarification, not "Calculator declined".
   - `missing input: assessable income`
   - `missing input: other deductions`
   - `missing input: limited deductions (enter 0 if none)`
   - `missing input: the character of a receipt (exempt income, not assessable and not exempt, or a split receipt)`
   - `missing input: confirmation that assessable income includes the assessable part of every split receipt`
2. **New refusal reasons that are genuine declines:**
   - `split receipt: outgoings stated for the whole receipt (state the amount attributable to the exempt part)`
   - `split receipt: foreign tax stated for the whole receipt (state the amount attributable to the exempt part)`
   - `losses brought forward: more than one amount from the same loss year (combine them into one)`
3. **New input facts:**
   - `<taxpayer> incurs revenue outgoings of <amount> attributable to the exempt part of <receipt>.`
   - `<taxpayer> pays foreign tax of <amount> attributable to the exempt part of <receipt>.`
   - `<taxpayer> includes the assessable part of every split receipt in assessable income in <year>.`
4. **A receipt's character is no longer an "unknown".** A missing character is now a `missing input:` refusal. Residency and corporate status are still returned as unknowns, as before.
5. **Unchanged:** templates, query names and figure wording for all existing outputs.

---

## Independent check (9 Nov 2026)

A separate agent, which had not seen the rules or their expected answers, worked out five cases from the Act alone. It read the text of ss 36-15 and 36-20 through Tax Genii. All five matched the rev 3 test figures exactly, on every output:

| Case | Rev 3 scenario | Net exempt income | Used (absorbed + deducted) | Taxable income | Carried forward | NEI left |
|---|---|---|---|---|---|---|
| 1 | R3-F1a | 5,100 | 5,100 + 2,900 | 1,100 | 0 | 0 |
| 2 | R3-F1b | 5,000 | 5,000 + 3,000 | 1,000 | 0 | 0 |
| 3 | R3-F2b | 0 | 0 + 5,000 | 0 | 2,000 | 0 |
| 4 | R3-F4b | 3,000 | 3,000 + 286 | 3,471 | 0 | 0 |
| 5 | R3-F4c | 4,579 | 3,286 + 0 | 2,178 | 0 | 1,293 |

On the law, the checker found:
- **Same-year losses:** s 36-10 produces a single tax loss per loss year, so two amounts from one year are one loss. s 36-15(5) orders only between years. This supports "combine them into one".
- **Split receipts:** s 36-20(1)(a) and (b) reduce net exempt income only by the outgoings and foreign tax relating to the exempt income. Apportionment is needed, which supports asking for the exempt-part amount rather than having the rules apportion.

## Still open (not in this build)

- The reviewer's confirmation of F1–F8 on this SHA (a short paid verification).
- Pack documents: strike the unverified "found it useful" sentence in `01`; deliver the bracketed-variable rendering owed to a round-one reviewer.
- Part-year residency, PP/non-PP split, s 393-5, Division 35 and Division 245: out of scope, as stated.
- **Pin:** LogicalEnglish2 `53c0021` (cited to Tax Genii on 14 Oct) no longer exists upstream. Archive `a4c314b` in `lodgeit-labs/le2-pins`.
