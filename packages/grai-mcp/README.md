# grai-gate MCP server

<!-- mcp-name: io.github.adrianpeticila/grai-mcp -->

Deterministic cadence scoring and cryptographic seal verification for AI-generated
drafts, exposed as a Model Context Protocol server over stdio.

No API key needed for scoring. The gate is a pure Python scorer with no
dependencies outside the standard library.

Free browser checker, no install: https://grai.page/ai-tells/

## Install

Requires Python 3.10+ and [uv](https://docs.astral.sh/uv/):

```bash
uvx --from grai-mcp grai-gate-mcp
```

Or with pip:

```bash
pip install grai-mcp
grai-gate-mcp
```

## Configure your client

Claude Desktop, Cursor, Cline, Windsurf and any client reading `mcpServers`:

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

If your client runs with pip instead of uv, use:

```json
{
  "mcpServers": {
    "grai-gate": {
      "command": "grai-gate-mcp"
    }
  }
}
```

### Config file locations

| Client | Configuration Path |
| --- | --- |
| Claude Desktop (macOS) | `~/Library/Application Support/Claude/claude_desktop_config.json` |
| Claude Desktop (Windows) | `%APPDATA%\Claude\claude_desktop_config.json` |
| Cursor | `~/.cursor/mcp.json` or `.cursor/mcp.json` in project root |
| Windsurf | `~/.codeium/windsurf/mcp_config.json` |
| Cline | VS Code MCP Servers panel |

*Note for macOS GUI apps:* Claude Desktop started from Finder does not inherit shell PATH. If the server fails to start with `ENOENT`, run `which uvx` in your terminal and put the absolute path in the `command` field (for example, `/Users/yourname/.local/bin/uvx`). Restart your client after saving the config.

## Tools

| Tool | Input arguments | Output | Needs network |
| --- | --- | --- | --- |
| `grai_score_draft` | `{"text": "..."}` | score (0-100), CV, pass, failed rules, advisory | no |
| `grai_issue_agency_seal` | `{"text": "...", "license_key": "...", "agency_name": "...", "client_ref": "..."}` | signed record and public verification link | yes |
| `grai_verify_seal` | `{"record_json": "..."}` | signature validity and key id | yes |

`grai_score_draft` runs entirely offline on stdio. The scorer engine is bundled directly inside the wheel.

## How to use in chat

In your AI chat (Claude Desktop, Cursor, etc.), prompt the model directly:

> "Score this draft with grai_score_draft: [paste your text here]"

The tool will return the calculated score, the sentence-length coefficient of variation (CV), and any detected slop rules. A score of 85 or higher passes.

## Input requirements

The score requires at least four sentences with a mean sentence length of at least four words. If you send a draft with fewer than four sentences, the engine returns `score: null` and sets `insufficient_sentences: true` in the advisory dictionary.

## What the gate checks

Sentence-length variance (CV), run-on sentences and comma splices, contrastive negation, epiphany openers, corporate slop words, em dashes, structural monotony, and five other deterministic rules. Same engine as the `grai-gate` CLI, so scores match between the CLI and the MCP server.

A flagged run-on sentence contributes at most 32 words to the CV, so swapping full stops for commas cannot inflate the score.

The lexical rules are calibrated for English. Other languages still get a cadence score, but word-level tells are skipped. The response carries `advisory.non_english_detected`, and the report card prints one note. No block, no silent pass.

## Links

- Product: https://grai.page
- Source: https://github.com/adrianpeticila/grai
- License: MIT
