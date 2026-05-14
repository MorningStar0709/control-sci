"""Task 1: 语料处理与题目生成 — 演示 plan + 前两步（dry_run mock 日志）"""
import random
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from benchmark.agent.agent import ControlSciAgent
from benchmark.agent.log_schema import LogStep, ExecutionLog

LOGS_DIR = Path(__file__).resolve().parent / "logs"
LOGS_DIR.mkdir(parents=True, exist_ok=True)


def main():
    agent = ControlSciAgent(task_id="controlsci-corpus-001", task_name="语料处理与题目生成")

    print("=" * 60)
    print("ControlSci Agent — Task 1: 语料处理与题目生成")
    print("=" * 60)

    plan = agent.plan_task()
    print(f"\n任务规划（共 {len(plan)} 步）:")
    for p in plan:
        print(f"  Step {p['step']}: {p['name']} ({p['tool']}) — {p['description']}")

    t0 = time.time()

    print("\n--- Step 1: 文献解析（dry_run）---")
    agent._run_step(
        step_id=1, step_name="文献解析", tool="MinerU",
        cmd_args=[sys.executable, "magic_pdf", "--input", ".", "--output", "corpus"],
        cwd=str(ROOT), dry_run=True,
    )

    time.sleep(random.uniform(0.1, 0.3))

    print("\n--- Step 2: 题目生成（dry_run）---")
    agent._run_step(
        step_id=2, step_name="题目生成", tool="build_benchmark.py",
        cmd_args=[
            sys.executable, "benchmark/pipeline/build_benchmark.py",
            "--corpus", str(ROOT / "corpus"),
            "--provider", "deepseek",
        ],
        cwd=str(ROOT), dry_run=True,
    )

    agent.log.final_status = "completed"
    agent.log.total_duration_ms = int((time.time() - t0) * 1000)

    log_path = LOGS_DIR / "task_1_corpus.json"
    agent.log.save(str(log_path))

    print(f"\n日志已保存: {log_path}")
    print(f"总步骤数: {len(agent.log.steps)}, 最终状态: {agent.log.final_status}")


if __name__ == "__main__":
    main()
