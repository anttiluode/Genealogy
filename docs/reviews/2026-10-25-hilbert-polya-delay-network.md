# Hilbert–Pólya via Rajapinta–Takens delay loops

**Atlas review:** 2026-10-25 · **Source project:** [HilbertPolyaReintepretation](https://github.com/anttiluode/HilbertPolyaReintepretation) · **Source draft:** June 2026.

## The idea worth retaining

Instead of guessing a finite Hermitian matrix whose eigenvalues are the nontrivial Riemann-zero ordinates, the paper proposes a linearized complex phase network with delayed coupling. A closed network walk has a total delay. Assign primitive prime-associated walks transit times `log(p)`, repeated walks `m log(p)`, and special amplitudes. The proposed **Prime Orbit Condition** (POC) demands exactly the prime-power trace content and cancellation of extraneous loops.

The POC is precise enough to say what the model would need to realize. The gap is equally precise: **an actual self-adjoint delay-network operator realizing all those loop amplitudes with the needed analytic properties has not been constructed.** This is a reinterpretation of the Hilbert–Pólya existence question, not a proof of RH.

## What is present in the repository

- [Paper](https://github.com/anttiluode/HilbertPolyaReintepretation/blob/main/rajapinta_takens_rh_paper.md) — definitions, theorem/proof sketches, unproved Lemma 5.2 (the realizability gap), and a distinct claimed 700-site study.
- [Python prime-loop approximation](https://github.com/anttiluode/HilbertPolyaReintepretation/blob/main/truncated_poc_engine.py) — computes a smoothed truncated explicit-formula counting curve from the prime loops and a Riemann–Siegel theta approximation; predicts ordinate locations by half-integer crossings.
- [Figure](https://github.com/anttiluode/HilbertPolyaReintepretation/blob/main/truncated_poc_result.png) — plots the reported improvement with prime cutoff.

The README and paper report first-20-zero RMS going **0.114 (X=3) → 0.0052 (X=500)**. The code contains 20 published zero ordinates for scoring and plotting reference lines. The `N_X` reconstruction does not use them as input. Gaussian smoothing changes with cutoff: `sigma = 1.6/log(X+2)`.

This shows the expected action of a **truncated prime explicit formula**, not eigenvalues measured from a separately built phase network. The claimed 700-site `rajapinta_takens_operator.py` and its supporting output are **not present** in the repository listing reviewed here. These metrics and formal results have not been independently rerun or proved in this Genealogy pass.

## Proof boundaries to keep visible

The claimed weighted-inner-product self-adjointness of a retarded-delay history generator needs careful domain and operator-theoretic review; symmetric couplings/delays alone do not substitute for that proof. Likewise, recognizing matching *shapes* of loop expansions is not sufficient to establish equality to the completed zeta function without convergence, normalization, analytic continuation and exact coefficient controls. The de Bruijn–Newman threshold analogy is interpretive here; no new bound on its constant is derived.

The concrete unresolved research question is whether a reciprocal delay graph can satisfy the exact POC while controlling unwanted composite walks, remaining self-adjoint in the infinite limit. That, not the finite cutoff reconstruction, is where a meaningful new mathematical result would have to appear.

## Relationship to the wall

- [PrimeCrystalVST](https://github.com/anttiluode/PrimeCrystalVST) turns log-prime frequencies and delays into a *working audio effect*. It is a practical use of the same arithmetic ingredients, not a proof or implementation of the paper's required spectral operator.
- [BirthOfClockfield](https://github.com/anttiluode/BirthOfClockfield) retains the failed generic GOE/prime-trace comparison as a caution. A chaotic-looking spectrum does not automatically contain arithmetic prime data. The new paper asks for the stronger exact loop-level condition.

These are **conceptual convergences**, not claims of direct code descent. The wall keeps the June 2026 origin separate from the October 25 review date.
