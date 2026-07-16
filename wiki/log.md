# Log

Append-only. Newest entries at the top. Prefix format `## [YYYY-MM-DD]
<type> | <title>` is deliberate — `grep "^## \[" log.md | tail -5` gives the
last 5 entries.

## [2026-07-16] extend | v3: entity coverage doubled, 4 new concept pages

Requested after live use of v2 surfaced that coverage (top-20 by volume) and
depth (one synthesis pass) both had real gaps. Extended in the same pattern
as v2's build: pre-extract raw material per subject, write a couple of
pages by hand first (`the-terminal-mythos.md`, plus backlink patching), then
9 parallel agents for the rest.

**+22 entity pages** (Ri-ShadowAssassin, E, Whale, B, Sam, Otter Krafter,
Asiman, Nikola, Wilson, Ohh Cedi, Anad Suji, ET, Ronald, Daniel R,
Svyatoslav, I'm lucky, PARZIVAL, Plum, Chosen, Rari, Ekul, Jahn) — coverage
now ~40 of 783 total senders, up from ~20.

**+4 concept pages:**
- `the-terminal-mythos.md` — traces the community's "terminal" fascination
  from `@tate_terminalbot` (day one) through T's 2024 jailbreak attempts on
  a different early bot, Gabriel's Mar 2025 "Band of Brothers" episode
  (which independently ties into [[fluxcapacitor]] as a "summoning phrase"),
  Widelton's Apr 2026 fan site, to the real bot Sergei built in May 2026 —
  the bot is the *arrival*, not the origin, of the mythology.
- `on-chain-forensics.md` — ties together six people's independent wallet-
  tracing efforts across 2.75 years; documents a genuine contradiction (the
  same 1,350 SOL transfer read as both rug evidence and bullish confirmation
  by different investigators five days apart).
- `the-real-world-trw.md` — Andrew Tate's paid platform, constantly cross-
  referenced; traces Sergei's own pivot from believer to "it's a TRW
  marketing funnel" theorist.
- `rival-tate-coins.md` — the `$Tate`/`$DADDY`/`$RNT`/`$TOPG` roster and the
  "cabal" vs. "brotherhood of one man" framing; found 3 more ban-for-cross-
  promotion incidents beyond the two already documented on individual pages.

**Lint pass:** all 55 pages re-verified — 579/579 raw-log citations resolve,
0 broken cross-reference links. Added targeted backlinks to reduce orphans
(pages with zero inbound cross-links beyond `index.md`) where agent reports
surfaced a genuine connection; left individually-self-contained pages
un-forced rather than padding cross-links that don't reflect anything real.

Ran `python build_bundle.py` and committed the result — see `SCHEMA.md`,
this step is mandatory after any page change or `/ask` answers from stale
content.

## [2026-07-16] rebuild | Wiki v1 → v2: RAG chunks to a real synthesized wiki

v1 (built same day, hours earlier) was a raw-source + keyword-chunk-retrieval
setup — every `/ask` answer was re-derived from scratch by scoring ~5,000
30-message windows against the question. It worked mechanically but tested
badly: asked "who is flux?", "why :) ?", and "whom can you consider diamond
hand holders?" against it live. Result: a false "not found" on flux despite
relevant material being retrieved (model was over-conservative), a hard
architectural miss on ":)" (the tokenizer strips punctuation-only queries to
nothing, so zero chunks ever get retrieved), and a wrong citation on diamond
hands — "tate terminal" was named as a holder when it's actually a forwarded-
content source, not a chat participant, due to a raw-log rendering bug.

Rebuilt as a real two-layer wiki per the Karpathy LLM-wiki pattern
(source: shared by the project owner, in-chat announcement predates this
even existing — see `wiki/entities/sergei.md`). `raw/` (the v1 day-logs,
unchanged, renamed under `raw/`) stays the immutable source. `wiki/` is new:
21 entity pages, 8 concept pages, `overview.md`, `timeline.md`, this log,
and `index.md`. Content was synthesized by 9 parallel Claude agents each
given pre-extracted raw material for their assigned subjects plus the
schema/exemplar pages as a quality bar, after 3 entity pages + 3 concept
pages were hand-written first specifically to set that bar and fix the 3
bugs above:
- [[tate-tateai-terminal-namespace]] — direct fix for the diamond-hands
  misattribution.
- [[smiley-heartbeat]] — documents the `:)` phenomenon a keyword search
  literally cannot retrieve (tokenizes to nothing).
- [[deleted-accounts]] — flags the single highest-volume "sender" as not
  being a real individual, a landmine for any naive per-person analysis.

Coverage: top ~20 participants by message volume (from 783 total senders in
the corpus) plus [[fluxcapacitor]] (seeded despite low volume — it's what
got tested against v1 and failed). `raw/index/chunks.json` remains as a
fallback for the long tail of ~760 people this pass didn't reach.

One cross-page consistency issue caught and fixed during integration: two
different agents independently investigated a "Lima" naming overlap between
[[limalemon]] (handle `@LimaLemon777`) and [[orchestra_lima_maxi]] (display
name coincidentally contains "Lima") — both correctly identified them as
different people and cross-linked accordingly; added a symmetric note to
`limalemon.md` so the connection reads clearly from either direction.

Next step after this entry: rewire the bot's `/ask` command to read
`wiki/index.md` and specific pages instead of blind-scoring
`raw/index/chunks.json` — see the bot repo's `docs/HANDOFF.md` §12 once
that lands.
