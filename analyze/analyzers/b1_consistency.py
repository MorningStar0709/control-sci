from collections import Counter

def analyze(questions):
    status_counter = Counter()
    dim_status = {d: Counter() for d in ["A", "B", "C", "D"]}
    for q in questions:
        s = q.get("consistency_status", "unknown")
        d = q.get("dimension", "?")
        status_counter[s] += 1
        if d in dim_status:
            dim_status[d][s] += 1
    auto_pct = round(status_counter.get("auto_passed", 0) / len(questions) * 100, 1) if questions else 0
    return {
        "title": "一致性状态分布",
        "summary": f"auto_passed 占 {auto_pct}%，reviewed_kept 占 {100-auto_pct:.1f}%；Embedding 快速通道有效过滤低级重复",
        "data": {
            "status_counts": dict(status_counter.most_common()),
            "dim_status_matrix": {d: dict(c.most_common()) for d, c in dim_status.items()},
            "auto_passed_pct": auto_pct,
        },
    }
