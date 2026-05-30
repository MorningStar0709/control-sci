"""医学术语映射管理器单元测试。

Usage:
  python -m pytest controlsci/medical/test_terminology.py -v
  python controlsci/medical/test_terminology.py
"""

from __future__ import annotations

import json
import os
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from controlsci.medical.terminology import (
    MedicalTerminologyManager,
    get_terminology_manager,
)


VALID_CONFIG = {
    "version": "1.0.0",
    "term_groups": [
        {
            "group_id": "test_group",
            "description": "测试组",
            "canonical_en": "test",
            "mappings": [
                {
                    "zh": "测试词A",
                    "en": "test_term_a",
                    "type": "specific",
                    "search_group": "1",
                },
                {
                    "zh": "测试词B",
                    "en": "test_term_b",
                    "type": "generic",
                    "search_group": "2",
                    "synonyms": ["同义词B"],
                },
            ],
        },
    ],
}


class TestMedicalTerminologyManager(unittest.TestCase):

    def setUp(self):
        self._original_env = os.environ.get("MEDICAL_TERMINOLOGY_PATH")
        os.environ.pop("MEDICAL_TERMINOLOGY_PATH", None)

    def tearDown(self):
        if self._original_env:
            os.environ["MEDICAL_TERMINOLOGY_PATH"] = self._original_env
        else:
            os.environ.pop("MEDICAL_TERMINOLOGY_PATH", None)

    def _write_config(self, config: dict) -> str:
        tmp = tempfile.NamedTemporaryFile(
            mode="w",
            suffix=".json",
            encoding="utf-8",
            delete=False,
        )
        json.dump(config, tmp)
        tmp.close()
        return tmp.name

    def test_load_valid_config(self):
        path = self._write_config(VALID_CONFIG)
        try:
            mgr = MedicalTerminologyManager(Path(path))
            self.assertTrue(mgr.is_loaded)
            self.assertEqual(len(mgr._zh_to_en), 3)  # 测试词A + 测试词B + 同义词B
            self.assertIn("测试词A", mgr._zh_to_en)
            self.assertIn("同义词B", mgr._zh_to_en)
        finally:
            os.unlink(path)

    def test_find_matches_chinese_query(self):
        path = self._write_config(VALID_CONFIG)
        try:
            mgr = MedicalTerminologyManager(Path(path))
            matches = mgr.find_matches("这是测试词A的查询")
            self.assertEqual(len(matches), 1)
            self.assertEqual(matches[0]["source"], "测试词A")
            self.assertEqual(matches[0]["rewrite"], "test_term_a")
            self.assertEqual(matches[0]["kind"], "specific")
            self.assertEqual(matches[0]["search_group"], "1")
        finally:
            os.unlink(path)

    def test_find_matches_synonym(self):
        path = self._write_config(VALID_CONFIG)
        try:
            mgr = MedicalTerminologyManager(Path(path))
            matches = mgr.find_matches("同义词B查询")
            self.assertEqual(len(matches), 1)
            self.assertEqual(matches[0]["source"], "同义词B")
            self.assertEqual(matches[0]["rewrite"], "test_term_b")
            self.assertTrue(matches[0]["is_synonym"])
        finally:
            os.unlink(path)

    def test_find_matches_multiple(self):
        path = self._write_config(VALID_CONFIG)
        try:
            mgr = MedicalTerminologyManager(Path(path))
            matches = mgr.find_matches("测试词A和测试词B")
            self.assertEqual(len(matches), 2)
            self.assertEqual(matches[0]["source"], "测试词A")
            self.assertEqual(matches[1]["source"], "测试词B")
        finally:
            os.unlink(path)

    def test_find_matches_sorted_by_pos(self):
        path = self._write_config(VALID_CONFIG)
        try:
            mgr = MedicalTerminologyManager(Path(path))
            matches = mgr.find_matches("前面同义词B后面测试词A")
            self.assertEqual(len(matches), 2)
            self.assertTrue(matches[0]["pos"] < matches[1]["pos"])
        finally:
            os.unlink(path)

    def test_no_matches(self):
        path = self._write_config(VALID_CONFIG)
        try:
            mgr = MedicalTerminologyManager(Path(path))
            matches = mgr.find_matches("无关文本")
            self.assertEqual(len(matches), 0)
        finally:
            os.unlink(path)

    def test_config_missing_graceful(self):
        nonexistent = Path(tempfile.gettempdir()) / "nonexistent_medical_terms.json"
        mgr = MedicalTerminologyManager(nonexistent)
        self.assertTrue(mgr.is_loaded)
        self.assertEqual(len(mgr._zh_to_en), 0)
        self.assertEqual(mgr.find_matches("测试词A"), [])

    def test_config_invalid_json(self):
        tmp = tempfile.NamedTemporaryFile(
            mode="w",
            suffix=".json",
            encoding="utf-8",
            delete=False,
        )
        tmp.write("{not valid json")
        tmp.close()
        try:
            mgr = MedicalTerminologyManager(Path(tmp.name))
            self.assertTrue(mgr.is_loaded)
            self.assertEqual(len(mgr._zh_to_en), 0)
        finally:
            os.unlink(tmp.name)

    def test_mapping_missing_zh_skipped(self):
        config = {
            "term_groups": [
                {
                    "group_id": "g",
                    "mappings": [
                        {"en": "only_en", "type": "specific"},
                        {"zh": "valid", "en": "valid_en", "type": "specific"},
                    ],
                }
            ]
        }
        path = self._write_config(config)
        try:
            mgr = MedicalTerminologyManager(Path(path))
            self.assertEqual(len(mgr._zh_to_en), 1)
            self.assertIn("valid", mgr._zh_to_en)
            self.assertNotIn("only_en", mgr._zh_to_en)
        finally:
            os.unlink(path)

    def test_mapping_missing_en_skipped(self):
        config = {
            "term_groups": [
                {
                    "group_id": "g",
                    "mappings": [
                        {"zh": "only_zh", "type": "specific"},
                        {"zh": "valid", "en": "valid_en", "type": "specific"},
                    ],
                }
            ]
        }
        path = self._write_config(config)
        try:
            mgr = MedicalTerminologyManager(Path(path))
            self.assertEqual(len(mgr._zh_to_en), 1)
            self.assertIn("valid", mgr._zh_to_en)
            self.assertNotIn("only_zh", mgr._zh_to_en)
        finally:
            os.unlink(path)

    def test_get_term_info(self):
        path = self._write_config(VALID_CONFIG)
        try:
            mgr = MedicalTerminologyManager(Path(path))
            info = mgr.get_term_info("测试词A")
            self.assertIsNotNone(info)
            self.assertEqual(info["en"], "test_term_a")
            self.assertIsNone(mgr.get_term_info("不存在的词"))
        finally:
            os.unlink(path)

    def test_get_group_terms_returns_copy(self):
        path = self._write_config(VALID_CONFIG)
        try:
            mgr = MedicalTerminologyManager(Path(path))
            terms = mgr.get_group_terms("test_group")
            self.assertEqual(len(terms), 2)
            terms.append({"zh": "注入"})
            terms2 = mgr.get_group_terms("test_group")
            self.assertEqual(len(terms2), 2)
        finally:
            os.unlink(path)

    def test_reload_config(self):
        config_v1 = {
            "term_groups": [{
                "group_id": "g",
                "mappings": [{"zh": "v1", "en": "v1_en", "type": "specific", "search_group": "1"}],
            }]
        }
        path = self._write_config(config_v1)
        try:
            mgr = MedicalTerminologyManager(Path(path))
            self.assertIn("v1", mgr._zh_to_en)

            config_v2 = {
                "term_groups": [{
                    "group_id": "g",
                    "mappings": [{"zh": "v2", "en": "v2_en", "type": "specific", "search_group": "1"}],
                }]
            }
            with open(path, "w", encoding="utf-8") as f:
                json.dump(config_v2, f)
                f.flush()
                os.fsync(f.fileno())

            mgr.reload_config()
            self.assertIn("v2", mgr._zh_to_en)
            self.assertNotIn("v1", mgr._zh_to_en)
        finally:
            os.unlink(path)

    def test_reload_skips_when_mtime_unchanged(self):
        path = self._write_config(VALID_CONFIG)
        try:
            mgr = MedicalTerminologyManager(Path(path))
            original_mtime = mgr._config_mtime
            mgr.reload_config()
            self.assertEqual(mgr._config_mtime, original_mtime)
            self.assertIn("测试词A", mgr._zh_to_en)
        finally:
            os.unlink(path)

    def test_env_config_path(self):
        path = self._write_config(VALID_CONFIG)
        os.environ["MEDICAL_TERMINOLOGY_PATH"] = path
        try:
            mgr = MedicalTerminologyManager()
            self.assertTrue(mgr.is_loaded)
            self.assertIn("测试词A", mgr._zh_to_en)
        finally:
            os.unlink(path)

    def test_get_terminology_manager_singleton(self):
        mgr1 = get_terminology_manager()
        mgr2 = get_terminology_manager()
        self.assertIs(mgr1, mgr2)


if __name__ == "__main__":
    unittest.main()
