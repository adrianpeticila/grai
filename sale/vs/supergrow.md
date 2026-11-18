# grai vs. Supergrow: $79/yr vs. $372 to $2,388 per Year (2026)

> **Last verified against public pricing and vendor documentation:** 2026-11-12
> **Canonical URL:** https://grai.page/vs/supergrow

**Direct Answer:** Supergrow is a LinkedIn personal branding SaaS with an idea library, a carousel maker, a posting queue and analytics. Pro costs $39/month ($31/month billed annually at $372/yr, or $468/yr monthly) and Teams costs $199/month ($189/month billed annually at $2,268/yr, or $2,388/yr monthly). `grai` ($79/yr, Solo Offline Edition, or $99/mo or $790/yr Agency) is a local-first HTML5 voice workbench. It never connects to a LinkedIn account, and it measures your Voice DNA instead of stocking a content calendar.

### TL;DR Comparison

| Option | Best For | Starting Price | Key Difference |
| :--- | :--- | :--- | :--- |
| **`grai`** (Solo) | Making each post match a measured personal cadence before it ships. | **$79/yr** (AI model/API usage separate if used) | about 630 KB local workbench. Voice DNA, 3-galley Writing Desk and a deterministic 8-rule gate with a `CV >= 0.32` floor. No LinkedIn account connection. |
| **Supergrow** | Solos who want a steady LinkedIn pipeline: ideas, carousels, queue and analytics in one tab. | **$39/month** ($31/month billed annually, Pro tier) | Hosted personal branding suite with a scheduler and carousel builder. The voice layer is a preset, not a measurement. |

---

## 1. Content Pipeline vs. Voice Instrument

Supergrow is built for throughput. You pick from an idea library, turn a post into a carousel, drop it into a queue, and read the analytics afterwards. The value is a publishing habit that survives a busy week, and the calendar is the product.

`grai` is built for the sentence. It extracts a quantitative profile from your real writing, drafts in three editorial galleys, then audits every draft against eight structural rules and a burstiness floor. No queue, no account connection, no carousel.

The two tools answer different questions. A full calendar with a flat rhythm still reads like the same model wrote all of it, which is the failure a founder notices last and an audience notices first.

---

## 2. Where Supergrow Wins vs. Where grai Wins

### Where Supergrow Wins

- **Content ideation:** a library of prompts and hooks so a blank page is never the blocker.
- **Carousel maker:** turns a text post into a swipeable document without a design tool.
- **Queue and analytics:** a publishing rhythm plus the numbers that show what landed.
- **Onboarding speed:** a personal branding suite is running the same day you pay.

### Where grai Wins

- **annual price:** $79/yr against $372 to $2,388 per year, and the files keep working after the year ends.
- **Measured Voice DNA:** a profile from 5 to 20 real samples, stored in your browser, not a brand preset typed into a form.
- **Deterministic gate:** eight regex rules plus a `CV >= 0.32` burstiness floor, with flagged spans and targeted repair before anything ships.
- **Zero OAuth exposure:** `grai` holds no LinkedIn token and cannot trip a third-party automation flag.

---

## 3. Side-by-Side Technical and Commercial Matrix

| Criterion | grai (Solo $79/yr / Agency $99/mo or $790/yr) | Supergrow (Pro $39 / Teams $199 per month) |
| :--- | :--- | :--- |
| Pricing model | **$79/yr** (Solo) or **$99/mo or $790/yr** (Agency) | **$39 to $199 per month** ($31 to $189/month billed annually) |
| Where the text is produced | **Shipped `grai.html`:** Copy-Paste mode (`connect-src 'none'`). **Custom source build:** direct BYOK API or local Ollama | Inside the Supergrow cloud workspace |
| Cadence verification | Deterministic browser audit: 8 regex rules + `CV >= 0.32` floor + span highlights | No deterministic sentence-rhythm gate |
| Scheduling | None. `grai` writes and audits, nothing else | Queue and scheduled publishing for LinkedIn |
| Social account connection | None required (zero OAuth tokens) | Account connection required for publishing |
| What happens if you stop paying | You keep `grai.html` and your `.grai` voice files permanently | Queue, analytics and the idea library stop |

