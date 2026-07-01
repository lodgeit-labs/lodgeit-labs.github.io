#!/usr/bin/env python3
"""
Generator for /bounties/bounty-NN-<slug>/index.html pages.

Kept as a build-time script so the ten project pages share the exact same
chrome/nav/footer as /bounties/index.html and /blog/*.

Content authored inline per-bounty as a dict; the HTML is rendered by
substituting into the SKELETON template. Run once, commit the emitted
index.html files. This script itself is committed for reproducibility.
"""

from pathlib import Path
import html

BOUNTIES_DIR = Path(__file__).parent

SKELETON = """<!DOCTYPE html>
<html lang="en" class="scroll-smooth">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | LodgeiT Bounties</title>
    <meta name="description" content="{description}">

    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;700;900&family=JetBrains+Mono:wght@400;700&display=swap" rel="stylesheet">

    <script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {{
            theme: {{
                extend: {{
                    colors: {{
                        lodgeit: {{ blue: '#0066FF', light: '#4D94FF', dark: '#004CCC' }},
                        obsidian: '#0a0f1a',
                        slate: {{ 850: '#151e2e', 900: '#0f172a', 950: '#0b1120' }}
                    }},
                    fontFamily: {{ sans: ['Inter', 'sans-serif'], mono: ['JetBrains Mono', 'monospace'] }},
                    boxShadow: {{
                        'neon': '0 0 20px rgba(0, 102, 255, 0.4)',
                        'glow': '0 0 40px rgba(0, 102, 255, 0.2)',
                    }}
                }}
            }}
        }}
    </script>
    <style>
        body {{ background-color: #0a0f1a; color: #e2e8f0; }}
        .gradient-text {{
            background: linear-gradient(to right, #ffffff, #4D94FF);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }}
        .grid-bg {{
            background-image:
                linear-gradient(to right, rgba(255,255,255,0.03) 1px, transparent 1px),
                linear-gradient(to bottom, rgba(255,255,255,0.03) 1px, transparent 1px);
            background-size: 40px 40px;
        }}
        .card-hover {{ transition: all 0.3s ease; }}
        .card-hover:hover {{
            transform: translateY(-5px);
            box-shadow: 0 0 20px rgba(0, 102, 255, 0.2);
            border-color: #4D94FF;
        }}
        pre {{ background: #0b1120; border: 1px solid #1e293b; border-radius: 0.5rem; padding: 1rem; overflow-x: auto; }}
        code {{ font-family: 'JetBrains Mono', monospace; font-size: 0.85rem; }}
        .prose-lodgeit p {{ margin-bottom: 1rem; line-height: 1.75; color: #cbd5e1; }}
        .prose-lodgeit h3 {{ font-size: 1.25rem; font-weight: 700; color: #ffffff; margin-top: 2rem; margin-bottom: 1rem; }}
        .prose-lodgeit h4 {{ font-size: 1.05rem; font-weight: 700; color: #ffffff; margin-top: 1.5rem; margin-bottom: 0.75rem; }}
        .prose-lodgeit ul {{ list-style: none; padding-left: 0; margin-bottom: 1rem; }}
        .prose-lodgeit ul li {{ padding-left: 1.5rem; position: relative; margin-bottom: 0.5rem; color: #cbd5e1; line-height: 1.7; }}
        .prose-lodgeit ul li::before {{ content: '—'; position: absolute; left: 0; color: #4D94FF; }}
        .prose-lodgeit ol {{ padding-left: 1.5rem; margin-bottom: 1rem; }}
        .prose-lodgeit ol li {{ margin-bottom: 0.5rem; color: #cbd5e1; line-height: 1.7; }}
        .prose-lodgeit table {{ width: 100%; border-collapse: collapse; margin: 1.5rem 0; font-size: 0.9rem; }}
        .prose-lodgeit th, .prose-lodgeit td {{ border: 1px solid #1e293b; padding: 0.6rem 0.8rem; text-align: left; }}
        .prose-lodgeit th {{ background: #0b1120; color: #ffffff; font-weight: 700; }}
        .prose-lodgeit td {{ color: #cbd5e1; }}
        .prose-lodgeit strong {{ color: #ffffff; font-weight: 700; }}
        .prose-lodgeit em {{ color: #94a3b8; }}
        .prose-lodgeit blockquote {{ border-left: 3px solid #4D94FF; padding-left: 1rem; margin: 1.5rem 0; color: #94a3b8; font-style: italic; }}
    </style>
</head>
<body class="font-sans antialiased grid-bg selection:bg-lodgeit-blue selection:text-white min-h-screen flex flex-col">

    <!-- Header -->
    <header class="border-b border-slate-800 bg-obsidian/80 backdrop-blur-md sticky top-0 z-50">
        <div class="max-w-7xl mx-auto px-6 py-4 flex justify-between items-center">
            <a href="/" class="flex items-center space-x-3">
                <img src="/assets/lodgeit-logo.png" alt="LodgeiT" class="h-8 w-auto">
                <span class="text-lodgeit-light font-mono text-sm font-bold tracking-tight mt-1">.ORG</span>
            </a>
            <nav class="hidden md:flex space-x-8 text-sm font-medium text-slate-400">
                <a href="/#discipline" class="hover:text-white transition">Discipline</a>
                <a href="/#ecosystem" class="hover:text-white transition">Ecosystem</a>
                <a href="/blog/" class="hover:text-white transition">Blog</a>
                <a href="/bounties/" class="hover:text-white transition">Bounties</a>
                <a href="https://github.com/lodgeit-labs" target="_blank" class="hover:text-white transition">GitHub Organization</a>
                <a href="https://lodgeit.net.au" target="_blank" class="hover:text-white transition">LodgeiT Commercial</a>
            </nav>
        </div>
    </header>

    <main class="flex-grow">

        <!-- Breadcrumb -->
        <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 pt-8">
            <p class="font-mono text-xs text-slate-500">
                <a href="/bounties/" class="hover:text-lodgeit-light transition">&larr; Bounties</a>
                &nbsp;/&nbsp; Bounty #{num_padded}
            </p>
        </div>

        <!-- Hero -->
        <section class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-10">
            <div class="flex items-center justify-between mb-6">
                <span class="text-lodgeit-light font-mono text-xs uppercase tracking-widest">Bounty #{num_padded} &middot; {calc_status}</span>
                <span class="text-white bg-lodgeit-blue px-4 py-2 rounded-full text-sm font-mono font-bold">${prize}</span>
            </div>
            <h1 class="text-3xl md:text-5xl font-black text-white leading-tight mb-6">
                <span class="gradient-text">{title}</span>
            </h1>
            <p class="text-slate-300 text-lg leading-relaxed mb-6">
                {tagline}
            </p>
            <div class="flex flex-wrap gap-3 text-xs font-mono">
                <span class="text-slate-400 bg-slate-800/50 border border-slate-700 px-3 py-1 rounded-full">{anchors}</span>
                <span class="text-slate-400 bg-slate-800/50 border border-slate-700 px-3 py-1 rounded-full">~{hours} hours</span>
                <span class="text-slate-400 bg-slate-800/50 border border-slate-700 px-3 py-1 rounded-full">{calculator}</span>
            </div>
        </section>

        <!-- Body -->
        <article class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-10 prose-lodgeit">

            {body}

        </article>

        <!-- Artefacts -->
        <section class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-12 border-t border-slate-800/50">
            <p class="text-lodgeit-light font-mono text-xs uppercase tracking-widest mb-4">Download the brief pack</p>
            <h2 class="text-3xl font-bold text-white mb-4">Artefact bundle</h2>
            <p class="text-slate-400 leading-relaxed mb-6">
                The full brief, worked example, forensic questions, verdict template, TaxGenii statutory appendix, and terms &mdash; all as markdown files you can open, print, or work through offline.
            </p>
            <div class="grid gap-3">
                {artefact_links}
            </div>
        </section>

        <!-- Apply -->
        <section class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-12 border-t border-slate-800/50">
            <p class="text-lodgeit-light font-mono text-xs uppercase tracking-widest mb-4">Reserve this bounty</p>
            <h2 class="text-3xl font-bold text-white mb-6">Ready to take it on?</h2>
            <p class="text-slate-400 leading-relaxed mb-6">
                Email us with a short note &mdash; your name, credential, and any comment on scope. First-in-first-served. We&rsquo;ll confirm reservation within one business day.
            </p>
            <a href="mailto:bounties@lodgeit.org?subject=Bounty%20%23{num_padded}%20-%20{title_url}" class="inline-block px-8 py-4 bg-lodgeit-blue hover:bg-lodgeit-light text-white font-bold rounded-lg transition-all shadow-neon">
                Reserve Bounty #{num_padded}
            </a>
        </section>

        <!-- Nav to next / index -->
        <section class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-12 border-t border-slate-800/50">
            <div class="flex justify-between items-center">
                <a href="/bounties/" class="text-lodgeit-light hover:text-white transition font-mono text-sm">
                    &larr; All bounties
                </a>
                {next_link}
            </div>
        </section>

    </main>

    <!-- Footer -->
    <footer class="border-t border-slate-800 py-8 mt-8">
        <div class="max-w-7xl mx-auto px-6 flex flex-col md:flex-row justify-between items-center text-slate-500 text-sm">
            <p>&copy; 2026 LodgeiT Labs. The methodology is the moat.</p>
            <div class="flex space-x-6 mt-4 md:mt-0">
                <a href="/" class="hover:text-white transition">Home</a>
                <a href="/blog/" class="hover:text-white transition">Blog</a>
                <a href="/bounties/" class="hover:text-white transition">Bounties</a>
                <a href="https://github.com/lodgeit-labs" target="_blank" class="hover:text-white transition">GitHub</a>
            </div>
        </div>
    </footer>

</body>
</html>
"""

