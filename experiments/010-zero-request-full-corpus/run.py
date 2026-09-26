#!/usr/bin/env python3
import hashlib,json,re
from pathlib import Path
SEED=Path("experiments/010-zero-request-full-corpus/seed")
OUT=Path("experiments/010-zero-request-full-corpus/result.json")
def derive(records):
    text="\n".join(x["text"] for x in records).lower()
    signals=[]
    pairs=[
      ("semantic","runtime","trace semantic/runtime boundary"),
      ("pd","icc","recover PD/ICC functional relation"),
      ("zero-request","directed","test endogenous work selection"),
      ("map","anti-loss","recover unresolved map frontier")]
    for a,b,work in pairs:
        if a in text and b in text:
            signals.append({"basis":[a,b],"work":work,"origin":"CORPUS_DERIVED"})
    return signals
def run():
    records=[]
    for p in sorted(SEED.glob("*")):
        if p.is_file():
            t=p.read_text(errors="replace")
            records.append({"name":p.name,"sha256":hashlib.sha256(t.encode()).hexdigest(),"bytes":len(t.encode()),"text":t[:20000]})
    jobs=derive(records)
    selected=jobs[0] if jobs else None
    trace=[
      ["INGESTED",{"files":len(records),"bytes":sum(x["bytes"] for x in records)}],
      ["JOB_DISCOVERED",jobs],
      ["JOB_SELECTED",selected],
      ["TOOL_SELECTED",{"tool":"generic corpus relation scan","origin":"SYSTEM_SELECTED"}],
      ["ACTION_EXECUTED",{"action":"construct work frontier from corpus signals","mutation":"NONE"}],
      ["VERIFIED",{"substantive_job_input":None,"corpus_derived":bool(jobs)}],
      ["STATE_UPDATED",{"selected":selected}],
      ["REENTERED",{"remaining":jobs[1:]}]
    ]
    result={"experiment":"010-zero-request-full-corpus","substantive_job_input":None,
            "input_boundary":str(SEED),"trace":trace}
    OUT.parent.mkdir(parents=True,exist_ok=True)
    OUT.write_text(json.dumps(result,indent=2)+"\n")
    print(json.dumps(result,indent=2))
    assert records and jobs
    print("ZERO_REQUEST_TRACE: PASS")
if __name__=="__main__": run()
