from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
PASS_PATH = DATA / "passes" / "probe-operator-tomography.json"


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload) -> None:
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def upsert_by_id(items: list[dict], item: dict) -> None:
    for index, current in enumerate(items):
        if current.get("id") == item["id"]:
            items[index] = item
            return
    items.append(item)


def upsert_repo(items: list[dict], item: dict) -> None:
    for index, current in enumerate(items):
        if current.get("name") == item["name"]:
            items[index] = item
            return
    items.append(item)


probe_pass = {
    "id": "probe-operator-tomography",
    "title": "Probe-defined operator coordinates: from hidden state to gauge-aware tomography",
    "summary": (
        "This pass joins an older system-identification thread to three September 23 experiments. "
        "HeadAsResonator supplied a measured known-input/observed-output transfer-function precedent; "
        "ReadWrite later made state-dependent response to a known intervention an explicit observability tool. "
        "SilentPing asks whether a fixed neutral probe can expose resident information that is weak or invisible at rest. "
        "PingToWord uses classical source-filter speech as a known-answer calibration showing that identity can live in an ordered "
        "operator trajectory rather than in the source. ResidentOperatorTomography then adds the missing identifiability constraint: "
        "a computation coordinate is meaningful only relative to a declared gauge group, so a valid grammar must ignore internal "
        "reparameterizations that preserve the computation while remaining sensitive to genuinely different factorizations."
    ),
    "order": 290,
    "reviewed_at": "2026-09-23",
    "nodes": [
        {
            "id": "SilentPing",
            "url": "https://github.com/anttiluode/SilentPing",
            "family": "operator-response",
            "status": "ledger",
            "claim": (
                "Tests whether a fixed neutral probe can read resident state that is poorly decodable from spontaneous output, "
                "using a short-term facilitation/depression calibration substrate and a cable neuron with a silent resident gain tag."
            ),
            "survived": (
                "The frozen 600-trial, four-item runs show the intended probe/read mechanism in both constructed substrates. "
                "STF rises from rest 0.265 to ping 0.805 and returns to 0.270 after state reset; the cable rises from rest 0.250 "
                "to ping 0.835 and returns to 0.260 after reset. The stronger transplant control moves only the resident state and "
                "makes the ping report the donor label at 0.733 (STF) and 0.840 (cable), separating state readout from the trial's visible history."
            ),
            "killed": (
                "This is a known-answer reproduction, not evidence that cortex uses either constructed substrate. Parameters were tuned, "
                "and 'silent' is observer- and drive-dependent: cable state leaks to a variance decoder around 0.35 and background activity "
                "acts as many weak incoherent pings; in STF the ping reads the combined facilitation/depression state rather than facilitation alone."
            ),
            "usefulness": "scientific",
            "confidence": "high",
            "evidence": "https://github.com/anttiluode/SilentPing/blob/main/README.md",
            "tags": [
                "active-probing",
                "resident-state",
                "activity-silent",
                "state-transplant",
                "impulse-response",
                "observability",
                "claim-boundary",
            ],
            "era": "Probe-defined hidden state",
            "era_order": 35,
        },
        {
            "id": "PingToWord",
            "url": "https://github.com/anttiluode/PingToWord",
            "family": "operator-response",
            "status": "ledger",
            "claim": (
                "Uses a time-varying source-filter speech model as a known-answer calibration for the idea that an ordered transfer/operator "
                "trajectory can carry identity while the driving source changes, then asks what endpoint-only versus residual-logged observation can identify."
            ),
            "survived": (
                "Across four vowel-glide words, the recovered filter trajectory decodes the word at 1.00 when trained on pinged speech and "
                "tested on held-out pings, whisper noise, or doubled pitch; source pitch alone stays near chance. Destroying frame order drops the "
                "we-versus-you reverse-trajectory contrast to 0.50. LPC recovers formants within roughly 4-26 Hz and every source ping with F1 1.00. "
                "When per-stage residuals are logged, telescoping reconstructs each intermediate to about 2e-16 and exposes known resonator/tanh stages hidden from output-only analysis."
            ),
            "killed": (
                "The source-filter, LPC and inverse-filter pieces are classical calibration rather than a novel speech result. Output-only source/filter "
                "separation retains a gain gauge: residual energy still decodes the word at about 0.92-0.97. Stage identification also relies on known "
                "candidate model classes, and telescoping reconstruction is an identity rather than evidence that arbitrary hidden operators are uniquely recoverable."
            ),
            "usefulness": "scientific",
            "confidence": "high",
            "evidence": "https://github.com/anttiluode/PingToWord/blob/main/README.md",
            "tags": [
                "source-filter",
                "operator-trajectory",
                "temporal-order",
                "residuals",
                "system-identification",
                "gauge-ambiguity",
                "known-answer",
            ],
            "era": "Operator trajectory as coordinate",
            "era_order": 36,
        },
        {
            "id": "ResidentOperatorTomography",
            "url": "https://github.com/anttiluode/ResidentOperatorTomography",
            "family": "operator-response",
            "status": "ledger",
            "claim": (
                "Combines logged residual trajectories with local Jacobian probes and asks for a computation grammar that is invariant under "
                "internal reparameterizations which preserve the computation, yet sensitive to genuinely different factorizations."
            ),
            "survived": (
                "The gauge test separates representation from computation in the d=8 toy. Raw Jacobians, stage eigenvalues and singular values fail "
                "under gauges larger than their allowed symmetry, while the general-gauge invariant descriptor (rank plus a Jacobian-pair nonlinearity index) "
                "stays within about 1e-8 to 4e-8 across random invertible reparameterizations. A distilled same-endpoint chain with a genuinely different nonlinear "
                "factorization has invariant grammar distance 1.50 while a gauged copy of the original is only 3.7e-8 away. Held-out probe directions are predicted, "
                "and a residual/shared-state architecture shrinks the gauge so per-stage eigenvalues become invariant again."
            ),
            "killed": (
                "This is still a toy d=8 known-stage-boundary experiment with stage families known to the experimenter. The fully general gauge leaves a deliberately "
                "coarse grammar, the nonlinearity coordinate depends on the traffic distribution and amplitude, rank-deficient pencil assumptions need care, and full-rank "
                "probing would be expensive at transformer residual-stream scale. It does not yet show that a learned network yields a stable human-readable algorithm."
            ),
            "usefulness": "scientific",
            "confidence": "high",
            "evidence": "https://github.com/anttiluode/ResidentOperatorTomography/blob/main/README.md",
            "tags": [
                "jacobian",
                "jvp",
                "operator-tomography",
                "computation-coordinate",
                "gauge-invariance",
                "residual-stream",
                "factorization",
                "held-out-probes",
            ],
            "era": "Gauge-aware operator tomography",
            "era_order": 37,
        },
    ],
    "edges": [
        {
            "source": "HeadAsResonator",
            "target": "PingToWord",
            "type": "converges",
            "confidence": "high",
            "why": (
                "HeadAsResonator is an older concrete system-identification case: known speech and observed electrode voltage identify a transfer function that can be inverted. "
                "PingToWord uses a deliberately known source-filter system to ask the same input/operator/output question with a moving transfer trajectory and explicit source swaps."
            ),
            "evidence": "https://github.com/anttiluode/PingToWord/blob/main/README.md",
        },
        {
            "source": "ReadWrite",
            "target": "SilentPing",
            "type": "converges",
            "confidence": "high",
            "why": (
                "ReadWrite established the synthetic observability principle that a known state-dependent intervention can separate states a passive read cannot. "
                "SilentPing isolates the same question as a fixed neutral impulse and adds reset, variance and resident-state transplant controls."
            ),
            "evidence": "https://github.com/anttiluode/SilentPing/blob/main/README.md",
        },
        {
            "source": "OperatorTime",
            "target": "SilentPing",
            "type": "converges",
            "confidence": "high",
            "why": (
                "OperatorTime makes resident history part of the effective operator available now. SilentPing measures that idea operationally: the same probe is transformed differently because a different resident state is present."
            ),
            "evidence": "https://github.com/anttiluode/SilentPing/blob/main/README.md",
        },
        {
            "source": "SilentPing",
            "target": "ResidentOperatorTomography",
            "type": "converges",
            "confidence": "medium",
            "why": (
                "SilentPing shows that a matched response can reveal resident state but only under a chosen observer/probe. ResidentOperatorTomography generalizes the readout from one probe response to a local operator sampled by multiple held-out perturbation directions."
            ),
            "evidence": "https://github.com/anttiluode/ResidentOperatorTomography/blob/main/README.md",
        },
        {
            "source": "PingToWord",
            "target": "ResidentOperatorTomography",
            "type": "converges",
            "confidence": "high",
            "why": (
                "PingToWord exposes both sides of the tomography problem: ordered operator trajectories can survive source swaps, while endpoint-only chains have factorization/gain ambiguity and residual logs reveal intermediate actions. "
                "ResidentOperatorTomography adds the missing invariance rule for deciding which differences count as computation rather than basis choice."
            ),
            "evidence": "https://github.com/anttiluode/ResidentOperatorTomography/blob/main/README.md",
        },
        {
            "source": "EATON",
            "target": "ResidentOperatorTomography",
            "type": "converges",
            "confidence": "high",
            "why": (
                "EATON reframed computation as transient state-conditioned operators and then began clustering local response behavior rather than raw activation. "
                "ResidentOperatorTomography attacks the identifiability problem that follows: a computation coordinate must ignore representation gauges that leave the computation unchanged."
            ),
            "evidence": "https://github.com/anttiluode/ResidentOperatorTomography/blob/main/README.md",
        },
    ],
    "motifs": [
        {
            "id": "probe-defined-operator-coordinate",
            "title": "A computation coordinate is a response equivalence class, modulo the allowed gauge",
            "description": (
                "Across measured transfer functions, active read/write probes, resident-state pings, source-filter trajectories and Jacobian tomography, the recurring object is not merely where an activation vector sits. "
                "A known perturbation asks what transformation is available here; several probes estimate a local response operator. States may be grouped when their relevant transfer behavior agrees, but only after declaring the gauge group: representation changes the observer is allowed not to know must not create a new computational label."
            ),
            "nodes": [
                "HeadAsResonator",
                "ReadWrite",
                "OperatorTime",
                "EATON",
                "SilentPing",
                "PingToWord",
                "ResidentOperatorTomography",
            ],
        }
    ],
}

