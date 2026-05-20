import argparse
import json
import os
import re
import sys
import time
import urllib.request
import urllib.parse


def parse_atom(text):
    papers = []
    for entry in text.split("<entry>")[1:]:
        m = re.search(r'<id>https?://arxiv\.org/abs/(.+?)</id>', entry)
        arxiv_id = m.group(1).split("v")[0] if m else ""

        m = re.search(r'<title>(.+?)</title>', entry, re.DOTALL)
        title = m.group(1).strip() if m else ""

        authors = [a.group(1).strip() for a in re.finditer(r'<name>(.+?)</name>', entry)]

        m = re.search(r'<published>(\d{4})', entry)
        year = int(m.group(1)) if m else 0

        m = re.search(r'<arxiv:primary_category[^>]*term="(.+?)"', entry)
        category = m.group(1) if m else ""

        categories = [c.group(1) for c in re.finditer(r'<category[^>]*term="(.+?)"', entry)]

        m = re.search(r'<summary>(.+?)</summary>', entry, re.DOTALL)
        summary = m.group(1).strip()[:200].replace("\n", " ") if m else ""

        papers.append({
            "arxiv_id": arxiv_id, "title": title,
            "authors": authors[:5], "year": year,
            "category": category, "categories": categories,
            "pdf_url": f"https://arxiv.org/pdf/{arxiv_id}",
            "abstract_preview": summary,
        })
    return papers


