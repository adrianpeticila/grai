#!/usr/bin/env python3
"""grai-gate: an advisory anti-slop linter for markdown and text.

The engine is deliberately small and deterministic. It uses only the Python
standard library modules re, sys, json, and math. It never calls the network,
never writes a file, and never asks a model for an opinion.

Two runtimes share one analyzer:

CLI:   python3 gate.py FILE [FILE ...]
       Clean files stay silent by default. A failing file prints a fixed
       report card to stdout. Use -j for JSON or -v for a clean line.

HOOK:  Antigravity sends a PostToolUse payload on stdin. The required JSON
       response goes to stdout. A failing file prints the card to stderr.
       Clean files, skipped files, and bad payloads stay completely silent.
       The hook always exits 0 and never denies a tool call.

Thresholds come from a 134,522 post study of 1,499 founder profiles,
January 2023 to September 2026. Human drafts keep a sentence-length
coefficient of variation at or above 0.40. Flat AI drafts land under 0.32.
A warning band starts at 0.35. The repair target is 0.45.
"""

import json
import math
import re
import sys

VERSION = "0.1.0"
UTM_URL = (
    "https://grai.page?utm_source=antigravity"
    "&utm_medium=plugin&utm_campaign=gate_v0.1"
)

PASS_SCORE = 85
CV_FLAT = 0.32
CV_WARN = 0.35
CV_HUMAN = 0.40
CV_TARGET = 0.45
CV_MIN_SENTENCES = 4
CV_MIN_MEAN = 4.0
MAX_CHARS = 2000000
MAX_SENTENCES = 6000

EM_DASH = "\u2014"
EN_DASH = "\u2013"
SENTINEL = "\u0001"
HYPHEN = chr(45)
DOUBLE_HYPHEN = HYPHEN * 2
TRIPLE_HYPHEN = HYPHEN * 3
BACKTICK = chr(96)
FENCE3 = BACKTICK * 3
TILDE3 = "~" * 3

TARGET_SUFFIXES = (".md", ".txt")
ARROWS = ("->", "=>", "\u2192", "\u21b3", "\u2794")

RE_HTML_COMMENT = re.compile(
    r"(?s)<!" + re.escape(DOUBLE_HYPHEN) + r".*?"
    + re.escape(DOUBLE_HYPHEN) + r">"
)
RE_HR = re.compile(r"(?m)^[ \t]*([-*_])(?:[ \t]*\1){2,}[ \t]*$")
RE_SETEXT = re.compile(r"(?m)^[ \t]*={3,}[ \t]*$")
RE_TABLE_SEP = re.compile(
    r"(?m)^[ \t]*\|?[ \t]*:?-{3,}:?[ \t]*"
    r"(?:\|[ \t]*:?-{3,}:?[ \t]*)+\|?[ \t]*$"
)
RE_REF_DEF = re.compile(r"(?m)^[ \t]*\[[^\]\n]{1,120}\]:[ \t]*\S[^\n]*$")
RE_HEADING = re.compile(r"^[ \t]*#{1,6}(?:[ \t]+(.*)|[ \t]*)$")
RE_BULLET = re.compile(r"^[ \t]*[-*+][ \t]+(.*)$")
RE_NUMBERED = re.compile(r"^[ \t]*\d{1,3}[.)][ \t]+(.*)$")
RE_QUOTE = re.compile(r"^[ \t]*>+[ \t]?(.*)$")
RE_TABLE_ROW = re.compile(r"^[ \t]*\|.*\|[ \t]*$")

RE_IMAGE = re.compile(r"!\[[^\]\n]{0,300}\]\([^)\n]{0,600}\)")
RE_LINK = re.compile(r"\[([^\]\n]{1,300})\]\([^)\n]{0,600}\)")
RE_AUTOLINK = re.compile(r"<https?://[^>\s]+>")
RE_HTML_TAG = re.compile(r"</?[A-Za-z][^>]{0,500}>")
RE_INLINE_CODE = re.compile(r"`+[^`\n]*`+")
RE_URL = re.compile(r"(?i)\b(?:https?://|www\.)[^\s<>()\[\]]+")
RE_WS = re.compile(r"[ \t]+")