# ---------------------------------------------------------------------------
# Per-bounty content
# ---------------------------------------------------------------------------

BOUNTIES = [
    {
        "num": 1,
        "slug": "div7a-minimum-yearly-repayment",
        "title": "Div 7A minimum yearly repayment",
        "title_url": "Div%207A%20MYR",
        "description": "Section 109E benchmark interest MYR audit — statute-to-predicate ratification bounty for CA/CTA/CPA/FIPA.",
        "prize": "550",
        "hours": "2",
        "anchors": "s 109E · s 109N · s 109D ITAA 1936",
        "calculator": "Div7A_Calculator (live)",
        "calc_status": "Calculator live",
        "tagline": "Ratify the minimum yearly repayment engine against the section 109E formula. The compliance loan model, benchmark rate application, repayment timing rules, and the s 109N/109D interaction on shortfall.",
        "artefacts": [
            ("01-brief.md", "Brief — scope, statutory anchors, out-of-scope"),
            ("02-worked-example.md", "Worked example — $100k MHPL→David FY2025 7-year unsecured loan"),
            ("03-forensic-questions.md", "Six forensic questions, easy → hard"),
            ("04-reviewer-verdict-template.md", "Reviewer verdict template (YAML frontmatter)"),
            ("05-taxgenii-appendix.md", "TaxGenii statutory appendix — pre-cited references"),
            ("06-terms.md", "Terms — IP, attribution, payment, timeline"),
        ],
    },
    {
        "num": 2,
        "slug": "depreciation-effective-life",
        "title": "Depreciation effective-life lookup",
        "title_url": "Depreciation%20effective-life",
        "description": "TR 2024/4 effective-life audit — Commissioner's determination vs self-assessment.",
        "prize": "400",
        "hours": "1.5",
        "anchors": "s 40-95, 40-100, 40-105 ITAA 1997 · TR 2024/4",
        "calculator": "Depreciation_Transforms (live)",
        "calc_status": "Calculator live",
        "tagline": "Ratify the effective-life lookup logic. TR 2024/4 Commissioner's determination, s 40-95 self-assessment election, statutory caps under s 40-102, and the ATO's industry-code hierarchy.",
        "artefacts": [
            ("01-brief.md", "Brief — scope, statutory anchors, out-of-scope"),
            ("02-worked-example.md", "Worked example — $18k excavator, plumbing subcontractor FY2025"),
            ("03-forensic-questions.md", "Six forensic questions, easy → hard"),
            ("04-reviewer-verdict-template.md", "Reviewer verdict template (YAML frontmatter)"),
            ("05-taxgenii-appendix.md", "TaxGenii statutory appendix — pre-cited references"),
            ("06-terms.md", "Terms — IP, attribution, payment, timeline"),
        ],
    },
    {
        "num": 3,
        "slug": "instant-asset-write-off",
        "title": "Instant Asset Write-Off eligibility",
        "title_url": "IAWO%20eligibility",
        "description": "$20k IAWO threshold FY2024–25 and the FY2025–26 transition audit.",
        "prize": "450",
        "hours": "2",
        "anchors": "s 328-180 ITAA 1997",
        "calculator": "Depreciation_Transforms (live)",
        "calc_status": "Calculator live",
        "tagline": "Ratify the IAWO eligibility gate. Aggregated turnover, per-asset $20k test (FY24–25), held-ready-for-use requirement, and the transition to the FY25–26 rules.",
        "artefacts": [
            ("01-brief.md", "Brief — scope, statutory anchors, out-of-scope"),
            ("02-worked-example.md", "Worked example — SBE trading co, three assets straddling the threshold"),
            ("03-forensic-questions.md", "Six forensic questions, easy → hard"),
            ("04-reviewer-verdict-template.md", "Reviewer verdict template (YAML frontmatter)"),
            ("05-taxgenii-appendix.md", "TaxGenii statutory appendix — pre-cited references"),
            ("06-terms.md", "Terms — IP, attribution, payment, timeline"),
        ],
    },
    {
        "num": 4,
        "slug": "small-business-general-pool",
        "title": "Small business general pool",
        "title_url": "SB%20general%20pool",
        "description": "Simplified depreciation pool audit — opening balance, additions, 15/30% rates, low-pool-value write-off.",
        "prize": "600",
        "hours": "2.5",
        "anchors": "Subdiv 328-D ITAA 1997",
        "calculator": "Depreciation_Transforms (live)",
        "calc_status": "Calculator live",
        "tagline": "Ratify the small business general pool mechanics. Opening balance carry-in, 15% first-year rate on additions, 30% subsequent-year rate, low-pool-value ($1000 threshold) write-off, and disposal treatment.",
        "artefacts": [
            ("01-brief.md", "Brief — scope, statutory anchors, out-of-scope"),
            ("02-worked-example.md", "Worked example — pool roll-forward with two additions and one disposal"),
            ("03-forensic-questions.md", "Six forensic questions, easy → hard"),
            ("04-reviewer-verdict-template.md", "Reviewer verdict template (YAML frontmatter)"),
            ("05-taxgenii-appendix.md", "TaxGenii statutory appendix — pre-cited references"),
            ("06-terms.md", "Terms — IP, attribution, payment, timeline"),
        ],
    },
    {
        "num": 5,
        "slug": "fbt-car-statutory-vs-operating",
        "title": "FBT car — statutory formula vs operating cost",
        "title_url": "FBT%20car%20method%20election",
        "description": "FBT car benefit — election mechanics between s 9 statutory formula and s 10 operating-cost method.",
        "prize": "800",
        "hours": "3",
        "anchors": "s 8, 9, 10, 10A FBTAA 1986",
        "calculator": "LodgeiT_FBT (live)",
        "calc_status": "Calculator live",
        "tagline": "Ratify the two FBT car methods. When statutory formula (20% of cost) beats operating-cost method (business-use percentage), the log-book requirement, held-period vs days-provided, and the election-once-made rule.",
        "artefacts": [
            ("01-brief.md", "Brief — scope, statutory anchors, out-of-scope"),
            ("02-worked-example.md", "Worked example — $65k SUV, mixed private/business use, log book present"),
            ("03-forensic-questions.md", "Seven forensic questions, easy → hard"),
            ("04-reviewer-verdict-template.md", "Reviewer verdict template (YAML frontmatter)"),
            ("05-taxgenii-appendix.md", "TaxGenii statutory appendix — pre-cited references"),
            ("06-terms.md", "Terms — IP, attribution, payment, timeline"),
        ],
    },
    {
        "num": 6,
        "slug": "fbt-car-parking",
        "title": "FBT car parking — commercial parking station threshold",
        "title_url": "FBT%20car%20parking",
        "description": "Post-TR 2021/2 commercial parking station threshold audit — 1km rule, all-day parking, lowest-fee.",
        "prize": "700",
        "hours": "2.5",
        "anchors": "s 39A FBTAA 1986 · TR 2021/2",
        "calculator": "LodgeiT_FBT (partial)",
        "calc_status": "Calculator partial",
        "tagline": "Ratify the car-parking-fringe-benefit threshold gate under the post-TR 2021/2 regime. The 1km commercial parking station test, what counts as 'all-day parking', the lowest-fee methodology, and the taxable-value calculation.",
        "artefacts": [
            ("01-brief.md", "Brief — scope, statutory anchors, out-of-scope"),
            ("02-worked-example.md", "Worked example — Sydney CBD employer, three nearby parking operators"),
            ("03-forensic-questions.md", "Six forensic questions, easy → hard"),
            ("04-reviewer-verdict-template.md", "Reviewer verdict template (YAML frontmatter)"),
            ("05-taxgenii-appendix.md", "TaxGenii statutory appendix — pre-cited references"),
            ("06-terms.md", "Terms — IP, attribution, payment, timeline"),
        ],
    },
    {
        "num": 7,
        "slug": "hire-purchase-interest-apportionment",
        "title": "Hire purchase — interest apportionment",
        "title_url": "HP%20interest%20apportionment",
        "description": "Division 240 notional loan — actuarial vs Rule-of-78 interest apportionment audit.",
        "prize": "550",
        "hours": "2",
        "anchors": "Div 240 ITAA 1997",
        "calculator": "HP_Calculator (live)",
        "calc_status": "Calculator live",
        "tagline": "Ratify the Division 240 hire-purchase treatment. Notional loan characterisation, actuarial vs Rule-of-78 interest apportionment, the tax-vs-accounting reconciliation, and the balloon-payment edge case.",
        "artefacts": [
            ("01-brief.md", "Brief — scope, statutory anchors, out-of-scope"),
            ("02-worked-example.md", "Worked example — $80k plant HP, 5-year term, monthly instalments + balloon"),
            ("03-forensic-questions.md", "Six forensic questions, easy → hard"),
            ("04-reviewer-verdict-template.md", "Reviewer verdict template (YAML frontmatter)"),
            ("05-taxgenii-appendix.md", "TaxGenii statutory appendix — pre-cited references"),
            ("06-terms.md", "Terms — IP, attribution, payment, timeline"),
        ],
    },
    {
        "num": 8,
        "slug": "cgt-sb-15-year-exemption",
        "title": "CGT small business 15-year exemption",
        "title_url": "CGT%2015-year%20exemption",
        "description": "Subdivision 152-B — basic conditions, 15-year ownership, retirement/incapacity nexus.",
        "prize": "900",
        "hours": "3",
        "anchors": "Subdiv 152-B ITAA 1997",
        "calculator": "Spec-first (no calc yet)",
        "calc_status": "Spec-first bounty",
        "tagline": "Author the ratification spec for the CGT small-business 15-year exemption. Basic conditions (s 152-10), 15-year continuous ownership, retirement or permanent-incapacity nexus, and the interaction with the small-business retirement exemption cap.",
        "artefacts": [
            ("01-brief.md", "Brief — scope, statutory anchors, out-of-scope"),
            ("02-worked-example.md", "Worked example — family trading trust, sole operator retiring at 68"),
            ("03-forensic-questions.md", "Seven forensic questions, easy → hard"),
            ("04-reviewer-verdict-template.md", "Reviewer verdict template (YAML frontmatter)"),
            ("05-taxgenii-appendix.md", "TaxGenii statutory appendix — pre-cited references"),
            ("06-terms.md", "Terms — IP, attribution, payment, timeline"),
        ],
    },
    {
        "num": 9,
        "slug": "cgt-active-asset-test",
        "title": "CGT small business active-asset test",
        "title_url": "CGT%20active-asset%20test",
        "description": "s 152-35 / s 152-40 — half-of-ownership test, main-use exclusions, TR 2019/1 mixed-use guidance.",
        "prize": "750",
        "hours": "2.5",
        "anchors": "s 152-35, s 152-40 ITAA 1997 · TR 2019/1",
        "calculator": "Spec-first (no calc yet)",
        "calc_status": "Spec-first bounty",
        "tagline": "Author the ratification spec for the CGT active-asset test. The half-of-ownership-period test, the main-use exclusion (rent, financial-instrument), the TR 2019/1 mixed-use guidance, and the connected-entity treatment.",
        "artefacts": [
            ("01-brief.md", "Brief — scope, statutory anchors, out-of-scope"),
            ("02-worked-example.md", "Worked example — commercial building 60% owner-occupied, 40% tenanted"),
            ("03-forensic-questions.md", "Six forensic questions, easy → hard"),
            ("04-reviewer-verdict-template.md", "Reviewer verdict template (YAML frontmatter)"),
            ("05-taxgenii-appendix.md", "TaxGenii statutory appendix — pre-cited references"),
            ("06-terms.md", "Terms — IP, attribution, payment, timeline"),
        ],
    },
    {
        "num": 10,
        "slug": "psi-attribution",
        "title": "PSI attribution — 80/20 and results test",
        "title_url": "PSI%20attribution",
        "description": "Div 84–87 personal services income — results test, 80/20 rule, unrelated clients, employment, business premises.",
        "prize": "850",
        "hours": "3",
        "anchors": "Div 84–87 ITAA 1997",
        "calculator": "Spec-first (no calc yet)",
        "calc_status": "Spec-first bounty",
        "tagline": "Author the ratification spec for PSI attribution. The results test (s 87-18), the 80/20 unrelated-clients test (s 87-20), the employment test (s 87-25), the business-premises test (s 87-30), and the attribution mechanics under Div 86.",
        "artefacts": [
            ("01-brief.md", "Brief — scope, statutory anchors, out-of-scope"),
            ("02-worked-example.md", "Worked example — IT contractor, three clients, mixed test outcomes"),
            ("03-forensic-questions.md", "Seven forensic questions, easy → hard"),
            ("04-reviewer-verdict-template.md", "Reviewer verdict template (YAML frontmatter)"),
            ("05-taxgenii-appendix.md", "TaxGenii statutory appendix — pre-cited references"),
            ("06-terms.md", "Terms — IP, attribution, payment, timeline"),
        ],
    },
]


