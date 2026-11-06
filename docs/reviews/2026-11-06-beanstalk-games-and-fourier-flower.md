# November 5–6, 2026 — two Beanstalk games and a Fourier bloom

**[Live wall](https://anttiluode.github.io/Genealogy/#nov6-beanstalk-fourier)** · [Curated pass](../../data/passes/november-6-beanstalk-games-and-fourier-flower.json)

The previous [November 5 pass](../../data/passes/november-5-vines-chains-and-garden-worlds.json) already contains Emergence3DSol, Köynnös and PsychedelicGarden. This follow-up adds the two missing games and November 6 FourierFlower without double-counting those three.

## First Beanstalk: the support idea becomes a story

[Source](https://github.com/anttiluode/SolAndTheBeanStalk/blob/main/README.md). Five authored chapters in a third-person WebGL2 island world. A green climbing bean grows bridges; golden roots and a blue pulse help advance the story; shared pin loading leads to root-or-release endings. The README names Köynnös (distant pin/chain load), CrystalMoon, PsychedelicGarden and Same Seed as influences, while explicitly describing a distinct implementation.

This is a **mechanic extraction** from Köynnös, not a code fork or a scientific evolution result. Seed generation, progression and inventory have source-reported tests. Actual device-specific browser/GPU playtesting remains limited. The chain-load economy is synthetic.

## Beanstalk 2: a different renderer and a faster main verb

[Source](https://github.com/anttiluode/SolAndTheBeanstalk2/blob/main/README.md). Four compact rooms with instant vine shooting, rooting, following, recoverable chain snaps, audible tension cues, crystal chambers and two endings. The README states explicitly that the **WebGL2 raymarch shader derives directly from PsychedelicGarden**, not from the first game's triangle-mesh renderer.

The first-to-second Beanstalk arrow is a **gameplay correction**, not proof of code reuse: instead of waiting for bridges to grow, the player acts immediately. Six rule/syntax checks are reported locally. The full normal shader was not successfully playtested on a real GPU, and simplified CI graphics cannot establish normal-device performance. Neither game models material fracture physically.

## FourierFlower: a standalone mathematical-art branch

[Source](https://github.com/anttiluode/FourierFlower/blob/main/README.md) · [Live visualization](https://anttiluode.github.io/FourierFlower/). Each flower traces a sum of rotating Fourier terms, z(t) = Σ aₖ exp(i(nₖt + φₖ)), laid out on a logarithmic 3D spiral. Layers, petals, depth, camera motion, particle glow and screenshots are adjustable; the README describes an independent software renderer fallback.

This is programmed geometry, not emergent biology, learning, or an explanation of why π has a particular value. There is no verified direct ancestry edge to the vine-game code. Similar-looking flowers do not justify one.

## Typed lineage

| Relation | Type | Boundary |
| --- | --- | --- |
| Köynnös → SolAndTheBeanStalk | extracts | Pin-load motif transferred to narrative/game rules |
| PsychedelicGarden → SolAndTheBeanStalk | converges | Explicit aesthetic influence; distinct renderer |
| PsychedelicGarden → SolAndTheBeanstalk2 | inherits | Direct WebGL2 raymarch engine inheritance |
| SolAndTheBeanStalk → SolAndTheBeanstalk2 | corrects | Pacing and player-action redesign, not a documented code fork |
| FourierFlower | independent | No supported code-descent claim |

**Useful next test:** player comprehension of chain strain (with/without feedback), plus genuine GPU playtests for both games; compare FourierFlower mathematical and renderer output across browsers. These validate UX/rendering, not evolution.