RE_EM_DASH = re.compile(EM_DASH)
RE_DOUBLE_HYPHEN = re.compile(r"\x2d{2,}")
RE_SENT_SPLIT = re.compile(r"(?<=[.!?])\s+")
RE_ABBREV = re.compile(
    r"(?i)\b(?:e\.g|i\.e|etc|vs|mr|mrs|ms|dr|prof|inc|ltd|no|fig|approx|"
    r"u\.s|u\.k|et\s+al)\.(?=\s|$)"
)
RE_TOKEN = re.compile(r"[^\W_]+(?:['\u2019-][^\W_]+)*", re.UNICODE)

RE_HERES = re.compile(
    r"(?i)^[\s\"'(\[\u2018\u201c]*(?:here(?:['\u2019]?s|\s+is)\s+why)\b"
)
RE_WEAK_CLOSING = re.compile(
    r"(?i)\b(?:"
    r"thoughts|any\s+thoughts|your\s+thoughts|"
    r"what\s+do\s+you\s+think|what\s+do\s+you\s+all\s+think|"
    r"what\s+do\s+you\s+guys\s+think|"
    r"what(?:['\u2019]s|\s+is)\s+your\s+take|"
    r"agree\s+or\s+disagree|agree|right|"
    r"sound\s+familiar|who(?:['\u2019]s|\s+is)\s+with\s+me|"
    r"am\s+i\s+(?:wrong|missing\s+anything)|"
    r"curious\s+(?:what\s+you\s+think|to\s+hear)"
    r")\??$"
)

_CONTRAST_SUBJECT = r"(?:it|this|that)"
_CONTRAST_IS = r"(?:['\u2019]s|\s+is|\s+was|\s+are|\s+were)"
RE_CONTRAST = re.compile(
    r"(?i)(?:"
    r"\b" + _CONTRAST_SUBJECT + _CONTRAST_IS + r"\s+not\s+"
    r"(?:just\s+|only\s+|merely\s+|really\s+|about\s+)?"
    r"[^.!?\n]{1,90}?[;,]?\s*"
    + _CONTRAST_SUBJECT + _CONTRAST_IS + r"\s+(?:about\s+)?[^.!?\n]{1,90}"
    r"|\b" + _CONTRAST_SUBJECT + _CONTRAST_IS + r"\s+not\s+about\s+"
    r"[^.!?\n]{1,90}?,\s*but\s+[^.!?\n]{1,90}"
    r"|\bnot\s+(?:just|only|merely)\s+"
    r"[^.!?\n]{1,80}?,?\s*but\s+(?:also\s+)?[^.!?\n]{1,80}"
    r"|\b" + _CONTRAST_SUBJECT + _CONTRAST_IS + r"\s+not\s+"
    r"[^.!?\n]{1,90}\.\s+"
    + _CONTRAST_SUBJECT + _CONTRAST_IS + r"\s+(?:about\s+)?[^.!?\n]{1,90}"
    r")"
)

ZOMBIE_PATTERNS = (
    r"delv\w*",
    r"leverag\w*",
    r"game[\s-]?chang\w*",
    r"tapestry",
    r"testament\s+to",
    r"in\s+today(?:['\u2019]s)?\s+fast[\s-]?paced\s+world",
    r"(?:excited|thrilled|humbled|proud)\s+to\s+announce",
    r"seamless(?:ly)?",
    r"dive\s+into",
    r"deep\s+dive",
    r"synerg\w*",
    r"cutting[\s-]?edge",
    r"revolutioniz\w*",
    r"unlock(?:ing|ed|s)?\s+(?:the\s+)?(?:full\s+)?potential",
    r"paradigm\s+shift",
    r"it(?:['\u2019]s|\s+is)\s+worth\s+noting",
    r"at\s+the\s+end\s+of\s+the\s+day",
    r"when\s+it\s+comes\s+to",
    r"ever[\s-]?evolving",
    r"holistic",
    r"actionable",
    r"impactful",
    r"learnings",
    r"best[\s-]?in[\s-]?class",
    r"world[\s-]?class",
    r"next[\s-]?generation",
    r"state[\s-]?of[\s-]?the[\s-]?art",
    r"moreover",
    r"furthermore",
    r"pivotal",
    r"foster\w*",
    r"underscor\w*",
    r"elevat(?:e|es|ed|ing)",
    r"unleash\w*",
    r"transformative",
    r"navigate\s+the\s+(?:complexities|landscape)",
    r"in\s+the\s+realm\s+of",
    r"rapidly\s+(?:changing|evolving)",
)
RE_ZOMBIE = re.compile(
    r"\b(?:" + "|".join(ZOMBIE_PATTERNS) + r")\b",
    re.IGNORECASE,
)

