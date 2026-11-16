# grai vs. Ghostbase: $790/yr for 10 Client Voices vs. $948/yr per Space (2026)

> **Last verified against public pricing and vendor documentation:** 2026-11-15. Ghostbase per-space prices checked 2026-10-23.
> **Canonical URL:** https://grai.page/vs/ghostbase

**Direct Answer:** Ghostbase is a cloud writing workspace for ghostwriters. It rents one space per client at $99 per space per month, or $79 per space per month billed annually ($948 per space per year). Each space holds a Digital Brain built from notes, documents, recordings and past work, plus a Voice ID and a custom writing model. `grai` ($79/yr Solo, or $99/mo or $790/yr Agency) is an approximately 630 KB local HTML5 workbench. It measures 5 to 20 of your own posts, audits every draft against 8 deterministic structural rules plus a `CV >= 0.32` burstiness floor, and keeps up to 10 client profiles with A4 SHA-256 Dossiers and ECDSA P-256 verification links.

### TL;DR Comparison

| Option | Best For | Starting Price | Key Difference |
| :--- | :--- | :--- | :--- |
| **`grai`** (Solo) | One founder or writer who wants a local Voice DNA profile and a deterministic cadence gate before publishing. | **$79/yr** | about 630 KB local HTML5 file. 8 structural rules + `CV >= 0.32` floor + exact span highlights + targeted repair. |
| **`grai`** (Agency) | Ghostwriters and boutique studios checking up to 10 client voices with a printable proof artifact. | **$99/mo or $790/yr** | Up to 10 isolated client profiles + A4 SHA-256 Client Voice DNA Dossiers + public ECDSA P-256 verification links. |
| **Ghostbase** | Ghostwriters who need a cloud Digital Brain that ingests documents and recordings for each client. | **$99/space/mo** monthly, or **$79/space/mo** annual ($948/space/year) | Per-space cloud workspace with a Voice ID, a custom writing model and a Digital Brain per client. |

---

## 1. Two Different Jobs: Renting a Cloud Brain vs. Owning a Voice Gate

Ghostbase starts with ingestion. You import notes, documents, recordings, ideas and past work into a Digital Brain, and the workspace writes LinkedIn posts, newsletters, emails and articles from that material. One space per client means one custom model, one Voice ID and one memory. That is real work a browser file cannot do.

`grai` starts with measurement. You paste 5 to 20 posts the client actually wrote. It extracts a quantitative Voice DNA profile: average sentence length, sentence-length variance, openings, endings, signature words. Every later draft is checked against 8 structural rules plus a burstiness floor at `CV >= 0.32`, and the exact failing span is highlighted in the text. The check runs in one file, in the browser. No account. No server.

The purchase decision is not "which tool writes better". It is "do you need a cloud knowledge base, or do you need a checkable voice record you can hand to a client". Ghostbase sells the first. `grai` sells the second.

---

## 2. Where Ghostbase Wins vs. Where grai Wins

### Where Ghostbase Wins

- **Document and recording ingestion:** the Digital Brain accepts notes, documents, recordings, ideas and past work. `grai` requires pasted text samples.
- **Per-client custom model and memory:** each space carries its own Voice ID and Digital Brain, so a client's material does not share a workspace with another client's material.
- **One workspace for several formats:** LinkedIn posts, newsletters, emails and articles are generated in the same cloud editor with writing frameworks.
- **Trial access:** 7 days on monthly billing and 14 days on annual billing, before the per-space charge starts.

### Where grai Wins

- **Annual price ($790/yr vs. $948/yr for one space):** the Agency Verification Protocol covers up to 10 isolated client profiles for $790/yr. One Ghostbase space costs $948/yr on annual billing. Five spaces cost $4,740/yr.
- **Deterministic 8-rule + `CV >= 0.32` gate:** the same input returns the same result. It highlights the exact span that fails and offers a targeted repair, without asking a model to vote on whether the draft sounds human.
- **Local ownership:** the shipped `grai.html` runs with `connect-src 'none'`. Profiles and drafts live in browser `localStorage` and portable `.grai` files, not in a vendor workspace.
- **Client proof:** the Agency edition issues printable A4 SHA-256 Client Voice DNA Dossiers and public ECDSA P-256 verification links at `grai.page/verify/:hash`.
- **No LinkedIn OAuth:** `grai` never holds a session token and never schedules or publishes. There is no automation surface to restrict.

---

## 3. Side-by-Side Technical and Commercial Matrix

| Criterion | grai (Solo $79/yr / Agency $99/mo or $790/yr) | Ghostbase ($99/space/mo monthly, $79/space/mo annual) |
| :--- | :--- | :--- |
| Pricing model | **$79/yr** (Solo) or **$99/mo or $790/yr** (Agency) | **$99 per space per month** monthly, or **$79 per space per month** annual ($948 per space per year) |
| Billing unit | One licence, up to 10 client profiles on Agency | One active space per client (a space can also be you or an organization) |
| Voice capture inputs | 5 to 20 pasted posts written by the client | Notes, documents, recordings, ideas and past work imported into a Digital Brain |
| Cadence verification | Deterministic 8 regex rules + `CV >= 0.32` floor + exact span highlights + targeted repair | No deterministic sentence-rhythm gate |
| Where profiles live | Browser `localStorage` and portable `.grai` files on disk | Hosted inside the Ghostbase cloud workspace |
| Client proof | A4 SHA-256 Client Voice DNA Dossier + public ECDSA P-256 receipts at `grai.page/verify/:hash` | No deterministic cadence record or public verification link stated |
| LinkedIn connection | None required. `grai` never schedules or publishes | Writing workspace. It is not a scheduler either |
| What happens if you stop paying | You keep `grai.html` and your `.grai` voice files permanently | Access to the cloud workspace and its Digital Brain stops |

