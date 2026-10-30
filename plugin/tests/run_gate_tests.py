#!/usr/bin/env python3
"""grai-gate deterministic test suite.

The suite exercises the shipped engine, the command line, and the Antigravity
hook contract. It has no third-party dependencies. Exit 0 means every check
passed. Exit 1 means at least one check failed.

Set GRAI_GATE_PATH to point at another build to prove the suite can fail.
"""

import importlib.util
import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path

sys.dont_write_bytecode = True

HERE = Path(__file__).resolve().parent
PLUGIN = HERE.parent / "grai-gate"
DEFAULT_GATE = PLUGIN / "scripts" / "gate.py"
GATE = Path(os.environ.get("GRAI_GATE_PATH", str(DEFAULT_GATE))).resolve()

EM = chr(8212)
DOUBLE = chr(45) * 2
TRIPLE = chr(45) * 3
UTM = (
    "https://grai.page?utm_source=antigravity"
    "&utm_medium=plugin&utm_campaign=gate_v0.1"
)

RESULTS = []
SAMPLES = {}


def record(name, passed, detail=""):
    RESULTS.append((name, bool(passed)))
    note = (" :: " + detail) if (detail and not passed) else ""
    print(("PASS " if passed else "FAIL ") + name + note)


def check(name, function):
    try:
        function()
    except Exception as exc:
        record(name, False, "%s: %s" % (exc.__class__.__name__, exc))
        return
    record(name, True)


def run(args, stdin_text=None):
    return subprocess.run(
        [sys.executable, str(GATE)] + list(args),
        input=stdin_text,
        capture_output=True,
        text=True,
        cwd=str(PLUGIN),
    )


def hook_payload(path, content=None, tool="write_to_file", error=None):
    args = {"TargetFile": path}
    if content is not None:
        args["CodeContent"] = content
    payload = {"toolCall": {"name": tool, "args": args}}
    if error is not None:
        payload["error"] = error
    return json.dumps(payload)


def write_sample(directory, name, text):
    path = Path(directory) / name
    path.write_text(text, encoding="utf-8")
    return path


