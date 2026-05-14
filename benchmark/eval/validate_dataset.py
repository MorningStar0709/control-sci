import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
DEFAULT_INPUT = ROOT / "benchmark" / "dataset" / "core.json"

ID_RE = re.compile(r"^CS-EVO-\d{5}$")

REQUIRED_META = ["project", "version", "updated", "total_questions", "dimensions"]
REQUIRED_Q = [
    "id", "dimension", "difficulty_level", "control_category",
    "question", "answer", "reasoning_steps", "source_ref",
    "consistency_status",
]
RUBRIC_KEYS = {"feasibility", "method_choice", "completeness", "innovation", "clarity"}
RUBRIC_SUB_KEYS = {"max_score", "weight", "description"}
ALLOWED_DIMENSIONS = {"A", "B", "C", "D"}
ALLOWED_DIFFICULTIES = {"L1", "L2", "L3", "L4"}
ALLOWED_CATEGORIES = {
    "classical", "modern", "nonlinear", "robust", "optimal",
    "adaptive", "digital", "intelligent", "mpc", "multi_agent",
}
ALLOWED_STATUS = {"auto_passed", "needs_review", "reviewed_kept", "reviewed_discarded"}
ALLOWED_SENSITIVITY = {"parameter", "environment", "constraint"}
EXPECTED_COUNT = 500
EXPECTED_PER_DIM = 125


def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def validate_meta(meta):
    errors = []
    for key in REQUIRED_META:
        if key not in meta:
            errors.append(f"meta.{key} missing")
    if not errors:
        tc = meta.get("total_questions")
        if not isinstance(tc, int):
            errors.append(f"meta.total_questions not int ({type(tc).__name__})")
        elif tc != EXPECTED_COUNT:
            errors.append(f"meta.total_questions={tc} != {EXPECTED_COUNT}")
    return errors


def validate_categories(errors, idx, qid, cats):
    if not isinstance(cats, list):
        errors.append(f"{idx} ({qid}): control_category must be array")
        return
    if not 1 <= len(cats) <= 3:
        errors.append(f"{idx} ({qid}): control_category must contain 1-3 items, got {len(cats)}")
    if len(cats) != len(set(cats)):
        errors.append(f"{idx} ({qid}): control_category has duplicates")
    for cat in cats:
        if cat not in ALLOWED_CATEGORIES:
            errors.append(f"{idx} ({qid}): control_category unknown: {cat}")


def validate_rubric(errors, idx, qid, rubric):
    if not isinstance(rubric, dict):
        errors.append(f"{idx} ({qid}): D-dim rubric must be object")
        return
    missing = RUBRIC_KEYS - set(rubric)
    if missing:
        errors.append(f"{idx} ({qid}): rubric missing top-level keys: {sorted(missing)}")
    for rk in RUBRIC_KEYS & set(rubric):
        item = rubric[rk]
        if not isinstance(item, dict):
            errors.append(f"{idx} ({qid}): rubric.{rk} not object")
            continue
        sub_missing = RUBRIC_SUB_KEYS - set(item)
        if sub_missing:
            errors.append(f"{idx} ({qid}): rubric.{rk} missing {sorted(sub_missing)}")
        for sk in RUBRIC_SUB_KEYS & set(item):
            val = item[sk]
            if sk in ("max_score", "weight") and not isinstance(val, (int, float)):
                errors.append(f"{idx} ({qid}): rubric.{rk}.{sk}={val} not numeric")
            elif sk == "description" and not isinstance(val, str):
                errors.append(f"{idx} ({qid}): rubric.{rk}.{sk} not string")


def validate_question(q, i, ids, dim_counts, difficulty_counts, status_counts, cat_counter):
    errors = []
    idx = f"questions[{i}]"
    if not isinstance(q, dict):
        errors.append(f"{idx} not JSON object")
        return errors

    qid = q.get("id", "<MISSING>")
    ids.append(qid)

    for key in REQUIRED_Q:
        if key not in q:
            errors.append(f"{idx} ({qid}): missing field {key}")

    if qid and not ID_RE.fullmatch(qid):
        errors.append(f"{idx}: id={qid} does not match CS-EVO-NNNNN")

    dim = q.get("dimension")
    if dim not in ALLOWED_DIMENSIONS:
        errors.append(f"{idx} ({qid}): dimension={dim} illegal")
    else:
        dim_counts[dim] += 1

    diff = q.get("difficulty_level")
    if diff not in ALLOWED_DIFFICULTIES:
        errors.append(f"{idx} ({qid}): difficulty_level={diff} illegal")
    else:
        difficulty_counts[diff] += 1

    status = q.get("consistency_status")
    if status not in ALLOWED_STATUS:
        errors.append(f"{idx} ({qid}): consistency_status={status} illegal")
    else:
        status_counts[status] += 1

    cats = q.get("control_category", [])
    validate_categories(errors, idx, qid, cats)
    if isinstance(cats, list):
        cat_counter.update(cats)

    if dim == "D":
        validate_rubric(errors, idx, qid, q.get("rubric"))
    elif q.get("rubric") not in (None, {}):
        errors.append(f"{idx} ({qid}): rubric set on non-D dimension")

    if dim == "C":
        sd = q.get("sensitivity_dimension")
        if sd not in ALLOWED_SENSITIVITY:
            errors.append(f"{idx} ({qid}): C-dim sensitivity_dimension={sd} illegal")
        sid = q.get("sibling_id")
        if not isinstance(sid, str) or not ID_RE.fullmatch(sid):
            errors.append(f"{idx} ({qid}): C-dim missing valid sibling_id")

    return errors


