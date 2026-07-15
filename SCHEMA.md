# Schema — how this wiki is built and maintained

This repo follows the "LLM Wiki" pattern: two layers, `raw/` and `wiki/`. If
you are an LLM agent picking this up in a future session, read this whole
file before touching anything.

## The two layers

**`raw/`** is the immutable source of truth. Full day-by-day transcripts of
the Telegram group **Terminal of Tate $TateAI**, parsed straight from
Telegram Desktop exports. Never edit these except to fix a parsing bug (see
"Known raw-layer issues" below) — they are not where synthesis happens.

- `raw/logs/<YYYY-MM>/<YYYY-MM-DD>.md` — one file per day, every message,
  clearly timestamped and attributed, UTC+05:00.
- `raw/pinned_messages.md` — every pin event resolved to its target message.
- `raw/index/chunks.json` — a flat JSON array of ~30-message windows. This
  was the *entire* retrieval mechanism in wiki v1 (blind keyword search over
  raw chunks) and is kept as a fallback full-text substrate — grep it, or
  point a proper search tool (see `qmd` in the Karpathy pattern doc) at it if
  `wiki/` doesn't have a page covering something yet. It is not maintained
  page-by-page like `wiki/` is.

**`wiki/`** is the compiled, LLM-maintained synthesis layer. This is where
the actual "knowledge" lives — everything in here should be *readable on its
own*, without the reader needing to go dig through months of raw transcript.

- `wiki/entities/<slug>.md` — one page per notable person. Bio, personality,
  notable quotes, timeline of appearances, relationships to other people.
- `wiki/concepts/<slug>.md` — one page per recurring theme, piece of lore, or
  thing that needs disambiguating (the token, the bot, running jokes,
  community rituals).
- `wiki/overview.md` — single-page synthesis: what this community is, its
  arc, its culture, in ~500-800 words. The page you'd hand someone who asks
  "what even is this chat."
- `wiki/timeline.md` — chronological narrative of eras/events, grounded in
  actual message-volume data and dated excerpts, not vibes.
- `wiki/index.md` — catalog of every wiki page: link + one-line summary,
  grouped by category. **Read this first** when answering a question or
  deciding whether a new page is needed. Update it every time you add or
  materially change a page.
