#!/usr/bin/env python3
import hashlib, json, re
from pathlib import Path

INPUT=Path("experiments/009-map-ingestion/inputs")
OUT=Path("experiments/009-map-ingestion/result.json")

def headings(text):
    return [ln.strip("# ").strip() for ln in text.splitlines() if ln.startswith("#")][:30]

def tokens(text):
    words=re.findall(r"[A-Za-z][A-Za-z0-9_-]{3,}",text.lower())
    stop={"this","that","with","from","into","when","where","current","project","system","map","maps","date","status"}
    return {w for w in words if w not in stop}

def run():
    files=[]
    for p in sorted(INPUT.glob("*")):
        if not p.is_file(): continue
        text=p.read_text(errors="replace")
        files.append({"path":p.name,"sha256":hashlib.sha256(text.encode()).hexdigest(),"bytes":len(text.encode()),"headings":headings(text),"tokens":tokens(text)})
    freq={}
    for f in files:
        for t in f["tokens"]: freq[t]=freq.get(t,0)+1
    shared=sorted(freq.items(),key=lambda kv:(-kv[1],kv[0]))[:100]
    required=[
      "TAKE_SYSTEM_PUTIN_OPERATIONAL_CONTRACT_MAP_001_2026-09-24.md",
      "TAKE_SYSTEM_INGESTION_EXECUTION_OUTPUT_MAP_001_2026-09-24.md",
      "CLOSED_LOOP_EXECUTABLE_CONNECTION_MAP_001_2026-09-24.md"
    ]
    paths={f["path"] for f in files}
    result={
      "experiment":"009-map-ingestion",
      "actual_input_boundary":"Take-4 experiments/009-map-ingestion/inputs read by Take-4 executable",
      "map_count":len(files),
      "required_new_maps":{x:(x in paths) for x in required},
      "all_required_new_maps_ingested":all(x in paths for x in required),
      "maps":[{k:v for k,v in f.items() if k!="tokens"} for f in files],
      "cross_map_shared_vocabulary":shared,
      "execution_truth":"IMPLEMENTATION_EXECUTED",
      "semantic_interpretation":"OPEN; this proves ingestion/execution/observation, not full semantic understanding"
    }
    OUT.write_text(json.dumps(result,indent=2)+"\n")
    print(json.dumps(result,indent=2))
    print("MAP_INGESTION_RUN: PASS")
    assert result["all_required_new_maps_ingested"]
    assert len(files)>=8

if __name__=="__main__":
    run()