def validate_cross_references(questions, errors):
    by_id = {}
    for q in questions:
        if isinstance(q, dict) and isinstance(q.get("id"), str):
            by_id[q["id"]] = q

    for q in questions:
        if not isinstance(q, dict) or q.get("dimension") != "C":
            continue
        qid = q.get("id")
        sibling_id = q.get("sibling_id")
        sibling = by_id.get(sibling_id)
        if not sibling:
            errors.append(f"{qid}: sibling_id={sibling_id} points to missing question")
            continue
        if sibling.get("sibling_id") != qid:
            errors.append(f"{qid}: sibling_id not bidirectional (other={sibling.get('sibling_id')})")
        if sibling.get("dimension") != "C":
            errors.append(f"{qid}: sibling_id={sibling_id} is not C-dimension")


def main():
    parser = argparse.ArgumentParser(description="Validate ControlSci core.json dataset integrity.")
    parser.add_argument("--input", "-i", default=str(DEFAULT_INPUT),
                        help=f"Path to core.json (default: {DEFAULT_INPUT})")
    args = parser.parse_args()

    input_path = Path(args.input).resolve()
    if not input_path.exists():
        print(f"ERROR: file not found: {input_path}")
        sys.exit(1)

    print(f"Loading: {input_path}")
    data = load_json(input_path)

    all_ok = True

    meta = data.get("meta", {})
    meta_errors = validate_meta(meta)
    if meta_errors:
        for e in meta_errors:
            print(f"  ERR meta: {e}")
        all_ok = False
    else:
        print(f"  OK meta complete")

    questions = data.get("questions", [])
    if not isinstance(questions, list):
        print(f"  ERR questions not array")
        sys.exit(1)

    print(f"  Checking {len(questions)} questions ...")
    ids = []
    dim_counts = Counter()
    difficulty_counts = Counter()
    status_counts = Counter()
    cat_counter = Counter()
    all_q_errors = []

    for i, q in enumerate(questions):
        q_errs = validate_question(q, i, ids, dim_counts, difficulty_counts, status_counts, cat_counter)
        all_q_errors.extend(q_errs)

    xref_warnings = []
    validate_cross_references(questions, xref_warnings)

    if all_q_errors:
        for e in all_q_errors:
            print(f"  ERR {e}")
        all_ok = False

    if xref_warnings:
        for w in xref_warnings:
            print(f"  WARN {w}")
        print(f"  INFO {len(xref_warnings)} C-dim sibling refs missing (expected: siblings span core+full)")

    dupes = [qid for qid, cnt in Counter(ids).items() if cnt > 1]

    dim_parts = []
    dim_ok = True
    for d in ("A", "B", "C", "D"):
        cnt = dim_counts.get(d, 0)
        dim_parts.append(f"{d}={cnt}")
        if cnt != EXPECTED_PER_DIM:
            dim_ok = False
    dim_str = " ".join(dim_parts)

    if dim_ok:
        print(f"  OK dimensions: {dim_str}")
    else:
        print(f"  ERR dimensions unbalanced: {dim_str} (expected A=B=C=D=125)")
        all_ok = False

    print(f"  STAT difficulty: {' '.join(f'{k}={v}' for k, v in sorted(difficulty_counts.items()))}")
    print(f"  STAT consistency: {' '.join(f'{k}={v}' for k, v in sorted(status_counts.items()))}")
    cat_str = " ".join(f"{k}={v}" for k, v in cat_counter.most_common())
    print(f"  STAT categories: {cat_str}")

    d_total = dim_counts.get("D", 0)
    d_rubric = sum(1 for q in questions if isinstance(q, dict) and q.get("dimension") == "D" and isinstance(q.get("rubric"), dict))
    if d_total > 0:
        if d_rubric == d_total:
            print(f"  OK rubric: {d_rubric}/{d_total} (100%)")
        else:
            print(f"  ERR rubric: {d_rubric}/{d_total}")
            all_ok = False

    if dupes:
        print(f"  ERR duplicate IDs: {dupes}")
        all_ok = False
    else:
        print(f"  OK 0 duplicate IDs")

    print()
    total = len(questions)
    summary = f"core.json: {total} questions ({dim_str}) | rubric={d_rubric}/{d_total} | dupes=0"
    print(summary)

    if not all_ok:
        sys.exit(1)


if __name__ == "__main__":
    main()
