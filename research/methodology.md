# The Architecture Under the Words: Linguistic Audit of 134,522 LinkedIn Posts (2023 - 2026)

> **Empirical Research Report · LigoSocial Dataset · Published September 25, 2026 · Updated October 23, 2026**
> **Author:** Adrian M. Peticila (`https://peticila.ro/#person` · Wikidata `Q140362129` · ORCID `0009-0005-9601-9527`)
> **Canonical HTML:** https://grai.page/methodology

---

## 1. Executive Summary: The Blocklist Paradox

Between January 2023 and September 2026, founder writing underwent a documented structural shift. As awareness of synthetic copy spread, creators aggressively scrubbed mocked vocabulary words from their drafts.

The result was unexpected. While individual lexical tells collapsed, broader rhythmic and structural predictability climbed by 400%. Writers deleted the words. The habits stayed.

---

## 2. Dataset and Sampling Methodology

The audit analyzed 134,522 organic posts across 1,499 verified founder profiles. Profiles met three distinct criteria: continuous publishing from Q1 2023 through Q3 2026, minimum 2,000 followers, and primary language English.

Every post was analyzed for sentence length distributions, initial cadences, and syntactic templates.

| Metric | Q1 2023 | Q3 2026 | Observed Delta |
|---|---:|---:|---:|
| Opening Formula ("Here is why") | 1.3% | 9.6% | +7.4x |
| Forced Opposition ("Not X, but Y") | 1.2% | 5.9% | +4.9x |
| Arrow Bullet Density | 0.6% | 12.3% | +20.5x |
| Mocked Cliché Vocabulary | 4.2% | 0.5% | -88.1% |
| Mean Burstiness Coefficient (CV) | 0.48 | 0.23 | -52.1% |

---

## 3. Cadence Variation and Mathematical Rhythm

Human prose exhibits natural burstiness: short punchy sentences interspersed with complex elaborations. In statistical linguistics, this is measured using the Coefficient of Variation ($CV = \sigma / \mu$) of sentence word counts.

A natural human conversation maintains a $CV$ above $0.38$ with natural shifts between short punchy lines and expansive reasoning. Default model outputs hover around $0.20$. Monotony takes over.

grai enforces a hard floor at $CV = 0.32$. Monotone sentence structures get flagged before you publish.

---

## 4. The Harness Argument

Google Research proved it with Harness2: do not burn cash fine-tuning models. Harness them with deterministic prompts, cadence verifiers, and offline profiles.

The paper keeps model weights frozen and measures what changes around the model. Its eight editable components: system prompt, guardrails, memory, tool guidance, subagents, skills, scripts, plugins. A single harness step lifted GLM-5 and Gemini 3.5 Flash by up to 11.5 points on WorkBuddy-Bench, 4.5 points on JobBench, and 11.8 percentage points on LAB's partial pass rate.

grai applies the same logic to voice. It does not train a model on your posts. It builds a harness: a deterministic instruction set, six structural cadence checks, a $CV$ floor at $0.32$, and a voice profile that stays in local browser storage. The model is replaceable. The harness is what makes the output sound like you.

---

- Return to homepage: https://grai.page/
- Full LLM Specification: https://grai.page/llms-full.txt
