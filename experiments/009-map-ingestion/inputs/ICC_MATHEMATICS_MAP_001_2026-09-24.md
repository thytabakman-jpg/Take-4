# ICC Mathematics Map 001 — Big Picture

Date: 2026-09-24
Purpose: organize the mathematical research program by the functionality each problem unlocks.
Status: live map; not a claim that every coordinate is solved.

## North-star system

The recurring target across PD, ICC, Take Two, kernel work, and outward expansion is a system that
can:

GOAL -> STATE -> OBSERVE -> DIAGNOSE -> SELECT -> BIND -> EXECUTE -> VERIFY -> UPDATE -> REENTER

and can improve/expand that process without losing protected behavior.

The math is not one problem. It is a connected dependency map.

## M0 — Definition / distinction / sensitivity mathematics

Historical roots:
PD, ED, PDAudit 1.0/1.1, recursive audit, orthogonal audit.

Questions:
- what exactly is the object/result?
- which distinctions are real?
- which coordinates are result-sensitive?
- which representations preserve/change the result?
- what is extension-determinate?
- when are two formulations behaviorally equivalent?

Representative objects:
fibers, result-changing pairs, MinSens, ED, representation-sensitive frontiers.

Functionality unlocked:
reliable problem localization; prevention of hidden equivocation; ability to know what must be
preserved when architecture changes.

Feeds every later region.

## M1 — Behavioral quotient / identity mathematics

Current line:
B -> sigma_B -> Q_B; continuation equivalence; protected behavior quotient.

Questions:
- when are two implementations/configurations “the same” for the job?
- what is observable vs intensional equivalence?
- what survives representation changes?
- what is residual/non-reconstructible behavior?

Open coordinates include congruence under composition and sufficient continuation family H_adm.

Functionality unlocked:
replace/rewrite kernels and tools without confusing implementation change with capability loss;
compare Take Two/Three/Four; safe compression.

## M2 — Improvement / specialization / frontier mathematics

Objects:
Bcal=<K,E,J,L,H_adm,P>
Specializes_Bcal(c|c0,T)
Sig=<SEM,CONT,META>
Max_Bcal(C)
RobustGeneric_F
NoGain
nondominated frontiers.

Questions:
- what counts as a real improvement?
- what is merely different?
- what is generic vs job-specific?
- how do we preserve incomparable gains?
- how do baseline multiplicity and basis changes affect conclusions?

Functionality unlocked:
ICC can improve tools/controllers without scalar “best” mistakes and without silently regressing
protected behavior.

## M3 — Composition / interaction mathematics

Objects:
Interaction_Bcal(x,y,order)
INDEPENDENT / COMMUTES / SYNERGY / INTERFERENCE / CONFLICT / OPEN.
MultiObject and cross-mode catalytic gain.

Questions:
- when does x after y differ from y after x?
- when does a bundle do something no member can do alone?
- how do local capabilities compose into programs/specializations/controllers?
- what information is lost by decomposition?

Functionality unlocked:
tool orchestration; targeted + autonomous catalytic loops; capability bundles; safe modularity.

## M4 — Controller / endogenous search mathematics

Recent Take-4 coordinates:
C1 partial-order choice/incomparability.
C2 endogenous problem generation.
C3 hierarchical composition/noncommutation.
C4 dynamic reselection/termination.
C5 capability preservation across trajectories.

Also:
autonomous vs targeted authority;
adaptive authority vector A;
residual frontier selection;
R_i=<Delta_i,Learn_i,Next_i>.

Questions:
- how does ICC choose what problem to work on?
- how does solving one problem change the next search?
- when should it reframe rather than continue?
- how do we maximize cumulative research gain rather than per-pass gain?

Functionality unlocked:
ICC becomes a learning research controller rather than a static audit protocol.

## M5 — Dynamics / re-entry / convergence mathematics

