# grai vs. ScriptGrain: Local Voice Ownership vs. Cloud Voice Brain SaaS (2026)

> **Last verified against public pricing and vendor documentation:** 2026-11-12
> **Canonical URL:** https://grai.page/vs/scriptgrain

**Direct Answer:** ScriptGrain is a hosted voice profiling and drafting SaaS that builds a 45-point voice profile across 8 groups and stores a persistent Voice Brain across drafts. Paid plans run from Writer (GBP 12/mo or GBP 115/yr) and Operator (GBP 29/mo or GBP 279/yr) to Studio (GBP 99/mo or GBP 949/yr) and Agency (GBP 299/mo or GBP 2,870/yr), with MCP on all tiers. `grai` ($79/yr Solo or $99/mo or $790/yr Agency) is a 618 KB local HTML5 workbench and open-source MCP server. It keeps your `.grai` profiles on your machine, runs a published 8-rule + `CV >= 0.32` deterministic gate offline, and issues ECDSA P-256 verification receipts at `grai.page/verify/:hash`.

### TL;DR Comparison

| Option | Best For | Starting Price | Key Difference |
| :--- | :--- | :--- | :--- |
| **`grai`** (Solo) | Writers and agencies who want local profile files, an open deterministic gate, and signed client proof. | **$79/yr** Solo ($99/mo or $790/yr Agency) | 618 KB local HTML5 app + MIT `grai-mcp` server. 8 regex rules + `CV >= 0.32` floor + ECDSA P-256 receipts. |
| **ScriptGrain** | Teams that want a hosted cloud workspace with a 45-point profile and cross-draft Voice Brain memory. | **GBP 12/month** (GBP 115/yr on Writer; Free tier has 1 draft) | Cloud SaaS with a 120-word 6-signal instant preview, 45-point profile in 8 groups, and hosted Voice Brain memory. |

---

## 1. Hosted Voice Brain vs. Local Deterministic Gate

ScriptGrain is the closest cloud competitor in the voice-profiling category. It analyses writing across 45 points grouped into 8 dimensions, maintains a hosted Voice Brain that remembers prior drafts and edits, and exposes that profile through an MCP integration.

`grai` takes the opposite architectural stance. Instead of storing your voice profile and draft history in a vendor database, `grai` runs inside a single 618 KB HTML5 file on your laptop. Your voice profile exports as a local `.grai` JSON file, and the cadence gate is published regex and burstiness math (`CV = sigma / mu >= 0.32`) that you can inspect line by line.

Both tools agree that generic AI prompts fail. They disagree on who should hold the profile and whether the audit rulebook should be a closed cloud score or an open mathematical contract.

---

## 2. Where ScriptGrain Wins vs. Where grai Wins

### Where ScriptGrain Wins

- **Low-friction 120-word preview:** extracts an initial 6-signal snapshot from a short 120-word sample on the landing page.
- **45-point taxonomy:** breaks voice down into 45 attributes across 8 groups inside a hosted dashboard.
- **Voice Brain memory:** tracks themes and prior drafts inside the cloud workspace so returning users do not re-upload context.
- **Hosted MCP on every tier:** connects the cloud profile to MCP-compatible editors without local file management.

### Where grai Wins

- **Annual cost at Solo and Agency scale:** $79/yr Solo versus GBP 115 to GBP 279/yr, and $790/yr Agency (up to 10 client profiles) versus GBP 949/yr (Studio) or GBP 2,870/yr (Agency).
- **Open, inspectable gate rules:** the 8 structural rules and the `CV >= 0.32` burstiness floor are public code in both the browser workbench and the MIT-licensed `grai-mcp` PyPI package.
- **Zero-prose cryptographic proof:** agencies issue live ECDSA P-256 verification links at `grai.page/verify/:hash` and printable A4 SHA-256 Dossiers without storing client prose on a server.
- **Permanent local ownership:** your `grai.html` file and `.grai` voice profiles stay on your disk even if you stop renewing.

---

## 3. Side-by-Side Technical and Commercial Matrix

| Criterion | grai (Solo $79/yr / Agency $99/mo or $790/yr) | ScriptGrain (GBP 12 to GBP 299 per month) |
| :--- | :--- | :--- |
| Pricing model | **$79/yr** (Solo) or **$99/mo or $790/yr** (Agency) | Free (1 profile, 1 draft), **GBP 12/mo** Writer (GBP 115/yr), **GBP 29/mo** Operator (GBP 279/yr), **GBP 99/mo** Studio (GBP 949/yr), **GBP 299/mo** Agency (GBP 2,870/yr) |
| Where the voice profile lives | Browser `localStorage` and portable `.grai` files on your disk | ScriptGrain cloud account and hosted Voice Brain database |
| Scoring transparency | Published 8 regex rules + `CV >= 0.32` formula, identical in browser and open-source `grai-mcp` | Proprietary 45-point cloud scoring across 8 groups |
| MCP server | Offline stdio server via `uvx --from grai-mcp grai-gate-mcp` (MIT license, zero network required for scoring) | Hosted MCP connection tied to your ScriptGrain account |
| Client verification deliverable | Printable A4 SHA-256 Dossier + public ECDSA P-256 seal at `grai.page/verify/:hash` | Workspace exports and dashboard review |
| What happens if you cancel | You keep `grai.html` and every exported `.grai` profile permanently | Cloud workspace access and hosted Voice Brain quotas end |

