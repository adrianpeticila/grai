# grai for Substack and Beehiiv Newsletter Writers (2026)

> **Last verified against public pricing and vendor documentation:** 2026-10-29
> **Canonical URL:** https://grai.page/vs/substack-writers

**Direct Answer:** A newsletter lives or dies on one thing: whether the essay sounds like the person who wrote it. `grai` ($79/yr, Solo Offline Edition, or $99/mo or $790/yr Agency) measures your published cadence, flags the drafts that flatten into the same register every AI newsletter uses, and enforces a `CV >= 0.32` floor before you hit send.

### TL;DR Comparison

| Option | Best For | Starting Price | Key Difference |
| :--- | :--- | :--- | :--- |
| **`grai`** (Solo) | Essay writers who publish weekly and need the cadence to stay jagged on draft eleven. | **$79/yr** (AI model/API usage separate if used) | about 630 KB local workbench. Voice DNA from 5 to 20 essays, 8 rules, `CV >= 0.32` floor. No account. |
| **Doing nothing** | Writers who assume the voice survives without a check. | **$0** | The cadence drifts toward the model default, one edited paragraph at a time. |

---

## 1. Why a Newsletter Voice Flattens

A weekly essay is a rhythm more than a topic. The first issue has a jagged cadence because it was written in one sitting by one person. By issue ten, the drafting has moved through a model, an editor and a rewrite, and the sentence lengths have quietly converged.

The vocabulary survives that drift. The structure does not. A writer can cut every banned word and still publish a paragraph where every sentence is fourteen words long, because that is what a model produces when nobody measures it.

`grai` measures it. It extracts a profile from 5 to 20 of your published essays, then audits each draft against eight structural rules and the burstiness floor before the newsletter goes out.

---

## 2. The Affiliate Loop for Newsletter Writers

Newsletter writers recommend tools constantly, usually for free. The grai partner program pays 40% across all 6 Stripe tiers.

Every eligible Stripe sale pays 40%: $7.60 on the $19 Starter Pass, $31.60 on the $79/yr Solo, $39.60 per $99/mo Agency cycle, $316 on the $790/yr Agency Annual, $380 on the $950 DFY. The footer line is one sentence, and the link can carry your partner code instead of the plain checkout URL.

- **Partner link:** https://grai.page/affiliate
- **Solo checkout:** https://grai.page/#tiers
- **Agency checkout:** https://grai.page/#tiers

---

## 3. Side-by-Side Technical and Commercial Matrix

| Criterion | grai (Solo $79/yr / Agency $99/mo or $790/yr) | No cadence check |
| :--- | :--- | :--- |
| Price | **$79/yr** (Solo) or **$99/mo or $790/yr** (Agency) | **$0**, plus the slow cost of a drifting voice |
| What it measures | Cadence profile from 5 to 20 published essays | Nothing, until a reader notices |
| Gate | 8 rules and `CV >= 0.32`, with flagged spans | None |
| Revenue side | **40% affiliate** across all 6 Stripe tiers | None |
| Where the text lives | In the browser, no upload in the shipped kit | Depends on the tools in the draft loop |
| What happens if you stop paying | You keep `grai.html` and your `.grai` files | The drift continues |

---

## 4. 12-Month and 24-Month Total Cost Comparison

| Setup | Month 1 | 12-Month Total | 24-Month Total | What Is Included |
| :--- | :--- | :--- | :--- | :--- |
| **`grai` Solo** (annual) | $79 | $79 | $158 | One voice profile, the 8-rule gate, local workbench |
| **`grai` Agency Verification Protocol** (annual) | $790 | $790 | $1,580 | up to 10 client or pen-name profiles, A4 SHA-256 Dossiers |
| **Two Solo referrals** (40% each) | - | -$63.20 | -$63.20 | 40% commission on two $79/yr Solo sales |
| **Solo Offline Edition net after two Solo referrals** | $79 | $15.80 | $15.80 | Net cost after $63.20 in Stripe commission |

---

## 5. Privacy and Data Flow Boundary

- **Shipped Pre-Built Kit (`grai.html`):** Ships with a Content Security Policy (`default-src 'none'; style-src 'unsafe-inline'; font-src data:; img-src data:; script-src 'unsafe-inline'; connect-src 'none'; object-src 'none'; base-uri 'none'`) that allows inline styles and inline scripts (plus `data:` fonts and images) while blocking direct API connections (`connect-src 'none'`) from the page. Out of the box, it runs in Copy-Paste mode.
- **Browser Storage:** Voice profiles and writing samples (along with drafts) are stored in your browser's `localStorage` when available. If your browser settings or private-browsing mode block `localStorage` on local `file://` pages, `grai` falls back to in-memory session storage (`memStorage`), which lasts until the tab closes. Export a `.grai` backup file to save your profiles permanently to disk.
- **When data leaves your machine:** only when you paste a prompt into a model in Copy-Paste mode, when a custom source build calls a BYOK provider, or when you send a draft to an editor yourself. A newsletter draft is often unpublished client material, so the local default matters.

---

## 6. Verdict: Which Should You Choose?

**Choose grai ($79/yr) if:** you publish an essay every week and the draft is starting to sound like the tool that helped you write it.

**Choose the Agency Verification Protocol ($99/mo or $790/yr) if:** you write under more than one name, or you edit other people's newsletters and need separate profiles.

**Use the partner program either way.** A footer line with your partner link turns a tool you already bought into a small revenue stream at 40% on eligible Stripe sales.

---

## Frequently Asked Questions

### Does grai write my newsletter for me?

No. It measures the cadence of what you wrote and flags the spans that broke it. The essay stays yours, which is the point for a publication built on a personal voice.

### How does the 40% affiliate program work for a newsletter?

You register at the partner link, get a `?ref=<handle>` link, and earn 40% on each eligible Stripe sale it drives.

### Does it work with drafts written in Google Docs?

Yes. Paste the draft into the local bench and run the audit. The gate reads text, not a file format, and the shipped kit keeps it in the browser.

**Checkout:** [Solo Offline Edition ($79/yr)](https://grai.page/#tiers) | [Agency Verification Protocol ($99/mo or $790/yr)](https://grai.page/#tiers)
