from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]  # project root
CORE_PATH = ROOT / "benchmark" / "dataset" / "core.json"
FULL_PATH = ROOT / "benchmark" / "dataset" / "full.json"
OUTPUT_DIR = ROOT / "analyze" / "outputs"
CHART_DIR = OUTPUT_DIR / "charts"