---

## 4. 12-Month and 24-Month Total Cost Comparison

| Setup | Month 1 | 12-Month Total | 24-Month Total | What Is Included |
| :--- | :--- | :--- | :--- | :--- |
| **ScriptGrain Writer** (annual billing) | GBP 12 | GBP 115 (GBP 144 monthly) | GBP 230 (GBP 288 monthly) | Entry solo tier with hosted profile and draft limits |
| **ScriptGrain Operator** (annual billing) | GBP 29 | GBP 279 (GBP 348 monthly) | GBP 558 (GBP 696 monthly) | Full solo operator tier with Voice Brain memory |
| **ScriptGrain Studio / Agency** (annual billing) | GBP 99 to GBP 299 | GBP 949 to GBP 2,870 | GBP 1,898 to GBP 5,740 | Multi-profile studio and agency tiers |
| **`grai` Solo Offline Edition** | $79 | $79 | $158 | Local 618 KB workbench + Voice DNA profiler + 8-rule Cadence Gate + `grai-mcp` |
| **`grai` Agency Verification Protocol** (annual) | $790 | $790 | $1,580 | Up to 10 client profiles + A4 SHA-256 Dossiers + live ECDSA seals at `/verify/:hash` |

---

## 5. Privacy and Data Flow Boundary

- **Shipped Pre-Built Kit (`grai.html`):** Ships with a Content Security Policy (`default-src 'none'; style-src 'unsafe-inline'; font-src data:; img-src data:; script-src 'unsafe-inline'; connect-src 'none'; object-src 'none'; base-uri 'none'`) that allows inline styles and inline scripts (plus `data:` fonts and images) while blocking direct API connections (`connect-src 'none'`) from the page. Out of the box, it runs in Copy-Paste mode.
- **Browser Storage:** Voice profiles and writing samples (along with drafts) are stored in your browser's `localStorage` when available. If your browser settings or private-browsing mode block `localStorage` on local `file://` pages, `grai` falls back to in-memory session storage (`memStorage`), which lasts until the tab closes. Export a `.grai` backup file to save your profiles permanently to disk.
- **When data leaves your machine:** (1) when you paste and submit a prompt into Claude or ChatGPT (or Gemini) in Copy-Paste mode, (2) when you run a custom source build with BYOK enabled and send a prompt to your selected API provider, or (3) when you export and share a `.grai` file or PDF Dossier yourself. ScriptGrain, by contrast, stores your voice profile and Voice Brain history in its cloud workspace by design.

---

## 6. Verdict: Which Should You Choose?

**Choose ScriptGrain (GBP 12 to GBP 299/month) if:** you want a hosted cloud application that stores your draft history in a persistent Voice Brain and you prefer a managed SaaS subscription over local files.

**Choose grai ($79/yr Solo, or $99/mo or $790/yr Agency) if:** you want to own your voice profiles as local `.grai` files, run an open deterministic cadence gate offline in your browser or MCP client, and hand agency clients cryptographic verification links at `grai.page/verify/:hash`.

---

## Frequently Asked Questions

### How do ScriptGrain and grai differ in where the voice profile lives?

ScriptGrain stores a 45-point voice profile and Voice Brain draft history inside a hosted cloud subscription. grai extracts a quantitative Voice DNA profile locally in your browser and exports it as a portable `.grai` file that remains on your machine.

### How does the 12-month cost compare between ScriptGrain and grai?

ScriptGrain paid plans start at GBP 12 per month (GBP 115 per year on Writer) and GBP 29 per month (GBP 279 per year on Operator). Studio is GBP 949 per year and Agency is GBP 2,870 per year. grai Solo Offline Edition is USD 79 per year, while the Agency Verification Protocol is USD 99 per month or USD 790 per year for up to 10 executive client profiles.

### Do both tools support Model Context Protocol (MCP)?

Yes. ScriptGrain includes MCP access across its hosted tiers. grai ships the open-source `grai-mcp` server on PyPI (`uvx --from grai-mcp grai-gate-mcp`), which scores drafts offline against the eight structural rules and `CV >= 0.32` floor with zero network calls.

**Checkout:** [Solo Offline Edition ($79/yr)](https://grai.page/#tiers) | [Agency Verification Protocol ($99/mo or $790/yr)](https://grai.page/#tiers)
