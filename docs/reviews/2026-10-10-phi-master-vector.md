# The master-vector idea, revisited through its actual reader

**The enduring idea is a hidden state whose appearance depends on the lens through which it is read.** This is a useful origin of Antti's field/observer questions even though the cosmological conclusions outrun the code. The return to phi-world-theory should recover that idea as well as correct its measurements.

Reviewed snapshots: [phi-world-theory `4ce6f58`](https://github.com/anttiluode/phi-world-theory/tree/4ce6f58c586993b5627cbeea6e6662780e1fadb9), [SpaceScreensaver `0024b59`](https://github.com/anttiluode/SpaceScreensaver/tree/0024b592d24f1b1880c9b444de7fcc21b0142141), and [MoonFormer `ef26aef`](https://github.com/anttiluode/MoonFormer/tree/ef26aeff37a70ad5142e2b26b0eda333a83708a2). Upstream source is left unchanged.

## The origin is documented

The phi README explicitly calls its 1,000-number vector a return to the earlier fictional SpaceScreensaver scenario and says that screensaver helped originate `best.py` and the field ideas. Its archived `SpaceScreensaver.py` matches the older repository's `Space_Screensaver.py` apart from one leading blank line after newline normalization. That is actual source ancestry. December 2024 is the older public repository's creation date; it does not date the author's first thought.

The inspected screensaver contains multiple 128-component particle cores, positions, velocities and a spatial field. The later single-global-vector scenario is an interpretation and a separate construction. `best.py` also contains an unusual idea worth retaining: stable detected field regions can be promoted into local sub-simulations and coupled back to the parent. That is source-inspected nested dynamical architecture, not proof of spontaneous minds or learned local physics.

The original Genealogy entry already retained the simulate → predict/extract → perturb → analyze workflow. This revisit gives equal visibility to another durable question: **what must an observer do to distinguish two underlying states that currently produce the same view?**

## What the master-vector scripts compute

In `findmastervector2.py`, twelve supplied icosahedral directions are extended with hand-chosen decaying complex harmonics to form a row-normalized matrix $A\in\mathbb C^{12\times1000}$. The optimizer changes a normalized vector $u$ while keeping the lens fixed:

$$a=Au,\qquad R(u)=\sum_i|a_i|^2=u^*A^*Au.$$

It maximizes this response sum while penalizing unequal response magnitudes. The script's `target_amplitudes` variable is unused. It does not learn the lens from the `best.py` trajectory, derive a physical law, or test whether the optimized state reproduces the nonlinear world's perturbation responses. The first master-vector script instead tries a 3-D field loss with Nelder–Mead, not gradient descent; its percentile-selected voxel count is not a local-maxima or connected-component count of twelve vertices.

The direction set and embedding already contain the desired geometry. Optimizing a state to excite those supplied directions is a valid inverse-design exercise. It is not evidence that the geometry was discovered as the source of a universe.

## Why 131.47% is possible

Row normalization makes each reading individually bounded; it does not make the twelve rows mutually orthogonal. Their Gram matrix is $G=AA^*$. An independent Float64 reconstruction gives:

| Quantity | Measured value |
| --- | ---: |
| Complex rank | 12 |
| Invisible complex dimensions | 988 |
| Smallest / largest Gram eigenvalue | 0.650419 / 1.399634 |
| Largest pairwise row overlap magnitude | 0.146078 |
| Maximum raw summed response of a unit vector | **139.963354%** |
| Correct orthogonal projection fraction for that maximizing vector | **100%** |

Overlapping measurements can count the same component repeatedly. The appropriate squared norm of the orthogonal projection into the observed subspace is

$$\|P_{\rm obs}u\|^2=a^*G^{-1}a,\qquad P_{\rm obs}=A^*G^{-1}A.$$

This stays at or below $\|u\|^2$. The reported 131.47% is compatible with overlap gain and balancing in the stated lens. This audit demonstrates that explanation without claiming to reproduce that particular unseeded PyTorch run. No extra energy or holographic physics is established.

The twelve unit 3-D directions do form a tight frame of their **three-dimensional** space: $K^TK=4I$. The hand-built 1,000-D extension has unequal nonzero frame eigenvalues and a 988-dimensional nullspace. The former identity should not be transported to the latter representation. For an isotropic unit vector, the expected raw response sum is $12/1000=1.2\%$; that dimensional average is not a measured fraction of semantic information or an entropy calculation.

## The deeper result: many sources, exactly one view

For this fixed lens, $A(u+v)=Au$ whenever $v$ lies in its nullspace. The 3-D field rendered from the twelve amplitudes cannot reveal those invisible directions either. More pixels do not increase its latent rank.

The audit constructs two **unit** vectors about 1.988 apart, nearly opposite on the unit sphere, whose complete complex readout vectors agree to roughly $1.7\times10^{-16}$. A constructed common rotation that mixes one hidden and one visible direction makes their readings diverge. This is an engineered observability example using the known null direction, not an agent discovering the right query.

This changes the interesting question from “have we found the unique source?” to “what additional reader or dynamical consequence would make the alternatives distinguishable?” It is the same question behind remembering a person through a place, a time or a rhythm: another cue must expose information the previous cue failed to distinguish. That cognitive comparison motivates an experiment; it is not a neuronal mechanism established by these scripts.

## Which early resonance examples need repair

Three direct code/algebra controls show why the promised behavior must be checked independently of its captions:

- `harmonicmemory.py` calls the original coherent template an “alien” input, but the stored thought changes only twelve of its thousand components. Their measured overlap is **0.993974**, so the alleged alien is almost identical to the memory. Recall is a direct inner-product score; the demo does not reconstruct an episode.
- `multiversenavigator.py` applies componentwise phases, then measures each component's absolute value. $|u_i e^{i\theta_i}|=|u_i|$: the steering cannot change its target readout. The independent rotation control changes magnitudes by only $2.8\times10^{-17}$. A phase-sensitive interference/mixing stage is required before this navigation can work.
- `resonant_attention.py` mixes three arbitrary real signals with phases $0,120,240$ degrees. Those tags have real rank two and sum to zero. Adding the same arbitrary signal to all three leaves the mixture unchanged, so rotation cannot uniquely recover three general independent signals. More carrier dimensions, independent frequencies, additional observations or a stated restricted prior would be needed.

These are useful design constraints. Phase can matter when the reader converts relative phase into interference. High-dimensional lifting can supply a larger distinguishable feature space, while a mere relabeling or redundant linear embedding cannot create missing information. None of these algebra controls runs the original PyTorch training or GUI.

## A new control in MoonFormer: same reading now, different future

MoonFormer's current wave reader depends on the signed structure $m$ through $\rho=B(m^2)$. Therefore $m$ and $-m$ have exactly the same density, wave speed and **all current wave responses**. This is a concrete ambiguity in the real prototype, not an imagined architecture.

Its structural evolution contains $g m^2$. With $g>0$, this breaks the sign symmetry, so equal present responses need not remain equal after waiting. I tested a retained arc at seed 3001 and its deliberate sign reversal using the unchanged prototype source:

| Additional unforced steps | Response difference RMS, $g=1.2$ | Response difference RMS, $g=0$ |
| --- | ---: | ---: |
| 0 | 0 | 0 |
| 1 | 0.000477447 | 0 |
| 100 | 0.011859276 | 0 |
| 500 | 0.015197958 | 0 |

The control starts from the same signed pair and removes only the symmetry-breaking coefficient. Its states remain sign reversals and its responses remain exactly identical at all four measured times. The positive case therefore has a specified causal mechanism for divergence.

This is one constructed pair, not two independently learned histories, a held-out retrieval benchmark or a claim that the signed material display looks identical. It shows why a present consequence fingerprint is weaker than a model of future consequences. Its sources are hash-checked by the reproducible audit script.

## The architecture suggested by the whole lineage

The useful generalization is **a memory as a query-to-consequence operator**. Instead of requiring one vector to decode into one picture, define a response family $\mathcal R_m(q,t)$: what a retained state does when asked question $q$ and observed at delay $t$.

| Role | Earlier phi construction | Current / proposed successor |
| --- | --- | --- |
| Hidden content | Fitted global vector $u$ | Retained structural field $m$, plus fast activity |
| Reader | Fixed supplied twelve-row lens $A$ | Material-dependent wave transport and receiver protocol |
| Observable | Twelve amplitudes and their rendered field | Measured response to a source, receiver and time window |
| Inverse handle | Gradient of fitting $u$ | Checked $\partial\mathcal R/\partial m$ and future-response differences |
| Next question | Supplied target, usually fixed | A query policy trained or selected to distinguish remaining alternatives |

For a fixed linear lens, the gradient is simply its fixed transport. In MoonFormer, changing the material changes the propagation operator and thus the consequences of several queries. This is the productive step beyond the old picture: an experience can change how later inputs travel, not only the image attached to a stored state.

Several Jacobian rows can be collected into an observability matrix. Its weak directions identify changes the current queries cannot distinguish. A candidate next query should separate plausible states or predicted futures at a matched cost and noise level, rather than merely light up a large derivative. Temporal samples matter too: the sign-pair control shows that waiting can reveal a distinction no instantaneous wave query can expose.

The next compelling demonstration would show two states with identical initial receiver displays, apply the same independently specified probes/evolution, then let a blind reader discover which underlying state was present. Ground truth remains outside the reader; null controls preserve equality; equal-budget fixed/random policies test whether query choice adds anything. A later cue → probe → revised cue loop could test associative recall. It is a proposal, not a feature already present in MoonFormer.

Any finite simulation state can be flattened into one vector. What makes the idea scientifically interesting is its dynamics, learned reader, observability and reusable predictions. Likewise, a modern AI's activation vectors do not by themselves imply a single universal state with physical laws. The architecture comparison is useful without that ontological conclusion.

## Reproduce these limited audits

NumPy is an optional dependency of the algebra audit, not of the atlas:

```sh
python scripts/audit_phi_master_vector.py --output data/audits/phi-master-vector.json
node scripts/audit_moonformer_sign_control.cjs /path/to/pinned/MoonFormer data/audits/moonformer-sign-control.json
```

Receipts: [master lens](../../data/audits/phi-master-vector.json), [MoonFormer sign control](../../data/audits/moonformer-sign-control.json). Source code: [master-vector optimizer](https://github.com/anttiluode/phi-world-theory/blob/4ce6f58c586993b5627cbeea6e6662780e1fadb9/findmastervector2.py), [memory](https://github.com/anttiluode/phi-world-theory/blob/4ce6f58c586993b5627cbeea6e6662780e1fadb9/harmonicmemory.py), [navigator](https://github.com/anttiluode/phi-world-theory/blob/4ce6f58c586993b5627cbeea6e6662780e1fadb9/multiversenavigator.py), [phase attention](https://github.com/anttiluode/phi-world-theory/blob/4ce6f58c586993b5627cbeea6e6662780e1fadb9/resonant_attention.py), [MoonFormer probe](https://github.com/anttiluode/MoonFormer/blob/ef26aeff37a70ad5142e2b26b0eda333a83708a2/src/probe.js), [structural evolution](https://github.com/anttiluode/MoonFormer/blob/ef26aeff37a70ad5142e2b26b0eda333a83708a2/src/field.js).