def render_body(b):
    """Render the main article body for a bounty — statute summary, what the reviewer does, edge cases surfaced."""
    return f"""
            <h3>The statutory question</h3>
            <p>{b['tagline']}</p>

            <h3>Why this matters</h3>
            <p>
                Our calculator emits a deterministic answer for any lawful input. The question the bounty answers is:
                <strong>does the calculator's answer match what a competent practitioner would produce from first principles reading the statute?</strong>
                If yes, the calculator's output is a witness. If no, the reviewer's correction becomes the fix.
            </p>
            <p>
                Either way, the reviewer's name is bound to the version of the engine they ratified. That binding &mdash;
                cryptographic hash of the reviewer's verdict against the calculator's version &mdash; travels with the engine downstream.
            </p>

            <h3>What you are being asked to do</h3>
            <ol>
                <li>Read the one-page brief and the worked example.</li>
                <li>Review the six (or seven) forensic questions. These are graded easy &rarr; hard; do not skip the easy ones &mdash; they anchor your reasoning trail.</li>
                <li>Fill out the reviewer-verdict template. It is a structured YAML-frontmatter document with three top-level verdicts &mdash; <span class="text-white font-semibold">ACCEPT</span>, <span class="text-white font-semibold">REJECT</span>, or <span class="text-white font-semibold">FIX</span> &mdash; and space for per-question citation trails.</li>
                <li>Return your verdict by email or as a pull request against the bounty repo. We&rsquo;ll review within one business day and confirm acceptance.</li>
            </ol>

            <h3>What is <em>not</em> in scope</h3>
            <p>
                We are not asking you to review our source code, run our engine, audit our maths, review our software architecture, or understand our cryptographic provenance chain. Those are separate concerns, handled separately. The bounty is a statute-to-predicate ratification exercise, nothing more, nothing less.
            </p>

            <h3>Statutory anchors (pre-loaded)</h3>
            <p>
                The TaxGenii appendix (file 05 in the artefact bundle) contains the primary statutory sections and key rulings pre-cited &mdash; you do not need to hunt sources. If the appendix is thin in an area you consider critical, that is itself useful information &mdash; flag it in your verdict under the &ldquo;coverage gap&rdquo; section and we&rsquo;ll feed the finding back to our knowledge-base team.
            </p>

            <h3>Attribution &mdash; how your work gets credited</h3>
            <p>
                Your accepted verdict is minted into the public <a href="/bounties/#attribution" class="text-lodgeit-light hover:text-white underline">reviewer registry</a> with:
            </p>
            <ul>
                <li>Your name and credential class (CA / CTA / CPA / FIPA / TPB &ndash; registered)</li>
                <li>The verdict hash (SHA-256 of your submitted document)</li>
                <li>The calculator version you ratified</li>
                <li>The publication date</li>
            </ul>
            <p>
                Default is <strong>named credit</strong>. You may opt down to initialled (&ldquo;J.D.&rdquo;) or anonymous when you submit. Opt-down does not reduce the prize.
            </p>

            <h3>Edge cases surfaced in the forensic questions</h3>
            <p>
                Each brief carries one deliberately load-bearing question &mdash; a scenario where a plausible-looking answer is subtly wrong &mdash; and one deliberately open-ended question that invites you to surface something we haven&rsquo;t yet caught. The load-bearing question separates careful readers from skim-readers; the open-ended question is where the best verdicts extract real value beyond the prize.
            </p>
    """


