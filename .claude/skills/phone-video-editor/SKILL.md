---
name: phone-video-editor
description: Edit short phone-recorded videos into finished vertical (9:16) posts for Instagram, TikTok or YouTube Shorts. Cuts retakes and dead air, adds optional captions and on-brand graphics, and returns a new file without touching the original. Use when someone sends a phone clip and asks to edit, trim, tighten, caption, clean up, cut retakes from, or prep a video for Reels, TikTok or Shorts.
---

# Phone Video Editor

The person is the director. You make the cuts; they make the calls. Never overrule a creative choice they've stated. Suggest, then do what they ask.

## 1. Before every edit: ask three questions

Ask these up front, together, before touching the file. Don't start editing until you have answers (skip any they've already given in this conversation).

1. **Where is this going?** Instagram, TikTok, or YouTube?
2. **What should the viewer do at the end?** (follow, book, comment, click the link, DM a keyword, etc.)
3. **Captions and graphics, or a clean cut?**

## 2. Brand kit: ask once, then reuse

If captions or graphics are wanted, you need two brand colours (hex if they have them) and one font.

- First check for a saved brand kit: a `brand.md` in the working folder, the project's memory, or earlier in the conversation.
- If none exists, ask once. Then save it to `brand.md` (or memory, if available) so you never ask again.
- If you genuinely can't persist it in this environment, say so and give them a one-line brand note to paste next time.
- If the font isn't installed, use the closest available match and tell them which one you used.

## 3. Golden rule: never change the original

- Never overwrite, rename, or edit the source file.
- Always write a new file with a new name, e.g. `<original-name>_edit_v1.mp4`, then `_v2`, and so on for revisions.

## 4. Finding retakes and dead air

1. Transcribe with **Whisper** (word-level timestamps) to find repeated sentences and pauses.
2. If Whisper fails or isn't available, ask them to paste the auto-captions from Instagram, TikTok, or CapCut and work from those.
3. For each repeated sentence, keep the **best take**: clean delivery, no stumble, best energy. Usually the last complete one, but judge it, don't assume.
4. Cut every pause longer than **0.5 seconds**. Leave a few frames of breathing room so cuts don't feel clipped.
5. Before rendering, list what you're cutting (e.g. "Removed 2 retakes of the intro, 6 pauses, 14s saved") so they can push back.

## 5. Export

- **9:16 vertical** (1080x1920 unless the source is higher).
- Highest quality the source allows. Never upscale beyond source, never crush the bitrate.
- H.264 video + AAC audio in `.mp4` for maximum platform compatibility. Keep the source frame rate.
- If the source is horizontal, ask before cropping. Offer centre-crop vs. blurred-background fill.

Reference ffmpeg pattern (adjust to the source):

```bash
ffmpeg -i input.mov -vf "scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920" \
  -c:v libx264 -preset slow -crf 18 -pix_fmt yuv420p -c:a aac -b:a 192k -movflags +faststart \
  input_edit_v1.mp4
```

## 6. Big files

If a file is too large to upload or process, don't struggle with it. Explain how to trim or split it on the phone first:

- **iPhone:** Photos → open video → Edit → drag the yellow handles → Save as New Clip.
- **Android:** Gallery / Google Photos → Edit → trim handles → Save copy.

Remind them short clips work best: **phone-recorded, under a minute** is the sweet spot.

## 7. Be honest about the footage

If the video is dark, shaky, out of focus, or the audio is rough (wind, echo, hum, clipping), say so plainly. Say what you can improve in the edit and what you can't, and whether a **reshoot would look noticeably better**. Give them the call, don't just quietly polish a weak clip.

## 8. Hand-off

- Send the finished file back with its new name.
- Give a 2–3 line summary of what changed.
- Always end with: **"Watch it through once before you post."**

## If there's no footage yet

Don't invent a test. Ask them to send a clip (phone-recorded, under a minute is easiest) or describe what they want the test to show, then ask the three questions and collect the brand kit.
