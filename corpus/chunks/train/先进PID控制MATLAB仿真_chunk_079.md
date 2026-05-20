# 【仿真之一】采用 Simulink 模块实现 Simulink 仿真

通过 Simulink 模块实现不确定对象的表示，取 $k_{p}=10$ ， $k_{i}=10$ ， $k_{d}=10$ 。仿真结果如图 1-6 所示。

![](image/f63197c2b38a8bee6cca1e58bb777bfe91475d8a52119b0c64e0cdc8c1a37c49.jpg)

<details>
<summary>line</summary>

| time(s) | Ideal position signal | Position tracking |
| --- | --- | --- |
| 0.0 | 0.0 | 0.0 |
| 0.5 | 0.5 | 0.5 |
| 1.0 | 0.0 | 0.0 |
| 1.5 | -0.5 | -0.5 |
| 2.0 | 0.0 | 0.0 |
| 2.5 | 0.5 | 0.5 |
| 3.0 | 0.0 | 0.0 |
| 3.5 | -0.5 | -0.5 |
| 4.0 | 0.0 | 0.0 |
| 4.5 | 0.5 | 0.5 |
| 5.0 | 0.0 | 0.0 |
</details>

图 1-6 正弦响应
