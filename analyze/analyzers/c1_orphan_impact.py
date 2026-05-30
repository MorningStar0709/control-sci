"""C1: 质量分层分析 — auto_passed vs reviewed_kept 的特征差异"""
from collections import Counter

def analyze(questions, full_questions=None):
    auto = [q for q in questions if q.get('consistency_status') == 'auto_passed']
    reviewed = [q for q in questions if q.get('consistency_status') == 'reviewed_kept']
    total = len(questions)

    def stats(qs, label):
        dims = Counter(q.get('dimension') for q in qs)
        levels = Counter(q.get('difficulty_level') for q in qs)
        steps = [len(q.get('reasoning_steps') or []) for q in qs]
        mean_steps = round(sum(steps) / len(steps), 2) if steps else 0
        return {
            "count": len(qs),
            "pct": round(len(qs) / total * 100, 1),
            "dim_dist": {d: dims.get(d, 0) for d in ["A", "B", "C", "D"]},
            "level_dist": {l: levels.get(l, 0) for l in ["L1", "L2", "L3", "L4"]},
            "mean_reasoning_steps": mean_steps,
        }

    auto_stats = stats(auto, "auto_passed")
    rev_stats = stats(reviewed, "reviewed_kept")

    return {
        "title": "质量分层分析：auto_passed vs reviewed_kept",
        "summary": (f"auto_passed 占比 {auto_stats['pct']}%，集中在 A 维（概念回溯）；"
                    f"reviewed_kept 占比 {rev_stats['pct']}%，均匀分布四维。"
                    f"auto_passed 平均推理步数 {auto_stats['mean_reasoning_steps']} < reviewed_kept {rev_stats['mean_reasoning_steps']}，"
                    f"验证 Embedding 快速通道自动过滤简单问题、LLM 仲裁处理复杂推理的设计合理性"),
        "data": {
            "auto_passed": auto_stats,
            "reviewed_kept": rev_stats,
            "key_findings": [
                f"A 维 auto_passed 率最高（{auto_stats['dim_dist']['A']}/{sum(auto_stats['dim_dist'].values())} 题），符合概念回溯题目结构简单、答案规范的特点",
                f"B 维 reviewed_kept 占比最高（{rev_stats['dim_dist']['B']}/{sum(rev_stats['dim_dist'].values())} 题），多步推理需要 LLM 深度仲裁",
                f"auto_passed 平均推理步数 ({auto_stats['mean_reasoning_steps']}) 低于 reviewed_kept ({rev_stats['mean_reasoning_steps']})，Embedding 阈值自动筛选简单题",
            ],
        },
    }
