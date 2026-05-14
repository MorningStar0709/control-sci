"""Deprecated compatibility entrypoint for the ControlSci Agent.

Use benchmark/agent/agent_cli.py for the maintained 14-intent router.
This wrapper intentionally avoids the legacy implementation so old calls do
not bypass current privacy, logging, and scheduler policies.
"""

import runpy
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
AGENT_CLI = ROOT / "benchmark" / "agent" / "agent_cli.py"


def main():
    print(
        "[DEPRECATED] benchmark/agent/agent.py is a compatibility wrapper. "
        "Forwarding to benchmark/agent/agent_cli.py.",
        file=sys.stderr,
    )
    sys.argv[0] = str(AGENT_CLI)
    runpy.run_path(str(AGENT_CLI), run_name="__main__")


if __name__ == "__main__":
    main()
