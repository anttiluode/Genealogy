# November 3, 2026 — UlamInterlace: prime spirals reveal the observer

**Repository:** https://github.com/anttiluode/UlamInterlace  
**Live tool:** https://anttiluode.github.io/UlamInterlace/  
**Recording:** https://www.youtube.com/watch?v=pyTtm_awohQ  
**Analysis and reproducible checker:** [README](https://github.com/anttiluode/UlamInterlace/blob/main/README.md), [analysis/xor_zones.py](https://github.com/anttiluode/UlamInterlace/blob/main/analysis/xor_zones.py)  
**Genealogy status:** new curated tool / mathematical instrument; applications not yet demonstrated.

## What the program actually computes

One browser page draws up to six copies of a Ulam prime spiral with shared centre and cell sizes \(z_j=z_0r^j\). Interlace chooses one layer by pixel position (Rows, Columns, Checker, Square rings, Round rings). Overlay blends layers; Coincide multiplies their sampled values; XOR uses

$
X(v_0,\ldots,v_{L-1})=\frac{1-\prod_j(1-2v_j)}{2}.
$

For binary inputs this is the parity of occupied layers. For subpixel prime-density values it is a continuous polynomial, not literal binary XOR.

The original motive was multiscale prime geometry: Ulam rows, columns and diagonals expose quadratic-polynomial prime densities; rational zooms can align modular residues across layers. Those are legitimate arithmetic subjects, but classical quadratic-prime theory and local divisibility explain much of the apparent structure. The repository's README distinguishes exact identities, measured finite-window lifts, and unproved extrapolations.

## The novel-to-this-project, exact box genealogy

With base 1 px/cell, ratio exactly 101/100, and integer image coordinates, layer \(j\) reads

$
T_j(x)=\left\lfloor x(100/101)^j+\frac12\right\rfloor.
$

The same map operates on y. In the 101×101 central window with integer coordinates (x,yin[-50,50]), integer-arithmetic enumeration of the code's coordinate rule gives the following **universal** cancellation regions. Universal means white for *any* binary image, not just for the prime spiral.

| Number of layers | Pair-agreement x intervals | Guaranteed white rectangles | Forced-white pixels |
|---|---|---:|---:|
| 2 | [-50,50] | 1 | 10,201 |
| 4 | [-50,-26], [-17,17], [26,50] | 9 | 7,225 |
| 6 | [-50,-39], [-30,-26], [-17,-13], [-10,10], [13,17], [26,30], [39,50] | 49 | 4,225 |

For even layer counts, where each adjacent pair samples the same 2-D coordinate, `A xor A xor B xor B...` vanishes regardless of whether A and B agree. Cartesian products of the one-dimensional pair-agreement intervals give the visible tile grids. Odd layer counts instead leave one unpaired sampled layer visible in the corresponding zones. The **fully locked** core half-widths across 2,3,4,5,6 layers are 50, 25, 17, 12, 10 pixels respectively, but those alone do not explain the nine and 49 box patterns.

The 101×101 exact-arithmetic checker [analysis/xor_zones.py](https://github.com/anttiluode/UlamInterlace/blob/main/analysis/xor_zones.py) enumerates thresholds and tests universal cancellation independently. Run from the repo root: `python analysis/xor_zones.py`. It requires no dependencies.

## What the video does and does not establish

The approximately 08:20–22:00 segment shows moving prime carpets, barcodes, circular-versus-square ring geometry, XOR squares and Coincide starbursts. Near 17:00 the actual configuration is **four-layer XOR at ratio 1.010**, not six layers at ratio 2. The central white square and surrounding radial hatching are explainable as integer resampling/cancellation and would occur on randomized binary input; they are not evidence of new prime correlations.

At (z<1) px per cell, the page averages touched primes and weights the density by a logarithm. Multiplying those shades in Coincide is not a six-way Boolean primality event. Geometry between Euclidean ring masks and Chebyshev spiral shells explains keystone arcs without assuming diffraction or physical wave propagation.

The README also contains a **separate**, explicitly labelled six-layer ratio-2 numeric test (821×821 window) that reports five, 61 and 225 surviving pixels for centre numbers 1, 17 and 41. For centre 41, 223 survivors are on the main diagonal, and a 40-position contiguous Euler-prime segment is guaranteed under any additional coarser layers. This is independent of the near-identity video setting and does not prove a new number-theory theorem.

## Why this earns a Genealogy card

The conceptual shift is from **a pattern in the data** to **a pattern induced by the measurement operator**. Repeatedly sampling one binary field through nearby magnifications yields exact agreement zones and quantization boundaries; XOR reveals parity of disagreement rather than magnitude. That is potentially useful as a diagnostic for resampling, scale mismatch or image registration. In smooth images, subtracting two nearby magnifications approximates a radial scale derivative proportional to (xI_x+yI_y); unlike signed subtraction, multi-layer XOR can cancel even when different pairs disagree.

**Relationship to SweepAtlas and VHSImageStitch:** comparison targets, *not proven ancestry or shared code*. Those tools align observed frames. UlamInterlace suggests a possible standalone diagnostic to identify where small scale errors cause pixel disagreement. No registration-quality improvement, drift reduction or runtime advantage has yet been measured.

**Next falsification test:** same synthetic or VHS frames, known imposed scale/translation errors, and four matched views: conventional difference, scale-XOR, scale-variance, and conventional feature-registration diagnostics. Measure whether the new operator estimates the known error or flags failures more accurately at comparable computational cost; use random binary controls to separate geometry from prime arithmetic.

**Evidence boundary:** mathematically exact one-dimensional resampling partitions and code behavior versus source-reported finite-window prime analyses and prospective applications. The atlas must not convert attractive moiré pictures into claims of a novel physical caustic, fractal dimension, learned attention mechanism or a prime-number theorem.
