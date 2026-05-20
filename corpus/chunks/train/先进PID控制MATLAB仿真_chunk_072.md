# 【仿真之二】 连续系统 PID 的 Simulink 仿真

在仿真一的基础上，将仿真结果输出到工作空间中，利用 M 语言作图，仿真结果如图 1-3 所示。

![](image/a81b73c6ae4ee4bcea8e5ede52788397eb7272036a7407f2ff8189915e9f01fc.jpg)

<details>
<summary>line</summary>

| time(s) | Ideal position signal | Position tracking |
| --- | --- | --- |
| 0 | 0.0 | 0.0 |
| 1 | 1.0 | 1.0 |
| 2 | 0.0 | 0.0 |
| 3 | -1.0 | -1.0 |
| 4 | 0.0 | 0.0 |
| 5 | 1.0 | 1.0 |
| 6 | 0.0 | 0.0 |
| 7 | -1.0 | -1.0 |
| 8 | 0.0 | 0.0 |
| 9 | 1.0 | 1.0 |
| 10 | 0.0 | 0.0 |
</details>

图 1-3 PID 控制正弦响应
