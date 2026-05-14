import argparse
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
DEFAULT_INPUT = ROOT / "benchmark" / "dataset" / "core.json"
DEFAULT_OUTPUT = ROOT / "huggingface" / "control-sci-corpus"


def load_json(path):
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def write_jsonl(questions, output_path):
    with output_path.open("w", encoding="utf-8", newline="\n") as f:
        for question in questions:
            f.write(json.dumps(question, ensure_ascii=False) + "\n")


def write_dataset_info(data, output_dir):
    info = {
        "dataset_name": "control-sci-corpus",
        "version": data.get("meta", {}).get("version", "1.0"),
        "description": "ControlSci Sci-Align benchmark for control science.",
        "formats": ["jsonl"],
        "features": {
            "id": "string",
            "dimension": "string",
            "difficulty_level": "string",
            "control_category": "list[string]",
            "question": "string",
            "answer": "string",
            "reasoning_steps": "list[string]",
            "source_ref": "string",
            "sensitivity_dimension": "string|null",
            "sibling_id": "string|null",
            "rubric": "object|null",
            "consistency_status": "string"
        },
        "splits": {"core": len(data.get("questions", []))}
    }
    (output_dir / "dataset_info.json").write_text(json.dumps(info, ensure_ascii=False, indent=2), encoding="utf-8")


def write_readme(data, output_dir):
    meta = data.get("meta", {})
    text = f"""# ControlSci Sci-Align Benchmark

Control science reasoning benchmark generated from the ControlSci structured corpus.

- Version: {meta.get("version", "1.0")}
- Total questions: {len(data.get("questions", []))}
- Source: {meta.get("source", "")}
- License: CC-BY-4.0

## Files

- `benchmark.jsonl`: one question per line.
- `benchmark.parquet`: optional, written when `pyarrow` is available.
- `dataset_info.json`: lightweight dataset metadata.
"""
    (output_dir / "README.md").write_text(text, encoding="utf-8", newline="\n")


def try_write_parquet(questions, output_path):
    try:
        import pyarrow as pa
        import pyarrow.parquet as pq
    except ImportError:
        return False

    try:
        rows = []
        for question in questions:
            row = dict(question)
            for field in ("control_category", "reasoning_steps"):
                val = row.get(field)
                row[field] = json.dumps(val, ensure_ascii=False) if val else "[]"
            rubric = row.get("rubric")
            row["rubric"] = json.dumps(rubric, ensure_ascii=False) if rubric else "null"
            json.dumps(row, ensure_ascii=False, allow_nan=False)
            rows.append(row)
        table = pa.Table.from_pylist(rows)
        pq.write_table(table, output_path)
        return True
    except (TypeError, ValueError, pa.ArrowException) as e:
        print(f"Warning: Parquet write failed ({e}), falling back to JSONL-only.", flush=True)
        return False


def export_dataset(input_path, output_dir):
    data = load_json(input_path)
    questions = data.get("questions", [])
    output_dir.mkdir(parents=True, exist_ok=True)
    write_jsonl(questions, output_dir / "benchmark.jsonl")
    parquet_written = try_write_parquet(questions, output_dir / "benchmark.parquet")
    write_dataset_info(data, output_dir)
    info_path = output_dir / "dataset_info.json"
    info = load_json(info_path)
    if parquet_written:
        info["formats"].append("parquet")
    else:
        info["parquet_note"] = "pyarrow is not installed; JSONL export was produced as the zero-dependency fallback."
    info_path.write_text(json.dumps(info, ensure_ascii=False, indent=2), encoding="utf-8")
    write_readme(data, output_dir)
    return len(questions), parquet_written


def main():
    parser = argparse.ArgumentParser(description="Export ControlSci benchmark to a HuggingFace-friendly directory.")
    parser.add_argument("--input", "-i", default=str(DEFAULT_INPUT), help="Benchmark JSON path.")
    parser.add_argument("--output", "-o", default=str(DEFAULT_OUTPUT), help="Output dataset directory.")
    parser.add_argument("--push-to-hub", default=None, help="HF dataset repo name (e.g. 'username/control-sci-benchmark'). Uploads output dir.")
    parser.add_argument("--hf-token", default=None, help="HF authentication token. Falls back to HF_TOKEN env var.")
    args = parser.parse_args()

    input_path = Path(args.input).resolve()
    output_dir = Path(args.output).resolve()
    if not input_path.exists():
        raise SystemExit(f"Input not found: {input_path}")

    total, parquet_written = export_dataset(input_path, output_dir)
    print(f"Exported {total} question(s) to {output_dir}")
    print(f"Parquet: {'written' if parquet_written else 'skipped (pyarrow not installed)'}")

    if args.push_to_hub:
        try:
            from huggingface_hub import HfApi
        except ImportError:
            print("huggingface_hub not installed. Run: pip install huggingface_hub")
            return
        token = args.hf_token or os.environ.get("HF_TOKEN")
        if not token:
            print("HF token required. Pass --hf-token or set HF_TOKEN env var.")
            return
        api = HfApi()
        api.upload_folder(
            folder_path=str(output_dir),
            repo_id=args.push_to_hub,
            token=token,
            repo_type="dataset",
            ignore_patterns=[".gitkeep"],
        )
        print(f"Uploaded to https://huggingface.co/datasets/{args.push_to_hub}")


if __name__ == "__main__":
    main()
