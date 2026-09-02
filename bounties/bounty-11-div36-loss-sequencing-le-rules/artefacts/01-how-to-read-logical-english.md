# How to read a Logical English rule

**A guide for reviewers. No technical background needed.**
LodgeiT Labs bounty programme — Phase 2, first rule-ratification round.

---

## Before anything else — three reassurances

**You do not need to install anything, run anything, or own any software.** The file we've sent is
plain text. Open it in Notepad, TextEdit, Word, or the preview pane of your email client. That's it.

**You cannot break anything.** You are reading, not editing. There is no submit button that fires
something into production. Nothing you do to your copy of the file affects ours.

**If a line does not read as clear English, that is our defect, not your failing.** The entire point
of Logical English is that a tax practitioner can read it without learning a programming language. If
you find yourself squinting at a line, write that down — "this line is unclear" is a legitimate and
useful finding, and we'd rather hear it than have you push past it.

You are being paid for your tax judgement. You are not being asked to learn a language.

---

## 1 — Why we're doing this at all

A LodgeiT customer told us our software was carrying forward too much tax loss. She was right. The
calculation had been built from the ATO's *form instructions* — the L1 label worksheet — rather than
from Division 36 of the ITAA 1997. In a year with taxable income the two agree. In a loss year they
don't, because s 36-15(4)(a) has a step the worksheet doesn't. Her client was in a loss year.

Three days, four staff, and two AI systems failed to work out who was right. She had it from the
start.

So we've written the law itself out as rules a machine can execute — and, crucially, that a human can
read and check. That's what Logical English is. But **a rule is only trustworthy if a credentialed
practitioner has read it and agreed it states the law correctly.** That's what we're asking you to do.

This is the first one. If it works, it becomes how we build.

---

## 2 — What Logical English actually is

Five sentences:

1. It is a way of writing rules that reads like English but is precise enough for a machine to
   execute.
2. It was developed by Bob Kowalski (Imperial College, one of the founders of logic programming) and
   colleagues. **LodgeiT is a co-owner** of the current version.
3. Every rule is of the form *"X is true if A and B and C"* — a conclusion and its conditions.
4. When it answers a question, it produces a **proof tree**: every rule that fired, in order, in
   plain English. That's the audit trail.
5. If it hasn't been told enough to answer, it **refuses** rather than guessing. That property is why
   we're using it.

Nothing else about it matters for your review.

---

## 3 — The shape of the file

Three sections, in order.

**a) `the templates are:`** — a list of the sentence patterns the file uses, with `*asterisks*`
marking the blanks:

```
*a taxpayer* has deductions of *an amount* in *a year*.
```

This is just declaring vocabulary — "I'm going to write sentences of this shape." **You can skip this
section entirely.** It carries no legal content.

**b) `the knowledge base ... includes:`** — the rules. **This is what you're reviewing.** Every rule
has a plain-English note above it saying what we think it means:

```
% s 36-15(4)(a). The excess of deductions over assessable income is taken off
% net exempt income FIRST, before anything reaches the loss brought forward.
a taxpayer has net exempt income left of an amount in a year
    if the taxpayer has net exempt income of a net exempt amount in the year
    and the taxpayer has an excess of deductions of an excess amount in the year
    and a remainder = net exempt amount - excess amount
    and the maximum of the remainder and 0 is the amount.
```

**c) `scenario ... is:`** — worked examples with the answers we expect. These are our test cases.

---

## 4 — Reading a rule, line by line

Take the one above.

| What you see | What it means |
|---|---|
| `% s 36-15(4)(a). The excess of deductions...` | A comment. Our plain-English claim about what this rule does. **Check this against the rule below it.** |
| `a taxpayer has net exempt income left of an amount in a year` | The conclusion. "There is an amount of net exempt income left." |
| `if the taxpayer has net exempt income of a net exempt amount in the year` | First condition. "…given the year's net exempt income (call it X)…" |
| `and the taxpayer has an excess of deductions of an excess amount in the year` | Second condition. "…and the excess of deductions over assessable income (call it Y)…" |
| `and a remainder = net exempt amount - excess amount` | The arithmetic. "X minus Y." |
| `and the maximum of the remainder and 0 is the amount` | "…and if that would be negative, it is nil." |

Read as ordinary prose: *"The net exempt income left for the year is the year's net exempt income
less the excess of deductions over assessable income, or nil if that would be negative."*

**The question for you is only: is that a correct statement of s 36-15(4)(a)?**

---

## 5 — The bits that look alarming and aren't

Everything on this list is cosmetic. None of it affects what you're checking.

