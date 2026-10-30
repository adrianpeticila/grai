# grai-gate submission pack

Antigravity Marketplace answers for version 0.1.0. Copy each block without changes.

Publisher: grai, https://grai.page?utm_source=antigravity&utm_medium=plugin&utm_campaign=gate_v0.1

Repository: https://github.com/adrianpeticila/grai

License: MIT

## Plugin Name

```
grai-gate
```

## Short Description (under 80 characters)

```
Advisory anti-slop gate for agent-written markdown and docs.
```

## Long Description (Markdown)

```
grai-gate is an advisory anti-slop linter for the markdown your coding agent writes. READMEs, changelogs, docs pages, PR notes: every file that reaches disk through an agent carries the same fingerprints. Flat sentence rhythm. Hype vocabulary. Bullet lists that grow arrows.

The plugin adds a PostToolUse hook for .md and .txt writes. After each write, the local Python engine computes sentence-length burstiness, then checks the six structural tells that survive spellcheck. A clean file stays completely silent. A sloppy file prints a fixed report card to stderr with a score, the worst offender, the full flag list, and a repair prompt the agent can reuse.

What it catches:
- Flat cadence. The coefficient of variation of words per sentence falls under 0.32. The warning band starts at 0.35 and the human baseline is 0.40.
- Em dashes and double hyphens used as punctuation.
- The "here's why" opener.
- Contrastive negation.
- Arrow bullet cascades.
- Blocks of three bullets with near-identical sentence lengths.
- Weak closing questions.
- A curated list of dead AI cliches.

Advisory by design. The hook always prints {} on stdout and exits 0. It never denies a tool call, never rewrites a file, and never blocks an edit. Clean files stay silent. The engine is pure Python 3 standard library with no network calls, no telemetry, and no account.

The thresholds come from a study of 134,522 posts across 1,499 founder profiles, January 2023 to September 2026. Human drafts held a sentence-length CV at or above 0.40. Flat AI drafts landed under 0.32.

Install from the Antigravity Marketplace, or run `agy plugin install ./grai-gate` from the bundle. The plugin works with the documented Antigravity write tools and with the `write_file` and `edit_file` aliases.

The free plugin is the gate. The paid cockpit at grai.page is the repair bench, with a Voice DNA profile and rewrite passes for client-ready reports. Founder Edition is $69. Agency Edition is $149. Checkout runs on Payhip and Stripe processes every card.

[Open grai.page](https://grai.page?utm_source=antigravity&utm_medium=plugin&utm_campaign=gate_v0.1)
```

## Primary Category and Tags

Primary category:

```
Developer Tools
```

Tags:

```
markdown, linter, documentation, code-quality, ai-slop, writing
```

## Suggested Prompts (exactly 3)

```
Score my README for AI slop and show the report card.
Audit every markdown file in this repo and rank the worst three.
Rewrite the worst file to pass grai-gate, then score it again.
```

## Commercial notes

The plugin is free and MIT licensed. The paid cockpit is a separate product on grai.page. Founder Edition is $69. Agency Edition is $149. Checkout is live on Payhip with Stripe card processing.

All grai.page links in the bundle use:

```
https://grai.page?utm_source=antigravity&utm_medium=plugin&utm_campaign=gate_v0.1
```

## Pre-submit checklist

- `agy plugin validate ./grai-gate` passes without errors.
- The manifest uses documented keys and holds exactly three suggested prompts.
- The skill folder is `skills/grai` and its frontmatter name is `grai`.
- The hook group is `grai-gate`, the event is PostToolUse, and the timeout is 10 seconds.
- A clean file produces no output. A sloppy file produces one card on stderr.
- Stdout is exactly `{}` on every hook run. Malformed payloads included.
- The logo is bundled at `assets/logo.svg`.
- Every grai.page link carries the campaign string above.
- The Payhip checkout for both editions returns a live payment page.

## Reviewer posture

- The free layer is complete. No account, no key, no network call, no paid gate inside the runtime.
- The hook is advisory. It never denies a tool call and never edits a file.
- The report card is deterministic and fixed. Reviewers can reproduce it with the repository test suite in `plugin/tests/run_gate_tests.py`.
- The paid link is a static footer in the card. The engine never fetches it.
