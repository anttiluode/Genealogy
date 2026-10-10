# CrystalMoon — a growing field becomes material, clock and lens

Reviewed 10 October 2026 at [`4adc6a3`](https://github.com/anttiluode/CrystalMoon/tree/4adc6a319bf9a84b6447a10e54b848d748808968). The source repository is unchanged by this review. [Open the world](https://anttiluode.github.io/CrystalMoon/).

CrystalMoon's strongest achievement is a usable connection between simulation and perception. A field grows structures, changes its local evolution speed, and changes the optical paths through which the observer sees it. Flight writes a decaying condition back into that field. The geometric moon gives this changing material another frame of reference and makes crossing into that view an action.

That puts it near AnttisBrain2's successful design: the mathematics has a consequence you can encounter. The committed screenshot displays a developed green crystal world at level 10. A screenshot establishes a rendered appearance, not its frame rate or the full interaction sequence.

## What the program actually does

| Component | Implementation | Consequence and boundary |
|---|---|---|
| Pattern formation | Nonconserved, quadratic-cubic Swift–Hohenberg relaxation on a periodic 64³ grid | A finite preferred wavelength grows into structured material. The grid, field and parameters are supplied; no images train the rule. |
| Local clock | Positive mobility `M(ψ)=1/(1+Tψ²)` | High-amplitude regions evolve more slowly. This changes the material's dynamics, not the player's clock or a relativistic metric. |
| Optical lens | Blur ψ² into ρ, set `n=1+κρ`, and integrate the projected refractive-index gradient along a ray | Material state alters the background and moon's appearance. The shader implements an optical toy; no quantitative ray-convergence or physical lens validation was reproduced. |
| Growth trace | Flight and clicks add a local trail to ε; the live trail decays with an approximately 150-second time constant | A previous action can change later growth at that address. CPU T6 tests a held growth bias and then abrupt removal, not the complete live decay/wake loop. |
| Inner view | Evaluate the second world's texture at the antipodal inversion of points inside the moon | Far distance is compressed near the centre. This changes coordinates, not the second world's governing PDE. |
| Descent | Promote the already displayed inner world; recycle the old buffer for the next level; seed it with `0.25*promoted_field + noise` | Two simulations suffice for continued descent. The old level is overwritten; a reproducible level law is not a saved world state. |

The general pattern-forming and crystal-growth mechanisms have established prior art. CrystalMoon's equation is most accurately described as nonconserved Swift–Hohenberg dynamics with a state-dependent mobility. Phase-field-crystal theory uses related free energy but conserves density; that dynamical distinction matters. See [Espath, Calo & Fried (2020)](https://doi.org/10.1007/s11012-020-01228-9) and [Elder, Katakowski, Haataja & Grant (2002)](https://doi.org/10.1103/PhysRevLett.88.245701).

## Why the appearance has a cause

The linear growth rate for a Fourier mode is proportional to

```text
ε − (q₀² − |k|²)².
```

It favours modes near |k|=q₀. Neighbouring voxels therefore participate in a selected spatial pattern instead of being independent decorative particles. Nonlinear terms limit growth and couple modes. Changing the displayed isosurface reveals different cuts through that same scalar field: separate peaks, connected necks or complementary foam-like structure.

For a fixed ε, the deterministic continuum equation can be written as a gradient flow of

```text
F[ψ] = ∫ [ −εψ²/2 + ((q₀²+Δ)ψ)²/2 − gψ³/3 + ψ⁴/4 ] dx
∂tψ = −M(ψ) δF/δψ.
```

Positive mobility then dissipates this energy. The live program also injects noise and changes ε through the trail, and uses explicit time steps. This continuum argument does not prove monotone energy for every rendered frame. The published linear step bound is not a global nonlinear stability theorem.

The same amplitude enters mobility, and its blurred square enters optics. That is an explicit causal connection between material state, rate and appearance. The clock and optical laws are separately chosen; they have not been derived from one spacetime action.

## What the moon's mathematics earns

The map is

```text
Φ(x) = c − R²(x−c)/|x−c|².
```

Away from its centre it swaps inside and outside, is its own inverse, preserves local angles and preserves orientation. Its derivative is a scale factor times a half-turn about the radial direction; on the sphere the scale is one. The camera handoff uses that rotation.

The map is singular at the centre, and its scale is R²/|x−c|². It is not a uniform contraction. AnttisBrain2's four-bounce rendering argument therefore does not transfer automatically. The apparent sequence of worlds here comes from two buffers and repeated replacement, not an infinite resident memory.

T8 checks a separate Kelvin-transform fact: multiplying the pulled-back harmonic field by R/|x−c| preserves harmonicity away from singularities. The crystal field is not harmonic, and the renderer does not use this weighting to evolve the inner simulation. T8's label “the inner world obeys the outer law” is broader than the result. The README already states the narrower boundary.

## Independently reproduced evidence

Command: `node tests/core.test.cjs` against the pinned source. **8/8 passed.**

- T1: deterministic level parameters; worst tested linear step product 1.50, below 2.
- T2: tested strong-growth condition remains finite; maximum |ψ| about 1.83.
- T3: about 68% of island voxels exceed the crystal threshold; far-sea maximum about 0.012.
- T4: radial spectral peak at mode shell 4, matching the selected wavelength.
- T5: reaching |ψ|=0.8 takes 1550 steps at T=0 and 1750 at T=6.
- T6: trail-supported maximum about 1.38; after removing the trail and evolving, about 0.002.
- T7: involution, radius product, conformality, antipode and boundary-frame errors all below 1e-13.
- T8: harmonic Kelvin residual about 1e-6 versus 0.87 for the unweighted pullback.

These are deterministic simulator checks. They do not establish BCC crystallographic order: a radial spectral peak identifies a length scale, not a lattice basis. They also do not validate interactive handoff, optical quality, hardware speed, semantic recall or useful computation.

Upstream reports a 25-step GPU/CPU difference of 1.5e-8 under headless SwiftShader. That GPU comparison was not independently rerun in this review. No real-GPU performance measurement was made here.

## Its place in the genealogy

**Documented:** AnttisBrain2 supplies the geometric/demo inspiration, and the Clockfield family supplies local slowing. The referenced May 2025 `crystal_kingdom.py` was not located in the currently indexed Clockfield repository; direct file ancestry is not asserted.

**Related ambition:** Cabbage and Janus made images queryable through coordinates and phase. CabbageFarmSihti asks how coarse geometry can organize fresh detail. CrystalMoon supplies a working spatial growth rule, but that rule is programmed, not learned from an example. These are useful comparisons, not established code inheritance, so this pass does not add those ancestry edges.

**Memory boundary:** MovingTarget2 defines memory through responses that survive change. CrystalMoon has action-dependent physical traces and partial inter-level inheritance, but no recall task demonstrating retained information. One-quarter field seeding can influence the next initial condition; whether that influence remains readable after its new law settles is unresolved.

There is a more specific timing boundary in `enterMoon()`: after promotion, the new child is seeded from the world just entered, not the departed outer world. That copy happens before exploring the promoted level. Its later flight trail therefore does not enter the already running child. The README's phrase “memory of the one you left” does not precisely describe the handoff. Current lineage carries a field at child creation, not the player's accumulated journey through its parent.

The strongest continuation would preserve the present interaction and investigate a real consequence: does inherited field structure carry recoverable information about an earlier world beyond what its new level law and noise already predict? A comparison with zero inheritance and spectrum-matched scrambled inheritance could distinguish retained spatial information from a transient warm start. That is a proposed experiment, not a feature or result of this update.
