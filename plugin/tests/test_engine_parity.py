#!/usr/bin/env python3
"""test_engine_parity.py — Parity test between app.html preflight and gate.py.

Extracts the shipped GRAI_RULES from app.html, compiles them in Python,
runs shared test specimens through both gate.analyze and preflight,
and verifies agreement on clean vs slop verdicts.
"""
import math
import os
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
REPO = HERE.parent.parent
APP_PATH = REPO / "source" / "src" / "app.html"
GATE_PATH = REPO / "plugin" / "grai-gate" / "scripts"
sys.path.insert(0, str(GATE_PATH))
import gate

FLAG_MAP = {"i": re.IGNORECASE, "m": re.MULTILINE, "s": re.DOTALL}
ENTRY = re.compile(
    r'\[\s*"([A-Z_]{3,})"\s*,\s*(\d+)\s*,\s*(\d+)\s*,\s*'
    r'/(?P<pat>(?:\\.|[^/\\])*)/(?P<flags>[a-z]*)\s*\]'
)


def js_to_py_pattern(pat):
    def repl(m):
        cp = int(m.group(1), 16)
        return ("\\u%04X" % cp) if cp <= 0xFFFF else ("\\U%08X" % cp)
    return re.sub(r"\\u\{([0-9A-Fa-f]+)\}", repl, pat)


def extract_array(text, name):
    i = text.find(name)
    if i < 0:
        return None
    i = text.find("[", i)
    if i < 0:
        return None
    depth = 0
    for j in range(i, len(text)):
        if text[j] == "[":
            depth += 1
        elif text[j] == "]":
            depth -= 1
            if depth == 0:
                return text[i:j + 1]
    return None


def load_app_rules():
    html = APP_PATH.read_text(encoding="utf-8")
    block = extract_array(html, "GRAI_RULES")
    rules = []
    for m in ENTRY.finditer(block):
        name, first, rep, pat, flags = (m.group(1), int(m.group(2)), int(m.group(3)),
                                        m.group("pat"), m.group("flags"))
        py_flags = 0
        for f in flags:
            if f in FLAG_MAP:
                py_flags |= FLAG_MAP[f]
        compiled = re.compile(js_to_py_pattern(pat), py_flags)
        rules.append((name, first, rep, compiled))
    return rules


RE_BRIDGE = re.compile(
    r"(?i)^\s*(?:that['\u2019]?s\s+why|this\s+is\s+why|which\s+is\s+why|in\s+other\s+words|"
    r"that['\u2019]?s\s+what|this\s+means(?:\s+that)?|which\s+means(?:\s+that)?|"
    r"that['\u2019]?s\s+exactly(?:\s+why|\s+what)?|so\s+what\s+does\s+this\s+mean)\b"
)


def app_preflight(text, rules):
    pen = 0
    hits = []
    for name, first, rep, pattern in rules:
        matches = list(pattern.finditer(text))
        if matches:
            pen += first + rep * (len(matches) - 1)
            hits.append(name)
    paras = [p.strip() for p in re.split(r"\n\s*\n", text) if p.strip()]
    bridge_hits = 0
    max_consec = 0
    cur_consec = 0
    for p in paras:
        if RE_BRIDGE.match(p):
            bridge_hits += 1
            cur_consec += 1
            if cur_consec > max_consec:
                max_consec = cur_consec
        else:
            cur_consec = 0
    if max_consec >= 3 or bridge_hits >= 4:
        count = max_consec if max_consec >= 3 else bridge_hits
        pen += 12 + 6 * (count - 1)
        hits.append("SMOOTH_BRIDGE")
    score = max(4, min(100, 100 - pen))
    return score, hits


SPECIMENS = [
    ("clean human", (
        "A $9/month user emailed us 14 times on Christmas Eve because he cleared his browser cookies, "
        "then filed a Stripe dispute before noon on the 26th.\n\n"
        "We killed monthly billing that afternoon.\n\n"
        "Revenue dipped for eleven days while affiliate traffic adjusted to the $79 one-time license, "
        "then climbed 40% above our previous peak with zero weekend support tickets."
    ), True),
    ("verdict colon", (
        "The harsh reality is: pricing low will destroy your margin before you find product market fit.\n\n"
        "We learned this the hard way after launching our initial beta."
    ), False),
    ("prose triad", (
        "Why did they quit? Was it the pricing? Could they not survive the transition?\n\n"
        "We spent three weeks asking every churned customer what went wrong."
    ), False),
    ("contrastive negation", (
        "It's not about the features you ship, it's about the problems you eliminate for the customer."
    ), False),
    ("heres truth colon single hit", (
        "Here's the truth: pricing low will destroy your margin before you find product market fit.\n\n"
        "We learned this the hard way after launching our initial beta."
    ), False),
    ("heres secret colon single hit", (
        "Here's the secret: pricing low will destroy your margin before you find product market fit.\n\n"
        "We learned this the hard way after launching our initial beta."
    ), False),
]


def test_parity():
    rules = load_app_rules()
    assert len(rules) == 8, f"Expected 8 rules in app.html, got {len(rules)}"
    worker_text = (REPO / "sale" / "_worker.js").read_text(encoding="utf-8")
    assert "VERDICT_COLON" in worker_text and "PROSE_TRIAD" in worker_text and "SMOOTH_BRIDGE" in worker_text, "Worker missing new rules"
    failures = []
    for label, text, expect_clean in SPECIMENS:
        gate_res = gate.analyze(text)
        app_score, app_hits = app_preflight(text, rules)
        gate_flagged = len(gate_res["flags"]) > 0
        app_flagged = len(app_hits) > 0

        # No double penalty on colon forms
        if "single hit" in label:
            if "EPIPHANY_OPENER" in app_hits and "VERDICT_COLON" in app_hits:
                failures.append(f"{label}: double fired EPIPHANY_OPENER and VERDICT_COLON in app_hits: {app_hits}")

        # Both must agree on clean vs flagged
        if expect_clean:
            if gate_flagged or app_flagged:
                failures.append(f"{label}: expected clean, gate_flagged={gate_flagged}, app_flagged={app_flagged}")
        else:
            if not gate_flagged or not app_flagged:
                failures.append(f"{label}: expected flagged, gate_flagged={gate_flagged}, app_flagged={app_flagged}")

    if failures:
        print("PARITY FAILURES:\n  " + "\n  ".join(failures))
        return 1
    print("ENGINE PARITY VERIFIED: all specimens match across gate.py and app.html rules.")
    return 0


if __name__ == "__main__":
    sys.exit(test_parity())
