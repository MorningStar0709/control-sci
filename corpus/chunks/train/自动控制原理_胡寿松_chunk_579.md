# 8-6 非线性控制系统设计

例 8-10 恒温箱温度控制。设恒温箱动态结构图如图 8-59 所示。若要求温度保持 $200^{\circ}C$ ，恒温箱由常温 $20^{\circ}C$ 启动，试在 $T_{c}-\dot{T}_{c}$ 相平面上作出温度控制的相轨迹，并计算升温时间和保持温度的精度，最后进行 MATLAB 验证。

![](image/5868716dc19a1917bf92d5bd770ef7612fc6e226e78c32af8cb840440aaf6143.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    A["200°C"] --> B((+))
    B --> C["110 (square root) / (-5 0 5)"]
    C --> D["5.5 / (100s+1)"]
    D --> E["Tc"]
    E --> F["-"]
    F --> B
```
</details>

图 8-59 恒温箱结构图

解 由图 8-59 可得系统分段微分方程为

$$
1 0 0 \dot {T} _ {c} + T _ {c} = \left\{ \begin{array}{l l} 6 0 5, & \left\{ \begin{array}{l} T _ {c} <   1 9 5 \\ T _ {c} <   2 0 5, \dot {T} _ {c} > 0 \end{array} \right. \\ 0, & \left\{ \begin{array}{l} T _ {c} > 2 0 5 \\ T _ {c} <   1 9 5, \dot {T} _ {c} <   0 \end{array} \right. \end{array} \right.
$$

相应的相轨迹如图 8-60 所示。相轨迹在开关线上跳至另一条相轨迹。

升温时间：在升温时，相轨迹沿图8-60中AB运动。AB段对应的相轨迹方程为

$$
\begin{array}{l} \dot {T} _ {c} = \frac {(6 0 5 - T _ {c})}{1 0 0} \\ t _ {r} = \int_ {2 0} ^ {2 0 0} \frac {\mathrm{d} T _ {c}}{\dot {T} _ {c}} = \int_ {2 0} ^ {2 0 0} \frac {1 0 0}{6 0 5 - T _ {c}} \mathrm{d} T _ {c} \\ = 1 0 0 \ln \frac {5 8 5}{4 0 5} = 3 6. 7 7 \mathrm{s} \\ \end{array}
$$

![](image/17d108d58e349bc9ad572fb1e839c50464c59d0c951ecaea8b7a69de2a091357.jpg)

<details>
<summary>line</summary>

| Point | Temperature (°C) |
| --- | --- |
| A | 20 |
| B | 200 |
</details>

图 8-60 恒温箱温度控制系统

MATLAB 验证：应用 MATLAB 软件包，在 Simulink 环境下搭建如图 8-61 所示的温控系统仿真模型，其中 MATLAB Function 环节的调用函数为 M 文件 fun.m，运行它可在相平面上精确绘出 $T_{c}-\dot{T}_{c}$ 相轨迹，同时也可绘出恒温箱温度控制系统的时间响应曲线，如图 8-62 中的 (a)，(b) 所示，最后测得：升温时间 $t_{r}=36.96s$ ，保温精度为 $\pm5^{\circ}C$ 。

MATLAB Function 环节的调用函数：

```matlab
function y=fun(u)
if ((u(2)>=5) | ((u(2)>=-5)&(u(1)>=0)))
y=110;
else y=0
end 
```

![](image/9d24969d31e2ac2c80578a58e648281a4fa678997c7e6e2d77292b8fb890484c.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["Clock"] --> B["t"]
    B --> C["To Workspace1"]
    D["200"] --> E["+"]
    E --> F["MATLAB Function nonlinear"]
    F --> G["0.055 Gain2"]
    G --> H["Gain1"]
    H --> I["+"]
    I --> J["Integrator"]
    J --> K["Tc"]
    L["dTc"] --> M["To Workspace2"]
    N["Tc"] --> O["To Workspace"]
    P["Constant"] --> E
```
</details>

图 8-61 Simulink 环境下的温控系统仿真模型

![](image/1c16f0ee92a278f65fc6d7c486ca57822d42774d137a21ab8299bb896eb8abca.jpg)

<details>
<summary>line</summary>

| T_c | ic |
| --- | --- |
| 0 | 6.0 |
| 50 | 5.5 |
| 100 | 5.0 |
| 150 | 4.5 |
| 200 | 4.0 |
| 200 | -2.0 |
| 250 | -2.0 |
</details>