Objects:
state S, update U, architectural succession G, fixed points, cycles, terminal conditions,
succession budget, lineage.

Questions:
- when does the loop re-enter?
- when has it converged?
- how do we detect cycling/no-op?
- when is architectural succession justified rather than ordinary state update?
- what does persistent learning mean across episodes?

Functionality unlocked:
continued autonomous work without endless self-revision; stable self-improvement; principled stop
and restart conditions.

This is the earlier “dynamical-systems” direction and must remain visible.

## M6 — Binding / kernel / execution semantics

This is the math underneath the Take Two / Take Three / Take Four and “inside vs above the
kernel” conversation.

Architecture question:
Controller -> Kernel/Worker -> Result -> Verification -> Controller.

Take Two's protected executable loop:
Observe -> PD -> Diagnose -> Decide -> Transition -> Verify -> Observe.

Questions:
- what information/authority must cross controller-kernel boundaries?
- is ICC inside the kernel, above it, or compiled into its policy?
- what is a semantic instruction versus executable binding?
- when is a controller decision faithfully realized by a worker?
- how are verification results returned without state loss?
- what behavior must a replacement kernel preserve?

Functionality unlocked:
turn ICC decisions into actual work; recover the earlier “drop a folder in and it comes out
fixed” behavior; allow kernels to be replaced while preserving capability.

This is currently one of the weakest/most operationally important regions.

## M7 — Capability boundary / reachability / acquisition mathematics

Current object:
augmented capability-gated reachability with typed cut diagnosis.

State:
z=(s,C)
typed capability hypergraph H_Xi.
State, transition, acquisition boundaries.
Target-separating cut frontier.
W_out relative novelty witness.

Questions:
- what target outcomes are unreachable?
- which transition is the blocking cut?
- is the cause missing capability, binding, authority, resource, evidence, policy, or verification?
- what acquisition changes future reachable space?
- which capability bundles restore a path?

Functionality unlocked:
ICC can discover genuinely new functionality rather than only improve what it already has.

## M8 — Observability / controllability / feedback mathematics

This is the outward direction exposed by the capability-boundary work and overlaps the earlier
dynamical-systems hunter.

Questions:
- can ICC infer the relevant internal/world state from observations?
- can available actions drive the system to a protected target?
- how reliable is the path?
- can target-level consequences be measured rather than proxy execution success?
- under partial observability/stochasticity, what can be guaranteed?

Functionality unlocked:
closed-loop control rather than “code ran successfully”; empirical learning from interventions.

This is a major bridge between M5 dynamics, M6 execution and M7 reachability.

## M9 — Evidence / uncertainty / experiment mathematics

Objects:
H_gen vs H_adm; evidence strata; OPEN resolver classes; holdouts; causal ablation; independent
replication; external evidence.

Questions:
- what evidence can discriminate live rivals?
- when is absence of gain informative?
- what experiment maximally resolves an OPEN coordinate?
- how does evidence update routing without overgeneralization?

Functionality unlocked:
ICC can actively learn which mathematical/architectural model is correct instead of only
reasoning from current state.

## M10 — Persistence / trajectory / cumulative-value mathematics

Objects:
Frozen Target Token; TargetEffect; persistent queue; improvement lineage; succession; cumulative
protected gain; capability-enabling support.

Questions:
- how is the user's actual target preserved through meta-work?
- how do useful intermediate actions get credit without pretending they completed the target?
- how do we optimize a whole research trajectory rather than isolated turns?
- how do we preserve state across execution episodes?

Functionality unlocked:
prevents TARGET-DISPLACED PROGRESS; enables long-horizon research/execution.

## The connected picture

There are four large bands:

A. KNOW WHAT MATTERS
M0 definition/sensitivity -> M1 quotient/identity.

B. KNOW WHAT IS BETTER AND HOW THINGS COMBINE
M2 improvement -> M3 composition -> M4 controller/search.

