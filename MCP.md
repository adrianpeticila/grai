# MCP

grai ships one Model Context Protocol server. This page lists every surface it lives on.

## The server

| Surface | Location | Notes |
| --- | --- | --- |
| Package | [`grai-mcp`](https://pypi.org/project/grai-mcp/) on PyPI | stdio server, standard library only |
| Registry | `io.github.adrianpeticila/grai-mcp` | official MCP Registry |
| Docker | [`docker/mcp/Dockerfile`](docker/mcp/Dockerfile) | image entrypoint `grai-gate-mcp` |
| LobeHub | [lobehub.com/mcp/adrianpeticila-grai](https://lobehub.com/mcp/adrianpeticila-grai) | listing with the three tools |
| Cline | `registry/mcps/grai-gate/entry.json` in `cline/marketplace` | one-line install inside Cline |
| Claude plugin | [`plugin/grai-gate/.claude-plugin/plugin.json`](plugin/grai-gate/.claude-plugin/plugin.json) | bundle with `skills/grai/SKILL.md` |
| Docs | [grai.page/mcp](https://grai.page/mcp) and [grai.page/mcp.md](https://grai.page/mcp.md) | install, config, tools |
| Free checker | [grai.page/ai-tells](https://grai.page/ai-tells/) | twelve deterministic checks, no account, no upload |

## Install

```bash
uvx --from grai-mcp grai-gate-mcp
```

Client configuration:

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

| Tool | Input | Output | Network |
| --- | --- | --- | --- |
| `grai_score_draft` | `text` | score, CV, pass, failed rules, fail reason, advisory | none |
| `grai_issue_agency_seal` | `text`, `license_key`, `agency_name`, `client_ref` | signed record and verification link | `grai.page/api/seal` |
| `grai_verify_seal` | `record_json` | signature validity and key id | `grai.page/api/verify` |

The score needs at least four sentences. Below four it comes back `null` by design.

Lexical filters are calibrated for English. A draft in another language still gets the cadence score, but word-level tells are skipped. The response marks it with `advisory.non_english_detected: true` and the report card prints one note. It never blocks.

## Repository map

| Repo or folder | Purpose |
| --- | --- |
| `adrianpeticila/grai` (public) | source of truth for the plugin, the package and the site copy |
| `adrianpeticila/grai-private` | internal working repo with the private pipeline |
| `plugin/grai-gate` | plugin folder: skill, manifests, `mcp_server.py` |
| `packages/grai-mcp` | the PyPI package |

## License

The distributed package is MIT. See [`packages/grai-mcp/LICENSE`](packages/grai-mcp/LICENSE). The hosted product keeps its own commercial license. See [`source/COMMERCIAL-LICENCE.md`](source/COMMERCIAL-LICENCE.md).
