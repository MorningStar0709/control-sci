from collections import Counter

def analyze(questions):
    cat_counter = Counter()
    dim_cat = {d: Counter() for d in ["A", "B", "C", "D"]}
    for q in questions:
        cats = q.get("control_category") or []
        d = q.get("dimension", "?")
        for c in cats:
            cat_counter[c] += 1
            if d in dim_cat:
                dim_cat[d][c] += 1
    top_cats = [c for c, _ in cat_counter.most_common(20)]
    dim_cat_matrix = {d: {c: dim_cat[d].get(c, 0) for c in top_cats} for d in ["A", "B", "C", "D"]}
    return {
        "title": "控制子领域标签覆盖率（Top 20）",
        "summary": f"唯一子领域标签 {len(cat_counter)} 个；Top 3: {', '.join(f'{c}({n})' for c,n in cat_counter.most_common(3))}；full.json 标签保持一致",
        "data": {"categories": dict(cat_counter.most_common(30)), "dim_cat_matrix": dim_cat_matrix},
    }
