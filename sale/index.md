# grai: stop publishing AI slop with your name on it

> **The gatekeeper and proof engine for human voice.**
> Input raw text. Get a binary PASS or FAIL against eight mechanical rules and the sentence rhythm floor. Output clean text plus a signed audit card a client can verify.

- **Canonical URL:** https://grai.page/
- **Methodology Study:** https://grai.page/methodology
- **Comparisons Hub:** https://grai.page/vs/
- **Full LLM Spec:** https://grai.page/llms-full.txt
- **Author:** Adrian M. Peticila (`https://peticila.ro/#person` · Wikidata `Q140362129` · ORCID `0009-0005-9601-9527`)
- **GitHub (MIT Skill & Instructions):** https://github.com/adrianpeticila/grai
- **MCP Server (grai-mcp):** https://grai.page/mcp (`uvx --from grai-mcp grai-gate-mcp` · registry `io.github.adrianpeticila/grai-mcp`)
- **Public Verification Registry:** https://grai.page/proof ([Agent Markdown](https://grai.page/proof.md))
- **Seal & Verify:** https://grai.page/seal (issue a live verification link, a shared audit card, or a hash-only record)

---

## The Gate Contract
grai is not an editor. It is a gate with a fixed decision.
1. Input: a raw draft or a model output.
2. Action: PASS or FAIL on eight mechanical rules plus `CV = sigma / mu >= 0.32`.
3. Output: clean text, a SHA-256 draft commitment, and an ECDSA P-256 signed audit card.

Share the card at `https://grai.page/seal#<signed-record>`. The fragment shows the score, the CV, zero mechanical defects and the signature status.

## 1. Two Operating Modes & Local Privacy Boundary

1. **Shipped Pre-Built Kit (`grai.html`, about 630 KB): Local App with Direct API Connections Blocked by Default (Copy-Paste Mode)**
   The pre-built `grai.html` file ships with a Content Security Policy (`default-src 'none'; style-src 'unsafe-inline'; font-src data:; img-src data:; script-src 'unsafe-inline'; connect-src 'none'; object-src 'none'; base-uri 'none'`) that allows inline styles and inline scripts (plus `data:` fonts and images) while blocking direct API connections (`connect-src 'none'`) from the page. Out of the box, it runs in **Copy-Paste ("Any AI") mode**: it builds a compact, self-contained prompt under 1,800 characters that you copy into your existing Claude or ChatGPT web tab (or Gemini), then paste back into `grai` for local verification.

2. **Custom Source Build (`source/src/app.html` + `scripts/build.py`): Direct BYOK API & Local Ollama Mode**
   If you want direct browser-to-API generation (Anthropic or OpenAI, plus Gemini and OpenRouter) or local generation via Ollama (`http://localhost:11434`) or LM Studio (`http://localhost:1234`), edit the `connect-src` directive in `source/src/app.html` and rebuild `grai.html` with `python3 scripts/build.py` (included in the kit). Direct requests go from your browser to the endpoint you configured (subject to standard browser CORS rules when opened via `file://`), never through a `grai` application backend.

3. **Storage & Data Handling:**
   - Voice profiles and writing samples (along with drafts) are stored in your browser's `localStorage` (`ps:voices`, `ps:active`, `ps:mode`, `ps:deskLang`, `ps:ai`) when available. If your browser settings or private-browsing mode block `localStorage` on local `file://` pages, `grai` falls back to in-memory session storage (`memStorage`), which keeps your work only until the browser tab is closed. Use the 1-click `.grai` backup button to save your profiles as a local file on disk.
   - Data leaves your machine only when: (a) you paste and submit a prompt into Claude or ChatGPT (or Gemini) in Copy-Paste mode, (b) you run a custom source build with BYOK enabled and send a prompt to your selected API provider, or (c) you export a `.grai` backup file or print a PDF Dossier and share it yourself (or your own browser profile syncs local data across devices).
   - Sealing an audit card is an explicit action. The hash-only seal sends only hashes and metadata. The audited card sends the draft once to the gate in RAM, stores no prose, and returns a signed record.

