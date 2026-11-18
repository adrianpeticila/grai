# grai for LinkedIn Ghostwriters and Boutique Agencies (2026)

> **Last verified against public pricing and vendor documentation:** 2026-10-29
> **Canonical URL:** https://grai.page/vs/linkedin-ghostwriters

**Direct Answer:** A boutique LinkedIn ghostwriter usually onboards a client with a call, a questionnaire and two weeks of voice calibration. `grai` Agency ($99/mo or $790/yr) compresses the calibration into one sitting: 5 to 20 client posts in, a measured Voice DNA profile out, and an A4 Client Voice DNA Dossier signed with a SHA-256 hash the client can verify. A retainer agency charges $3,000 per month for the same artifact wrapped in a team.

### TL;DR Comparison

| Option | Best For | Starting Price | Key Difference |
| :--- | :--- | :--- | :--- |
| **`grai`** (Agency $99/mo or $790/yr) | A solo ghostwriter or a small studio that needs fast onboarding and a client-facing proof artifact. | **$99/mo or $790/yr** (up to 10 client profiles) | Local workbench, measured Voice DNA per client, A4 SHA-256 Dossier, deterministic gate. The writing stays with you. |
| **Ghostwriting agency** | Companies that want strategy, a team and reporting on retainer. | **About $3,000/month** (market rate) | A team owns the channel and the calendar. The voice calibration is usually a document, not a measured profile you can verify. |

---

## 1. The Onboarding Problem

Voice calibration is the expensive part of ghostwriting. A client sends old posts, takes a call, answers a questionnaire, and waits. Two weeks pass before the first draft, and the client has no artifact to hold while they wait.

The agency version is not faster. It is a junior writer plus an editor plus a project manager, and the $3,000 monthly retainer pays for that layer. The calibration document lives in a shared drive and nobody outside the team can verify it.

`grai` replaces the document with a measurement. The client pastes 5 to 20 posts, the profiler extracts cadence, and the first gated draft proves the profile works. That is the demonstration a client can see in the first meeting.

---

## 2. Ten Minutes, One Dossier

The Agency flow has four steps. Open a client profile, paste their last 5 to 20 posts, run the profiler, and print the A4 Client Voice DNA Dossier. The dossier carries the measured profile, the 8-rule result, the CV value, and a SHA-256 hash over the payload.

The hash matters. Anyone can edit a Google Doc after the fact. A dossier whose SHA-256 no longer matches its content is visibly altered, which turns a soft promise into a checkable claim.

Then the real work starts: you write in the client's voice, run each draft through the gate, and ship the ones that pass. grai does not write for you, and the dossier does not replace your judgement. It removes the two weeks of guessing.

---

## 3. The Unit Economics

An agency retainer at $3,000 per month is $36,000 per year. A boutique ghostwriter with the Agency Verification Protocol pays $99/mo or $790/yr, keeps the client relationship, and prices the writing instead of the coordination layer.

The comparison is not a like-for-like swap. An agency sells strategy, distribution and reporting alongside the writing. If the client needs a team to own the channel, the retainer is the right product.

But a large share of founder clients need one thing: posts that sound like them, delivered on time. For that job, $99/mo or $790/yr against $36,000 per year is not a close call, and the dossier is the artifact the client keeps.

---

## 4. Side-by-Side Technical and Commercial Matrix

| Criterion | grai Agency Verification Protocol ($99/mo or $790/yr) | Ghostwriting agency (about $3,000 per month) |
| :--- | :--- | :--- |
| Price model | **$99/mo or $790/yr**, annual or monthly billing | **About $3,000 per month**, so $36,000 per year |
| Onboarding | One sitting: 5 to 20 posts, a profiled voice, a first gated draft | Calls, questionnaires and a calibration document over one to two weeks |
| Proof artifact | A4 Client Voice DNA Dossier with a SHA-256 hash the client can verify | A shared document, usually not hashed |
| Who writes | The ghostwriter, with every draft gated locally | A junior writer, an editor and a project manager |
| Client profiles | up to 10 isolated profiles in one local workbench | One per account, stored in the agency workspace |
| Where client text lives | On the ghostwriter's machine, no upload | In the agency cloud workspace |

---

## 5. 12-Month and 24-Month Total Cost Comparison

| Setup | Month 1 | 12-Month Total | 24-Month Total | What Is Included |
| :--- | :--- | :--- | :--- | :--- |
| **Full agency retainer** | $3,000 | $36,000 | $72,000 | Writing, strategy and distribution from a team |
| **Mid-size boutique retainer** | $1,500 | $18,000 | $36,000 | Writing and scheduling with a smaller team |
| **`grai` Agency Verification Protocol** (annual) | $790 | $790 | $1,580 | up to 10 client profiles, A4 SHA-256 Dossiers, local gate |
| **`grai` Solo Offline Edition** (solo, annual) | $79 | $79 | $158 | One personal voice profile and the full gate |

---

## 6. Privacy and Data Flow Boundary

- **Shipped Pre-Built Kit (`grai.html`):** Ships with a Content Security Policy (`default-src 'none'; style-src 'unsafe-inline'; font-src data:; img-src data:; script-src 'unsafe-inline'; connect-src 'none'; object-src 'none'; base-uri 'none'`) that allows inline styles and inline scripts (plus `data:` fonts and images) while blocking direct API connections (`connect-src 'none'`) from the page. Out of the box, it runs in Copy-Paste mode.
- **Browser Storage:** Voice profiles and writing samples (along with drafts) are stored in your browser's `localStorage` when available. If your browser settings or private-browsing mode block `localStorage` on local `file://` pages, `grai` falls back to in-memory session storage (`memStorage`), which lasts until the tab closes. Export a `.grai` backup file to save your profiles permanently to disk.
- **When client data leaves your machine:** only when you paste a prompt into a model in Copy-Paste mode, when a custom source build calls a BYOK provider, or when you choose to send a dossier to the client. The profiles themselves stay in your browser, which is the point for a ghostwriter holding several client voices.

---

## 7. Verdict: Which Should You Choose?

**Choose an agency retainer (about $3,000/month) if:** the client needs strategy, distribution and a team that owns the channel, with reporting attached. The writing is one line item in a larger service.

**Choose grai Agency Verification Protocol ($99/mo or $790/yr) if:** you already write well and the bottleneck is calibration and proof. One sitting to a measured profile, and a dossier that survives scrutiny.

**Run both models if:** you keep a retainer for strategy and use grai to onboard the writing layer in a single meeting, which takes ten minutes. The dossier becomes the artifact the client shows internally.

---

## Frequently Asked Questions

### Does grai replace a ghostwriter?

No. It measures the client's voice and blocks drafts that break the measured cadence. The writing, the judgement and the relationship stay with the ghostwriter.

### What is the SHA-256 hash on the dossier for?

It fingerprints the profile and the audit payload. If the dossier is edited after delivery, the hash no longer matches, so a client can verify the artifact was not altered.

### How long does onboarding actually take?

One sitting. The client supplies 5 to 20 posts, the profiler extracts the profile, and the first gated draft is ready in the same meeting. The two-week calibration cycle is what disappears.

**Checkout:** [Solo Offline Edition ($79/yr)](https://grai.page/#tiers) | [Agency Verification Protocol ($99/mo or $790/yr)](https://grai.page/#tiers)
