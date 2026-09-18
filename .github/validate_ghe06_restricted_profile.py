#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROFILE = ROOT / "config/ghe06-restricted-profile.json"
WORKFLOWS = ROOT / ".github/workflows"

def main():
    data = json.loads(PROFILE.read_text(encoding="utf-8"))
    assert data["schemaVersion"] == "iaap-guard-ghe06-restricted-profile/v1"
    assert data["supportClaim"] is False
    assert data["restrictedNetworkExecutionSupported"] is False
    assert data["retiredCompositeAction"] is True
    assert data["runtimeRepository"] == "InfrastructureProductWorks/iaap-guard-core"
    actual = sorted(p.name for p in WORKFLOWS.glob("*.yml"))
    assert actual == sorted(data["excludedWorkflows"]), (actual, data["excludedWorkflows"])
    assert not (ROOT / "action.yml").exists()
    assert not (ROOT / "action.yaml").exists()
    for field in (
        "packageRegistryDisposition",
        "containerRegistryDisposition",
        "githubActionsDisposition",
        "telemetryDisposition",
        "githubApiDisposition",
    ):
        assert isinstance(data[field], str) and data[field]
    print("Public Guard GHE-06 restricted boundary verified")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
