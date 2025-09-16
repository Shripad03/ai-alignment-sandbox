# agent/interceptor.py
import json, os, uuid, time
from datetime import datetime, timezone

class RunLogger:
    def __init__(self, runs_dir="runs", run_id=None):
        os.makedirs(runs_dir, exist_ok=True)
        self.run_id = run_id or str(uuid.uuid4())
        self.path = os.path.join(runs_dir, f"{self.run_id}.jsonl")
        self.step = 0

    def log(self, thought, action, observation, goal, meta=None):
        self.step += 1
        evt = {
            "run_id": self.run_id,
            "step": self.step,
            "ts": datetime.now(timezone.utc).isoformat(),
            "trace": {
                "goal": goal,
                "thought": thought,
                "action": action,        # {"tool": "...", "args": {...}}
                "observation": observation,
                "result_summary": (observation[:140] + "…") if observation and len(observation) > 140 else observation
            },
            "meta": meta or {}
        }
        with open(self.path, "a", encoding="utf-8") as f:
            f.write(json.dumps(evt, ensure_ascii=False) + "\n")
        return evt
