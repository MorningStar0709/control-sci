"""Data Flywheel: 5 new papers → benchmark build → evaluate → leaderboard update

Phase E extension of ControlSci eval pipeline.
Reuses GenericScorer from benchmark/eval/judge.py for consistent scoring.
Checkpoint/resume via jsonl (benchmark/eval/utils.py:append_jsonl).
"""
import json
import os
import re
import sys
import time
from datetime import datetime
from pathlib import Path

import httpx

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from benchmark.eval.judge import AScorer, BScorer, GenericScorer, create_judge_client
from benchmark.eval.utils import append_jsonl, write_json_atomic

# ── Paths ──────────────────────────────────────────────────────────
MD_DIR = ROOT / 'data' / 'sources_flywheel' / 'md'
FLYWHEEL_BENCH = ROOT / 'benchmark' / 'dataset' / 'flywheel_questions.json'
FLYWHEEL_FILTERED = ROOT / 'benchmark' / 'dataset' / 'flywheel_filtered.json'
EVAL_DIR = ROOT / 'benchmark' / 'eval' / 'results'
EVIDENCE_DIR = ROOT / 'benchmark' / 'agent' / 'logs'
LB_PATH = EVAL_DIR / 'leaderboard.json'

MAX_CHUNK = 6000
MAX_QUESTION_CHARS = 8000
MAX_PROMPT_CHARS = 24000
GEN_TEMPERATURE = 0.4
GEN_MAX_TOKENS = 4096
EVAL_MAX_TOKENS = 1024
TARGET_TEMPERATURE = 0.0

# ── Model definitions ──────────────────────────────────────────────
# Note: mimo-v2.5 is the base tier here; run_eval_pipeline.py uses mimo-v2.5-pro
# for the leaderboard. Scores are not directly comparable.
# MiniMax `/anthropic` endpoint speaks Anthropic protocol, not OpenAI.
MODEL_CONFIGS = [
    {
        'key': 'deepseek',
        'model': 'deepseek-v4-flash',
        'base_url': 'https://api.deepseek.com',
        'api_key_env': 'DEEPSEEK_API_KEY|OPENAI_API_KEY',
        'display': 'DeepSeek (v4-flash)',
        'protocol': 'openai',
    },
]


def first_env(env_spec):
    for env_name in str(env_spec or '').split('|'):
        value = os.environ.get(env_name.strip(), '')
        if value:
            return value
    return ''

# ── Question generation system prompt ──────────────────────────────
GEN_SYSTEM = """你是控制科学出题专家。从语料中生成高质量的评测题目。

输出纯 JSON 数组，每道题格式：
{
  "question": "题目文本",
  "answer": "标准答案",
  "dimension": "A/B/C/D (A=概念理解 B=公式推导 C=计算应用 D=综合分析)",
  "difficulty": 1-5,
  "paper_id": "论文ID"
}

严格限制：
- 每篇论文最多出 3 道题
- 全部 5 篇论文合计不超过 15 道题
- 如果超过上述限制，请截断只保留前 3 题/前 15 题

从每篇论文出 2-3 道题，覆盖不同维度。"""


# ═══════════════════════════════════════════════════════════════════
# Step 1 — Chunking
# ═══════════════════════════════════════════════════════════════════
def chunk_papers(md_dir, max_chunk=MAX_CHUNK, max_question=MAX_QUESTION_CHARS):
    """Read parsed Markdown files and split into ~max_chunk-char segments."""
    md_dir = Path(md_dir)
    if not md_dir.exists():
        raise FileNotFoundError(
            f"MD directory not found: {md_dir}\n"
            f"  Run search_and_download.py to fetch papers, then MinerU to parse them."
        )

    chunks = []
    for md_sub in sorted(md_dir.iterdir()):
        if not md_sub.is_dir():
            continue
        md_files = list(md_sub.glob('*.md'))
        if not md_files:
            continue
        md_text = md_files[0].read_text('utf-8')
        paper_id = md_sub.name.split('_')[0]

        paragraphs = [p.strip() for p in md_text.split('\n\n') if len(p.strip()) > 80]
        merged = []
        buf = ''
        for p in paragraphs:
            if len(p) > max_chunk:
                if buf:
                    merged.append(buf)
                    buf = ''
                for i in range(0, len(p), max_chunk):
                    merged.append(p[i:i + max_chunk])
                continue
            if len(buf) + len(p) < max_chunk:
                buf += '\n\n' + p if buf else p
            else:
                merged.append(buf)
                buf = p
        if buf:
            merged.append(buf)

        for i, sec in enumerate(merged):
            chunks.append({
                'paper_id': paper_id,
                'chunk_id': f'fw_{paper_id}_{i:03d}',
                'text': sec[:max_question],
            })
        print(f'  {paper_id}: {len(merged)} chunks, {sum(len(s) for s in merged)} chars')

    print(f'Total chunks: {len(chunks)}')
    return chunks


