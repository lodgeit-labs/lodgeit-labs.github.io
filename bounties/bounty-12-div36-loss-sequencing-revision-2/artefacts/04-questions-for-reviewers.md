# Questions for reviewers: revision 2

These are open points where a practitioner's view will decide what the file, or the product built on it, does next. Answers are optional and not part of the verdict; they are the most valuable thing you can send us apart from a broken fact pattern.

## QA. Missing core inputs

The file names three facts as open scope conditions (resident, not corporate, every receipt characterised): if any is absent, every figure comes back "cannot be determined" with the missing fact named. But the core inputs, assessable income and the two deductions figures, are not treated that way: if one is absent the file simply returns no answer, with no unknown named. Should a missing core input also surface as "cannot be determined: the taxpayer has assessable income of some amount"? Or is silence the right answer for a form that was not filled in?

## QB. Division 35 and net exempt income (s 35-15(2))

We read s 35-15(2) as reducing the para 35-10(2)(b) deferral by the net exempt income left after Division 36 has used it. So the file takes deductions net of the 35-10(2)(a) excess, and outputs "net exempt income remaining after ss 36-10 and 36-15" for a Division 35 file to consume. Test case:

- Assessable income 55,000; deductions 17,000 of which 10,000 is the s 35-10(2)(a) excess (so 7,000 enters Division 36); net exempt income 4,000; loss brought forward 3,000.
- We get: taxable income 48,000; the loss absorbed by net exempt income; nil carried forward; net exempt income remaining 1,000; next year's deferral reduced from 10,000 to 9,000.

Do you agree? If not, show a Division 36 figure that Division 35 changes.

## QC. Primary production and non-primary production

The file has no PP/non-PP concept, because Division 36 has none; the split is a return-label matter. Two practitioners have told us: across loss years, earliest first, regardless of type; within one loss year holding both types, the preparer chooses, for planning reasons (averaging, farm management deposits), and the choice must be reasonable and consistent. The ATO's L1 Step 6 says the same. Is that your practice? Is there any case where the Act constrains the within-year choice?

## QD. The partly exempt receipt: asserted or derived assessable income?

One reviewer's preference was that the file derive annual assessable income from the receipts' assessable parts plus "other income", rather than check the parts against a typed annual figure. We agree that is the more correct model. We could not make it run within the reasoner's per-query limit, so the file keeps the annual figure as an asserted input and refuses if the receipts' assessable parts exceed it. Is the check-based design acceptable for ratification, with the derivation noted as deferred? Or is a file that lets a preparer type an annual figure the receipts don't support not fit to certify, refusal or no refusal?

## QE. Division 245: order of loss reduction

For a later Division 245 file: when a net forgiven amount is applied against tax losses under s 245-115, does the debtor choose which loss years are reduced, or is there a statutory order within the class? If it is a choice, we will take it as a supplied fact, never derive it. We have the cross-class order (tax losses, then net capital losses, then expenditure, then cost bases) from the section headings and would like the within-class rule confirmed from the text.

## QF. Malformed split receipt: refuse, or "cannot be determined"?

A split receipt whose parts are negative or do not sum to its gross is refused with a reason. The alternative was to treat such a receipt as having no valid character, so every figure would come back "cannot be determined: the pension is characterised". Refusal is louder; the unknown is more precise about what is missing. Which would you rather see on a return?

## QG. Break it

Same as revision 1, and still the question we value most: facts, your expected figure, and if you ran it, what the file gave.
