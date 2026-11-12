# grai-gate MCP install

Local stdio server. No API key needed for scoring.

Free browser checker, no install: https://grai.page/ai-tells/

## 1. Install

```bash
uvx --from grai-mcp grai-gate-mcp
```

If `uvx` is missing, install uv first: `curl -LsSf https://astral.sh/uv/install.sh | sh`.

Without uv:

```bash
pip install grai-mcp
```

## 2. Register the server

Add this to the MCP client config. The file path depends on the client, the block is the same:

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

With pip instead of uv:

```json
{
  "mcpServers": {
    "grai-gate": {
      "command": "grai-gate-mcp",
      "args": []
    }
  }
}
```

Client config paths:

- Cline: MCP Servers panel, or `cline_mcp_settings.json`
- Claude Desktop: `~/Library/Application Support/Claude/claude_desktop_config.json` on macOS, `%APPDATA%\Claude\claude_desktop_config.json` on Windows
- Cursor: `.cursor/mcp.json` or the global `~/.cursor/mcp.json`
- Windsurf: `~/.codeium/windsurf/mcp_config.json`

## 3. Verify

Send a JSON-RPC line over stdin and wait for the response. A working server answers immediately with `serverInfo.name` set to `grai-gate`:

```bash
echo '{"jsonrpc":"2.0","id":1,"method":"initialize","params":{}}' | uvx --from grai-mcp grai-gate-mcp
```

Expected shape:

```json
{"jsonrpc":"2.0","id":1,"result":{"protocolVersion":"2024-11-05","capabilities":{"tools":{}},"serverInfo":{"name":"grai-gate","version":"0.1.0"}}}
```

Then list the tools:

```bash
echo '{"jsonrpc":"2.0","id":2,"method":"tools/list","params":{}}' | uvx --from grai-mcp grai-gate-mcp
```

Three tools should come back: `grai_score_draft`, `grai_issue_agency_seal`, `grai_verify_seal`.

## 4. First call

```bash
echo '{"jsonrpc":"2.0","id":3,"method":"tools/call","params":{"name":"grai_score_draft","arguments":{"text":"First sentence here. Second one. Third one. Fourth one."}}}' | uvx --from grai-mcp grai-gate-mcp
```

The result is a JSON string in `result.content[0].text` with `ok`, `score`, `cv`, `pass` and `flags`. Scoring needs at least four sentences, otherwise `score` comes back `null` by design. `cv` needs four sentences and a mean sentence length of at least four words.

## Notes

- `grai_score_draft` is offline. No network call.
- `grai_issue_agency_seal` and `grai_verify_seal` call `https://grai.page/api/*` over HTTPS.
- Python 3.9 or newer.
