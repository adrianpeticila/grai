# Visuals: image concepts, image prompts, text cards

## 1. Image for a post (mode IMAGE)

Input: a post, or a variant from mode POST. Ask for the platform if it is not clear.

Output 3 concepts that differ in kind, not only in style:
1. Literal: shows the subject of the post.
2. Metaphor: one object or scene that carries the idea.
3. Text card: no photo, the key line or number as typography (see section 3).

For each concept:
- `Concept:` one line.
- `Why it works:` one line, tied to the post's first line.
- `Image prompt:` ready to paste into any image tool (ChatGPT, Gemini, Midjourney, Firefly, Ideogram, Canva). Use the formula in section 2.
- `Size:` the aspect ratio and pixels for the platform (see platforms.md).
- `Alt text:` one sentence that describes the image for screen readers. Max 125 characters.
- `Caption:` the caption for this image, in the voice. If the post itself is the caption, write "use the post".

Then the user chooses. Do not rank.

## 2. Image prompt formula

Write the prompt in English, even when the post is in another language. Image tools follow English best.

`<subject>, <action or state>, <setting>, <composition and camera>, <light>, <style>, <colour palette>, <aspect ratio>. Avoid: <list>.`

Rules:
- One subject. One idea. No collage unless the user asks.
- No text in the image unless the user asks. Image tools misspell text. Put text in a card instead.
- No real person's face or name. No brand logos. No trademarked characters.
- No stock clichés: handshakes, a glowing brain, a robot hand touching a human hand, people pointing at a screen, a lightbulb for "idea".
- If the user gave brand colours, use their hex codes. Else name a palette in 2 to 3 colours.
- `Avoid:` always lists: text, watermark, extra fingers, distorted faces, logos.

## 3. Text card

A text card is typography on a plain background. It works for a strong line, a number or a short list. Output it in this block, so the grai page can render it as a PNG:

```
CARD
Template: <quote | number | list | before-after>
Kicker: <max 4 words, optional>
Headline: <max 12 words>
Body: <max 30 words, optional; for list: items split by " | ">
Footer: <name or handle, optional>
Size: <square | portrait | landscape | story>
END CARD
```

Templates:
- quote: one strong line from the post. Headline = the line.
- number: Headline = the number and its unit. Body = what it means, one sentence. Only a number the user gave.
- list: Headline = the claim. Body = 3 to 5 items.
- before-after: Headline = the change. Body = `before text | after text`.

If the user has no grai page, also offer the card as SVG code (1080 x 1080, system font, high contrast). The user can open the SVG file in a browser and take a screenshot.
