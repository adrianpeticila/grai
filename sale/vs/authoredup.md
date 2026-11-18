# grai vs. AuthoredUp: Voice DNA and Cadence Gate vs. LinkedIn Text Formatter (2026)

> **Last verified against public pricing and vendor documentation:** 2026-11-16
> **Canonical URL:** https://grai.page/vs/authoredup

**Direct Answer:** AuthoredUp ($19.95/month, $239.40/year on monthly billing, or $16.63/month billed at $199.50/year) is a LinkedIn formatting extension: bold and italic Unicode, fold preview, snippets and post analytics. Coauthor, its AI writing assistant in closed beta, learns from your own posts, but AuthoredUp publishes no quantitative Voice DNA method and no sentence-length burstiness threshold. `grai` ($79/yr, Solo Offline Edition) is a local voice workbench: it profiles 5 to 20 real texts, runs an 8-rule syntactic gate plus a `CV >= 0.32` floor, and prints an A4 Voice DNA Dossier with a SHA-256 hash.

### TL;DR Comparison

| Option | Best For | Starting Price | Key Difference |
| :--- | :--- | :--- | :--- |
| **`grai`** (Solo) | Proving the text itself does not read like a flat model draft, before it is published. | **$79/yr** (AI model/API usage separate if used) | Local HTML5 workbench, about 630 KB. 8-rule gate + `CV >= 0.32` floor + A4 SHA-256 Dossier. No LinkedIn connection. |
| **AuthoredUp** | Making a finished post look right on LinkedIn: bold, italics, fold preview, snippets. | **$19.95/month** ($239.40/yr monthly, or $16.63/mo billed $199.50/yr) | Browser extension for visual formatting and analytics, plus Coauthor AI in closed beta. No published quantitative voice method or CV floor. |

---

## 1. Different Layers of the Same Post

AuthoredUp works on presentation. It changes how the text renders on LinkedIn: bold and italic Unicode, line breaks that survive the feed, a preview of where the fold cuts the post, reusable snippets and post analytics.

`grai` works on the text before presentation. It measures how you actually write: sentence length distribution, banned constructions, structural habits. It refuses to let a flat rhythm through. A model draft with perfect formatting is still a model draft.

One does not replace the other. A post can be beautifully formatted and still read like a press release written by a machine, which is the real problem. A post can also have a human rhythm; it can still look like a wall of text.

---

## 2. Where AuthoredUp Wins vs. Where grai Wins

### Where AuthoredUp Wins

- **Formatting inside LinkedIn:** bold, italics and Unicode tricks applied where you write, without copy-paste gymnastics.
- **Fold preview:** shows where the see-more cut lands, which is a real distribution lever on LinkedIn.
- **Snippets and templates:** reusable fragments for repeated hooks or signatures.
- **Post analytics:** performance data next to the editor.

### Where grai Wins

- **Quantitative Voice DNA:** extracts measurable habits from 5 to 20 real texts instead of guessing at a tone.
- **Deterministic gate:** 8 syntactic rules plus a burstiness floor (`CV >= 0.32`), computed in JavaScript, with flagged spans and targeted repair.
- **Premise Sparring:** three galleys (THE SCALPEL, THE BROADSHEET, THE LEDGER) reshape the argument before the draft exists, which no formatter does.
- **Client evidence ($99/mo or $790/yr Agency):** an A4 Client Voice DNA Dossier signed with a SHA-256 hash, for studios that must prove the deliverable is not generic.

---

## 3. The Workflow That Uses Both

A practical sequence: shape the premise in `grai` (THE SCALPEL for a sharp claim, THE BROADSHEET for an essay, THE LEDGER for a list). Draft, run the cadence gate until the score is clean, paste the result into LinkedIn, then use AuthoredUp for bold, italics and the fold preview. The formatter never sees a flat draft. The gate never has to care about Unicode, because the measurement happens before presentation.

---

## 4. Side-by-Side Technical and Commercial Matrix

| Criterion | grai (Solo $79/yr / Agency $99/mo or $790/yr) | AuthoredUp ($19.95/mo, or $16.63/mo billed yearly) |
| :--- | :--- | :--- |
| Pricing model | **$79/yr** (Solo) or **$99/mo or $790/yr** (Agency) | **$19.95/mo** ($239.40/yr) or **$16.63/mo** billed $199.50/yr for Individual. Business **$14.95/profile/mo** or **$12.46/profile/mo** billed $149.50/yr |
| Primary job | Voice extraction and deterministic cadence verification | Visual formatting and layout inside LinkedIn |
| Voice DNA profile | Yes: quantitative profile from 5 to 20 samples, stored locally | Coauthor (closed beta) learns from your posts; no published quantitative Voice DNA method |
| Cadence verification | 8 regex rules + `CV >= 0.32` burstiness floor, with flagged spans | Readability grade and length insights; no published sentence-rhythm metric or CV threshold |
| Fold preview | No | Yes, inside the LinkedIn composer |
| LinkedIn account connection | None required | Extension acts inside your logged-in LinkedIn tab |
| What happens if you stop paying | You keep `grai.html` and your `.grai` files permanently | Formatting tools stop working in the composer |