FLAG_ORDER = {
    "flat": 0,
    "low_burst": 1,
    "borderline": 2,
    "em_dash": 3,
    "heres_why": 4,
    "contrast": 5,
    "arrows": 6,
    "triplet": 7,
    "closing": 8,
    "zombie": 9,
}


def _configure_streams():
    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(errors="replace")
        except (AttributeError, ValueError):
            pass


def _clean_line(text):
    if not text:
        return ""
    text = RE_IMAGE.sub(" ", text)
    text = RE_LINK.sub(lambda match: match.group(1), text)
    text = RE_AUTOLINK.sub(" ", text)
    text = RE_HTML_TAG.sub(" ", text)
    text = RE_INLINE_CODE.sub(" ", text)
    text = RE_URL.sub(" ", text)
    text = text.replace("**", "").replace("__", "")
    text = re.sub(r"\*([^*]+)\*", r"\1", text)
    text = re.sub(r"(?<!\w)_([^_]+)_(?!\w)", r"\1", text)
    text = text.replace("`", " ")
    text = RE_WS.sub(" ", text).strip()
    return text


def _drop_frontmatter(lines):
    if not lines or lines[0].strip() != TRIPLE_HYPHEN:
        return lines
    for index in range(1, min(len(lines), 500)):
        if lines[index].strip() == TRIPLE_HYPHEN:
            return lines[index + 1:]
    return lines


def _parse_blocks(text):
    text = text.replace("\r\n", "\n").replace("\r", "\n").lstrip("\ufeff")
    text = RE_HTML_COMMENT.sub(" ", text)
    lines = _drop_frontmatter(text.split("\n"))
    blocks = []
    paragraph = []
    fence = None

    def flush_paragraph():
        if paragraph:
            body = _clean_line(" ".join(paragraph))
            if body:
                blocks.append({"kind": "prose", "text": body})
            del paragraph[:]

    for line in lines:
        stripped = line.strip()
        if fence is not None:
            if stripped.startswith(fence):
                fence = None
            continue
        if stripped.startswith(FENCE3):
            flush_paragraph()
            fence = FENCE3
            continue
        if stripped.startswith(TILDE3):
            flush_paragraph()
            fence = TILDE3
            continue
        if not stripped:
            flush_paragraph()
            continue
        if RE_HR.match(line) or RE_SETEXT.match(line) or RE_TABLE_SEP.match(line):
            flush_paragraph()
            continue
        if RE_REF_DEF.match(line):
            flush_paragraph()
            continue

        match = RE_HEADING.match(line)
        if match:
            flush_paragraph()
            heading = (match.group(1) or "").strip()
            heading = re.sub(r"[ \t]+#+[ \t]*$", "", heading)
            heading = _clean_line(heading)
            if heading:
                blocks.append({"kind": "heading", "text": heading})
            continue

        match = RE_BULLET.match(line)
        if match:
            flush_paragraph()
            body = _clean_line(match.group(1))
            if body:
                blocks.append({"kind": "bullet", "text": body})
            continue

        match = RE_NUMBERED.match(line)
        if match:
            flush_paragraph()
            body = _clean_line(match.group(1))
            if body:
                blocks.append({"kind": "bullet", "text": body})
            continue

        match = RE_QUOTE.match(line)
        if match:
            flush_paragraph()
            body = _clean_line(match.group(1))
            if body:
                blocks.append({"kind": "quote", "text": body})
            continue

        if RE_TABLE_ROW.match(line):
            flush_paragraph()
            body = _clean_line(line.strip(" \t|").replace("|", " "))
            if body:
                blocks.append({"kind": "table", "text": body})
            continue

        paragraph.append(line)

    flush_paragraph()
    return blocks


def _split_sentences(text):
    if not text:
        return []
    text = text.replace("...", ".")
    protected = RE_ABBREV.sub(
        lambda match: match.group(0).replace(".", SENTINEL),
        text,
    )
    sentences = []
    for part in RE_SENT_SPLIT.split(protected):
        part = part.replace(SENTINEL, ".").strip()
        if part:
            sentences.append(part)
    return sentences


def _token_count(text):
    if not text:
        return 0
    return len(RE_TOKEN.findall(text))


