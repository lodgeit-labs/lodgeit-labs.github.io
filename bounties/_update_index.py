#!/usr/bin/env python3
"""Update bounties/index.html status badges + intro line from bounties/registry/index.yml.

Idempotent by design: re-running produces the same output. Future bounty rounds
cost one registry row + one re-run of this script (no hand-editing HTML).

Kept dependency-free (matches _build_pages.py posture).
"""
import re
from pathlib import Path
from _build_pages import load_registry  # reuse the loader

BOUNTIES_DIR = Path(__file__).parent
INDEX = BOUNTIES_DIR / "index.html"

# 10 canonical bounty ids in order
BOUNTIES_ORDERED = [
    "bounty-01-div7a-minimum-yearly-repayment",
    "bounty-02-depreciation-effective-life",
    "bounty-03-instant-asset-write-off",
    "bounty-04-small-business-general-pool",
    "bounty-05-fbt-car-statutory-vs-operating",
    "bounty-06-fbt-car-parking",
    "bounty-07-hire-purchase-interest-apportionment",
    "bounty-08-cgt-sb-15-year-exemption",
    "bounty-09-cgt-active-asset-test",
    "bounty-10-psi-attribution",
]


def render_status_pill(status):
    if status == "PAID & REVIEWED":
        return (
            '<span class="text-emerald-400 bg-emerald-400/10 border border-emerald-400/20 '
            'px-2.5 py-0.5 rounded-full text-[10px] uppercase tracking-wider font-semibold font-mono ml-2">'
            'PAID &amp; REVIEWED</span>'
        )
    return (
        '<span class="text-slate-400 bg-slate-700/30 border border-slate-600/40 '
        'px-2.5 py-0.5 rounded-full text-[10px] uppercase tracking-wider font-semibold font-mono ml-2">'
        'IN PROGRESS</span>'
    )


def main():
    registry = load_registry()
    html = INDEX.read_text(encoding="utf-8")

    # Update intro line (per PR-B directive)
    old_intro = "Ranked by effort and prize. Bounty #1 is live and dispatched. Bounties #2&ndash;#10 open for applications from today."
    new_intro = (
        "Reviews are published in full, with hash receipts. "
        "See the <a href=\"/bounties/registry/index.yml\" class=\"text-lodgeit-light hover:text-white underline font-mono\">registry index</a> "
        "for the append-only ledger. Two bounties (#3 IAWO, #8 CGT SB 15-year) remain open for reviewers."
    )
    if old_intro in html:
        html = html.replace(old_intro, new_intro)

    # For each bounty, inject a status pill after the BOUNTY #NN span.
    # The pattern in each card is:
    #   <span class="text-lodgeit-light font-mono text-xs font-bold">BOUNTY #NN</span>
    # We insert the pill immediately after that span, inside the same flex row.
    changes = 0
    for bounty_id in BOUNTIES_ORDERED:
        num = bounty_id.split("-")[1]  # "01".."10"
        status = "PAID & REVIEWED" if registry.get(bounty_id) else "IN PROGRESS"
        pill = render_status_pill(status)

        # Match against the specific card by anchoring on the bounty href
        card_href = f'href="/bounties/{bounty_id}/"'
        card_pos = html.find(card_href)
        if card_pos < 0:
            print(f"  MISS: card for {bounty_id} not found")
            continue

        # Find the "BOUNTY #NN" span *after* this href
        span_pat = f'<span class="text-lodgeit-light font-mono text-xs font-bold">BOUNTY #{num}</span>'
        span_pos = html.find(span_pat, card_pos)
        if span_pos < 0:
            print(f"  MISS: BOUNTY #{num} span not found after card href")
            continue

        # Check if pill already there (idempotency)
        after_span = span_pos + len(span_pat)
        if html[after_span:after_span+200].strip().startswith('<span class="text-emerald-400') or \
           html[after_span:after_span+200].strip().startswith('<span class="text-slate-400 bg-slate-700'):
            # Replace existing pill (idempotent update)
            # Find the next </span> after span_pat
            m = re.search(
                r'(<span class="(?:text-emerald-400|text-slate-400 bg-slate-700)[^"]*"[^>]*>[^<]*</span>)',
                html[after_span:after_span+400]
            )
            if m:
                start = after_span + m.start()
                end = after_span + m.end()
                html = html[:start] + pill + html[end:]
                changes += 1
                print(f"  UPDATE: {bounty_id} → {status}")
                continue

        # Insert new
        html = html[:after_span] + pill + html[after_span:]
        changes += 1
        print(f"  INSERT: {bounty_id} → {status}")

    INDEX.write_text(html, encoding="utf-8")
    print(f"\nTotal changes: {changes}")


if __name__ == "__main__":
    main()
