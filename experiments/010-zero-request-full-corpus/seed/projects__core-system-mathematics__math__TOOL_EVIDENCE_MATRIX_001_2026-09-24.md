# Tool Evidence Matrix 001

Date: 2026-09-24
Status: synthesized empirical evidence
Purpose: determine what each mathematical/research tool contributes, when it fails, and
what combination patterns are supported by actual runs.

## Evidence dimensions

For method H_i on target X:
R_i(X) = recovered result set.

Pairwise overlap:
O_ij(X)=R_i(X) intersection R_j(X).

Ordered interaction:
D_{i->j}(X)=H_j(H_i(X)) minus H_j(X).

Candidate reduction requires preserving:
findings
grounds
dependencies
unresolved variation
provenance
representation sensitivity
discriminating tests
epistemic license
action license
downstream control consequences.

## Recursive historical audit

Yield: HIGH discovery.

Strong:
- hidden dependencies;
- causal/epistemic transitions;
- competing interpretations;
- repair propagation;
- generators/root causes;
- state changes.

Weak:
- poor stopping mechanism in early versions;
- target/level drift;
- discovery and verification mixed;
- local closure overread as global completeness.

Best condition:
freeze target/level/corpus/basis and recurse only on material delta.

## Orthogonal five-lens audit

Yield: HIGH-CONDITIONAL.

Strong:
- representation challenge;
- information-loss;
- inverse-problem;
- selection effects;
- counterfactual history.

Weak:
- less productive once the representation has stabilized and the lenses converge.

Best condition:
frozen common input, isolated passes, synthesis only after independent results.

## PDAudit 1.0

Yield: MEDIUM/HIGH for fixed frames.

Strong:
compact localization of result-sensitive coordinates.

Weak:
cannot determine whether frame/target/bearer/representation itself is correct.

Best condition:
downstream verification after frame freeze.

## PDAudit 1.1

Yield: HIGH.

Strong:
- representation-sensitive MinSens;
- fibers/result partitions;
- unresolved variation;
- invariance across representations.

Best condition:
multiple admissible representations and explicit result equivalence.

## Artifact repair + rerun

Yield: VERY HIGH.

Strong:
repair -> rerun -> detect secondary consequences/regressions.

Best condition:
baseline frozen, delta explicit, protected observables declared.

## Multi-Object

Yield: HIGH-CONDITIONAL.

Strong:
- typed relations;
- higher-order relation residuals;
- arity;
- direction;
- hierarchy;
- representation;
- ordering effects.

The 24-permutation experiment showed:
discovery-order sensitivity can differ from normalized-result sensitivity.
Full factorial expansion became late-stage redundant.

Best condition:
typed objects + strategic order contrasts before factorial expansion.

## Factorization / Quotient

Yield: HIGH.

Strong:
- common structure;
- quotient/residual;
- reconstruction;
- accounting;
- reduction/minimality;
- incomparable alternatives.

Weak:
without AccountingRule + ReconstructionCheck it can falsely explain away structure.

Best condition:
late enough to expose common structure, but before duplicated implementations proliferate.

## Raise the Ceiling / RTC

Yield: HIGH after state/search repairs.

Strong:
- same-task strict gain;
- incomparable successor frontier;
- success/failure signatures;
- search coverage;
- basis-relative closure;
- anti-loop invalidation;
- PD as successor generator.

Weak before v2:
- scalar result;
- weak closure basis;
- success overclaim;
- generator lock-in;
- poor failure memory.

Best condition:
explicit result frontier + search state + protection + coverage + independent
maximality rule.

## TransferCore

Yield: HIGH as bridge/provenance validator.

Strong:
- source/target freeze;
- relation typing;
- provenance;
- bridge licensing;
- target-effect separation.

Weak:
cannot make a downstream benefit legitimate when the bridge is unlicensed.

Best condition:
after discovery and before transfer/promotion.

## ImprovementCore

Yield: HIGH as experiment selector/orchestrator.

Strong:
- selects unresolved coordinates;
- minimizes indiscriminate tool use;
- triggers re-entry after material changes;
- distinguishes exploration from proof/validation.

Weak:
does not itself supply the substantive mathematics.
It also becomes unreliable if its own version identity is unresolved.

Best condition:
typed current state + explicit uncertainty coordinates + return/re-entry rule.

## Giant all-tools sweeps

Yield: VARIABLE.

Strong:
comprehensive discovery when the target is still badly under-mapped.

Weak:
- timeouts/stalls;
- huge outputs before checkpoints;
- unclear incremental yield;
- repeated rediscovery;
- difficult attribution.

Repair:
bounded phases, durable checkpoints, delta-only re-entry, interaction-gated expansion.

## Goal/spine audits

Yield: HIGH when target is bounded.

Strong:
- load-bearing dependencies;
- hidden generators;
- conditional spine refinements.

Weak:
a valid spine does not establish whole project architecture.

## Naming/referent continuity

Yield: HIGH for its narrow defect class.

Strong:
detects stable labels with drifting referents.

Weak:
does not solve general routing/capture/closure.

## OrphanScan / ConsequenceClosure / regression

Yield: HIGH verification/propagation.

Strong:
- uncaptured outputs;
- downstream consequences;
- lossy compression;
- repair regressions.

Weak:
depends on knowing what object/event matters first.

## SORT_LATER / capture queues

Yield: HIGH as emergency persistence.

Weak:
flat lifecycle mixing, stale queues, manual capture dependence.

Useful mathematical lesson:
capture is a state-propagation problem, not merely storage.

## Tool-order findings

High-yield pattern:
DISCOVER
-> FREEZE
-> DIFFERENTIATE
-> RELATE/RECONSTRUCT
-> FACTOR
-> CHALLENGE
-> IMPROVEMENTCORE
-> STRENGTHEN
-> U
-> R
-> VALIDATE.

This is not universal. It is the currently best-supported pattern.

## Core methodological findings

1. A method can be highly valuable for discovery and poor for stopping.
2. A method can become redundant after another method closes the same normalized result.
3. Equal final results do not imply equivalent methods.
4. Tool interaction can be result-producing:
   H_j(H_i(X)) != H_j(X).
5. Ordered discovery and normalized-result invariance are different properties.
6. A tool's output volume is not its information yield.
7. A tool is most valuable when it attacks a live unresolved coordinate.
8. Re-entry must be triggered by material semantic delta, not merely by the passage of
   another run.
9. A named tool can survive operationally after ceasing to be a primitive mathematical
   operator.
10. Tool completeness is not achieved by running everything once; it is achieved when
    the remaining unresolved coordinate set is explicitly characterized and the chosen
    basis has survived discriminating holdouts.