- `wiki/log.md` — append-only. One entry per ingest/synthesis/lint pass.
- `wiki/_bundle.json` — **machine-generated, do not hand-edit.** Every
  `entities/`+`concepts/`+`overview.md`+`timeline.md` page flattened into one
  JSON array (`{id, type, title, tags, text}`), built by `build_bundle.py` in
  the repo root. This is what the bot's `/ask` command actually fetches and
  scores — one HTTP GET, ~140KB (vs. v1's 13MB `raw/index/chunks.json`),
  because the whole point of `wiki/` is that a handful of curated pages beats
  thousands of raw windows. **Run `python build_bundle.py` and commit the
  result any time you add or edit a `wiki/entities/` or `wiki/concepts/`
  page** — `/ask` only ever sees what's in `_bundle.json`, not the live `.md`
  files directly.

## Page conventions

Every `wiki/entities/*.md` and `wiki/concepts/*.md` page starts with
YAML frontmatter:

```yaml
---
type: entity            # or: concept
name: FluxCapacitor
aliases: [Flux, Flux Capacitor]     # entities only
message_count: 162                  # entities only, as of last sync
first_seen: 2024-11-22
tags: [community-member]            # or whatever fits
---
```

Cross-references use Obsidian-style `[[wikilink]]` syntax (`[[rgk1]]`,
`[[contract-address]]` — filename without extension, page basename only,
Obsidian resolves it regardless of folder). This repo is a plain folder of
markdown, not literally an Obsidian vault, but writing links this way means
it becomes one for free if anyone opens it in Obsidian — graph view, backlinks,
all of it, with zero extra work.

Citations point back into `raw/`: `[2024-11-22](../../raw/logs/2024-11/2024-11-22.md)`.
Every non-obvious claim on a wiki page should be traceable to a raw log this
way. A page with no citations is a page someone made up.

**Honesty over completeness.** If the raw material for a concept is thin (4
mentions, one specific pattern, whatever), say that plainly and keep the page
short. Do not pad a page with generic crypto-Telegram color to make it look
more substantial than the source material supports. The failure mode we're
correcting away from is exactly this: v1 of this wiki was long on process and
short on actually-synthesized judgment. A three-sentence honest page beats a
thirty-line invented one.

## Known raw-layer issues (as of 2026-07-16)

- **Forwarded-message sender rendering bug.** In `raw/logs/`, a forwarded
  message's displayed "sender" sometimes concatenates the original author's
  name with their forward timestamp, e.g. `` `Watcher Guru 04.07.2025
  00:23:21` `` instead of `` `Watcher Guru` ``. Anyone (human or LLM) reading
  raw logs should mentally strip a trailing date off a from-name that looks
  like `Name DD.MM.YYYY HH:MM:SS`. Not yet fixed at the source (would require
  re-running the HTML parser); flagged here so it doesn't get mistaken for a
  real distinct chat participant. **This directly caused a wrong answer in
  wiki v1 testing** — `/ask` cited "tate terminal" as a diamond-hands holder
  when it was actually a forwarded-content source, not a person. See
  [[tate-tateai-terminal-namespace]].
- **`Deleted Account` is not one person.** It's Telegram's placeholder for
  any user who deleted their account before export time — the single
  highest-message-count "sender" in the whole corpus (33.8k messages) is this
  label covering an unknown number of *different* real people. Never write an
  entity page for "Deleted Account" as if it were an individual. See
  `wiki/concepts/deleted-accounts.md`.
- **Display names that look like real names are not claims of identity.**
  Senders named "Tate AI" or "Donald Trump" are ordinary community members
  who picked a joke display name — not the real Andrew Tate, not the real
  Donald Trump, not an official project account. Telegram display names are
  self-chosen and unverified. See [[tate-tateai-terminal-namespace]].

## Workflows

### Ingesting a new export chunk

1. Parse the new Telegram Desktop export into the `raw/logs/` day-file
   format (script was ad-hoc/session-scratch in v1 — if it needs rebuilding,
   the format is simple enough to redo from scratch: BeautifulSoup +
   `html.parser` over `messages*.html`, one record per `.message` div, fields
   = id/date/sender/text/reply_to/media/reactions).
2. Dedupe on **positive** message ids only against existing `raw/` content
   (two independently-exported chunks share exactly the messages Telegram
   re-included at the boundary). Do **not** dedupe negative/service ids
   across exports — those are per-export synthetic counters, not stable
   identifiers, and colliding values between two exports are unrelated
   events.
3. Regenerate `raw/index/chunks.json` if you're keeping that fallback
   mechanism current (optional at this point — it's a fallback, not primary).
4. Walk `wiki/index.md`: for every entity/concept page whose subject shows up
   materially in the new material, re-read the page, decide whether it needs
   updating (new notable quote, contradicts an old claim, timeline shift),
   and edit it in place. Note what changed in `wiki/log.md`.
5. For any new person who's now clearly notable (high message count in the
   new range, or came up in a question someone asked), consider seeding a new
   entity page — don't feel obligated to cover everyone, this compounds over
   time.
6. Run `python build_bundle.py` and commit `wiki/_bundle.json` along with
   whatever pages you changed. Forgetting this step means `/ask` keeps
   answering from stale pages even after you've updated them.

### Answering a question (what `/ask` should do, and what a human session should do)

1. Read `wiki/index.md` first — don't go straight to `raw/`.
2. If a wiki page covers it, read that page (and anything it links to) and
   answer from it, citing the page and/or the raw log dates it cites.
3. If no page covers it, fall back to `raw/index/chunks.json` (or grep
   `raw/logs/`) to find something to answer from — and if the question is
   one that will plausibly come up again, that's a signal a new wiki page
   should be filed, not just an answer given and forgotten. Karpathy's point
   about "queries compound the wiki too" — a good ad-hoc answer is a
   candidate wiki page, not just chat output.
4. Never state something as fact that isn't traceable to `raw/`. If it's not
   there, say so plainly (this chat's raw log is extensive but not complete —
   see the "Known raw-layer issues" section for what's genuinely thin, like
   `oracle` at only 4 real mentions).

### Lint pass

Periodically (and definitely before telling anyone this wiki is
"exhibition-quality"):

- Every `wiki/entities/*.md` and `wiki/concepts/*.md` file is linked from
  `wiki/index.md`. No orphans.
- Every page has at least one working citation into `raw/`.
- Cross-check `[[wikilinks]]` resolve to an actual page (or are a deliberate
  stub worth creating).
- Spot-check a few claims by re-reading the cited raw log — synthesis drift
  (a page confidently saying something the raw material only weakly
  supports) is the main way these wikis go bad silently.

## Why `raw/index/chunks.json` still exists

It was the whole mechanism in v1 and is now a fallback, per the Karpathy
pattern's own guidance: "at small scale the index file is alone enough...
as the wiki grows you might want a proper search tool (qmd, etc.)." Given
~165k messages and ~30 seeded entity pages as of this writing, most
real questions should be answerable from `wiki/` alone; `raw/index/` covers
the long tail this first pass didn't get to.