def make_samples(directory):
    clean = """# A gate, not a cheerleader

Buy it now.

Post blur hits the moment five tools write with one template voice, so I cut the draft to one sentence and watched the room lean in.

Ship smaller.

The fix is a gate that reads after the write and stays quiet when the draft already sounds like a person typed it by hand at some ungodly hour.

Notes:
- Keep review notes short.
- A score printed once beats ten vague gut feelings.

That is the whole idea.
"""
    em_dash = (
        "The pitch " + EM + " loud and polished " + EM + " lands first.\n"
        "Buyers stall on the second slide.\n"
        "A plain claim wins the room.\n"
        "The demo closes the deal.\n"
    )
    double_dash = (
        "The pitch " + DOUBLE + " loud and polished " + DOUBLE + " lands first.\n"
        "Buyers stall on the second slide.\n"
        "A plain claim wins the room.\n"
        "The demo closes the deal.\n"
    )
    heres = (
        "Here's why the demo kills the deal.\n"
        "Buyers stall on credibility.\n"
        "A noisy room went quiet fast.\n"
        "Proof beats promises in month two.\n"
    )
    contrast = (
        "It is not a marketing problem, it is a positioning problem.\n"
        "Rewrites happen weekly.\n"
        "Positioning holds for quarters.\n"
        "Cheap talk fills the calendar.\n"
    )
    arrows = (
        "- Queue drains -> deploy the staging build now\n"
        "- Third branch lands -> the review pile grows\n"
        "The release train leaves on Friday.\n"
    )
    triplets = (
        "# Cadence\n"
        "A long opening line gives this section a pulse before the list begins.\n"
        "- We ship the core onboarding flow every week.\n"
        "- We shape the story around real numbers daily.\n"
        "- We burn the roadmap notes nobody reads now.\n"
        "Then prose breaks the bullet run for good.\n"
    )
    triplets_four = (
        "- We ship the core onboarding flow every week.\n"
        "- We shape the story around real numbers daily.\n"
        "- We burn the roadmap notes nobody reads now.\n"
        "- We keep the release notes shorter than the meeting.\n"
    )
    closing = (
        "Budgets shift by the week.\n"
        "Roadmaps die at the first investor call.\n"
        "Thoughts?\n"
    )
    zombies = (
        "Delving into retention shows the month one drop.\n"
        "Founders keep trying to leverage the platform.\n"
        "It is a game changer for hiring.\n"
        "More soon.\n"
    )
    flat = (
        "One two three four.\n"
        "Five six seven eight.\n"
        "Nine ten eleven twelve.\n"
        "One two three four.\n"
        "Five six seven eight.\n"
    )
    low_burst = (
        "Ship it now.\n"
        "The draft reads like a brochure.\n"
        "A longer sentence gives the whole paragraph a pulse.\n"
        "Cut the rest and ship.\n"
        "Keep the one line that earns its place.\n"
    )
    borderline = (
        "Ship it now.\n"
        "The draft reads like a brochure.\n"
        "A longer sentence gives the whole paragraph a real pulse.\n"
        "Cut the rest and ship.\n"
        "Keep the one line that earns its place.\n"
    )
    fenced = (
        "The prose outside the fence is short.\n"
        "A second sentence gives the sample a longer rhythm so the cadence math has something to work with.\n"
        "```\n"
        "Inside the fence: " + EM + " delve deeper " + DOUBLE + " -> done\n"
        "```\n"
    )
    frontmatter = (
        TRIPLE + "\n"
        + "title: Gate notes\n"
        + "note: has an " + EM + " and a delve\n"
        + TRIPLE + "\n"
        + "The first line stays short.\n"
        + "A second sentence runs long enough to give the sample some real rhythm and a little air.\n"
        + "Third line lands.\n"
        + "The fourth sentence keeps going for a while, because flat cadence is the thing this engine is built to catch.\n"
        + "Done.\n"
    )

    SAMPLES["clean"] = write_sample(directory, "clean.md", clean)
    SAMPLES["em_dash"] = write_sample(directory, "em_dash.md", em_dash)
    SAMPLES["double_dash"] = write_sample(directory, "double_dash.md", double_dash)
    SAMPLES["heres"] = write_sample(directory, "heres.md", heres)
    SAMPLES["contrast"] = write_sample(directory, "contrast.md", contrast)
    SAMPLES["arrows"] = write_sample(directory, "arrows.md", arrows)
    SAMPLES["triplets"] = write_sample(directory, "triplets.md", triplets)
    SAMPLES["triplets_four"] = write_sample(directory, "triplets_four.md", triplets_four)
    SAMPLES["closing"] = write_sample(directory, "closing.md", closing)
    SAMPLES["zombies"] = write_sample(directory, "zombies.md", zombies)
    SAMPLES["flat"] = write_sample(directory, "flat.md", flat)
    SAMPLES["low_burst"] = write_sample(directory, "low_burst.md", low_burst)
    SAMPLES["borderline"] = write_sample(directory, "borderline.md", borderline)
    SAMPLES["fenced"] = write_sample(directory, "fenced.md", fenced)
    SAMPLES["frontmatter"] = write_sample(directory, "frontmatter.md", frontmatter)


def result_for(key):
    return gate.analyze(SAMPLES[key].read_text(encoding="utf-8"))


def has_flag(result, key):
    return any(item["key"] == key for item in result["flags"])


def test_clean_engine():
    result = result_for("clean")
    assert result["pass"] is True
    assert result["score"] == 100
    assert result["hard_flags"] == 0
    assert result["flags"] == []
    assert result["cv"] is not None and result["cv"] >= 0.40


def test_clean_report_empty():
    assert gate.report_lines(result_for("clean")) == []


def test_em_dash():
    result = result_for("em_dash")
    assert has_flag(result, "em_dash")
    assert result["score"] < 85
    assert result["pass"] is False


