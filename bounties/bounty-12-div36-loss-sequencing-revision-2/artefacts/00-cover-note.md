# Bounty #12 (Division 36, revision 2): cover note

Round one of these rules was Bounty #11, now closed. Revision 2 is reviewed as its own bounty, #12.

**To:** Devashish Magoon, Sami Charaf, Jen H, Graeme Pollard (and Louise Ingoe on reply)
**From:** Andrew Noble, LodgeiT
**Date:** 2026-09-25

## What you are being sent

- `div36_rev2.le`, SHA-256 `aa97844c777b9b46b38aa69b83fe5a6f151f13ac303b2bea3883ae20a5bc6b8d`
- `01-how-to-read-revision-2.md` (read this first, ten minutes; it covers what is new since revision 1)
- `03-verdict-form-revision-2.md`
- `04-questions-for-reviewers.md`

The file is 51 rules, 36 scenarios and 205 embedded test cases. Every test passes on the reasoner it was built against (`LogicalContracts/LogicalEnglish2 @ 445b4da`, SWI-Prolog 9.0.4). A test passing means the file agrees with itself; it does not mean the file states the law correctly. That is what you are being paid for.

## Terms

- **$1,000 ex GST**, paid within five business days of your verdict. Revision 1 was $750; revision 2 is a materially larger file, and every reviewer is on the same terms.
- **A REJECT is worth the same as an ACCEPT.** A polite approval of something wrong is the one outcome we cannot use.
- **Verdicts by Friday 10 October 2026.** Say if you need longer.
- **Named credit by default**, in the public reviewer registry, with the verdict hash and the file hash. Opt down to initialled or anonymous on the form.
- Send the completed form to support@lodgeit.net.au. Prose in an email is equally acceptable.

## What changed since revision 1, and where your findings went

Revision 1 (about 90 lines, three scenarios) never deducted brought-forward losses against assessable income; it only applied them against net exempt income. Four of five reviewers said FIX. Revision 2 is a different file. In brief:

| Area | Revision 2 |
|---|---|
| s 36-15(2), (3) | Profit-year deduction of earlier losses, loss taken first from net exempt income then from the excess of assessable income |
| s 36-15(4) | Loss-year absorption, as before, corrected |
| s 36-15(5) | Losses held as one fact per loss year, applied earliest first; net exempt income pool consumed earliest first across years |
| s 36-10 | Steps 1–4; step-1 exclusion of tax losses from deductions |
| s 26-55 | Gifts, covenants, s 25-50 and s 290-150 super cannot create or add to a loss |
| s 36-20(1) | Net exempt income = exempt income less revenue outgoings less foreign tax, floored at nil, summed over receipts; a partly exempt receipt carries an exempt part |
| s 4-15 | Taxable income output |
| New outputs | Absorbed by net exempt income, deducted, taxable income, net exempt income remaining after ss 36-10 and 36-15 |
| Refusals | Corporate tax entity (s 960-115, tested in the deduction year), s 51-100 receipt, foreign resident, malformed split receipt, assessable parts exceeding asserted income |
| Tri-state | Every figure is proven, cannot be determined (with the missing fact named), or refused (with a reason) |

Where each of your round-one findings landed:

- **Sami:** the "$1" (nil) case is fixture P1; the per-year ledger is s 36-15(5) as you described; the s 51-100 refusal stands with your reasoning in the comment; the Division 35 interaction is a stated precondition on the deductions input, and the file now outputs net exempt income remaining for a Division 35 file to consume. Your test case for that is open in `04-questions`.
- **Dev:** s 6-20(4) is cited; your two fixtures are DM-1 and DM-2 with your figures; the partly exempt pension is DM-3; the corporate guard is keyed to s 960-115 and the deduction year. Your preference for deriving assessable income from receipt parts was not adopted, for a reason set out in `01-how-to-read` and put back to you in `04-questions`.
- **Jen:** s 35-15 corrected (we had the section wrong, you were right); every rule now carries an "If … then …" comment naming its subsection; s 36-10(4) closed as note 2; no PP/non-PP concept in the file, by design.
- **Graeme:** your Q6 fact pattern is fixture S13.
- **Louise:** your s 26-55 fact pattern is fixture S12.

## What you are asked to ratify, and what you are not

- **Ratify:** every rule whose comment names a subsection. Does the "If … then …" line state the law, and does the rule beneath it do what the line says?
- **Do not ratify:** rules marked "Mechanical: no statutory content", the scope rule, and the block headed "Implementation note (not law)". These are engineering. Read them if you like; they are not claims about the Act.
- **Out of scope** (refused or not modelled, stated in the header): s 36-17 corporate deduction, Division 35 internals, primary production / non-primary production labels, Division 245, net capital losses, s 393-5 farm management deposits, s 36-20(2) foreign residents.

## The question we value most

Can you construct a fact pattern where these rules produce a plausible figure that is wrong? Give the facts and the figure you expect, and we will run it. Three such patterns from an independent reviewer this week (Tests A–C) are already in the file.

Andrew