def render_artefact_links(artefacts):
    out = []
    for filename, description in artefacts:
        out.append(f"""<a href="artefacts/{filename}" class="block group rounded-xl bg-obsidian border border-slate-800 hover:border-blue-500/50 card-hover p-5">
                    <div class="flex items-center justify-between">
                        <div class="flex-1">
                            <div class="font-mono text-xs text-lodgeit-light mb-1">{filename}</div>
                            <div class="text-white group-hover:text-blue-400 transition">{description}</div>
                        </div>
                        <div class="text-slate-500 group-hover:text-lodgeit-light transition text-2xl ml-4">&darr;</div>
                    </div>
                </a>""")
    return "\n                ".join(out)


def render_next_link(idx):
    if idx + 1 < len(BOUNTIES):
        b_next = BOUNTIES[idx + 1]
        return f'<a href="/bounties/bounty-{b_next["num"]:02d}-{b_next["slug"]}/" class="text-lodgeit-light hover:text-white transition font-mono text-sm">Next: Bounty #{b_next["num"]:02d} &rarr;</a>'
    return '<a href="mailto:bounties@lodgeit.org" class="text-lodgeit-light hover:text-white transition font-mono text-sm">Get in touch &rarr;</a>'


def main():
    for idx, b in enumerate(BOUNTIES):
        num_padded = f"{b['num']:02d}"
        dir_name = f"bounty-{num_padded}-{b['slug']}"
        target_dir = BOUNTIES_DIR / dir_name
        target_dir.mkdir(exist_ok=True)
        (target_dir / "artefacts").mkdir(exist_ok=True)

        html_out = SKELETON.format(
            title=b["title"],
            title_url=b["title_url"],
            description=b["description"],
            num_padded=num_padded,
            prize=b["prize"],
            hours=b["hours"],
            anchors=b["anchors"],
            calculator=b["calculator"],
            calc_status=b["calc_status"],
            tagline=b["tagline"],
            body=render_body(b),
            artefact_links=render_artefact_links(b["artefacts"]),
            next_link=render_next_link(idx),
        )
        (target_dir / "index.html").write_text(html_out)
        print(f"  wrote {dir_name}/index.html ({len(html_out)} bytes)")


if __name__ == "__main__":
    main()