def _sanitize_quote(text, limit=64):
    if not text:
        return ""
    out = text.replace(EM_DASH, " - ").replace(EN_DASH, "-")
    out = RE_DOUBLE_HYPHEN.sub("-", out)
    out = out.replace("\u2018", "'").replace("\u2019", "'")
    out = out.replace("\u201c", "'").replace("\u201d", "'")
    out = out.replace('"', "'").replace("`", "'")
    out = " ".join(out.split())
    if len(out) > limit:
        cut = out[:limit].rstrip()
        if " " in cut:
            cut = cut.rsplit(" ", 1)[0]
        out = cut.rstrip(" -:;,") + "..."
    return out.strip(" \t\r\n")


def _context(text, start, before=30, after=40):
    low = max(0, start - before)
    high = min(len(text), start + after)
    if low > 0:
        space = text.find(" ", low, start)
        if space != -1:
            low = space + 1
    if high < len(text):
        space = text.rfind(" ", start, high)
        if space != -1:
            high = space
    return _sanitize_quote(text[low:high])


def _flag(key, name, count, penalty, hard, quote):
    return {
        "key": key,
        "name": name,
        "count": int(count),
        "penalty": int(penalty),
        "hard": bool(hard),
        "quote": _sanitize_quote(quote),
    }


def analyze(text):
    """Score one markdown or text document and return a result dictionary."""
    blocks = _parse_blocks(text)
    scan_text = "\n".join(block["text"] for block in blocks)
    flags = []

    em_hits = list(RE_EM_DASH.finditer(scan_text))
    em_hits.extend(RE_DOUBLE_HYPHEN.finditer(scan_text))
    em_hits.sort(key=lambda match: match.start())
    if em_hits:
        count = len(em_hits)
        flags.append(_flag(
            "em_dash",
            "em dash",
            count,
            18 * min(count, 3),
            True,
            _context(scan_text, em_hits[0].start()),
        ))

    here_units = []
    for block in blocks:
        if block["kind"] == "heading":
            if RE_HERES.match(block["text"]):
                here_units.append(block["text"])
        else:
            for sentence in _split_sentences(block["text"]):
                if RE_HERES.match(sentence):
                    here_units.append(sentence)
    if here_units:
        flags.append(_flag(
            "heres_why",
            "here's why opener",
            len(here_units),
            12 * min(len(here_units), 2),
            True,
            here_units[0],
        ))

    contrast_hits = [match.group(0) for match in RE_CONTRAST.finditer(scan_text)]
    if contrast_hits:
        flags.append(_flag(
            "contrast",
            "contrastive negation",
            len(contrast_hits),
            14 * min(len(contrast_hits), 2),
            True,
            contrast_hits[0],
        ))

    arrow_lines = []
    arrow_total = 0
    for block in blocks:
        if block["kind"] == "bullet":
            count = sum(block["text"].count(arrow) for arrow in ARROWS)
            if count:
                arrow_lines.append(block["text"])
                arrow_total += count
        elif block["kind"] in ("prose", "quote"):
            first = block["text"].lstrip()
            if any(first.startswith(arrow) for arrow in ARROWS):
                count = sum(block["text"].count(arrow) for arrow in ARROWS)
                if count:
                    arrow_lines.append(block["text"])
                    arrow_total += count
    if arrow_total >= 2:
        flags.append(_flag(
            "arrows",
            "arrow cascade",
            arrow_total,
            12 + 4 * min(arrow_total - 2, 2),
            True,
            arrow_lines[0],
        ))

    triplets = []
    index = 0
    while index < len(blocks):
        if blocks[index]["kind"] != "bullet":
            index += 1
            continue
        end = index
        while end < len(blocks) and blocks[end]["kind"] == "bullet":
            end += 1
        group = blocks[index:end]
        if len(group) == 3:
            single_sentence = True
            for item in group:
                if len(_split_sentences(item["text"])) > 1:
                    single_sentence = False
                    break
            if single_sentence:
                lengths = [_token_count(item["text"]) for item in group]
                if min(lengths) >= 4 and max(lengths) - min(lengths) <= 2:
                    triplets.append(lengths)
        index = end
    if triplets:
        lengths = triplets[0]
        flags.append(_flag(
            "triplet",
            "monotonous triplet",
            len(triplets),
            10 * min(len(triplets), 2),
            True,
            "%d, %d, %d words" % (lengths[0], lengths[1], lengths[2]),
        ))

    last_sentence = ""
    for block in reversed(blocks):
        if block["kind"] in ("prose", "bullet", "quote"):
            sentences = _split_sentences(block["text"])
            if sentences:
                last_sentence = sentences[-1].strip()
                break
    if last_sentence.endswith("?") and RE_WEAK_CLOSING.search(last_sentence):
        flags.append(_flag(
            "closing",
            "weak closing question",
            1,
            12,
            True,
            last_sentence,
        ))

    zombie_hits = list(RE_ZOMBIE.finditer(scan_text))
    if zombie_hits:
        examples = []
        seen = set()
        for match in zombie_hits:
            word = match.group(0).strip().lower()
            if word and word not in seen:
                seen.add(word)
                examples.append(word)
        count = len(zombie_hits)
        zombie_flag = _flag(
            "zombie",
            "zombie words",
            count,
            8 * min(count, 4),
            False,
            _context(scan_text, zombie_hits[0].start()),
        )
        zombie_flag["examples"] = examples[:4]
        flags.append(zombie_flag)

    sentence_lengths = []
    for block in blocks:
        if block["kind"] in ("prose", "bullet", "quote"):
            for sentence in _split_sentences(block["text"]):
                length = _token_count(sentence)
                if length >= 2 and len(sentence_lengths) < MAX_SENTENCES:
                    sentence_lengths.append(length)
    sentence_count = len(sentence_lengths)
    cv = None
    if sentence_count >= CV_MIN_SENTENCES:
        mean = sum(sentence_lengths) / float(sentence_count)
        if mean >= CV_MIN_MEAN:
            variance = (
                sum((length - mean) ** 2 for length in sentence_lengths)
                / float(sentence_count)
            )
            sigma = math.sqrt(variance)
            cv = sigma / mean
            if cv < CV_FLAT:
                flags.append(_flag(
                    "flat",
                    "flat cadence",
                    1,
                    20,
                    True,
                    "CV %.2f across %d sentences" % (cv, sentence_count),
                ))
            elif cv < CV_WARN:
                flags.append(_flag(
                    "low_burst",
                    "low burstiness",
                    1,
                    14,
                    True,
                    "CV %.2f across %d sentences" % (cv, sentence_count),
                ))
            elif cv < CV_HUMAN:
                flags.append(_flag(
                    "borderline",
                    "borderline cadence",
                    1,
                    3,
                    False,
                    "CV %.2f across %d sentences" % (cv, sentence_count),
                ))

    flags.sort(key=lambda item: (-item["penalty"], FLAG_ORDER.get(item["key"], 99)))
    penalty = sum(item["penalty"] for item in flags)
    score = max(0, min(100, 100 - penalty))
    hard_flags = sum(1 for item in flags if item["hard"])
    return {
        "score": score,
        "cv": cv,
        "sentences": sentence_count,
        "flags": flags,
        "hard_flags": hard_flags,
        "pass": bool(score >= PASS_SCORE and hard_flags == 0),
        "worst": flags[0] if flags else None,
    }


