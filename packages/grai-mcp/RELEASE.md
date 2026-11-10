# Release

Two artifacts: the PyPI package and the registry entry.

## 1. PyPI

```bash
cd packages/grai-mcp
uv build
uv publish
```

`uv publish` reads `UV_PUBLISH_TOKEN`. The token in `~/.pypirc` is scoped to
`grai-gate` and cannot create `grai-mcp`, so the first upload needs an
account-scoped token from https://pypi.org/manage/account/token/.

Verify:

```bash
uvx --from grai-mcp grai-gate-mcp
```

## 2. MCP Registry

The registry validates against PyPI, so the package has to be live first. It
checks for `mcp-name: io.github.adrianpeticila/grai-mcp` in the PyPI README,
which comes from `README.md` in this folder.

```bash
cd packages/grai-mcp
mcp-publisher validate
mcp-publisher login github
mcp-publisher publish
```

## 3. Version bumps

`version` must match in three places before a release:

- `pyproject.toml`
- `src/grai_mcp/__init__.py`
- `server.json` (both the top-level version and `packages[0].version`)

A PyPI version cannot be reused. Bump it even for a one-character fix.
