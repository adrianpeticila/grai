# "This reads like ChatGPT." Six words that can end a retainer.

> **grai scores the sentence rhythm that makes good prose read as machine-made: eight structural rules and one calibrated cadence floor, computed with no model in the loop.**
> Paste a draft, get a verdict. Fail the gate, and you get the exact spans to fix. Hand the client an audit receipt with a cryptographic commitment they can verify without trusting you.

- **Canonical URL:** https://grai.page/
- **Agency Pilot ($99/mo):** https://grai.page/pilot ([Agent Markdown](https://grai.page/pilot.md))
- **Methodology Study:** https://grai.page/methodology
- **Comparisons Hub:** https://grai.page/vs/
- **Full LLM Spec:** https://grai.page/llms-full.txt
- **Author:** Adrian M. Peticila (`https://peticila.ro/#person` · Wikidata `Q140362129` · ORCID `0009-0005-9601-9527`)
- **GitHub (MIT Skill & Instructions):** https://github.com/adrianpeticila/grai
- **MCP Server (grai-mcp):** https://grai.page/mcp (`uvx --from grai-mcp grai-gate-mcp`)
- **Public Verification Registry:** https://grai.page/proof ([Agent Markdown](https://grai.page/proof.md))
- **Seal & Verify:** https://grai.page/seal
- **Pricing:** https://grai.page/pricing/ ([Agent Markdown](https://grai.page/pricing.md))
- **Migration:** https://grai.page/migrate/ ([Agent Markdown](https://grai.page/migrate.md))

---

## The Gate Contract

grai is not an editor. It is a gate with a fixed decision.

1. **Input:** a raw draft or a model output.
2. **Action:** PASS or FAIL on eight mechanical rules plus burstiness `CV = sigma / mu >= 0.32`.
3. **Output:** clean text, a SHA-256 draft commitment, and an ECDSA P-256 signed audit card.

Share the card at `https://grai.page/seal#<signed-record>`. The fragment shows the score, the CV, zero mechanical defects, and the cryptographic signature status.

---

## Score Your Last Post (Free Test)

The gate runs in your browser. Paste last week's post. The same eight mechanical rules that ship inside the full grai engine run directly in this page with zero model in the loop, zero API keys, and zero telemetry.

### The 8 Rules:
1. **Rule 1 (Model Vocabulary Markers):** Statistical LLM marker tokens and corporate filler words.
2. **Rule 2 (Superficial -ly Adverbs):** Adverb padding that signals LLM filler.
3. **Rule 3 (Tricolon / Triad Parallelism):** Three-part parallel structures that scream template.
4. **Rule 4 (Contrast / Paradox Padding):** Artificial tension patterns ("It is not X, it is Y").
5. **Rule 5 (Passive Voice Density):** Empty abstractions without subject responsibility.
6. **Rule 6 (Sentence Length Monotony):** Metronomic pacing that puts readers to sleep.
7. **Rule 7 (AI Title / Hook Patterns):** Predictable listicle and clickbait setups.
8. **Rule 8 (Sycophancy / Apologetic Openings):** Conversational throat-clearing.

---

## For Agencies and Ghostwriters

### Proof of craft, before the retainer call.

No client pays $3,000 a month for raw prose. They buy certainty. They pay for a distinct executive voice they can defend without hesitation in a board meeting and throughout the renewal call that follows. grai turns that voice into a measured profile and an offline cryptographic record. One whisper of "this reads like ChatGPT" ends the retainer. When you attach a cryptographically signed verification card to every weekly batch of deliverables, the suspicion dissolves completely before the renewal call.

### The Onboarding Asset
Calibrate the executive's voice from 5 to 20 past posts. Export a baseline profile. Show the client the exact mathematical difference between their natural rhythm and generic AI prose.

### The Internal QA Filter
Run every draft through the gate before it reaches the account director. Eliminate junior writer drift and robotic tells without endless review cycles.

### How Style Lock Works
1. **Export the rules:** The account lead exports the client's measured voice as a `.grai` profile. Rules only. Zero client draft text.
2. **Import once:** The ghostwriter imports the `.grai` profile into their local workbench once. The rules persist locally on their device.
3. **Gate every draft:** Every draft is scored against the client's rules before submission. Drafts stay on the writer's machine. Zero seat fees.

---

## Editions and Pricing

### Agency Verification Protocol: $99/mo Pilot or $790/yr Annual
*Built for 1 to 5 person ghostwriting agencies billing executive clients $3,000 to $5,000 a month.*

- **Monthly Pilot ($99/mo):** https://buy.stripe.com/3cI28lbcs51v2Y9bArds401
- **Annual Protocol ($790/yr, saves $398):** https://buy.stripe.com/dRmfZb2FWalP42d5c3ds402
- **Paid 30-Day Pilot:** $99 first month, credited in full toward the $790 annual plan within 30 days. https://grai.page/pilot
- Up to 10 executive client voice profiles.
- White-label A4 **Client Voice DNA Dossier** with your agency branding.
- Live ECDSA P-256 verification links at `grai.page/verify/:hash`.
- Exportable Style Lock `.grai` profiles for contractor writers.
- Instant access to the local HTML5 workbench with zero server telemetry.

### Solo Offline Edition: $79/yr ($1.52/week, billed annually)
*Built for founders and independent writers who want one calibrated voice, offline.*
- **Details & Checkout:** https://grai.page/pricing/ ([Stripe](https://buy.stripe.com/3cIaERgwM9hLbuF33Vds400))
- Watermarked `grai.html` local workbench.
- 1 named voice profile with 1 year of engine updates.

### Pre-calibrated Voice DNA Archetypes ($39 Pack)
*Four pre-calibrated baseline profiles for instant calibration.*
- **Archetypes:** Brutalist Engineer (CV 0.52), Contrarian Bootstrapper (CV 0.44), B2B Sniper (CV 0.38), Substack Essayist (CV 0.41).
- **Checkout:** https://buy.stripe.com/fZu6oB1BS79D6algULds405

### Executive Voice DNA Architecture ($950 One-Time)
*Turnkey concierge calibration for a founder or CEO.*
- 50 executive posts calibrated by hand within 24 hours.
- Locked `.grai.json` profile, A4 executive reference dossier, and 1 year of Solo Workbench included.
- **Checkout:** https://buy.stripe.com/aFa5kx1BS2Tn8it47Zds403

---

## Three Questions Agencies Ask

### Why pay $99/mo when we already have ChatGPT Plus or Claude Pro?
Your model subscription generates prose in a generic statistical cadence. grai does not replace your model; it sits on top as an enforcement layer. It measures your client's cadence from published writing, gates every draft against eight structural rules and a CV >= 0.32 rhythm floor, and gives you a live verification link and A4 dossier to defend the retainer.

### Where do client drafts go, and can they be used to train AI models?
The local `grai.html` workbench runs entirely in your browser with zero application backend and zero telemetry. Client profiles and drafts stay in browser local storage or exported `.grai` files on your disk. Free scoring on the homepage is local; issuing a signed server seal audits the text once in RAM without storing draft prose.

### What happens after 30 days on the Agency Pilot?
Stripe bills $99 per month until you cancel. Within 30 days you can upgrade to the $790 annual plan with your first $99 credited in full, cancel by email with one click, or request a full 100% refund.

---

## The 30-Day Distinction Guarantee

If grai does not make your agency deliverables visibly sharper and faster to defend within 30 days, email `refund@grai.page` with your order number. 100% refund, no forms, no questions.

**Early Access CTA:** [Start Agency Pilot ($99/mo)](https://grai.page/pilot) | [Explore All Editions](https://grai.page/pricing/)
