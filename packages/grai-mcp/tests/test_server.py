"""End-to-end stdio handshake for the installed console script."""

import json
import shutil
import subprocess
import sys
import unittest

TIMEOUT = 20


def _script():
    found = shutil.which("grai-gate-mcp")
    if found:
        return [found]
    return [sys.executable, "-m", "grai_mcp.server"]


def _run(messages):
    payload = "".join(json.dumps(m) + "\n" for m in messages)
    proc = subprocess.run(
        _script(),
        input=payload,
        capture_output=True,
        text=True,
        timeout=TIMEOUT,
    )
    lines = [line for line in proc.stdout.splitlines() if line.strip()]
    return [json.loads(line) for line in lines]


class HandshakeTest(unittest.TestCase):
    def test_initialize_and_list(self):
        responses = _run(
            [
                {"jsonrpc": "2.0", "id": 1, "method": "initialize", "params": {}},
                {"jsonrpc": "2.0", "method": "notifications/initialized"},
                {"jsonrpc": "2.0", "id": 2, "method": "tools/list", "params": {}},
            ]
        )
        self.assertEqual(len(responses), 2)
        self.assertEqual(responses[0]["result"]["serverInfo"]["name"], "grai-gate")
        names = [t["name"] for t in responses[1]["result"]["tools"]]
        self.assertEqual(
            names,
            ["grai_score_draft", "grai_issue_agency_seal", "grai_verify_seal"],
        )

    def test_score_is_local(self):
        text = (
            "The gate reads the draft. It counts sentence length. It flags the "
            "patterns. Nothing leaves the machine. The score comes back."
        )
        responses = _run(
            [
                {"jsonrpc": "2.0", "id": 1, "method": "initialize", "params": {}},
                {
                    "jsonrpc": "2.0",
                    "id": 2,
                    "method": "tools/call",
                    "params": {
                        "name": "grai_score_draft",
                        "arguments": {"text": text},
                    },
                },
            ]
        )
        result = responses[-1]["result"]
        self.assertFalse(result.get("isError", False))
        body = json.loads(result["content"][0]["text"])
        self.assertTrue(body["ok"])
        self.assertIn("score", body)
        self.assertIn("cv", body)

    def test_empty_text_is_rejected(self):
        responses = _run(
            [
                {"jsonrpc": "2.0", "id": 1, "method": "initialize", "params": {}},
                {
                    "jsonrpc": "2.0",
                    "id": 2,
                    "method": "tools/call",
                    "params": {"name": "grai_score_draft", "arguments": {"text": "  "}},
                },
            ]
        )
        self.assertTrue(responses[-1]["result"].get("isError"))


if __name__ == "__main__":
    unittest.main()
