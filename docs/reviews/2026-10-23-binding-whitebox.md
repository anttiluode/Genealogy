# Field note — October 23, 2026: BindingClaude, BindingSol, WhiteBox and the SihtiStack return boundary

**Status:** source-curated history; not a new scientific experiment. Reviewed the published October 23 main-branch repositories and the October 19 SihtiStack/SihtiBrain sources. The atlas did not rerun their training or pretrained-model inference. Genealogy is the *curator* of these projects, not an additional experimental arm.

## Where the lines meet — and where they do not

The long SighImageSuper/Sihti branch concerns repeated transformations, residues, and what can survive repeated passage through a filter. SighImageSuper's original loop is explicitly \`x_next = alpha*x_original + (1-alpha)*EQ(x)\`, with optional per-generation renormalization: it **already has recurrence**, but not experience-discovered higher-order constraints.

The October 23 forks concern different barriers:

1. **BindingClaude** discovers high-order parity constraints among already identified pieces and uses them to complete masked toy states via asynchronous recurrence. An energy equation can be read and individual branches knocked out. Its slow rewriting did not reliably adapt.
2. **BindingSol** asks a different question: will a joint model learn a single discrete, usable *message* between independently structured sender and receiver inputs? It sometimes does, but misses its registered reliability threshold.
3. **WhiteBox** starts with a *trained* neural network. It treats the model's thresholded behavior over a binary cube as a function, and reconstructs its exact Walsh–Fourier coefficients. For these parity toys, one branch suffices. This is **behavioral distillation**, not identification of the network's internal causal mechanism.
4. **SihtiStack** (October 19) independently tested the possibility of restoring fact expression by returning a saved middle-layer activation difference. The reported real Qwen attempt failed even when the fact was expressible in the prompt. There is no warrant to equate information recoverability with an effective actuator.

These are neither four independent breakthroughs nor one unified running system. They are **separate controlled instruments** that narrow the engineering problem.

## Ledger of source-grounded findings

| Source | Working result | Limit preserved |
| --- | --- | --- |
| [SihtiStack preregistration](https://github.com/anttiluode/SihtiStack/blob/main/PREREG.md), [README](https://github.com/anttiluode/SihtiStack/blob/main/README.md) | Stored donor-minus-neutral vector at layer 14; five-arm harness and nine local/synthetic tests; original additive residual-stream identity correctly distinguishes a sum from its history. | Its README still marks the pretrained test unrun and does not contain user Qwen JSON. [SihtiBrain's later consolidation](https://github.com/anttiluode/SihtiBrain/blob/main/docs/RESEARCH_MAP_2026-10-19.md) explicitly records the user's pretrained run: fact in context **12/12**, none, correct-return and wrong-city return **2/12** each. The tested channel did not restore the fact. |
| [BindingClaude Part 3](https://github.com/anttiluode/BindingClaude/blob/main/results/PART3_LEDGER.md) | True binding consolidation 10/10 for both synthetic worlds; covered h3 expected one-shot 50%, asynchronous completion mean 99.10%; context ± about 99.59%; one selective branch cut lowers target context to 49.59% while preserving the other. | Settling benefits from update order and resolves in the first ordered sweep. Part 3 is not a Sihti natural-image test; lookup eventually catches up, direct MLP has a short 100-update budget, binder sees complete scenes while MLP sees visible labeled data. |
| [BindingClaude S4](https://github.com/anttiluode/BindingClaude/blob/main/results/PART3_LEDGER.md) | Unchanged context retained about 99.61% accuracy after reversal. | Context + recovers to ≥95% in **only 1/10** seeds; final average **56.01%**. No robust branch forgetting/relearning. |
| [BindingSol v0](https://github.com/anttiluode/BindingSol/blob/main/RESULTS.md) | Leakage/balance/gradient instrument G0 passes; two of five seeds learn completely usable one-bit messages (100% vs 50% erased/random and 0% sign-reversed/wrong-world). | G1/G2/G3 all **FAIL** at **2/5**, registered ≥4/5; mean 85% held-out for joint/fresh reader versus 90% direct equal-parameter MLP. Fresh reader learns from labels, no zero-shot cross-play. |
| [WhiteBox v0](https://github.com/anttiluode/WhiteBox/blob/main/results/results.json) | Exact clean Boolean-cube Fourier readout gives one parity branch with coefficient 1 on three trained tanh MLPs (n=11,12,19). On noisy fresh examples the surrogate agrees with the teacher 98.7%, 97.3%, 98.3%. | Query counts **32,800**, **37,600**, **56,800** versus cubes **2,048**, **4,096**, **524,288** respectively. Meaningful query saving shown only at n=19. A spurious T3 tiny coefficient was removed in a later threshold-fix commit; no real LLM or endogenous latent-feature result. |

**Evidence hygiene:** Raw complete Part 3 experiment JSON is not committed to BindingClaude main; the upstream ledger describes how to regenerate it, and this atlas is not an independent replication. WhiteBox has committed result JSON. BindingSol has committed per-seed result files and weights. Do not substitute the different provenance for one another.

## The mathematical bridge, carefully stated

For a binary-input *behavioral* oracle \(f:\{-1,+1\}^n\to\mathbb R\), the Walsh basis is exact:

\[
f(x)=\sum_{S\subseteq[n]}\theta_S\prod_{i\in S}x_i,\qquad
\theta_S=2^{-n}\sum_x f(x)\prod_{i\in S}x_i.
\]

A high-order coefficient identifies a higher-order dependence **in the chosen input basis and distribution**. The result does not directly tell us which hidden units compute it, how to edit a teacher's internal circuit, or how the oracle behaves away from Boolean vertices.

For a constructed conditional constraint machine, a separate output node \(y\) may participate in energy:

\[
E(x,y)=-y\sum_{S}\theta_S\prod_{i\in S}x_i,
\]

and suitable clamped coordinate updates can turn the extracted relation into a recurrent prediction. **This conversion has not been tested by WhiteBox v0**. A stable energy minimum is not automatically a correct or calibrated completion. With multiple unknown inputs, product branches can have zero local field; uncertainty and alternative minima must be represented.

### Why the three clocks remain an open engineering hypothesis

- **Fast:** clamp observed information and iteratively settle with frozen weights; compare update orders and retain unresolved ambiguity.
- **Medium:** adjust relation strengths from later, external observations; the data moments are not generally the same as an energy model's log-linear couplings when constraints interact.
- **Slow:** keep, prune and grow structure based on out-of-loop predictive improvement, not the attractor's own opinion. Control forgetting against an unchanged context.

This is a way to construct an *auditable computational material*, not a new theorem about hypergraphs, Walsh functions or biological dendrites.

## Follow-up without opening ten more projects

- Within **BindingSol**, the first unchecked experiment remains diagnosing why three senders misencode two source triples (v1); a design-only visual-circuit PR is separate.
- Within **BindingClaude**, reversal and fair-order tests plus reliable revision remain the critical mechanism work.
- Within **WhiteBox**, teacher-distribution fidelity and edit/ablation fidelity on a more complex task precede a pretrained language-model query experiment.
- **Next Sihti** would integrate learned relation discovery or behavioral extraction with the **old explicit EQ recurrence**, rather than quietly rewriting Fourier filtering as a Hopfield energy. It should expose unresolved hypotheses and compare with interpolation, lookup and fixed relation controls on genuinely new images.

The key question is no longer whether hyperedges or iterative filters are mathematically possible. It is whether *learned, inspectable changes to computation* provide a measurable advantage over ordinary controls, persist under environmental change, and remain causally interpretable.
