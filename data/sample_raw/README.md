# 原始数据样例 / Raw Data Samples

本目录提供 3 组原始 PDF → MinerU 解析输出的对照样例，用于展示 MinerU 跨模态提取管线在不同类型文档上的处理效果。

| 样例 | 类型 | 来源 | MinerU 输出 |
|:----:|------|------|:-----------:|
| 01 | 扫描版教材 | Khalil《非线性系统》第三版（中文翻译版，电子工业出版社） | chunk_001.md |
| 02 | 数字版论文 | arXiv:2201.02997 — Performance Analysis of Event-Triggered Consensus Control | chunk_042.md |
| 03 | 公式密集型教材 | Ogata《Modern Control Engineering》Fifth Edition (Prentice Hall) | chunk_015.md |

## 文件说明

每组样例的结构如下：

```
sample_raw/
├── README.md
├── 01_scanned_textbook/
│   └── mineru_output/
│       └── chunk_001.md        # MinerU 管线输出的前 80 行（封面+内容简介）
├── 02_digital_paper/
│   └── mineru_output/
│       └── chunk_042.md        # MinerU 管线输出的前 80 行（摘要+引言+预备知识）
└── 03_formula_dense/
    └── mineru_output/
        └── chunk_015.md        # MinerU 管线输出的前 80 行（封面+版权+目录）
```

## 数据来源声明

- **样例 01**：Khalil, H. K. (2002). *Nonlinear Systems* (3rd ed.). Pearson Education. 中文翻译版由电子工业出版社出版（2017）。本书为控制科学领域经典教材，覆盖非线性系统分析的核心方法。
- **样例 02**：Tatari, F. et al. (2022). *Performance Analysis of Event-Triggered Consensus Control for Multi-agent Systems under Cyber-Physical Attacks*. arXiv:2201.02997. 开放获取论文，来自 arXiv。
- **样例 03**：Ogata, K. (2010). *Modern Control Engineering* (5th ed.). Prentice Hall. 控制工程领域经典教材，以大量数学推导和公式著称。

所有原始 PDF 文件来源于公开渠道（arXiv 开放获取 / 教材公开发行版本），此处仅提供 MinerU 管线解析后的输出样页作为技术验证用途，不重新分发完整原始 PDF 文件。

## 用途

这些样例用于：
1. 展示 MinerU 对扫描版 PDF（含图像 OCR）的版面还原能力
2. 展示 MinerU 对数字原生 PDF（含 LaTeX 公式）的结构化提取效果
3. 展示 MinerU 对公式密集型文档（含复杂数学排版）的解析精度

完整语料库（23 本教材 + 339 篇论文）的 chunk 级元数据见 `benchmark/dataset/multimodal_index.json`，处理管线代码见 `pipeline/` 目录。
