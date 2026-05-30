"""PPL Matrix: base Qwen3.5-9B vs QLoRA 9B on test.jsonl 89 questions.
Also generates per-dimension breakdown for heatmap use in report.
"""
import json, time
from pathlib import Path
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig
from peft import PeftModel

ROOT = Path(__file__).resolve