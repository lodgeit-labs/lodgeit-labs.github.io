# Bounty #13 — Coal LSL levy: statute-to-calculator review

**Status:** OPEN · SEEKING REVIEWER
**Prize:** AUD $800 ex GST — *proposed; Andrew to confirm the amount before a reviewer is engaged.*
**Estimated effort:** ~3 hours
**Credential class sought:** CA / CTA / CPA / FIPA / TPB-registered, with payroll-tax or
Australian employment-entitlements experience. Coal-industry payroll familiarity is a plus.

---

## The target

An **external contributor's** calculator, newly mounted into the LodgeiT Calculator Constellation:

- **Calculator:** `urn:sbrm:calculator:coal-lsl:levy` (module `urn:sbrm:module:coal-lsl`)
- **What it does:** computes monthly **eligible wages** and the **Coal Mining Industry long
  service leave payroll levy** for **one employee, one month**. The caller establishes the
  employee's eligibility and pay facts; the calculator does not assess them.
- **Built and hosted by:** **Ryan Duguid** — <https://duguid.com.au/>
  (browser version: <https://duguid.com.au/tools/coal-lsl-levy/>).
  Source: `github.com/ryanduguid/ryanduguid.github.io`, path `service/coal-lsl-levy`,
  pinned at revision **`53ba9b8`** (v0.4.0).
- **Hosted on the contributor's own Cloudflare Worker**, not on LodgeiT infrastructure:
  `https://coal-lsl-levy.coal-lsl-levy-service.workers.dev`
- **Page:** <https://lodgeit.org/coal-lsl.html>

This is the **first federated (external-contributor) entry** in the constellation, and the first
to instantiate the `conformance-passed` attestation tier. Your review is what decides whether it
climbs to `practitioner-attested`.

---

## What it ALREADY passes (so you don't re-do this)

The calculator is at attestation tier **conformance-passed**. That means its numbers reproduce
against a pinned, inspectable source — *not* that anyone has certified the tax is correct. The
chain, all independently checkable:

1. **Pinned public source** at `53ba9b8` (v0.4.0).
2. **Public runnable conformance suite:**
   `npm run conformance -- --base https://coal-lsl-levy.coal-lsl-levy-service.workers.dev`
   over **23 synthetic fixtures** (`service/coal-lsl-levy/fixtures/cases.json`): 8 computed
   results, 5 factual refusals, 8 validation failures, 2 unsupported periods.
3. **Live manifest** carries rate/method content hashes and the engine `code_revision`, proving
   the running Worker is the reviewed source.
4. **LodgeiT independent re-pass (2026-10-11):** source tests **64/64**; live conformance
   **16/16** against the Worker; `npm audit --audit-level=high` **0 vulnerabilities**; rounding
   policy `half_up_cent_final_step` matches the published LodgeiT rounding standard; manifest
   hashes are SHA-256 of the served bytes; money returned as decimal strings; the factual
   refusals are exercised. (The Worker unit test `worker.test.mjs` was not run on our host —
   wrangler would not install — a tooling gap, not a defect.)

**Conformance-passed ≠ correct-in-law.** That gap is exactly what this bounty closes.

---

## What we WANT you to review (the actual job)

Read the *Coal Mining Industry (Long Service Leave) Payroll Levy Collection Act 1992* (s 3B) and
the current levy regulations, and **try to break the calculator against the statute.** Specifically:

1. **Eligible-wages definition.** Does the engine's reading of s 3B(1)–(4) match the statute?
   Formula A (base rate including incentive payments and bonuses) vs Formula B (75% of base +
   overtime/penalty rates + allowances other than expense reimbursements), and the "greater of"
   rule. Are the salary-sacrifice (s 3B(4)(a),(aa),(b)) and bonus-frequency (s 3B(4)(c),(d),
   "at least monthly") treatments right?
2. **Levy rate.** The engine applies **2.7%** (from `methods.json`, record `s3b-from-2024-01`).
   **We have flagged this rate as "reviewer to verify"** — confirm 2.7% against the current levy
   regulations for the periods served (and flag any period where it differs).
3. **Formula B basis.** The 0.75 factor and exactly which pay components it sweeps in.
4. **Rounding choice.** The engine rounds once at the end, half up to cents
   (`half_up_cent_final_step`). The contributor documents this as *its own choice, not a
   statutory rule*. Is a single final half-up rounding the right treatment for a levy return, or
   does the statute/regulation prescribe something else (e.g. truncation, per-component rounding)?
5. **Eligibility and branch tests.** `base_rate` / `annual_salary` / `casual` branch selection,
   and the refusals (unknown eligibility, not eligible, casual loading unanswered, casual
   components not read, allowances without the expense-reimbursement assertion). Are the refusals
   the statutorily-correct places to refuse?
6. **Monthly period boundaries.** Supported months are January 2024 to August 2026. Is the
   monthly return period the right unit, and are the boundaries (pre-amendment months, the
   September partial-coverage edge) handled correctly?

The annual-salary and casual branches implement s 3B(2) and s 3B(3); include them in scope.

## Deliver

Fill out the **reviewer verdict template** (file 04): a top-level **ACCEPT / REJECT / FIX**, with
a per-question citation trail to the primary source. Return by email or as a pull request. We
review within one business day. The verdict is published in full with a SHA-256 hash receipt.

**A passing (ACCEPT) verdict lifts the calculator from `conformance-passed` to
`practitioner-attested`**, and your name (or initials, or anonymous — your choice; opt-down does
not reduce the prize) is cryptographically bound to the version you ratified. Ryan Duguid is
credited as the builder on every surface.

---

*Not advice. The statutory anchors here are pointers for a qualified reviewer, not a legal
opinion. Any levy rate or statutory threshold on the calculator pages is reported from the
contributor's pinned source and marked for your verification — it has not been independently
re-derived by LodgeiT.*
