# Privacy

grai stores what you give it and nothing else. There is no account, no tracking pixel, and no per-visitor analytics. The site counts page views as daily totals per visitor category, described below.

## What stays on your device

| What | Where | Why |
|---|---|---|
| Your posts and your voice profile | this browser, in `localStorage` | so the tool works without a server |
| Your settings, language, selected tab | this browser, in `localStorage` | so the page remembers your setup |
| The files you export | your disk, as JSON or PNG | you asked for them |
| Local cadence scoring (`grai_score_draft`) | local environment / stdin | offline deterministic execution, zero network requests |

Deleting a voice in the page removes it from this browser. Clearing site data removes everything.

## What leaves your device, and when

1. **Copy and paste mode.** When you press a button, grai builds a prompt that contains your posts and your voice profile, copies it to your clipboard and opens an AI you picked. From that point the data follows that provider's terms. grai has no control over it and receives nothing.
2. **Direct mode.** If you connect a model, grai calls that provider directly from your browser using your own key. The prompt goes to that provider. grai never sees it, never stores it, and cannot log it, because there is no server.
3. **Fonts.** The page loads two typefaces from Google Fonts. That request reveals your IP address and page referrer to Google, and it happens on every load. This is a privacy exposure, not a feature.
4. **Agency Verification Protocol (`grai_issue_agency_seal`).** When an agency issues a live seal, the draft text, license key, and optional agency or client labels are sent over HTTPS to `grai.page/api/seal`. The server processes the text in volatile RAM to compute sentence cadence metrics and sign the certificate with ECDSA P-256. The draft text itself is discarded from memory immediately after signing and is never written to disk or database. Only the resulting signed record (SHA-256 draft hash, score metrics, client reference, and cryptographic signature) is saved to the Cloudflare KV verification registry.
5. **Seal verification (`grai_verify_seal`).** Verifying a seal sends the signed record JSON to `grai.page/api/verify` to validate signatures against the public keyring. No draft text is sent.

## Aggregate page counts

The site counts page views per day and per visitor category: human, AI agent, AI crawler, crawler or bot. Only daily totals are stored. No IP address, request path, header, user agent string or cookie is stored. Counts are kept for 90 days.

## Data retention and deletion

- **Local data:** Stored only in your browser (`localStorage`) or local machine. You control it directly.
- **Agency seal records:** Retained in the public verification registry to power the public receipt link. The license holder who issued the seal can request record deletion at any time by emailing `hello@grai.page` with their active license key and the seal hash.
- **Draft text:** Never stored on any server.

## What is never collected

No usage data, no error reports, no crash reports, no cookies, no fingerprinting, no identifiers.

## Model keys

If you connect an external model, the key stays in this browser only. It is never transmitted to us. It is never written into an exported voice file. Clear it from the settings panel before exporting or sharing any configuration file.

## Your responsibilities

Do not paste confidential material. grai transmits what you paste directly to your chosen third-party model. Client names, private figures, and non-disclosure obligations remain entirely your legal risk.

## Your rights

Everything grai holds stays on your device. You can export it or wipe it. Under GDPR you have full rights to access, correct, erase and port your data. Exporting yields everything in a single clean JSON document. For agency seal records stored in the KV verification registry, email `hello@grai.page` for permanent manual deletion.

Last updated: 2026-11-10.
