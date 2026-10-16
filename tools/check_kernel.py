#!/usr/bin/env python3
"""Validate Take-4's experimental kernel in ordinary and optimized Python."""
from pathlib import Path
import yaml

root = Path(__file__).resolve().parents[1]
k = yaml.safe_load((root / "KERNEL.yaml").read_text())

def require(condition, message):
    if not condition:
        raise SystemExit(f"Take-4 kernel fitness: FAIL ({message})")

require(isinstance(k, dict), "kernel must be a mapping")
require(k.get("experiment") == "take_4_informed_reconstruction", "experiment")
require(k.get("loop") == ["ORIENT", "NAVIGATE", "RESOLVE", "SELECT", "EXECUTE", "VERIFY", "UPDATE", "RESELECT"], "loop")
require(k.get("inheritance_rule") == "inherit_evidence_not_architecture", "inheritance_rule")
require(isinstance(k.get("external_corpora"), dict) and k["external_corpora"].get("reaserch") == "thytabakman-jpg/Reaserch", "external_corpora.reaserch")
require(k.get("promoted_runtime_external") == "IC-2026-09-23-018", "promoted_runtime_external")
require(isinstance(k.get("protected"), list), "protected")
for p in ["project_local_authority", "OPEN", "INCOMPARABLE", "semantic_runtime_authority_separation"]:
    require(p in k["protected"], f"protected.{p}")
print("Take-4 kernel fitness: PASS")