write_json(PASS_PATH, probe_pass)

# Register the pass.
index_path = DATA / "passes" / "index.json"
pass_index = read_json(index_path)
entry = {"path": "probe-operator-tomography.json", "enabled": True}
if not any(item.get("path") == entry["path"] for item in pass_index):
    pass_index.append(entry)
write_json(index_path, pass_index)

# Evidence ledger: narrow claims only.
evidence_path = DATA / "evidence.json"
evidence = read_json(evidence_path)

silent_evidence = {
    "id": "silent-ping-v0",
    "node": "SilentPing",
    "claim": "In the two constructed substrates, a fixed neutral ping reads resident item state that is weak or absent in the matched resting linear readout, and transplanting only that state transfers the decoded item.",
    "design": "Four-item known-answer assay on two substrates (short-term facilitation/depression and a cable with a slow resident gain tag). Compare late-delay/rest readout, second-order variance attacker, neutral ping, state reset before ping, and cross-label resident-state transplant using the same ping-trained decoder.",
    "result": "supports",
    "motifs": ["probe-defined-operator-coordinate"],
    "sample": {"unit": "trial per substrate", "count": 600},
    "metrics": [
        {"name": "STF rest accuracy", "value": 0.265},
        {"name": "STF ping accuracy", "value": 0.805},
        {"name": "STF reset then ping accuracy", "value": 0.270},
        {"name": "STF transplant donor-label accuracy", "value": 0.733},
        {"name": "cable rest accuracy", "value": 0.250},
        {"name": "cable ping accuracy", "value": 0.835},
        {"name": "cable reset then ping accuracy", "value": 0.260},
        {"name": "cable transplant donor-label accuracy", "value": 0.840},
        {"name": "cable rest variance-attacker accuracy", "value": 0.348},
    ],
    "controls": [
        "Reset the resident state immediately before the otherwise identical neutral ping",
        "Transplant only the resident state from a different-label donor trial and score the donor label rather than the visible trial history",
        "Rest and late-delay linear decoding test whether the item is already published without a coherent probe",
        "Binned-variance rest/delay attacker tests whether 'silent' is only a failure of the linear decoder",
        "Background-drive sweeps test whether ordinary traffic becomes a stream of weak incoherent probes",
    ],
    "replication": "600 trials per substrate with four balanced items; committed frozen results",
    "held_out": True,
    "external_data": False,
    "limitations": [
        "Known-answer reproduction: both substrates were built so resident state changes how a later input is transformed, and parameters were tuned before the frozen run",
        "The cable is not fully silent to a second-order observer: the variance attacker reaches about 0.35",
        "Background traffic leaks the same state progressively, so ping advantage depends on a low-drive regime",
        "The STF ping reads the combined facilitation/depression state rather than facilitation alone",
        "This is a synthetic mechanism/control demonstration, not evidence that human working memory uses either implementation",
    ],
    "source": "https://github.com/anttiluode/SilentPing/blob/main/README.md",
}
upsert_by_id(evidence, silent_evidence)

