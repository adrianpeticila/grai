#!/usr/bin/env python3
"""grai-gate MCP server.

A dependency-free JSON-RPC 2.0 server over stdio for Claude Desktop, Cursor,
Windsurf and Cline. It exposes three tools:

  grai_score_draft       local deterministic cadence score
  grai_issue_agency_seal live ECDSA P-256 seal via grai.page
  grai_verify_seal       verify a signed seal record

Only the Python standard library is used. The local scorer imports the
shipped gate.py from this plugin, so the MCP result matches the CLI result.
"""
import json
import sys
import urllib.error
import urllib.request

from . import __version__
from . import gate as gate_engine

VERSION = __version__
SERVER_NAME = "grai-gate"
API_BASE = "https://grai.page"
USER_AGENT = "GraiProtocol/3.3 (+https://grai.page)"

UPGRADE = {
    "solo_offline": "https://buy.stripe.com/3cIaERgwM9hLbuF33Vds400",
    "agency_monthly": "https://buy.stripe.com/3cI28lbcs51v2Y9bArds401",
    "agency_annual": "https://buy.stripe.com/dRmfZb2FWalP42d5c3ds402",
    "dfy_architecture": "https://buy.stripe.com/aFa5kx1BS2Tn8it47Zds403",
}

TOOLS = [
    {
        "name": "grai_score_draft",
        "description": (
            "Score a draft with the deterministic grai cadence gate. Returns the "
            "score, sentence-length CV, failed rules and direct upgrade links."
        ),
        "inputSchema": {
            "type": "object",
            "properties": {
                "text": {"type": "string", "description": "Draft text to audit."}
            },
            "required": ["text"],
        },
    },
    {
        "name": "grai_issue_agency_seal",
        "description": (
            "Audit a finished client draft in server memory and return a public "
            "verification link. Requires an Agency Verification Protocol license."
        ),
        "inputSchema": {
            "type": "object",
            "properties": {
                "text": {"type": "string", "description": "Finished client draft."},
                "license_key": {"type": "string", "description": "Agency license key."},
                "agency_name": {"type": "string", "description": "Agency display name."},
                "client_ref": {"type": "string", "description": "Client reference for the receipt."},
            },
            "required": ["text"],
        },
    },
    {
        "name": "grai_verify_seal",
        "description": "Verify a signed grai seal record against the public keyring.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "record_json": {
                    "type": "string",
                    "description": "The signed seal record as JSON.",
                }
            },
            "required": ["record_json"],
        },
    },
]


def _post_json(path, payload, timeout=25):
    data = json.dumps(payload).encode("utf-8")
    request = urllib.request.Request(
        API_BASE + path,
        data=data,
        headers={
            "Content-Type": "application/json",
            "Accept": "application/json",
            "User-Agent": USER_AGENT,
        },
        method="POST",
    )
    with urllib.request.urlopen(request, timeout=timeout) as response:
        raw = response.read().decode("utf-8", "replace")
    return json.loads(raw)


def _score_payload(text):
    try:
        analysis = gate_engine.analyze(text)
        flags = []
        for item in analysis.get("flags", []):
            flags.append(
                {
                    "key": item.get("key"),
                    "name": item.get("name"),
                    "count": item.get("count"),
                    "penalty": item.get("penalty"),
                    "quote": item.get("quote"),
                }
            )
        return {
            "ok": True,
            "score": analysis.get("score"),
            "cv": analysis.get("cv"),
            "pass": analysis.get("pass"),
            "sentences": analysis.get("sentences"),
            "flags": flags,
            "fail_reason": analysis.get("fail_reason"),
            "upgrade": UPGRADE,
        }
    except Exception:
        result = _post_json("/api/score", {"text": text})
        result["upgrade"] = UPGRADE
        return result


def _tool_result(text, is_error=False):
    result = {"content": [{"type": "text", "text": text}]}
    if is_error:
        result["isError"] = True
    return result


def _tool_error(message):
    return _tool_result(message, True)


