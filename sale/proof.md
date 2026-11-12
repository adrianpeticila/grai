# grai Public Verification Registry: Live Cryptographic Cadence Receipts (2026)

> **Registry state verified:** 2026-11-12
> **Canonical URL:** https://grai.page/proof

**Why no draft text appears on this page:** Every receipt at `grai.page/verify/:hash` stores the SHA-256 commitment of the draft, the measured cadence score, the sentence-length burstiness (`CV`), the rule pass count, and the ECDSA P-256 signature status. Zero client prose is stored on our servers. That privacy boundary is the product.

---

## 1. The Three Public Reference Records

| Record | Client Reference | Verdict & Score | Metrics | Signature Status | Live Receipt URL |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **01. Plain Human Cadence** | Paul Graham, Write Simply (reference sample) | **VERIFIED** (`100/100`) | `8 of 8` rules passed, `CV >= 0.32` | Signed ECDSA P-256 (`grai-seal-1`) | https://grai.page/verify/4a4cb85cd0cb46b46959e69e6ab39c99da4da5f3afae4e6258e320d1dbe378be |
| **02. Rejected AI Template** | Generic AI LinkedIn Template | **FAILED_CADENCE** (`34/100`) | `5 of 8` rules passed, `CV 0.14` (below `0.32` floor) | `not_issued_failed_gate` (unsigned by rule) | https://grai.page/verify/bae6d7849c6cef2f8a3846f078147620fd3e01eb6edbf602ffe3d4913af49c30 |
| **03. Executive Calibrated Draft** | Executive Calibrated Draft, Agency Protocol | **VERIFIED** (`100/100`) | `8 of 8` rules passed, `CV >= 0.32` | Signed ECDSA P-256 (`grai-seal-1`) | https://grai.page/verify/398ec41412a09deaa39c766e48e4176355d95fc9f6a5f0b5b26b3b51e6fc01f2 |

> **Note:** Record 01 is a synthetic reference sample written in a short declarative register, not a direct quotation from Paul Graham.

---

## 2. How Zero-Prose Verification Works

When a ghostwriting studio or executive team seals a draft under the Agency Verification Protocol, the worker audits the text in volatile memory against the eight structural rules and the `CV >= 0.32` sentence-length burstiness floor.

If the draft passes, the server signs the metadata commitment with ECDSA P-256 and writes only the SHA-256 hash, the score, the CV, the rule count, and the agency reference to the registry. If a draft fails the gate, the server refuses to issue a cryptographic signature (`not_issued_failed_gate`). In both cases, the client prose is discarded immediately after the hash is computed.

**Checkout:** [Solo Offline Edition ($79/yr)](https://buy.stripe.com/3cIaERgwM9hLbuF33Vds400) | [Agency Verification Protocol ($99/mo)](https://buy.stripe.com/3cI28lbcs51v2Y9bArds401) | [Agency Annual ($790/yr)](https://buy.stripe.com/dRmfZb2FWalP42d5c3ds402)