def report_lines(result):
    """Return the fixed report card for a failing result. A pass returns []."""
    if result["pass"]:
        return []
    flags = result["flags"]
    cv_text = "n/a" if result["cv"] is None else "%.2f" % result["cv"]
    lines = [
        "[grai-gate] Slop Score: %d/100 (CV: %s | Flags: %d)"
        % (result["score"], cv_text, len(flags))
    ]

    worst = result["worst"]
    if worst:
        if worst["quote"]:
            lines.append(
                '- Worst offender: %s ("%s")' % (worst["name"], worst["quote"])
            )
        else:
            lines.append("- Worst offender: %s" % worst["name"])
    else:
        lines.append("- Worst offender: none")

    tells = []
    for item in flags:
        label = item["name"]
        if item["count"] > 1:
            label += " (x%d)" % item["count"]
        tells.append(label)
    lines.append("- Tells detected: %s" % (", ".join(tells) if tells else "none"))

    fix_names = []
    for item in flags:
        if item["name"] not in fix_names:
            fix_names.append(item["name"])
    fix_text = ", ".join(fix_names) if fix_names else "the flagged patterns"
    lines.append(
        '- Fix prompt: "Rewrite to increase sentence burstiness '
        '(target CV > %.2f) and eliminate %s."' % (CV_TARGET, fix_text)
    )
    lines.append(
        "- Pro Cockpit: Full Voice DNA & repair workbench at %s" % UTM_URL
    )
    return lines


