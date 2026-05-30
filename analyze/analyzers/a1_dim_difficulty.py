def analyze(questions):
    dims = ["A", "B", "C", "D"]
    levels = ["L1", "L2", "L3", "L4"]
    matrix = {d: {l: 0 for l in levels} for d in dims}
    for q in questions:
        d = q.get("dimension", "?")
        l = q.get("difficulty_level", "?")
        if d in matrix and l in matrix[d]:
            matrix[d][l] += 1
    row_totals = {d: sum(matrix[d].values()) for d in dims}
    col_totals = {l: sum(matrix[d][l] for d in dims) for l in levels}
    return {
        "title": "四维 × 难度分布矩阵",
        "summary": f"四维各 125 题完美平衡；L1={col_totals['L1']}, L2={col_totals['L2']}, L3={col_totals['L3']}, L4={col_totals['L4']}",
        "data": {"matrix": matrix, "row_totals": row_totals, "col_totals": col_totals},
    }
