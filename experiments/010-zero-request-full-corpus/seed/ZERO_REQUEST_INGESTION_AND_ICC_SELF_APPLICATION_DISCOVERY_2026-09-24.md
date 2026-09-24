# Zero-Request Ingestion and ICC Self-Application Discovery

Date: 2026-09-24
Status: research report / architecture hypothesis
Authority: descriptive analysis only; no architecture promotion authorized

## Goal

Capture the architectural discovery exposed by the proposed Take-4 experiment before the experiment is contaminated by supplying Take-4 with a task, desired output, decomposition, or governing request.

The central question is:

Can a system receive a corpus with no externally supplied request and endogenously determine what, if anything, the corpus warrants doing?

A second question follows:

What changes when the object placed through such a tool is ICC-relevant material or ICC itself, rather than an ordinary external research object?

## 1. Existing ICC pattern

Most ICC work to date can be represented approximately as:

    ICC(T, x) -> y

where:

- T is a task, governing goal, or bounded problem;
- x is an object/corpus/state;
- ICC selects or composes capabilities;
- y is a result, state change, diagnosis, recommendation, experiment, or verified output.

PD, ImprovementCore, TransferCore, audits, mathematical maps, child ICCs, and runtime tools can all participate in this pattern.

Even autonomous ICC work generally begins from some governing goal or admissible problem domain.

## 2. Newly exposed operation

The proposed Take-4 use is different:

    x -> ICC -> ?

No task is supplied.

No question is supplied.

No desired output is supplied.

No decomposition is supplied.

No stopping condition is supplied beyond whatever can legitimately be recovered or derived.

The corpus itself is evidence from which the system must determine whether any operation is warranted.

This is not merely another tool invocation.

It introduces a new control problem.

## 3. Provisional unbounded-ingestion operator

A provisional representation is:

    I(x) -> <G?, P?, A?, C?, O?>

where:

- G = recoverable governing goal(s), if warranted;
- P = problems or opportunities exposed by the corpus;
- A = admissible actions;
- C = capabilities worth invoking;
- O = warranted outputs.

Every coordinate can remain OPEN.

The operator must not invent a goal merely because the downstream controller expects one.

This makes the operation directly dependent on epistemic constraints developed in PD research.

## 4. Difference from current Take-4 Experiment 009

Experiment 009 currently implements an actual input boundary for map ingestion.

Its procedure is approximately:

    known corpus type
    -> known discovery rule
    -> known ingestion procedure
    -> known observable output

It automatically discovers every tracked text artifact whose filename contains "map" plus the mathematical MASTER_REGISTER, hashes/reads them, emits an inventory/vocabulary result, runs the closed-loop witness, checks kernel fitness, and uploads an artifact.

That is real ingestion/execution/observation.

But it is still bounded in advance by:

- the source repository;
- the input class;
- the discovery rule;
- the ingestion procedure;
- the expected output class.

Its own documentation explicitly leaves semantic ICC synthesis OPEN.

The newly proposed operation is stronger:

    corpus -> ?

The system must determine what the material is, what matters, whether action is warranted, which capabilities are relevant, what questions emerge, and what output form follows.

## 5. Relation to the desired historical Take-2 behavior

The user has repeatedly described a valuable earlier behavior approximately as:

"dump folders in and they come out fixed."

The new formulation clarifies why that behavior is difficult to recover.

The valuable capability was not simply file processing.

It required endogenous interpretation and orchestration:

    ingest
    -> recover object/state
    -> determine relevant problems
    -> select capabilities
    -> perform work
    -> verify consequences
    -> continue/reenter as warranted

The new architecture must be stronger than assuming "fixed" is the required result.

For a zero-request corpus, the warranted result could instead be:

- organization;
- synthesis;
- contradiction detection;
- mathematical formalization;
- architecture repair;
- source acquisition;
- multiple child investigations;
- a persistent queue;
- no action;
- OPEN.

The system, constrained by evidence and authority, must determine which of these is justified.

## 6. Missing pre-goal stage

Current controller models generally begin from a governing goal:

    G
    -> ORIENT
    -> NAVIGATE
    -> RESOLVE
    -> SELECT
    -> EXECUTE
    -> VERIFY
    -> UPDATE
    -> RESELECT

Zero-request ingestion exposes a missing stage before G:

    X
    -> DISCOVER
    -> G / P / OPEN
    -> ICC
    -> ...

DISCOVER here is not ordinary search.

It is reconstruction of the intentional possibilities of the corpus without imposing an intentional structure in advance.

This creates a new architectural boundary between raw/partially interpreted input and goal-directed control.

## 7. PD connection

PD is directly relevant because the new operation requires the system to distinguish:

- what object is actually present;
- which distinctions are result-sensitive;
- what can be inferred from the corpus;
- what remains underdetermined;
- which apparent goals are imported rather than evidenced;
- which representations preserve or alter the result;
- when multiple interpretations remain PLURAL or OPEN.

Therefore goal-free ingestion cannot safely be implemented as unconstrained goal invention.

A core epistemic rule is:

    absence of supplied goal != license to manufacture a goal

The system needs a warranted transition from corpus evidence to intentional structure.

## 8. Self-application discovery

The prompt exposed a second, separate architecture.

Three configurations must be distinguished.

### Configuration A: external tool use

    ICC -> Tool(x)

ICC controls a tool applied to an external object.

### Configuration B: ICC improves a tool

    ICC -> Improve(Tool)

The tool itself becomes the object of ICC-directed analysis/improvement.

### Configuration C: tool applied to ICC or ICC-relevant corpus

    Tool(ICC / ICC-corpus)

Here the object passed through the tool is the controller, its architecture, its history, or evidence about its own operation.

