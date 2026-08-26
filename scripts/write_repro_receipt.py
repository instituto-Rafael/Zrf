#!/usr/bin/env python3
"""Emit a HEAD-bound receipt for the ZRF mathematics core verification."""
from __future__ import annotations

import hashlib
import json
import os
import platform
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from mathematics import get_all_operations

OUT = ROOT / "artifacts" / "reproducibility" / "zrf-mathematics-core-receipt.json"
INPUTS = (
    ".github/workflows/reproducible-mathematics-core.yml",
    "scripts/verify_mathematics.py",
    "scripts/write_repro_receipt.py",
    "src/mathematics.py",
)


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def env(name: str) -> str:
    value = os.environ.get(name, "").strip()
    return value or "TOKEN_VAZIO"


def main() -> int:
    ops = get_all_operations()
    registry = [{"id": i, "name": ops[i][0]} for i in sorted(ops)]
    registry_bytes = json.dumps(registry, sort_keys=True, separators=(",", ":")).encode()
    inputs = {rel: {"sha256": sha256(ROOT / rel), "bytes": (ROOT / rel).stat().st_size} for rel in INPUTS}

    payload = {
        "schema": "rafaelia.zrf-mathematics-repro-receipt/v1",
        "repository": env("GITHUB_REPOSITORY"),
        "head_sha": env("GITHUB_SHA"),
        "ref": env("GITHUB_REF"),
        "run_id": env("GITHUB_RUN_ID"),
        "run_attempt": env("GITHUB_RUN_ATTEMPT"),
        "execution_scope": "69-slot operation registry completeness plus the numerical sample assertions in scripts/verify_mathematics.py",
        "container": env("REPRO_CONTAINER_IMAGE"),
        "actions": {
            "checkout_commit": env("REPRO_CHECKOUT_SHA"),
            "upload_artifact_commit": env("REPRO_UPLOAD_ARTIFACT_SHA"),
        },
        "runtime": {
            "python": platform.python_version(),
            "implementation": platform.python_implementation(),
            "machine": platform.machine(),
        },
        "gate_outcomes": {
            "py_compile": env("GATE_COMPILE"),
            "registry_69_slots": env("GATE_REGISTRY"),
            "sample_numeric_verifier": env("GATE_VERIFY"),
        },
        "operation_registry_count": len(registry),
        "operation_registry_sha256": hashlib.sha256(registry_bytes).hexdigest(),
        "operation_registry": registry,
        "inputs": inputs,
        "all_69_operations_numerically_proven": False,
        "sample_numeric_verification_passed": env("GATE_VERIFY") == "success",
        "claim_allowed": False,
        "boundary": "Registry completeness proves 69 named operation slots exist. The bundled verifier samples selected derivatives, antiderivatives and inverses; it does not exhaustively prove all 69 formulas over their domains.",
    }
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    payload["canonical_payload_sha256"] = hashlib.sha256(canonical).hexdigest()
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(payload, indent=2, sort_keys=True, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"receipt={OUT}")
    print(f"payload_sha256={payload['canonical_payload_sha256']}")
    print(f"operation_registry_count={len(registry)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
