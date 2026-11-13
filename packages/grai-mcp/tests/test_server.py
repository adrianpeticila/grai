"""End-to-end stdio handshake for the installed console script."""

import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import unittest

TIMEOUT = 20
SRC = Path(__file__).resolve().parent.parent / "src"

if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

import grai_mcp.server as server  # noqa: E402


def _script():
    found = shutil.which("grai-gate-mcp")
    if found:
        return [found]
    return [sys.executable, "-m", "grai_mcp.server"]


def _run(messages):
    payload = "".join(json.dumps(m) + "\n" for m in messages)
    env = dict(os.environ)
    env["PYTHONPATH"] = str(SRC) + (":" + env["PYTHONPATH"] if "PYTHONPATH" in env else "")
    proc = subprocess.run(
        _script(),
        input=payload,
        capture_output=True,
        text=True,
        timeout=TIMEOUT,
        env=env,
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


class ScoreOfflineContractTest(unittest.TestCase):
    def setUp(self):
        self._orig_analyze = server.gate_engine.analyze
        self._orig_post = server._post_json
        self.network_calls = []

    def tearDown(self):
        server.gate_engine.analyze = self._orig_analyze
        server._post_json = self._orig_post

    def _forbid_network(self, *args, **kwargs):
        self.network_calls.append((args, kwargs))
        raise AssertionError("score path attempted a network call")

    def test_analyze_failure_never_posts(self):
        def boom(text):
            raise RuntimeError("engine exploded")

        server.gate_engine.analyze = boom
        server._post_json = self._forbid_network

        with self.assertRaises(ValueError):
            server._score_payload("One sentence here. Another one follows. A third.")

        self.assertEqual(self.network_calls, [])

    def test_tool_call_returns_error_without_posting(self):
        def boom(text):
            raise RuntimeError("engine exploded")

        server.gate_engine.analyze = boom
        server._post_json = self._forbid_network

        result = server.call_tool(
            "grai_score_draft",
            {"text": "One sentence here. Another one follows. A third."},
        )

        self.assertTrue(result.get("isError"))
        self.assertEqual(self.network_calls, [])


if __name__ == "__main__":
    unittest.main()
