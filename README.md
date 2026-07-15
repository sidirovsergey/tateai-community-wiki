# Terminal of Tate $TateAI — LLM Wiki

A knowledge base about the **Terminal of Tate $TateAI** Telegram community,
built following the "LLM Wiki" pattern (an LLM incrementally compiles raw
sources into a persistent, cross-linked wiki, instead of re-deriving answers
from scratch on every query). See `SCHEMA.md` for the full pattern and how
this repo follows it.

## Two layers

1. **`raw/`** — immutable source of truth. Full day-by-day transcripts
   parsed from Telegram Desktop exports, one file per day, every message
   timestamped and attributed.
2. **`wiki/`** — the actual knowledge base. LLM-synthesized entity pages
   (people), concept pages (lore, running jokes, things that need
   disambiguating), an overview, a timeline, and an index. **Start at
   [`wiki/index.md`](wiki/index.md).**

## Provenance

- Chat: **Terminal of Tate $TateAI**
- Export window: 2024-10-26 .. 2026-07-15
- Total messages: 164,440 (+913 service events), 628 days covered
- All timestamps: UTC+05:00 (as recorded by Telegram export)
- `wiki/`: 21 entity pages, 8 concept pages, overview + timeline, built
  2026-07-16 — see `wiki/log.md` for the build history
- Media (photos/video/voice/stickers) is referenced by type + original
  filename only — content was not captioned or transcribed in this pass
- The chat's raw language is uncensored community banter (profanity, slurs,
  dark humor) — preserved faithfully in `raw/`, and quoted plainly rather
  than smoothed over in `wiki/` where it's load-bearing for a page (a
  conscious choice, not an oversight)

## Files

- `wiki/index.md` — **start here.** Catalog of every wiki page.
- `wiki/overview.md`, `wiki/timeline.md` — top-level synthesis.
- `wiki/entities/*.md`, `wiki/concepts/*.md` — the actual pages.
- `wiki/log.md` — chronological build/ingest log.
- `raw/logs/<month>/<day>.md` — full day transcripts (the source layer).
- `raw/pinned_messages.md` — every pin event resolved to its target message.
- `raw/index/chunks.json` — v1's retrieval mechanism (blind keyword search
  over 30-message windows); kept as a fallback for the long tail of ~760
  chat participants `wiki/` hasn't seeded pages for yet.
- `SCHEMA.md` — conventions and workflows for maintaining this wiki.