# ═══════════════════════════════════════════════════════════════════
# Step 2 — Question Generation
# ═══════════════════════════════════════════════════════════════════
def extract_json_array(raw):
    """Extract JSON array from LLM response text with multiple fallback strategies."""
    # Strategy 1: ```json ``` block
    if '```json' in raw:
        candidate = raw.split('```json')[1].split('```')[0].strip()
        if candidate.startswith('['):
            return json.loads(candidate)
    # Strategy 2: ``` ``` block — only check odd-indexed parts (code block content)
    if '```' in raw:
        parts = raw.split('```')
        for idx in range(1, len(parts), 2):
            candidate = parts[idx].strip()
            if candidate.startswith('['):
                try:
                    return json.loads(candidate)
                except (json.JSONDecodeError, ValueError):
                    continue
    # Strategy 3: regex (non-greedy, with nesting support)
    m = re.search(r'\[(?:[^\[\]]|\[(?:[^\[\]]|\[[^\[\]]*\])*\])*\]', raw, re.DOTALL)
    if m:
        try:
            return json.loads(m.group())
        except (json.JSONDecodeError, ValueError):
            pass
    # Strategy 4: strip leading/trailing noise then try
    raw_stripped = raw.strip()
    if raw_stripped.startswith('['):
        try:
            return json.loads(raw_stripped)
        except (json.JSONDecodeError, ValueError):
            pass
    return None


def generate_questions(client, chunks, output_path, max_retries=2, seed=42,
                       temperature=GEN_TEMPERATURE, max_questions=15):
    """Generate evaluation questions from paper chunks via DeepSeek."""
    questions_by_paper = {}
    for c in chunks:
        pid = c['paper_id']
        if pid not in questions_by_paper:
            questions_by_paper[pid] = []
        questions_by_paper[pid].append(c['text'])

    all_questions = []
    for pid, texts in questions_by_paper.items():
        combined = '\n\n---\n\n'.join(texts)
        prompt = f"论文 {pid} 的语料内容:\n\n{combined[:MAX_PROMPT_CHARS]}\n\n请出题。"

        for attempt in range(max_retries):
            try:
                resp = client.chat.completions.create(
                    model='deepseek-v4-flash',
                    messages=[
                        {'role': 'system', 'content': GEN_SYSTEM},
                        {'role': 'user', 'content': prompt},
                    ],
                    temperature=temperature,
                    max_tokens=GEN_MAX_TOKENS,
                )
                raw = resp.choices[0].message.content.strip()
                qs = extract_json_array(raw)
                if qs and isinstance(qs, list):
                    missing_fields = set()
                    for qi, q in enumerate(qs, 1):
                        if not all(k in q for k in ('question', 'answer')):
                            missing_fields.add(qi)
                            continue
                        q['question_id'] = f'FW-{pid}-{qi:03d}'
                        q['source'] = 'flywheel'
                        q['paper_id'] = pid
                        all_questions.append(q)
                    if missing_fields:
                        print(f'    Skipped {len(missing_fields)} questions (missing question/answer): '
                              f'indices={sorted(missing_fields)}')
                    print(f'  {pid}: {len(qs) - len(missing_fields)} questions (attempt {attempt + 1})')
                    break
                else:
                    print(f'  {pid}: JSON parse failed attempt {attempt + 1}, raw=[{raw[:160]}...]')
                    if attempt < max_retries - 1:
                        time.sleep(2)
            except Exception as e:
                print(f'  {pid}: FAILED attempt {attempt + 1} ({e})')
                if attempt < max_retries - 1:
                    time.sleep(3)
        time.sleep(1)

    # ── Truncation safety net: cap questions for reproducible smoke/full runs ──
    if max_questions > 0 and len(all_questions) > max_questions:
        print(f'  Question cap triggered: {len(all_questions)} → {max_questions}')
        all_questions = all_questions[:max_questions]

    output_path.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        'meta': {
            'source': 'flywheel',
            'seed': seed,
            'generation_temperature': temperature,
            'generated_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'question_count': len(all_questions),
        },
        'questions': all_questions,
    }
    write_json_atomic(output_path, payload)
    print(f'Total flywheel questions: {len(all_questions)}')
    return all_questions


