from reference.ewg import State, run

def test_zero_request_no_hidden_job():
    assert run(State("ZERO_REQUEST_DISCOVERY")) == "JOB_OPEN"

def test_semantic_block():
    assert run(State("JOB_CONDITIONED", obligations=["analyze"], semantic_ready=False)) == "BLOCKED"

def test_missing_binding():
    assert run(State("JOB_CONDITIONED", obligations=["execute:mta"], authority="execute")) == "OPEN_REALIZATION"

def test_authority_gap():
    assert run(State("JOB_CONDITIONED", obligations=["execute:mta"]), {"mta"}) == "BLOCKED"

def test_bounded_run_not_closure():
    assert run(State("JOB_CONDITIONED", obligations=["a"], budget=0)) == "PAUSED_OPEN"

def test_persistent_new_abstraction_does_not_false_close():
    state = State("JOB_CONDITIONED", new_abstraction=True, budget=2)
    assert run(state) == "PAUSED_OPEN"
    assert state.new_abstraction is True

def test_new_abstraction_closes_only_after_verified_resolution():
    state = State("JOB_CONDITIONED", new_abstraction=True)
    assert run(state, verified_effects={"semantic_delta_audit"}) == "CLOSED"
    assert state.new_abstraction is False

def test_persistent_verification_failure_does_not_false_close():
    state = State("JOB_CONDITIONED", verification_failed=True, budget=2)
    assert run(state) == "PAUSED_OPEN"
    assert state.verification_failed is True

def test_verification_failure_closes_only_after_verified_repair():
    state = State("JOB_CONDITIONED", verification_failed=True)
    assert run(state, verified_effects={"repair_verification_failure"}) == "CLOSED"
    assert state.verification_failed is False

def test_exec_success_then_closure():
    state = State("JOB_CONDITIONED", obligations=["execute:mta"], authority="execute")
    assert run(state, {"mta"}) == "CLOSED"
    assert "execute:mta" in state.discharged
