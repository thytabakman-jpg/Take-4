# Comprehensive Kernel Lineage Evaluation and ICC Recommendation

Date: 2026-09-24
Status: historical and architectural evaluation
Scope: Reaserch, Take-2, Take-3, Take-4, and the controller/runtime distinctions exposed by ICC work

## Goal

Evaluate every kernel lineage and meaningful kernel iteration currently recoverable from repository history, identify strengths, weaknesses, gains, regressions, and capability cuts, and derive an architecture recommendation using the ICC framework.

This report distinguishes kernel, controller, runtime, epistemic machinery, and repository architecture. Earlier work sometimes allowed these roles to blur together. That distinction is itself one of the central findings.

## Executive result

Four kernel lineages are materially relevant:

1. Reaserch distributed architecture and its Project Anatomy Semantic Kernel candidate.
2. Take-2 clean-room / PD-centered kernel.
3. Take-3 clean-room minimal control kernel.
4. Take-4 informed-reconstruction kernel and its later functional controller/execution experiments.

A separate controller lineage also exists and must not be treated as a sequence of kernels:

IC-018 -> IC-022 -> later ICC/controller development -> autonomous/recursive ICC.

The strongest evidence does not support selecting any current kernel unchanged.

The recommended synthesis is:

- a small invariant/transition kernel;
- PD as the epistemic reasoning path;
- ICC as the recursive adaptive controller above the kernel;
- a separately accountable worker/runtime;
- explicit verification and observation;
- persistent cumulative state;
- Take-3's strict architectural admission rule to prevent renewed accretion.

The central architecture is therefore not "put ICC and PD wholesale inside KERNEL.yaml." It is a typed closed loop in which the kernel enforces contracts, PD performs epistemic work, ICC controls search and orchestration, runtime executes, verification establishes consequences, and persistent state feeds the controller.

## 1. Reaserch distributed architecture

Reaserch is the accumulated historical operating environment. It does not use the same single root KERNEL.yaml convention as Take-2 through Take-4.

It accumulated project authority, state, audits, routing, event handling, ImprovementCore, TransferCore, PracticalCore, PD machinery, workflows, registries, ledgers, repair mechanisms, and specialized controls.

### Strengths

Reaserch achieved broad capability coverage.

It generated distinctions that survived later reconstruction:

- authority is not evidence;
- history is not current authority;
- storage topology is not semantic topology;
- derived views are not authoritative merely because they are convenient;
- semantic success is not runtime success;
- OPEN must survive;
- semantic distinctions do not automatically require independent storage surfaces.

Its accumulated corpus is valuable historical evidence and remains an authority source for capabilities/projects not migrated elsewhere.

### Weaknesses

The architecture grew by accretion.

Newly discovered problems frequently produced new files, registries, policies, workflows, engines, or control surfaces. This increased coverage while making global behavior harder to recover and reason about.

Recurring costs included:

- overlapping or duplicate machinery;
- unclear ownership;
- stale derived state;
- orphaned outputs;
- hidden coupling;
- manual orchestration;
- wrong-object/currentness failures;
- uncertainty about whether a control existed semantically, operationally, or both.

The important lesson is not that Reaserch lacked capability. It is that capability and architecture became too tightly coupled.

## 2. Reaserch Project Anatomy Semantic Kernel Candidate 0.1

Commit evidence on 2026-09-23 created a file explicitly titled "Project Anatomy Semantic Kernel — Candidate 0.1."

Its purpose was to freeze enough typed vocabulary to run relational PD without pre-deciding the final ontology.

It introduced:

- PROJECT;
- eight candidate architecture axes;
- thirteen candidate project-anatomy slots;
- typed applicability;
- coordinate-specific authoritative ownership;
- derived views;
- projection;
- history evidence and reconciliation;
- distinctions among PC-RUNTIME, G2P, G2U, G2R;
- the three-engine partition as a testable candidate rather than an assumed natural kind.

It explicitly prohibited unearned identities including:

PROJECT = FOLDER
PROJECT PAGE = AUTHORITY
GOAL = EVERY INTENTIONAL OBJECT
GOAL HIERARCHY = DEPENDENCY SPINE
SPINE = SPLINE
HUMAN NAVIGATION = STORAGE TOPOLOGY
PRACTICALCORE RUNTIME = G2P = G2U = G2R
CURRENT THREE ENGINES = NATURAL COMPLETE PARTITION
HISTORY = CURRENT AUTHORITY