---

## 5. 12-Month and 24-Month Total Cost Comparison

| Setup | Month 1 | 12-Month Total | 24-Month Total | What Is Included |
| :--- | :--- | :--- | :--- | :--- |
| **AuthoredUp Individual** (monthly billing) | $19.95 | $239.40 | $478.80 | Formatting, fold preview, snippets, analytics |
| **AuthoredUp Individual** (annual billing) | $16.63 | $199.50 | $399.00 | Same plan billed yearly |
| **AuthoredUp Business** (monthly billing, per profile) | $14.95 | $179.40 | $358.80 | 3 profile minimum; formatting, analytics, team features |
| **AuthoredUp Business** (annual billing, per profile) | $12.46 | $149.50 | $299.00 | 3 profile minimum; billed yearly |
| **`grai` Solo** (annual) | $79 | $79 | $158 | Local Voice DNA + Cadence Gate + A4 Dossier export, forever |
| **Both, used together** (AuthoredUp monthly) | $88.95 | $308.40 | $547.80 | Formatted posts that also pass the cadence gate |
| **`grai` Agency Verification Protocol** (annual, for studios) | $790 | $790 | $1,580 | up to 10 client profiles and client-ready SHA-256 Dossiers |

---

## 6. Privacy and Data Flow Boundary

- **Shipped Pre-Built Kit (`grai.html`):** Ships with a Content Security Policy (`default-src 'none'; style-src 'unsafe-inline'; font-src data:; img-src data:; script-src 'unsafe-inline'; connect-src 'none'; object-src 'none'; base-uri 'none'`) that allows inline styles and inline scripts (plus `data:` fonts and images) while blocking direct API connections (`connect-src 'none'`) from the page. Out of the box, it runs in Copy-Paste mode.
- **Browser Storage:** Voice profiles and writing samples (along with drafts) are stored in your browser's `localStorage` when available. If your browser settings or private-browsing mode block `localStorage` on local `file://` pages, `grai` falls back to in-memory session storage (`memStorage`), which lasts until the tab closes. Export a `.grai` backup file to save your profiles permanently to disk.
- **When data leaves your machine:** (1) when you paste and submit a prompt into Claude or ChatGPT (or Gemini) in Copy-Paste mode, (2) when you run a custom source build with BYOK enabled and send a prompt to your selected API provider, or (3) when you export and share a `.grai` file or PDF Dossier yourself. A browser extension, by contrast, operates inside the page where you are already logged in, so its permissions deserve a read.

---

## 7. Verdict: Which Should You Choose?

**Choose AuthoredUp ($19.95/month, or $16.63/month billed yearly) if:** your posts already sound like you and the missing piece is presentation inside LinkedIn.

**Choose grai ($79/yr) if:** the text is the problem. Flat rhythm and generic transitions survive every formatter, no matter how clean the layout looks. Only a measurement gate catches them.

**Choose both if:** you publish often and want the argument, the rhythm and the layout controlled at the same time. The combined first-year cost is $308.40, which is less than two years of AuthoredUp alone.

---

## Frequently Asked Questions

### Does AuthoredUp check whether a draft sounds like AI?

No. AuthoredUp is a formatting and analytics extension. Coauthor, its AI assistant in closed beta, learns from your own posts, but AuthoredUp publishes no quantitative voice profile and no sentence-length burstiness metric, so it cannot tell you that a draft has a flat rhythm. grai does that measurement with 8 syntactic rules and a CV floor of 0.32.

### Do I need both grai and AuthoredUp?

Only if you want both jobs done. AuthoredUp formats a post inside LinkedIn; grai verifies that the text has a human cadence and profiles your voice. If you only need bold and italic text plus a fold preview, AuthoredUp alone is enough.

### Which one is cheaper over two years?

grai Solo Offline is $79/yr. AuthoredUp at $19.95 per month costs $478.80 over 24 months, or $399.00 over 24 months on the Individual annual plan at $199.50/year. They solve different problems, so the honest answer is that the comparison only matters if you need voice verification at all.

**Checkout:** [Solo Offline Edition ($79/yr)](https://grai.page/#tiers) | [Agency Verification Protocol ($99/mo or $790/yr)](https://grai.page/#tiers)