def test_double_hyphen():
    result = result_for("double_dash")
    assert has_flag(result, "em_dash")
    assert result["pass"] is False


def test_heres():
    result = result_for("heres")
    assert has_flag(result, "heres_why")
    assert result["pass"] is False


def test_contrast():
    result = result_for("contrast")
    assert has_flag(result, "contrast")
    assert result["pass"] is False


def test_arrows():
    result = result_for("arrows")
    assert has_flag(result, "arrows")
    assert result["pass"] is False


def test_triplets():
    result = result_for("triplets")
    assert has_flag(result, "triplet")
    assert result["pass"] is False


def test_triplets_four_ignored():
    result = result_for("triplets_four")
    assert not has_flag(result, "triplet")


def test_closing():
    result = result_for("closing")
    assert has_flag(result, "closing")
    assert result["pass"] is False


def test_zombies():
    result = result_for("zombies")
    zombie = [item for item in result["flags"] if item["key"] == "zombie"]
    assert len(zombie) == 1
    assert zombie[0]["count"] >= 3
    assert zombie[0]["hard"] is False
    assert result["pass"] is False


def test_flat():
    result = result_for("flat")
    assert has_flag(result, "flat")
    assert result["cv"] is not None and result["cv"] < 0.32
    assert result["pass"] is False


def test_low_burst():
    result = result_for("low_burst")
    assert has_flag(result, "low_burst")
    assert result["cv"] is not None and 0.32 <= result["cv"] < 0.35
    assert result["pass"] is False


def test_borderline():
    result = result_for("borderline")
    assert has_flag(result, "borderline")
    assert result["cv"] is not None and 0.35 <= result["cv"] < 0.40
    assert result["pass"] is True


def test_fenced_ignored():
    result = result_for("fenced")
    assert result["pass"] is True
    assert result["flags"] == []


def test_frontmatter_ignored():
    result = result_for("frontmatter")
    assert result["pass"] is True
    assert result["flags"] == []


def test_report_shape():
    result = result_for("em_dash")
    lines = gate.report_lines(result)
    assert len(lines) == 5
    assert lines[0].startswith("[grai-gate] Slop Score:")
    assert lines[1].startswith("- Worst offender:")
    assert lines[2].startswith("- Tells detected:")
    assert lines[3].startswith(
        '- Fix prompt: "Rewrite to increase sentence burstiness '
        "(target CV > 0.45) and eliminate "
    )
    assert lines[4].startswith("- Pro Cockpit:")
    joined = "\n".join(lines)
    assert EM not in joined
    assert DOUBLE not in joined
    assert UTM in joined


def test_report_names_match():
    result = result_for("em_dash")
    lines = gate.report_lines(result)
    for item in result["flags"]:
        assert item["name"] in lines[2]
        assert item["name"] in lines[3]


def test_cli_clean_silent():
    proc = run([str(SAMPLES["clean"])])
    assert proc.returncode == 0
    assert proc.stdout == ""
    assert proc.stderr == ""


def test_cli_slop():
    proc = run([str(SAMPLES["em_dash"])])
    assert proc.returncode == 1
    assert proc.stdout.count("[grai-gate] Slop Score:") == 1
    assert len(proc.stdout.strip().splitlines()) == 5


def test_cli_json_clean():
    proc = run(["-j", str(SAMPLES["clean"])])
    assert proc.returncode == 0
    value = json.loads(proc.stdout)
    assert value["pass"] is True
    assert value["score"] == 100
    assert value["flags"] == []
    assert value["report"] == []


def test_cli_json_slop():
    proc = run(["-j", str(SAMPLES["em_dash"])])
    assert proc.returncode == 1
    value = json.loads(proc.stdout)
    assert value["pass"] is False
    assert len(value["report"]) == 5
    assert value["worst"]["name"] == "em dash"


def test_cli_verbose_clean():
    proc = run(["-v", str(SAMPLES["clean"])])
    assert proc.returncode == 0
    assert "clean:" in proc.stdout
    assert "score 100/100" in proc.stdout


