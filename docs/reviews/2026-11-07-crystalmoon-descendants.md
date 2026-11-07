# November 7, 2026 — CrystalMoonV2 and NotKansas

[Live wall](https://anttiluode.github.io/Genealogy/#nov7-crystal-descendants) · [Curated pass](../../data/passes/november-7-crystalmoon-descendants.json)

Two missing repositories join the census (**597 → 599**). The existing CrystalMoon node is not duplicated, nor are Story2, ZetaDreamer3D or ZetaDreamer3DV2, which were indexed earlier today. These are real implementation descendants: **CrystalMoon → CrystalMoonV2 → NotKansas**. This audit is based on the source repositories' current READMEs and code descriptions; numbers below are source-reported, not independently rerun by Genealogy.

## CrystalMoonV2 — nested crystal and light-writing feedback

[README](https://github.com/anttiluode/CrystalMoonV2/blob/main/README.md) · [WebGL world](https://anttiluode.github.io/CrystalMoonV2/)

The original CrystalMoon periodic 64³ Swift–Hohenberg-type field, density lens, mobility-dependent clocks and inverted moon remain. V2 uses a coarse body field and fine lattice field with reciprocal growth feedback. It traces **16,384 ray-like photons** over several frames and deposits light into growth: crystal affects the ray path; the ray path affects crystal growth. A mirrored voxel correspondence couples worlds across the moon membrane; refracted glass permits vision past foreground crystals.

The source reports **12/12 CPU checks** and 25-step headless GPU–CPU numerical agreement around 10^-8. A synthetic light-guiding fixture reports rod illumination changing from **0.058 (straight rays)** to **3.0 (bent rays, capped)**. These are demonstrations of a particular ray-feedback rule, not Maxwell/Kerr wave solutions or real optical solitons. A reported 320×180 **SwiftShader** frame changed from **4.9 to 2.2 seconds** in optimization tests; no native RTX 3060 FPS has been established.

## NotKansas — hyperbolic interior and a mathematical exhibit

[README](https://github.com/anttiluode/NotKansas/blob/main/README.md) · [World](https://anttiluode.github.io/NotKansas/) · [Kaplansky page](https://anttiluode.github.io/NotKansas/kaplansky.html)

The V2 engine remains, while navigation/view rays inside the moon follow approximate geodesics of the **Poincaré ball**, metric `ds=2|dx|/(1-r²)`. A reflected **{4,3,5} hyperbolic cubic honeycomb**, five cubes meeting at each edge, generates repeating chambers. Its wall is infinitely distant in the metric, but the renderer has finite steps and a boundary cutoff. **Actual growth remains on a flat periodic 64³ grid**, sampled and mirrored in the chambers—not a Laplace–Beltrami crystal model.

The source reports **H1–H3 hyperbolic geometry tests** and **K1–K6 unit tests**. The separate exhibit visualizes **Giles Gardam's 2021 counterexample to Kaplansky's *unit* conjecture** in the torsion-free Hantzsche–Wendt group: 21-term factors, **441 products**, 121 resulting group elements and F₂ cancellations to the identity in both multiplication orders. It is **not** a new counterexample or a model of the November 2026 *zero-divisor* conjecture counterexamples in random hyperbolic groups. The honeycomb's Coxeter reflection group contains torsion and is not one of those groups.

## Typed source-supported lineage

| From | To | Type | Basis |
| --- | --- | --- | --- |
| [CrystalMoon](https://github.com/anttiluode/CrystalMoon) | [CrystalMoonV2](https://github.com/anttiluode/CrystalMoonV2) | **inherits** | V2 retains the existing field, clock, lens and inversion engine and extends it; [source](https://github.com/anttiluode/CrystalMoonV2/blob/main/README.md) |
| [CrystalMoonV2](https://github.com/anttiluode/CrystalMoonV2) | [NotKansas](https://github.com/anttiluode/NotKansas) | **inherits** | NotKansas keeps V2's simulation, light, membrane and camera and replaces the interior geometry; [source](https://github.com/anttiluode/NotKansas/blob/main/README.md) |

**Next controlled experiment:** compare the current flat 64³ crystal mirrored into hyperbolic chambers with a truly hyperbolic field simulation under a discretized Laplace–Beltrami operator, at matched sample and rendering budgets. Benchmark the native GPU before making speed claims.