### Strengths

This was a strong semantic correction to the accumulated Reaserch architecture.

It separated implementation/storage structures from semantic structures, authority structures, and human-facing structures.

It treated relations themselves as objects requiring audit rather than assuming that object distinctions alone were sufficient.

### Weaknesses

It was primarily an ontology/semantic kernel.

It did not itself provide a compact executable control loop capable of taking arbitrary incoming work through discovery, selection, execution, verification, persistent update, and autonomous reentry.

Its own status was candidate/disposable pending relational testing.

## 3. Take-2 iteration 0: clean-room direction

The first Take-2 commit on 2026-09-24 was "Bootstrap Take-2 as a clean-room research kernel."

At this initial point the repository contained only README.md. No KERNEL.yaml yet existed.

The architectural shift was nevertheless important:

migrate capabilities, not legacy files.

### Strength

This changed the unit of inheritance.

Instead of copying Reaserch architecture because it existed, Take-2 required capabilities to demonstrate value before admission.

This is one of the strongest architectural decisions in the lineage.

### Weakness

This stage was a design direction, not yet an implemented kernel contract.

## 4. Take-2 iteration 1: PD-centered kernel

The next Take-2 iteration created the root KERNEL.yaml.

Its core loop is described as:

Observe -> PD -> Diagnose/Understand -> Decide -> Transition -> Verify -> Observe

Its kernel principles include:

- distinctions_do_not_imply_surfaces
- consequential_change_uses_transition
- pd_is_epistemic_kernel
- preserve_OPEN_and_incomparability
- evidence_does_not_self_authorize
- observations_precede_causal_claims
- migrate_capabilities_not_files
- executable_fitness_over_policy_only

Its durable primitive surfaces are:

- Object
- Relation
- Event
- Transition
- Observation

It also defines transition statuses, epistemic statuses, and migration dispositions.

Subsequent work added a ledger, executable kernel fitness checks, a GitHub Actions workflow, and experimental slices.

### Strengths

Take-2 is the strongest explicit epistemic kernel in the current lineage.

It correctly makes PD part of the reasoning/control path rather than an optional after-the-fact audit.

It protects several important invariants:

- evidence does not self-authorize;
- consequential change is transition-governed;
- observation is distinguished from causal inference;
- OPEN/plurality survive;
- semantic distinctions do not automatically create infrastructure;
- capability migration is separated from file migration;
- executable evidence matters.

Its experiments produced real mathematical clarification.

### Experiment evidence

Modifier/Router mathematics distinguished higher-order transformation from state-conditioned routing and rejected unjustified total-order selection.

Update mathematics separated:

- Event as occurrence record;
- Transition as governed attempted/application record;
- U as semantic persistent state-transition law.

State mathematics defined state as the minimal persistent semantic carrier sufficient for future behavior rather than identifying state with a file, ledger, snapshot, or dashboard.

These results demonstrate that the kernel can support serious formal work rather than merely store policy prose.

### Weaknesses

Take-2 does not adequately represent the full adaptive controller.

It preserves important machinery used inside a research episode, but it does not fully encode the supervisory capability that decides:

- what problem matters next;
- when to regenerate the problem domain;
- when to invoke a different capability;
- when to recurse;
- when to delegate;
- when a new mathematical map has appeared;
- when verification requires another episode;
- when the governing goal is actually complete.

This is the major capability cut.

The earlier desired behavior was approximately:

messy input -> recover actual state/problem -> diagnose -> organize -> repair/work -> verify -> continue until closure.

Take-2 captured much of the semantic and epistemic machinery inside that process but did not fully preserve orchestration as a protected capability.

## 5. Take-3: clean-room minimal control kernel

Take-3 was created as ICC's clean-room control experiment.

Its objective is broad_task_to_verified_reentered_state.

Its durable candidate record types are only:

- Task
- Finding
- Action
- Result

Its loop is:

TASK -> DISCOVER -> DECIDE -> ACT -> VERIFY -> REENTER

Its admission rule is:

add_architecture_only_after_result_sensitive_failure_or_strict_gain

### Strengths

Take-3 asks the key scientific question:

How little architecture is actually necessary?

It refuses to treat historical architecture as evidence of necessity.

This makes Take-3 a valuable ablation/control condition.

The admission rule is especially strong and deserves to survive into future architecture-development practice.

