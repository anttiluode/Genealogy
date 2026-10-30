# October 30, 2026 — SweepAtlas and TransformerX: observed space versus learned inference-time state

**Scope:** Two new repositories in Genealogy's October 30 review. These are *independent artifacts*, not a joint architecture. [Live Genealogy wall](https://anttiluode.github.io/Genealogy/#oct30-atlas-transformerx) · [Structured pass](../../data/passes/october-30-sweepatlas-transformerx.json).

## TransformerX — from transient history to altered transformer computation

[Repository](https://github.com/anttiluode/TransformerX) · [Nine-run results](https://github.com/anttiluode/TransformerX/blob/main/results/FULL_SWEEP_2026-10-30.md) · [Audit CSV](https://github.com/anttiluode/TransformerX/blob/main/results/FULL_SWEEP_2026-10-30.csv) · [Merged PR #1](https://github.com/anttiluode/TransformerX/pull/1).

The pretrained experiment freezes DistilGPT-2, adds low-rank residual operators, a trainable reader/router and a bounded **64-number state per stream**, and trains those additions on a synthetic **silent changing-rule** task. No later labels enter the forward computation; the same current input can lead to different outputs depending on previous feedback. The repo explicitly credits RoundAndRound and LoopAImemory as inspiration, not inherited code.

### Source-reported nine-run main test (October 30)

Each router trains for 1,000 steps, uses the minimum-validation-NLL checkpoint and tests on **6,144 trials per seed**; seeds **7, 17, 27**.

| Model | Seed 7 | Seed 17 | Seed 27 | Mean test accuracy | Mean NLL | Trainable parameters |
|---|---:|---:|---:|---:|---:|---:|
| Interaction | 91.94% | 92.45% | 92.42% | **92.27%** | 0.22115 | 166,279 |
| Additive | 91.86% | 92.48% | 92.32% | **92.22%** | 0.22292 | 166,279 |
| Concat | 91.81% | 92.48% | 92.40% | **92.23%** | **0.21884** | **159,591** |

Same-stream no-history marginal mean: **80.46%**; known-model Bayesian reference: **92.89%**. These are stream means, not universal ceilings.

**Causal read test:** with the stored state retained but its output disconnected, average scores drop to **80.17% / 80.65% / 80.17%** (interaction/additive/concat). Gains from state read range **+9.81 to +12.96 percentage points** over the nine runs; reconnecting state gives exactly the original predictions. This establishes that **state access changes inference** in the trained system. The intervention removes both state-dependent routing and additive memory readout; it does **not** uniquely identify the multiplicative product features.

**Router comparison:** interaction beats concat by only **0.038 percentage points** averaged across seeds, seven net answers of 18,432. Concat uses **6,688 fewer trainable parameters (4.02%)** and has lower NLL in every seed. This is a useful correction against promoting extra router complexity from one good run.

**Boundaries and failures:** no-feedback means are **73.23% / 71.25% / 72.29%**; the ablation introduces a feedback token absent from training, so exact failure mechanism is confounded with distribution shift. Earlier supervised dictionary-language and occluded-vision experiments remain **23.96% / 24.74%**, roughly four-way chance. A frozen pretrained language backbone here does not imply an improved chatbot, arbitrary text generation, exceptional memory compression, lifelong learning, or victory over GRU/token/window baselines (not included in the nine-run sweep). There are three training-seed replicates; the source report and CSV were reviewed here, but **no new GPU training was run in Genealogy**.

**Suggested decisive next test:** compare concat and interaction against ordinary recurrent tokens, matched GRU and fixed-window history on *fresh* tasks, matched state/parameter/compute budgets, missing feedback seen during training and held-out long delays.

## SweepAtlas — a local observed-pixel world canvas, not full SLAM

[Repository](https://github.com/anttiluode/SweepAtlas) · [Usage and controls](https://github.com/anttiluode/SweepAtlas/blob/main/README.md) · [Main stitcher](https://github.com/anttiluode/SweepAtlas/blob/main/SweepAtlas.py) · [Video player](https://github.com/anttiluode/SweepAtlas/blob/main/SweepAtlasVideo.py) · [Image adjustments](https://github.com/anttiluode/SweepAtlas/blob/main/SweepAtlasAdjust.py).

The Python/OpenCV program captures webcam imagery or reads local video, detects ORB features, matches and verifies view alignment with RANSAC, and adds only **observed pixels** to lazily allocated **512×512** image tiles. It can reference earlier keyframes when tracking fails and can export an RGBA PNG with unobserved areas transparent. Video mode includes file loading, playback, a draggable timeline, frame stepping and 5-second jumps. Seeking is **preview-only**: it does not backfill or silently stitch skipped images.

Contrast and sharpness sliders change the preview and export **non-destructively** without changing the stored source pixels or feature matching. An alpha-preserving stripe processor sharpens large exports without allocating another full-resolution image. The source repo reports passing Windows CI, including synthetic planar geometry and video/seek/adjustment tests; these establish implementation checks rather than performance on diverse handheld real scenes.

**Not proved:** global pose optimization, metric 3-D scene reconstruction, SLAM, object persistence, unseen-content generation, or recovery from nonplanar parallax and moving objects. A successful large panorama is not a learned world model. The practical artifact is useful even if the research ambitions remain open.

**Suggested decisive next test:** record planar table/wall sweeps and a separate nonplanar camera walk with repeated visits and moved objects. Compare atlas versus direct frame retrieval and a standard stitcher on registration drift, change detection, scene recall and compute. Use a calibrated depth-aware method when evaluating genuine 3-D reconstruction.

## Genealogy links: fact vs proposal

- **[LoopAImemory](https://github.com/anttiluode/LoopAImemory) → TransformerX:** conceptual convergence; TransformerX README explicitly names it as inspiration. LoopAImemory uses trained readouts of synthetic history; TransformerX changes hidden computation in a frozen pretrained backbone.
- **[RoundAndRound](https://github.com/anttiluode/RoundAndRound) → TransformerX:** explicit conceptual inspiration, *not* inheritance of the slow residue-reawakening system or a proof of consolidation.
- **[Loopcraft](https://github.com/anttiluode/Loopcraft) ↔ SweepAtlas:** independent practical tools for video timelines, but Loopcraft makes GIF clips while SweepAtlas aligns overlapping observed pixels into a growing 2-D canvas.
- **[WorldModel](https://github.com/anttiluode/WorldModel) and [SihtiImageModel5](https://github.com/anttiluode/SihtiImageModel5):** **proposed integration only**. Their evidence-versus-imagination and remembered-versus-inferred pixel distinctions are natural discriminators for a future spatial memory stack. The current SweepAtlas code does not implement those models.

The unifying *research question* is not whether two unrelated October 30 projects already form one machine. It is whether **history can be accessible through both persistent observations (space) and a compact learned inference state (time), without confusing retained evidence with model-generated guesses**.

## Review methodology

This is a documentary source audit based on the repositories' October 30 README, scripts, stored test reports and TransformerX's merged PR #1. Numeric results are copied from the repository's own completed nine-run analysis; no model checkpoints were rerun by Genealogy and no real-world video benchmark was added here. The two new Genealogy cards, three carefully typed convergence edges, three motifs, three evidence receipts and two unresolved experiments are in the [structured pass](../../data/passes/october-30-sweepatlas-transformerx.json) and [evidence ledger](../../data/evidence.json).