def _json_result(label, result):
    flags = []
    for item in result["flags"]:
        entry = {
            "key": item["key"],
            "name": item["name"],
            "count": item["count"],
            "penalty": item["penalty"],
            "hard": item["hard"],
            "quote": item["quote"],
        }
        if item.get("examples"):
            entry["examples"] = item["examples"]
        flags.append(entry)
    worst = None
    if result["worst"]:
        worst = {
            "key": result["worst"]["key"],
            "name": result["worst"]["name"],
            "quote": result["worst"]["quote"],
            "penalty": result["worst"]["penalty"],
        }
    return {
        "file": label,
        "score": result["score"],
        "cv": None if result["cv"] is None else round(result["cv"], 4),
        "sentences": result["sentences"],
        "flags": flags,
        "hard_flags": result["hard_flags"],
        "pass": result["pass"],
        "worst": worst,
        "report": report_lines(result),
    }


def _clean_summary(label, result):
    cv_text = "n/a" if result["cv"] is None else "%.2f" % result["cv"]
    names = ", ".join(item["name"] for item in result["flags"])
    if names:
        return (
            "[grai-gate] clean: %s (score %d/100, CV %s, soft flags: %s)"
            % (label, result["score"], cv_text, names)
        )
    return (
        "[grai-gate] clean: %s (score %d/100, CV %s, 0 flags)"
        % (label, result["score"], cv_text)
    )


def _read_path(path, workspaces):
    candidates = [path]
    if not _is_absolute(path) and isinstance(workspaces, list):
        for workspace in workspaces:
            if isinstance(workspace, str) and workspace:
                candidates.append(workspace.rstrip("/\\") + "/" + path)
    for candidate in candidates:
        try:
            with open(candidate, "r", encoding="utf-8", errors="replace") as handle:
                data = handle.read(MAX_CHARS + 1)
        except (OSError, ValueError, UnicodeError):
            continue
        if len(data) > MAX_CHARS:
            return None
        return data
    return None


def _is_absolute(path):
    if path.startswith("/") or path.startswith("\\\\"):
        return True
    if len(path) >= 3 and path[1] == ":" and path[2] in ("/", "\\"):
        return True
    return False


def _normalize_path(path):
    if path.startswith("file://"):
        path = path[7:]
        if len(path) >= 3 and path[0] == "/" and path[1].isalpha() and path[2] == ":":
            path = path[1:]
    return path


def _flatten_args(args):
    flat = {}
    for key, value in args.items():
        if isinstance(key, str):
            flat[re.sub(r"[^a-z0-9]", "", key.lower())] = value
    return flat


def _first_string(args, keys):
    for key in keys:
        value = args.get(key)
        if isinstance(value, str) and value.strip():
            return value.strip()
    return None


def _run_hook(payload):
    try:
        if payload.get("error"):
            return
        tool_call = payload.get("toolCall") or payload.get("tool_call") or {}
        if not isinstance(tool_call, dict):
            return
        raw_args = tool_call.get("args") or tool_call.get("arguments") or {}
        if not isinstance(raw_args, dict):
            return
        args = _flatten_args(raw_args)
        path = _first_string(
            args,
            ("targetfile", "path", "filepath", "absolutepath", "filename", "file"),
        )
        if not path:
            return
        path = _normalize_path(path)
        if not path.lower().endswith(TARGET_SUFFIXES):
            return

        text = _read_path(path, payload.get("workspacePaths"))
        if text is None:
            inline = _first_string(args, ("codecontent", "content"))
            if inline is not None:
                text = inline
        if text is None:
            return
        if len(text) > MAX_CHARS or "\x00" in text:
            return

        result = analyze(text)
        if not result["pass"]:
            for line in report_lines(result):
                sys.stderr.write(line + "\n")
            sys.stderr.flush()
    except Exception:
        pass
    finally:
        sys.stdout.write("{}\n")
        sys.stdout.flush()


