# Mad Monday — 19 October 2026

> One 3 a.m. intuition. A day of testable detours. Not ten independent breakthroughs.

**This is an intellectual-history entry, not a claim that one biological theory was proved.** It records the prompt that started the day, the divergent experiments, their controls and the revised question that survived. The reported numbers come from the linked projects and PRs; Genealogy did not independently rerun those experiments.

## The ignition: a dendrite as a distributed local lens

The morning question, in the researcher's own language:

> *What does the dendrite do? Purifies. But how can it be good to lose detail? Aha: it breaks signal into gradients. What does soma do? Summates gradients. Live gradient descent! And ping: it fires to keep the ball rolling.*

The motivating contrast with early PerceptionLab checkerboard/homeostatic-node experiments was concrete: returning **four brightness samples** versus returning **four directional differences** to the same feedback controller. The hypothesis was that purification might move information into local differences and a history-dependent response, rather than simply remove it. Gemini's conversation catalyzed the image/soma/return interpretation; Claude, Sol, other model instances and the researcher then explored different paths.

Three distinct mathematical meanings of “gradient” must be kept separate:

1. **Spatial voltage or image differences**: local slopes that may produce currents via conductances.
2. **Temporal differences**: `v(t) − v(t−1)`, another way of presenting the same history to a reader.
3. **Learning gradients**: derivatives of a task objective with respect to a state or parameter.

A passive electrical network can descend an explicitly defined voltage energy without establishing that dendrites perform backpropagation or learn the perceptual task's loss gradient.

## The day's branching trail

| Path | Research question | Source and bounded result |
| --- | --- | --- |
| [SihtiBrain](https://github.com/anttiluode/SihtiBrain), [V2](https://github.com/anttiluode/SihtiBrainV2), [V3](https://github.com/anttiluode/SihtibrainV3) | Can the first soma read be blind while a state-dependent return reveals branch-local distinctions? | Consolidated [research map](https://github.com/anttiluode/SihtiBrain/blob/main/docs/RESEARCH_MAP_2026-10-19.md): V2 echo −0.11495, after-reset conductance echo −0.04817. Fixed linear ping is blind. V3 adaptive and preset phases tie; averaging phases cancels direction and tracking loses 0.615 vs 0.781 to velocity extrapolation. |
| [AIBrain](https://github.com/anttiluode/AIBrain), [AIbrainV2](https://github.com/anttiluode/AIbrainV2) | Can experience change a response operator that an incoming cue reads? | At load 32 AIBrain scored 71.9% vs 95.4% matched Hebbian memory. AIbrainV2 improved graph response versus raw weights, but degree normalization nearly accounted for it (55.6 vs 53.4% overall), with indexed lookup at 73.9%. |
| [RealTimeReadWriteClaude](https://github.com/anttiluode/RealTimeReadWriteClaude), [SihtiStack](https://github.com/anttiluode/SihtiStack) | Can a frozen language model find an address or use a returned middle-layer activation? | Contextual address recovered by a learned linear diagnostic is not native autonomous storage. The archived Qwen activation-return gate was negative (2/12); a residual-stream bookkeeping identity does not imply recoverability from its final sum. |
| [SihtiImageModel3](https://github.com/anttiluode/SihtiImageModel3) | Can learned top-down coarse fields tell missing local patches how to reconnect? | [R3](https://github.com/anttiluode/SihtiImageModel3/blob/main/docs/GATE_R3_RESULT.md): privileged coarse oracle 0.08408 MSE versus 0.10151 learned control, but ordinary learned feedback still fails. [R4](https://github.com/anttiluode/SihtiImageModel3/blob/main/docs/GATE_R4_RESULT.md): predicted mean+signed flux 0.08020 versus mean alone 0.08480 pixel MSE; **edge error worsens** 0.05337 → 0.05632, so the combined gate fails. |
| [Sihtiimagemodel4](https://github.com/anttiluode/Sihtiimagemodel4) | What should the top-down message contain, and can a ping improve reconstruction? | Predeclared gradient follow-up: **true structure-tensor orientation** 0.0272 synthetic MSE vs true brightness 0.0451; ordinary predicted orientation is not established. Signed summed gradients *alone* are worse than true brightness. Its ping fails sham comparison; natural test covers only three source photos. |
| [BrainAsInverseModelerV3 PR #3](https://github.com/anttiluode/BrainAsInverseModelerV3/pull/3) | Is a raw scalar soma reading the right coordinate system for a forecast during a blackout? | On four fresh held-out trajectories, same 19 samples: raw soma 0.674525 NRMSE; voltage differences **without** pulse 0.393459; with pulse 0.395142. The invertible transform improves this fixed reader; no new information was created and the pulse does not help the primary gate. **PR was open at the time of this record.** |

**[Local Lens Lab](https://anttiluode.github.io/Genealogy/demos/local-lens-lab.html)** ([offline HTML source](../../demos/local-lens-lab.html)) was also built as a standalone offline teaching instrument: movable contour/chessboard/stripe patch; four signed differences versus brightness; waiting cable activity, leak/geometry proxies, optional context and return, and Oja normalization on weights. It illustrates the feedback workflow; it is not a validated biological simulator or image-recognition benchmark.

## A correction to the tempting “one mathematical bug” diagnosis

The three uncomfortable results **suggest a shared question about sufficient representation and readout coupling**, but do **not** establish that every failure comes from the same mathematical bug.

- A block mean removes orientation. That can obstruct the intended edge-continuation message.
- Replacing the mean with the **sum of signed first derivatives** does not fix everything: opposing edges cancel, and their location within the block is still unknown. Model4's better privileged readout was a **second-order structure tensor**: `(gx², gy², gx·gy)`. This retains dominant orientation but not exact polarity or position.
- A measured image-space gradient only helps a learned or constrained decoder when there is a path from the message into the decoder's actual controls. A true oracle message demonstrates potential; predicting the hidden message from visible inputs is a separate problem.
- In the cable, `v(t) − v(t−1)` and raw `v(t)` are invertibly related given one anchor. The observed win is a change in **conditioning/regularization of a fixed reader**, not proof that spatial gradients or probe echoes encode new memory.
- A state-dependent pulse may expose hidden operator structure under controlled conditions; in other settings it adds no useful forecast advantage. A ping that moves a model into a deeper minimum need not produce a more truthful image.

## The core that outlived the detours

```text
experience / input
       ↓
local medium holds a distributed, evolving state
       ↓
a limited readout exposes only part of it
       ↓
a question, perturbation or context enters THROUGH that medium
       ↓
the response depends on what remains and how it is coupled
       ↓
future processing may change; learning requires a separate test
```

This is the most defensible cross-repository inheritance. **What persists? What does a given reader discard? What does a controlled return actually make usable?** Sihti's decomposition, PerceptionLab's homeostatic loop, image patch lenses, dendritic cables and writable operator memories are different instruments for asking that question. Some gates worked, several failed, and neither result should be erased.

## Curation decision

Keep the earlier **one surviving SihtiBrain card** and its nine preserved receipts. Add independent, reviewed cards for **SihtiImageModel3** and **Sihtiimagemodel4** because they test different image reconstruction operators. Retain the existing **BrainAsInverseModelerV3** card while explicitly linking to its *open* PR #3. Link the AI/memory side projects as historical branches; do not inflate them back into separate curated survivor nodes. Negative gates are in [empirical evidence](../../data/evidence.json) and the [Mad Monday pass](../../data/passes/october-19-mad-monday-image-gradient.json).
