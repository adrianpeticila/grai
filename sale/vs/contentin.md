# grai vs. ContentIn: Local Voice Ownership vs. Cloud LinkedIn SaaS (2026)

> **Last verified against public pricing and source architecture:** 2026-10-24
> **Canonical URL:** https://grai.page/vs/contentin

**Direct Answer:** ContentIn ($39/month, or $468/year on monthly billing) is a hosted cloud LinkedIn SaaS that combines AI ghostwriting, post templates, and LinkedIn post scheduling. `grai` ($79/yr, Solo Offline Edition) is a local-first HTML5 voice workbench that stores your Voice DNA locally and requires zero LinkedIn account connection. It audits every draft against 8 structural regex rules and a mathematical burstiness floor (`CV >= 0.32`).

### TL;DR Comparison

| Option | Best For | Starting Price | Key Difference |
| :--- | :--- | :--- | :--- |
| **`grai`** (Solo) | Quantitative Voice DNA profiling and repeatable local cadence audits before publishing. | **$79/yr** (AI model/API usage separate if used) | Offline about 630 KB HTML5 file. Profiles and cadence checks stay local in your browser, though external AI prompts reach the provider you choose. Requires no LinkedIn connection. |
| **ContentIn** | LinkedIn post drafting and direct calendar scheduling. | **$39/month** (Growth plan on monthly billing) | Hosted cloud SaaS with integrated AI generation and LinkedIn post scheduling. |

---

## 1. Two Different Philosophies: Cloud Distribution Suite vs. Local Voice Instrument

ContentIn is built for users who want a single cloud dashboard where they can browse viral post ideas, generate drafts with hosted AI credits, and schedule posts directly to LinkedIn via OAuth.

`grai` deliberately refuses to be a social media scheduler. It is an approximately 630 KB local HTML5 workbench (`grai.html`) designed for one job: extracting your quantitative Voice DNA and auditing every draft so you never publish synthetic AI slop under your name.

---

## 2. Where ContentIn Wins vs. Where grai Wins

### Where ContentIn Wins
- **Built-In LinkedIn Scheduler:** Queue and auto-publish posts to LinkedIn from a cloud calendar.
- **Hosted AI Credits Included:** Generate drafts inside the web app without pasting prompts into a separate AI tab.
- **Viral Post Feed & Templates:** Browse a library of categorized LinkedIn post templates and hook formulas.
- **LinkedIn Profile Analytics:** Track impressions and follower growth inside the same cloud dashboard.

### Where grai Wins
- **Local Ownership ($79/yr vs. $468/yr):** Buy once. Your Voice DNA profile never gets locked behind an expired monthly subscription.
- **Zero LinkedIn OAuth Exposure:** `grai` never connects to your LinkedIn account and never triggers third-party automation flags.
- **Deterministic Cadence Gate (`CV >= 0.32`):** Audits sentence-length burstiness (`CV = sigma / mu >= 0.32`) and 8 structural rules in JavaScript, highlights matching spans, and offers targeted span repair.
- **Multi-Client Agency Dossier ($99/mo or $790/yr):** up to 10 client profiles, 1-click `.grai` Slack sync, and a printable A4 Dossier with 8 audit fields.

---

## 3. Side-by-Side Technical & Commercial Matrix

| Criterion | `grai` (Solo $79/yr / Agency $99/mo or $790/yr) | ContentIn ($39/mo Cloud SaaS) |
| :--- | :--- | :--- |
| **Pricing model** | **$79/yr** (Solo) or **$99/mo or $790/yr** (Agency) | **$39/month** recurring ($468 over 12 months / $936 over 24 months on monthly billing) |
| **How AI generation runs** | **Shipped `grai.html`:** Copy-Paste mode (`connect-src 'none'` blocks direct API calls). **Custom source build:** Direct BYOK API or local Ollama after editing CSP and running `python3 scripts/build.py` | Cloud-hosted LLM generation included in the monthly subscription |
| **Cadence & anti-slop verification** | Deterministic browser audit: 8 regex rules + `CV >= 0.32` floor + span highlights + targeted span repair; user keeps final control over editing and copying | Cloud prompt emulation ("AI Ghostwriter") without a deterministic local `CV` floor |
| **LinkedIn account connection** | None required (zero OAuth tokens) | Requires LinkedIn OAuth connection for scheduling and analytics |
| **What happens if you stop paying** | Nothing to stop paying; you keep `grai.html` and your `.grai` voice files permanently | Subscription access ends and cloud-hosted workflows stop |

---

## 4. 12-Month & 24-Month Total Cost Comparison

| Setup | Month 1 | 12-Month Total | 24-Month Total | What Is Included |
| :--- | :--- | :--- | :--- | :--- |
| **ContentIn** (monthly billing) | $39 | $468 | $936 | Cloud AI ghostwriter + templates + LinkedIn scheduler |
| **`grai` Solo + existing Claude Pro / ChatGPT Plus** (Copy-Paste mode) | $99 ($79 + $20) | $319 ($79 + $240) | $638 ($158 + $480) | Local Voice DNA + Cadence Gate + frontier AI subscription you already use for work *(or $279 / $558 with annual Claude billing at $200/yr)* |
| **`grai` Solo + custom source build (Local Ollama)** | $79/yr + $0 API fee | $79/yr + $0 API fee | $79/yr + $0 API fee | Local Voice DNA + Cadence Gate + local model *(local hardware/electricity applies; zero API fees)* |

---

## 5. Privacy & Data Flow Boundary

- **Shipped Pre-Built Kit (`grai.html`):** Ships with a Content Security Policy (`default-src 'none'; style-src 'unsafe-inline'; font-src data:; img-src data:; script-src 'unsafe-inline'; connect-src 'none'; object-src 'none'; base-uri 'none'`) that allows inline styles and inline scripts (plus `data:` fonts and images) while blocking direct API connections (`connect-src 'none'`) from the page. Out of the box, it runs in Copy-Paste mode.
- **Browser Storage:** Voice profiles and writing samples (along with drafts) are stored in your browser's `localStorage` when available. If your browser settings or private-browsing mode block `localStorage` on local `file://` pages, `grai` falls back to in-memory session storage (`memStorage`), which lasts until the tab closes. Export a `.grai` backup file to save your profiles permanently to disk.
- **When data leaves your machine:** (1) when you paste and submit a prompt into Claude or ChatGPT (or Gemini) in Copy-Paste mode, (2) when you run a custom source build with BYOK enabled and send a prompt to your selected API provider, or (3) when you export and share a `.grai` file or PDF Dossier yourself (such as over Slack or cloud messaging, where data transfers to that external platform), or if your own browser syncs local data across devices.

---

## 6. Verdict: Which Should You Choose?

- **Choose ContentIn ($39/month) if:** you want a cloud LinkedIn scheduler, analytics dashboard, and template swipe file bundled with hosted AI generation.
- **Choose `grai` ($79/yr, or $99/mo or $790/yr Agency) if:** you prefer to publish manually without connecting third-party OAuth apps to your LinkedIn account, already use Claude or ChatGPT (or local Ollama), and want a deterministic local cadence gate (`CV >= 0.32`) that you own for life.
- **Checkout:** [Solo Offline Edition ($79/yr)](https://grai.page/#tiers) · [Agency Verification Protocol ($99/mo or $790/yr)](https://grai.page/#tiers)
