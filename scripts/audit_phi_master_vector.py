"""Independent Float64 algebra audit of phi-world-theory's fixed master lens.

Requires NumPy; does not run the upstream optimizer, GUI or PyTorch examples.
Run from the atlas root:
    python scripts/audit_phi_master_vector.py --output data/audits/phi-master-vector.json
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np

PHI_SOURCE = "4ce6f58c586993b5627cbeea6e6662780e1fadb9"


def lens() -> tuple[np.ndarray, np.ndarray]:
    phi = (1 + np.sqrt(5)) / 2
    directions = np.array([
        [0, 1, phi], [0, 1, -phi], [0, -1, phi], [0, -1, -phi],
        [1, phi, 0], [1, -phi, 0], [-1, phi, 0], [-1, -phi, 0],
        [phi, 0, 1], [phi, 0, -1], [-phi, 0, 1], [-phi, 0, -1],
    ])
    directions /= np.linalg.norm(directions, axis=1, keepdims=True)
    matrix = np.zeros((12, 1000), dtype=complex)
    matrix[:, :3] = directions
    d = np.arange(997)
    for i in range(12):
        matrix[i, 3:] = np.exp(-d / 100) * np.exp(1j * d * phi * (i + 1) / 12)
    matrix /= np.linalg.norm(matrix, axis=1, keepdims=True)
    return matrix, directions


def run() -> dict:
    matrix, directions = lens()
    gram = matrix @ matrix.conj().T
    eigenvalues, eigenvectors = np.linalg.eigh(gram)
    rank = int(np.linalg.matrix_rank(matrix))
    leading = matrix.conj().T @ eigenvectors[:, -1]
    leading /= np.linalg.norm(leading)
    coefficients = matrix @ leading
    raw_power = float(np.vdot(coefficients, coefficients).real)
    orthogonal_power = float(np.vdot(coefficients, np.linalg.solve(gram, coefficients)).real)
    assert np.isclose(raw_power, eigenvalues[-1], atol=1e-12)
    assert raw_power > 1.3 and np.isclose(orthogonal_power, 1, atol=1e-12)
    assert rank == 12

    # Two unit vectors with identical complex readouts, not just similar images.
    rng = np.random.default_rng(42)
    state = rng.standard_normal(1000) + 1j * rng.standard_normal(1000)
    state /= np.linalg.norm(state)
    visible = matrix.conj().T @ np.linalg.solve(gram, matrix @ state)
    hidden = state - visible
    hidden /= np.linalg.norm(hidden)
    hidden_length = np.sqrt(1 - np.vdot(visible, visible).real)
    plus = visible + hidden_length * hidden
    minus = visible - hidden_length * hidden
    response_error = float(np.linalg.norm(matrix @ plus - matrix @ minus))
    assert response_error < 1e-12
    assert np.isclose(np.linalg.norm(plus), 1) and np.isclose(np.linalg.norm(minus), 1)

    # An engineered unitary mixing of one visible and one hidden direction.
    # This is an existence example, not a blind discovery policy or learned law.
    visible_length = np.linalg.norm(visible)
    axis = visible / visible_length
    angle = 0.12
    rotated = []
    for sign in [1, -1]:
        x, y = visible_length, sign * hidden_length
        rotated.append((np.cos(angle) * x - np.sin(angle) * y) * axis
                       + (np.sin(angle) * x + np.cos(angle) * y) * hidden)
    after_difference = float(np.linalg.norm(matrix @ rotated[0] - matrix @ rotated[1]))
    assert after_difference > 0.1

    # harmonicmemory.py's "alien" is the same unmodified coherent template.
    phi = (1 + np.sqrt(5)) / 2
    template = np.exp(1j * np.linspace(0, 4 * np.pi, 1000)) / np.sqrt(1000)
    memory = template.copy()
    memory[:12] *= np.exp(1j * np.array([0, phi, -phi, 0, 1, -1, phi, 0, 0, 1, phi, -1]))
    alien_overlap = float(abs(np.vdot(template, memory)))
    assert alien_overlap > 0.99

    # multiversenavigator.py reads |U_i exp(i theta_i)|, invariant to its steering.
    navigator = np.zeros(1000, dtype=complex)
    navigator[:12] = 1
    navigator += 0.2 * np.exp(1j * np.linspace(0, 10 * np.pi, 1000))
    navigator /= np.linalg.norm(navigator)
    theta = rng.standard_normal(1000)
    phase_error = float(np.max(abs(abs(navigator[:12]) - abs((navigator * np.exp(1j * theta))[:12]))))
    assert phase_error < 1e-14

    # Three phase tags at 0, 120 and 240 degrees live in two real dimensions.
    tags = np.exp(1j * np.array([0, 2 * np.pi / 3, 4 * np.pi / 3]))
    tag_matrix = np.vstack([tags.real, tags.imag])
    assert np.linalg.matrix_rank(tag_matrix) == 2
    assert abs(sum(tags)) < 1e-14

    return {
        "protocol": "phi-master-vector-algebra-v1",
        "source_commit": PHI_SOURCE,
        "arithmetic": "independent NumPy Float64 reconstruction of the specified lens",
        "frame": {
            "ambient_complex_dimensions": 1000,
            "readout_complex_rank": rank,
            "complex_null_dimensions": 1000 - rank,
            "gram_eigenvalues": eigenvalues.tolist(),
            "largest_off_diagonal_overlap": float(np.max(abs(gram - np.eye(12)))),
            "normalized_state_raw_power_maximum": raw_power,
            "correct_orthogonal_projection_fraction_at_maximum": orthogonal_power,
            "expected_raw_power_for_isotropic_unit_state": float(np.trace(gram).real / 1000),
            "three_dimensional_direction_frame_error": float(np.linalg.norm(directions.T @ directions - 4 * np.eye(3))),
        },
        "indistinguishable_unit_states": {
            "state_distance": float(np.linalg.norm(plus - minus)),
            "initial_response_difference": response_error,
            "null_direction_response_norm": float(np.linalg.norm(matrix @ hidden)),
            "engineered_common_rotation_radians": angle,
            "response_difference_after_common_rotation": after_difference,
        },
        "example_controls": {
            "supposed_alien_memory_overlap": alien_overlap,
            "navigator_phase_rotation_magnitude_error": phase_error,
            "three_phase_tags_real_rank": 2,
            "three_phase_tags_common_signal_null_residual": float(abs(sum(tags))),
        },
        "limitations": [
            "Does not reproduce the unseeded PyTorch optimization or authenticate the reported 131.47% run.",
            "The upstream Float32 construction has rounding differences; this independently checks the stated formula in Float64.",
            "The paired-state rotation is constructed using a known null direction, not learned or selected without access to the states.",
            "Code/algebra controls do not benchmark learned recall, full field physics, GUI rendering or biological mechanisms.",
        ],
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    receipt = run()
    serialized = json.dumps(receipt, ensure_ascii=False, indent=2, allow_nan=False) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(serialized, encoding="utf-8")
    print(serialized, end="")
