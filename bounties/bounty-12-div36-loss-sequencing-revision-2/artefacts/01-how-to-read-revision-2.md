# How to read revision 2

This supplements the revision 1 note (`01-how-to-read-logical-english.md`), which still applies: a rule is a conclusion, then `if`, then conditions joined by `and`; `a taxpayer` introduces a thing, `the taxpayer` refers back to it; numbers are plain. Revision 2 adds six constructs. Each is explained once here so that nothing in the file surprises you.

## 1. Every rule has a comment above it

The comment says, in plain English, "If … then …" and names the subsection. **The comment is the claim you are ratifying.** If the comment states the law wrongly, the rule is wrong even if the arithmetic is right. If the comment is right but the rule beneath it does something else, that is a defect too, and a more dangerous one. Three kinds of comment carry no legal claim:

- `% Mechanical: no statutory content.` A helper the engine needs, such as "the total of the losses brought forward". Check it is arithmetic, nothing more.
- `% Scope rule …` One rule that gathers the conditions under which the file will answer at all (see 3).
- `% Implementation note (not law): …` One block explaining why some arithmetic is repeated rather than factored. It is there for honesty. It is not a statement about the Act.

## 2. Three answers, not two

Ask the file a question and it gives one of three things:

- **Proven.** Answers, and an empty list of unknowns. The figures are certified on the facts given.
- **Cannot be determined.** Answers **together with unknowns**, such as `Wren Kavanagh is an Australian resident in FY2026` or `the pension is characterised`. The figures hold only if those facts are true, and the file was not told. A caller must not treat them as certified.
- **Refused.** No figures, and a sentence beginning `it is refused that … because …`, naming the reason: the taxpayer is a corporate tax entity, a receipt is exempt under s 51-100, the taxpayer is a foreign resident, a split receipt is malformed, or the receipts' assessable parts exceed the assessable income asserted.

The word `; unknown` after a template in the templates block marks the facts that, if absent, produce the second kind of answer rather than silence.

## 3. The scope rule

`a taxpayer is within the scope of these rules in a year` is true when the taxpayer is not a corporate tax entity at any time in the year, is an Australian resident, every receipt has a stated character, and no refusal applies. Every figure rule tests it, directly or through a rule that tests it. It exists so the file does not compute a Division 36 figure for a company or a foreign resident. It makes no claim about the law beyond the corporate limb, which is s 36-15's own condition.

## 4. Losses are held one per year

`Wren Kavanagh has a loss brought forward of 3000 from FY2023 into FY2026.` Each loss year is a fact. The rules apply them earliest first (s 36-15(5)), and the outputs are per loss year: applied, absorbed by net exempt income, deducted, carried forward. There is no aggregate loss figure as an input.

## 5. Receipts, and the partly exempt receipt

A receipt enters as `receives the pension of 4579 in FY2026` plus a character: `is exempt income under section 52-10`, or `is not assessable and not exempt under section 59-30`, or `is exempt under section 51-100`. Outgoings and foreign tax attach to the receipt.

A **partly exempt receipt** (a pension with an exempt part and an assessable part, say) enters as three facts:

```
Wren Kavanagh receives the pension of 4579 in FY2026.
the pension is a split receipt.
the pension has an exempt part of 3000 and an assessable part of 1579 and a non-assessable non-exempt part of 0.
```

The exempt part, not the gross, is the s 36-20(1) figure. The assessable part is declared separately by the preparer within the annual assessable income figure (`has assessable income of 1579`), and the file refuses if the parts across all receipts exceed that figure. The second line, `is a split receipt`, is a marker the reasoner needs; it carries no legal content. We considered having the file derive annual assessable income from the receipts' parts, which is the more correct model, and could not make it run within the reasoner's limits; the note in the header says so.

## 6. Sums and the loss-year chain

`G is the sum of each gross amount such that …` adds up every receipt matching the conditions. `for all cases in which … it is the case that …` is a universal: every receipt has a character. `the minimum of A and B is C` and `the maximum of A and B is C` are what they say. The chain `earlier losses before a loss year` → `losses available before a loss year` → `applies` is how "earliest first" is done without loops: for each loss year, the amount still available after all earlier years have taken theirs.

## What to look for

- A comment that misstates a subsection.
- A rule that does something the comment does not say.
- A fact pattern where the answer is plausible and wrong. Give us the facts and your expected figure.
- A case where the file answers when it should refuse, or refuses when it should answer.
- A line you cannot read. That is our defect, not yours, and it is a finding.

## Running it yourself (optional)

You do not need to. If you want to, the public Logical English editor at https://le2.logicalcontracts.com/ will load the file; queries are at the bottom of the file and scenarios can be edited in place. Reviewers who did this in round one found it useful for "what if" questions; it is not required for a verdict.
