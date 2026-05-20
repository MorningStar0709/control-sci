# 【仿真之一】连续系统 PID 的 Simulink 仿真

PID 控制器由 Simulink 下的工具箱提供。

Simulink 仿真程序: chap1\_1.mdl

![](image/50fc7d9dd35b3546cddddde447cf34de1840698852d9bd3bc93f9ad7201b6a25.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    A["Signal Generator"] --> B["Sum"]
    B --> C["PID Controller"]
    C --> D["Transfer Fcn"]
    D --> E["Mux"]
    E --> F["Scope"]
    B --> G["-"]
    G --> B
    D --> H["133/(s²+25s)"]
```
</details>

上述 PID 控制器采用 Simulink 封装的形式，其内部结构如下：

![](image/8cd982fc43edf3296227f56f40471ed2f083baeece24410ca36d471846a836e7.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["1 In_1"] --> B["Proportional"]
    A --> C["Integral"]
    A --> D["Derivative"]
    B --> E["Sum"]
    C --> E
    D --> E
    E --> F["Out_1"]
```
</details>

连续系统的模拟 PID 控制正弦响应结果如图 1-2 所示。

![](image/1e43f38b02035548d971541cb9b928d9654cfd64a69df33cbcdf188724429e5b.jpg)

<details>
<summary>line</summary>

| Time offset | Value |
| --- | --- |
| 0 | 0 |
| 1 | 1 |
| 2 | 0 |
| 3 | -1 |
| 4 | -2 |
| 5 | -1 |
| 6 | 0 |
| 7 | 1 |
| 8 | 0 |
| 9 | -1 |
| 10 | 0 |
</details>

图 1-2 连续系统的模拟 PID 控制正弦响应