word_evidence = {
    "id": "ping-to-word-v0",
    "node": "PingToWord",
    "claim": "In the known source-filter calibration, ordered transfer-function trajectory carries word identity across large source changes, while endpoint-only chain observation leaves factorization/gain ambiguities that intermediate residual logs remove for the tested known stage families.",
    "design": "Generate four vowel-glide words from identical source families through a moving F1-F4 resonator cascade, recover source/filter with frame-wise LPC, train a trajectory decoder on pinged speech and test source swaps, destroy temporal order, then compare output-only versus residual-logged identification of a resonator/tanh chain.",
    "result": "supports",
    "motifs": ["probe-defined-operator-coordinate"],
    "sample": {"unit": "word trajectory", "count": 4},
    "metrics": [
        {"name": "filter-trajectory word accuracy, held-out ping source", "value": 1.0},
        {"name": "filter-trajectory word accuracy, whisper source", "value": 1.0},
        {"name": "filter-trajectory word accuracy, high-pitch source", "value": 1.0},
        {"name": "bag-of-frames we-vs-you accuracy", "value": 0.5},
        {"name": "ping recovery F1", "value": 1.0},
        {"name": "maximum residual-telescoping reconstruction error", "value": 2e-16},
        {"name": "same-endpoint linear-stage permutation relative output change", "display": "~6e-15"},
        {"name": "residual pitch+energy word accuracy", "display": "0.92-0.97"},
    ],
    "controls": [
        "Replace the ping source with whisper noise and with a much higher-pitch pulse train while keeping the operator trajectory",
        "Destroy frame order; the we/you reverse-trajectory pair then becomes chance while visiting the same state set",
        "Use source pitch alone as a negative word decoder",
        "Permute commuting linear stages and trade reciprocal gain between stages to expose endpoint gauge freedom",
        "Insert a tanh between resonators to hide an upstream 500 Hz stage from output-only LPC, then log per-stage residuals",
    ],
    "replication": "240 training utterances plus held-out source families for four synthetic vowel-glide words; deterministic chain-identification calibration",
    "held_out": True,
    "external_data": False,
    "limitations": [
        "Parts A-C reproduce classical source-filter speech, LPC and inverse filtering rather than establishing a new speech result",
        "The four words are deliberately easy; the informative control is trajectory order and source swap rather than ceiling accuracy",
        "Output-only source/filter separation retains a gain gauge: residual energy still carries substantial word information",
        "Residual logging guarantees intermediate reconstruction by telescoping; it does not uniquely identify arbitrary unknown operator families",
        "Stage identification succeeds within known candidate classes (two-pole resonator versus memoryless tanh)",
    ],
    "source": "https://github.com/anttiluode/PingToWord/blob/main/README.md",
}
upsert_by_id(evidence, word_evidence)