### Weaknesses

The minimal representation deliberately omits distinctions that historical evidence suggests can change results.

Its own bootstrap result immediately identifies wrong-object recovery as a likely discriminator because exact identity/currentness is not represented as explicitly as in Take-4.

Take-3 therefore has high experimental value but insufficient current evidence as a complete operating architecture.

Its job is partly to falsify unnecessary complexity.

## 6. Take-4: informed-reconstruction kernel

Take-4 is ICC's informed-reconstruction experiment.

It may inherit evidence and demonstrated distinctions but not architecture merely because architecture exists.

Its root kernel declares:

- Reaserch and Take-2 as external corpora;
- IC-022 as controller_candidate;
- IC-2026-09-23-018 as promoted_runtime_external.

Its semantic coordinates are:

- Episode
- Object
- Evidence
- Authority
- Decision
- Transition
- Verification
- State Delta

Its loop is:

ORIENT -> NAVIGATE -> RESOLVE -> SELECT -> EXECUTE -> VERIFY -> UPDATE -> RESELECT

Its protected distinctions include:

- project-local authority;
- exact identity;
- provenance;
- currentness;
- OPEN;
- INCOMPARABLE;
- candidate/promoted distinction;
- semantic/runtime authority separation.

It also states:

inheritance_rule: inherit_evidence_not_architecture

surface_rule: semantic_coordinate_does_not_require_independent_registry

### Strengths

Take-4 is the strongest current representation of historically demonstrated control distinctions.

It explicitly represents exact identity/currentness.

It separates evidence from authority.

It represents eligible/selected/incomparable decisions.

It separates transition from verification.

It represents persistent state delta and reentry.

Its inheritance rule is a stronger generalization of Take-2's "migrate capabilities, not files."

### Weaknesses

The root kernel explicitly points to IC-022, while subsequent ICC/controller work advanced beyond that point. The pointer is therefore a historical controller candidate, not a sufficient description of the latest controller capability.

Take-4 also does not explicitly declare PD as its epistemic kernel in the way Take-2 does.

Thus Take-4 gained stronger controller-oriented distinctions without formally inheriting Take-2's strongest epistemic integration.

## 7. Take-4 functional iterations beyond KERNEL.yaml

A critical finding is that much of Take-4's real evolution occurred without repeatedly rewriting KERNEL.yaml.

Therefore repository history contains functional architecture iterations that are not cleanly represented as kernel-version numbers.

The major stages include:

1. controller mathematics;
2. autonomous stewardship witness;
3. minimal executable closed loop;
4. multi-generation autonomy;
5. adaptive-program reconstruction;
6. semantic ablation;
7. runtime-blocker diagnosis and repair;
8. ten-step recursive autonomy;
9. autonomous governing-goal reconstruction.

### Controller mathematics

The controller-math work distinguished pointed/directed control from autonomous control.

The key discovery was that autonomy is not merely "more actions."

It adds licensed evidence-sensitive authority to expand, contract, or reconstruct the admissible problem closure relative to the governing goal.

This identified problem-generation itself as result-sensitive.

### Autonomous witness

The autonomous stewardship witness tested a closure-aware controller against a pointed incumbent on a synthetic fixture.

It showed that semantic reasoning alone was insufficient.

The next bottleneck became executable binding:

Can a real controller issue a transition request, obtain worker acknowledgement/post-state evidence, feed verification back into control, and re-enter?

### Minimal closed loop

The next experiment built a small executable trace around:

SELECT -> BIND -> EXECUTE -> OBSERVE -> VERIFY -> UPDATE -> RESELECT

This is a major architectural gain.

It explicitly tests the boundary between semantic intent and executed transition.

### Recursive/adaptive autonomy

Later Take-4 work added adaptive harnesses, blocker diagnosis, recursive autonomy, and autonomous goal reconstruction.

The important result is that controller development became dynamic and evidence-responsive rather than a fixed audit sequence.

### Autonomous goal reconstruction

The autonomous goal-reconstruction experiment rejected several narrower governing goals.

It selected the stronger current candidate:

Create a system that can accept a governing research goal and autonomously perform the work required to advance it over time, while preserving and accumulating verified knowledge and capabilities, detecting and repairing failures in its own research process, and improving that process when doing so advances the governing goal.

This exposed a new longitudinal requirement:

the system must preserve reusable verified contributions across episodes and keep them reachable by future control.

