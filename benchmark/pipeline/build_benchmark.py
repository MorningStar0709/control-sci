"""Build ControlSci Sci-Align benchmark questions from corpus chunks.

Responsibilities:
  - CLI parsing & orchestration (main)
  - Corpus loading / chunk selection
  - Mock question generation
  - Question generation loop (API mode) with quality monitoring + periodic reset
  - Checkpoint / output persistence
"""
import argparse
import json
import os
import random
import sys
import time
from datetime import date
from pathlib import Path

_project_root = str(Path(__file__).resolve().parents[2])
if _project_root not in sys.path:
    sys.path.insert(0, _project_root)

from benchmark.pipeline.arbiter import arbitrate_questions
from benchmark.generator.api import (
    PROVIDER_CONFIG, PROVIDER_ENV_MAP,
    call_llm, validate_api_question,
)
from benchmark.generator.distribution import (
    CATEGORY_MAP, DIMENSION_CYCLE, DIFFICULTY_BY_DIMENSION,
    DIM_TARGET, DIFFICULTY_TARGET, normalize_categories, pick_next_dim_and_diff,
)
from benchmark.generator.prompts import build_system_prompt, build_user_prompt
from benchmark.generator.quality import QualityMonitor


ROOT = Path(__file__).resolve().parents[2]
DEFAULT_CORPUS = ROOT / "corpus"
DEFAULT_OUTPUT = ROOT / "benchmark" / "dataset" / "benchmark.json"
DEFAULT_REVIEW = ROOT / "benchmark" / "dataset" / "manual_review.json"
DEFAULT_SEED = 42
RUN_SEED = DEFAULT_SEED


def first_env(env_spec: str) -> str:
    for env_name in env_spec.split("|"):
        value = os.environ.get(env_name.strip(), "")
        if value:
            return value
    return ""


def load_json(path):
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def write_json_atomic(path, data):
    tmp_path = path.with_suffix(path.suffix + ".tmp")
    tmp_path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    tmp_path.replace(path)


def load_corpus(corpus_dir):
    metadata_path = corpus_dir / "metadata.json"
    manifest_path = corpus_dir / "chunks" / "chunks_manifest.json"
    if not metadata_path.exists():
        raise SystemExit(f"Missing corpus metadata: {metadata_path}")
    if not manifest_path.exists():
        raise SystemExit(f"Missing chunks manifest: {manifest_path}")
    metadata = load_json(metadata_path)
    manifest = load_json(manifest_path)
    docs = {doc["id"]: doc for doc in metadata.get("docs", [])}
    chunks = manifest.get("chunks", [])
    return docs, chunks


def read_chunk_text(corpus_dir, chunk):
    filepath = Path(chunk["filepath"])
    path = filepath if filepath.is_absolute() else ROOT / filepath
    if not path.exists():
        path = corpus_dir / filepath.name
    if not path.exists():
        return ""
    text = path.read_text(encoding="utf-8", errors="ignore").strip()
    return text[:2400]


def select_chunks(corpus_dir, docs, chunks, category=None, min_tokens=80, seed=DEFAULT_SEED):
    selected = []
    for chunk in chunks:
        if chunk.get("estimated_tokens", 0) < min_tokens:
            continue
        doc = docs.get(chunk.get("doc_id"), {})
        cats = normalize_categories(doc.get("control_category"))
        if category and category not in cats:
            continue
        text = read_chunk_text(corpus_dir, chunk)
        if not text:
            continue
        selected.append({**chunk, "categories": cats, "text": text})
    random.Random(seed).shuffle(selected)
    return selected


def default_rubric(topic):
    return {
        "feasibility": {"max_score": 1, "weight": 0.2, "description": f"{topic}方案是否具有工程可实施性"},
        "method_choice": {"max_score": 1, "weight": 0.2, "description": f"控制方法选择是否适合{topic}问题"},
        "completeness": {"max_score": 1, "weight": 0.2, "description": "是否覆盖建模、设计、分析与验证流程"},
        "innovation": {"max_score": 1, "weight": 0.2, "description": "是否包含有价值的设计改进或工程权衡"},
        "clarity": {"max_score": 1, "weight": 0.2, "description": "数学表达和文字说明是否清晰准确"},
    }


