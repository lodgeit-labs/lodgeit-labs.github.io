# The Scene Protocol

*Ledgers are caches. Activity is the truth.*

---

## The premise

Every trade is one shared story: a commitment is made, work is done or goods change hands, a claim is issued, money settles, a receipt closes the loop. **Commitment → fulfilment → claim → settlement → receipt.** That lifecycle — the *scene* — is the primary economic object. It happened once, between two parties, in the world.

What each party's accounting system holds is not the scene. It is a **projection** of the scene onto that party's chart of accounts and policy choices. Your ledger and your counterparty's ledger are two cached views of the same shared events — and like all caches, they drift, and the drift has a name: reconciliation.

Accrual accounting, seen this way, is interval arithmetic over the lifecycle. A receivable is the open interval between claim and settlement. Deferred revenue is settlement arriving before fulfilment. The balance sheet is the set of intervals still open at a point in time; the general ledger is the integral of the event stream. None of this is new mathematics — it is what bookkeeping has always computed, one keystroke at a time, from evidence each party gathered separately.

## The oldest idea in accounting

Pacioli described three books, not two. Before the journal and the ledger came the *memoriale* — the memorandum book where the merchant wrote down what actually happened, in full narrative detail, before any of it was formalised into entries. The profession kept the journal and the ledger and quietly dropped the memorial, because capturing rich records of raw activity was expensive and abstracting them was cheap.

The idea has been reinvented on schedule ever since. McCarthy's REA model (1982) formalised resources-events-agents as the proper basis of accounting systems and became ISO 15944-4. Ian Grigg's triple-entry work put it crisply: *the receipt is the transaction* — a single signed record shared between parties beats two private ones. The thesis is old and, we think, correct. What killed every previous attempt was never the theory. It was adoption economics: someone had to key in the memorial by hand, and nobody would.

## Why now

Three preconditions have arrived within a few years of each other.

**The rails.** Structured e-invoicing is becoming the default carrier of business activity. The EU's ViDA package, adopted in 2025, makes digital reporting and structured e-invoicing the norm for cross-border trade from 2030; Australia has set 2026 deadlines for e-invoicing in federal procurement over the Peppol network, with the B2B network growing underneath. The regulator is becoming a subscriber to the activity stream rather than a reader of annual abstracts.

**The capture.** Large language models can finally read the unstructured residue — the emails, contracts, quotes and PDFs that surround every deal. Hand-keying the memorial was the historic killer; nobody has to hand-key it any more.

**The settlement layer is already event-native.** Payment processors emit webhooks. Banks emit feeds. The settlement leg of the lifecycle has been a machine-readable event stream for years.

One precondition is still missing, and it is not arriving from any standards committee: **the trust layer** — what makes a *shared* record of the scene admissible between parties whose interests are adverse, and to the auditors, lenders and regulators who rely on it. That is the piece the Scene Protocol exists to supply.

## What it replaces

Reconciliation is the deadweight loss of not sharing the scene. One scene, honestly shared, supports any number of projections — per party, per basis (accounting, tax, cash), per jurisdiction — provided each projection is a **pure, replayable function** of the scene and a declared policy. When projection is replayable, audit collapses into recomputation: run the same function over the same evidence and compare. Sampling was only ever a workaround for projections that couldn't be re-run.

The risk profile changes shape, and we are direct about this: projection errors are systematic, not random. One wrong policy line misstates everything it matches, identically and silently. That is the argument *for* versioned, dated, attested, replayable policy — the error that would have hidden in ten thousand keystrokes becomes a one-line diff.

## The three components

**Mirror** — ledger mirrors from the systems businesses already use (Xero, QuickBooks, MYOB). Mirror is what kills the cold-start problem that buried every predecessor of this idea: it delivers value against the installed base on day one, with no counterparty adoption required. Backward replay against mirrored ledgers is where the protocol meets existing books.

**Scenery** — the evidence layer: a canonical, hash-chained export format for scenes. Files first, machine-readable, portable. Specification in progress.

**Casting** — the policy layer: projection policy as plain, versioned policy notes. The core mechanic is write-back: every resolved exception becomes a new policy note, so judgment is exercised once and accreted — not re-exercised per transaction, and not drifted through a model's weights. Resolution is layered: personal policy, then firm, then commons, then the statutory floor. Specification in progress.

## The algebra

Six methods define the protocol surface:

`mirror` — replicate an existing ledger faithfully. `project(scene, policy)` — compute a ledger view from evidence and declared policy. `abduce(journals, feeds, policy)` — run projection in reverse: infer *presumptive* scenes from legacy books; the gaps it cannot explain become a work-order, and presumptive scenes upgrade to evidenced ones as evidence attaches. `replay-diff` — recompute and compare, forward for scene-native books and backward for legacy ones. `attest` — bind a party's signature to a scene or a projection. `anchor` — commit a hash of the record to an external timestamping substrate.

## The conformance ladder

* **L0 — Export:** scenes leave the system in the canonical format, complete.
* **L1 — Chained:** exports carry tamper-evident hash chains.
* **L2 — Anchored:** chain heads are anchored to an external substrate.
* **L3 — Attested:** parties sign what they assert.
* **L4 — Interchanged:** two independent implementations exchange scenes and reproduce each other's projections.

The specification will be prose; **the test suite is the law.** Conformance is decided by golden files, not by prose interpretation — any implementation, including a competitor's and including a vibe-coded one, can self-certify by running the suite.

## Commitments

This is a protocol, not a product moat, and the commitments are structural rather than promissory:

* **Local-authoritative.** The user's own repository of scenes is the source of truth. Hosted copies are caches and lose on conflict — as a conformance requirement, not a terms-of-service clause.
* **No hostage data.** A conforming host must re-emit full-fidelity files on demand, or it is nonconforming by definition.
* **Multi-host by design.** Nothing in the format binds a scene repository to any provider, including us.
* **Paid rails that work for everyone.** Anchoring, attestation, conformance certification and per-call verification are metered services (L402) available to every implementation, including competing ones. Ecosystem growth is the revenue model, not the threat model.

## Where this stands — honestly

We run both sides of a live exchange stack — proposals, invoicing, settlement events, auto-journals — and we are turning it into the first conformance experiment: nightly replay-diffs over a real engagement cohort, every diff classified, tamper-detection demonstrated, and the standard reports derived from the scene alone.

Two things should be said plainly. First, this is a **hypothesis with a falsifier**, not a result: if replay-diffs cannot be driven to explainable-zero on a real cohort, the thesis fails in public. Second, a single operator running both sides proves **determinism and tamper-evidence** — it does not and cannot prove trust-minimisation between adverse parties. That claim waits until independent parties run the protocol against each other at L4.

The graveyard of this idea is full — REA tooling, XBRL GL, a decade of triple-entry startups — and it died of adoption economics every time. Our bet is narrow: Mirror pays its way against the installed base before anyone adopts anything, and the test suite makes trust portable. If we are wrong, the replay-diffs will say so.

## Follow the work

The methodology behind this programme — the discipline stack, the audit machinery, the receipts — is public in [brain-pattern](https://github.com/lodgeit-labs/brain-pattern). Statutory calculators are verified in the open through the [bounty programme](/bounties/), where practitioner reviewers are paid to break our reasoning against statute. The Mirror specification and the conformance suite will publish first, here.
