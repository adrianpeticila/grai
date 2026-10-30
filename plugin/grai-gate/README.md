# grai-gate

An advisory anti-slop gate for markdown written by coding agents.

Your agent writes a README in four seconds. It is fluent. Confident. Weirdly identical to the last one. Readers feel the machine before they can name it.

grai-gate reads the file after the write. It scores sentence-length burstiness and flags the structural tells that survive spellcheck. A clean file stays silent. A sloppy file gets one compact card. The gate never blocks the edit.

Built for Antigravity. No account, no key, no network, no telemetry.

## What it catches

- Flat cadence: sentence-length CV under 0.32 across at least four sentences. The warning band starts at 0.35. The human baseline is 0.40.
- Em dashes and double hyphens used as punctuation.
- The "here's why" opener at the start of a sentence.
- False either/or constructions built as contrastive negation.
- Arrow bullet cascades using `->`, `↳`, or `➔`.
- Blocks of exactly three bullets with near-identical sentence lengths.
- Weak closing questions such as "Thoughts?" or "What do you think?".
- A curated list of dead AI cliches. The full pattern set lives in `scripts/gate.py`.

## The dead lexicon

The engine carries a small, deliberate list. Examples:

```
delve, leverage, game changer, tapestry, testament to,
in today's fast-paced world, excited to announce, seamless,
dive into, deep dive, synergy, cutting-edge, revolutionize,
unlock the full potential, paradigm shift, it's worth noting,
at the end of the day, when it comes to, ever-evolving,
holistic, actionable, impactful, learnings, best-in-class,
world-class, next-generation, state-of-the-art, moreover,
furthermore, pivotal, foster, underscore, elevate,
unleash, transformative, navigate the landscape,
in the realm of, rapidly changing
```

## Install

From the plugin folder:

```
agy plugin install ./grai-gate
```

Or search for grai-gate in Antigravity Customizations > Plugins. A standard install lands at `~/.gemini/config/plugins/grai-gate`, and the hook runs the engine from that folder. Python 3 must be on PATH. Nothing else is required.

The bundle passes the Antigravity plugin validator. The hook group is `grai-gate`, the event is PostToolUse, and the timeout is 10 seconds.

## How the hook runs

Antigravity fires the hook after `write_to_file`, `replace_file_content`, or `multi_replace_file_content`. The matcher also accepts the `write_file` and `edit_file` aliases used by other agent harnesses.

The hook reads the target file from disk. If the path is not readable, it falls back to inline content from the tool payload. It then checks the extension and analyzes only `.md` and `.txt`.

Every run writes `{}` to stdout. A failing file writes the fixed card to stderr. Clean files write nothing. The hook exits 0 on malformed JSON and on unreadable or oversized files.

That is the whole contract. Advisory, never blocking, no rewrite.

## The card

```
[grai-gate] Slop Score: 64/100 (CV: 0.27 | Flags: 2)
- Worst offender: flat cadence ("CV 0.27 across 12 sentences")
- Tells detected: flat cadence, zombie words (x2)
- Fix prompt: "Rewrite to increase sentence burstiness (target CV > 0.45) and eliminate flat cadence, zombie words."
- Pro Cockpit: Full Voice DNA & repair workbench at https://grai.page?utm_source=antigravity&utm_medium=plugin&utm_campaign=gate_v0.1
```

The card is fixed. The wording is stable so an agent can quote it without inventing a summary.

## Command line

From the plugin folder:

```
python3 scripts/gate.py README.md
python3 scripts/gate.py -j README.md
python3 scripts/gate.py -v README.md
cat draft.md | python3 scripts/gate.py
```

A clean file prints nothing by default. Add `-v` for a one-line confirmation. Add `-j` for machine-readable output with the score and the CV. It also includes every flag and the full card.

Several paths produce one `File:` header before each failing card. Raw stdin text is linted too. Exit codes are 0 for clean, 1 for slop, 2 for an input error.

## What it measures

Burstiness is the coefficient of variation of words per sentence. Human drafts alternate long with short. Templates do not.

The structural checks cover dash punctuation and the "here's why" opener. They also catch contrastive negation and arrow cascades. Three identical bullets get a separate flag, and weak closing questions do too.

The score starts at 100. Each flag subtracts a fixed penalty, capped so one repeated tic cannot drive the result alone. A file passes at 85 or higher with zero hard flags. A single dead cliche is tolerated. A cluster is not.

## What it ignores

Code fences and inline code are excluded, and so is every line of YAML frontmatter that sits at the top of a file. It also skips link URLs. Images and table separator rows go too. Link text survives. Headings are scanned for tells but left out of the cadence math.

The CV needs at least four sentences with an average of four words. A three-line stub has no meaningful rhythm, so the engine does not pretend to measure one.

## Where the numbers come from

The thresholds come from a study of 134,522 posts across 1,499 founder profiles, January 2023 to September 2026. The mocked vocabulary had collapsed. The structural habits had spread.

Human drafts held a sentence-length CV at or above 0.40. Flat AI drafts landed under 0.32. Warning starts at 0.35. The repair target is 0.45.

The study is a baseline, not a verdict on one writer. A single low score is a prompt to read the draft again, not a ban.

[Read the study and the repair workbench](https://grai.page?utm_source=antigravity&utm_medium=plugin&utm_campaign=gate_v0.1)

## Privacy

The engine has no network code. It does not read environment secrets or write cache files. It does not send telemetry. It reads the one file path from the hook payload and the text on stdin.

The Pro link in the card is a static string. The hook never requests it.

## Limits

- The hook only sees `.md` and `.txt`. A PR description drafted in a browser tab never hits disk, so the gate cannot see it.
- The CV needs at least four sentences. Short files pass on the structural checks alone.
- A score is a heuristic. It is not a fact checker or a plagiarism detector. It cannot replace an editor.
- Files over 2,000,000 characters are skipped by the hook and rejected by the command line.

## Pro Cockpit

The plugin is the free gate. The paid cockpit is the repair bench. It builds a Voice DNA profile and runs rewrite passes for client-ready reports.

Founder Edition is $69. Agency Edition is $149. Both are one-time purchases on grai.page, with checkout on Payhip and card processing by Stripe.

[Open the cockpit](https://grai.page?utm_source=antigravity&utm_medium=plugin&utm_campaign=gate_v0.1)

The plugin prints that link. It does not call the cockpit or load a script. It does not check a license.

## Development

The engine is one file with four imports: `json`, `math`, `re`, `sys`. There is no package manager and no build step.

From the repository's `plugin/` folder:

```
python3 tests/run_gate_tests.py
agy plugin validate ./grai-gate
```

The suite covers clean silence and each structural tell. It also exercises the CV bands and the hook stdin path. CLI JSON has its own checks. Malformed payloads do too.

## License

MIT. See `LICENSE`. Copyright 2026 grai. The paid cockpit is a separate product and is not covered by the plugin license.