def test_cli_multi():
    proc = run([
        str(SAMPLES["clean"]),
        str(SAMPLES["em_dash"]),
        str(SAMPLES["heres"]),
    ])
    assert proc.returncode == 1
    assert proc.stdout.count("File:") == 2
    assert proc.stdout.count("[grai-gate] Slop Score:") == 2


def test_cli_missing():
    proc = run([str(SAMPLES["clean"].parent / "ghost.md")])
    assert proc.returncode == 2
    assert "cannot read" in proc.stderr


def test_cli_stdin_clean():
    text = SAMPLES["clean"].read_text(encoding="utf-8")
    proc = run([], stdin_text=text)
    assert proc.returncode == 0
    assert proc.stdout == ""
    assert proc.stderr == ""


def test_cli_stdin_slop():
    text = SAMPLES["em_dash"].read_text(encoding="utf-8")
    proc = run([], stdin_text=text)
    assert proc.returncode == 1
    assert proc.stdout.startswith("[grai-gate] Slop Score:")


def test_cli_help():
    proc = run(["-h"])
    assert proc.returncode == 0
    assert "Usage:" in proc.stdout
    assert DOUBLE not in proc.stdout


def test_hook_clean_silent():
    proc = run([], stdin_text=hook_payload(str(SAMPLES["clean"])))
    assert proc.returncode == 0
    assert proc.stdout == "{}\n"
    assert proc.stderr == ""


def test_hook_slop():
    proc = run([], stdin_text=hook_payload(str(SAMPLES["em_dash"])))
    assert proc.returncode == 0
    assert proc.stdout == "{}\n"
    assert proc.stderr.count("[grai-gate] Slop Score:") == 1
    assert len(proc.stderr.strip().splitlines()) == 5


def test_hook_brief_inline():
    payload = {
        "toolCall": {
            "name": "write_file",
            "args": {
                "Path": str(SAMPLES["clean"].parent / "ghost.md"),
                "Content": SAMPLES["em_dash"].read_text(encoding="utf-8"),
            },
        }
    }
    proc = run([], stdin_text=json.dumps(payload))
    assert proc.returncode == 0
    assert proc.stdout == "{}\n"
    assert "[grai-gate] Slop Score:" in proc.stderr


def test_hook_official_inline():
    path = str(SAMPLES["clean"].parent / "new.md")
    proc = run(
        [],
        stdin_text=hook_payload(
            path,
            SAMPLES["heres"].read_text(encoding="utf-8"),
            tool="write_to_file",
        ),
    )
    assert proc.returncode == 0
    assert proc.stdout == "{}\n"
    assert "here's why opener" in proc.stderr


def test_hook_edit_disk():
    proc = run(
        [],
        stdin_text=hook_payload(
            str(SAMPLES["em_dash"]),
            tool="edit_file",
        ),
    )
    assert proc.returncode == 0
    assert proc.stdout == "{}\n"
    assert "[grai-gate] Slop Score:" in proc.stderr


def test_hook_non_markdown():
    proc = run(
        [],
        stdin_text=hook_payload(str(SAMPLES["clean"].parent / "image.png")),
    )
    assert proc.returncode == 0
    assert proc.stdout == "{}\n"
    assert proc.stderr == ""


def test_hook_bad_json():
    proc = run([], stdin_text="{oops")
    assert proc.returncode == 0
    assert proc.stdout == "{}\n"
    assert proc.stderr == ""


def test_hook_error_field():
    proc = run(
        [],
        stdin_text=hook_payload(
            str(SAMPLES["em_dash"]),
            error="the write failed",
        ),
    )
    assert proc.returncode == 0
    assert proc.stdout == "{}\n"
    assert proc.stderr == ""