---

## 4. 12-Month and 24-Month Total Cost Comparison

The table treats one Ghostbase space as one client, which is the common ghostwriting setup. A space can also be you or an organization. Prices checked 2026-11-15; Ghostbase per-space prices from its public billing handbook, checked 2026-10-23.

| Setup | Month 1 | 12-Month Total | 24-Month Total | What Is Included |
| :--- | :--- | :--- | :--- | :--- |
| **Ghostbase, 1 space** (monthly billing) | $99 | $1,188 | $2,376 | One client space, Digital Brain, Voice ID, 7-day trial |
| **Ghostbase, 1 space** (annual billing) | $79 | $948 | $1,896 | One client space, Digital Brain, Voice ID, 14-day trial |
| **Ghostbase, 5 client spaces** (monthly billing) | $495 | $5,940 | $11,880 | Five client spaces with separate Digital Brains and Voice IDs |
| **Ghostbase, 5 client spaces** (annual billing) | $395 | $4,740 | $9,480 | Five client spaces with separate Digital Brains and Voice IDs |
| **`grai` Agency Verification Protocol** (annual) | $790 | $790 | $1,580 | Up to 10 client profiles + A4 SHA-256 Dossiers + live ECDSA seals at `/verify/:hash` |
| **`grai` Agency Verification Protocol** (monthly) | $99 | $1,188 | $2,376 | Same Agency features, cancellable monthly |
| **`grai` Solo Offline Edition** (annual) | $79 | $79 | $158 | One voice profile + 8-rule Cadence Gate + `grai-mcp` |

---

## 5. Privacy and Data Flow Boundary

- **Shipped Pre-Built Kit (`grai.html`):** Ships with a Content Security Policy (`default-src 'none'; style-src 'unsafe-inline'; font-src data:; img-src data:; script-src 'unsafe-inline'; connect-src 'none'; object-src 'none'; base-uri 'none'`) that allows inline styles and inline scripts (plus `data:` fonts and images) while blocking direct API connections (`connect-src 'none'`) from the page. Out of the box, it runs in Copy-Paste mode.
- **Browser Storage:** Voice profiles, samples and drafts are stored in your browser's `localStorage` when available. If your browser blocks `localStorage` on local `file://` pages, `grai` falls back to in-memory session storage, which lasts until the tab closes. Export a `.grai` backup file to keep the profile permanently on disk.
- **When data leaves your machine:** only when you paste a prompt into Claude, ChatGPT or Gemini in Copy-Paste mode, when you run a custom source build with BYOK and send a prompt to your chosen provider, or when you export and share a `.grai` file or PDF Dossier yourself. Ghostbase runs the Digital Brain, Voice ID and drafts inside its cloud workspace by design.
- **Language scope:** voice extraction works in any language you paste. The 8 deterministic structural rules are tuned for English. Test a non-English draft before you rely on the rule count.

---

## 6. Verdict: Which Should You Choose?

**Choose Ghostbase ($99 per space per month, $79 annual) if:** the job is ingestion and cloud collaboration. You want a Digital Brain to absorb documents and recordings, one space per client, and a workspace that writes several formats from that material. The per-space rent is the price of that convenience.

**Choose grai ($79/yr Solo, or $99/mo or $790/yr Agency) if:** the job is voice fidelity and proof. You want a deterministic 8-rule + `CV >= 0.32` gate, exact span repairs, portable `.grai` profiles, and up to 10 client Dossiers with public ECDSA verification for one flat annual price.

**Use both if:** Ghostbase handles research, ingestion and the first draft, and `grai` runs the final cadence check before anything is published. The two do not overlap.

**Do not buy grai if:** you need automatic document or recording ingestion, a cloud workspace your clients log into, or a scheduler. Ghostbase is the better buy for those jobs.

---

## Frequently Asked Questions

### How does Ghostbase pricing compare with grai?

Ghostbase costs $99 per space per month on monthly billing, or $79 per space per month billed annually ($948 per space per year). A space can be you, one client, or an organization. grai Solo is $79 per year, and the Agency Verification Protocol is $99 per month or $790 per year for up to 10 isolated client profiles.

### Does Ghostbase include a deterministic cadence checker?

No. Ghostbase generates text inside its cloud workspace with a Digital Brain, Voice ID and a custom writing model. grai runs 8 structural regex rules plus a `CV >= 0.32` burstiness floor in the browser, highlights the exact spans that fail, and offers targeted repair.

### Can I use Ghostbase for client research and grai for the final check?

Yes. Use Ghostbase to ingest documents and recordings and to draft in the client workspace, then paste the draft into grai or the free scorer at https://grai.page/#test. grai returns the measured cadence and the failing spans. Neither tool publishes to LinkedIn for you.

**Checkout:** [Solo Offline Edition ($79/yr)](https://grai.page/#tiers) | [Agency Verification Protocol ($99/mo or $790/yr)](https://grai.page/#tiers)
