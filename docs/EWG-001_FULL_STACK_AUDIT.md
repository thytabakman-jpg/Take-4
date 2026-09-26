# EWG-001 full-stack audit result

Branch: ic/endogenous-work-generator-v1
Status: EXPERIMENTAL / NO PRODUCTION AUTHORITY

## Mathematical classification

EWG-001 is a controller-subsystem semantics for endogenous work generation and residual closure.

It is not:
- the epistemic kernel;
- Improvement Core itself;
- a single audit/tool;
- mutation authority;
- a promotion authority.

Core object:

`EWG = <M,J,S,A,B,O,Psi,pi,Gamma,X,V,D,Q,K>`

It maps an explicit entry mode plus admitted state into a justified work frontier, selects licensed work while preserving incomparability, realizes executable behavior, verifies deltas, records discharge, and re-enters until fresh obligation generation is empty. Budget exhaustion yields PAUSED_OPEN, never closure.

## Full meaningful-angle review

Important status correction: the named tool families below were used as an adversarial review matrix. They were not each independently executed through their historical runtime implementation. Therefore their statuses are typed as specification/review results, not runtime execution evidence.

### Goal / control family
Goal Spine, Recovered Goal, Goal Completion:
SPECIFICATION PASS after adding explicit JOB_CONDITIONED and ZERO_REQUEST_DISCOVERY modes. Hidden goal injection is prohibited.

### Semantic / epistemic family
PD/PDAudit, A01, A03, A04, A06, A08, A09, A14, A16, RP-004, Semantic Preflight:
SPECIFICATION PASS after making TYPE_BEFORE_OPERATION and post-run semantic-delta admission mandatory.

### Structural / mathematical family
MT/MTA, FACTOR, DIFFERENTIATE, RELATE, RECONSTRUCT, Multi-Object, Tool Role Algebra:
STRUCTURAL REVIEW PASS. The original monolithic controller notion factors into admission, obligation generation, selection, realization, execution, verification, closure, and two entry modes.

### Architecture family
Architecture Analysis, placement, dependency, boundary analysis:
ARCHITECTURE REVIEW PASS. Least-foundational current placement is controller subsystem. PD supplies epistemic behaviors; MTA supplies factorization; Improvement Core supplies improvement policy; Tool Run Closure supplies per-operation terminal closure; HF-001 supplies recursive discovery/reconstruction behavior. EWG owns cross-operation frontier regeneration and earned run closure.

### Selection / priority family
Priority, Compare Everything, MinSens/MinDet, selector integrity:
SPECIFICATION FAIL -> REPAIRED. A selector pi and explicit selection basis were missing. The repair records selector grounds and preserves INCOMPARABLE when no licensed total order exists.

### Recursive / closure family
HF-001, Tool Run Closure, ConsequenceClosure, Raise the Roof, Raise the Ceiling/RTC:
REFERENCE-MODEL PASS after a later closure repair. Material deltas, failed verification, and new abstractions regenerate requirements. Fresh requirement satisfaction is required before STOP.

### Runtime / execution-truth family
Execution Envelope, binding, native execution, execution-truth:
PARTIAL EXECUTION PASS. The reference state machine was executed in-session after the closure repair and 10/10 adversarial checks passed. This is not repository CI and is not evidence that actual Take-4 tool/runtime bindings execute. Those bindings remain OPEN.

### Failure / pathology family
RCA, Diagnosis, recurrence, OrphanScan, Ghost, Conflict:
SPECIFICATION PASS. Explicit terminal states exist for BLOCKED, OPEN_REALIZATION, BASIS_GAP, CONFLICT, JOB_OPEN, PAUSED_OPEN. Search failure is not basis insufficiency. Unowned or unauthorized work cannot silently execute.

### Improvement family
Improvement Core, stronger-successor, repair, non-regression:
ARCHITECTURE REVIEW PASS with boundary correction. Improvement Core consumes work obligations and proposes stronger successors; it does not define the frontier, authorize itself, or close the run. Self-improvement creates candidates only.

### Transfer family
TransferCore, capability migration, Take Five:
TRANSFER REVIEW PASS. The transferable unit is the EWG behavior contract and protected semantics, not Take-4 files or placement. Take Five may independently place or factor the same capabilities.

### Ablation / redundancy family
Ablation, reduction, strict-gain, clean-room reconstruction:
RESEARCH-DESIGN PASS; promotion remains OPEN. Removing semantic admission, obligation generation, selection, verification, or reentry destroys a named protected behavior. Whether EWG deserves a dedicated subsystem rather than composition is still an empirical strict-gain question.

### Holdout / prospective family
Holdout Validation, Independent Replication, Discriminating Experiment Designer:
OPEN. The current fixtures are known-failure adversaries. A prospective hidden-defect corpus is still required for promotion evidence.

### Authority / governance family
Exact Object Preflight, authority, provenance, currentness, promotion gates:
SPECIFICATION PASS. Generate != Admit != Execute != Promote. Child authority cannot exceed grant. No self-promotion. OPEN and INCOMPARABLE are preserved.

## Improvements made during the sweep

1. Reclassified Take Four's special behavior as an endogenous work generator / residual-closure controller subsystem.
2. Added explicit zero-request discovery rather than hidden-job injection.
3. Added mandatory semantic admission and semantic-delta retyping.
4. Added explicit obligation selector pi.
5. Added bounded-run / PAUSED_OPEN semantics.
6. Distinguished search failure from BASIS_GAP.
7. Separated EWG lifecycle control from Improvement Core optimization policy.
8. Added explicit Tool Run Closure and HF-001 relations.
9. Added adversarial fixtures and validation matrix.
10. Added executable Python reference model.
11. Initial tests were authored but not executed before the first audit claim. That execution-truth defect was later detected.
12. Repaired the deeper false-closure bug: discharge no longer subtracts unsatisfied requirements.
13. Executed the repaired reference model in-session against 10 adversarial checks: 10/10 passed. Repository CI remains OPEN.

## Current decision

EWG-001 is a structurally coherent experimental specification and reference model for Take Four, and a candidate design input for Take Five. It is not yet promotion-ready.

The live proof obligations are:
1. implement/test Psi, the zero-request candidate-job synthesizer, on a messy held-out corpus;
2. bind generated behaviors to actual Take-4 runtime operations and prove execution truth plus reentry;
3. add repository-level automated execution/CI evidence;
4. run a prospective holdout where the hidden defect is not encoded in the fixture.

No additional architectural primitive is currently justified by the completed sweep.


## Closure-semantics correction

The earlier equation `O = Generate - D` was rejected. A discharge ledger records work history; it cannot make an unsatisfied requirement disappear. The current model generates unsatisfied requirements from state and closes only when their satisfaction predicates are verified true. This correction directly addresses premature closure.
