# November 12, 2026 — TärinäSR: subpixel shake becomes image information

**[TarinaSR repository](https://github.com/anttiluode/TarinaSR/)** · [Play the browser lab](https://anttiluode.github.io/TarinaSR/) · [Benchmark JSON](https://github.com/anttiluode/TarinaSR/blob/main/results/benchmark.json) · [Realistic synthetic-camera stress](https://github.com/anttiluode/TarinaSR/blob/main/results/realistic.json).

## What was actually built

TärinäSR (GitHub repo `TarinaSR`) is a small ×2, grayscale, multi-frame super-resolution instrument. It **copies SihtiSR's single-frame code/model unchanged** to initialize a high-resolution estimate. It then estimates shifts by phase correlation, refines shifts and small rotations with Lucas–Kanade on blurred copies, holds 16 frames with their spatial motions, and visits four stored frames per incoming observation. Each visit subtracts the reprojected high-res estimate from a measured frame, then warps/enlarges that residual back to update the estimate:

```
residual = observation - downsample(blur(warp(x, motion)))
x += 0.4 * unwarp(blur(upscale(residual)), motion)
```

This is **classical iterative back-projection**, not native GeometricNeuronV27 logic, XOR pulse storage or an implementation of the three-temporal-offset phase hub. The ring metaphor connects conceptually to GoldOpus; PhaseLockedPredictiveCoding provides a shared-alignment theme, but **temporal frame-phase selection and spatial subpixel registration are different mechanisms**.

## Source-reported results — synthetic frames, no independent Genealogy rerun

Eight scikit-image photos, ×2 grayscale, 16 separately shifted/noised 8-bit low-res observations, shifts *estimated* rather than supplied:

| Method | Mean PSNR (dB) |
|---|---:|
| Bicubic, single frame | 30.90 |
| SihtiSR, single frame | 31.86 |
| TarinaSR, 2 frames | 32.57 |
| TarinaSR, 4 frames | 34.14 |
| TarinaSR, 8 frames | 36.01 |
| **TarinaSR, 16 frames** | **37.42** |
| Same 16 frames registered and averaged, then SihtiSR | 31.64 |
| Whole-low-res-pixel shake only, 16-frame ring | 32.05 |

The controls demonstrate why the small shifts matter: registered averaging loses phase information, while integer-aligned frames do not supply distinct subpixel samples. Mean registration error reported ~0.02 high-res pixels. Additional synthetic rotations ±0.3° and ±1° give 37.24 and 37.19 dB; ±40 high-res pixel shake gives 36.82 dB.

More realistic but still **simulated** optics (Gaussian lens blur σ 0.7 high-res px, JPEG quality 85, ±0.5° rotation): bicubic 29.33 dB; SihtiSR 29.99; no lens model 30.83; deliberately too-small lens 0.5 gives 31.53; matched lens 0.7 gives **32.06**; too-large lens 0.9 gives 31.63. Thus the strong clean-simulation +5.56 dB gain over SihtiSR narrows to +2.07 dB with the correct simulated lens, or +0.84 dB with no lens model.

## Proper scientific boundary

1. **Not new:** multi-frame iterative back-projection was published by Irani & Peleg (1991). Burst image SR with natural handheld camera tremor is established, including Wronski et al. (SIGGRAPH 2019). Motion estimation via phase correlation and Lucas–Kanade is standard.
2. **Not real-phone-validated:** the camera/video interface exists but source tests do **not** establish PSNR improvements on real phone footage. Moving objects, perspective change, rolling shutter, optical distortion and video compression can invalidate the rigid-motion model.
3. **Fairer comparison:** the eight test photos and synthetic acquisition regime are **different from SihtiSR's 200-image BSDS500 PSNR test**. Do not compare their absolute PSNR numbers as though obtained on the same benchmark. The TarinaSR benchmark includes its own *single-frame SihtiSR baseline*.
4. **Lineage:** SihtiSR → TarinaSR is real code/model inheritance. GoldOpus's ring idea is a conceptual extraction; PhaseLockedPredictiveCoding's alignment is a related theme, not the same implementation or temporal phase variable.
5. **Audit status:** Genealogy inspected the README, core algorithm, benchmark generation and committed JSON results; it did not rerun Python/JS tests or test real camera frames.

**Consequence:** This branch has a meaningful practical objective—let a person shake a phone slightly to recover detail that a single frame cannot sample—but its value will depend on observed results on real camera/video input and comparisons with conventional burst-SR baselines, not on novelty of the mechanism.
