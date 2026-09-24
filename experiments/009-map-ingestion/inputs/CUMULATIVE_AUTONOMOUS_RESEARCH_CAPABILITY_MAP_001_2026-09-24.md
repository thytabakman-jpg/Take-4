# Cumulative Autonomous Research Capability — Mathematical Map 001

Date: 2026-09-24
Status: LIVE CANDIDATE MAP — FOUNDATIONAL TERMS OPEN
Origin: autonomous ICC goal reconstruction 008

## Problem seed

Episode-level research success is insufficient for the governing goal.

A research system can solve or advance individual tasks while:
forgetting verified discoveries;
losing old capabilities;
making prior knowledge unreachable to its controller;
requiring the user to restore context;
failing to propagate accepted changes;
or accumulating mutually interfering artifacts.

The target therefore includes cumulative autonomous research capability across episodes.

## Candidate longitudinal condition

For research episodes e_1,...,e_n with persistent states S_0,...,S_n:

VerifiedReusable(e_i) should remain available in later S_j, j>i,
unless later licensed evidence revises, retracts, supersedes, or proves it irrelevant to the protected future job.

This sentence is not yet mathematics. Every operative term is under attack.

## Dependency map

### C1 Episode
What determines episode identity? User turn, goal interval, controller program, experiment, state transition sequence, or authority-bounded run?
OPEN.

### C2 Persistent state
What survives an episode? Artifacts, observations, proofs, failed hypotheses, capabilities, routing evidence, provenance, authority, executable witnesses?
OPEN.

### C3 Contribution
What counts as a contribution rather than activity or state noise?
OPEN.

### C4 Verified
Verification relative to what observation language, evidence basis, runtime, authority and protected behavior?
OPEN.

### C5 Reusable
Reusable by existence is insufficient. Need future discoverability/reachability and admissible invocation.
OPEN.

### C6 Preservation
Literal artifact persistence is too weak. Behavioral preservation may survive representation change; file persistence may coexist with functional loss.
OPEN.

### C7 Reachability
A capability can exist but be unreachable by the controller. Need distinguish existence, search reachability, authority reachability, binding reachability and policy realizability.
OPEN.

### C8 Revision/retraction/supersession
Need licensed forgetting. Accumulation cannot mean monotonic retention of false or obsolete claims.
OPEN.

### C9 Interference
Two individually useful contributions can conflict, alter routing, invalidate assumptions, or increase search cost.
OPEN.

### C10 Forgetting/regression
Need observational tests for loss of reusable contribution and loss of controller access.
OPEN.

### C11 Capability accumulation
Set inclusion is too crude. More stored capabilities can worsen control. Need protected behavioral refinement plus reachable/useful contribution.
OPEN.

### C12 Goal continuity
Which prior contributions remain protected when governing goals change?
OPEN.

### C13 Cross-episode provenance
Future controller must distinguish source, status, evidence basis, supersession and authority.
OPEN.

### C14 Propagation
An accepted mathematical or architectural delta is not cumulatively learned until material dependents are UPDATED, PROVEN_NO_EFFECT, or OPEN/BLOCKED.
Candidate inherited from existing propagation invariant; integration OPEN.

### C15 Longitudinal success
Need a criterion stronger than per-episode success and weaker than impossible global monotonic improvement.
OPEN.

## First rival formalisms

R1 Artifact monotonicity:
A_i subseteq A_j.
Likely reject: preserves files, not usable capability; prevents licensed deletion.

R2 Capability-set monotonicity:
Cap(S_i) subseteq Cap(S_j).
Too strong/underspecified when capability identity or authority changes.

R3 Protected behavioral refinement:
S_i preceq_B S_j.
Promising but does not alone require new knowledge to remain reachable by controller.

R4 Reachable protected refinement:
S_i preceq_B S_j plus every protected reusable contribution has a future controller-realizable witness.
Current strongest candidate; still underdefined.

## First discriminator

Construct two later states with identical stored artifacts and identical terminal task capability, but only one lets the controller recover and use a prior verified contribution without user reconstruction.

If the governing goal distinguishes them, storage and terminal capability quotients are too coarse.

## Links

Connects directly to:
behavioral refinement;
capability existence/reachability/controller realizability;
job-relative diagnostic equivalence;
state quotient;
provenance;
TransferCore;
propagation invariant;
controller closure;
routing;
self-improvement regression;
Take-2 remembered folder-repair capability.

## Anti-canonization

No term in the candidate longitudinal condition is accepted merely because it appears in this map.

## Next autonomous action

Build the discriminator pair and use it to attack C5-C7: reusable, preservation and reachability.
