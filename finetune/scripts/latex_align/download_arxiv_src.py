"""
下载5篇arXiv论文的LaTeX源码（用于LaTeX对齐PoC）
用法: conda run -n myenv python finetune/scripts/latex_align/download_arxiv_src.py
"""
import os, json, time, urllib.request
from _formula_utils import project_root, PAPERS

OUT_DIR = os.path.join(project_root(), "tmp", "latex_align")
os.makedirs(OUT_DIR, exist_ok=True)

def download_arxiv_source(arxiv_id, label):
    url = f"https://arxiv.org/e-print/{arxiv_id}"
    target_dir = os.path.join(OUT_DIR, f"{arxiv_id}_{label}")
    os.makedirs(target_dir, exist_ok=True)

    tar_path = os.path.join(target_dir, f"{arxiv_id}.tar.gz")

    if os.path.exists(tar_path) and os.path.getsize(tar_path) > 4096:
        print(f"  [SKIP] {arxiv_id}: already exists ({os.path.getsize(tar_path)} bytes)")
        return tar_path, target_dir

    print(f"  [DL] {arxiv_id} -> {tar_path}")
    try:
        req = urllib.request.Request(url, headers={
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36"
        })
        with urllib.request.urlopen(req, timeout=60) as resp:
            data = resp.read()
        with open(tar_path, 'wb') as f:
            f.write(data)
        print(f"  [OK] {arxiv_id}: {len(data)} bytes downloaded")
        time.sleep(2)
        return tar_path, target_dir
    except Exception as e:
        print(f"  [FAIL] {arxiv_id}: {e}")
        return None, target_dir

def _is_safe_member(target_dir, member_name):
    target_root = os.path.abspath(target_dir)
    dest_path = os.path.abspath(os.path.join(target_root, member_name))
    return dest_path == target_root or dest_path.startswith(target_root + os.sep)


def extract_tar(tar_path, target_dir):
    import tarfile
    try:
        with tarfile.open(tar_path, 'r:gz') as tar:
            members = tar.getmembers()
            tex_files = [m for m in members if m.name.endswith('.tex')]
            print(f"  [TAR] {len(members)} files, {len(tex_files)} .tex files")
            safe_members = []
            for member in members:
                if member.islnk() or member.issym():
                    print(f"  [SKIP] link member: {member.name}")
                    continue
                if not _is_safe_member(target_dir, member.name):
                    print(f"  [SKIP] unsafe path: {member.name}")
                    continue
                safe_members.append(member)
            tar.extractall(path=target_dir, members=safe_members)
            print(f"  [EXTRACT] -> {target_dir}")
            return tex_files
    except Exception as e:
        print(f"  [TAR FAIL] {e}")
        if tar_path and os.path.exists(tar_path):
            import shutil
            shutil.copy(tar_path, os.path.join(target_dir, "source.tex"))
            print(f"  [RAW] Copied as source.tex")
            return []

print(f"LaTeX源码输出目录: {OUT_DIR}")
print("=" * 60)

all_results = {}
for arxiv_id, label in PAPERS:
    print(f"\n--- {arxiv_id} ({label}) ---")
    tar_path, target_dir = download_arxiv_source(arxiv_id, label)
    if tar_path and os.path.exists(tar_path):
        tex_files = extract_tar(tar_path, target_dir)
        all_results[arxiv_id] = {
            "target_dir": target_dir,
            "tar_path": tar_path,
            "tex_files": [m.name for m in tex_files] if tex_files else [],
        }

print("\n" + "=" * 60)
print("下载摘要:")
for arxiv_id, info in all_results.items():
    tex_count = len(info.get("tex_files", []))
    print(f"  {arxiv_id}: {tex_count} .tex文件 -> {info['target_dir']}")

with open(os.path.join(OUT_DIR, "download_report.json"), 'w') as f:
    json.dump(all_results, f, indent=2, ensure_ascii=False)
print(f"\n报告保存: {os.path.join(OUT_DIR, 'download_report.json')}")
