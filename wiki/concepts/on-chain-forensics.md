---
type: concept
name: On-chain forensics
tags: [on-chain, investigation, lore, recurring-theme]
---

# On-chain forensics

This chat has never had a professional research arm, but it has never
stopped producing amateur ones. From the first hour of the export through
the most recent material in 2026, a rotating cast of members has
independently taken to Solscan (and later Bubble Maps, Photon, and Helius)
to trace wallets, cluster holders, and argue over what the blockchain
"proves." [[sergei]], [[t]], [[marcin_krukowski]], [[bob]], [[widelton]],
and [[0xvoid]] each did this on their own timeline and in their own
register — this page is where those threads get read together rather than
as isolated personality traits.

## The method, and how it evolved

**Solscan link-pasting** is the constant. From the very first day —
`🄰🄽🄰🄳 🅂🅄🄹🄸` posting a raw transaction link four minutes into the
export ([26 Oct 2024](../../raw/logs/2024-10/2024-10-26.md)) — through
[[sergei]]'s multi-year run of dated wallet checks, a bare Solscan URL
dropped into the chat with no comment is one of the most common message
shapes in this archive. Reading it requires clicking through; the chat
treats the link itself as the argument.

**Automated cluster/bubble scans** show up early and recur. Patrick posts
a fully-formed bot-generated holder-cluster readout for the CA on
[31 Oct 2024](../../raw/logs/2024-10/2024-10-31.md) (*"Scanned 100 TH /
👤 Single: 94.0% wallet, 51.01% supply / 👥 Cluster: 6.0% wallets, 6.42%
supply..."*) — the same style of tool [[t]] references two months later
(*"You can easily check the cluster tho on bubble maps"* —
[6 Jan 2025](../../raw/logs/2025-01/2025-01-06.md)) and Sergei asks about
directly (*"Blockchain Bubblemap?"* —
[2 Apr 2025](../../raw/logs/2025-04/2025-04-02.md), followed five days
later by *"main central wallet of this cluster - H96kZr3aFNmVZt9A5e4FGH7ifcZGwvTvnHKUhda3BhXW"*,
[7 Apr 2025](../../raw/logs/2025-04/2025-04-07.md)).

**Manual narrative tracing** — following one wallet's transfers and telling
a story about them — is what most of the named investigators actually spend
their time on: Asiman walking the chat through the deployer wallet's
Coinbase funding within the first hour
([26 Oct 2024](../../raw/logs/2024-10/2024-10-26.md), see
[[launch-and-origins]]), [[marcin_krukowski]] pointing at a single-token
transfer as unfalsifiable proof (*"Afteral only one thing u cant argue.
$tateai is only one token moved from main adress and sent to new one. FOR
WHAT?"* — [27 Oct 2024](../../raw/logs/2024-10/2024-10-27.md)), and
[[0xvoid]] independently testing whether CEX-to-token transfers were
traceable in the same week.

**LLM-assisted investigation** is the newest and most methodologically
serious form, and it appears exactly twice in this material, both from
people who'd been doing manual versions of the same work for over a year.
[[widelton]] posts a full attribution-dossier methodology on
[15 Oct 2025](../../raw/logs/2025-10/2025-10-15.md) — deployer/bytecode
tracing, multisig checks, timing-correlation statistics, and a proposed
division of labor ("B. On-chain contract/deployer linkage... E. Timing &
statistical correlation... Assign people: one member does on-chain
deployer tracing; another runs holder/tx graph..."). It reads as a
professional-grade research plan; nothing in the sampled material shows it
actually being executed by the group. Seven months later, [[sergei]]
posts the real thing — a completed Phase-A run:

> "Testing Claude Code + Obsidian (Karpathy LLM-wiki idea) + Helius (for
> SOL api) for Tates public 4j... wallet investingation, scheme hunting...
> Issa is an active sybil funder with 7 clusters... Top 5 sybil hubs, new
> suspects: G9L2G5uCA…, CmvpPEK5j…, D3PdBbJt2…, 6cuHB5iEB…, each ring
> funded 396–486 wallets per day in November–December 2024. Three bot
> fleets of 45–74 wallets each, synchronized across different mints. Graph:
> 131k unique wallets, 5k mints, 194k aggregated edges."
> — Sergei, [18 May 2026](../../raw/logs/2026-05/2026-05-18.md)

Notably, this is also the first forensics post in the whole archive that
plainly lists its own failure modes (*"Gaps: what did not work... Snipe and
pump_dump returned 0 events because we did not crawl mint-creation
transactions"*) rather than presenting a conclusion as settled.

## What they were looking for, at three different moments

1. **Oct–Nov 2024, the ticker hunt** — is `$TateAI` the "real" coin? Early
   investigators (Asiman, Marcin, 0xVoid, plus dozens of one-off Solscan
   pastes) were building a circumstantial case for the ticker itself. See
   [[launch-and-origins]] and [[contract-address]] for the full saga.
2. **Nov 2024 – 2025, scam/rug suspicion** — once the ticker question
   quieted down, the same tracing habit turned inward, onto whether the
   project's own top holders were manipulating price. This is where [[t]]
   and, later, [[sergei]] spend most of their forensic energy.
3. **2025–2026, provenance and attribution** — [[widelton]]'s dossier
   methodology, Sergei's Helius/sybil-cluster work, and [[bob]]'s 2026
   cross-referencing of a US court filing against a wallet address (see
   [[bob]] for that specific claim — not repeated here) all aim at a
   different, harder question: not "is this the ticker" but "who actually
   controls these wallets and can it be proven."

## The same fact, read two opposite ways

The clearest illustration that this body of work never converged on a
consensus is a single wallet, nicknamed "BBY," that received 1,350 SOL from
Andrew Tate's public wallet. [[t]] reads the transfer as evidence of a rug:

> "Tate sent 1350 solana from his public wallet to the BBY wallet which is
> the one that was 'rugging' tate ai selling 50m per day to keep price
> down"
> — T, [16 Nov 2024](../../raw/logs/2024-11/2024-11-16.md)

Five days later, the *identical transaction* is posted as proof of the
opposite — that Tate is personally involved and TateAI is legitimate. The
line is first posted by a `Deleted Account` member and then reposted by
Ankh later the same day:

> "We finally have find our floor now and the blockchain evidence linking
> to Tate has only got stronger. So the BBY wallet (currently top holder of
> TATEAI) received 1350 from TATES public wallet
> '4jRX4iW2F5wBnfYMyB7RjS2PU5MjXrST3fB9DoV4BjHa'... This is confirmation
> that TATE knows this wallet and there is a plan in place for TATEAI"
> — Ankh (forwarding a `Deleted Account` post), [21 Nov 2024](../../raw/logs/2024-11/2024-11-21.md)

Same transfer, same wallet, opposite conclusions — bearish rug evidence to
one investigator, bullish confirmation to another, with no resolution
recorded in this material either way.

## Did any of it converge?

Mostly no, and the community's most rigorous internal analyst eventually
said so. By early 2025, [[sergei]] had shifted from gathering circumstantial
wallet evidence to openly doubting the community's other favorite piece of
"proof" — that Jupiter's token-verification tooling linked `$TateAI` to the
Tate Terminal X account — pointing out that the terminal never actually
posted the CA anywhere Jupiter could have used to verify it (see
[[contract-address]] for that exchange in full). His own running theory by
this point had moved away from "the wallets prove Tate personally chose
this coin" toward a colder read: that the whole terminal-coin ecosystem was
downstream of The Real World's marketing funnel rather than a genuine
Tate-endorsed project (see [[the-real-world-trw]]) — a conclusion built
*from* the forensics work rather than confirming its original premise.

The one place actual methodological improvement is visible is the jump from
2024's link-pasting and cluster screenshots to 2026's Helius-backed,
LLM-assisted graph analysis — real infrastructure, real numbers (131k
wallets, 194k edges), and, for the first time, an investigator willing to
publish what the method *couldn't* show. What none of these efforts ever
produced, across 2.75 years and at least six different named investigators,
is an external, independently-verifiable confirmation that Andrew Tate
personally controls or endorses `$TateAI`. The forensics got more
sophisticated; the underlying question stayed open.

## Related
[[sergei]], [[t]], [[marcin_krukowski]], [[bob]], [[widelton]], [[0xvoid]],
[[otter_krafter]], [[asiman]], [[nikola]], [[svyatoslav]],
[[contract-address]], [[launch-and-origins]], [[the-real-world-trw]]
