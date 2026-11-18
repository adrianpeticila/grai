# grai MCP server

> **grai-gate** is a Model Context Protocol server. It scores a draft for cadence and structural slop, and it verifies signed client seals. Works in Claude Desktop, Cursor, Cline, Windsurf and any other MCP client.

- **Canonical page:** https://grai.page/mcp
- **Package:** https://pypi.org/project/grai-mcp/ (`grai-mcp` on PyPI)
- **Current release:** `0.1.3` on PyPI (bundling `gate.py` engine `0.2.0`), verified 2026-11-13
- **Registry name:** `io.github.adrianpeticila/grai-mcp`
- **Source:** https://github.com/adrianpeticila/grai
- **Free checker:** https://grai.page/ai-tells/ (twelve deterministic checks, no account, no upload)
- **Install guide for agents:** https://github.com/adrianpeticila/grai/blob/main/llms-install.md
- **License:** MIT for the package, https://github.com/adrianpeticila/grai/blob/main/packages/grai-mcp/LICENSE

---

## Install

```
uvx --from grai-mcp grai-gate-mcp
```

Without uv: `pip install grai-mcp` and run `grai-gate-mcp`.

## Client configuration

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

Config locations:

| Client | Path |
|---|---|
| Claude Desktop | `claude_desktop_config.json` |
| Cursor | `.cursor/mcp.json` |
| Cline | MCP Servers panel |
| Windsurf | `mcp_config.json` |

## Tools

| Tool | Input | Output | Network |
|---|---|---|---|
| `grai_score_draft` | `text` | score, CV, pass, failed rules, fail reason, advisory | none |
| `grai_issue_agency_seal` | `text`, `license_key`, `agency_name`, `client_ref` | signed record and public verification link | `https://grai.page/api/seal` |
| `grai_verify_seal` | `record_json` | signature validity and key id | `https://grai.page/api/verify` |

Scoring runs offline. No API key, no account, no draft text leaving the machine.

## Score input requirements

The score is computed from at least four sentences. Below four, the score comes back `null` by design. The CV needs four sentences and a mean sentence length of at least four words.

## Language scope

The lexical filters are calibrated for English. A German, French or Romanian draft still gets the cadence score, but word-level tells will not catch local slop. Those drafts come back with `advisory.non_english_detected: true`, and the report card prints one note. The gate does not block, and it does not pretend the draft passed a lexical check it never ran.

## Verify the install

```
echo '{"jsonrpc":"2.0","id":1,"method":"initialize","params":{}}' | uvx --from grai-mcp grai-gate-mcp
```

A working server answers with `serverInfo` name `grai-gate`.

## Docker

The repository ships a container image definition at `docker/mcp/Dockerfile`, entrypoint `grai-gate-mcp`.

---

Last updated: 2026-11-13.
