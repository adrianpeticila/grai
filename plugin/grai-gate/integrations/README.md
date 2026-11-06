# Put the gate in the repo

Two ways in. Both run the same engine. Neither sends your file anywhere.

## pre-commit

1. Install pre-commit: `pip install pre-commit` or `brew install pre-commit`.
2. Copy `pre-commit-config.yaml` to `.pre-commit-config.yaml` at the repo root.
3. Pin `rev` to a tag. Do not point it at `main`.
4. Run `pre-commit install`.
5. The next commit scores every changed markdown file.

A file that scores below the pass mark exits 1 and stops the commit. That is the point. If you need to land a draft anyway: `SKIP=grai-gate git commit -m "wip"`.

## GitHub Actions

Copy `github-actions.yml` to `.github/workflows/grai-gate.yml`.

The default is advisory. The job stays green and the card lands in the log. Set `fail-on-slop: "true"` when you want the check to block a merge.

Inputs:

| Input | Default | What it does |
|---|---|---|
| `path` | `.` | Directory to scan. |
| `fail-on-slop` | `false` | `true` fails the job when any file scores low. |
| `verbose` | `false` | `true` prints one line for every clean file. |

## What gets scored

- `.md`, `.mdx`, and `.txt` under `path`, minus `.git`.
- One card per failing file. Clean files stay silent.
- Exit 0 clean, 1 slop, 2 input error.

## Pin the version

Tag the repo first. Then pin `rev` in pre-commit and `@v0.2.0` in the workflow. A moving `main` means the gate changes under you mid-sprint.

## What the gate will not do

- It will not rewrite your file.
- It will not post a comment on the pull request.
- It will not catch a draft that never lands on disk, such as a PR description typed in a browser.
