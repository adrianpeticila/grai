# grai for Executive PR and Thought Leadership Agencies (2026)

> **Last verified against public pricing and vendor documentation:** 2026-10-29
> **Canonical URL:** https://grai.page/vs/pr-agencies

**Direct Answer:** A PR agency sells one scarce asset: a C-suite voice that sounds like the executive and not like the agency. `grai` Agency ($99/mo or $790/yr) calibrates up to 10 executive voices in local browser storage and .grai files. It enforces the same 8 rules and `CV >= 0.32` floor on every draft, then prints an A4 Client Voice DNA Dossier signed with a SHA-256 hash for each executive profile.

### TL;DR Comparison

| Option | Best For | Starting Price | Key Difference |
| :--- | :--- | :--- | :--- |
| **`grai`** (Agency $99/mo or $790/yr) | Comms teams that hold several executive voices and must prove the writing is bespoke. | **$99/mo or $790/yr** (up to 10 profiles) | Local workbench, air-gapped by default, per-executive profiles and printable SHA-256 A4 Dossiers. |
| **Manual style guides** | Agencies that sell a long discovery process as part of the retainer. | **Weeks of billable time** | A document of adjectives that drifts the moment a new writer takes over. |

---

## 1. The Executive Voice Problem

An executive's LinkedIn presence is now a board-level asset, which means the writing has to survive legal review, a comms lead and a ghostwriter without losing the person. That is a hard constraint, and a style guide of adjectives does not satisfy it.

PR teams also hold sensitive material. An unpublished earnings note or a crisis statement should not sit in a cloud writing tool by default. `grai` runs in the browser with `connect-src 'none'` in the shipped kit, so the draft stays on the machine.

The Agency Verification Protocol adds the two things a comms team actually needs: separate profiles per executive, and a one-page A4 dossier that proves the voice was measured rather than guessed.

---

## 2. Where the Agency Verification Protocol Fits

### Before the draft

- **Profile the executive:** 5 to 20 published posts in, a measured cadence profile out.
- **Lock the target:** sentence-length distribution and the `CV >= 0.32` floor are explicit.
- **Keep it local:** the profile sits in local browser storage and .grai files on the agency machine.

### After the draft

- **Gate every version:** 8 syntactic rules and the rhythm floor, with the exact failed spans.
- **Print the dossier:** an A4 Client Voice DNA Dossier with a SHA-256 hash the client can verify.
- **Repeat per executive:** up to 10 isolated profiles in one licence.

---

## 3. Side-by-Side Technical and Commercial Matrix

| Criterion | grai Agency Verification Protocol ($99/mo or $790/yr) | Cloud writing tool plus a style guide |
| :--- | :--- | :--- |
| Price model | **$99/mo or $790/yr** for up to 10 executive profiles | Per-seat monthly fees, plus the discovery project |
| Voice proof | A4 Dossier with a SHA-256 hash per executive | A document that can change without a trace |
| Data boundary | Local by default, `connect-src 'none'` in the shipped kit | Drafts stored in a vendor cloud |
| Gate | 8 rules and `CV >= 0.32`, deterministic | A model opinion, if anything |
| Capacity | up to 10 isolated profiles in one local workbench | One workspace per seat |
| What happens if you stop paying | You keep `grai.html` and the `.grai` files | Access stops |

---

## 4. 12-Month and 24-Month Total Cost Comparison

| Setup | Month 1 | 12-Month Total | 24-Month Total | What Is Included |
| :--- | :--- | :--- | :--- | :--- |
| **Cloud writing seats, five people** | $75 | $900 | $1,800 | Shared workspace and a monthly subscription |
| **`grai` Agency Verification Protocol** (annual) | $790 | $790 | $1,580 | up to 10 executive profiles, local gate and A4 Dossiers |
| **`grai` Solo Offline Edition** (annual, solo) | $79 | $79 | $158 | One profile and the full gate |

---

## 5. Privacy and Data Flow Boundary

- **Shipped Pre-Built Kit (`grai.html`):** Ships with a Content Security Policy (`default-src 'none'; style-src 'unsafe-inline'; font-src data:; img-src data:; script-src 'unsafe-inline'; connect-src 'none'; object-src 'none'; base-uri 'none'`) that allows inline styles and inline scripts (plus `data:` fonts and images) while blocking direct API connections (`connect-src 'none'`) from the page. Out of the box, it runs in Copy-Paste mode.
- **Browser Storage:** Voice profiles and writing samples (along with drafts) are stored in your browser's `localStorage` when available. If your browser settings or private-browsing mode block `localStorage` on local `file://` pages, `grai` falls back to in-memory session storage (`memStorage`), which lasts until the tab closes. Export a `.grai` backup file to save your profiles permanently to disk.
- **Why this matters for PR:** unpublished executive statements and crisis drafts are often confidential. The shipped kit blocks network calls with `connect-src 'none'` and keeps every profile local, so the only time text leaves the machine is when a person chooses to send it.

---

## 6. Verdict: Which Should You Choose?

**Choose grai Agency Verification Protocol ($99/mo or $790/yr) if:** your team holds several executive voices and the client asks how the writing stays bespoke. The dossier answers that question with a measurement.

**Keep the cloud suite if:** the team needs collaborative editing and approval workflows. grai is not a document editor and does not try to be.

**Run both if:** the draft is written in the tools the team already uses, and grai is the gate plus the client-facing proof before it ships.

---

## Frequently Asked Questions

### Is grai suitable for confidential executive material?

The shipped kit runs with `connect-src 'none'`, so the draft and the profiles stay in the browser. A custom source build with a BYOK provider sends text only when a person triggers a model call.

### How many executives can one Agency licence hold?

Up to 10 isolated Client Voice Profiles in local browser storage and .grai files, each with its own A4 Client Voice DNA Dossier signed with a SHA-256 hash.

### Does it replace a PR agency?

No. It measures and protects the executive voice inside the agency's process. Strategy, media relations and the client relationship stay with the team.

**Checkout:** [Solo Offline Edition ($79/yr)](https://grai.page/#tiers) | [Agency Verification Protocol ($99/mo or $790/yr)](https://grai.page/#tiers)
