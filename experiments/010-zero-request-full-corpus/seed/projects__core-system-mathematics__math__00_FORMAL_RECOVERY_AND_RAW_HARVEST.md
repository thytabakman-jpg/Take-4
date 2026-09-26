# Formal Recovery and Raw Equation Harvest

Date: 2026-09-24
Status: integrated mathematical source layer

## 1. Historical formal recovery

The PD/ED formal recovery layer contains:
- FORMAL_INVENTORY.md
- FORMAL_RESULT_REGISTER.md
- FORMAL_AUDIT_REPORT.md
- FORMAL_CORE.md
- RAW_EQUATION_HARVEST.md

The raw harvest recorded:
575 displayed-math occurrences
488 normalized unique expressions

This is a bookkeeping/recovery count, not 488 independent mathematical results.

## 2. Recovery status model

Recovered mathematics is typed:
RECOVERED
PARTIAL
CURRENT-CANDIDATE
HISTORICAL
LITERATURE

Inter-formulation relations are explicitly tracked:
EQUIVALENT
SPECIALIZATION
GENERALIZATION
COMPLEMENTARY
REVISION
INCOMPATIBLE
DIFFERENT-TARGET
UNRESOLVED

No raw recovered expression becomes canonical merely by appearing in the harvest.

## 3. ED mathematical families

The formal inventory contains multiple semantic lineages:
- realization/projection;
- compatible classification;
- task/output-set;
- permitted-extension frame;
- expansion/target-invariance.

Current integration retains the abstract frame semantics:

F=<K,S,Phi>

LD_F(b) iff |Phi_b|=1
ED(F) iff forall b in K, |Phi_b|=1
EX(F) iff forall b in K, Phi_b != emptyset
UN(F) iff forall b in K, |Phi_b| <= 1

ED(F) iff EX(F) and UN(F).

But the richer realization/task/model-expansion formulations remain provenance-level
instantiations, not silently identical notation.

## 4. Characterization and sufficiency mathematics

The recovered corpus contains:
- regime-relative characterization;
- regime-relative necessity;
- regime-relative sufficiency;
- finite explicit target compilation;
- classical projective Beth collapse;
- finite-model separation from uniform FO explicit definability;
- LFP expressive extension;
- expressive versus compilational reduction.

These are not all theorems of ED itself. Their assumptions and semantic regimes are
separate.

## 5. Attribution / supplementation

Recovered distinction:
target-conservative application preserves the permitted target extension.

Comp(D,f) or V(D,f) remains unchanged under target-conservative application.

Supplementation:
D+κ can change the compatible target family and can turn a nondeterminate system into a
determinate one.

Therefore determinacy after supplementation is attributable to the augmented system, not
retroactively to the original system.

## 6. Counterexamples / negative results

Recovered counterexamples include:
- unique target without unique internal realization;
- target determinacy without presented dependency acyclicity;
- repaired no-self-loop cyclic witness;
- task-relative quantifier-order controls.

These are negative constraints on overstrong proposed necessary conditions.

## 7. PDAudit recovery

1.0:
static result/sensitivity audit over an already supplied admissible space.

1.1:
representation-aware result classes, fibers, coordinate-relative MinSens, openness,
and result-changing pairs.

Important repair:
rho must be explicit in the fixed frame.

Important distinction:
empty MinSens family != empty coordinate set as a member.

PDAudit remains fixed-frame unless outer-frame variation is represented explicitly.

## 8. Closure mathematics

Recovered:
licensed source closure;
certificate + preservation;
compatible-target preservation;
anti-retroactive attribution;
result-complete closure relative to a declared completeness basis;
false closure/nonidentifiability;
restricted minimum result-complete attack basis NP-completeness;
monotone-but-not-submodular recursive result yield.

These results now feed directly into:
K contract semantics
C judgment
Strengthen coverage
PD Difference
minimality/closure.

## 9. Recovery gaps

Five historical theorem families were marked recovery-blocked in the original recovery
pass because exact statements/proofs were not recovered.

Those are preserved as OPEN in the formal inventory. They have not been invented or
promoted.

The raw harvest remains subordinate to the audited register and formal core.

## 10. Relation to the current mathematics project

The recovery layer supplies foundational mathematics and constraints.

It does not settle:
- the final system-role basis;
- the final primitive operator basis;
- the exact dynamic PD protocol;
- the external novelty question.

Those require the current Core System Mathematics work.
