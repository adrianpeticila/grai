# grai vs. Typefully: Local Voice Ownership vs. Cloud Publishing Calendar (2026)

> **Last verified against public pricing and vendor documentation:** 2026-11-16
> **Canonical URL:** https://grai.page/vs/typefully

**Direct Answer:** Typefully is a cloud publishing tool for X/Twitter, Bluesky, LinkedIn, Threads, Mastodon and Substack. It combines a thread composer, a queue, a publishing calendar and post analytics. Plans run from Free to Creator at $99 per year, with Business at $18 per social set per month on annual billing. It also publishes an API, an MCP server and AI Agent Skills, so Claude, ChatGPT or Notion can queue drafts and read the calendar. `grai` starts at $79/yr for Solo, or $99/mo or $790/yr for Agency, and it is a local-first HTML5 voice workbench that never connects to a social account. It profiles your Voice DNA locally, shapes the argument in three editorial galleys, and audits every draft against 8 structural regex rules plus a mathematical burstiness floor (`CV >= 0.32`).

### TL;DR Comparison

| Option | Best For | Starting Price | Key Difference |
| :--- | :--- | :--- | :--- |
| **`grai`** (Solo) | Making the text itself sound like you, before it reaches any scheduler. | **$79/yr** (AI model/API usage separate if used) | Offline about 630 KB HTML5 workbench. Voice DNA, 3-galley Writing Desk and the 8-rule cadence gate run in your browser. No social account connection. |
| **Typefully** | Writing threads and shipping a consistent posting calendar across X/Twitter, Bluesky, LinkedIn, Threads, Mastodon and Substack. | **$8.25/month** (Creator, $99/year, annual only) | Hosted cloud composer, queue and analytics for six networks, plus an API, an MCP server and AI Agent Skills. Account OAuth is required for publishing. |

---

## 1. Two Different Jobs: Publishing Calendar vs. Voice Instrument

Typefully is built around distribution. You write in a cloud composer, arrange a queue, schedule the week across X/Twitter, Bluesky, LinkedIn, Threads, Mastodon and Substack, and read the analytics in the same dashboard. The value is rhythm of publishing and the fact that you never open the social app to post.

`grai` is built around the text. It extracts a quantitative profile from your real samples, reshapes the premise in three galleys, and runs a deterministic audit before anything is published. It does not schedule, does not queue, and never asks for a social account.

The order matters. A post scheduled at the perfect hour with flat, generic cadence still reads as filler. A post with your real rhythm can be published manually in ten seconds.

---

## 2. Where Typefully Wins vs. Where grai Wins

### Where Typefully Wins

- **Thread composer:** a writing surface built for long X threads, with a clean preview.
- **Queue and scheduling:** a calendar for the week, with automatic publishing at the chosen hour.
- **Cross-posting:** one draft aimed at X/Twitter, Bluesky, LinkedIn, Threads, Mastodon and Substack at the same time.
- **Post analytics:** impressions and engagement for what you published.
- **MCP, API and AI Agent Skills:** a documented API and a hosted MCP server let Claude, ChatGPT or Notion queue drafts and read the calendar, with agent skills for repeatable workflows.
- **LinkedIn PDF carousels:** native document carousels for LinkedIn, alongside threads, images and long-form posts.

### Where grai Wins

- **annual price ($79/yr vs. $99 to $240/year):** Creator is $99 per year, which is about $8.25 per month. Business is $18 per social set per month on annual billing, or $20 monthly. grai is an annual licence; Typefully is a recurring subscription.
- **Zero social OAuth exposure:** `grai` holds no token for X, LinkedIn or any other network and never acts on your account, so no third-party automation flag can reach you.
- **Deterministic cadence gate (`CV >= 0.32`):** audits sentence-length burstiness and 8 structural rules in JavaScript, highlights the matching spans and offers targeted repair.
- **Premise before prose:** three galleys (THE SCALPEL, THE BROADSHEET, THE LEDGER) decide the structure of the argument before a single sentence is written.

---

## 3. Side-by-Side Technical and Commercial Matrix