def save_checkpoint(output_path, review_path, questions, review_items, index, chunk_index, group_index, provider, model, source, start_time, limit=0, consecutive_failures=0, token_usage=None, quality_summary=None, questions_since_reset=0):
    cp_out = output_path.with_suffix(".checkpoint.json")
    cp_rev = review_path.with_suffix(".checkpoint.json")
    data = {
        "meta": build_meta(questions, source),
        "state": {
            "next_index": index,
            "chunk_index": chunk_index,
            "provider": provider,
            "model": model,
            "seed": RUN_SEED,
            "consecutive_failures": consecutive_failures,
            "questions_since_reset": questions_since_reset,
        },
        "questions": questions,
    }
    write_json_atomic(cp_out, data)
    review = {"total": len(review_items), "items": review_items}
    write_json_atomic(cp_rev, review)
    elapsed = time.time() - start_time
    rate = len(questions) / elapsed * 60 if elapsed > 0 else 0
    remaining = max(limit - len(questions), 0)
    eta_min = remaining / rate if rate > 0 else 0

    status = {
        "progress": f"{len(questions)}/{limit}",
        "percent": round(len(questions) / max(limit, 1) * 100, 1),
        "rate": round(rate, 1),
        "eta_min": round(eta_min, 0),
        "dimensions": build_meta(questions, source)["dimensions"],
        "consecutive_failures": consecutive_failures,
        "questions_since_reset": questions_since_reset,
        "last_question_time": time.strftime("%H:%M:%S"),
        "provider": provider,
        "seed": RUN_SEED,
        "status": "running",
    }
    if token_usage:
        status["token_usage"] = {"prompt": token_usage[0], "completion": token_usage[1]}
    if quality_summary:
        status["quality"] = quality_summary
    status_path = output_path.parent / "generation_status.json"
    write_json_atomic(status_path, status)
    return rate, eta_min


def _write_light_status(status_path, questions, limit, consecutive_failures, token_usage, start_time, provider, quality_summary=None, questions_since_reset=0):
    elapsed = time.time() - start_time
    total_q = len(questions)
    rate = total_q / elapsed * 60 if elapsed > 0 else 0
    eta_min = (max(limit - total_q, 0)) / rate if rate > 0 else 0
    dim_counts = {"A": 0, "B": 0, "C": 0, "D": 0}
    for q in questions:
        d = q.get("dimension", "")
        dim_counts[d] = dim_counts.get(d, 0) + 1
    s = {
        "progress": f"{total_q}/{limit}",
        "percent": round(total_q / max(limit, 1) * 100, 1),
        "rate": round(rate, 1),
        "eta_min": round(eta_min, 0),
        "dimensions": dim_counts,
        "consecutive_failures": consecutive_failures,
        "questions_since_reset": questions_since_reset,
        "token_usage": {"prompt": token_usage[0], "completion": token_usage[1]},
        "last_question_time": time.strftime("%H:%M:%S"),
        "provider": provider,
        "seed": RUN_SEED,
        "status": "running",
    }
    if quality_summary:
        s["quality"] = quality_summary
    write_json_atomic(status_path, s)


def make_question_from_llm(llm_output, qid, chunk, dimension, difficulty, provider="unknown"):
    section = chunk.get("source_section") or chunk.get("chunk_id", "")
    raw_cats = llm_output.get("control_category", [])
    valid = {"classical", "modern", "nonlinear", "robust", "optimal",
             "adaptive", "digital", "intelligent", "mpc", "multi_agent"}
    categories = [c for c in raw_cats if c in valid][:3] or ["classical"]

    question = {
        "id": qid,
        "dimension": dimension,
        "difficulty_level": difficulty,
        "control_category": categories,
        "question": llm_output.get("question", ""),
        "answer": llm_output.get("answer", ""),
        "reasoning_steps": llm_output.get("reasoning_steps", []),
        "source_ref": chunk.get("chunk_id", section),
        "model_source": provider,
        "sensitivity_dimension": None,
        "sibling_id": None,
        "rubric": None,
        "consistency_status": "auto_passed",
    }

    if dimension == "C":
        question["sensitivity_dimension"] = llm_output.get("sensitivity_dimension", "parameter")

    if dimension == "D":
        question["rubric"] = llm_output.get("rubric") or default_rubric(section)

    return question


