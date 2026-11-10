# grai-gate MCP server

<!-- mcp-name: io.github.adrianpeticila/grai-mcp -->

Deterministic cadence scoring and cryptographic seal verification for AI-generated
drafts, exposed as a Model Context Protocol server over stdio.

No API key needed for scoring. The gate is a pure Python scorer with no
dependencies outside the standard library.

## Install

```bash
uvx --from grai-mcp grai-gate-mcp
```

Or with pip:

```bash
pip install grai-mcp
grai-gate-mcp
```

## Configure your client

Claude Desktop, Cursor, Cline, Windsurf and anything else that reads `mcpServers`:

```json
{
  "mcpServers": {
    "grai-gate": {
      "command": "uvx",
      "args": ["--from", "grai-mcp", "grai-gate-mcp"]
    }
  }
}
```

## Tools

| Tool | What it does | Needs network |
| --- | --- | --- |
| `grai_score_draft` | Scores a draft, returns score, sentence-length CV, failed rules | no |
| `grai_issue_agency_seal` | Audits a client draft and returns a public verification link | yes |
| `grai_verify_seal` | Verifies a signed seal record against the public keyring | yes |

`grai_score_draft` runs entirely offline. If the local scorer cannot load, it
falls back to the hosted endpoint.

## Example

```json
{"name": "grai_score_draft", "arguments": {"text": "Your draft goes here."}}
```

The response carries the score, the CV, the rules that failed, and upgrade
links. A score of 85 or higher passes.

## What the gate checks

Sentence-length variance (CV), contrastive negation, epiphany openers,
corporate slop words, em dashes, structural monotony, and five other
deterministic rules. Same engine as the `grai-gate` CLI, so scores match
between the CLI and the MCP server.

## Links

- Product: https://grai.page
- Source: https://github.com/adrianpeticila/grai
- License: MIT
