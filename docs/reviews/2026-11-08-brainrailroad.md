# November 8, 2026 — BrainRailRoad: the railway attempts to learn

[BrainRailRoad repository](https://github.com/anttiluode/BrainRailRoad) · [Offline hard-event lab](https://anttiluode.github.io/BrainRailRoad/) · [Live genealogy chapter](https://anttiluode.github.io/Genealogy/#nov8-railway-causality) · [Curated pass](../../data/passes/november-8-brainrailroad-hard-event-learning.json)

**Position in the family:** TurntableNeuron supplies receiver phase windows and phase-addressed output; TurntableAISol explores multilayer yards with apical, basket and chandelier roles. BrainRailRoad makes those ideas into a 12-hidden-yard, two-output hard-event classification network with a supervised surrogate-gradient training system. Both KasvavatKiskot projects are same-day conceptual relatives for timing and candidate rails, **not inherited route-growing code**.

## The machine, not just the illustration

The [project README](https://github.com/anttiluode/BrainRailRoad/blob/main/README.md) and [model code](https://github.com/anttiluode/BrainRailRoad/blob/main/circuits/model.py) specify 90 candidate directed rails, 36 active from fixed destination quotas; four release addresses 0, 8, 16 and 24 ticks on 32-tick exit clocks; learned delay and port/weight candidates; simulated apical gain, basket shunting and chandelier veto. The supervised task is contextual A/B order XOR context, with seeded manifests and a tie treated as an error. The browser runs the **real exported hard forward engine** with rail damage, jitter, packet logs and model import. Its bundled reference is **random/untrained**.

The original release reports **14 Python tests**, **16 Python↔JavaScript event-trace fixtures**, and **8 baseline parity fixtures**. Straight-through BPTT has finite nonzero gradients, including for candidate/delay and phase-dependent parameters. These are source-reported engineering controls, **not evidence of successful learning**.

## Scientific negative result: silent outputs

The first threshold initialization at 0.35 drove output counts to zero and tied predictions; 0.20 and 0.16 development attempts also collapsed toward abstentions. The README explicitly retains this negative result. Training loss near ln(2) is not a classification win. Full five-seed railway training, topology/phase/delay ablations, lesion recovery and claimed 95%/85% targets remain unachieved or unrun.

## Control that actually learns

The separate GRU comparator has **15 hidden units**, **977 trainable parameters**, and a final prediction read at **tick 127**, after the stimulus. Five development seeds trained for **700 updates**, checkpoints selected using validation, and separate frozen 2048-example evaluation manifests used afterwards. Reported median accuracy:

| Frozen evaluation | Five-seed GRU median |
| --- | ---: |
| Unseen interpolation gaps | **100.00%** |
| Independent ±2-tick jitter | **99.61%** |
| Out-of-range gaps | **95.12%** |

[Machine-readable five-seed GRU receipts](https://github.com/anttiluode/BrainRailRoad/blob/main/circuits/results/gru_five_seed_development_summary.json). The earlier tick-319 GRU failed to learn in one development probe, so changing the readout was a labeled **development intervention**, not a stealth gain for the railway. The GRU result proves the task can be learned under that comparator; it **does not** establish a trained railway, superior inference efficiency, local growth, or a fair matched-energy result.

## Follow-up rescue — the zero-vector credit bottleneck (November 8)

[Measured rescue protocol, source data and reproducibility instructions](https://github.com/anttiluode/BrainRailRoad/blob/main/circuits/RESCUE.md).

Claude's later CPU rescue uses **one seed (11)**, identical training batches across the four combinations (absolute/stimulus-reset clock × penalties on/off), a separate 128-trial dev selector, and **512 held-out validation trials scored through the float64 hard reference**, not an analog surrogate. This is *order only*; the full context-XOR task was not retested.

| Random-onset configuration | Hard validation accuracy | Abstentions |
| --- | ---: | ---: |
| Absolute clock, penalties on | 0% | 512/512 |
| Absolute clock, no penalties | 0% | 512/512 |
| Stimulus reset, penalties on | 19.7% | 411/512 |
| Stimulus reset, no penalties | 50% | 256/512 |
| Stimulus reset, no penalties, 600 updates | 50% | 256/512 |

On fixed-onset order-only trials, the original clock likewise reaches **50% with 256 ties**. Both that model and the randomized-onset reset model possess an *order-discriminating* fire-versus-silence code: one input order produces output events, the other produces none. The design deliberately counts a tie as an error, so one-sided discrimination is **not** successful two-class hard-event classification.

The optional label-neutral first-source pilot reaches all 14 yards, resets their 32-tick phase reference and costs **14 counted pilot deliveries per trial**. It is exported and mirrored in JavaScript; the original clock remains default. Source reports 12 reset parity fixtures, exact 512-trial decision/count parity of a trained reset export, and full event-trace agreement for the first 24.

**Mechanistic failure:** class-zero trials have zero H2 and output events; when integrated complex vector z is zero, the derivative of its magnitude with respect to upstream inputs is zero. Removing the empty-yard surrogate fire mask adds gradients only to thresholds, not operational rail weights, topology or delays; those remain zero in the measured probe. Further 600-update optimization is therefore a fixed point, not a missing learning-rate sweep. The proposed differentiable scalar-load credit path is a **new backward estimator, not yet tested**, and must preserve the original hard forward and valid scoring rules.

**Historical comparison:** [JelloBrain](https://github.com/anttiluode/JelloBrain) S3 restored a trapped spatial route from 0 to 1.0 via context-specific prediction-error exploration; this is *an analogous credit/trapping issue*, not a demonstrated cure for a zero-vector Jacobian. [NSSN2](https://github.com/anttiluode/NSSN2) prediction-residual learning partially repaired Hebbian damage but lost to its frozen control; no direct dead-output cure is demonstrated there either. [SilentPing](https://github.com/anttiluode/SilentPing) showed that neutral pings can read activity-silent state, a different inference/memory question.

**Decision:** keep the original negative railway-learning verdict. The rescue makes the *clock* hypothesis partially supported and localizes the next falsifiable optimizer intervention.

## What genealogy should preserve

- **TurntableNeuron → BrainRailRoad**: timed reception and phase release extracted into a new hard-event architecture.
- **TurntableAISol → BrainRailRoad**: multilayer biological-role analogues extracted as computational controls, not verified copied files.
- **KasvavatKiskotSol / KasvavatKiskotClaude → BrainRailRoad**: *convergence*, not ancestry: those routes receive destination reinforcement; BrainRailRoad's candidate rails are searched with a global supervised loss.
- **Remaining question**: can the sparse hard-event circuit learn robustly without a hidden differentiable shortcut or label-leaking browser animation? Compare frozen accuracy, event counts, compute, jitter and damage recovery against a task-matched GRU.

This is a **seventh distinct November 8 railway-family repository** added after the earlier contribution tally of six projects. The previous 15-commit historical record is left intact. The Genealogy census changes **604 → 605**.

*Provenance:* architecture, test counts and results above are from BrainRailRoad's README and saved receipts; this genealogy update does not claim to independently reproduce the model training.
