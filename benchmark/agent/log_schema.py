"""Structured execution log schema for ControlSci Agent."""
import json
from dataclasses import dataclass, field, asdict
from datetime import datetime
from pathlib import Path
from typing import List, Literal, Optional


StepStatus = Literal["success", "failed", "skipped", "timeout"]
FinalStatus = Literal["running", "completed", "partial", "failed"]


@dataclass
class LogStep:
    schema_version: str = "1.0"
    step_id: int = 0
    step_name: str = ""
    tool: str = ""
    input_summary: str = ""
    output_summary: str = ""
    status: StepStatus = "success"
    duration_ms: int = 0
    timestamp: str = field(default_factory=lambda: datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    error: Optional[str] = None


@dataclass
class ExecutionLog:
    schema_version: str = "1.0"
    task_id: str = ""
    task_name: str = ""
    steps: List[LogStep] = field(default_factory=list)
    total_duration_ms: int = 0
    final_status: FinalStatus = "running"
    created_at: str = field(default_factory=lambda: datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    def add_step(self, step: LogStep):
        self.steps.append(step)

    def to_dict(self):
        return asdict(self)

    def save(self, path: str):
        p = Path(path)
        p.parent.mkdir(parents=True, exist_ok=True)
        content = json.dumps(self.to_dict(), ensure_ascii=False, indent=2)
        tmp = p.with_suffix(p.suffix + ".tmp")
        tmp.write_text(content, encoding="utf-8")
        tmp.replace(p)


def load_log(path: str) -> ExecutionLog:
    raw = json.loads(Path(path).read_text(encoding="utf-8"))
    steps = [LogStep(**s) for s in raw.get("steps", [])]
    log = ExecutionLog(
        schema_version=raw.get("schema_version", "1.0"),
        task_id=raw["task_id"],
        task_name=raw["task_name"],
        steps=steps,
        total_duration_ms=raw.get("total_duration_ms", 0),
        final_status=raw.get("final_status", "running"),
        created_at=raw.get("created_at", ""),
    )
    return log