def _make_diag_ctx(q_index, provider, round_label):
    return {"q_index": q_index, "provider": provider, "round": round_label}


def _record_quality(quality, llm_output):
    """Record one LLM response and return whether it passed validation."""
    ok = llm_output is not None and validate_api_question(llm_output)
    quality.check({
        "parse_success": llm_output is not None,
        "validation_passed": ok,
        "content_length": len(str(llm_output)) if llm_output else 0,
    })
    return ok


def generate_api_questions(chunks, limit, api_key, model, corpus_dir, provider="deepseek",
                            start_index=1, start_chunk=0, resume_questions=None, output_path=None, review_path=None,
                            reset_every=15, diag_path=None):
    import logging
    if output_path:
        log_path = output_path.with_suffix(".log")
    else:
        log_path = ROOT / "benchmark" / "generation.log"
    logging.basicConfig(filename=str(log_path), level=logging.INFO,
                        format="%(asctime)s [%(levelname)s] %(message)s", encoding="utf-8")
    logger = logging.getLogger(__name__)

    print(f"[API] Starting: limit={limit}, chunks={len(chunks)}, provider={provider}, reset_every={reset_every}", flush=True)
    logger.info(f"Start: limit={limit}, chunks={len(chunks)}, provider={provider}, reset_every={reset_every}")

    quality = QualityMonitor(window_size=15, consecutive_threshold=3)
    questions = list(resume_questions) if resume_questions else []
    review_items = []
    index = start_index
    chunk_index = start_chunk
    consecutive_failures = 0
    questions_since_reset = 0
    start_time = time.time()
    current_provider = provider
    active_api_key = api_key
    active_model = model
    token_usage = [0, 0]

    system_prompt = build_system_prompt()

    while len(questions) < limit and chunk_index < len(chunks):
        failure_threshold = min(max(20, limit // 5), len(chunks))
        if consecutive_failures >= failure_threshold:
            print(f"[API] Too many failures ({consecutive_failures}), stopping.", flush=True)
            logger.warning(f"Stopped early after {consecutive_failures} failures")
            break

        dim, difficulty = pick_next_dim_and_diff(questions, limit)
        chunk = chunks[chunk_index]
        chunk_text = chunk.get("text", "")
        if not chunk_text:
            chunk_index += 1
            consecutive_failures += 1
            continue

        user_prompt = build_user_prompt(chunk_text, chunk.get("chunk_id", ""), dim, difficulty)

        dim_counts = {}
        for q in questions:
            d = q.get("dimension")
            if not d:
                continue
            dim_counts[d] = dim_counts.get(d, 0) + 1

        print(f"[API] q{index}: dim={dim}, diff={difficulty}, chunk={chunk_index}, reset_ct={questions_since_reset}", flush=True)
        logger.info(f"q{index}: dim={dim}, diff={difficulty}, chunk={chunk_index}, provider={current_provider}")

        diag_ctx_1 = _make_diag_ctx(index, current_provider, 1)
        q1 = call_llm(current_provider, active_api_key, system_prompt, user_prompt, _usage_acc=token_usage, diag_path=diag_path, diag_ctx=diag_ctx_1)
        q1_ok = _record_quality(quality, q1)
        if q1:
            print(f"  [API] Round1 validated OK, q[:50]={q1.get('question','')[:50]}", flush=True)
        else:
            print(f"  [API] Round1 returned None", flush=True)

        if not q1_ok:
            chunk_index += 1
            consecutive_failures += 1
            continue

        diag_ctx_2 = _make_diag_ctx(index, current_provider, 2)
        q2 = call_llm(current_provider, active_api_key, system_prompt, user_prompt, max_retries=2, _usage_acc=token_usage, diag_path=diag_path, diag_ctx=diag_ctx_2)
        q2_ok = _record_quality(quality, q2)

        if dim == "C" and len(questions) + 2 <= limit:
            qid_a = f"CS-EVO-{index:05d}"
            qid_b = f"CS-EVO-{index + 1:05d}"
            c2_prompt = build_user_prompt(
                chunk_text, chunk.get("chunk_id", ""), dim, difficulty,
                override_desc="生成一道与上一题配对的C维度变体题。\n保持相同的基准条件，但改变sensitivity_dimension方向（如果上题是parameter就改为environment，反之亦然）。\n题目必须是单一、聚焦的问题，一次只分析一个不同的变化因素。\n"
            )
            diag_ctx_1b = _make_diag_ctx(index + 1, current_provider, "1b")
            q1b = call_llm(current_provider, active_api_key, system_prompt, c2_prompt, _usage_acc=token_usage, diag_path=diag_path, diag_ctx=diag_ctx_1b)
            q1b_ok = _record_quality(quality, q1b)
            if q1b_ok:
                q1["sibling_id"] = qid_b
                q1b["sibling_id"] = qid_a
                diag_ctx_2b = _make_diag_ctx(index + 1, current_provider, "2b")
                q2b = call_llm(current_provider, active_api_key, system_prompt, c2_prompt, max_retries=1, _usage_acc=token_usage, diag_path=diag_path, diag_ctx=diag_ctx_2b)
                q2b_ok = _record_quality(quality, q2b)
                for (base, r1, r2_data, r2_ok) in [(q1, q1, q2, q2_ok), (q1b, q1b, q2b, q2b_ok)]:
                    question_id = qid_a if base is q1 else qid_b
                    self_consistent = False
                    if r2_ok:
                        self_consistent = (r1.get("answer", "").strip() == r2_data.get("answer", "").strip())
                    final_q = make_question_from_llm(r1, question_id, chunk, dim, difficulty, provider=current_provider)
                    final_q["consistency_status"] = "auto_passed" if self_consistent else "needs_review"
                    if not self_consistent and r2_data:
                        review_items.append({
                            "id": question_id, "dimension": dim, "difficulty": difficulty,
                            "question": r1.get("question", ""),
                            "round_1_answer": r1.get("answer", ""), "round_1_steps": r1.get("reasoning_steps", []),
                            "round_2_answer": r2_data.get("answer", ""), "round_2_steps": r2_data.get("reasoning_steps", []),
                            "verdict": None,
                        })
                    questions.append(final_q)
                index += 2
            else:
                self_consistent = False
                if q2_ok:
                    self_consistent = (q1.get("answer", "").strip() == q2.get("answer", "").strip())
                final_q = make_question_from_llm(q1, qid_a, chunk, dim, difficulty, provider=current_provider)
                final_q["consistency_status"] = "auto_passed" if self_consistent else "needs_review"
                if not self_consistent and q2:
                    review_items.append({
                        "id": qid_a, "dimension": dim, "difficulty": difficulty,
                        "question": q1.get("question", ""),
                        "round_1_answer": q1.get("answer", ""), "round_1_steps": q1.get("reasoning_steps", []),
                        "round_2_answer": q2.get("answer", ""), "round_2_steps": q2.get("reasoning_steps", []),
                        "verdict": None,
                    })
                questions.append(final_q)
                index += 1
        else:
            qid = f"CS-EVO-{index:05d}"
            self_consistent = False
            if q2_ok:
                self_consistent = (q1.get("answer", "").strip() == q2.get("answer", "").strip())
            final_q = make_question_from_llm(q1, qid, chunk, dim, difficulty, provider=current_provider)
            final_q["consistency_status"] = "auto_passed" if self_consistent else "needs_review"
            if not self_consistent and q2:
                review_items.append({
                    "id": qid, "dimension": dim, "difficulty": difficulty,
                    "question": q1.get("question", ""),
                    "round_1_answer": q1.get("answer", ""), "round_1_steps": q1.get("reasoning_steps", []),
                    "round_2_answer": q2.get("answer", ""), "round_2_steps": q2.get("reasoning_steps", []),
                    "verdict": None,
                })
            questions.append(final_q)
            index += 1

        chunk_index += 1
        consecutive_failures = 0
        questions_since_reset += 1

        if questions_since_reset >= reset_every or quality.should_reset():
            trigger = "quality" if quality.should_reset() else "periodic"
            print(f"  [Reset] {trigger} reset after {questions_since_reset} questions since last reset", flush=True)
            logger.info(f"{trigger.capitalize()} reset at {len(questions)} questions, {questions_since_reset} since last reset")
            system_prompt = build_system_prompt()
            quality.reset()
            questions_since_reset = 0

        if output_path and review_path and len(questions) % 10 == 0:
            qs = quality.summary()
            rate, eta_min = save_checkpoint(
                output_path, review_path, questions, review_items,
                index, chunk_index, 0, current_provider, active_model,
                f"AI-generated via {current_provider}/{active_model}",
                start_time, limit=limit, consecutive_failures=consecutive_failures,
                token_usage=token_usage, quality_summary=qs, questions_since_reset=questions_since_reset,
            )
            dim_counts_str = " ".join(f"{d}={dim_counts.get(d,0)}" for d in "ABCD")
            print(f"  ✓ checkpoint ({len(questions)}/{limit}) {rate:.1f}题/min ETA:{eta_min:.0f}min | {dim_counts_str}", flush=True)
            logger.info(f"Checkpoint: {len(questions)}/{limit}, rate={rate:.1f}, eta={eta_min:.0f}min")

        if output_path and review_path and len(questions) > 0:
            status_path = output_path.parent / "generation_status.json"
            _write_light_status(status_path, questions, limit, consecutive_failures, token_usage, start_time, current_provider, quality_summary=quality.summary(), questions_since_reset=questions_since_reset)

    reached_limit = len(questions) >= limit

    if output_path and review_path:
        qs = quality.summary()
        save_checkpoint(
            output_path, review_path, questions, review_items,
            index, chunk_index, 0, current_provider, active_model,
            f"AI-generated via {current_provider}/{active_model}",
            start_time, limit=limit, consecutive_failures=consecutive_failures,
            token_usage=token_usage, quality_summary=qs, questions_since_reset=questions_since_reset,
        )
        elapsed = time.time() - start_time
        logger.info(f"Done: {len(questions)}/{limit} in {elapsed:.0f}s")
        status_path = output_path.parent / "generation_status.json"
        final_dim = build_meta(questions, f"AI-generated via {current_provider}/{active_model}")["dimensions"]
        final_status = "completed" if reached_limit else "stopped_early"
        write_json_atomic(status_path, {
            "progress": f"{len(questions)}/{limit}",
            "percent": round(len(questions) / max(limit, 1) * 100, 1),
            "rate": round(len(questions) / elapsed * 60, 1) if elapsed > 0 else 0,
            "eta_min": 0,
            "dimensions": final_dim,
            "consecutive_failures": consecutive_failures,
            "questions_since_reset": questions_since_reset,
            "token_usage": {"prompt": token_usage[0], "completion": token_usage[1]},
            "elapsed_sec": round(elapsed, 0),
            "provider": current_provider,
            "seed": RUN_SEED,
            "status": final_status,
            "quality": qs,
            "last_updated": time.strftime("%H:%M:%S"),
        })

    return questions[:limit], review_items


def make_question(qid, dimension, difficulty, chunk, sibling_id=None):
    section = chunk.get("source_section") or chunk.get("chunk_id")
    categories = normalize_categories(chunk.get("categories"))
    topic = section.replace("#", "").strip()[:80] or chunk.get("filename", "控制系统")
    source_ref = chunk.get("chunk_id")

    base = {
        "id": qid,
        "dimension": dimension,
        "difficulty_level": difficulty,
        "control_category": categories,
        "source_ref": source_ref,
        "consistency_status": "auto_passed",
        "sensitivity_dimension": None,
        "sibling_id": None,
        "rubric": None,
    }

    if dimension == "A":
        base.update(
            {
                "question": f"结合教材片段“{topic}”，说明其中涉及的核心控制概念，并给出必要的数学表达。",
                "answer": f"该片段围绕{topic}展开。答案应给出概念定义、关键变量含义，并写出与该概念对应的核心表达式或判据。",
                "reasoning_steps": ["识别片段主题", "抽取核心概念", "说明数学表达", "解释变量或判据含义"],
            }
        )
    elif dimension == "B":
        base.update(
            {
                "question": f"基于教材片段“{topic}”，构造一个多步推理问题：从系统描述出发推导控制结论。",
                "answer": "应先建立模型或方程，再应用对应控制理论判据，最后给出稳定性、性能或控制律结论。",
                "reasoning_steps": ["建立系统描述", "选择适用判据或方法", "执行代数或逻辑推导", "给出结论并解释"],
            }
        )
    elif dimension == "C":
        base.update(
            {
                "question": f"在“{topic}”场景下，如果关键参数或约束发生变化，原控制结论是否保持？请说明。",
                "answer": "需要比较变化前后的模型、参数或约束，判断控制性能或稳定性结论是否改变，并说明敏感性来源。",
                "reasoning_steps": ["确定基准条件", "引入条件变化", "比较判据或性能指标", "解释结论变化"],
                "sensitivity_dimension": "parameter",
                "sibling_id": sibling_id,
            }
        )
    else:
        base.update(
            {
                "question": f"围绕“{topic}”设计一个完整控制方案，要求说明建模、控制器设计、验证指标和工程约束。",
                "answer": "可行方案应覆盖系统建模、控制方法选择、参数整定或优化、仿真/实验验证以及工程约束处理。",
                "reasoning_steps": ["分析控制目标", "建立模型", "选择控制方法", "设计验证流程", "讨论工程约束"],
                "rubric": default_rubric(topic),
            }
        )
    return base


def generate_mock_questions(chunks, limit):
    questions = []
    index = 1
    chunk_index = 0
    group_index = 0
    while len(questions) < limit and chunks:
        dimension = DIMENSION_CYCLE[group_index % len(DIMENSION_CYCLE)]
        difficulty_options = DIFFICULTY_BY_DIMENSION[dimension]
        difficulty = difficulty_options[group_index % len(difficulty_options)]
        chunk = chunks[chunk_index % len(chunks)]

        if dimension == "C" and len(questions) + 2 <= limit:
            qid_a = f"CS-EVO-{index:05d}"
            qid_b = f"CS-EVO-{index + 1:05d}"
            questions.append(make_question(qid_a, "C", difficulty, chunk, sibling_id=qid_b))
            questions.append(make_question(qid_b, "C", difficulty, chunk, sibling_id=qid_a))
            index += 2
        else:
            if dimension == "C":
                dimension = "D"
                difficulty = DIFFICULTY_BY_DIMENSION[dimension][group_index % len(DIFFICULTY_BY_DIMENSION[dimension])]
            qid = f"CS-EVO-{index:05d}"
            questions.append(make_question(qid, dimension, difficulty, chunk))
            index += 1
        chunk_index += 1
        group_index += 1
    return questions[:limit]


def build_meta(questions, source):
    dimensions = {dimension: 0 for dimension in DIMENSION_CYCLE}
    for question in questions:
        dimension = question.get("dimension")
        if dimension in dimensions:
            dimensions[dimension] += 1
    is_mock = "mock" in source.lower()
    return {
        "project": "ControlSci — 控制科学结构化语料库与 Sci-Align 跨模态对齐评测基准",
        "version": "1.0-mock" if is_mock else "1.0",
        "updated": str(date.today()),
        "total_questions": len(questions),
        "dimensions": dimensions,
        "source": source,
        "seed": RUN_SEED,
    }


def write_outputs(questions, output_path, review_path, source, review_items=None):
    data = {"meta": build_meta(questions, source), "questions": questions}
    output_path.parent.mkdir(parents=True, exist_ok=True)
    if output_path.exists():
        backup = output_path.with_suffix(f".{date.today().strftime('%Y%m%d_%H%M%S')}.bak.json")
        output_path.rename(backup)
        print(f"  Backup saved: {backup.name}", flush=True)
    write_json_atomic(output_path, data)
    if review_items:
        review = {"total": len(review_items), "items": review_items}
    else:
        review = {"total": 0, "items": []}
    review_path.parent.mkdir(parents=True, exist_ok=True)
    if review_path.exists():
        backup_rev = review_path.with_suffix(f".{date.today().strftime('%Y%m%d_%H%M%S')}.bak.json")
        review_path.rename(backup_rev)
    write_json_atomic(review_path, review)
    return data


def main():
    parser = argparse.ArgumentParser(description="Build ControlSci Sci-Align benchmark questions from corpus chunks.")
    parser.add_argument("--corpus", default=str(DEFAULT_CORPUS), help="Corpus root directory.")
    parser.add_argument("--output", default=str(DEFAULT_OUTPUT), help="Benchmark output JSON path.")
    parser.add_argument("--manual-review-output", default=str(DEFAULT_REVIEW), help="Manual review JSON path.")
    parser.add_argument("--model", default=None, help="Override model name (otherwise uses provider default).")
    parser.add_argument("--api-key", default=None, help="API key. Falls back to provider env var.")
    parser.add_argument("--category", default=None, help="Optional normalized control category filter, e.g. classical.")
    parser.add_argument("--limit", type=int, default=10, help="Number of questions to generate.")
    parser.add_argument("--mock", action="store_true", help="Generate deterministic mock questions without API calls.")
    parser.add_argument("--dry-run", action="store_true", help="Print generation plan without writing files.")
    parser.add_argument("--provider", default="deepseek", choices=["deepseek", "minimax", "mimo"],
                        help="Provider to use for generation.")
    parser.add_argument("--arbitrate", action="store_true",
                        help="Run arbitration pass: reads existing benchmark+review, resolves needs_review via DeepSeek.")
    parser.add_argument("--arbitrate-workers", type=int, default=3,
                        help="Parallel arbitration API calls. Default 3 balances speed and stability.")
    parser.add_argument("--arbitrate-max-tokens", type=int, default=1024,
                        help="Max tokens for each arbitration response. Default 1024.")
    parser.add_argument("--resume", action="store_true",
                        help="Resume from checkpoint files (benchmark.checkpoint.json + manual_review.checkpoint.json).")
    parser.add_argument("--supplement", type=int, default=0,
                        help="Generate N additional questions and append to existing benchmark.json.")
    parser.add_argument("--reset-every", type=int, default=15,
                        help="Rebuild OpenAI client and system prompt every N questions (default: 15).")
    parser.add_argument("--diag-stem", default=None,
                        help="Stem name for diagnostic log file (e.g. 'diag_test'). Writes to benchmark/logs/diag/generation_diag_{stem}.logl.")
    parser.add_argument("--seed", type=int, default=DEFAULT_SEED,
                        help="Random seed for chunk ordering and reproducible sampling metadata.")
    args = parser.parse_args()
    global RUN_SEED
    RUN_SEED = args.seed

    if args.arbitrate:
        output_path = Path(args.output).resolve()
        review_path = Path(args.manual_review_output).resolve()
        if not output_path.exists():
            raise SystemExit(f"Benchmark file not found: {output_path}")
        if not review_path.exists():
            raise SystemExit(f"Manual review file not found: {review_path}")
        api_key = args.api_key or first_env("DEEPSEEK_API_KEY|OPENAI_API_KEY")
        if not api_key:
            raise SystemExit("Arbitration mode requires --api-key or DEEPSEEK_API_KEY/OPENAI_API_KEY (uses DeepSeek).")
        arbitrate_questions(
            str(output_path), str(review_path), str(output_path), api_key,
            workers=args.arbitrate_workers,
            max_tokens=args.arbitrate_max_tokens,
        )
        return

    corpus_dir = Path(args.corpus).resolve()
    output_path = Path(args.output).resolve()
    review_path = Path(args.manual_review_output).resolve()

    diag_path = None
    if args.diag_stem:
        diag_path = str(ROOT / "benchmark" / "logs" / "diag" / f"generation_diag_{args.diag_stem}.logl")

    start_index = 1
    start_chunk = 0
    resume_questions = None
    if args.resume:
        cp_out = output_path.with_suffix(".checkpoint.json")
        cp_rev = review_path.with_suffix(".checkpoint.json")
        if not cp_out.exists() or not cp_rev.exists():
            raise SystemExit(f"Checkpoint files not found. Expected: {cp_out} and {cp_rev}")
        cp_data = load_json(cp_out)
        resume_questions = cp_data.get("questions", [])
        state = cp_data.get("state", {})
        checkpoint_seed = state.get("seed")
        if checkpoint_seed is not None and int(checkpoint_seed) != args.seed:
            raise SystemExit(f"Checkpoint seed={checkpoint_seed} does not match --seed {args.seed}. Use the original seed or start a new run.")
        start_index = state.get("next_index") or (len(resume_questions) + 1)
        start_chunk = state.get("chunk_index")
        if start_chunk is None:
            start_chunk = start_index - 1
        print(
            f"[Resume] Found {len(resume_questions)} checkpoint questions, "
            f"resuming from q{start_index}, chunk={start_chunk}",
            flush=True,
        )

    if args.supplement > 0:
        if not output_path.exists():
            raise SystemExit(f"Supplement mode requires existing benchmark.json: {output_path}")
        existing = load_json(output_path)
        resume_questions = existing.get("questions", [])
        start_index = len(resume_questions) + 1
        total_limit = len(resume_questions) + args.supplement
        print(f"[Supplement] Adding {args.supplement} to existing {len(resume_questions)} → total {total_limit}", flush=True)
    else:
        total_limit = args.limit

    docs, chunks = load_corpus(corpus_dir)
    selected = select_chunks(corpus_dir, docs, chunks, category=args.category, seed=args.seed)
    if not selected:
        raise SystemExit("No usable chunks found for the requested filters.")

    if args.dry_run:
        print(f"Corpus: {corpus_dir}")
        print(f"Usable chunks: {len(selected)}")
        requested = total_limit if args.supplement > 0 else args.limit
        print(f"Requested questions: {requested}")
        print(f"Mode: {'mock' if args.mock else 'api'}, provider: {args.provider}")
        print(f"Seed: {args.seed}")
        print(f"Reset every: {args.reset_every} questions")
        if diag_path:
            print(f"Diagnostic log: {diag_path}")
        if args.resume:
            print(f"Resume: checkpoint={len(resume_questions) if resume_questions else 0} questions")
        if args.supplement > 0:
            print(f"Supplement: +{args.supplement} to existing {len(resume_questions) if resume_questions else 0}")
        return

    provider = args.provider
    config = PROVIDER_CONFIG[provider]
    model = args.model or config["model"]

    env_spec = PROVIDER_ENV_MAP[provider]
    api_key = args.api_key or first_env(env_spec)
    if not api_key:
        raise SystemExit(f"API mode requires --api-key or {env_spec.replace('|', '/')} env var for provider '{provider}'.")

    print(f"[DEBUG] selected {len(selected)} chunks, provider={provider}, model={model}, limit={total_limit}, seed={args.seed}, reset_every={args.reset_every}", flush=True)

    if args.mock:
        questions = generate_mock_questions(selected, total_limit)
        data = write_outputs(
            questions,
            output_path,
            review_path,
            source=f"Mock-generated from ControlSci corpus chunks; model target={model}",
        )
    else:
        print("[DEBUG] calling generate_api_questions...", flush=True)
        questions, review_items = generate_api_questions(
            selected, total_limit, api_key, model, corpus_dir, provider=provider,
            start_index=start_index, start_chunk=start_chunk,
            resume_questions=resume_questions,
            output_path=output_path, review_path=review_path,
            reset_every=args.reset_every,
            diag_path=diag_path,
        )
        print(f"[DEBUG] generate_api_questions returned {len(questions)} questions", flush=True)
        data = write_outputs(
            questions,
            output_path,
            review_path,
            source=f"AI-generated via {provider}/{model} from ControlSci corpus chunks",
            review_items=review_items,
        )
        cp_out = output_path.with_suffix(".checkpoint.json")
        cp_rev = review_path.with_suffix(".checkpoint.json")
        if cp_out.exists():
            cp_out.unlink()
        if cp_rev.exists():
            cp_rev.unlink()
        needs_review = sum(1 for q in questions if q.get("consistency_status") == "needs_review")
        print(f"Questions needing review: {needs_review}/{data['meta']['total_questions']}")

    print(f"Benchmark saved: {output_path}")
    print(f"Manual review saved: {review_path}")
    print(f"Questions: {data['meta']['total_questions']}")


if __name__ == "__main__":
    main()