| Criterion | grai (Solo $79/yr / Agency $99/mo or $790/yr) | Typefully (Free, Creator $99/yr, Business from $18/set/mo, API and MCP) |
| :--- | :--- | :--- |
| Pricing model | **$79/yr** (Solo) or **$99/mo or $790/yr** (Agency) | **Free, Creator $99/year (annual only), Business $18 per set per month annual or $20 monthly** |
| Where the text is produced | **Shipped `grai.html`:** Copy-Paste mode (`connect-src 'none'` blocks direct API calls). **Custom source build:** direct BYOK API or local Ollama | Inside the Typefully cloud composer |
| Cadence verification | Deterministic browser audit: 8 regex rules + `CV >= 0.32` floor + span highlights + targeted repair | No deterministic sentence-rhythm gate |
| Scheduling | None. `grai` writes and audits, nothing else | Queue and auto-publish across X/Twitter, Bluesky, LinkedIn, Threads, Mastodon and Substack |
| Integrations and AI agents | None. No API, no MCP server, no agent skills | API, MCP server, AI Agent Skills, and Claude, ChatGPT or Notion integrations |
| LinkedIn carousels | None. `grai` writes and audits text, nothing else | PDF carousel generator, alongside threads and long-form posts |
| Social account connection | None required (zero OAuth tokens) | Account connection required for publishing |
| What happens if you stop paying | You keep `grai.html` and your `.grai` voice files permanently | Scheduling and analytics stop |

---

## 4. 12-Month and 24-Month Total Cost Comparison

| Setup | Month 1 | 12-Month Total | 24-Month Total | What Is Included |
| :--- | :--- | :--- | :--- | :--- |
| **Typefully Creator** (annual billing) | $8.25 | $99 | $198 | Composer, queue, calendar, 1 social set, 1,000 posts/month, AI, X analytics, API and MCP |
| **Typefully Business** (annual billing, 1 set) | $18 | $216 | $432 | Up to 50 social sets, teams, approvals, higher limits, API and MCP |
| **`grai` Solo + existing Claude Pro / ChatGPT Plus** | $99 ($79 + $20) | $319 ($79 + $240) | $638 ($158 + $480) | Local Voice DNA + Cadence Gate + the AI subscription you already use |
| **`grai` Agency Verification Protocol** (annual) | $790 | $790 | $1,580 | up to 10 client Voice Profiles + A4 SHA-256 Client Voice DNA Dossiers |

---

## 5. Privacy and Data Flow Boundary

- **Shipped Pre-Built Kit (`grai.html`):** Ships with a Content Security Policy (`default-src 'none'; style-src 'unsafe-inline'; font-src data:; img-src data:; script-src 'unsafe-inline'; connect-src 'none'; object-src 'none'; base-uri 'none'`) that allows inline styles and inline scripts (plus `data:` fonts and images) while blocking direct API connections (`connect-src 'none'`) from the page. Out of the box, it runs in Copy-Paste mode.
- **Browser Storage:** Voice profiles and writing samples (along with drafts) are stored in your browser's `localStorage` when available. If your browser settings or private-browsing mode block `localStorage` on local `file://` pages, `grai` falls back to in-memory session storage (`memStorage`), which lasts until the tab closes. Export a `.grai` backup file to save your profiles permanently to disk.
- **When data leaves your machine:** (1) when you paste and submit a prompt into Claude or ChatGPT (or Gemini) in Copy-Paste mode, (2) when you run a custom source build with BYOK enabled and send a prompt to your selected API provider, or (3) when you export and share a `.grai` file or PDF Dossier yourself. Typefully, by contrast, stores drafts and the account connection in its cloud by design.

---

## 6. Verdict: Which Should You Choose?

**Choose Typefully (free plan, Creator $99/year, Business from $18/set/month) if:** you publish across several networks on a schedule and want a queue plus analytics without opening the social app.

**Choose grai ($79/yr) if:** the problem is the writing. A scheduling tool cannot tell you that your sentences are all the same length, and that is the tell readers notice first.

**Use both if:** you draft and audit in grai, then paste the audited text into Typefully and let it publish on schedule. The two do not overlap at all.

---

## Frequently Asked Questions

### Does grai schedule posts like Typefully?

No. Typefully is a cloud publisher with a queue and account connections. grai is a local writing workbench and deterministic cadence auditor: it never connects to a social account and never publishes.

### How does the 12-month cost compare?

Typefully costs $0 on the Free plan, $99 per year on Creator (about $8.25 per month, annual billing only), and $18 per social set per month on Business when billed yearly, or $20 monthly. grai Solo Offline Edition is $79/yr, and the Agency Verification Protocol is $99/mo or $790/yr.

### Can I use grai and Typefully together?

Yes. Draft and audit in grai, then paste the result into Typefully for scheduling. The cadence gate runs before the text reaches the scheduler, which is the order that matters.

**Checkout:** [Solo Offline Edition ($79/yr)](https://grai.page/#tiers) | [Agency Verification Protocol ($99/mo or $790/yr)](https://grai.page/#tiers)
