# November 11–12, 2026 — The ring, the blind archaeologist, Sihti residue and XOR madness

**Evidence status:** a source-linked historical audit, not an independent rerun of the scientific tests. The original November 11 V26/V27 genealogy pass correctly recorded V27 as a proposal *at that early checkpoint*; its later implemented work must be preserved as a correction, not overwritten as if it always existed.

## November 11 — four projects with different scientific purposes

- **[GeometricNeuronV27](https://github.com/anttiluode/GeometricNeuronV27)** retained the 2025 Perception Lab loop with hand-wired delay/attenuation cables. Later results: 8-/16-relay rings held 40/40 sampled patterns after 1,000 laps; a one-tick +12 setpoint pulse erased one selected event on 12/12 tested rings. Short dense all-ones patterns fail because the 50-tick variance machinery leaves the silent-relay regime. Classical delay-line memory, not endogenous synaptic learning.
- **[GeometricNeuronV28](https://github.com/anttiluode/GeometricNeuronV28)** retained the native loop and added a second original constant-1.0 ~59-tick clock. Coincidence of that clock and an eight-relay 32-tick ring drives a native receiver: 1,917/1,917 two-tick OR-window reads, 27/27 source patterns unchanged and 32/32 start phases sampled. Dense all-ones control only 55/71; single-tick externally scheduled reads 190/192. No arbitrary single-bit phase-query or trained weights.
- **[Tunnistus](https://github.com/anttiluode/Tunnistus)** gave an instruction-blinded Fable subject neutral names, documented rules and a black box containing four hidden variations. The beta subject committed 4/4 hidden modifications, 19/19 live/dead probes and 8/8 withheld predictions, then built clock and a 40-bit memory that held 4,000 ticks; reader gate not reached. Alpha committed nothing. Both runs stopped for usage limits. One seed/family, instructions-only blindness and a documented model; brute-force sweep baseline did not find memory.
- **[SihtiSR](https://github.com/anttiluode/SihtiSR)** uses 216 structure-tensor gradient-angle/strength/coherence buckets and one solved 25→4 linear map per bucket. ×2 grayscale BSDS500 (200 held-out images, 2×2 mean shrink): 29.45 dB vs bicubic 28.56, Lanczos 28.81, single global filter 29.09. Lock adds no measured PSNR. This independently re-encounters known RAISR-type super-resolution; no world-first interpolation claim.

[Moon](https://github.com/anttiluode/Moon) is already an independently curated November 11 item (formula-written light weights, inspired by but not a fork of HypaNet) and is not duplicated.

## November 12 — eight distinct pieces, one controlled argument

| Repository | Role | Boundary |
|---|---|---|
| [MuistoVaihde](https://github.com/anttiluode/MuistoVaihde) | Coprime 5×7 ring addresses, 35 explicit A/B weights, separate V2 P→A→B→END replay | Identical cue to different episodes merges the recalls; the transition table is engineered |
| [GN-XOR](https://github.com/anttiluode/GN-XOR) | Native 3-unit synchronous non-monotone comparator, plus seeded mismatch ring | One-tick lag breaks cancellation; seeded ring has no learning |
| [KultaaVaiKatinkultaa](https://github.com/anttiluode/KultaaVaiKatinkultaa) | Sol's native signed comparators and one-wire writeback | 255/255 eight-slot rhythms, but close source beats and jitter fail |
| [KultaaVaiKatinkultaaOpus](https://github.com/anttiluode/KultaaVaiKatinkultaaOpus) | Native one-wire versus signed pair and checkerboard-free window control | 31/33 native one-wire memory-exact vs 22/33 signed, window control 33/33 relative to emitted source; only 20/33 sources exact |
| [GoldOpus](https://github.com/anttiluode/GoldOpus) | Reduced window K-tick integrated rhythm looper | K=2j+1 tolerates bounded ±j jitter with sufficient hop; no tempo learning or native GN proof |
| [GoldSol](https://github.com/anttiluode/GoldSol) | Native history and signal_in jitter-rescue audit | No consistent benefit across 12 variants; 12/336 conditioned responses all at two-tick recovery |
| [GoldGemini](https://github.com/anttiluode/GoldGemini) | 64×64×4 buffer-backed reduced XOR memory lab | 16,384 logical streams/262,144 stored bits at period 16, not native Geometric Neurons |
| [PhaseLockedPredictiveCoding](https://github.com/anttiluode/PhaseLockedPredictiveCoding) | One shared phase choice among t−1,t,t+1 remembered frames | 128/128 phase matches, 77,071→0 false bits (no intrusions), 768/768 injected novelty (with intrusions). Synthetic templates, not camera motion |

**Mechanism:** `error = world XOR ring`; the one unsigned mismatch pulse, fed back through the nonlinear firing band, writes an absent pulse or suppresses an obsolete one. Algebraically `ring_next = ring XOR error = world`. This is T-flip-flop/delay-line state logic. The 25-line abstract window unit reproduced all 255 core rhythm results, about 17× faster than full native GN27. The checkerboard is not needed for this capability.

**Scientific boundaries:** logic, nonmonotonic band gating, delayed memory, coincidence filtering, global template alignment and predictive-error feedback all have established prior art. The exact self-error-wiring may still be a distinctive *construction* but an initial targeted prior-art search does not establish priority. Native GN-only leaks and a 59-tick oscillator are not a demonstrated advantage. A shared temporal phase selector is *not* a spatial camera-movement compensator, GPU acceleration result or learned PLL. Its out-of-range, independently moving regions and phase-masquerade failure cases remain explicit.

**What remains open:** Can a native nonlinear recurrent machine make useful history-conditioned decisions that the small window/digital-buffer baseline cannot? Could multiple rings interact through a persistent shared complex state to change routing? None of the eight repositories establishes that larger architecture.

[GoldOpus playable looper](https://anttiluode.github.io/GoldOpus/) · [GoldGemini browser demo](https://anttiluode.github.io/GoldGemini/gn_ghost_16_384_self_writing_xor_rings.html) · [Genealogy wall](https://anttiluode.github.io/Genealogy/).
