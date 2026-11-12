# grai vs. DoppelWriter: Own Your Voice DNA vs. Imitate 129 Public Writers (2026)

> **Last verified against public pricing and vendor documentation:** 2026-11-12
> **Canonical URL:** https://grai.page/vs/doppelwriter

**Direct Answer:** DoppelWriter is a cloud writing tool built around 129 prebuilt public writer voices and 71 task templates. It offers a Free tier (20 uses/month, or 3 demos/hour without an account) and a Pro plan at $15/month billed annually ($180/yr, or $19/month monthly at $228/yr) for custom voices. `grai` ($79/yr Solo or $99/mo or $790/yr Agency) is a 618 KB local HTML5 workbench built for founders and ghostwriting agencies. It measures your own cadence, enforces 8 deterministic regex rules plus a `CV >= 0.32` burstiness floor, and issues signed client verification links.

### TL;DR Comparison

| Option | Best For | Starting Price | Key Difference |
| :--- | :--- | :--- | :--- |
| **`grai`** (Solo) | Founders and ghostwriters enforcing their own or a client's real cadence before publishing. | **$79/yr** Solo ($99/mo or $790/yr Agency) | 618 KB local HTML5 workbench. 8 structural rules + `CV >= 0.32` floor + A4 SHA-256 Dossiers + ECDSA seals. |
| **DoppelWriter** | Experimenting with 129 famous or public writer styles across 71 task templates in the cloud. | **$15/month** billed annually ($180/yr, or $19/mo monthly; 20 free uses/mo) | Cloud catalog of 129 public voices and 71 templates, plus custom voice creation on the Pro plan. |

---

## 1. Borrowing a Famous Voice vs. Auditing Your Own

DoppelWriter starts with a library of 129 public writer voices and 71 task templates. You pick a public style or create a custom voice on the Pro plan, pick a template, and generate a draft inside the web app.

`grai` is built for people whose own name is on the line: founders, executives and the boutique agencies who write for them. An executive on LinkedIn does not want to sound like a famous novelist. They want their draft to match their own historical sentence-length variance and pass a strict mechanical check so no reader spots synthetic phrasing.

---

## 2. Where DoppelWriter Wins vs. Where grai Wins

### Where DoppelWriter Wins

- **129 prebuilt public voices:** instant experimentation with recognizable literary and public styles without uploading samples first.
- **71 task templates:** structured forms for common writing tasks inside the browser dashboard.
- **Zero-signup demo quota:** allows 3 demos per hour without an account and 20 uses per month on the Free tier.

### Where grai Wins

- **Annual price ($79/yr vs. $180 to $228/yr):** custom voices in DoppelWriter require the Pro plan ($180/yr billed annually or $228/yr monthly). `grai` Solo is $79/yr.
- **Deterministic 8-rule + `CV >= 0.32` gate:** checks every sentence against eight structural anti-slop rules and a mathematical burstiness floor. It highlights exact spans for 1-click surgical repair.
- **Local HTML5 ownership and MCP server:** runs from a 618 KB local file with `connect-src 'none'` by default, plus the MIT-licensed `grai-mcp` server for Claude Desktop, Cursor, Cline and Windsurf.
- **Agency verification protocol ($99/mo or $790/yr):** up to 10 isolated client profiles, printable A4 SHA-256 Dossiers, and live ECDSA P-256 verification links at `grai.page/verify/:hash`.

---

## 3. Side-by-Side Technical and Commercial Matrix

| Criterion | grai (Solo $79/yr / Agency $99/mo or $790/yr) | DoppelWriter (Free / Pro $15 to $19 per month) |
| :--- | :--- | :--- |
| Pricing model | **$79/yr** (Solo) or **$99/mo or $790/yr** (Agency) | Free (20 uses/mo), **$15/mo** Pro billed annually ($180/yr) or **$19/mo** billed monthly ($228/yr) |
| Primary focus | Measuring and enforcing your own or your client's Voice DNA | 129 public writer voices + 71 task templates + Pro custom voices |
| Cadence verification | Deterministic 8 regex rules + `CV >= 0.32` floor + span highlights | No deterministic sentence-rhythm gate |
| Where profiles live | Browser `localStorage` and portable `.grai` files on disk | Hosted inside the DoppelWriter cloud account |
| Agency proof | A4 SHA-256 Dossier + public ECDSA P-256 receipts at `grai.page/verify/:hash` | None |
| What happens if you stop paying | You keep `grai.html` and your `.grai` voice files permanently | Pro custom voices and unlimited cloud generation stop |

