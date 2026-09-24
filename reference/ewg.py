from dataclasses import dataclass, field
from typing import List, Set, Optional

@dataclass
class State:
    mode: str
    obligations: List[str] = field(default_factory=list)
    discharged: Set[str] = field(default_factory=set)
    semantic_ready: bool = True
    authority: str = "analysis_only"
    new_abstraction: bool = False
    verification_failed: bool = False
    budget: int = 10
    history: List[str] = field(default_factory=list)

def generate(state: State) -> List[str]:
    obligations = list(state.obligations)
    if not state.semantic_ready and "semantic_admission" not in obligations:
        obligations.insert(0, "semantic_admission")
    if state.new_abstraction and "semantic_delta_audit" not in obligations:
        obligations.append("semantic_delta_audit")
    if state.verification_failed and "repair_verification_failure" not in obligations:
        obligations.append("repair_verification_failure")
    return [x for x in obligations if x not in state.discharged]

def step(state: State, runtime_bindings: Optional[Set[str]] = None) -> str:
    runtime_bindings = runtime_bindings or set()
    open_obligations = generate(state)

    if state.mode == "ZERO_REQUEST_DISCOVERY" and not open_obligations:
        return "JOB_OPEN"
    if open_obligations and open_obligations[0] == "semantic_admission":
        return "BLOCKED"
    if state.budget <= 0:
        return "PAUSED_OPEN"
    if not open_obligations:
        return "CLOSED" if not generate(state) else "PAUSED_OPEN"

    work = open_obligations[0]
    if work.startswith("execute:"):
        behavior = work.split(":", 1)[1]
        if behavior not in runtime_bindings:
            return "OPEN_REALIZATION"
        if state.authority not in {"execute", "production"}:
            return "BLOCKED"

    state.history.append(work)
    state.discharged.add(work)
    state.budget -= 1
    return "REENTER"

def run(state: State, runtime_bindings=None, max_steps: int = 100) -> str:
    for _ in range(max_steps):
        status = step(state, runtime_bindings)
        if status != "REENTER":
            return status
    return "PAUSED_OPEN"
