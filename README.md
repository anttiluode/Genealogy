# Genealogy

Evidence-backed archaeology of Antti Luode's research repositories.

The central premise is that hundreds of repositories are not hundreds of independent ideas. The project separates raw repository inventory from curated scientific interpretation, then records explicit inheritance, corrections, rediscoveries, convergences and extracted mechanisms.

## Live atlas

https://anttiluode.github.io/Genealogy/

The static atlas includes:

- the complete repository census,
- a curated genealogy graph,
- modular archaeology passes,
- scientific-era Timeline and Corrections views,
- survivor motifs and archaeology queue,
- family/status/pass/edge filters,
- one-hop lineage focus,
- dependency-free SVG wheel zoom, drag pan, `− / + / Fit` controls, and zoom readout.

## Current archaeology passes

### Foundation atlas

The first cross-family curated slice. It captures recurring mechanisms such as bounded observation, structural memory, operator compilation, active probing, persistent state, sparse publication, splat/world representation, and search/routing.

### GeometricNeuron ladder

Treats the numbered GeometricNeuron repositories as scientific eras instead of assuming version-number ancestry. Explicit corrections survive; unsupported numerical ladders do not become edges.

### Splat / WorldModel

Tracks layered Gabor tools, phase transport, persistent fields, sparse predictive belief, observer-resource attacks, shared operator worlds and active inverse sensing. This pass corrected the atlas's own earlier speculative `Splatworld2 → WorldModel` edge using WorldModel's explicit ancestry.

### Clockfield pruning

Separates four things that had become entangled in the Clockfield family:

1. executable toy field dynamics,
2. grand physical identifications,
3. later falsifiers/autopsies,
4. computational mechanisms that remain useful after the physics story is removed.

The pass adds nine reviewed repositories, including `BirthOfClockfield`, `SimpsonsUniverse`, `HorizonNet`, `OutoSynapsi`, and `ClockfieldUnified`. The strongest survivors are not the cosmological claims: they are the Beurling-lattice mathematical object isolated by the SimpsonsUniverse audit, HorizonNet's idleness/observer-horizon result, traffic-shaped body geometry in OutoSynapsi, and the narrow Physics Router extraction in ClockfieldUnified.

## Evidence rule

An edge means evidence was found for that relationship. Similar names and version numbers are only discovery hints.

Negative results remain in the tree. A failed interpretation often explains why a later mechanism exists, so deleting it would erase the actual genealogy.

## Data layout

```text
data/repos.json          complete census snapshot
data/nodes.json          foundation curated nodes
data/edges.json          foundation evidence edges
data/motifs.json         foundation recurring mechanisms
data/passes/index.json   enabled archaeology passes
data/passes/*.json       separable reviewed passes
```

Passes stay modular so later archaeology can correct one family without rewriting the whole atlas.

## Validation

```bash
python scripts/validate_data.py
python -m unittest discover -s tests -v
node --check assets/app.js
node --check assets/zoom.js
```

GitHub Actions runs the same checks on pull requests and `main` pushes. The repository census refresh remains separate from interpretation changes.

## Rule

**Names are hints, not evidence. Negative results stay in the family tree.**
