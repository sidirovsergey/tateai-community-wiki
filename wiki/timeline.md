---
type: overview
name: Timeline
tags: [overview]
---

# Timeline

Grounded in the archive's actual daily message-volume series
(`raw/index/chunks.json` covers the same range; see `SCHEMA.md` for how this
was computed), not vibes. 164,440 messages total,
[26 Oct 2024](../raw/logs/2024-10/2024-10-26.md) .. [15 Jul
2026](../raw/logs/2026-07/2026-07-15.md).

## Monthly volume

| Month | Messages | |
|---|---:|---|
| 2024-10 | 41,863 | founding + launch rush begins |
| 2024-11 | 74,370 | **peak** — launch rush continues |
| 2024-12 | 4,928 | sharp falloff |
| 2025-01 | 12,635 | secondary wave (AI-agent narrative) |
| 2025-02 .. 2025-07 | ~2,500–3,400/mo | steady low baseline |
| 2025-08 .. 2026-04 | 600–1,600/mo | long quiet tail |
| 2026-05 .. 2026-07 | 400–1,200/mo | bot-building era (see below) |

Roughly **70% of everything ever posted in this chat happened in its first
three weeks** (26 Oct – 14 Nov 2024). Every month since has been a small
fraction of that opening rush. This is the single most important shape to
understand about this community: it is fundamentally a launch-hype chat that
found a small steady core afterward, not a chat that grew over time.

## Oct 26 – Nov 2, 2024 — the ticker hunt

The group existed as "a basic group" and was converted to the current
supergroup right at the start of the export
([26 Oct 2024](../raw/logs/2024-10/2024-10-26.md)). The founding activity is
not "here's our coin" — it's amateur on-chain detective work trying to
figure out *which* token, among several candidates, was the "real" one
Andrew Tate had hinted at via "Easter eggs." [[sergei]] was one of the
people doing that analysis; the confirmed answer became `$TateAI`
(contract `BoBj68cWnCvzMNUKzJyR7Jq7tLM3v76D1pYL1E8rpump` — see
[[contract-address]]). See [[tate-tateai-terminal-namespace]] for how this
token relates to (and is routinely confused with) Andrew Tate's own `$Tate`/
`$DADDY` coin and to the separate `@tate_terminalbot` feed.

## Nov 2024 — peak, then the crowd thins

74,370 messages in November alone — the single busiest month by a wide
margin, days regularly exceeding 5,000-10,000 messages (peak: **11,394 on 29
Oct**, the single busiest day in the archive). This is also when the chat's
recurring characters establish themselves: [[rgk1]]'s "Be cool" persona and
[[fluxcapacitor]]'s first documented "HELLO WORLD" appearances both land in
this window.

## Dec 2024 — the crash in volume

Message volume drops by roughly 15x from November to December almost
overnight (74,370 → 4,928) — consistent with a typical memecoin-launch
attention curve: the founding rush and price-discovery period ends and most
of the crowd that arrived for the ticker hunt moves on.

## Jan 2025 — the AI-agent narrative wave

A secondary, smaller wave (12,635 messages, elevated but not spiky — no
single dominant day) coincides with the broader crypto "AI agent" narrative
gaining traction industry-wide. [[rgk1]]'s posting shifts into dense
philosophical essays specifically framing `$TateAI` within that narrative
("Is Andrew the General manager and Terminal the Head Coach?"). This is the
last month of meaningfully elevated activity.

## Feb 2025 – Apr 2026 — the long tail

Roughly 15 months of low, steady activity (a few hundred to a few thousand
messages/month) — a small core of regulars (see the message-count leaders in
`wiki/index.md`) keeping the chat alive without another comparable spike.
[[fluxcapacitor]] makes two more documented appearances in this window
(31 Jul 2025, 5 Mar 2026), each still drawing strong reaction counts despite
the otherwise-quiet chat.

## May – Jul 2026 — the bot-building era

- **[18 May 2026](../raw/logs/2026-05/2026-05-18.md)** — [[sergei]] posts
  about using "Claude Code + Obsidian (Karpathy LLM-wiki idea)" for an
  on-chain wallet-investigation project — the same pattern this very wiki
  now follows.
- The Terminal Subagent bot goes live (per the bot repo's own
  `docs/HANDOFF.md`, built 10–14 May 2026): auto-`/CA` on join, the `:)`
  heartbeat (see [[smiley-heartbeat]]), `/oracle`, `/info`.
- **[12 Jul 2026](../raw/logs/2026-07/2026-07-12.md)** — Sergei announces,
  in-chat, the plan to build exactly this wiki and an `/ask` command
  ("who is flux?" is his own example question) — see [[sergei]].
- **15 Jul 2026** — the raw export this wiki is built from ends.

## Related
[[sergei]], [[rgk1]], [[fluxcapacitor]], [[tate-tateai-terminal-namespace]], [[contract-address]]
