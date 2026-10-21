# Jäännös — GPT-2 residue routing: real-model G4 KILL (21 October 2026)

**Repository:** [anttiluode/Jaannos](https://github.com/anttiluode/Jaannos)  
**Original received receipt:** [archived complete GPT-2 JSON](https://github.com/anttiluode/Genealogy/blob/main/data/audits/jaannos-gpt2-2026-10-21.json)  
**Protocol:** [Jaannos preregistration](https://github.com/anttiluode/Jaannos/blob/main/docs/PREREG.md)  
**Reproduction code:** [gpt2_gate.py](https://github.com/anttiluode/Jaannos/blob/main/gpt2_gate.py)

## What was tested

An activation-aware decomposition `W = W_out + A_0 B_0 + Σ A_j B_j` for all 24 GPT-2 small MLP matrices: always-on sparse outliers and rank-256 core, eight extra rank-64 bands, four sketch rows per residual band. The local rule selects the number of bands per matrix/token from the sketched *output norm* of omitted bands. The runs use 32,768 WikiText-2 calibration tokens and 16 evaluation sequences of 512 tokens (=8,192 token positions), at budgets 0.6, 0.7, 0.8 and 0.9 of dense **routed-MLP theoretical multiply-add cost**. The receipt reports CUDA execution and maximum relative reconstruction error **3.18008×10⁻¹³**.

## Frozen G4 result — KILL

Percentage agreement with unmodified GPT-2 top-1 predictions at matched theoretical routed-MLP budgets:

| Router | 0.60 | 0.70 | 0.80 | 0.90 |
|---|---:|---:|---:|---:|
| **Fixed rank** | **53.66** | **62.53** | **70.10** | **76.62** |
| Local sketch | 40.54 | 48.40 | 57.41 | 68.00 |
| Local exact norm (free-test oracle) | 41.42 | 50.36 | 60.19 | 71.51 |
| Local ranks randomly permuted | 37.50 | 43.43 | 50.96 | 61.41 |
| Global output-margin reference | 51.74 | 60.41 | 67.17 | 73.82 |

- Relative to fixed rank, local sketch loses by **13.12, 14.13, 12.68 and 8.61 percentage points**.
- The exact *norm* oracle is not an oracle for the best possible decision-aware allocation; it knows tail magnitude but keeps the same norm-threshold policy.
- Local sketch beats randomized per-token rank allocations by **3.04, 4.96, 6.46 and 6.60 points**. A useful local signal exists, but it is not sufficient to beat fixed allocation.
- `global_margin` is an optimistic analysis reference: it substitutes precomputed dense-model logits on selected positions and charges an approximate selective-rerun cost. It should not be claimed as an implementable speedup, nor as a universal winner; fixed beats it here.

## Quality and cost boundaries

Dense GPT-2 perplexity on the receipt's WikiText test portion: **41.9705**. At nearby actual (not interpolated) settings, fixed k=5 costs **0.9376** and has perplexity **46.27**; local sketch at epsilon=0.14678 costs **0.92145** and has perplexity **49.19**. These are different operating points, so avoid calling them exact cost-matched perplexity comparisons.

The core alone costs **0.41677**, the sketch **0.02604**, and all eight bands on cost **1.25010** of the dense routed MLP operations. With an epsilon yielding over 99% dense top-1 agreement, the local router costs around **1.272** or more. The repo computes full factors and masks bands; outlier application uses a dense tensor. These are operation-count estimates for an unimplemented selective-kernel execution, **not throughput or energy measurements**. Moreover, the local policy computes a core `forward` to obtain its reference norm and calls `forward` again after selecting bands; the reported theoretical token cost counts core work once, implicitly assuming a reuse optimization that the current PyTorch path does not provide. This favors the local router on paper, making the observed loss no less credible.

The long tokenizer warning (443,951 tokens vs GPT-2's 1,024-token context) concerns corpus tokenization before chunking; the model was fed length-512 sequences. The run did complete and saved the receipt.

## What the result licenses

A banded weight representation can reconstruct exactly and a small random sketch can approximate a residual output *norm* cheaply on paper. This supplies a test instrument. It does **not** supply the orientation or downstream sensitivity needed to estimate whether omitted bands will change a future prediction or true next-token loss. The core mathematical mismatch is between `||r||` and downstream consequence, which in a local linear approximation depends on a direction-sensitive `gᵀr`. Computing a good, cheap `g` proxy is an **open problem**, not something this result demonstrates.

The real G4 is **KILL** under the preregistered rule. Retain the win over randomized allocation, the failing fixed-rank comparison, the earlier ceiling-effect toy receipt, and the real-model receipt. Do not retune to recast this as PASS. A later *offline diagnostic*, if chosen, would measure actual next-token-loss consequences of adding omitted bands at a subset of tokens, and clearly label it post-result exploration.

**Provenance:** The full JSON in this atlas was uploaded by the user from their actual run and was reviewed against Jaannos code and preregistration. The Genealogy update did **not** rerun or independently replicate the GPT-2 GPU workload. Correlated token positions are not 8,192 independent experimental replicates.
