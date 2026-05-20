# Track 1 Local Dataset Loading Check

## Purpose

验证赛道一核心 JSON 数据可以被标准 `datasets.load_dataset("json")` 直接加载，说明公开数据不仅能在项目脚本中使用，也能以通用数据集工具链读取。

## Command

```powershell
python -c "from datasets import load_dataset; ds=load_dataset('json', data_files={'core':'benchmark/dataset/core.json'}, field='questions', split='core'); print('rows=', len(ds)); print('columns=', ','.join(ds.column_names)); print('first_id=', ds[0].get('id')); print('first_dimension=', ds[0].get('dimension')); print('last_id=', ds[-1].get('id')); print('last_dimension=', ds[-1].get('dimension'))"
```

## Result

- Rows loaded: `500`
- Columns loaded: `id, dimension, difficulty_level, control_category, question, answer, reasoning_steps, source_ref, model_source, sensitivity_dimension, sibling_id, rubric, consistency_status`
- First sample: `CS-EVO-00071`, dimension `A`
- Last sample: `CS-EVO-00187`, dimension `D`

## Evidence

- Raw stdout/stderr: `local_json_load_dataset.log`

## Notes

本检查只读取 `benchmark/dataset/core.json`，没有修改数据文件。