That is stronger than successful isolated task completion.

## 8. Controller lineage is not kernel lineage

The repository evidence requires a clean distinction between:

1. repository/container;
2. semantic kernel;
3. epistemic machinery;
4. controller;
5. runtime/worker;
6. verification;
7. persistent state/authority.

The controller lineage includes IC-018, IC-022, and later autonomous/recursive ICC development.

It is a category error to count each controller version as a kernel version.

Likewise, a kernel pointing to a controller does not make the controller identical to the kernel.

Take-4 makes this especially clear by separately declaring:

controller_candidate: IC-022
promoted_runtime_external: IC-2026-09-23-018

## 9. Cross-lineage strengths

### Reaserch contributes

- accumulated real-world failure evidence;
- rich project/capability history;
- authority/state machinery;
- many distinctions later shown to matter.

### Project Anatomy Semantic Kernel contributes

- semantic typing;
- axis separation;
- authority/view distinction;
- projection;
- anti-conflation constraints.

### Take-2 contributes

- PD as epistemic kernel;
- compact durable primitives;
- transition discipline;
- executable fitness;
- OPEN/incomparability preservation;
- capability-not-file migration;
- strong mathematical experiment support.

### Take-3 contributes

- clean-room control;
- strict architecture admission;
- ablation logic;
- protection against inherited complexity.

### Take-4 contributes

- exact identity/currentness;
- evidence/authority separation;
- explicit decision frontier;
- verification/state-delta/reentry;
- informed reconstruction;
- autonomous controller mathematics;
- executable binding;
- recursive/adaptive controller evidence;
- governing-goal reconstruction.

## 10. Cross-lineage weaknesses

### Reaserch

Capability accretion became architecture accretion.

### Project Anatomy Semantic Kernel

Strong ontology, weak executable closed-loop control.

### Take-2

Strong epistemic/transition kernel, insufficiently represented adaptive orchestration.

### Take-3

Strong minimality experiment, intentionally underpowered representation.

### Take-4

Strong controller/control semantics, incomplete explicit PD integration, stale explicit IC-022 pointer relative to later controller research, and no evidence yet that the entire desired cumulative system has been validated end to end.

## 11. ICC diagnosis of the historical failure

The repeated architectural error was placing newly discovered functionality at the wrong layer.

Examples:

- PD was at times treated as though it were the whole system rather than epistemic machinery.
- ICC/controller behavior was at times discussed as though it were the kernel.
- runtime success and semantic success were conflated.
- files/registries were allowed to stand in for capabilities.
- semantic distinctions were allowed to imply durable surfaces.
- Take-2's useful behavior was partially identified with its represented primitives rather than with the orchestration policy that made those primitives work together.

The corrected decomposition is:

Goal
-> Controller
-> Epistemic reasoning
-> Kernel transition contract
-> Worker/runtime
-> Observation
-> Verification
-> Persistent state
-> Controller

These are distinct jobs even when one implementation combines several of them.

## 12. Recommendation

Do not select Reaserch, Take-2, Take-3, or Take-4 unchanged.

Do not rebuild Reaserch's full architecture.

Construct the next experiment around a synthesis of demonstrated strengths.

### 12.1 Kernel

Keep the kernel small.

Its job is to enforce stable semantic/transition contracts such as:

- exact identity/currentness;
- authority;
- provenance;
- protected behavior;
- admissible transition;
- verification obligations;
- OPEN/INCOMPARABLE preservation;
- persistent state-delta/reentry information.

Take-4 supplies the strongest current coordinate model for this layer, while Take-2 supplies important transition semantics.

### 12.2 PD

Retain PD in the epistemic path as Take-2 demonstrated.

PD answers questions including:

- what exactly is the object?
- which distinction changes the result?
- what hidden dependency exists?
- what remains OPEN?
- what representation is adequate?
- what apparent identity or reduction fails?

PD does not need to become the entire controller.

### 12.3 ICC

Use the newest validated ICC/controller lineage as the recursive adaptive controller above the kernel.

Its job includes:

- reconstruct the governing goal;
- choose the current problem;
- generate/revise subproblems;
- choose capabilities;
- invoke PD recursively;
- delegate;
- reconcile child results;
- detect newly exposed mathematical maps;
- decide when evidence requires reframing;
- reenter after failed verification;
- choose the next episode;
- stop only at a verified goal-relative closure condition.

This is the capability missing from Take-2's compact kernel.