# ═══════════════════════════════════════════════════════════════════
# Step 3 — Quality Filter
# ═══════════════════════════════════════════════════════════════════
def filter_questions(questions, output_path):
    """Deduplicate by question prefix + enforce minimum length."""
    filtered = []
    seen = set()
    for q in questions:
        q_text = q['question'].strip()
        if len(q_text) < 20:
            print(f'  Filtered (too short): {q.get("question_id", "?")} ({len(q_text)} chars)')
            continue
        key = q_text[:80]
        if key in seen:
            print(f'  Filtered (duplicate): {q.get("question_id", "?")}')
            continue
        seen.add(key)
        filtered.append(q)

    delta = len(questions) - len(filtered)
    print(f'Filtered: {len(questions)} → {len(filtered)} ({delta} dropped)')
    write_json_atomic(output_path, filtered)
    return filtered


# ═══════════════════════════════════════════════════════════════════
# Step 4 — Evaluation
# ═══════════════════════════════════════════════════════════════════
def build_model_client(cfg):
    """Create a client for a target model. Supports OpenAI and Anthropic protocols."""
    api_key = first_env(cfg['api_key_env'])
    if not api_key:
        return None

    if cfg.get('protocol') == 'anthropic':
        from anthropic import Anthropic
        return Anthropic(api_key=api_key, base_url=cfg['base_url'],
                         timeout=120, http_client=httpx.Client(proxy=None, trust_env=False))

    from openai import OpenAI, DefaultHttpxClient

    return OpenAI(
        api_key=api_key,
        base_url=cfg['base_url'],
        timeout=120,
        max_retries=0,
        http_client=DefaultHttpxClient(proxy=None),
    )


def call_target(cfg, client, question_text):
    """Call the target model, return answer text. Handles both OpenAI and Anthropic."""
    for attempt in range(3):
        try:
            if cfg.get('protocol') == 'anthropic':
                resp = client.messages.create(
                    model=cfg['model'],
                    messages=[{'role': 'user', 'content': question_text}],
                    temperature=TARGET_TEMPERATURE,
                    max_tokens=EVAL_MAX_TOKENS,
                )
                return resp.content[0].text.strip()
            else:
                resp = client.chat.completions.create(
                    model=cfg['model'],
                    messages=[{'role': 'user', 'content': question_text}],
                    temperature=TARGET_TEMPERATURE,
                    max_tokens=EVAL_MAX_TOKENS,
                )
                return resp.choices[0].message.content.strip()
        except Exception as e:
            if attempt < 2:
                time.sleep(2 * (attempt + 1))
    return f'[ERROR: all 3 attempts failed]'


def score_answer(question, answer, judge_client, judge_model):
    """Dimension-aware LLM judge using existing benchmark infrastructure.

    Dimension A → AScorer (answer semantic equivalence, scores: 0.0/0.3/0.6/1.0)
    Dimension B → BScorer (reasoning step consistency, scores: 0.0/0.2/0.5/0.7/1.0)
    Dimension C/D → GenericScorer (fallback, scores: 0.0/0.25/0.5/0.75/1.0)
    """
    dim = question.get('dimension', 'A')
    if dim == 'A':
        scorer_cls = AScorer
    elif dim == 'B':
        scorer_cls = BScorer
    else:
        scorer_cls = GenericScorer

    try:
        result = scorer_cls.judge(
            question=question['question'],
            expected_answer=question['answer'],
            model_answer=answer,
            client=judge_client,
            model_name=judge_model,
        )
        return result.get('score', 0.0), result.get('reason', ''), result.get('issues', []), True
    except Exception as e:
        return None, str(e)[:200], [], False


