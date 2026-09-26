# Put-In Operational Contract Map 001

Date: 2026-09-24
Status: live candidate mathematical map
Origin: PD audit of the phrase "put that in".

## Distinction

Persist(X,Y), Available(X,Y), SemanticApply(X,Y), PutIn(X,Y), and RunThrough(X,Y) are distinct.

Candidate operational relation:

PutIn(X,Y) iff X crosses Y's actual input boundary and causally participates in Y's execution.

RunThrough(X,Y) iff PutIn(X,Y) AND Exec(Y,X) AND Observed(Output_Y(X)).

## Result-sensitive consequences

Writing X into a repository reachable by Y establishes at most persistence/availability.
Reasoning about what Y would do establishes semantic application.
Neither entails PutIn.

"See what comes out" adds the output-observation condition and therefore targets RunThrough.

## Open mathematical questions

1. What counts as an actual input boundary for composed controllers?
2. Is causal participation trace-based, counterfactual, or provenance-based?
3. What quotient identifies equivalent ingestion routes?
4. How is partial ingestion represented?
5. How do nested systems compose PutIn and RunThrough?
6. What evidence is sufficient to certify Exec rather than semantic simulation?

## Functionality unlocked

Prevents storage, availability, semantic simulation, and actual execution from collapsing into one
execution claim. Supplies a testable ingestion contract for Take systems and other runtimes.
