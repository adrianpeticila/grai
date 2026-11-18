# grai vs. Retainer Ghostwriting Agencies: Software vs. Done-For-You Service (2026)

> **Last verified against public pricing and source architecture:** 2026-10-24
> **Canonical URL:** https://grai.page/vs/ghostwriting-agency

**Direct Answer:** A retainer ghostwriting agency ($1,500 to $4,000/month for a mid-level package, per NYC Ghostwriting's 2026 guide) is a human service that conducts interviews, plans editorial strategy, and writes drafts for you. `grai` ($79/yr Solo / $99/mo or $790/yr Agency, annual licence) is a self-operated local HTML5 software workbench. They are not identical substitutes: founders use `grai` when they want to draft and audit their own posts locally, while agencies buy the $99/mo or $790/yr Agency Verification Protocol to audit client voice standards across their writers.

### TL;DR Comparison

| Option | Best For | Starting Price | Key Difference |
| :--- | :--- | :--- | :--- |
| **`grai`** (Agency) | Solos and agencies wanting self-operated software to profile Voice DNA and audit drafts locally. | **$99/mo or $790/yr** ($79/yr Solo for solo use) | Self-operated software tool. Audits cadence deterministically and exports printable A4 client Dossiers, but requires user-driven drafting. |
| **Retainer Ghostwriting Agency** | Hands-off editorial strategy and done-for-you ghostwriting. | **$1,500 to $4,000/month** (single vendor guide, NYC Ghostwriting; varies by scope) | Full human service with professional editorial judgment. Not an equivalent software comparison; pricing reflects human labor across contract scope. |

---

## 1. How Agencies and Software Fit Together

A skilled human ghostwriter who interviews you, challenges your positioning, and crafts original prose is a high-value editorial partner. The fee buys human labor and judgment: the writer finds the angles, researches the topic, and owns delivery deadlines.

Agencies vary in how they use AI. Before signing a retainer, ask who drafts the posts, what research and editing are included, and how client data is handled. Whether you write your own posts or work with an external ghostwriter, `grai` gives you a deterministic local cadence gate (`CV >= 0.32`) to measure voice fidelity before publishing.

---

## 2. Where a Human Agency Wins vs. Where grai Wins

### Where a Retainer Agency Wins
- **Done-For-You Service:** You share ideas on an interview call; the agency handles research and drafting (plus revisions and publishing when included in your contract scope).
- **Editorial Strategy & Interviews:** A skilled human interviewer pulls stories out of your head that you would never think to write down.
- **Accountability & Calendar Management:** Someone else chases you for approvals and keeps the publishing cadence alive during busy quarters.

### Where grai Wins
- **Self-Operated Workbench at annual cost:** Turn your own raw notes into 3 calibrated galleys (Scalpel, Broadsheet, Ledger) for $79/yr instead of a recurring software subscription.
- **Mathematical Slop Detection (`CV >= 0.32`):** Whether you write the draft yourself or receive it from a ghostwriter, `grai` scores it from 4 to 100 and highlights structural AI tells in your browser.
- **Built FOR Agencies ($99/mo or $790/yr Agency Verification Protocol):** Agencies use `grai` to lock each client's Voice DNA into a portable `.grai` file and print an A4 Dossier for client onboarding.

---

## 3. Side-by-Side Comparison Matrix

| Criterion | `grai` (Solo $79/yr / Agency $99/mo or $790/yr) | Retainer Ghostwriting Agency |
| :--- | :--- | :--- |
| **Category** | Self-operated local HTML5 voice workbench and deterministic cadence auditor | Done-for-you human editorial and ghostwriting service |
| **Typical cost scenario** | **$79/yr** (Solo) or **$99/mo or $790/yr** (Agency) + your existing AI subscription ($240/yr) or local Ollama ($0 API fee) | **$1,500 to $4,000/month** mid-level range ($24,000 over 12 months / $48,000 over 24 months at a $2,000/mo retainer scenario) |
| **Who does the work** | Self-operated (you supply the raw premise, run the prompt, and review highlighted spans) | Human writer and editor (you participate in interview calls and draft approvals per your contract) |
| **Data & raw notes privacy** | Stored in local browser `localStorage` (with session `memStorage` fallback if restricted on `file://`) and user-exported `.grai` files; no `grai` application backend | May be governed by an NDA; actual data handling depends on the agency and its contract (plus the tools its writers use) |
| **Voice fidelity verification** | Deterministic 8-rule regex audit + `CV >= 0.32` floor + span highlights + targeted span repair; user keeps final control over editing and copying | Depends on the assigned writer and editor (unless the agency audits drafts through `grai`) |

---

## 4. Why Ghostwriters & Agencies Buy the $99/mo or $790/yr Agency Verification Protocol

`grai` is not an enemy of good ghostwriters; it is their quality-control instrument. The **Agency Verification Protocol ($99/mo or $790/yr)** includes commercial rights for client work, an multi-client voice switcher, 1-click `.grai` profile sharing over Slack (with zero per-seat cloud fees), and the printable 1-page A4 **Client Voice DNA Dossier** (`#grai-print-certificate`).

When you click *Print cadence certificate* on The Writing Desk, `grai` renders 8 concrete DOM fields onto a single A4 page:
1. **Voice (`#cert-voice`):** The active client profile name.
2. **Samples analysed (`#cert-samples`):** The exact count of real client posts ingested.
3. **Target sentence length (`#cert-len`):** The calibrated length target for the client profile.
4. **Platforms (`#cert-platforms`):** The configured publishing surfaces (such as LinkedIn and X).
5. **Rules passed (`#cert-rules`):** How many of the 8 structural anti-slop rules the active draft passed (`X of 8`).
6. **Cadence score (`#cert-score`):** The 4-to-100 cadence score and measured sentence burstiness (`score/100 (CV X.XX)`).
7. **Generated (`#cert-date`):** The ISO generation date (`YYYY-MM-DD`).
8. **SHA-256 Checksum (`#cert-fingerprint`):** A locally computed `SHA-256` hash over the JSON payload of the profile and audit state (via Web Crypto or `sha256OfflineFallback`). This serves as a deterministic content fingerprint of the audited state, not a third-party identity signature.

---

## 5. Execution Modes & Privacy Boundary

- **Shipped Pre-Built Kit (`grai.html`):** Ships with a Content Security Policy (`default-src 'none'; style-src 'unsafe-inline'; font-src data:; img-src data:; script-src 'unsafe-inline'; connect-src 'none'; object-src 'none'; base-uri 'none'`) that allows inline styles and inline scripts (plus `data:` fonts and images) while blocking direct API connections (`connect-src 'none'`) from the page. Out of the box, it runs in Copy-Paste mode.
- **Custom Source Build:** To enable direct browser-to-API calls (BYOK) or local Ollama (`http://localhost:11434`), edit `connect-src` in `source/src/app.html` and rebuild with `python3 scripts/build.py`.
- **When data leaves your machine:** (1) when you paste and submit a prompt into Claude or ChatGPT (or Gemini) in Copy-Paste mode, (2) when you run a custom source build with BYOK enabled and send a prompt to your selected API provider, or (3) when you voluntarily export and share a `.grai` file or PDF Dossier (such as over Slack or email, which transfers the exported profile to that external communication service), or if your own browser profile syncs local storage across your devices.

---

## 6. Verdict: Which Should You Choose?

- **Hire a human ghostwriting agency ($1,500 to $4,000/mo) if:** you have the budget for a full-service editorial partner, do not want to touch a keyboard, and want a human to interview you and manage your content calendar.
- **Buy `grai` Solo Offline Edition ($79/yr) if:** you prefer to draft and edit your own ideas using your existing AI subscription, or want to audit drafts your ghostwriter sends you before approving them.
- **Buy `grai` Agency Verification Protocol ($99/mo or $790/yr) if:** you are a ghostwriter or agency owner who wants to onboard clients with a measurable A4 Voice DNA Dossier. It helps writers check drafts against each client's cadence with zero monthly seat fees.
- **Checkout:** [Solo Offline Edition ($79/yr)](https://grai.page/#tiers) · [Agency Verification Protocol ($99/mo or $790/yr)](https://grai.page/#tiers)
