# November 5, 2026 — three vine worlds, three different jobs

**Repositories:** [Emergence3DSol](https://github.com/anttiluode/Emergence3DSol) · [Köynnös](https://github.com/anttiluode/Koynnos) · [PsychedelicGarden](https://github.com/anttiluode/PsychedelicGarden).  
**Atlas:** [live wall](https://anttiluode.github.io/Genealogy/#nov5-vines-chains) · [curated pass](../../data/passes/november-5-vines-chains-and-garden-worlds.json).

## The question behind the pictures

A climbing vine gains reach by gripping something it did not build. Each tip may detect contact but may not know the accumulated load at the distant pin holding the scaffold. Could local searching and inherited policies exploit borrowed support, and when does that advantage become a liability for the whole structure?

The November 5 repositories take **three different routes**. Similar vines and chains are a motif, **not proof of shared code, actual evolution, or a learned world model**.

## 1. Emergence3DSol — a testable support economy

[README and methods](https://github.com/anttiluode/Emergence3DSol/blob/main/README.md) · [experiment runner](https://github.com/anttiluode/Emergence3DSol/blob/main/experiment.py)

This is an explicit **implementation descendant of Emergence3D**, which itself embeds Emergence-style genomes into a *supplied* 3D voxel ecology. Inert vertical rods occupy and shade voxels; cells sense rod and foreign-body proximity, may emit a grip decision, and pay an altitude-dependent synthetic stress cost discounted by contact. A heritable phase biases horizontal and upward growth when a support is held. The phase-guided search rule is *programmed*, not an evolution-discovered circumnutation mechanism.

Four proposed comparison arms use matched seeds: **vine**, **grip without twining bias**, **no grip**, and **no rods**. The first three retain the same physical rod obstacles and shading. An additional timed rod-severing intervention tests dependence on the scaffold. Diagnostics report grip fraction, near-rod opportunity and high-cell occupancy.

**Evidence boundary:** the README documents code, integration checks, controls and hypotheses; it does **not** publish a multi-seed outcome demonstrating a survival or altitude advantage. A gorgeous spiral alone cannot establish an adaptation. The contact discount is an energy bookkeeping rule, not a force/tension model. A future comparison should report seed-wise survival, high-light occupancy, energy cost and post-sever collapse, with and without contact, at equal environmental difficulty.

## 2. Köynnös — local senses versus a distant pin

[Live garden](https://anttiluode.github.io/Koynnos/) · [README](https://github.com/anttiluode/Koynnos/blob/main/README.md)

Köynnös is a **procedural browser instrument** using Three.js rather than an extension of the PyTorch voxel solver. Unattached tips sweep with finite reach; touching a post, tree, chain or mature stem can form new support. Hanging chains collect load from vegetation; their pins fail above a capacity. A fig-like species may respond by growing downward roots, sometimes unloading the pin. A 2D evolving field with a slowly accumulated memory layer can generate crystals that attract growth and are perturbed by visitors.

The page provides manual interventions—toggle circling search, load-sensitive fig roots, vine-on-vine support, field display—plus seed fragments and pin-capacity visualizations. These are **interactive comparisons**, not pre-registered causal controls across matched seed ensembles. There is no trained neural model or biologically calibrated structure in this garden.

The genuinely new *question* compared with Emergence3DSol is whether a local policy can compensate for **load accumulated at a remote shared attachment point**. To test it, track outcomes at matched seeds and fixed growth budgets, compare informed figs against blind/always-root controls, and score both pin survival and organism fitness.

## 3. PsychedelicGarden — turning growth into progression

[Source](https://github.com/anttiluode/PsychedelicGarden) · [README](https://github.com/anttiluode/PsychedelicGarden/blob/main/README.md)

This branch explicitly reports **AnttisBrain2 Descent** as its source engine: a single WebGL2 raymarcher, hash-generated rooms, mirrored moons and a webcam-reactive boundary. Chained moons acquire SDF vines, leaves and blooms. A level hides a gold key moon behind a vine cage; local motion—webcam activity or flying around the room—feeds growth, the cage opens, and the key unlocks the next room's seal.

That is an **authored gameplay loop** rather than a selection experiment. Its README reports a headless shader/game-logic check, but not an on-GPU frame-rate measurement. The extra SDF steps could make scenes expensive, so real-device performance and whether players understand the grow→key→gate loop remain unmeasured.

## Inheritance without collapsing distinct implementations

| Connection | Genealogy type | Why |
|---|---|---|
| Emergence3D → Emergence3DSol | **inherits** | The same original voxel ecology is extended and controlled. |
| Emergence3DSol → Köynnös | **converges** | Köynnös explicitly names the related evolutionary support branch, but uses a separate browser model. |
| PsychedelicGarden → Köynnös | **converges** | Shared vines/chains imagery; separate game and garden engines. |

PsychedelicGarden's **AnttisBrain2 Descent** source ancestry is recorded in its node and this review, but no graph edge is added to the older engine until that parent has a verified curated node in the atlas; linking to an unreviewed ID would create a dangling edge.

## Surviving research question

Can a system that only sees local support contacts learn or evolve a policy that improves **held-out whole-structure survival** while accounting for hidden shared failure costs? A credible test needs matched obstacles, budgets and seeds, a blind local policy, a policy that sees pin load, a no-contact control, and sever/load interventions. This remains an open problem. The browser demonstrations are valuable independently as visualization and game design.

*All capabilities above are sourced from repository READMEs and inspected repository structure. Genealogy did not independently run these programs or verify GPU performance.*
