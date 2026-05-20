# 1. 一阶系统的数学模型

研究图 3-2(a) 所示 RC 电路, 其运动微分方程为

$$T \dot {c} (t) + c (t) = r (t) \tag {3-2}$$

式中， $c(t)$ 为电路输出电压； $r(t)$ 为电路输入电压；T=RC 为时间常数。当该电路的初始条件为零时，其传递函数为

$$\Phi (s) = \frac {C (s)}{R (s)} = \frac {1}{T s + 1} \tag {3-3}$$

相应的结构图如图 3-2(b) 所示。可以证明，室温调节系统、恒温箱以及水位调节系统的闭环传递函数形式与式(3-3)完全相同，仅时间常数含意有所区别。因此，式(3-2)或式(3-3)称为一阶系统的数学模型。在以下的分析和计算中，均假定系统初始条件为零。

应当指出,具有同一运动方程或传递函数的所有线性系统,对同一输入信号的响应是相同的。当然,对于不同形式或不同功能的一阶系统,其响应特性的数学表达式具有不同的物理意义。

![](image/959ccad05477c866c3ecd36af385806f8c6c902194ebbb813cdc23d936341969.jpg)

<details>
<summary>text_image</summary>

R
i(t)
r(t)
C
c(t)
</details>

(a)

![](image/9295ccb6ef9d3d8d235e8baa768ba0f25dadffbcde85a1037386b9ef8b22fbea.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    R["s"] --> A((+))
    A --> B["1/R"]
    B --> C["1/Cs"]
    C --> D["C(s)"]
    D --> E["Feedback"]
    E --> A
```
</details>

(b)   
图 3-2 一阶控制系统

![](image/68c47b4753f0f511d5e18bf9a9437eaadb08b93dd3a52c2feffcae5b8550db31.jpg)

<details>
<summary>line</summary>

| t | c(t) | Label |
| --- | --- | --- |
| T | 0.632 | c(t)=1-e^(-tT) |
| 2T | 0.865 | c(t)=1-e^(-tT) |
| 3T | - | c(t)=1-e^(-tT) |
| 4T | - | c(t)=1 |
</details>

图 3-3 一阶系统的单位阶跃响应曲线
