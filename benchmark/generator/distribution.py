"""Dimension and difficulty distribution control for benchmark generation."""

CATEGORY_MAP = {
    "控制理论": "classical",
    "控制科学": "modern",
    "控制系统": "classical",
    "经典控制": "classical",
    "现代控制": "modern",
    "非线性控制": "nonlinear",
    "鲁棒控制": "robust",
    "最优控制": "optimal",
    "自适应控制": "adaptive",
    "数字控制": "digital",
    "智能控制": "intelligent",
    "模型预测控制": "mpc",
    "多智能体系统": "multi_agent",
}

DIMENSION_CYCLE = ["A", "B", "C", "D"]

DIFFICULTY_BY_DIMENSION = {
    "A": ["L1", "L2", "L3", "L4"],
    "B": ["L2", "L3", "L4", "L1"],
    "C": ["L2", "L3", "L4"],
    "D": ["L2", "L3", "L4"],
}

DIM_TARGET = {
    "A": 100, "B": 150, "C": 100, "D": 150,
}

DIFFICULTY_TARGET = {
    "A": {"L1": 40, "L2": 30, "L3": 20, "L4": 10},
    "B": {"L2": 20, "L3": 50, "L4": 50},
    "C": {"L2": 50, "L3": 30, "L4": 20},
    "D": {"L2": 30, "L3": 70, "L4": 50},
}


def normalize_categories(raw_categories):
    categories = []
    for raw in raw_categories or []:
        mapped = CATEGORY_MAP.get(raw, raw)
        if mapped not in categories:
            categories.append(mapped)
    return categories[:3] or ["classical"]


def pick_next_dim_and_diff(questions, limit):
    if not questions:
        return "A", "L1"
    counts = {"A": 0, "B": 0, "C": 0, "D": 0}
    for q in questions:
        dimension = q.get("dimension")
        if dimension in counts:
            counts[dimension] += 1
    total_target = sum(DIM_TARGET.values())
    target_ratio = {d: DIM_TARGET[d] / total_target for d in DIM_TARGET}
    current_ratio = {d: counts[d] / max(len(questions), 1) for d in counts}
    dim = max(DIM_TARGET, key=lambda d: target_ratio[d] - current_ratio[d])
    if DIM_TARGET[dim] > 0 and counts[dim] >= DIM_TARGET[dim]:
        remaining = [d for d in DIM_TARGET if counts[d] < DIM_TARGET[d]]
        if remaining:
            dim = max(remaining, key=lambda d: target_ratio[d] - current_ratio[d])

    diff_target = DIFFICULTY_TARGET[dim]
    diff_counts = {d: 0 for d in diff_target}
    for q in questions:
        if q.get("dimension") == dim:
            difficulty = q.get("difficulty_level")
            if difficulty in diff_counts:
                diff_counts[difficulty] += 1
    total_diff_target = sum(diff_target.values())
    diff_target_ratio = {d: diff_target[d] / total_diff_target for d in diff_target}
    diff_current_ratio = {d: diff_counts.get(d, 0) / max(sum(diff_counts.values()), 1) for d in diff_target}
    difficulty = max(diff_target, key=lambda d: diff_target_ratio.get(d, 0) - diff_current_ratio.get(d, 0))
    return dim, difficulty
