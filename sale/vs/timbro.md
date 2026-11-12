# grai vs. Timbro: Local Voice DNA Workbench vs. Cloud AI Rewriter (2026)

> **Last verified against public pricing and vendor documentation:** 2026-11-12
> **Canonical URL:** https://grai.page/vs/timbro

**Direct Answer:** Timbro is a cloud AI rewriter. It learns from a 900-word sample and rewrites pasted drafts across 7 modes while aiming to preserve facts, numbers, quotes and links. After 3 free rewrites, plans cost $12/month ($144/yr, 110,000 characters), $23/month ($276/yr, 240,000 characters) or $59/month ($708/yr, 620,000 characters). `grai` ($79/yr Solo or $99/mo or $790/yr Agency) is an approximately 630 KB local HTML5 workbench and MCP gate with zero character quotas, 8 deterministic regex rules, a `CV >= 0.32` burstiness floor, and signed client verification receipts.

### TL;DR Comparison

| Option | Best For | Starting Price | Key Difference |
| :--- | :--- | :--- | :--- |
| **`grai`** (Solo) | Full drafting, surgical span repair, unlimited local cadence checks, and agency proof. | **$79/yr** Solo ($99/mo or $790/yr Agency) | about 630 KB local HTML5 workbench + 3-galley Writing Desk + 8-rule deterministic gate + `grai-mcp`. |
| **Timbro** | Rewriting existing AI drafts in the cloud with character-metered quotas and fact preservation. | **$12/month** ($144/yr, 110,000 characters; 3 free rewrites) | Hosted cloud rewriter with 7 rewrite modes and explicit fact, number, quote and link preservation. |

---

## 1. Rewrite Pass vs. Full Writing Workbench & Gate

Timbro is designed for the final rewrite pass. You upload at least 900 words of your own writing, paste a draft produced by ChatGPT or Claude, pick one of seven rewrite modes, and let Timbro rewrite the text inside its cloud interface while keeping your numbers, quotes and links intact.

`grai` covers the entire workflow before and after the draft exists. It extracts a quantitative Voice DNA profile from 5 to 20 posts, challenges weak premises before drafting, generates three structural galleys (Scalpel, Broadsheet, Ledger), and runs a deterministic 8-rule + `CV >= 0.32` audit locally in your browser. Instead of rewriting the whole page blindly, `grai` highlights the exact offending spans and repairs only those spans.

---

## 2. Where Timbro Wins vs. Where grai Wins

### Where Timbro Wins

- **Explicit fact-preservation focus:** built specifically to rewrite prose while keeping embedded numbers, quotes and URLs untouched.
- **Seven rewrite modes:** quick mode switching for users who only want a cloud rewrite pass on an existing draft.
- **Three free rewrites on signup:** lets a casual user test the cloud rewriter before choosing a monthly character quota.

### Where grai Wins

- **$79/yr with zero character caps:** Timbro meters every plan by monthly characters ($144/yr for 110k chars/mo up to $708/yr for 620k chars/mo). `grai` runs locally on your machine with unlimited cadence audits.
- **Deterministic gate instead of black-box rewrite:** a neural rewrite can remove one AI cliche while introducing another. `grai` checks the output against 8 hard regex rules and a `CV >= 0.32` sentence-length variance floor.
- **MCP server included:** `grai-mcp` lets Claude Desktop, Cursor, Cline and Windsurf score drafts offline before showing them to you.
- **Agency verification receipts ($99/mo or $790/yr):** printable A4 SHA-256 Dossiers and live ECDSA P-256 verification links at `grai.page/verify/:hash`.

---

## 3. Side-by-Side Technical and Commercial Matrix

| Criterion | grai (Solo $79/yr / Agency $99/mo or $790/yr) | Timbro ($12 to $59 per month) |
| :--- | :--- | :--- |
| Pricing model | **$79/yr** (Solo) or **$99/mo or $790/yr** (Agency) | 3 free rewrites, then **$12/mo** Starter ($144/yr), **$23/mo** Pro ($276/yr), **$59/mo** Premium ($708/yr) |
| Usage limits | Unlimited local audits and unlimited local prompts | Metered monthly character quotas (110,000 / 240,000 / 620,000 characters) |
| Core mechanism | Voice DNA profiler + 3-galley Writing Desk + 8-rule deterministic gate + surgical span repair | Cloud neural rewriter across 7 modes |
| Cadence verification | 8 regex rules + `CV >= 0.32` burstiness floor in browser and via `grai-mcp` | No deterministic sentence-rhythm gate or public receipt |
| Where data lives | Browser `localStorage` and local `.grai` files on disk | Hosted in the Timbro cloud web application |
| What happens if you stop paying | You keep `grai.html` and your `.grai` voice profiles permanently | Monthly character quota and cloud rewriter access end |

