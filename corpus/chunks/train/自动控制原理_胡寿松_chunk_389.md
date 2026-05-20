# (2) 采样系统的典型结构图

根据采样器在系统中所处的位置不同,可以构成各种采样系统。如果采样器位于系统闭合回路之外,或者系统本身不存在闭合回路,则称为开环采样系统;如果采样器位于系统闭合回路之内,则称为闭环采样系统。在各种采样控制系统中,用得最多的是误差采样控制的闭环采样系统,其典型结构图如图7-4所示。图中，S 为理想采样开关，其采样瞬时的脉冲幅值，等于相应采样瞬时误差信号 $e(t)$ 的幅值，且采样持续时间 $\tau$ 趋于零； $G_{h}(s)$ 为保持器的传递函数； $G_{0}(s)$ 为被控对象的传递函数； $H(s)$ 为测量变送反馈元件的传递函数。

![](image/bb899e8dbc3a63fdf7fe0f0029d828b8927374c39b94748dbf13e13a3c0aaaca.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    A["e*(t)"] --> B["信号复现滤波器 (保持器)"]
    B --> C["e_h(t)"]
```
</details>

图 7-3 保持器的输入与输出信号

![](image/7d40597807ff9d081453f610af24c25c93bb24a62f3137c15e27d57e24e9a443.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["e(t)"] --> B["Time t"]
    B --> C["e*(t)"]
    C --> D["Time t"]
    D --> E["e_h(t)"]
    E --> F["Time t"]
    F --> G["e(t)"]
    G --> H["S"]
    H --> I["r(t)"]
    I --> J["e(t)"]
    J --> K["e*(t)"]
    K --> L["G_h(s)"]
    L --> M["e_h(t)"]
    M --> N["G_0(s)"]
    N --> O["c(t)"]
    O --> P["H(s)"]
    P --> Q["b(t)"]
    Q --> R["-"]
    R --> S["Feedback to G_h(s)"]
    S --> T["Summing Junction"]
    T --> U["Summing Junction"]
    U --> V["Summing Junction"]
```
</details>

图 7-4 采样系统典型结构图

由图 7-4 可见, 采样开关 S 的输出 $e^{*}(t)$ 的幅值, 与其输入 $e(t)$ 的幅值之间存在线性关系。

当采样开关和系统其余部分的传递函数都具有线性特性时,这样的系统就称为线性采样系统。