C. MAKE IT ACTUALLY RUN
M5 dynamics -> M6 binding/kernel -> M8 feedback/control -> M10 persistence.

D. GROW THE REACHABLE WORLD
M7 capability boundary/acquisition <-> M9 evidence/experimentation, feeding back into A-C.

Core cycle:

M0/M1 establish invariants
 -> M2/M3 identify admissible gains
 -> M4 chooses work
 -> M6 binds it to execution
 -> M8 observes consequences
 -> M5/M10 update/reenter
 -> M7 asks what remains unreachable
 -> M9 acquires discriminating evidence
 -> back to M0/M1.

## Important recovered “lost direction”

There are TWO previously easy-to-lose directions that belong explicitly on the map.

1. DYNAMICAL SYSTEMS / CONTROL:
fixed points, convergence, cycles, stability, reachability, controllability, observability,
termination and re-entry. This was proposed as a distinct ICC research direction before the
capability-boundary work. The new reachability work does not replace it; it connects to it.

2. KERNEL BOUNDARY / BINDING:
the controller math and the executable kernel are different layers. The unsolved question is not
merely “put ICC in the kernel or above it.” It is to characterize the interface/refinement
relation that makes either architecture behaviorally faithful. Solving that math can make the
placement question partly implementation-equivalent under the protected quotient.

## Highest-leverage intersections

I1 M1 x M6:
behavioral refinement for kernel replacement.
Unlock: Take Two functionality can survive new controllers/kernels.

I2 M3 x M4:
composition + endogenous search.
Unlock: ICC can exploit targeted/autonomous/tool synergy dynamically.

I3 M5 x M8:
dynamics + observability/controllability.
Unlock: principled re-entry, convergence and real closed-loop control.

I4 M6 x M7:
binding + capability cuts.
Unlock: distinguish “new capability needed” from “existing capability lacks executable binding.”

I5 M7 x M9:
reachability + active evidence acquisition.
Unlock: ICC can choose experiments specifically to expose/repair its own capability boundary.

I6 M4 x M10:
controller choice + trajectory value.
Unlock: optimize cumulative mathematical growth rather than local test value.

I7 M1 x M2 x M3:
quotient + improvement + composition.
Unlock: the common mathematical substrate suspected earlier:
equivalence -> specialization -> interaction -> improvement frontier.

## Current meta-hypothesis

The apparently separate math problems are increasingly clustering around three mathematical
families:

Q — QUOTIENT / INVARIANT MATH
What differences matter?

T — TRANSITION / CONTROL MATH
What changes are possible, executable, observable and stable?

F — FRONTIER / SEARCH MATH
Which nondominated next changes expand value/reachability?

Candidate compression:
ICC mathematics may ultimately be organized around <Q,T,F> plus evidence/governance indexing,
rather than the historical list of tools.

This is a hypothesis to attack, not an admitted reduction.

## Next research move

Do not pick one isolated math problem blindly.

Run coupled ICC over the seven intersections I1-I7, with each result immediately updating the
shared map. First target I1/I4 together because they connect the kernel/functionality problem to
the new capability-boundary mathematics; simultaneously preserve I3 as the control-theory
alternative representation and I7 as the common-substrate formalization.

The objective is to discover whether <Q,T,F> really compresses the map without losing any
demonstrated functionality.


## 2026-09-24 controller-closure integration

The later Take-4 pointed/autonomous experiments refine M4 and its links to M1, M3, M5, M6 and M10.

### M4 refinement — admissible-closure control

The earlier placeholders

`arg max Q | target fixed`

and

`arg max ExpectedGoalGain`

are not licensed scalar objectives. Controller choice is set-valued over an admissible/nondominated frontier unless a justified scalarization exists.

For a frozen target p*, pointed control operates inside a licensed admissible closure:

`Cl_D(z,p*)`.

Autonomous control has licensed evidence-sensitive operators that can revise the future problem/policy domain relative to governing goal G:

`Cl_A(z,G)`.

The candidate autonomous residual is:

`DeltaCl = Cl_A(z,G) \ Cl_D(z,p*)`.

DeltaCl represents genuine added capability only where it enables a verified G-relevant trajectory unavailable inside pointed closure while preserving protected behavior.

### Static equivalence boundary

Pointed and autonomous modes reduce to the same behavioral frontier, up to projection of a singleton problem label, when:
1. the autonomous problem set is {p*};
2. feasible policy maps are identical;
3. evidence semantics are identical;
4. comparison relations are identical;
5. protected-capability and authority constraints are identical;
6. stopping semantics are identical;
7. no problem-set regeneration authority exists during the episode.

### Dynamic divergence

The cleanest current divergence is evidence-sensitive problem-domain regeneration. Both modes can begin with the same singleton domain and diverge after an observation when autonomous authority permits reconstruction of the admissible problem domain and pointed authority does not.

The action/problem typing boundary is itself result-sensitive: apparent autonomous gain disappears when every useful reframe, experiment or decomposition is already admitted as an ordinary pointed action.

### Joint controller

Current candidate composition:

`AUTONOMOUS CLOSURE SELECTION -> FREEZE p* -> POINTED EXECUTION -> VERIFY -> AUTONOMOUS CHALLENGE/RESELECTION`.

Problem selection and local policy optimization generally do not commute. The controller must therefore record order-sensitive composition rather than assume alternating modes are equivalent.

This refines, rather than deletes, the earlier authority-vector result. The authority vector specifies which closure-revision operators are licensed; admissible-closure mathematics specifies the behavioral domain those permissions generate.

### Capability-preservation link

A controller/kernel replacement is not licensed merely because components or local tests survive. Protected behavior B requires a refinement/preservation witness, provisionally `S <=_B S'`, plus controller realizability and independent verification. The current research target is a behavioral quotient sufficient to certify preservation without exhaustive execution.

### Updated coupled frontier

M4 now contains five coupled problems:
C1 choice algebra under partial order/incomparability;
C2 endogenous problem-generation and admissible-closure semantics;
C3 hierarchical composition and noncommutation;
C4 dynamic reselection/termination under evidence updates;
C5 compositional capability preservation across controller trajectories.

Highest-information next work:
define Cl_D and Cl_A as typed closure operators; test extensivity, monotonicity, idempotence and authority sensitivity; test commutation with evidence update; characterize DeltaCl without scalarizing incomparable outcomes; and connect closure expansion to behavioral refinement/preservation.


---

# Map Update C66 — Routing Uncertainty / Plural Continuation Mathematics

Add M11 — ROUTING UNCERTAINTY / COLLAPSE MATHEMATICS.

Core question:
When is ICC justified in collapsing multiple materially distinct possible continuations to one?

Objects:
- continuation frontier K_t;
- routing uncertainty RU_t;
- Collapse Certificate CC;
- plural directed/autonomous/tool continuations;
- exploration/exploitation control;
- search/routing cuts versus true capability cuts.

Dependencies:
M1 quotient math removes behaviorally duplicate continuations.
M3 interaction math detects synergy/order effects.
M4 controller math generates/selects continuations.
M7 capability math tests whether apparent unreachability is caused by routing collapse.
M9 evidence math supplies discrimination.
M10 trajectory math evaluates exploration cost versus cumulative protected gain.

New high-leverage intersection I8:
M4 x M7 x M9 x M11.
Unlock:
ICC stops treating its own uncertain tool-selection judgment as ground truth. It preserves
material alternatives until evidence licenses collapse, reducing false capability diagnoses and
premature local-optimum lock-in.

Updated Q/T/F interpretation:
Q = which continuations are genuinely distinct?
T = what continuation transitions are available?
F = which nondominated continuations remain live, and when may the frontier collapse?

This is now a first-class part of the mathematics map.