| Looks like | Actually is |
|---|---|
| `*a taxpayer*` with asterisks | A blank in a sentence pattern. Only in the templates section, which you skip. |
| `% something` | A comment — our note to you. Often the most useful line on the page. |
| `a net exempt amount` where you expect a number | A named placeholder, like "let X be…". The name is chosen to read as English. |
| `the maximum of X and 0 is Y` | "Y is X, or nil if X would be negative." |
| `a remainder = A - B` | Ordinary subtraction. |
| `it is not the case that ...` | "…is not true." Standard negation. |
| Indentation | Grouping, the way sub-paragraphs group in a section. Conditions at the same indent are joined by `and` / `or`. |
| `scenario ticket is:` | A worked example. `ticket` is just its name. |
| `expects answers ["… 1529 …"]` | The answer we expect that example to produce. If we're wrong, the test fails loudly. |
| `; scenario element` | Housekeeping: "this fact is always supplied per-case, never derived." Ignore it. |
| `the target language is: prolog.` | Machine housekeeping. Ignore it. |
| `FY2026`, `section 52-10` | Labels. `section 52-10` in the examples is a *placeholder* — see §8. |

**If something not on this list makes you hesitate, that's a finding.** Write it down.

---

## 6 — What we're asking you to check

In rough order of value to us.

**1. Is each rule a correct statement of the law it cites?**
The comment above each rule says what we think the provision does. Is that right? Does the rule
underneath actually do that?

**2. Is the provision correctly identified?**
Right Act, right section, right subsection, and still in force for the relevant year. Phase 1's most
valuable findings were of exactly this kind — a repealed subsection, a misapplied ruling, a
fabricated TR reference.

**3. Is anything missing?**
A condition, an exception, a proviso, a carve-out. A rule that is right as far as it goes but silent
on a limb is the most dangerous kind of error here, because it produces a confident wrong answer.

**4. Is the order right?**
This whole exercise exists because a sequencing step was omitted. Where the law says one thing
happens *before* another, does the file do that?

**5. Do the worked examples actually follow?**
The `scenario` blocks carry figures and expected answers. Work them through. If a number doesn't
follow from the rules, one of the two is wrong.

**6. Is anything asserted that the law doesn't say?**
Over-reach is as much a defect as omission.

**7. What has been assumed without being stated?**
Entity type, residency, income year, the character of a receipt. If a rule quietly assumes something,
say so.

**8. Where would this give a wrong answer that looks right?**
The most valuable question on this list. If you can construct a fact pattern where the file produces
a plausible figure that is wrong, that is worth the whole fee on its own.

---

## 7 — What we are *not* asking

- **Not** to review coding style, structure, or elegance.
- **Not** to run anything.
- **Not** to suggest how to fix it. Telling us it's wrong, and why, is the deliverable. The fix is our job.
- **Not** to be diplomatic. See below.

---

## 8 — Things about this particular file you should know

**`section 52-10` in the scenarios is a placeholder.** It stands in for "some provision that makes
this receipt exempt". We are not asserting that s 52-10 applies to anything in particular. The point
being modelled is that the provision must be *named* — not which one it is.

**The taxpayer is fictional.** "Wren Kavanagh" and "Trellis Holdings Pty Ltd" are stand-ins. The
figures are from the real ticket.

**Division 165 is not modelled.** For the company scenario, continuity of ownership and business
continuity tests could independently deny the loss. We know. Out of scope for this file — but if you
think that omission makes the file misleading, say so.

**One scenario deliberately produces no answer.** `scenario uncharacterised` leaves the character of
the receipt unstated, and the file refuses to produce a carry-forward figure at all. That is intended
behaviour, not a bug. Whether it's the *right* behaviour is a fair thing to comment on.

---

## 9 — A rejection is worth the same as an approval

Stated plainly because it matters: **the fee is the same whether you approve the file or reject it.**

Phase 1's single most valuable finding, by information per dollar, was a reviewer who rejected our
brief outright — the framing of the question was itself defective. That reviewer was paid in full,
and the finding changed how we write briefs.

There is no version of this where telling us we're wrong costs you anything. If the file is sound,
say so and take the fee. If it's rotten, say that and take the same fee. What we cannot use is a
polite approval of something that isn't right.

---

## 10 — If you want to go deeper (entirely optional)

None of this is required.

- The full working file (same law plus machinery a reviewer doesn't need — aggregation, a
  conservation check, and a corporate-entity branch) is available on request. Email
  `support@lodgeit.net.au` and we'll send it.
- A transcript showing the proof trees the rules produce, in English, is likewise available on
  request.
- The live editor is at **le2.logicalcontracts.com** — you can paste a file in and press a button. It
  is genuinely fun to poke at. It is also entirely unnecessary for this review.

---

## 11 — How to respond

Use the response form we've attached (`03-verdict-form.md`) — it keeps verdicts comparable
across reviewers and slots into our registry. Plain prose in an email is fine too if you'd rather;
we'll transcribe it.

Rough shape of a useful finding:

> **Rule:** "a taxpayer has net exempt income left of an amount in a year"
> **Issue:** The comment cites s 36-15(4)(a), but the rule as written also applies where the taxpayer
> is a corporate tax entity, which is governed by s 36-17(4).
> **Consequence:** Right answer on these figures, wrong provision cited. Would matter where the two
> diverge.
> **Confidence:** High.

Short, specific, points at a line. That's all we need.

Questions at any point — including "I don't understand what this line is doing" — are welcome and
are not a sign you're doing it wrong. They're a sign we wrote it badly.

---

*LodgeiT Labs — support@lodgeit.net.au*
