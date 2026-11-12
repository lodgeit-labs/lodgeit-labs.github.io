# Independent check (brief §7)  [run]

A separate agent, given only `statute_notes.md` and the facts of 12 scenarios with every expectation stripped (`indep/facts_only.txt`), re-derived the figures from the Act. It did not read any `.le` file or test output and did not run the reasoner. Its full working is in `indep/independent_derivation.md`.

Scenarios covered one from each group of brief §5: worked examples (s7 ordering, s8 collectables), boundaries (s11 PUA $10,000, s13 nil/$1, s52 leap-year anniversary, s58 collectable $500 via market value), ordering (s7, s8, s10, s28, s54), entity/residency (s23 apportionment), break-it (s13, s14 s 118-20, s15 market value substitution, s28).

| Scenario | Independent figure | File figure | Agree |
|---|---|---|---|
| s7 ordering | 9,000 (11,000 under the other order) | 9,000 | yes |
| s8 collectables | 250; collectable loss c/f 200 | 250; 200 | yes |
| s10 prior losses exceed | 0; 5,000 unapplied | 0; 5,000 | yes |
| s11 personal use assets | 5,000 (d1 disregarded at exactly 10,000; d3 loss disregarded) | 5,000 | yes |
| s13 nil and one dollar | 1 — **with an open point**: if s 110-45(2) strips the deducted 30 from the cost base, d3 is a gain of 10 and the total 11 | was 1 | **disagreement, resolved: see below** |
| s14 otherwise assessable | 30,000 | 30,000 | yes |
| s15 market value substitution | 75,000 | 75,000 | yes |
| s23 foreign resident part period | 7,263.27 (1,827 days; 27.3673%) | 7,263.27 | yes |
| s28 net loss with prior loss | net capital loss 3,000; 2,000 prior loss untouched | same | yes |
| s52 leap year anniversary | 2024: 300; 2025: 300 (p, r fail; q, s pass) | same | yes |
| s54 loss year strictness | 2025: 1,000; 2026: 600 | same | yes |
| s58 collectable no consideration | 0 (disregarded) | 0 | yes |

## Disagreement and resolution (s13)

The checker raised s 110-45(2): for an asset acquired after 7.30 pm on 13 May 1997, expenditure does not form part of the **cost base** to the extent the taxpayer has deducted or can deduct it. My draft applied the exclusion only to the reduced cost base (s 110-55(4)). I retrieved s 110-45 through Tax Genii (ATO ID 2004/404 quoting 110-45(2) and (4); TD 2022/14 quoting 110-45(2) in full) **[statute]** and the checker is right. Fix: the cost base rule now subtracts deducted amounts for assets acquired after 13 May 1997, and keeps them for earlier acquisitions (the reduced cost base excludes them in both cases). Scenario s13 was extended: building one (acquired 2024) now has cost base 90 and gives a gain of 10; building two (acquired 1990) keeps the cost base / reduced cost base gap and gives neither gain nor loss. Net capital gain 11. Re-run: 153/153 pass.

This is the finding the independent check exists for: a plausible wrong figure (1 instead of 11) that every file-derived test would have confirmed.