rot_evidence = {
    "id": "resident-operator-tomography-v0",
    "node": "ResidentOperatorTomography",
    "claim": "A local computation grammar is only meaningful relative to a declared gauge: in the tested chain, a gauge-invariant response descriptor ignores invertible internal reparameterizations while distinguishing a genuinely different nonlinear factorization with nearly the same endpoint behavior.",
    "design": "Log residuals to recover intermediate states, estimate local Jacobian actions from probes, compare naive/Jacobian-eigenvalue/singular-value/general-gauge descriptors, then jointly test held-out probe directions, held-out source families, same-endpoint different factorization, random interface gauges, amplitude-dependent nonlinearity, and residual/shared-state gauges.",
    "result": "supports",
    "motifs": ["probe-defined-operator-coordinate"],
    "sample": {"unit": "state point", "count": 40},
    "metrics": [
        {"name": "held-out tanh probe prediction error", "value": 5e-8},
        {"name": "general-gauge invariant grammar distance", "value": 3.5e-8},
        {"name": "orthogonal-gauge invariant grammar distance", "value": 1.2e-8},
        {"name": "same-endpoint A-vs-B held-out R2", "value": 0.9999},
        {"name": "invariant grammar distance A vs different factorization B", "value": 1.50},
        {"name": "invariant grammar distance A vs gauged A", "value": 3.7e-8},
        {"name": "residual/shared-gauge eigenvalue grammar distance", "value": 5.1e-8},
        {"name": "per-interface gauge eigenvalue grammar distance", "value": 3.79},
    ],
    "controls": [
        "Fit local Jacobian action on probe set P_A and predict an independent probe set P_B",
        "Repeat on RMS-matched Gaussian, uniform and sparse heavy-tailed source families",
        "Distill a different L-S-L-S-L factorization to the same endpoint behavior as L-L-S-L-L",
        "Apply random orthogonal and general invertible interface gauges while fixing the endpoint",
        "Sweep traffic amplitude through the tanh stage to test whether its local operator changes only when saturation is exercised",
        "Compare one shared residual-stream gauge with illegal per-interface gauges that destroy residual-form structure",
    ],
    "replication": "d=8 toy chains, 40 sampled state points and 10 random gauges in the invariance panel",
    "held_out": True,
    "external_data": False,
    "limitations": [
        "Toy d=8 chains with stage boundaries supplied and stage families known to the experimenter",
        "The fully general invariant grammar is deliberately coarse: full-rank linear rotations/scalings are pure gauge and collapse together",
        "The nonlinearity index is source- and amplitude-dependent, so grammars require matched traffic for comparison",
        "The rank-deficient generalized-eigenvalue construction assumes compatible null spaces/ranges in the tested projection case",
        "Full-rank probing scales poorly to a 4096-dimensional transformer residual stream; JVP subspaces would be required",
        "No learned network has yet shown a stable cross-seed computational grammar under this criterion",
    ],
    "source": "https://github.com/anttiluode/ResidentOperatorTomography/blob/main/README.md",
}
upsert_by_id(evidence, rot_evidence)
write_json(evidence_path, evidence)

