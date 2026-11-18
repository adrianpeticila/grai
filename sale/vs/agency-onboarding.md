# grai vs. Manual Client Voice Onboarding Docs (2026)

> **Last verified against public pricing and vendor documentation:** 2026-10-29
> **Canonical URL:** https://grai.page/vs/agency-onboarding

**Direct Answer:** A boutique agency usually onboards a new client with a style guide: a Google Doc assembled over two or three weeks of calls, sample posts and revisions. `grai` Agency ($99/mo or $790/yr) replaces the document with a measurement. The client supplies 5 to 20 posts, the profiler extracts a Voice DNA profile, and the A4 dossier is signed with a SHA-256 hash the client can verify.

### TL;DR Comparison

| Option | Best For | Starting Price | Key Difference |
| :--- | :--- | :--- | :--- |
| **`grai`** (Agency $99/mo or $790/yr) | Solo ghostwriters and studios of one to five people who need fast, verifiable client onboarding. | **$99/mo or $790/yr** (up to 10 client profiles) | Ten-minute calibration, a measured profile per client, an A4 SHA-256 dossier and a deterministic gate. The writing stays with you. |
| **Manual onboarding doc** | Agencies that sell strategy and a long discovery process as part of the retainer. | **Two to three weeks of billable time** | A written guide of rules and examples. Useful, but unmeasured and easy to drift from once the writer changes. |

---

## 1. The Three-Week Document

The standard onboarding artifact is a document. A strategist interviews the client, collects samples, writes a tone section, adds do and do not examples, and sends it for approval. Two or three weeks pass before the first draft, and the client pays for that time.

The document has a second problem. It describes a voice in adjectives, and adjectives do not survive a handover. A new writer reads confident, warm and direct, produces something plausible, and the client says it does not sound like me without being able to say why.

`grai` turns the adjectives into numbers. The profile records sentence-length distribution, the burstiness coefficient and the eight structural habits the audit can verify. A new writer can run a draft against it in seconds instead of guessing from a paragraph of description.

---

## 2. The Ten-Minute Calibration

The onboarding session has four steps. Open a client profile, paste 5 to 20 of their posts, run the profiler, and print the A4 Client Voice DNA Dossier. The dossier holds the measured profile, the eight-rule result, the CV value and a SHA-256 hash over the payload.

The hash is the part a document cannot offer. Anyone can edit a Google Doc after delivery, and nobody can prove what changed. A dossier whose hash no longer matches its content is visibly altered, so the client holds a claim that can be checked.

Then the work continues as it did before, except each draft passes through the gate before it reaches the client. grai does not replace the ghostwriter or the strategist. It removes the three weeks of guessing and the drift after a handover.

---

## 3. The Economics of the Switch

A three-week onboarding at an agency day rate is a real cost, and it is paid before the first post exists. The Agency Verification Protocol is $99/mo or $790/yr and covers up to 10 client profiles, so the calibration layer stops being a project and becomes a step in the first meeting.

The comparison is not a like-for-like swap. An agency sells strategy, distribution and a team, and a document is part of that package. If the client is buying the strategy layer, keep the document.

But when the deliverable is posts that sound like the founder, the measurement is the stronger artifact. It is faster to produce, harder to fake and cheaper to repeat for the next client.

---

## 4. Side-by-Side Technical and Commercial Matrix

| Criterion | grai Agency Verification Protocol ($99/mo or $790/yr) | Manual onboarding doc (two to three weeks) |
| :--- | :--- | :--- |
| Time to first draft | One sitting, about ten minutes | Two to three weeks of calls and revisions |
| Artifact | A4 Client Voice DNA Dossier with a SHA-256 hash | A Google Doc with adjectives and examples |
| Verifiable | Yes, the hash breaks if the dossier is edited | No, the document can change silently |
| Per-client cost | **$99/mo or $790/yr** for up to 10 clients | Billable hours before the first post |
| Handover | A new writer runs drafts against the profile | A new writer interprets the document |
| Who writes | The ghostwriter, with every draft gated locally | The ghostwriter, without a deterministic check |

---

## 5. 12-Month and 24-Month Total Cost Comparison

| Setup | Month 1 | 12-Month Total | 24-Month Total | What Is Included |
| :--- | :--- | :--- | :--- | :--- |
| **Manual onboarding project** | Two to three weeks of billable time | Same | Same per new client | A style document and a calibration call |
| **`grai` Agency Verification Protocol** (annual) | $790 | $790 | $1,580 | up to 10 client profiles, A4 SHA-256 Dossiers, local gate |
| **`grai` Solo Offline Edition** (solo, annual) | $79 | $79 | $158 | One personal voice profile and the full gate |
| **Agency Verification Protocol + one replacement client** | $790 | $790 | $1,580 | The up to 10 profiles cover the next 24 clients at no extra cost |

---

## 6. Privacy and Data Flow Boundary

- **Shipped Pre-Built Kit (`grai.html`):** Ships with a Content Security Policy (`default-src 'none'; style-src 'unsafe-inline'; font-src data:; img-src data:; script-src 'unsafe-inline'; connect-src 'none'; object-src 'none'; base-uri 'none'`) that allows inline styles and inline scripts (plus `data:` fonts and images) while blocking direct API connections (`connect-src 'none'`) from the page. Out of the box, it runs in Copy-Paste mode.
- **Browser Storage:** Voice profiles and writing samples (along with drafts) are stored in your browser's `localStorage` when available. If your browser settings or private-browsing mode block `localStorage` on local `file://` pages, `grai` falls back to in-memory session storage (`memStorage`), which lasts until the tab closes. Export a `.grai` backup file to save your profiles permanently to disk.
- **When client data leaves your machine:** only when you paste a prompt into a model in Copy-Paste mode, when a custom source build calls a BYOK provider, or when you send the dossier to the client yourself. The profiles stay in your browser, which matters when you hold several client voices.

---

## 7. Verdict: Which Should You Choose?

**Keep the manual doc if:** the client is buying strategy, workshops and a discovery process. The document is part of a larger engagement and the three weeks are part of what they pay for.

**Switch to grai Agency Verification Protocol ($99/mo or $790/yr) if:** the deliverable is posts in the founder's voice and the onboarding is overhead. Ten minutes and a verifiable dossier beat three weeks and a document.

**Run both if:** you sell the strategy engagement and use grai to deliver the writing layer. The dossier becomes the artifact the client forwards internally.

---

## Frequently Asked Questions

### Does grai write the posts for the agency?

No. It measures the client's voice and blocks drafts that break the measured cadence. The writing, the judgement and the client relationship stay with the ghostwriter.

### What does the A4 dossier contain?

The measured Voice DNA profile, the eight-rule audit result, the CV value with the 0.32 floor, the sample size and a SHA-256 hash over the profile and audit payload.

### Can one licence cover several clients?

The Agency Verification Protocol is $99/mo or $790/yr and includes up to 10 isolated client profiles, so a studio can onboard its book of clients without a per-seat or monthly fee.

**Checkout:** [Solo Offline Edition ($79/yr)](https://grai.page/#tiers) | [Agency Verification Protocol ($99/mo or $790/yr)](https://grai.page/#tiers)