def _run_files(paths, json_mode, verbose):
    records = []
    errors = 0
    any_fail = False

    for path in paths:
        try:
            with open(path, "r", encoding="utf-8", errors="replace") as handle:
                data = handle.read(MAX_CHARS + 1)
        except (OSError, ValueError, UnicodeError) as exc:
            sys.stderr.write(
                "[grai-gate] error: cannot read %s: %s\n" % (path, exc)
            )
            errors += 1
            continue
        if len(data) > MAX_CHARS:
            sys.stderr.write(
                "[grai-gate] error: %s exceeds the %d character limit\n"
                % (path, MAX_CHARS)
            )
            errors += 1
            continue
        if "\x00" in data:
            sys.stderr.write("[grai-gate] error: %s looks binary\n" % path)
            errors += 1
            continue
        result = analyze(data)
        records.append((path, result))
        if not result["pass"]:
            any_fail = True

    if json_mode:
        values = [_json_result(path, result) for path, result in records]
        if len(paths) == 1 and len(values) == 1:
            output = values[0]
        else:
            output = values
        sys.stdout.write(json.dumps(output, ensure_ascii=True) + "\n")
    else:
        printed = False
        for path, result in records:
            if result["pass"]:
                if verbose:
                    sys.stdout.write(_clean_summary(path, result) + "\n")
                continue
            if printed:
                sys.stdout.write("\n")
            if len(paths) > 1:
                sys.stdout.write("File: %s\n" % path)
            for line in report_lines(result):
                sys.stdout.write(line + "\n")
            printed = True

    if errors:
        return 2
    if any_fail:
        return 1
    return 0


def _run_text(text, label, json_mode, verbose):
    if len(text) > MAX_CHARS:
        sys.stderr.write(
            "[grai-gate] error: %s exceeds the %d character limit\n"
            % (label, MAX_CHARS)
        )
        return 2
    if "\x00" in text:
        sys.stderr.write("[grai-gate] error: %s looks binary\n" % label)
        return 2
    result = analyze(text)
    if json_mode:
        sys.stdout.write(
            json.dumps(_json_result(label, result), ensure_ascii=True) + "\n"
        )
    elif not result["pass"]:
        for line in report_lines(result):
            sys.stdout.write(line + "\n")
    elif verbose:
        sys.stdout.write(_clean_summary(label, result) + "\n")
    return 0 if result["pass"] else 1


USAGE = """grai-gate %s: advisory anti-slop linter for markdown and text.

Usage:
  python3 gate.py FILE [FILE ...]
  python3 gate.py -j FILE [FILE ...]
  python3 gate.py -v FILE
  cat draft.md | python3 gate.py

Options:
  -j  JSON output. One object for one file, an array for several.
  -v  Verbose. Print a clean line when a file passes.
  -h  Show this help.

Clean files are silent by default. The hook always exits 0 and prints {}.
Exit codes for the command line: 0 clean, 1 slop found, 2 input error.
""" % VERSION


def run_cli(argv):
    paths = []
    json_mode = False
    verbose = False

    for argument in argv:
        if argument == "-h":
            sys.stdout.write(USAGE)
            return 0
        if argument == "-j":
            json_mode = True
            continue
        if argument == "-v":
            verbose = True
            continue
        if argument.startswith("-") and argument != "-":
            sys.stderr.write(
                "[grai-gate] error: unknown option %s\n" % argument
            )
            sys.stderr.write(USAGE)
            return 2
        paths.append(argument)

    if paths:
        return _run_files(paths, json_mode, verbose)

    if sys.stdin.isatty():
        sys.stderr.write(USAGE)
        return 2

    raw = sys.stdin.read()
    if not raw.strip():
        sys.stdout.write("{}\n")
        return 0

    stripped = raw.lstrip()
    if stripped.startswith("{") or stripped.startswith("["):
        try:
            payload = json.loads(raw)
        except ValueError:
            sys.stdout.write("{}\n")
            return 0
        if isinstance(payload, dict):
            tool_call = payload.get("toolCall") or payload.get("tool_call")
            if isinstance(tool_call, dict):
                _run_hook(payload)
                return 0
        sys.stdout.write("{}\n")
        return 0

    return _run_text(raw, "stdin", json_mode, verbose)


def main():
    _configure_streams()
    try:
        return run_cli(sys.argv[1:])
    except BrokenPipeError:
        return 0
    except KeyboardInterrupt:
        return 130
    except Exception as exc:
        sys.stderr.write("[grai-gate] fatal: %s\n" % exc)
        return 2


if __name__ == "__main__":
    sys.exit(main())
