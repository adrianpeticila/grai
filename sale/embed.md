# grai embeddable voice dna audit widget

A compact, responsive audit widget that an agency can place on its own site as a free lead magnet. The visitor pastes a draft, sees the score and the cadence floor, and the upgrade links carry the partner code.

## Embed

```html
<iframe src="https://grai.page/embed?ref=PARTNER_ID" width="100%" height="520" frameborder="0" title="grai voice dna audit"></iframe>
```

## Partner parameter

- `?ref=PARTNER_ID` injects `client_reference_id=<tier>__aff_<PARTNER_ID>__<timestamp>` into all five Stripe checkout links (`wStarter`, `wFounder`, `wAgency`, `wAgencyAnnual`, `wStudio`) and appends `?aff=PARTNER_ID` to Payhip. Partners earn 40% commission across all tiers.
- The widget posts `{ "type": "grai-embed-height", "height": N }` to the parent frame, so a host page can resize the iframe without a scrollbar.
- The reference is sanitized to lowercase URL-safe characters (`a-z`, `0-9`, `-`, `_`) before it reaches a link.

## What the widget runs

The same eight syntactic rules and the same `CV >= 0.32` burstiness floor as `https://grai.page/#test`. The audit runs in the browser, makes no network call, and the draft never leaves the page.

## Commercial links

- Starter Audit Pass, $19 once (`STARTER19` 14-day upgrade credit): https://buy.stripe.com/14A00deoE51v56h1ZRds404
- Solo Offline Edition, $79/yr: https://buy.stripe.com/3cIaERgwM9hLbuF33Vds400
- Agency Verification Protocol, $99/mo: https://buy.stripe.com/3cI28lbcs51v2Y9bArds401
- Agency Verification Protocol, $790/yr: https://buy.stripe.com/dRmfZb2FWalP42d5c3ds402
- Executive Voice DNA Architecture, $950 one-time: https://buy.stripe.com/aFa5kx1BS2Tn8it47Zds403
- Voice DNA Archetype Presets, $39 once: https://payhip.com/b/ZAISC
- Partner program & link generator (40% commission): https://grai.page/affiliate
