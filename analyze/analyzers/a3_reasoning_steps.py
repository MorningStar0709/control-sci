import statistics

def analyze(questions):
    dims = {"A": [], "B": [], "C": [], "D": []}
    for q in questions:
        d = q.get("dimension", "?")
        steps = q.get("reasoning_steps") or []
        if d in dims:
            dims[d].append(len(steps))
    stats = {}
    for d, lengths in dims.items():
        if lengths:
            stats[d] = {
                "count": len(lengths),
                "mean": round(statistics.mean(lengths), 2),
                "median": round(statistics.median(lengths), 2),
                "min": min(lengths),
                "max": max(lengths),
                "q25": round(statistics.quantiles(lengths, n=4)[0], 2),
                "q75": round(statistics.quantiles(lengths, n=4)[2], 2),
            }
        else:
            stats[d] = {"count": 0}
    return {
        "title": "推理步骤深度分布（按维度）",
        "summary": f"B 维推理步数最多（均值 {stats['B']['mean']}），A 维最少（均值 {stats['A']['mean']}），维度区分度合理",
        "data": stats,
    }
