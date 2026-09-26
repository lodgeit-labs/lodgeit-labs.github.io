# Verdict form: Bounty #12 (Division 36, revision 2)

Fill in the YAML block below and return this file, as the .md, attached to an email to support@lodgeit.net.au. Prose in the email itself is welcome alongside it. The block exists so your verdict can be hashed and entered in the registry without anyone retyping it. Leave any field blank rather than guess.

```yaml
bounty: 12
revision: 2
file_sha256: aa97844c777b9b46b38aa69b83fe5a6f151f13ac303b2bea3883ae20a5bc6b8d

reviewer:
  name:            # as you want it in the registry, or leave blank
  display: named   # named | initialled | anonymous
  credential:      # e.g. CA, CPA, LLB LLM, registered tax agent
  hours:

verdict: FIX       # ACCEPT | FIX | REJECT
# ACCEPT: the file states the law correctly for its declared scope.
# FIX:    one or more rules misstate the law or misbehave; findings below.
# REJECT: the approach or scope is wrong; a fix would not make it right.

summary: >
  Two or three sentences in your own words.

# Q1  Did you read 01-how-to-read-revision-2? Was any construct unclear?
q1_readability: >

# Q2  Rule-by-rule: did every comment that names a subsection state that
#     subsection correctly? List any that did not, under findings.
q2_comments_state_the_law: yes   # yes | no | partly

# Q3  Did every rule do what its comment says? List any that did not.
q3_rules_match_comments: yes     # yes | no | partly

# Q4  The 36 scenarios: did you trace any by hand? Which, and did the
#     expected figures follow from the Act?
q4_scenarios_traced: []          # e.g. [P5, P7, DM-3]
q4_scenarios_comment: >

# Q5  Unstated assumptions the file relies on that a practitioner would
#     want stated.
q5_assumptions: >

# Q6  A fact pattern where the rules produce a plausible figure that is
#     wrong. Give facts and the figure you expect. Leave empty if none.
q6_break_it:
  facts: >
  expected: >
  file_gives: >          # if you ran it

# Q7  Refusals and unknowns: any case that should refuse and doesn't, or
#     answers when it should say "cannot be determined"?
q7_refusals: >

# Q8  Scope: anything declared out of scope that, in your practice, would
#     make the file unusable for the ordinary individual return?
q8_scope: >

findings:
  - id: F1
    rule: ""             # the rule's first line, or the comment's first words
    subsection: ""       # e.g. s 36-15(4)
    kind: wrong-law      # wrong-law | wrong-figure | unclear | missing | other
    severity: high       # high | medium | low
    text: >
      What is wrong and what it should say.
    fact_pattern: >
      Optional: facts that show it.

answers_to_04_questions:
  QA: >
  QB: >
  QC: >
  QD: >
  QE: >
  QF: >
```

Notes on filling it in:

- **One finding per defect.** A comment that is wrong and a rule that is wrong in the same place are two findings if they would be fixed separately.
- **"wrong-figure"** means the rule's arithmetic gives the wrong number for its stated subsection; **"wrong-law"** means the subsection is misstated; **"unclear"** means you could not tell, which is our defect.
- The `answers_to_04_questions` keys match `04-questions-for-reviewers.md`. They are optional and valued.
- Your fee does not depend on the verdict, the number of findings, or whether you answered the optional questions.
