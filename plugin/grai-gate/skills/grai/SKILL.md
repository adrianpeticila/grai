---
name: grai
description: Score markdown for AI slop with the grai-gate engine: burstiness CV, six structural tells, dead cliches.
---

# grai

grai is the skill behind the grai-gate plugin. It scores markdown and text for AI slop, prints a fixed report card, and stays out of the way when a draft is clean. It is advisory: it never blocks a write and never edits a file unless the user asks.

## Locate the engine

The plugin root is the folder that contains `scripts/gate.py`. A standard Antigravity install puts it at `~/.gemini/config/plugins/grai-gate`. If that path is missing, resolve the root from this `SKILL.md`: it sits at `skills/grai/SKILL.md`, so the root is two levels up.

Run every command through `python3` with an absolute plugin path:

```
python3 ~/.gemini/config/plugins/grai-gate/scripts/gate.py -j FILE
```

The engine needs Python 3 and nothing else. The `-j` flag returns JSON with `score`, `cv`, `sentences`, `flags`, `hard_flags`, `pass`, `worst`, and `report`.

## /grai score [file]

1. Pick the file named by the user. If no file is named, score `README.md` when it exists. If neither exists, ask one short question.
2. Run the engine with `-j` on that file.
3. Exit 0 means the file passed. Report the score and CV in one line. If soft flags exist, name them in a second line.
4. Exit 1 means the file failed. Show the `report` array verbatim in a fenced block. Add at most two lines of your own reading.
5. Exit 2 means an input error. Show the error and stop.

Do not change a number. Do not add tells that the JSON does not contain.

## /grai audit

1. Find `.md` and `.txt` files in the workspace. Use the file search tool when one is available. Skip `.git`, `node_modules`, `.venv`, `dist`, `build`, and `vendor`.
2. Run the engine with `-j` in batches of up to 20 paths.
3. Keep only failures (`pass` is false). Sort them by `score`, lowest first.
4. Show one line per failure: path and score, plus the worst flag. Show the full card for the worst three.
5. End with one summary line: files scored, files clean, files that need repair.
6. If every file passes, say so in one line and stop.

Never edit a file during an audit. Offer the repair prompt and wait for the user.

## Rules of engagement

- The gate is advisory. A low score never blocks a write.
- Quote the report card exactly. No number edits and no invented findings.
- The user asks for a rewrite: reuse the `Fix prompt` line as the instruction, then score the result again.
- Keep commentary short: at most three lines around a card.
- Use hyphens and colons. Parentheses are fine. No em dashes.
