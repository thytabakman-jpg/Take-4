# Improvement Core conversation-wide audit — 2026-09-26

Scope: the conversation that developed behavior-first capabilities, the behavioral compiler idea,
Improvement Core activation/closure logic, PD decomposition, Take Two/Take Four analysis, and EWG-001.

Authority: analytical/experimental only. No production promotion.

## Governing finding

The conversation made a genuine architectural advance but repeatedly collapsed four distinct statuses:

PROPOSED -> SPECIFIED -> EXECUTED -> INTEGRATED

A statement at one status was sometimes narrated as though it had reached a later status.

The durable correction is to require every load-bearing system claim to carry one of these states,
plus evidence and authority.

## Findings

1. Behavior-first decomposition is the strongest cross-cutting improvement in the conversation.
   Tool names are implementations; behaviors/capabilities are the reusable unit.

2. The exact count "58 capabilities" is not canonical from this conversation-wide audit.
   Historical counts may refer to recovered objects, tools, or capability candidates. A fresh normalized
   inventory is required before treating any count as architecture.

3. The behavioral compiler remains a candidate formal architecture. Its constructive synthesis
   function Gamma and universal/adequacy claims are not established by this conversation.

4. The Improvement Core premature-closure diagnosis is sound at the design level: capability possession
   does not imply correct activation. The obligation/requirement layer is needed. However, the conversation
   did not prove that the current live Improvement Core runtime has been modified accordingly.

5. PD is not removed. The canonical PD project already distinguishes formal determinacy work from the
   audit/protocol object. PDAudit can be treated as an executable behavioral machine without collapsing the
   research program into a tool.

6. "Run every tool/behavior" was previously represented as a full-stack run, but the evidence supports an
   adversarial review matrix, not literal independent runtime execution of every historical tool. This is
   now corrected in the EWG audit.

7. The first EWG reference-test claim violated execution truth: tests had been written, not yet executed.
   The tests were subsequently executed in-session.

8. Actual execution then exposed a deeper false-closure bug: subtracting the discharge ledger from regenerated
   obligations allows completed work to mask a still-unsatisfied requirement.

9. The closure model is now repaired:
   work history is evidence only; closure depends on verified satisfaction predicates in current state.

10. The repaired reference model passed 10/10 in-session adversarial checks. This remains reference-model
    evidence, not Take Four runtime binding evidence and not repository CI.

## Current architecture state

Take Four branch: ic/endogenous-work-generator-v1

EWG-001 status:
- mathematical/specification object: candidate, materially improved;
- reference implementation: executable in-session;
- zero-request synthesizer Psi: OPEN;
- actual Take Four behavior bindings: OPEN;
- repository CI: OPEN;
- prospective holdout: OPEN;
- production authority: NONE;
- promotion: OPEN.

## Improvement Core decision

Do not add another architectural primitive now.

The next highest-value work is execution-truth closure:
1. implement Psi on a genuinely messy held-out corpus;
2. bind generated behavior requests to actual Take Four operations;
3. create repository-level automated tests;
4. run a prospective hidden-defect holdout;
5. only then compare EWG against simpler compositions by ablation/strict-gain.

For Take Five, migrate the corrected behavior contracts and invariants, not the Take Four repository layout
and not any unverified success claim.

## New invariant

No system claim may advance from SPECIFIED to EXECUTED, or from EXECUTED to INTEGRATED, without the
corresponding witness. No successful tool run may discharge an underlying requirement unless the required
postcondition is verified in state.
