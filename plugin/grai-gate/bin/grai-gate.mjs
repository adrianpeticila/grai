#!/usr/bin/env node
// bin/grai-gate.mjs
// Deterministic. No network. No model calls. Math only.

import { readFileSync } from 'node:fs';

const MIN_CV = 0.32;
const MAX_SLOP = 0;

const SLOP = [
  /\bleverage\b/i,
  /\bsynergy\b/i,
  /\bseamless(ly)?\b/i,
  /\bdelve into\b/i,
  /\btestament to\b/i,
  /\bin today'?s fast[- ]paced\b/i,
  /\bunlock the power\b/i,
  /\bit'?s important to note\b/i,
  /\bnavigate the landscape\b/i,
  /\bat the end of the day\b/i,
  /\btake it to the next level\b/i,
  /\bgame[- ]chang(er|ing)\b/i,
];

function extractProse(md) {
  const lines = md.split(/\r?\n/);
  const keep = [];
  let inFence = false;
  for (const raw of lines) {
    const line = raw.trim();
    if (/^```/.test(line)) { inFence = !inFence; continue; }
    if (inFence) continue;
    if (!line) continue;
    if (/^#{1,6}\s/.test(line)) continue;
    if (/^\|/.test(line)) continue;
    if (/^[-*_]{3,}$/.test(line)) continue;
    keep.push(line);
  }
  return keep.join(' ');
}

function sentences(text) {
  const cleaned = text
    .replace(/\[([^\]]+)\]\([^)]+\)/g, '$1')
    .replace(/!\[[^\]]*\]\([^)]*\)/g, '')
    .replace(/[*_`>#]/g, '')
    .replace(/^\s*[-+*]\s+/gm, '')
    .replace(/\s+/g, ' ')
    .trim();
  if (!cleaned) return [];
  return cleaned
    .split(/(?<=[.!?])\s+/)
    .map(function (s) { return s.trim(); })
    .filter(function (s) { return s.length > 0; });
}

function cv(lengths) {
  if (lengths.length < 2) return 0;
  const n = lengths.length;
  const mean = lengths.reduce(function (a, b) { return a + b; }, 0) / n;
  if (mean === 0) return 0;
  const variance = lengths.reduce(function (a, b) {
    return a + Math.pow(b - mean, 2);
  }, 0) / n;
  return Math.sqrt(variance) / mean;
}

function countSlop(text) {
  let hits = 0;
  const found = [];
  for (const re of SLOP) {
    const m = text.match(re);
    if (m) { hits += 1; found.push(m[0]); }
  }
  return { hits: hits, found: found };
}

function main(argv) {
  const file = argv[2];
  if (!file) {
    console.error('Usage: grai-gate <file.md>');
    process.exit(2);
  }

  let text;
  try {
    text = readFileSync(file, 'utf8');
  } catch (err) {
    console.error('Cannot read ' + file + ': ' + err.message);
    process.exit(2);
  }

  const prose = extractProse(text);
  const sents = sentences(prose);

  if (sents.length < 3) {
    console.error('SKIP: fewer than 3 sentences in ' + file);
    process.exit(0);
  }

  const lengths = sents.map(function (s) {
    return s.split(/\s+/).filter(Boolean).length;
  });

  const score = cv(lengths);
  const slop = countSlop(prose);

  console.log(
    file +
    ' | CV ' + score.toFixed(3) +
    ' | sentences ' + sents.length +
    ' | slop ' + slop.hits
  );

  let fail = false;

  if (score < MIN_CV) {
    console.error('FAIL: CV ' + score.toFixed(3) + ' below ' + MIN_CV + '. Cadence flattened. Rewrite for variance.');
    fail = true;
  }

  if (slop.hits > MAX_SLOP) {
    console.error('FAIL: ' + slop.hits + ' slop tells. Found: ' + slop.found.join(', '));
    fail = true;
  }

  if (fail) process.exit(1);
  console.log('PASS. Cadence survives.');
}

main(process.argv);