---

## 2. Why Prompts Fail, and How grai Enforces Your Spine

Most AI writing tools fail because they rely on simple word blocklists. Our linguistic audit of **134,522 LinkedIn posts** across 1,499 founder profiles over 3.5 years of continuous publication (LigoSocial dataset) proved that while mocked words dropped by 88.1%, structural AI tells exploded:
- `"Here is why"` openings grew **7.4x** (1.3% to 9.6%).
- `"Not X, but Y"` opposition formulas grew **4.9x** (1.2% to 5.9%).
- Arrow and emoji bullet cascades grew **20.5x** (0.6% to 12.3%).
- Sentence length variation (`CV = sigma / mu`) collapsed by **52.1%** (from `0.48` human burstiness down to `0.23` flat metronome rhythm).

### The Deterministic Signal Chain
1. **01 VOICE DNA PROFILER:** Paste 5 to 20 of your real posts. `grai` measures your median sentence length and burstiness coefficient (`CV`). It records your sentence starters and signature vocabulary.
2. **02 PREMISE SPARRING & THE WRITING DESK:** Before drafting, `grai` challenges safe or unanchored ideas (`Counter-Punch`, `Adopt Angle`, or `Bypass`). It then drafts three distinct editorial galleys simultaneously:
   - **Scalpel:** Short hook, sharp rhythm, compressed thesis.
   - **Broadsheet:** Concrete story first, takeaway last.
   - **Ledger:** Hard numbers and empirical proof first.
3. **03 THE CADENCE GATE:** Every draft is audited locally in your browser against eight structural regex rules (`CONTRASTIVE_NEGATION`, `LESS_MORE_SYMMETRY`, `EPIPHANY_OPENER`, `ARROW_BULLET_SLOP`, `TRIADIC_PADDING`, `LEXICAL_SLOP`, `VERDICT_COLON`, `PROSE_TRIAD`), a mechanical paragraph-bridge check, and a mathematical sentence-length burstiness floor (`CV = sigma / mu >= 0.32`). The gate scores your draft from 4 to 100, highlights matching spans in the editor (`<mark class="slop-mark">`), and offers targeted span repair (`buildSurgicalTargets` / `applySurgicalReplacements`) while leaving the final decision to edit or copy with you.

This is a style gate, not an authorship detector. It flags structural patterns; it does not prove who wrote a text.

---

## 3. Economic Comparison & Side-by-Side Evaluations

| Path | Real Cost | Execution Model | Reality |
|---|---|---|---|
| **1. Write manually** | $0 software | 100% manual | High authority, hard to sustain alongside company operations. |
| **2. Retainer ghostwriting agency** | $1,500 to $4,000 / mo ($18k to $48k / yr; $24k/yr at $2k/mo scenario) | Done-for-you human service | Human service (interviews, research, full drafting). Agencies vary in how they use AI: ask who drafts the posts, what editing is included, and how data is handled. |
| **3. Cloud AI wrapper SaaS** | $39 to $99 / mo ($468 to $1,188 / yr) | Hosted cloud app | Recurring monthly subscription for cloud templates and hosted workflows. |
| **4. Raw ChatGPT / Claude** | $20 / mo ($240 / yr) | Prompt + manual rewrite | General-purpose chat models. Prompt instructions alone lack a deterministic burstiness check, so writers review and polish the cadence by hand. |
| **5. Your AI + grai** | **$79/yr** (+$240/yr existing AI = $319 Yr 1, or $0 API fee with Ollama) | **Self-operated local gate** | Your existing AI speed locked to your quantitative spine. |