def main():
    parser = argparse.ArgumentParser(description="Search arXiv papers by direction keywords")
    parser.add_argument("--project-dir", default=None, help="Override project root detection")
    parser.add_argument("--output-dir", default=None, help="Custom output directory for arxiv_candidates.json (overrides --project-dir)")
    parser.add_argument("--queries-file", default=None, help="Path to JSON file with custom queries. Format: [{\"key\": \"...\", \"name\": \"...\", \"query\": \"abs:...\", \"target\": N}]")
    parser.add_argument("--max-results", type=int, default=60, help="Results per query (default 60)")
    parser.add_argument("--delay", type=int, default=3, help="Seconds between queries (default 3)")
    args = parser.parse_args()

    if args.queries_file:
        with open(args.queries_file, "r", encoding="utf-8") as f:
            raw = json.load(f)
        queries = [(q["key"], q["name"], q["query"], q["target"]) for q in raw]
    else:
        queries = [
            ("multi_agent", "多智能体系统", 'abs:"multi-agent" AND abs:control AND cat:eess.SY', 30),
            ("reinforcement_learning_control", "智能控制（强化学习）", 'abs:"reinforcement learning" AND abs:control AND cat:eess.SY', 18),
            ("neural_network_control", "智能控制（神经网络）", 'abs:"neural network" AND abs:control AND NOT abs:reinforcement AND cat:eess.SY', 17),
            ("nonlinear_control", "非线性控制", 'abs:"nonlinear control" OR abs:"sliding mode" OR abs:Lyapunov AND cat:eess.SY', 25),
            ("robust_control", "鲁棒控制", 'abs:"robust control" OR abs:"H-infinity" OR abs:LMI AND cat:eess.SY', 20),
            ("model_predictive_control", "模型预测控制", 'abs:"model predictive control" OR abs:MPC AND cat:eess.SY', 15),
            ("optimal_control", "最优控制", 'abs:"optimal control" OR abs:"dynamic programming" AND cat:eess.SY', 10),
            ("adaptive_control", "自适应控制", 'abs:"adaptive control" OR abs:"self-tuning" AND cat:eess.SY', 15),
            ("event_triggered_control", "事件触发控制", 'abs:"event-triggered" OR abs:"self-triggered" AND cat:eess.SY', 8),
            ("networked_control", "网络化控制", 'abs:"networked control" OR abs:NCS AND cat:eess.SY', 7),
            ("distributed_control", "分布式/协同控制", 'abs:"distributed control" OR abs:consensus AND cat:eess.SY', 15),
            ("switched_hybrid_systems", "切换/混合系统", 'abs:"switched system" OR abs:"hybrid system" AND cat:eess.SY', 12),
            ("state_space_observers", "状态空间/观测器", 'abs:"state observer" OR abs:"state estimation" AND cat:eess.SY', 18),
            ("system_identification", "系统辨识/数据驱动", 'abs:"system identification" OR abs:"data-driven" AND cat:eess.SY', 15),
            ("stochastic_control", "随机控制/滤波", 'abs:"stochastic control" OR abs:"stochastic stability" AND cat:eess.SY', 12),
            ("robot_control", "机器人/运动规划", 'abs:"robot control" OR abs:"trajectory tracking" AND cat:eess.SY', 10),
            ("aero_guidance", "航空航天/制导", 'abs:guidance OR abs:UAV OR abs:quadrotor AND cat:eess.SY', 10),
            ("cyber_physical", "网络/信息物理系统", 'abs:"cyber-physical" OR abs:"secure control" AND cat:eess.SY', 10),
            ("game_economic_control", "博弈/经济控制", 'abs:"optimal transport" OR abs:"mean field game" AND cat:eess.SY', 10),
        ]

    if args.output_dir:
        candidates_path = os.path.join(os.path.abspath(args.output_dir), "arxiv_candidates.json")
    elif args.project_dir:
        base_dir = os.path.abspath(args.project_dir)
        candidates_path = os.path.join(base_dir, "data", "sources", "arxiv_candidates.json")
    else:
        base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        candidates_path = os.path.join(base_dir, "data", "sources", "arxiv_candidates.json")

    os.makedirs(os.path.dirname(candidates_path), exist_ok=True)

    if os.path.exists(candidates_path):
        with open(candidates_path, "r", encoding="utf-8") as f:
            data = json.load(f)
    else:
        data = []

    existing_ids = set()
    for entry in data:
        for c in entry["candidates"]:
            existing_ids.add(c["arxiv_id"])

    all_targets = {}
    new_entries = []
    failed_queries = 0

    for direction, direction_cn, query, target in queries:
        all_targets[direction] = target
        params = urllib.parse.urlencode({"search_query": query, "max_results": args.max_results, "sortBy": "relevance", "sortOrder": "descending"})
        url = f"https://export.arxiv.org/api/query?{params}"

        print(f"\n=== {direction_cn} ({direction}) ===")
        print(f"    Target: {target}")
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(req, timeout=120) as resp:
                text = resp.read().decode("utf-8")
            papers = parse_atom(text)
            new = [dict(p, selected=False, notes="") for p in papers if p["arxiv_id"] and p["year"] >= 2022 and p["arxiv_id"] not in existing_ids]
            for p in new:
                existing_ids.add(p["arxiv_id"])
            print(f"    New candidates: {len(new)}")
            new_entries.append({"direction": direction, "direction_cn": direction_cn, "target": target, "candidates": new})
        except Exception as e:
            print(f"    FAIL: {e}")
            failed_queries += 1
        time.sleep(args.delay)

    data.extend(new_entries)
    for entry in data:
        if entry["direction"] in all_targets:
            entry["target"] = all_targets[entry["direction"]]

    with open(candidates_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    total_candidates = sum(len(e["candidates"]) for e in data)
    total_target = sum(e["target"] for e in data)
    print(f"\nDone! Directions={len(data)} Candidates={total_candidates} Target={total_target}")

    for entry in data:
        if entry["target"] > 0:
            pool = len(entry["candidates"])
            mark = "OK" if pool >= entry["target"] else "SHORT"
            print(f"  [{mark}] {entry['direction_cn']:20s} target={entry['target']:2d} pool={pool:3d}")

    if failed_queries > 0:
        sys.exit(1)


if __name__ == "__main__":
    main()
