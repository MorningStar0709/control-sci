# 7.8 补偿器设计：复合控制律与估计器

如果将7.5节所介绍的控制律设计方法与7.7节介绍的估计器设计方法相结合，用估计的状态变量来实现控制律的设计，那么可以获得抑制扰动却不跟踪外部参考输入的调节器。然而，因为控制律是为实际(非估计)状态的反馈而设计的，人们可能想知道用 $\hat{x}$ 代替 $x$ 会对系统动态产生什么影响。本节就来讨论这种影响。为此，我们要先计算出闭环特征方程以及开环补偿器传递函数，然后用这些结果比较状态空间设计与根轨迹、频率响应设计方法之间的差别。

具有反馈的被控对象方程为

$$\dot {x} = A x - B K \hat {x} \tag {7.165}$$

可将上式用状态误差 $\tilde{x}$ 表示为

$$\dot {x} = A x - B K (x - \widetilde {x}) \tag {7.166}$$

将式(7.166)与估计误差[式(7.132)]相结合，从而得到状态形式的整个系统动态为

$$
\left[ \begin{array}{c} \dot {x} \\ \dot {\widetilde {x}} \end{array} \right] = \left[ \begin{array}{c c} A - B K & B K \\ 0 & A - L C \end{array} \right] \left[ \begin{array}{c} x \\ \widetilde {x} \end{array} \right] \tag {7.167}
$$

该闭环系统的特征方程为

$$
\det \left[ \begin{array}{c c} s \mathbf {I} - \mathbf {A} + \mathbf {B K} & - \mathbf {B K} \\ \mathbf {0} & s \mathbf {I} - \mathbf {A} + \mathbf {L C} \end{array} \right] = 0 \tag {7.168}
$$

因为该矩阵为块三角形式(参见附录 WD，网址 www.fpe7e.com 可供参考及查询)，所以可将式(7.168)改写为

$$\det (s \mathbf {I} - \mathbf {A} + \mathbf {B K}) \cdot \det (s \mathbf {I} - \mathbf {A} + \mathbf {L C}) = \alpha_ {\mathrm{c}} (s) \alpha_ {\mathrm{e}} (s) = 0 \tag {7.169}$$

换句话说，复合系统的这组极点由控制极点与估计极点组成。这意味着控制律与估计器的设计可以独立进行，然而，当两者按此方式结合使用时，极点保持不变 $^{①}$ 。

将状态变量设计方法与在第5章和第6章所讨论的变换方法相比较，由图7.35蓝色阴影部分注意到对应着补偿器。将控制律 $u = -K\hat{x}$ （由于它是补偿器的一部分）代入估计器式(7.130)，从而得到该补偿器的状态方程为

$$\dot {\hat {x}} = (A - B K - L C) \hat {x} + L y \tag {7.170a}u = - \mathbf {K} \hat {\mathbf {x}} \tag {7.170b}$$

注意，式(7.170a)与式(7.18a)具有相同的结构，重写式(7.170a)为

![](image/d98a9d41270b2c8e930a2adb34532da2fe56edb2a04985126dca021d07143943.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["被控对象"] -->|w| B["传感器"]
    C["控制律"] -->|-K| D["补偿器"]
    B -->|x(t)| C
    D -->|u(t)| A
    D -->|x̂(t)| E["\hat{x} = Ax + Bu + L(y - C\hat{x})"]
    E -->|v| B
    B --> F["y(t)"]
    F --> G["补偿器"]
```
</details>

图 7.35 估计器与控制器机理

$$\dot {x} = A x + B u \tag {7.171}$$

由于式 $(7.18a)$ 的特征方程为

$$\det (s \mathbf {I} - \mathbf {A}) = 0 \tag {7.172}$$

比较式(7.170a)与式(7.171)，将等效矩阵代入式(7.172)，从而得到补偿器的特征方程为

$$\det (s \boldsymbol {I} - \boldsymbol {A} + \boldsymbol {B K} + \boldsymbol {L C}) = 0 \tag {7.173}$$

注意到我们既没有确定式(7.173)的根也没有在我们的状态空间设计法的讨论中用到这些根(注意补偿器并不一定稳定；式(7.173)的根有可能在右半平面)。从 y 到 u 的传递函数代表了动态补偿器，通过观察式(7.45)，以及代换式(7.173)中的相应矩阵，得到该传递函数为

$$D _ {c} (s) = \frac {U (s)}{Y (s)} = - K (s I - A + B K + L C) ^ {- 1} L \tag {7.174}$$

同样的方法可用于降阶估计器。此时，控制律为