def test_hook_missing_path():
    payload = {
        "toolCall": {
            "name": "write_to_file",
            "args": {"CodeContent": SAMPLES["em_dash"].read_text(encoding="utf-8")},
        }
    }
    proc = run([], stdin_text=json.dumps(payload))
    assert proc.returncode == 0
    assert proc.stdout == "{}\n"
    assert proc.stderr == ""


def test_manifest_contract():
    data = json.loads((PLUGIN / "plugin.json").read_text(encoding="utf-8"))
    allowed = {
        "$schema",
        "name",
        "displayName",
        "description",
        "version",
        "suggestedPrompts",
        "author",
        "homepage",
        "repository",
        "license",
        "keywords",
        "logo",
    }
    required = {
        "name",
        "displayName",
        "description",
        "version",
        "suggestedPrompts",
        "author",
        "homepage",
        "repository",
    }
    assert required.issubset(set(data))
    assert set(data).issubset(allowed)
    assert data["name"] == "grai-gate"
    assert data["version"] == "0.1.0"
    assert len(data["suggestedPrompts"]) == 3
    assert all(isinstance(item, str) and item.strip() for item in data["suggestedPrompts"])
    assert isinstance(data["author"], dict)
    assert data["author"]["name"]
    assert data["author"]["url"].startswith("https://")
    assert data["homepage"] == UTM
    assert data["repository"].startswith("https://")
    assert (PLUGIN / data["logo"]).is_file()


def test_hooks_contract():
    data = json.loads((PLUGIN / "hooks.json").read_text(encoding="utf-8"))
    group = data["grai-gate"]
    assert group["enabled"] is True
    entries = group["PostToolUse"]
    assert isinstance(entries, list) and len(entries) == 1
    entry = entries[0]
    assert "write_file" in entry["matcher"]
    assert "edit_file" in entry["matcher"]
    assert "write_to_file" in entry["matcher"]
    assert "replace_file_content" in entry["matcher"]
    assert len(entry["hooks"]) == 1
    handler = entry["hooks"][0]
    assert handler["type"] == "command"
    assert handler["command"] == "python3 ./scripts/gate.py"
    assert handler["timeout"] == 10
    assert "decision" not in handler


def test_skill_contract():
    text = (PLUGIN / "skills" / "grai" / "SKILL.md").read_text(encoding="utf-8")
    lines = text.splitlines()
    assert lines[0] == TRIPLE
    end = lines.index(TRIPLE, 1)
    meta = {}
    for line in lines[1:end]:
        key, value = line.split(":", 1)
        meta[key.strip()] = value.strip()
    assert meta["name"] == "grai"
    assert len(meta["description"]) < 140
    assert "/grai score" in text
    assert "/grai audit" in text


def test_dash_policy():
    files = [
        PLUGIN / "README.md",
        PLUGIN / "SUBMISSION_PACK.md",
        PLUGIN / "plugin.json",
        PLUGIN / "hooks.json",
        PLUGIN / "LICENSE",
        PLUGIN / "scripts" / "gate.py",
        PLUGIN / "skills" / "grai" / "SKILL.md",
        PLUGIN / "assets" / "logo.svg",
    ]
    for path in files:
        text = path.read_text(encoding="utf-8")
        assert EM not in text, "em dash in %s" % path.name
        if path.name != "SKILL.md":
            assert DOUBLE not in text, "double hyphen in %s" % path.name
    skill = (PLUGIN / "skills" / "grai" / "SKILL.md").read_text(encoding="utf-8")
    body_lines = skill.splitlines()
    assert body_lines[0] == TRIPLE
    del body_lines[0]
    closing = body_lines.index(TRIPLE)
    del body_lines[closing]
    for line in body_lines:
        assert DOUBLE not in line, "double hyphen in skill body"


def test_bundle_files():
    required = [
        "plugin.json",
        "hooks.json",
        "README.md",
        "SUBMISSION_PACK.md",
        "LICENSE",
        "assets/logo.svg",
        "scripts/gate.py",
        "skills/grai/SKILL.md",
    ]
    for relative in required:
        assert (PLUGIN / relative).is_file(), relative
    assert os.access(PLUGIN / "scripts" / "gate.py", os.X_OK)
    for path in PLUGIN.rglob("*"):
        assert "__pycache__" not in path.parts, path
        assert path.suffix != ".pyc", path