---

## 4. 12-Month and 24-Month Total Cost Comparison

| Setup | Month 1 | 12-Month Total | 24-Month Total | What Is Included |
| :--- | :--- | :--- | :--- | :--- |
| **Timbro Starter** (110,000 chars/mo) | $12 | $144 | $288 | Entry cloud rewriter with 110k monthly character cap |
| **Timbro Pro** (240,000 chars/mo) | $23 | $276 | $552 | Mid-tier cloud rewriter with 240k monthly character cap |
| **Timbro Premium** (620,000 chars/mo) | $59 | $708 | $1,416 | High-volume cloud rewriter with 620k monthly character cap |
| **`grai` Solo Offline Edition** | $79 | $79 | $158 | Unlimited local Voice DNA profiling, 3-galley desk, and 8-rule Cadence Gate |
| **`grai` Agency Verification Protocol** (annual) | $790 | $790 | $1,580 | Up to 10 client profiles + A4 SHA-256 Dossiers + live ECDSA seals at `/verify/:hash` |

---

## 5. Privacy and Data Flow Boundary

- **Shipped Pre-Built Kit (`grai.html`):** Ships with a Content Security Policy (`default-src 'none'; style-src 'unsafe-inline'; font-src data:; img-src data:; script-src 'unsafe-inline'; connect-src 'none'; object-src 'none'; base-uri 'none'`) that allows inline styles and inline scripts (plus `data:` fonts and images) while blocking direct API connections (`connect-src 'none'`) from the page. Out of the box, it runs in Copy-Paste mode.
- **Browser Storage:** Voice profiles and writing samples (along with drafts) are stored in your browser's `localStorage` when available. If your browser settings or private-browsing mode block `localStorage` on local `file://` pages, `grai` falls back to in-memory session storage (`memStorage`), which lasts until the tab closes. Export a `.grai` backup file to save your profiles permanently to disk.
- **When data leaves your machine:** (1) when you paste and submit a prompt into Claude or ChatGPT (or Gemini) in Copy-Paste mode, (2) when you run a custom source build with BYOK enabled and send a prompt to your selected API provider, or (3) when you export and share a `.grai` file or PDF Dossier yourself. Timbro processes every rewrite inside its cloud service by design.

---

## 6. Verdict: Which Should You Choose?

**Choose Timbro ($12 to $59/month) if:** you only want a cloud rewrite button for existing drafts, your monthly volume fits inside a character quota, and you do not need a deterministic cadence gate or agency verification receipts.

**Choose grai ($79/yr Solo, or $99/mo or $790/yr Agency) if:** you want an offline HTML5 workbench with zero character caps, a deterministic 8-rule + `CV >= 0.32` gate that highlights exact spans instead of rewriting blindly, and cryptographic proof for client deliverables.

---

## Frequently Asked Questions

### Is Timbro a writing workbench or a rewriter?

Timbro is a cloud rewriter that learns from your writing samples (minimum 900 words recommended) and rewrites pasted drafts across seven modes while preserving facts, numbers, quotes and links. grai is a local three-column writing workbench, premise sparring tool and deterministic eight-rule cadence gate.

### How does the 12-month cost compare between Timbro and grai?

Timbro offers 3 free rewrites, then charges $12 per month ($144 per year, 110,000 characters) on Starter, $23 per month ($276 per year, 240,000 characters) on Pro, and $59 per month ($708 per year, 620,000 characters) on Premium. grai Solo Offline Edition is $79 per year with unlimited local cadence checks.

### Does Timbro issue client verification links for agencies?

No. Timbro focuses on rewriting text inside its web app. grai Agency Verification Protocol ($99/mo or $790/yr) issues printable A4 SHA-256 Client Voice DNA Dossiers and live ECDSA P-256 verification links at `grai.page/verify/:hash`.

**Checkout:** [Solo Offline Edition ($79/yr)](https://grai.page/#tiers) | [Agency Verification Protocol ($99/mo or $790/yr)](https://grai.page/#tiers)
