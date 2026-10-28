# How to read `cgt_a1.le` (ten minutes)

You are reading a legal specification, not code. Each rule is an English sentence of the form *conclusion* **if** *conditions*. The file runs, but you need not run it.

## The shape of the file
1. **Header** (first 90 lines): scope, refusals, design choices, pin, counts. Read this first.
2. **`the templates are:`** — every sentence the file understands. Lines ending `; undefined` are **inputs** a scenario states (facts about the taxpayer, asset and disposal). The rest are conclusions the rules derive.
3. **`the knowledge base cgt_a1 includes:`** — the rules, in Parts A–I:
   - A income year · B refusals · C missing inputs · D capital proceeds · E cost base · F disregarded gains/losses (Div 118 etc.) · G the capital gain or loss (s 104-10(4), s 118-20) · H discount (Div 115) · I the method statement (s 102-5) and net capital loss.
   - Then **Implementation notes (not law)**: plumbing you need not ratify.
4. **Scenarios** s1–s62: each has a `% Working` comment (the hand derivation with provisions), the facts, and `expects answers [...]` lines (what the file must say). The runner has confirmed every expectation.
5. **Queries**: the sixteen questions a scenario can ask.

## Reading a rule
```
% If the asset was acquired before 20 September 1985 then the gain or loss is
% disregarded (s 104-10(5)(a)).
the capital gain or loss from a disposal is disregarded because paragraph 104-10(5)(a) asset acquired before 20 September 1985
    if the disposal is assessable
    and the disposal is a disposal of an asset by a taxpayer
    and the asset was acquired by the taxpayer on a date
    and the date is before 1985-09-20.
```
The comment states what the rule claims the subsection says. Your two questions for every rule: **does the comment state the subsection correctly?** and **does the rule do what the comment says?** Words like `a date`, `the asset` are variables; `it is not the case that` is negation; `the sum of each … such that …` adds up every match.

## Three answers only
For any disposal the file gives a figure, or "cannot be assessed because *fact* is missing", or "is refused because *provision* not encoded". It never guesses. If you think it should refuse something it computes, or compute something it refuses, that is a finding.

## Conventions worth knowing
- Income year 2025 = year ending 30 June 2025.
- "At least 12 months before" is counted as in TD 2002/10 (both end days excluded): sold on the anniversary fails, the day after passes.
- Losses are applied to non-discount gains first (a choice; see open question Q2).
- Residency and asset character (collectable / personal use asset / neither) must be stated; the file does not assume the common case.

## The question we value most
Construct a fact pattern inside the stated scope where the file would give a plausible figure that is wrong. Give the facts in the file's own sentences and the figure you expect; we run it and report back.