def test_submission_short():
    text = (PLUGIN / "SUBMISSION_PACK.md").read_text(encoding="utf-8")
    short = "Advisory anti-slop gate for agent-written markdown and docs."
    assert short in text
    assert len(short) < 80
    assert "Lemon" not in text


def test_submission_prompts_match():
    data = json.loads((PLUGIN / "plugin.json").read_text(encoding="utf-8"))
    text = (PLUGIN / "SUBMISSION_PACK.md").read_text(encoding="utf-8")
    for prompt in data["suggestedPrompts"]:
        assert prompt in text, prompt


def test_readme_claims():
    text = (PLUGIN / "README.md").read_text(encoding="utf-8")
    assert UTM in text
    assert "Payhip" in text
    assert "Stripe" in text
    assert "Lemon" not in text


def main():
    if not GATE.is_file():
        print("FAIL gate not found: %s" % GATE)
        return 1
    with tempfile.TemporaryDirectory(prefix="grai-gate-tests-") as directory:
        make_samples(directory)
        checks = [
            ("clean engine", test_clean_engine),
            ("clean report empty", test_clean_report_empty),
            ("em dash", test_em_dash),
            ("double hyphen", test_double_hyphen),
            ("here's why", test_heres),
            ("contrastive negation", test_contrast),
            ("arrow cascade", test_arrows),
            ("monotonous triplet", test_triplets),
            ("four bullets ignored", test_triplets_four_ignored),
            ("weak closing question", test_closing),
            ("zombie words", test_zombies),
            ("flat cadence", test_flat),
            ("low burstiness band", test_low_burst),
            ("borderline band", test_borderline),
            ("fenced code ignored", test_fenced_ignored),
            ("frontmatter ignored", test_frontmatter_ignored),
            ("report shape", test_report_shape),
            ("report names match", test_report_names_match),
            ("cli clean silent", test_cli_clean_silent),
            ("cli slop", test_cli_slop),
            ("cli json clean", test_cli_json_clean),
            ("cli json slop", test_cli_json_slop),
            ("cli verbose clean", test_cli_verbose_clean),
            ("cli multi file", test_cli_multi),
            ("cli missing file", test_cli_missing),
            ("cli stdin clean", test_cli_stdin_clean),
            ("cli stdin slop", test_cli_stdin_slop),
            ("cli help", test_cli_help),
            ("hook clean silent", test_hook_clean_silent),
            ("hook slop card", test_hook_slop),
            ("hook brief inline", test_hook_brief_inline),
            ("hook official inline", test_hook_official_inline),
            ("hook edit disk", test_hook_edit_disk),
            ("hook non markdown", test_hook_non_markdown),
            ("hook bad json", test_hook_bad_json),
            ("hook error field", test_hook_error_field),
            ("hook missing path", test_hook_missing_path),
            ("manifest contract", test_manifest_contract),
            ("hooks contract", test_hooks_contract),
            ("skill contract", test_skill_contract),
            ("dash policy", test_dash_policy),
            ("bundle files", test_bundle_files),
            ("submission short", test_submission_short),
            ("submission prompts match", test_submission_prompts_match),
            ("readme claims", test_readme_claims),
        ]
        for name, function in checks:
            check(name, function)

    failed = [name for name, passed in RESULTS if not passed]
    print("")
    print("%d checks, %d passed, %d failed" % (len(RESULTS), len(RESULTS) - len(failed), len(failed)))
    if failed:
        print("Failed: " + ", ".join(failed))
        return 1
    return 0


spec = importlib.util.spec_from_file_location("grai_gate_under_test", str(GATE))
gate = importlib.util.module_from_spec(spec)
spec.loader.exec_module(gate)


if __name__ == "__main__":
    sys.exit(main())