def call_tool(name, arguments):
    if name == "grai_score_draft":
        text = str((arguments or {}).get("text") or "")
        if not text.strip():
            return _tool_error("text is required")
        try:
            return _tool_result(json.dumps(_score_payload(text), indent=2, ensure_ascii=False))
        except (urllib.error.URLError, OSError, ValueError) as exc:
            return _tool_error("grai score failed: %s" % exc)

    if name == "grai_issue_agency_seal":
        text = str((arguments or {}).get("text") or "")
        license_key = str((arguments or {}).get("license_key") or "").strip()
        agency_name = str((arguments or {}).get("agency_name") or "").strip()
        client_ref = str((arguments or {}).get("client_ref") or "").strip()
        if not text.strip():
            return _tool_error("text is required")
        if not license_key:
            return _tool_error(
                "A license_key is required to issue a live verification link. "
                "Buy the Agency Verification Protocol at "
                + UPGRADE["agency_monthly"]
            )
        payload = {"license_key": license_key, "text": text}
        if agency_name:
            payload["agency_name"] = agency_name
        if client_ref:
            payload["client_ref"] = client_ref
        try:
            result = _post_json("/api/seal", payload)
        except urllib.error.HTTPError as exc:
            body = exc.read().decode("utf-8", "replace")
            return _tool_error("grai seal failed (%s): %s" % (exc.code, body))
        except (urllib.error.URLError, OSError, ValueError) as exc:
            return _tool_error("grai seal failed: %s" % exc)
        if isinstance(result, dict):
            result["upgrade"] = UPGRADE
        return _tool_result(json.dumps(result, indent=2, ensure_ascii=False))

    if name == "grai_verify_seal":
        raw = str((arguments or {}).get("record_json") or "").strip()
        if not raw:
            return _tool_error("record_json is required")
        try:
            record = json.loads(raw)
        except ValueError as exc:
            return _tool_error("record_json is not valid JSON: %s" % exc)
        try:
            result = _post_json("/api/verify", {"record": record})
        except (urllib.error.URLError, OSError, ValueError) as exc:
            return _tool_error("grai verify failed: %s" % exc)
        if isinstance(result, dict):
            result["upgrade"] = UPGRADE
        return _tool_result(json.dumps(result, indent=2, ensure_ascii=False))

    return _tool_error("unknown tool: %s" % name)


def handle(message):
    if not isinstance(message, dict):
        return {
            "jsonrpc": "2.0",
            "id": None,
            "error": {"code": -32600, "message": "Invalid Request"},
        }

    method = message.get("method")
    message_id = message.get("id")
    params = message.get("params") or {}

    if method == "initialize":
        return {
            "jsonrpc": "2.0",
            "id": message_id,
            "result": {
                "protocolVersion": "2024-11-05",
                "capabilities": {"tools": {}},
                "serverInfo": {"name": SERVER_NAME, "version": VERSION},
            },
        }

    if method == "notifications/initialized":
        return None

    if method == "ping":
        return {"jsonrpc": "2.0", "id": message_id, "result": {}}

    if method == "tools/list":
        return {
            "jsonrpc": "2.0",
            "id": message_id,
            "result": {"tools": TOOLS},
        }

    if method == "tools/call":
        name = params.get("name")
        arguments = params.get("arguments") or {}
        return {
            "jsonrpc": "2.0",
            "id": message_id,
            "result": call_tool(name, arguments),
        }

    if message_id is None:
        return None

    return {
        "jsonrpc": "2.0",
        "id": message_id,
        "error": {"code": -32601, "message": "Method not found: %s" % method},
    }


def main():
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            message = json.loads(line)
        except ValueError:
            response = {
                "jsonrpc": "2.0",
                "id": None,
                "error": {"code": -32700, "message": "Parse error"},
            }
        else:
            response = handle(message)
        if response is None:
            continue
        sys.stdout.write(json.dumps(response, ensure_ascii=False) + "\n")
        sys.stdout.flush()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
