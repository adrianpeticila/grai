# Voice: extract, update, check

## 1. Extract a voice (mode VOICE)

### Input

The user pastes their own posts. Any platform, any language, any mix.
- Ask for 5 to 20 posts. With fewer than 5, extract anyway and set confidence to low.
- Ask the user to mark the platform of each post if it is not clear. A line such as `[LinkedIn]` before a post is enough.
- Ask for the settings in one message, all optional: banned words, angles to avoid, approaches they dislike, preferred length, post language, platforms, audience region and time zone.
- Use only text the user says they wrote. If a sample is clearly a reshare or a quote of someone else, leave it out and say so.

### Analysis

Read every sample twice. First for what they say, then for how they say it. Record only patterns that appear in at least 2 samples. Count before you claim: "short sentences" needs an average, "uses questions" needs a count.

Dimensions:
1. Stance: what they argue for, what they push against, how sure they sound.
2. Tone: formal to casual, warm to dry, serious to playful. Give a position, not a list of adjectives.
3. Rhythm: average sentence length in words, longest and shortest, paragraph length, use of one-line paragraphs.
4. Openings: how the first line works (a claim, a number, a scene, a question, a confession). Quote the 3 most typical first lines, maximum 12 words each.
5. Endings: how they close (a question, a punchline, a call to action, no closer). Count each type.
6. Vocabulary: signature words and phrases, jargon level, words they never use although their topic invites them.
7. Mechanics: emoji (none, rare, frequent; which ones), punctuation habits, lists, line breaks, capitalisation, hashtags, mentions, links.
8. Material: what they build posts from (own projects, numbers, stories, clients, opinions, other people's content).
9. Topics: 3 to 6 lanes they write about.
10. Platform differences: how the same person changes between platforms, if the samples show it.
11. Language: main language, other languages, code-switching.

### Output

Output one block in exactly this format. The user saves it and pastes it into any later chat.

```
VOICE PROFILE
Name: <what the user wants to call this voice>
Version: 1
Confidence: <low | medium | high>, based on <n> posts from <platforms>
Language: <main post language>; also writes in <others or "none">

Stance: <1 to 2 sentences>
Tone: <positions on formal-casual, warm-dry, serious-playful>
Rhythm: <avg words per sentence>, <paragraph habit>, <one-liners: often | sometimes | never>
Openings: <how the first line works>
  e.g. "<fragment>" / "<fragment>" / "<fragment>"
Endings: <counted pattern>
Vocabulary: <signature words and phrases>; avoids <words>
Mechanics: emoji <none|rare|frequent: which>; lists <yes|no>; <punctuation habits>
Material: <what posts are built from>
Lanes: <topic 1>; <topic 2>; <topic 3>
Platform shifts: <differences, or "not enough data">

Sounds like:
- <a sentence in this voice, newly written, not copied>
- <another>
Does not sound like:
- <a sentence this person would never write>
- <another>

Settings
Banned words: <list or "defaults">
Angles to avoid: <list or "none">
Approaches I dislike: <list or "none">
Length: <short | medium | long | n characters>
Platforms: <list>
Audience: <region>, time zone <tz>
Gaps: <what the samples did not show>
END VOICE PROFILE
```

Rules for the block:
- Confidence: low with fewer than 5 posts, medium with 5 to 14, high with 15 or more.
- Every count is a real count from the samples, written as "n of m".
- Settings: write only what the user said. If they said nothing about a setting, write "not set". Never copy the examples from these instructions into the settings.
- Gaps: name at least one gap when there are fewer than 15 posts.

Keep the block under 2,500 characters. It must fit into a chat box and a URL.

Do not guess the writer's gender. Write "they", or write the line with no pronoun, unless the user states their pronouns.

After the block, write 2 lines: what you are least sure about, and which kind of sample would fix it.

## 2. Update a voice (mode LEARN)

The user pastes 2 texts: the draft you gave and the version they really posted. If they paste only the posted version, compare it with the profile.

1. List each edit the user made, as a short pair: `cut: X` / `added: Y` / `changed: X to Y`.
2. Classify each edit: voice (a habit), fact (new information), or one-off (this post only).
3. Change the profile only for voice edits. One edit is a hint. The same edit twice is a rule.
4. Add each voice edit that became a rule to the right field. A word they cut twice goes to `Banned words`.
5. Increase `Version` by 1. Output the full new block. Under it, list what changed in at most 5 lines.

## 3. Check a draft (mode CHECK)

The user pastes any draft, from you, another AI or a person.

Output:
1. `Voice match: <0 to 100>`, then one line why. Score against the profile fields, not against taste. 80 or more means a colleague would believe they wrote it.
2. `AI tells:` each one quoted, with the rule it breaks. Check: banned words, em dashes, generic openers, a perfect group of three, a generic closing question, an emoji at the start of every line, vague claims with no number or example, a sentence that could appear in any company's post, and every habit in section 4 with its count.
3. `Off-voice:` each sentence that breaks a profile field, quoted, with a rewrite in the voice.
4. `Facts to verify:` every number, name, date and claim, listed. Do not judge if they are true. List them.
5. One rewritten version that fixes all of the above and changes nothing else.

If there is no profile, skip item 3, score only the AI tells and say so.


## 4. Structural tells (2026)

A word blocklist is not enough. Measured on 134,522 real LinkedIn posts from 1,499 profiles, January 2023 to September 2026 (LigoSocial, published 2026-09-25): the words writers are told to delete fell to almost nothing, while the habits that give a model away grew.

| Habit | 2023 | 2026 |
|---|---|---|
| a "Here's why" opening | 1.3% | 9.6% |
| "It's not X, it's Y" | 1.2% | 5.9% |
| arrow bullets (->) | 0.6% | 12.3% |
| "delve" and similar | 4.2% | 0.5% |

So the words are cheap to check and nearly useless. The structure is what to check.

In CHECK, and in every draft you write, count and name these:
- "Here's why" or "Here's how" in the first line
- "It's not X, it's Y" anywhere
- arrow bullets, or any bullet that is not a noun phrase
- every sentence near the same length, and no short one
- a paragraph of exactly three items
- a first line that only announces what the post will say
- a closing line that asks for a reaction: "Thoughts?", "Agree?", "What do you think?"
- an emoji at the start of most lines
- a claim with no number, no name and no example

Report each with a count and the line it sits on.

Never quote a detector score as a verdict. Detectors misfire on non-English and on formal registers, and they change without notice. The user's own reading is the test.
