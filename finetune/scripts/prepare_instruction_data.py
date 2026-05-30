import argparse
import json
import os
import random
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DEFAULT_INPUT = ROOT / "benchmark" / "dataset" / "full.json"
DEFAULT_OUTPUT_DIR = ROOT / "finetune" / "data"
DEFAULT_SEED = 42

SYSTEM_PROMPT = "你是控制科学专家。请回答以下科学演化推理题目。"


def format_as_instruction(question, include_reasoning=False):
    qid = question.get("id", "?")

    try:
        assistant_content = question["answer"]
    except KeyError:
        raise ValueError(f"题目 {qid} 缺少 'answer' 字段，无法生成 instruction")

    if include_reasoning and question.get("reasoning_steps"):
        steps = "\n".join(f"{i+1}. {s}" for i, s in enumerate(question["reasoning_steps"]))
        assistant_content = f"{steps}\n\n答案: {assistant_content}"

    dim = question.get("dimension", "unknown")
    q_text = question.get("question", "")
    if not q_text:
        raise ValueError(f"题目 {qid} 缺少 'question' 字段，无法生成 instruction")

    return {
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": f"[维度: {dim}] {q_text}"},
            {"role": "assistant", "content": assistant_content}
        ]
    }


def stratified_split(questions, train_ratio=0.8, val_ratio=0.1, test_ratio=0.1):
    by_dim = {}
    for q in questions:
        dim = q.get("dimension", "unknown")
        by_dim.setdefault(dim, []).append(q)

    train, val, test = [], [], []
    small_dims = []

    for dim, items in sorted(by_dim.items()):
        random.shuffle(items)
        n = len(items)

        n_train = round(n * train_ratio)
        n_val = round(n * val_ratio)

        if n_train + n_val > n:
            n_val = max(0, n - n_train)
        if n_train + n_val > n:
            n_train = n
            n_val = 0

        if n < 10:
            small_dims.append((dim, n, n_train, n_val, n - n_train - n_val))

        train.extend(items[:n_train])
        val.extend(items[n_train:n_train + n_val])
        test.extend(items[n_train + n_val:])

    if small_dims:
        print("[WARNING] 小维度组 (<10 条) 实际分配：")
        for dim, n, nt, nv, nte in small_dims:
            print(f"  {dim}: total={n}, train={nt}, val={nv}, test={nte}")

    random.shuffle(train)
    random.shuffle(val)
    random.shuffle(test)
    return train, val, test


def _write_atomic(dir_path, name, subset, include_reasoning):
    path = Path(dir_path) / f"{name}.jsonl"
    fd, tmp_path = tempfile.mkstemp(suffix=".jsonl", prefix=f"{name}_", dir=str(dir_path))
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            for q in subset:
                f.write(json.dumps(format_as_instruction(q, include_reasoning), ensure_ascii=False) + "\n")
        os.replace(tmp_path, str(path))
        print(f"[OK] {name}.jsonl: {len(subset)} 条", flush=True)
    except Exception:
        try:
            os.unlink(tmp_path)
        except OSError:
            pass
        raise


def _validate_ratios(train_ratio, val_ratio, test_ratio):
    ratio_sum = train_ratio + val_ratio + test_ratio
    if not (0.999 <= ratio_sum <= 1.001):
        return f"ratio 之和必须为 1.0，当前为 {ratio_sum:.3f}"
    for label, val in [("train", train_ratio), ("val", val_ratio), ("test", test_ratio)]:
        if not (0.0 < val < 1.0):
            return f"{label}-ratio 必须在 (0, 1) 之间，当前为 {val}"
    return None


def main():
    parser = argparse.ArgumentParser(description="将评测数据转换为 QLoRA 训练格式 (ChatML)")
    parser.add_argument("--input", type=str, default=str(DEFAULT_INPUT), help="full.json 路径")
    parser.add_argument("--output-dir", type=str, default=str(DEFAULT_OUTPUT_DIR), help="输出目录")
    parser.add_argument("--train-ratio", type=float, default=0.8)
    parser.add_argument("--val-ratio", type=float, default=0.1)
    parser.add_argument("--test-ratio", type=float, default=0.1)
    parser.add_argument("--seed", type=int, default=DEFAULT_SEED)
    parser.add_argument("--include-reasoning", action="store_true", help="将 reasoning_steps 加入 assistant 输出")
    args = parser.parse_args()

    err = _validate_ratios(args.train_ratio, args.val_ratio, args.test_ratio)
    if err:
        sys.exit(f"[ERROR] 比例校验失败: {err}")

    input_path = Path(args.input)
    if not input_path.exists():
        sys.exit(f"[ERROR] 输入文件不存在: {input_path}")

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    with open(input_path, encoding="utf-8") as f:
        data = json.load(f)

    questions = data["questions"]
    meta = data.get("meta", {})

    declared_total = meta.get("total_questions", 0)
    actual_total = len(questions)
    if declared_total and declared_total != actual_total:
        print(f"[WARNING] meta.total_questions={declared_total} ≠ 实际加载 {actual_total} 题，以实际为准")
    total = actual_total

    print(f"[源文件] {input_path.name}  (v{meta.get('version','?')}, {total} 题)")
    print(f"[配置  ] seed={args.seed}, train={args.train_ratio}, val={args.val_ratio}, test={args.test_ratio}, "
          f"推理链={'ON' if args.include_reasoning else 'OFF'}")
    print()

    random.seed(args.seed)
    train, val, test = stratified_split(questions, args.train_ratio, args.val_ratio, args.test_ratio)

    splits = {"train": train, "val": val, "test": test}

    for name, subset in splits.items():
        _write_atomic(output_dir, name, subset, args.include_reasoning)

    print(f"\n总计: {sum(len(s) for s in splits.values())} 条 (来源: {total} 题)")
    print(f"比例: {len(train)/total:.1%} / {len(val)/total:.1%} / {len(test)/total:.1%}")

    for name, subset in splits.items():
        dist = {}
        for q in subset:
            dim = q.get("dimension", "?")
            dist[dim] = dist.get(dim, 0) + 1
        print(f"  {name} 分布: {dict(sorted(dist.items()))}")


if __name__ == "__main__":
    main()
