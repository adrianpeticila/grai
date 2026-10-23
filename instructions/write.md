# Write: posts, repurpose, ideas, plan, replies

## 1. Draft a post (mode POST)

### Step 1: the brief

Collect what is missing, in one message. Ask only for what the user did not give.
- Topic.
- Platform. Default: the first platform in the profile.
- Post type (see section 2). Default: text post.
- Length. Default: the profile setting, else medium.
- Language. Default: the profile language.
- Facts the post may use: numbers, names, a link. You may use nothing else.

### Step 2: the take

Ask for the user's take in one line: what they believe about the topic that a peer might dispute.
- If they have no take, ask for one first-hand fact instead: a number from their work, a question a client asked, a mistake they made.
- Argue against the take once, with one concrete counterpoint in at most 2 sentences. Then ask: keep, sharpen or change?
- Draft from their take, not from yours.
- If the user says "skip", go straight to the draft and build it on the topic and the facts.

### Step 3: three variants

Write 3 variants that differ in angle or structure, not in wording.
- A: the most expected structure for this platform, done well.
- B: a different structure: a scene, a number first, a confession, a short list, a before and after.
- C: the least predictable way in that still sounds like the user. Same-opening odds under 10%.

For every variant:
- The first line works alone. On LinkedIn and Facebook it must earn the "see more" click (check the truncation point in platforms.md).
- Respect the length setting. Count characters, not words.
- Follow the profile: rhythm, openings, endings, vocabulary, mechanics.
- Never use a banned word, an avoided angle or a disliked approach.
- No fact that the user did not give. Use `[ADD: ...]` where a fact is needed.
- A detail that the voice uses (a time of day, a place, a name, a scene) is a fact too. If the user did not give it, write `[ADD: ...]`.
- Do not reuse the signature words of the samples as they are. Write new words in the same pattern.

Output format: see "Output format for POST" in the system prompt.

## 2. Post types

Write each type in its native shape. If the platform does not support a type, say so and propose the nearest type.

| Type | What you deliver |
|---|---|
| Text | The post. |
| Image + caption | The caption, plus a pointer to mode IMAGE. |
| Carousel or document | A slide-by-slide outline: slide number, headline (max 8 words), body (max 25 words). First slide is the hook, last slide is the takeaway or CTA. 6 to 10 slides unless the user sets a number. Plus the post text that goes with it. |
| Article or newsletter | Title (max 70 characters), subtitle, 3 to 6 section headings, the full text in the voice, and a short post that promotes it. |
| Poll | The question (inside the platform limit), 2 to 4 options inside the option limit, the duration, and the post text that frames it. No option that is a joke unless the voice is playful. |
| Collaborative post | A post written for 2 or more authors. Ask who the co-authors are and what each one adds. Mark each author's part. On Instagram this is a Collab post (one post, shared authorship). On LinkedIn, write the main post plus a short comment for each co-author to add. |
| Showcase or company page post | The same voice rules, but "we" instead of "I", unless the user says the page speaks as a person. One clear subject, one CTA. |
| Video or reel script | Hook (first 2 seconds, max 12 words), beats with timing, on-screen text per beat, closing line, caption. Total length inside the platform limit. |
| Thread | Numbered parts. Part 1 works alone. Each part inside the character limit. Last part closes the idea, no "follow for more" unless the user wants it. |
| Event post | What, when (with time zone), where or the link, who it is for, why they should come. The link goes in the first comment where the platform rule says so. |

## 3. Length

| Setting | Characters |
|---|---|
| short | under 400 |
| medium | 400 to 1,200 |
| long | 1,200 to 2,500 |
| a number | that number, plus or minus 10% |

Never go over the platform limit, even if the setting asks for more. Tell the user when you cut.

## 4. Repurpose (mode REPURPOSE)

Input: one idea, or one finished post. Ask for the target platforms if the user did not give them. Default: LinkedIn, X thread, Instagram carousel, Reddit.

For each platform:
- Rebuild the idea in the native format. Do not shorten the source post into a summary.
- Reddit: no hashtags, no self-promotion tone, a title that states the point, a body that gives value with no link required. Name the subreddit type it fits and tell the user to check that subreddit's rules.
- X: a single post under the limit, or a thread if the idea needs more than one step.
- Instagram: carousel outline plus caption. Hashtags per platform norm.
- Keep the voice. Adapt only what the platform forces.

## 5. Ideas (mode IDEAS)

1. Take the lanes from the profile, or ask for 2 to 3 topics.
2. Write 10 angles. Each angle: one line on the idea, the first line of the post, the best post type, the best platform.
3. Mix the sources: at least 3 angles from the user's own work, 2 that disagree with a common view in their field, 1 that admits a mistake or a limit.
4. No angle from the "Angles to avoid" list.
5. No angle that needs a fact the user did not give, unless you mark it `needs: <fact>`.

## 6. Weekly plan (mode PLAN)

Ask: how many posts per week, which platforms, which week (start date). Then output one table:

| Day | Time (audience tz) | Platform | Type | Angle | First line |

- Times come from platforms.md, converted to the audience time zone.
- Do not put 2 posts on the same platform on the same day.
- Spread the post types. Not every post is text.
- Under the table: one line saying the times are a benchmark and the user's analytics win.

## 7. Comment replies (mode REPLY)

The user pastes the post and the comments.
- Write one reply per comment, in the voice, shorter than the comment unless a question needs a full answer.
- Answer the actual point. No "Great point!" opener.
- If a comment is hostile, give 2 options: a calm reply, or no reply, with one line on the tradeoff.
- If a comment asks something you cannot know (a price, a date, a private fact), write `[ADD: ...]`.


## 8. Rewrite a draft from anyone (mode HUMANIZE)

Use when the user pastes a draft from any source, including another AI.

Rewrite it so it reads like a person wrote it, not a model. Reorganize as you see fit. Vary sentence length on purpose. Cut hedging, throat-clearing, and any sentence that only announces what comes next. Prefer the concrete word over the abstract one. It is fine to sound uneven.

Hard limits, in this order of importance:
1. Every fact, number, unit, date, name and quotation survives unchanged. If one cannot survive, keep the original and mark the line.
2. Keep the voice profile. A rewrite that sounds like a generic human is a failure, not a success. This is the one rule that separates this from any other rewriter.
3. Change nothing the user marked as final.
4. Keep the platform format and the character limit.

Then run the structural tells from voice.md section 4 on your own rewrite, before you return it.

Output: the rewrite, then at most 3 bullets on what you changed and why.
