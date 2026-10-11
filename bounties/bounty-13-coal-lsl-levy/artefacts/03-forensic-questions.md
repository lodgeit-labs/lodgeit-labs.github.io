# Forensic questions — Coal LSL levy

Six questions, graded easy → hard. Do not skip the easy ones; they anchor your reasoning trail.
Answer each against the primary source (s 3B of the *Coal Mining Industry (Long Service Leave)
Payroll Levy Collection Act 1992* and the current levy regulations), citing section and
compilation. One question (Q5) is deliberately load-bearing; one (Q6) is deliberately open-ended.

---

**Q1 — The levy rate (verification, not derivation).**
The engine applies a **2.7%** levy rate for all served months (Jan 2024 – Aug 2026), drawn from
`methods.json` record `s3b-from-2024-01`. Confirm 2.7% against the current levy regulations for
these periods. Is there any month in the served range where the applicable rate differs? Cite the
instrument and the rate for the period(s).

**Q2 — Formula A vs Formula B, and the "greater of" rule (s 3B(1)).**
In the base-rate branch, eligible wages are the greater of Formula A (base rate incl. incentive
payments and bonuses) and Formula B (0.75 × (base + overtime/penalty + allowances other than
expense reimbursements)). Is the engine's component split correct? In particular, does Formula A
correctly *exclude* overtime/penalty rates and allowances, and does Formula B correctly *include*
them at the 0.75 factor?

**Q3 — Allowances and the expense-reimbursement carve-out.**
The engine refuses (400) when `allowances` is non-zero but
`allowances_exclude_expense_reimbursements` is not asserted. Is that the right place to refuse —
i.e. does s 3B require that expense-reimbursement allowances be excluded from Formula B, such that
the engine cannot proceed without the caller confirming the allowance figure already excludes
them?

**Q4 — Salary sacrifice and bonus frequency (s 3B(4)).**
The engine reads base rate and ordinary rate *before* salary-sacrifice deductions (s 3B(4)(a),
(aa)) and also applies s 3B(4)(b) to annual salary; and it counts incentive payments and bonuses
only where paid **at least monthly** (s 3B(4)(c),(d) as implemented). Are both treatments
faithful to the statute? Is "at least monthly" the correct frequency threshold?

**Q5 — Rounding choice (LOAD-BEARING).**
The engine computes the levy exactly, then rounds **once at the end**, half up to cents
(`half_up_cent_final_step`: 192.375 → 192.38). The contributor documents this as *its own choice,
not a statutory rule.* Is a single final half-up rounding correct for a Coal LSL levy return? Does
the Act, the regulations, or Coal LSL's own return/remittance practice prescribe a different
rounding (e.g. truncation to the cent, rounding down, or per-component rounding)? If the prescribed
treatment differs, by how much could a monthly levy figure diverge, and in which direction?

**Q6 — Scope and monthly boundaries (OPEN-ENDED).**
Supported months run January 2024 to August 2026, with the pre-amendment casual method deliberately
*not served* before 2024-01, and September 2026 flagged as not-whole-month-covered. Given the
monthly return period: is anything about the levy's statutory operation that the one-employee,
one-month scope cannot capture (e.g. annualisation, caps applied across a period, aggregation
across employees or branches, apprentice/trainee treatment)? Surface anything you consider a
correctness risk that the forensic questions above have not already named.

---

*Not advice. These questions are a review scaffold for a qualified practitioner, not a statement of
the law. Statutory values on the calculator pages are reported from the contributor's pinned source
and marked for your verification.*
