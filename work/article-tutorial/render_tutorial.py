import copy
import json
import shutil
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent
BASE = "http://127.0.0.1:8188"


def request(path, payload=None):
    data = None if payload is None else json.dumps(payload, ensure_ascii=False).encode("utf-8")
    req = urllib.request.Request(BASE + path, data=data, headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=90) as response:
        return json.load(response)


def run(job):
    evidence = ROOT / "evidence" / (job["id"] + ".json")
    if evidence.exists() and json.loads(evidence.read_text(encoding="utf-8")).get("completed"):
        print("EXISTS " + job["id"], flush=True)
        return
    while True:
        queue = request("/queue")
        if not queue["queue_running"] and not queue["queue_pending"]:
            break
        time.sleep(15)
    graph = json.loads((ROOT / "evidence/workflow-api.json").read_text(encoding="utf-8"))
    graph["7"]["inputs"]["prompt"] = job["prompt"]
    graph["9"]["inputs"]["seed"] = job.get("seed", 2026092807)
    graph["17"]["inputs"]["aspect_ratio"] = job.get("aspect_ratio", "3:4 (Portrait Standard)")
    graph["17"]["inputs"]["megapixels"] = job.get("megapixels", 1.0)
    graph["16"]["inputs"]["filename_prefix"] = "portrait_tutorial_20260928/" + job["id"]
    result = request("/prompt", {"prompt": graph, "client_id": "portrait-tutorial-primary", "extra_data": {"tutorial_job": job["id"]}})
    pid = result["prompt_id"]
    record = {"job": job, "prompt_id": pid, "graph": graph, "submitted_at": time.time(), "completed": False}
    evidence.write_text(json.dumps(record, ensure_ascii=False, indent=2), encoding="utf-8")
    print("QUEUED " + job["id"] + " " + pid, flush=True)
    started = time.time()
    while time.time() - started < 1800:
        history = request("/history/" + pid)
        if pid in history:
            item = history[pid]
            record["history"] = item
            if item.get("status", {}).get("status_str") == "error":
                evidence.write_text(json.dumps(record, ensure_ascii=False, indent=2), encoding="utf-8")
                raise RuntimeError("Generation failed: " + job["id"])
            outputs = item.get("outputs", {}).get("16", {}).get("images", [])
            if outputs:
                source = Path("I:/ComfyUI-aki-v3.2/ComfyUI/output") / outputs[0].get("subfolder", "") / outputs[0]["filename"]
                target = ROOT / "images" / (job["id"] + ".png")
                shutil.copy2(source, target)
                record.update(completed=True, source=str(source), image=str(target), elapsed_seconds=round(time.time()-started, 2))
                evidence.write_text(json.dumps(record, ensure_ascii=False, indent=2), encoding="utf-8")
                print("DONE " + job["id"] + " " + str(record["elapsed_seconds"]) + "s", flush=True)
                return
        time.sleep(5)
    raise TimeoutError("Generation still unresolved: " + pid)


jobs = json.loads((ROOT / "jobs.json").read_text(encoding="utf-8"))
selected = set(sys.argv[1:])
for job in jobs:
    if not selected or job["id"] in selected:
        run(job)
