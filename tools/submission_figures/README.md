# Submission figure scripts

This directory contains maintained scripts for generating figures and visual evidence used by the submission reports.

Scripts here were promoted from the ignored `_tools/` workspace because they generate public report assets or reusable evaluation figures.

## Contents

- `viz_dual_role_matrix.py` - dual-role answerer vs judge matrix.
- `viz_multi_format_demo.py` - multi-format parsing capability table.
- `bench_mineru_1.2b_vlm.py` - MinerU 1.2B VLM vs MiMo formula recognition comparison.
- `viz_dual_track_synergy.py` - dual-track synergy matrix.
- `viz_alignment_gallery.py` - visual audit best/worst alignment gallery.
- `viz_code_structure.py` - code structure flow figure.

Run from the repository root with the project Python environment, for example:

```powershell
& "python" "tools\submission_figures\viz_dual_role_matrix.py"
```

