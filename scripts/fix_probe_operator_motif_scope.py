import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

motif = {
    "id": "probe-defined-operator-coordinate",
    "title": "A computation coordinate is a response equivalence class, modulo the allowed gauge",
    "description": "Across measured transfer functions, active read/write probes, resident-state pings, source-filter trajectories and Jacobian tomography, the recurring object is not merely where an activation vector sits. A known perturbation asks what transformation is available here; several probes estimate a local response operator. States may be grouped when their relevant transfer behavior agrees, but only after declaring the gauge group: representation changes the observer is allowed not to know must not create a new computational label.",
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

motifs_path = ROOT / "data" / "motifs.json"
motifs = json.loads(motifs_path.read_text(encoding="utf-8"))
for i, current in enumerate(motifs):
    if current.get("id") == motif["id"]:
        motifs[i] = motif
        break
else:
    motifs.append(motif)
motifs_path.write_text(json.dumps(motifs, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

pass_path = ROOT / "data" / "passes" / "probe-operator-tomography.json"
probe_pass = json.loads(pass_path.read_text(encoding="utf-8"))
probe_pass["motifs"] = []
pass_path.write_text(json.dumps(probe_pass, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