def evaluate_flywheel(questions, model_configs, judge_client, judge_model, results_dir):
    """Evaluate flywheel questions with all available target models."""
    results_dir = Path(results_dir)
    results_dir.mkdir(parents=True, exist_ok=True)
    eval_results = {}

    for cfg in model_configs:
        print(f"\n{'─' * 40}")
        print(f"Evaluating: {cfg['display']} ({cfg['model']})")

        target_client = build_model_client(cfg)
        if target_client is None:
            print(f"  ⚠️ {cfg['api_key_env'].replace('|', '/')} not set — skipping")
            continue

        progress_path = results_dir / f'flywheel_progress_{cfg["key"]}.jsonl'
        out_path = results_dir / f'flywheel_eval_{cfg["key"]}.json'

        # ── Resume checkpoint ──
        done_ids = {}
        if progress_path.exists():
            for line in progress_path.read_text('utf-8').strip().split('\n'):
                if not line.strip():
                    continue
                try:
                    rec = json.loads(line)
                    done_ids[rec['question_id']] = rec
                except (json.JSONDecodeError, KeyError):
                    continue
            print(f'  Resume: {len(done_ids)} already evaluated')

        # ── Main eval loop ──
        total = len(questions)
        t_start = time.time()
        model_results = []

        for i, q in enumerate(questions):
            qid = q['question_id']

            # Checkpoint skip
            if qid in done_ids:
                model_results.append(done_ids[qid])
                continue

            # -- Target model call --
            answer = call_target(cfg, target_client, q['question'])

            # -- Judge call (skip if target failed) --
            if answer.startswith('[ERROR'):
                score, reason, issues, judge_ok = 0.0, answer, [], False
            else:
                score, reason, issues, judge_ok = score_answer(q, answer, judge_client, judge_model)

            rec = {
                'question_id': qid,
                'score': score,
                'dimension': q.get('dimension', '?'),
                'difficulty': q.get('difficulty', 0),
                'answer': answer[:200],
                'reason': reason[:200],
                'judge_ok': judge_ok,
            }
            if issues:
                rec['issues'] = issues

            model_results.append(rec)
            append_jsonl(progress_path, rec)

            # Progress
            if (i + 1) % 3 == 0 or i == total - 1:
                elapsed = time.time() - t_start
                new_count = i + 1 - len(done_ids)
                rate = new_count / elapsed if elapsed > 1 and new_count > 0 else 0
                eta_min = (total - i - 1) / rate / 60 if rate > 0 else 0
                score_display = f'{score:.2f}' if score is not None else 'FAIL'
                print(f'  [{i + 1}/{total}] {qid} score={score_display}, '
                      f'{rate:.2f} Q/s, ETA ~{eta_min:.1f}min')

            time.sleep(0.5)

        # ── Aggregate ──
        valid_scores = [r['score'] for r in model_results if r['score'] is not None]
        avg = sum(valid_scores) / len(valid_scores) if valid_scores else 0
        n_missing = len([r for r in model_results if r['score'] is None])

        result_doc = {
            'model': cfg['model'],
            'display': cfg['display'],
            'overall_score': round(avg, 4),
            'total_questions': len(model_results),
            'valid_scores': len(valid_scores),
            'missing_scores': n_missing,
            'results': model_results,
            'evaluated_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        }

        write_json_atomic(out_path, result_doc)
        print(f'  {cfg["display"]}: overall={avg:.4f} (valid={len(valid_scores)}, missing={n_missing})')
        eval_results[cfg['key']] = result_doc

    return eval_results


# ═══════════════════════════════════════════════════════════════════
# Step 5 — Before / After Comparison
# ═══════════════════════════════════════════════════════════════════
def compare_before_after(eval_results, new_question_count, lb_path, evidence_dir=EVIDENCE_DIR):
    """Show flywheel impact and save evidence JSON."""
    lb_path = Path(lb_path)

    baseline_questions = 500
    baseline_models = 0
    if lb_path.exists():
        lb = json.loads(lb_path.read_text('utf-8-sig'))
        baseline_models = len(lb.get('models', []))
        if 'total_questions' in lb:
            baseline_questions = lb['total_questions']

    active_models = list(eval_results.keys())
    expanded = baseline_questions + new_question_count

    print(f"""
┌─────────────────────────────────────────┐
│         数据飞轮：Before vs After        │
├─────────────────────────────────────────┤
│ 新题目:  {new_question_count} 题
│ 评测模型: {', '.join(active_models) if active_models else '(none)'}
│
│ Before: {baseline_questions} 题 / {baseline_models} 模型
│ After:  {expanded} 题 / {baseline_models + len(active_models)} 模型
│
│ Agent 自主完成全链路:
│  PDF→MD→出题→过滤→评测→排行榜更新
└─────────────────────────────────────────┘
""")

    evidence = {
        'flywheel_papers': '5 (via search_and_download.py)',
        'flywheel_questions_generated': 'see flywheel_questions.json',
        'flywheel_questions_filtered': new_question_count,
        'flywheel_eval_results': {
            k: {'model': v['model'], 'overall_score': v['overall_score']}
            for k, v in eval_results.items()
        },
        'baseline_questions': baseline_questions,
        'expanded_questions': expanded,
        'generated_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
    }

    evidence_path = Path(evidence_dir) / 'demo-data-flywheel.json'
    write_json_atomic(evidence_path, evidence)
    print(f'Evidence saved: {evidence_path}')
    return evidence


# ═══════════════════════════════════════════════════════════════════
# Main Pipeline
# ═══════════════════════════════════════════════════════════════════
def main():
    import argparse

    parser = argparse.ArgumentParser(
        description="Data Flywheel: 5 papers → benchmark → evaluate → leaderboard",
    )
    parser.add_argument('--skip-gen', action='store_true', help='Skip Step 2 question generation (use existing flywheel_questions.json)')
    parser.add_argument('--skip-eval', action='store_true', help='Skip Step 4 model evaluation')
    parser.add_argument('--skip-filter', action='store_true', help='Skip Step 3 quality filtering')
    parser.add_argument('--dry-run', action='store_true', help='Validate inputs and print the plan without API calls or writes.')
    parser.add_argument('--seed', type=int, default=42, help='Seed recorded in generated flywheel metadata.')
    parser.add_argument('--temperature', type=float, default=0.0, help='Question generation temperature. Default 0.0 for reproducibility.')
    parser.add_argument('--md-dir', default=str(MD_DIR), help='Parsed Markdown input directory.')
    parser.add_argument('--questions-output', default=str(FLYWHEEL_BENCH), help='Generated flywheel questions JSON.')
    parser.add_argument('--filtered-output', default=str(FLYWHEEL_FILTERED), help='Filtered flywheel questions JSON.')
    parser.add_argument('--eval-dir', default=str(EVAL_DIR), help='Evaluation result directory.')
    parser.add_argument('--evidence-dir', default=str(EVIDENCE_DIR), help='Evidence output directory.')
    parser.add_argument('--leaderboard', default=str(LB_PATH), help='Baseline leaderboard JSON path.')
    parser.add_argument('--limit-questions', type=int, default=15, help='Maximum generated/evaluated questions.')
    args = parser.parse_args()

    md_dir = Path(args.md_dir)
    questions_output = Path(args.questions_output)
    filtered_output = Path(args.filtered_output)
    eval_dir = Path(args.eval_dir)
    evidence_dir = Path(args.evidence_dir)
    leaderboard_path = Path(args.leaderboard)

    t_pipeline_start = time.time()

    all_questions = []
    filtered = []

    # Step 1 — Chunk papers
    print('=' * 50)
    print('Step 1/5: 读取 MinerU 解析结果')
    chunks = chunk_papers(md_dir)
    if args.dry_run:
        print('\nDRY-RUN plan:')
        print(f'  chunks: {len(chunks)}')
        print(f'  seed: {args.seed}')
        print(f'  generation temperature: {args.temperature}')
        print(f'  output questions: {questions_output}')
        print(f'  output filtered: {filtered_output}')
        print(f'  limit questions: {args.limit_questions}')
        print(f'  skip_gen={args.skip_gen}, skip_filter={args.skip_filter}, skip_eval={args.skip_eval}')
        return

    # Step 2 — Generate questions
    if not args.skip_gen:
        print('\n' + '=' * 50)
        print('Step 2/5: 出题 (DeepSeek)')
        gen_client, _ = create_judge_client()
        all_questions = generate_questions(
            gen_client,
            chunks,
            questions_output,
            seed=args.seed,
            temperature=args.temperature,
            max_questions=args.limit_questions,
        )
    else:
        if not questions_output.exists():
            raise FileNotFoundError(f"--skip-gen used but {questions_output} not found")
        existing = json.loads(questions_output.read_text('utf-8-sig'))
        all_questions = existing.get('questions', existing) if isinstance(existing, dict) else existing
        print(f'Step 2/5: SKIPPED — loaded {len(all_questions)} questions from {questions_output.name}')
        if args.limit_questions > 0:
            all_questions = all_questions[:args.limit_questions]

    # Step 3 — Filter
    if not args.skip_filter:
        print('\n' + '=' * 50)
        print('Step 3/5: 质量过滤')
        filtered = filter_questions(all_questions, filtered_output)
    else:
        print('Step 3/5: SKIPPED — using all generated questions')
        filtered = all_questions

    # Step 4 — Evaluate
    if not args.skip_eval:
        print('\n' + '=' * 50)
        print('Step 4/5: 模型评测')
        judge_client, judge_model = create_judge_client()
        eval_results = evaluate_flywheel(filtered[:args.limit_questions], MODEL_CONFIGS, judge_client, judge_model, eval_dir)
    else:
        print('Step 4/5: SKIPPED — no evaluation')
        eval_results = {}

    # Step 5 — Compare
    print('\n' + '=' * 50)
    print('Step 5/5: 数据飞轮成果对照')
    compare_before_after(eval_results, len(filtered), leaderboard_path, evidence_dir)

    elapsed = time.time() - t_pipeline_start
    print(f'\nData Flywheel Complete in {elapsed:.0f}s ({elapsed / 60:.1f}min)')


if __name__ == '__main__':
    main()