relations_path = DATA / "evidence_motif_relations.json"
relations = read_json(relations_path)
for evidence_id in ("silent-ping-v0", "ping-to-word-v0", "resident-operator-tomography-v0"):
    relations[evidence_id] = {"probe-defined-operator-coordinate": "supports"}
write_json(relations_path, relations)

# Mark the three new repositories as reviewed in the inventory. The scheduled census refresh preserves review status.
repos_path = DATA / "repos.json"
repos = read_json(repos_path)
for repo in (
    {
        "name": "SilentPing",
        "url": "https://github.com/anttiluode/SilentPing",
        "default_branch": "main",
        "size": 220,
        "visibility": "public",
        "description": "Can a neutral ping read an item out of state that is invisible at rest? Claude 5.5 Opus. ",
        "created_at": "2026-09-23T11:22:57Z",
        "updated_at": "2026-09-23T11:23:20Z",
        "inventory_status": "reviewed",
    },
    {
        "name": "PingToWord",
        "url": "https://github.com/anttiluode/PingToWord",
        "default_branch": "main",
        "size": 0,
        "visibility": "public",
        "description": "A ping becomes a word; then take it apart again. Opus 5.5 repo",
        "created_at": "2026-09-23T11:55:43Z",
        "updated_at": "2026-09-23T11:56:14Z",
        "inventory_status": "reviewed",
    },
    {
        "name": "ResidentOperatorTomography",
        "url": "https://github.com/anttiluode/ResidentOperatorTomography",
        "default_branch": "main",
        "size": 0,
        "visibility": "public",
        "description": "Can we read how a chain computes, and not only what it outputs? Opus 5.5 repo",
        "created_at": "2026-09-23T12:27:01Z",
        "updated_at": "2026-09-23T12:28:22Z",
        "inventory_status": "reviewed",
    },
):
    upsert_repo(repos, repo)
repos.sort(key=lambda item: item.get("name", "").lower())
write_json(repos_path, repos)