### 12.4 Runtime

Keep runtime execution separately accountable.

A controller decision is not evidence that an operation occurred.

The worker/runtime must return execution receipts and post-state observations.

### 12.5 Verification

Verification must establish both target effect and preservation of protected behavior.

Execution success alone is insufficient.

### 12.6 Persistent state

The system needs cumulative state capable of retaining verified reusable contributions across episodes while supporting explicit revision/retraction.

This is necessary to satisfy the governing cumulative-research goal.

### 12.7 Architecture admission

Adopt Take-3's rule:

add architecture only after result-sensitive failure or strict gain.

This is the primary defense against rebuilding Reaserch's accretion problem.

## 13. Recommended relationship among ICC, PD, kernel, runtime, and state

The evidence does not support simply placing ICC and PD wholesale inside KERNEL.yaml.

The recommended relation is:

ICC
-> PD / epistemic work
-> KERNEL CONTRACT
<-> RUNTIME
-> OBSERVATION
-> VERIFICATION
-> PERSISTENT STATE
-> ICC

with recursive re-entry and with PD callable again whenever semantic uncertainty becomes result-sensitive.

The kernel contains contracts ICC and PD cannot silently violate.

PD supplies epistemic machinery.

ICC supplies adaptive control.

Runtime supplies execution.

Verification supplies evidence about consequences.

Persistent state supplies cumulative memory and future reachability.

## 14. Why this explains the Take-2 capability-loss problem

The earlier high-value Take-2-like behavior was not merely a property of five durable primitives.

The useful behavior depended on coherent orchestration across:

- recovery;
- diagnosis;
- tool selection;
- transformation;
- verification;
- reentry;
- continuation.

When the architecture was formalized, many semantic invariants were preserved but orchestration itself was not adequately frozen as a protected capability.

Later Take-4 controller mathematics independently rediscovered this missing layer through endogenous search, closure revision, autonomous stewardship, and executable binding.

Therefore the old and new systems are not competing alternatives.

The desired system combines their demonstrated capabilities at the correct architectural layers.

## 15. Current synthesis candidate

The strongest current architecture hypothesis is:

Take-4 semantic/control distinctions
+ Take-2 PD epistemic core and transition discipline
+ Take-3 strict architectural minimality/admission
+ newest validated autonomous ICC controller
+ separately accountable executable runtime
+ explicit verification
+ persistent cumulative state.

This is a hypothesis to test, not yet a promoted production architecture.

## 16. Required next experiment before implementation/promotion

Do not immediately promote the synthesis.

First freeze the protected behavior that a replacement must preserve.

Then construct matched tests against the existing systems.

The experiment must determine whether the synthesis:

- recovers exact current objects;
- preserves constraints;
- preserves provenance and authority;
- detects hidden semantic primitives;
- preserves OPEN/INCOMPARABLE;
- performs broad-corpus navigation;
- chooses and binds capabilities;
- executes rather than merely recommends;
- obtains post-state evidence;
- verifies target effect;
- reenters after failure;
- preserves reusable prior capability;
- captures new mathematical maps;
- propagates accepted changes;
- distinguishes capability absence from binding/runtime failure;
- performs autonomous problem reselection;
- terminates at verified goal-relative closure.

Take-3's anti-overfit logic remains important: historical failure classes can guide development, but a prospective holdout must test generalization.

## 17. Final recommendation

The next architectural target is not another monolithic kernel.

It is a minimal typed closed-loop research system with a stable kernel contract and replaceable/improvable controller, epistemic, and runtime components.

The kernel protects invariants.

PD protects epistemic quality.

ICC supplies adaptive intelligence and orchestration.

Runtime establishes action truth.

Verification establishes consequence truth.

Persistent state makes improvement cumulative.

Architectural additions earn admission through result-sensitive necessity or strict demonstrated gain.

This arrangement best explains the historical strengths and failures currently visible across Reaserch, Take-2, Take-3, Take-4, and the ICC experiments.

## Evidence status and limitations

This report is based on the repository state and commit history inspected on 2026-09-24.

Not every historical conceptual "kernel" necessarily existed as a file named KERNEL.yaml. The report therefore distinguishes explicit root kernels, semantic-kernel artifacts, and functional architecture/controller iterations.

The recommendation is an ICC-derived architecture hypothesis. It is not a promotion decision and does not authorize mutation of any existing production authority.