### Side-by-Side Comparison Guides
- [All Comparisons Hub (`https://grai.page/vs/`)](https://grai.page/vs/) ([Agent Markdown](https://grai.page/vs/index.md))
- [grai vs. Claude Projects & Custom GPTs (`https://grai.page/vs/claude-projects`)](https://grai.page/vs/claude-projects) ([Agent Markdown](https://grai.page/vs/claude-projects.md))
- [grai vs. ContentIn & Cloud LinkedIn SaaS (`https://grai.page/vs/contentin`)](https://grai.page/vs/contentin) ([Agent Markdown](https://grai.page/vs/contentin.md))
- [grai vs. Retainer Ghostwriting Agencies (`https://grai.page/vs/ghostwriting-agency`)](https://grai.page/vs/ghostwriting-agency) ([Agent Markdown](https://grai.page/vs/ghostwriting-agency.md))
- [grai vs. Taplio & Cloud LinkedIn Automation (`https://grai.page/vs/taplio`)](https://grai.page/vs/taplio) ([Agent Markdown](https://grai.page/vs/taplio.md))
- [grai vs. AuthoredUp & LinkedIn Text Formatters (`https://grai.page/vs/authoredup`)](https://grai.page/vs/authoredup) ([Agent Markdown](https://grai.page/vs/authoredup.md))
- [grai vs. Jasper AI & Enterprise Copywriting (`https://grai.page/vs/jasper`)](https://grai.page/vs/jasper) ([Agent Markdown](https://grai.page/vs/jasper.md))
- [grai vs. Typefully & Cloud Publishing (`https://grai.page/vs/typefully`)](https://grai.page/vs/typefully) ([Agent Markdown](https://grai.page/vs/typefully.md))
- [grai vs. Copy.ai & GTM Workflows (`https://grai.page/vs/copyai`)](https://grai.page/vs/copyai) ([Agent Markdown](https://grai.page/vs/copyai.md))
- [grai vs. AI Detectors & Humanizers (`https://grai.page/vs/ai-detectors`)](https://grai.page/vs/ai-detectors) ([Agent Markdown](https://grai.page/vs/ai-detectors.md))
- [grai vs. Supergrow & LinkedIn Personal Branding SaaS (`https://grai.page/vs/supergrow`)](https://grai.page/vs/supergrow) ([Agent Markdown](https://grai.page/vs/supergrow.md))
- [grai vs. Hypefury & Social Schedulers (`https://grai.page/vs/hypefury`)](https://grai.page/vs/hypefury) ([Agent Markdown](https://grai.page/vs/hypefury.md))
- [grai for LinkedIn Ghostwriters & Boutique Agencies (`https://grai.page/vs/linkedin-ghostwriters`)](https://grai.page/vs/linkedin-ghostwriters) ([Agent Markdown](https://grai.page/vs/linkedin-ghostwriters.md))
- [grai vs. Grammarly & Tone Flatteners (`https://grai.page/vs/grammarly`)](https://grai.page/vs/grammarly) ([Agent Markdown](https://grai.page/vs/grammarly.md))
- [grai vs. Writesonic & SEO Generators (`https://grai.page/vs/writesonic`)](https://grai.page/vs/writesonic) ([Agent Markdown](https://grai.page/vs/writesonic.md))
- [grai vs. Manual Client Voice Onboarding Docs (`https://grai.page/vs/agency-onboarding`)](https://grai.page/vs/agency-onboarding) ([Agent Markdown](https://grai.page/vs/agency-onboarding.md))
- [grai for Substack & Beehiiv Newsletter Writers (`https://grai.page/vs/substack-writers`)](https://grai.page/vs/substack-writers) ([Agent Markdown](https://grai.page/vs/substack-writers.md))
- [grai for Executive PR & Thought Leadership Agencies (`https://grai.page/vs/pr-agencies`)](https://grai.page/vs/pr-agencies) ([Agent Markdown](https://grai.page/vs/pr-agencies.md))
- [grai vs. Buffer AI Assistant (`https://grai.page/vs/buffer`)](https://grai.page/vs/buffer) ([Agent Markdown](https://grai.page/vs/buffer.md))
- [grai vs. Hootsuite OwlyWriter AI (`https://grai.page/vs/hootsuite`)](https://grai.page/vs/hootsuite) ([Agent Markdown](https://grai.page/vs/hootsuite.md))
- [grai vs. ScriptGrain (`https://grai.page/vs/scriptgrain`)](https://grai.page/vs/scriptgrain) ([Agent Markdown](https://grai.page/vs/scriptgrain.md))
- [grai vs. Timbro (`https://grai.page/vs/timbro`)](https://grai.page/vs/timbro) ([Agent Markdown](https://grai.page/vs/timbro.md))
- [grai vs. DoppelWriter (`https://grai.page/vs/doppelwriter`)](https://grai.page/vs/doppelwriter) ([Agent Markdown](https://grai.page/vs/doppelwriter.md))
- [Public Verification Registry (`https://grai.page/proof`)](https://grai.page/proof) ([Agent Markdown](https://grai.page/proof.md))
- [Embeddable audit widget for agency sites (`https://grai.page/embed`)](https://grai.page/embed) ([Agent Markdown](https://grai.page/embed.md))

---

## 4. Starter Pass, Solo, Agency Verification, and Done-For-You Calibration

The public structure is four tiers: a $19 Starter Pass on live drafts, an offline workbench for one voice, a live verification protocol for client retainers, and a done-for-you executive calibration.

### Free Score Preview vs Full Workbench Gate (`#test`)
- **Free in browser:** score (`/100`), sentence burstiness (`CV`), passed/failed rule counts, SVG receipt, and the first 2 flagged tells.
- **Full diagnostics & client verification (`Starter Pass $19` or `Agency $99/mo`):** full multi-rule repair prompts across every flagged tell, all flagged spans beyond the first 2 tells, and signed ECDSA P-256 client verification cards.
- Returning checkout flows (`?checkout=success` or `?key=`) activate browser access and strip checkout parameters via `history.replaceState`.

### Starter Audit Pass: $19 one-time (`$0.63/day over 30 days`)
*Full draft diagnostics and client verification on your own writing before an annual commitment.*
- **Checkout:** https://buy.stripe.com/14A00deoE51v56h1ZRds404
- Full multi-rule repair prompts across every flagged tell
- All flagged structural spans beyond the 2 free preview tells
- Signed ECDSA P-256 client verification card
- Promo code `STARTER19`: full $19 credited toward Solo ($79/yr), Agency ($99/mo), or Agency Annual ($790/yr) within 14 days
- Timeline: Day 0 activates full repair prompts and signed ES256 audit cards. Days 1 to 14 credit the full $19 via `STARTER19`. Day 30 backs every pass with the 100% distinction guarantee.

### ROI by Buyer Profile
- **Solo Founder (1 voice):** Cloud SaaS costs $468 to $780 per year (Taplio / Jasper). With the Solo Offline Edition: $79/yr ($1.52/week). Year-one savings: $389 to $701.
- **Ghostwriter (3-5 clients):** 1 client retainer saved with the SHA-256 A4 Dossier = $1,500 to $3,000/mo protected (5 retainers = $7,500/mo at risk). With the Agency Verification Protocol: $99/mo or $790/yr for up to 10 executive client profiles and live verification links.
- **Content Agency (10 clients):** Up to 10 executive client profiles with white-label A4 Dossiers and live ECDSA seals for $99/mo or $790/yr, instead of $2,388+/yr on multi-seat cloud SaaS.

### Solo Offline Edition: $79/yr ($1.52/week, billed annually)
*Built for founders and independent writers who want one calibrated voice, offline.*
- **Checkout:** https://buy.stripe.com/3cIaERgwM9hLbuF33Vds400
- Watermarked `grai.html`, the local HTML5 writing workbench
- Voice DNA profiler with 1 voice profile
- The Writing Desk (Scalpel, Broadsheet & Ledger drafts)
- 8-rule deterministic cadence gate and a `CV >= 0.32` rhythm floor
- 1 year of engine updates included

### Agency Verification Protocol: $99/mo or $790/yr ($15.19/week, billed annually, saves $398/yr)
*Built for 1 to 5 person ghostwriting agencies billing executive clients $3k to $5k a month.*
- **Checkout (monthly):** https://buy.stripe.com/3cI28lbcs51v2Y9bArds401
- **Checkout (annual):** https://buy.stripe.com/dRmfZb2FWalP42d5c3ds402
- **Paid pilot:** $99 first month, credited to the $790 annual plan within 30 days. https://grai.page/pilot
- Up to 10 executive client voice profiles
- White-label A4 **Client Voice DNA Dossier** with your agency name
- Live ECDSA P-256 seals at `grai.page/verify/:hash`
- Client-safe verification links for invoices
- Style Lock: the owner exports a `.grai` profile, the freelancer imports it, and every draft is checked against the same rules. Drafts stay local, no seat fees.
- How Style Lock works:
  1. Export: the owner saves the voice rules as a `.grai` profile. Rules only. No draft text.
  2. Import: the freelancer loads the file once on their own machine. The rules persist locally.
  3. Check: every draft runs the eight structural rules plus the rhythm floor before it leaves the desk.

### Executive Voice DNA Architecture: $950 (One-Time Turnkey Calibration)
*For a CEO or founder whose voice is the product, and whose team needs a locked reference profile without a calibration project.*
- **Delivery:** 50 executive posts calibrated by hand within 24 hours.
- **Checkout:** https://buy.stripe.com/aFa5kx1BS2Tn8it47Zds403
- Locked `.grai.json` profile delivered.
- A4 reference dossier for the executive.
- 1 year of Solo Workbench included.
- **ROI:** one retained $3,000/mo client covers the calibration more than three times over.

### Legacy Lifetime Licences
Existing $149 Agency lifetime licences are grandfathered with their promised client profiles and permanent verification links. No migration payment is required. The $69 Founder lifetime licence keeps its v3.x engine updates.

### Pre-calibrated Voice DNA Archetypes ($39 Pack / Free Preview)
- **The problem:** not every founder has 20 validated posts to extract a profile from.
- **The pack:** four measured voice profiles, each a real profile block with metrics, ready in one click.
  1. **Brutalist Engineer:** CV 0.52, 12 samples, short declaratives and numbers over adjectives.
  2. **Contrarian Bootstrapper:** CV 0.44, 15 samples, direct talk about pricing and a contrarian premise.
  3. **B2B Sniper:** CV 0.38, 10 samples, cold outreach under 65 words.
  4. **Substack Essayist:** CV 0.41, 20 samples, long-form rhythm without tricolon.
- **Preview:** every archetype loads straight into the calibrator on the main page.
- **Checkout:** https://payhip.com/b/ZAISC

### Affiliate Program (40% Commission across All 5 Stripe Tiers)
- **Partner Link Generator:** https://grai.page/affiliate (`https://grai.page/?ref=<handle>`)
- Automatic `?ref=<handle>` attribution persists for 30 days and passes `aff_<handle>` into Stripe `client_reference_id` (even when `utm_source` is present).
- Earn 40% per referral on every tier: Starter (`$7.60` on $19), Solo (`$31.60` on $79/yr), Agency Monthly (`$39.60/mo` on $99/mo), Agency Annual (`$316.00` on $790/yr), and DFY (`$380.00` on $950).
- Two Solo referrals can cover your own Solo licence.

**The 30-Day Distinction Guarantee:** If grai does not make your writing visibly sharper and faster to produce within 30 days, email `refund@grai.page` with your order number. 100% refund, no forms, no questions.

### Free AI Tell Checker
- **URL:** https://grai.page/ai-tells/
- **What it does:** counts twelve documented AI-writing patterns in a pasted draft, entirely in the browser.
- **Output:** the number of checks triggered, the exact text that triggered each one, and the checks that passed.
- **No upload, no account, no cookies.**