---

## 4. 12-Month and 24-Month Total Cost Comparison

| Setup | Month 1 | 12-Month Total | 24-Month Total | What Is Included |
| :--- | :--- | :--- | :--- | :--- |
| **DoppelWriter Pro** (annual billing) | $15 | $180 | $360 | 129 public voices, 71 templates, custom voices in cloud |
| **DoppelWriter Pro** (monthly billing) | $19 | $228 | $456 | Same Pro features on month-to-month billing |
| **`grai` Solo Offline Edition** | $79 | $79 | $158 | Local 618 KB workbench + Voice DNA profiler + 8-rule Cadence Gate + `grai-mcp` |
| **`grai` Agency Verification Protocol** (annual) | $790 | $790 | $1,580 | Up to 10 client profiles + A4 SHA-256 Dossiers + live ECDSA seals at `/verify/:hash` |

---

## 5. Privacy and Data Flow Boundary

- **Shipped Pre-Built Kit (`grai.html`):** Ships with a Content Security Policy (`default-src 'none'; style-src 'unsafe-inline'; font-src data:; img-src data:; script-src 'unsafe-inline'; connect-src 'none'; object-src 'none'; base-uri 'none'`) that allows inline styles and inline scripts (plus `data:` fonts and images) while blocking direct API connections (`connect-src 'none'`) from the page. Out of the box, it runs in Copy-Paste mode.
- **Browser Storage:** Voice profiles and writing samples (along with drafts) are stored in your browser's `localStorage` when available. If your browser settings or private-browsing mode block `localStorage` on local `file://` pages, `grai` falls back to in-memory session storage (`memStorage`), which lasts until the tab closes. Export a `.grai` backup file to save your profiles permanently to disk.
- **When data leaves your machine:** (1) when you paste and submit a prompt into Claude or ChatGPT (or Gemini) in Copy-Paste mode, (2) when you run a custom source build with BYOK enabled and send a prompt to your selected API provider, or (3) when you export and share a `.grai` file or PDF Dossier yourself. DoppelWriter runs generation and custom voices inside its cloud workspace by design.

---

## 6. Verdict: Which Should You Choose?

**Choose DoppelWriter ($15 to $19/month) if:** you want a cloud catalog of 129 famous writer styles and 71 templates for quick creative experiments.

**Choose grai ($79/yr Solo, or $99/mo or $790/yr Agency) if:** you publish under your own or your client's executive name, you need a deterministic 8-rule + `CV >= 0.32` cadence gate, and you want local `.grai` profile files that you own permanently.

---

## Frequently Asked Questions

### What is the main difference between DoppelWriter and grai?

DoppelWriter is a cloud app built around 129 prebuilt public writer voices and 71 task templates, plus custom voice creation on Pro. grai is a local 618 KB HTML5 workbench built to measure and enforce your own executive or founder cadence against 8 structural rules and a `CV >= 0.32` burstiness floor.

### How does the 12-month cost compare between DoppelWriter and grai?

DoppelWriter offers a Free tier (20 uses per month) and a Pro plan at $15 per month billed annually ($180 per year) or $19 per month on monthly billing ($228 per year). grai Solo Offline Edition is $79 per year, and the Agency Verification Protocol is $99 per month or $790 per year.

### Does DoppelWriter include an offline cadence gate or agency verification links?

No. DoppelWriter generates text inside its cloud workspace. grai audits drafts locally in your browser or via the `grai-mcp` server, and issues printable A4 SHA-256 Dossiers plus ECDSA P-256 verification links at `grai.page/verify/:hash`.

**Checkout:** [Solo Offline Edition ($79/yr)](https://grai.page/#tiers) | [Agency Verification Protocol ($99/mo or $790/yr)](https://grai.page/#tiers)