# README narrative, inserted just before the documentary/evidence layer.
readme_path = ROOT / "README.md"
readme = readme_path.read_text(encoding="utf-8")
heading = "### Probe-defined operator coordinates — from neutral pings to gauge-aware tomography"
section = """### Probe-defined operator coordinates — from neutral pings to gauge-aware tomography

Three September 23 repositories now join an older system-identification thread. **HeadAsResonator** had already provided a concrete calibration case: known speech plus observed electrode voltage identifies an approximate physical transfer function, which can then be inverted without turning the artifact into neural speech decoding. **ReadWrite** later made the more general observability point that a known state-dependent intervention can expose a hidden distinction that passive reading misses.

**SilentPing** joins that probe side to the resident-state line. In two deliberately constructed substrates, the same neutral ping carries no item label of its own, yet the response becomes item-decodable because resident state changes the operator the ping crosses. Reset returns decoding to chance, and the strongest control is a cross-label state transplant: moving only the resident state makes the ping report the donor item. The claim remains narrow. The mechanisms are known-answer constructions, parameters were tuned, and “silent” depends on the observer and traffic: the cable leaks to a variance decoder and background drive becomes a cloud of weak incoherent pings.

**PingToWord** provides a known-answer transfer calibration with an older engineering language. Identical source families driven through a moving vocal-tract-style resonator trajectory produce four synthetic words; the recovered filter trajectory classifies the word perfectly even when the source is replaced by whisper noise or a much higher pitch. Destroying order collapses the reverse-trajectory `we`/`you` pair to chance. This is classical source-filter/LPC territory, not a novelty claim. Its useful bridge is identifiability: endpoint-only chains admit order/gain ambiguities and a nonlinearity can hide an upstream stage, while logged residuals recover the actual intermediate trajectory. A residual-energy word leak remains as an explicit gain-gauge boundary.

**ResidentOperatorTomography** asks the harder question exposed by that calibration: when are two different-looking internal trajectories actually different computations? Residual logging plus local Jacobian probes is not enough unless the observer declares the allowed **gauge**. Under arbitrary invertible per-interface reparameterization, raw Jacobians, stage eigenvalues and singular values can change even though the computation is unchanged; in the tested d=8 chain only a deliberately coarse rank/nonlinearity descriptor survives the full gauge while still separating a genuinely different same-endpoint nonlinear factorization. Residual/shared-state architecture then shrinks the admissible gauge, restoring richer invariants such as per-stage eigenvalues. The result is still a toy with supplied stage boundaries and known stage families, but it gives the wall a stricter definition: a computation coordinate is a response-equivalence class **modulo representation changes the observer is allowed not to know**.

Genealogically this is a convergence, not a new invented ancestry chain: `HeadAsResonator` contributes measured transfer identification; `ReadWrite` contributes intervention-conditioned observability; `OperatorTime` and `EATON` contribute resident/state-conditioned operator language; `SilentPing` supplies the fixed-probe/transplant assay; `PingToWord` supplies a temporal operator-trajectory calibration; and `ResidentOperatorTomography` supplies the gauge-invariance attacker. The next serious handoff is a learned system or real residual stream where nobody chose the operator classes or coefficients to make the answer easy.

"""
if heading not in readme:
    marker = "## Documentary confidence and empirical evidence"
    readme = readme.replace(marker, section + marker)
else:
    start = readme.index(heading)
    marker = "## Documentary confidence and empirical evidence"
    end = readme.index(marker, start)
    readme = readme[:start] + section + readme[end:]

old_audited = "Current audited examples include `GeometricNeuronV24`, `ReadWrite`, `LentoOrava`, `GrowingAnttisNeuron`, `Operaattori`, `ActiveVectorNN`, `NewMachine`, `WorldModel`, `PhaseStigmergy`, `FusionMachine`, `Sihti`, `SighImageFactorization`, `WhatToLookAt`, `AdaptiveObserverCache`, and `EATON`."
new_audited = "Current audited examples include `GeometricNeuronV24`, `ReadWrite`, `LentoOrava`, `GrowingAnttisNeuron`, `Operaattori`, `ActiveVectorNN`, `NewMachine`, `WorldModel`, `PhaseStigmergy`, `FusionMachine`, `Sihti`, `SighImageFactorization`, `WhatToLookAt`, `AdaptiveObserverCache`, `EATON`, `SilentPing`, `PingToWord`, and `ResidentOperatorTomography`."
readme = readme.replace(old_audited, new_audited)
readme_path.write_text(readme, encoding="utf-8")

# Site recent-update banner.
index_html_path = ROOT / "index.html"
index_html = index_html_path.read_text(encoding="utf-8")
old_banner = "RECENT UPDATE · EATON transient handoff · AOC first-ask distance · Operator Time · SimpleNeuron/NSSN2"
new_banner = "RECENT UPDATE · Resident Operator Tomography · SilentPing / PingToWord · EATON · Operator Time"
index_html = index_html.replace(old_banner, new_banner)
index_html_path.write_text(index_html, encoding="utf-8")

print("probe/operator tomography genealogy update applied")
