from collections import Counter

def analyze(questions):
    source_counter = Counter()
    dim_source = {d: Counter() for d in ["A", "B", "C", "D"]}
    for q in questions:
        s = q.get("model_source", "unknown")
        d = q.get("dimension", "?")
        source_counter[s] += 1
        if d in dim_source:
            dim_source[d][s] += 1
    return {
        "title": "三 Provider 贡献分析",
        "summary": f"Provider 分布: {dict(source_counter.most_common())}",
        "data": {
            "provider_counts": dict(source_counter.most_common()),
            "dim_provider_matrix": {d: dict(c.most_common()) for d, c in dim_source.items()},
        },
    }