This third configuration is not reducible to ordinary tool use.

It creates a possible self-referential improvement channel:

    ICC_n
    -> Tool(ICC_n)
    -> Evidence
    -> ICC_(n+1)

A tool controlled by ICC can therefore produce evidence about ICC that the controller's current internal representation may not expose.

That evidence can subsequently become input to controller improvement.

## 9. Why self-application must remain typed

This must not be collapsed into generic "self-improvement."

Evaluator, evaluated object, runtime, and evidence can become coupled.

Relevant risks include:

- circular validation;
- evaluator/evaluated non-independence;
- self-confirming goal reconstruction;
- loss of baseline;
- hidden architecture mutation;
- confusing semantic improvement with runtime improvement;
- treating self-generated evidence as independently validating;
- recursive drift away from the user's governing target.

Therefore self-application requires explicit provenance and baseline preservation.

## 10. New ICC capability candidate

The discovery suggests a new controller capability:

    goal-free ingestion and endogenous task formation under epistemic constraints

This capability is broader than Experiment 009.

It connects multiple regions of the current ICC mathematics map:

- M0 definition/distinction/sensitivity mathematics;
- M4 controller/endogenous-search mathematics;
- M6 binding/kernel/execution semantics;
- M7 capability boundary/reachability;
- M9 evidence/experiment mathematics;
- M10 persistence/trajectory mathematics.

It also exposes a possible new intersection among these regions rather than fitting cleanly inside only one existing map.

## 11. Zero-request experimental condition

The proposed experiment must preserve a true zero-request condition.

The experimental input is:

    Input = X

where X is the frozen corpus.

The input must not additionally contain instructions such as:

- summarize this;
- determine the best architecture;
- find the problems;
- improve ICC;
- organize the material;
- decide what to do;
- reconstruct the goal.

Even "figure out what to do with this" is itself a control instruction and therefore changes the condition being tested.

The experiment asks whether warranted intentional structure emerges without that external instruction.

## 12. Proposed ICC self-application condition

A second condition can use an ICC-relevant corpus:

    Input = ICC-relevant corpus

This corpus can contain:

- the conversation;
- kernel reports;
- ICC reports;
- relevant mathematical maps;
- Take-2/Take-3/Take-4 evidence;
- controller history;
- experiment results;
- current architecture evidence.

The system is not told that the purpose is to improve ICC.

It is not told which parts are important.

It receives the corpus.

What it does becomes experimental evidence.

## 13. Required protections before the experiment

The experiment must preserve enough structure to distinguish actual endogenous behavior from hidden prompting.

Minimum protections:

1. Freeze the exact input corpus and hash/identify it.
2. Preserve the absence of a user task as an experimental fact.
3. Record every automatically supplied system/controller instruction.
4. Preserve the exact controller/kernel/runtime versions.
5. Preserve provenance for every additional source acquired.
6. Record endogenous goals/problems separately from externally supplied constraints.
7. Preserve OPEN rather than forcing task formation.
8. Record all capability selections and child-generation events.
9. Record execution receipts and post-state observations.
10. Preserve the original corpus and baseline unchanged.
11. Separate experimental outputs from production authority.
12. Prevent self-generated conclusions from automatically promoting themselves.

These protections define the experimental boundary without specifying what substantive work the system must perform.

## 14. Queue/concurrency consequence

The earlier proposal to use Take-4 while other work may also be using it exposes a separate runtime requirement.

If Take-4 becomes a reusable ingestion service, it needs job identity and concurrency semantics.

A candidate lifecycle is:

    SUBMITTED
    -> QUEUED
    -> CLAIMED
    -> RUNNING
    -> COMPLETED / BLOCKED / FAILED

This is runtime infrastructure, not part of the semantic request.

A queue must preserve:

- exact input identity;
- controller/runtime version;
- claim ownership;
- immutable baseline;
- execution receipts;
- result identity;
- reentry state.

Queue infrastructure must not add a substantive task to a zero-request job.

## 15. ICC decision

Do not yet run the conversation corpus through Take-4 with a descriptive request.

Doing so would destroy the clean zero-request condition.

First create/generalize an input boundary capable of accepting a frozen corpus with no substantive task.

Then submit only the corpus.

Observe what the system does.

The resulting behavior is evidence about whether Take-4 can cross:

    uninterpreted/partially interpreted corpus
    -> warranted intentional structure
    -> controlled work

without an externally supplied governing request.

## 16. Implication for ICC architecture

This operation is not merely a Take-4 feature.

If validated, it becomes a candidate ICC capability.

ICC would then support both:

    Given G, determine and perform work that advances G.

and:

    Given X without G, determine whether X warrants formation/recovery of G, P, or OPEN and proceed only under justified control.

That expands ICC from a goal-directed adaptive controller toward a system capable of epistemically constrained endogenous task formation.

## 17. Central research question

The experiment can now be stated without turning it into the runtime prompt:

Can Take-4 cross from a corpus with no externally supplied task to warranted intentional structure and subsequent controlled work, while preserving OPEN, provenance, authority, baseline identity, and protection against self-authorizing recursion?

This question belongs to the research report and evaluator.

It does not belong inside the zero-request input.

## 18. Current recommendation

Preserve this discovery as a separate mathematical and architectural research coordinate.

Do not silently fold it into existing "autonomy" terminology.

Autonomous work given a governing goal and endogenous task formation from a corpus with no supplied goal are different capabilities.

Likewise, ordinary ICC tool use and applying an ICC-controlled tool to ICC itself are different configurations.

The next implementation experiment needs to preserve these distinctions so the resulting evidence can tell us whether the capability actually exists.
