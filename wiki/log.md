# Log

Append-only. Newest entries at the top. Prefix format `## [YYYY-MM-DD]
<type> | <title>` is deliberate — `grep "^## \[" log.md | tail -5` gives the
last 5 entries.

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
