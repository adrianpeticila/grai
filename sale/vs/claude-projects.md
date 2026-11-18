# grai vs. Claude Projects & Custom GPTs: Why System Prompts Drift (2026)

> **Last verified against public pricing and source architecture:** 2026-10-24
> **Canonical URL:** https://grai.page/vs/claude-projects

**Direct Answer:** Claude Projects (available with Claude Pro at $20/month) and Custom GPTs (available with ChatGPT Plus at $20/month) are cloud chat workspaces that rely on probabilistic instructions. `grai` ($79/yr, Solo Offline Edition) is a local-first HTML5 voice harness that sits on top of Claude or ChatGPT. It extracts quantitative Voice DNA metrics from your posts and runs a deterministic 8-rule regex and sentence-burstiness audit (`CV >= 0.32`) in your browser outside the model.

### TL;DR Comparison

| Option | Best For | Starting Price | Key Difference |
| :--- | :--- | :--- | :--- |
| **`grai`** (Solo) | Measured Voice DNA profiles and repeatable local cadence audits before publishing. | **$79/yr** (model/API usage separate) | Runs locally in your browser. Audits sentence burstiness (`CV >= 0.32`) and 8 regex slop patterns deterministically outside the model. |
| **Claude Projects / Custom GPTs** | General AI chat workspaces for document analysis and interactive research. | **$20/month** ($20/mo Claude Pro; $20/mo ChatGPT Plus) | Cloud LLM chat with persistent prompt instructions. Generation compute is included within vendor plan limits, but instructions remain probabilistic without a deterministic cadence linter. |

---

## 1. Why System Prompts and Mathematical Cadence Differ

Most founders start by opening a Claude Project or Custom GPT and uploading past writing samples. They add custom instructions such as: *"Write in my voice. No fluff. No corporate jargon."*

Prompt instructions tell a model what tone to adopt, but large language models generate tokens probabilistically without calculating the sentence-length variance or running deterministic regex checks while streaming. `grai` complements your model by providing an external, deterministic linter and burstiness calculation (`CV >= 0.32`) directly in your browser.

---

## 2. Where Claude Projects Win vs. Where grai Wins

### Where Claude Projects / Custom GPTs Win
- **Massive Reference Context:** Upload 100-page PDFs and codebases (plus call transcripts) into a single cloud project.
- **Native Mobile & Cloud Sync:** Chat from your phone app and pick up the thread on your laptop automatically.
- **Web Search & General Tasks:** Research live URLs, summarize documents, write code, and brainstorm in one subscription.
- **Built-In Model Compute:** Your $20/month subscription includes frontier LLM generation tokens.

### Where grai Wins
- **Deterministic Cadence Gate (`CV >= 0.32`):** Audits every draft in JavaScript against 8 structural regex rules and a mathematical burstiness floor (`CV = sigma / mu >= 0.32`).
- **Live Highlights & Targeted Span Repair:** Flags matching spans in the editor (`<mark class="slop-mark">`) and generates surgical span replacements without rewriting your unflagged prose.
- **Premise Sparring & 3 Galleys:** Challenges safe takes before drafting and outputs three variations side by side (Scalpel, Broadsheet, Ledger).
- **Works Over Your Existing Claude Tab:** In the default Copy-Paste mode, `grai` builds a dense prompt under 1,800 characters that you paste into Claude Pro at zero extra API cost.

---

## 3. Side-by-Side Technical Matrix

| Criterion | `grai` (Solo $79/yr / Agency $99/mo or $790/yr) | Claude Projects / Custom GPTs |
| :--- | :--- | :--- |
| **Primary role** | Local Voice DNA profiler, 3-column Writing Desk, and deterministic cadence auditor | General-purpose cloud LLM chat with persistent system instructions and file uploads |
| **How AI generation runs** | **Shipped `grai.html`:** Copy-Paste mode (`connect-src 'none'` blocks direct API calls). **Custom source build:** Direct BYOK API or local Ollama after editing CSP and running `python3 scripts/build.py` | Cloud generation included in your $20/mo subscription |
| **Cadence & anti-slop verification** | Deterministic browser audit: 8 regex rules + `CV >= 0.32` floor + span highlights + targeted span repair; user keeps final control over editing and copying | Probabilistic prompt instructions; the model can ignore rules and cannot compute `CV` deterministically |
| **Where voice profiles live** | Browser `localStorage` when available (with session `memStorage` fallback if restricted on `file://`) + 1-click `.grai` local file backup | Stored in your cloud account on Anthropic or OpenAI servers |
| **Client voice proof (Agencies)** | Printable 1-page A4 Dossier (`#grai-print-certificate`) with 8 audit fields and locally computed `SHA-256` payload checksum (Agency Verification Protocol) | None (shared chat links or exported text only) |

---

## 4. Real 12-Month & 24-Month Cost Math

| Setup | Month 1 | 12-Month Total | 24-Month Total | What Does the Work |
| :--- | :--- | :--- | :--- | :--- |
| **Claude Pro alone** (monthly billing) | $20 | $240 | $480 | Cloud LLM chat + static custom instructions |
| **`grai` Solo + Claude Pro** (Copy-Paste mode) | $89 ($79/yr license + $20/mo) | $319 ($79 + $240) | $638 ($158 + $480) | Local Voice DNA + Cadence Gate + Claude generation *(or $279 at 12 mo / $558 at 24 mo with annual Claude billing at $200/yr)* |
| **`grai` Solo + custom source build (Local Ollama)** | $79/yr + $0 API fee | $79/yr + $0 API fee | $79/yr + $0 API fee | Local Voice DNA + Cadence Gate + local model *(local hardware/electricity applies; zero API fees)* |
| **`grai` Solo + custom source build (Direct BYOK API)** | $79/yr + API usage | $79/yr + API usage | $79/yr + API usage | Local Voice DNA + Cadence Gate + direct API calls from your browser |

---

## 5. Privacy & Data Flow Boundary

- **Where your data lives in the browser:** Voice profiles and writing samples (along with drafts) are stored in your browser's `localStorage` (`ps:voices`, `ps:active`, `ps:mode`, `ps:deskLang`, `ps:ai`) when available. If your browser settings or private-browsing mode block `localStorage` on local `file://` pages, `grai` falls back to in-memory session storage (`memStorage`), which keeps your work only until the browser tab is closed. Use the 1-click `.grai` backup button to save your profiles permanently as a local file on disk.
- **When data leaves your machine:**
  1. When you **paste and submit** a prompt into Claude or ChatGPT (or Gemini) in Copy-Paste mode, that text is sent to the AI provider you chose.
  2. When you run a custom source build with BYOK enabled, the prompt is sent from your browser to your selected API provider.
  3. When you export a `.grai` backup file or print a PDF Dossier and share it yourself (such as over Slack or email, which transfers the exported profile to that external communication service), or if your own browser profile syncs local data or clipboard history across your devices.

---

## 6. Verdict: Which Should You Choose?

- **Keep Claude Projects alone if:** you use AI primarily for research or code generation (plus document summaries and internal notes) where public voice cadence does not matter.
- **Add `grai` ($79/yr) on top of Claude if:** you publish under your own name (or write for clients) and want a deterministic browser gate that measures your sentence variance (`CV >= 0.32`), highlights structural AI tells, and repairs flagged spans before you publish.
- **Checkout:** [Solo Offline Edition ($79/yr)](https://grai.page/#tiers) · [Agency Verification Protocol ($99/mo or $790/yr)](https://grai.page/#tiers)
