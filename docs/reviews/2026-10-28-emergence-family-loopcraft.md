# October 28, 2026 — Emergence, Emergence2, EmergenceAstra and Loopcraft

## Scope

Four newly created public repositories were absent from the 550-project Genealogy census before this pass. This review adds them once to the census and the live wall. It separates direct source ancestry, conceptual common ground, and an unrelated creative utility.

## 1. Emergence — mutating instructions interpreted by a fixed machine

[Emergence README](https://github.com/anttiluode/Emergence/blob/main/README.md) describes cells on a GPU grid with lineage-specific token genomes, a shared fixed transformer that interprets those tokens together with a lineage-state token, and a fixed cell action network. Genomes mutate at birth. Cells grow as attach/detach bodies, consume food, share and steal energy, signal, age and die. The design of these action possibilities is explicit; particular genomes and shapes are not scripted.

A source-reported 128×128, 30,000-step CPU pilot shows a collapse in founder diversity, transient larger attached bodies, and later selection for small grazing organisms. The README correctly rejects genome-length increase as evidence of adaptation without correcting for the bias introduced by insertions and duplications. A million-step GPU trajectory and durable multicellularity remain experiments, not confirmed results.

## 2. Emergence2 — an explicit second layer, with a hard baseline

[Emergence2 README](https://github.com/anttiluode/Emergence2/blob/main/README.md) identifies Emergence as level one and adds moving hunters: shared conv/GRU actor-critic learning, world-model prediction, danger traces available to cells and deliberately written marks available to hunters. Thus the typed **Emergence → Emergence2 / inherits** link has documentary basis.

The source reports that learned hunters can beat random walkers in a simplified frozen-world sanity check. In the full regrowing ecology, however, learned hunters have not convincingly beaten a cheap **straight-line with occasional turns** baseline. The world model has not yet beat copying the prior frame. Probing latent features, showing a hunter actually uses marks rather than writes them, and observing evolved prey defenses require separate tests. Reported predator–prey cycles are within engineered model dynamics.

## 3. EmergenceAstra — a genuinely different mechanism, not a fork

[EmergenceAstra README](https://github.com/anttiluode/EmergenceAstra/blob/main/README.md) describes independent random byte-token genomes that initialize sender, receiver and developmental tables. Cells locally update communication policies from pairwise catalyst outcomes, build/prune bonds, use energy and bud mutated descendants. Unlike Emergence, the sender and receiver tables learn within a lifetime, while learned policy weights are **not inherited** by a child. The development rule is fixed after initialization, although changing inputs can select different actions.

The balanced diagnostic's shuffled and muted baselines are mathematically one-third. They do not by themselves show an emergent symbolic language, evolutionary usefulness, or ecological self-sustenance. The two requested tests should remain separate: learned conventions in a stationary ring versus persistence when births, deaths and changing partner neighborhoods are enabled. The project itself flags population-ceiling artifacts.

We do **not** draw an 'inherits' or 'forks' edge from Emergence to EmergenceAstra. They converge conceptually on asking what inherited genomes and lifetime changes can generate, but source-level ancestry is not shown.

## 4. Loopcraft — a shipped utility rather than a research claim

[Loopcraft README](https://github.com/anttiluode/Loopcraft/blob/main/README.md) documents a local YouTube/video → GIF GUI built with tkinter, yt-dlp and FFmpeg via imageio-ffmpeg. It exposes a full-video overview plus a zoomed detail timeline, IN/OUT markers and timecodes, silent preview, source speed, FPS, crop/pad/stretch and palette export.

October 28 fixes address the long-video selection issue by defaulting to an eight-second zoomed clip, add Apply times to commit both timecodes together, and pin Save As / Create GIF outside the scrollable settings area. This is useful for capturing world simulations, but that use is a workflow relationship, **not** code descent from the Emergence repositories.

## What this pass claims and does not claim

- Documentary: four current repositories, descriptions and URLs; Emergence2 extends Emergence.
- Mechanistic: evolution of inherited instructions, online learning of predators, and local learning of communication are distinct processes.
- Not shown: open-ended digital life, beneficial evolutionary multicellularity on large worlds, predators modeling their world better than simple controls, stable learned mark conventions, or emergent language sustaining an ecology.
- Evidence provenance: repository READMEs and their referenced experimental scripts; Genealogy did **not** independently run the worlds or test the GUI on Windows.

The useful forward comparison is not *which one looks most alive?* but *which adaptation mechanisms preserve a measurable advantage over simple resource-matched controls and across ecological turnover?*