---

## 4. 12-Month and 24-Month Total Cost Comparison

| Setup | Month 1 | 12-Month Total | 24-Month Total | What Is Included |
| :--- | :--- | :--- | :--- | :--- |
| **Supergrow Pro** (monthly billing) | $39 | $468 ($372 annual) | $936 ($744 annual) | Ideas, carousel maker, queue and analytics for one profile |
| **Supergrow Teams** (monthly billing) | $199 | $2,388 ($2,268 annual) | $4,776 ($4,536 annual) | Agency and team workspace with client management |
| **`grai` Solo + existing Claude Pro / ChatGPT Plus** | $99 ($79 + $20) | $319 ($79 + $240) | $638 ($158 + $480) | Local Voice DNA + Cadence Gate + the AI subscription you already use |
| **`grai` Agency Verification Protocol** (annual) | $790 | $790 | $1,580 | up to 10 client Voice Profiles + A4 SHA-256 Client Voice DNA Dossiers |

---

## 5. Privacy and Data Flow Boundary

- **Shipped Pre-Built Kit (`grai.html`):** Ships with a Content Security Policy (`default-src 'none'; style-src 'unsafe-inline'; font-src data:; img-src data:; script-src 'unsafe-inline'; connect-src 'none'; object-src 'none'; base-uri 'none'`) that allows inline styles and inline scripts (plus `data:` fonts and images) while blocking direct API connections (`connect-src 'none'`) from the page. Out of the box, it runs in Copy-Paste mode.
- **Browser Storage:** Voice profiles and writing samples (along with drafts) are stored in your browser's `localStorage` when available. If your browser settings or private-browsing mode block `localStorage` on local `file://` pages, `grai` falls back to in-memory session storage (`memStorage`), which lasts until the tab closes. Export a `.grai` backup file to save your profiles permanently to disk.
- **When data leaves your machine:** (1) when you paste and submit a prompt into Claude or ChatGPT (or Gemini) in Copy-Paste mode, (2) when you run a custom source build with BYOK enabled and send a prompt to your selected API provider, or (3) when you export and share a `.grai` file or PDF Dossier yourself. Supergrow stores drafts and the LinkedIn connection in its cloud by design.

---

## 6. Verdict: Which Should You Choose?

**Choose Supergrow ($39 to $199/month) if:** the blocker is consistency. You need ideas, carousels and a queue that keeps the week moving.

**Choose grai ($79/yr) if:** the blocker is that the posts all sound alike and the calendar will not fix it. A scheduler cannot measure cadence, and a preset cannot replace a profile.

**Use both if:** you draft and audit in grai, then paste the approved text into Supergrow and let the queue do the publishing. The tools do not overlap.

---

## Frequently Asked Questions

### Does grai schedule LinkedIn posts like Supergrow?

No. Supergrow is a personal branding suite with a queue and a LinkedIn connection. grai is a local writing workbench and deterministic cadence auditor: it never connects to a social account and never publishes.

### How does the 12-month cost compare?

Supergrow Pro costs $39 per month ($468 per year monthly, or $31 per month billed annually at $372 per year) and Supergrow Teams costs $199 per month ($2,388 per year monthly, or $189 per month billed annually at $2,268 per year). grai Solo Offline Edition is $79/yr, and the Agency Verification Protocol is $99/mo or $790/yr.

### Can I use grai and Supergrow together?

Yes. Draft and audit in grai, then paste the result into Supergrow for carousels and scheduling. The cadence gate runs before the text reaches the queue, which is the order that matters.

**Checkout:** [Solo Offline Edition ($79/yr)](https://grai.page/#tiers) | [Agency Verification Protocol ($99/mo or $790/yr)](https://grai.page/#tiers)
