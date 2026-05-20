# 5.2 二阶系统对初始状态的响应

首先分析二阶系统对初始状态的响应,即考虑无输入的情况, $u(t)=0$ 。试想如果在时间 $t=0$ 的时刻,质量块的位置 $x(0)\neq0$ 或者速度 $\left.\frac{\mathrm{d}x(t)}{\mathrm{d}t}\right|_{t=0}\neq0$ ,系统将如何运行?在4.2.2节中曾经分析过,使用相轨迹可以直观清晰地定性分析系统对初始条件的响应,因此本节将从此角度入手进行分析。当系统的输入 $u(t)=0$ 时,式(5.1.5)可写成

$$
\frac {\mathrm{d} z (t)}{\mathrm{d} t} = A z (t), \quad \text {其中} A = \left[ \begin{array}{c c} {{0}} & {{1}} \\ {{- \omega_ {\mathrm{n}} ^ {2}}} & {{- 2 \zeta \omega_ {\mathrm{n}}}} \end{array} \right] \tag {5.2.1}
$$

求这个系统的平衡点，令 $\frac{\mathrm{d}z(t)}{\mathrm{d}t} = 0$ ，可得

$$
\left\{ \begin{array}{l} 0 = z _ {2 \mathrm{f}} \\ 0 = - \omega_ {\mathrm{n}} ^ {2} z _ {1 \mathrm{f}} - 2 \zeta \omega_ {\mathrm{n}} z _ {2 \mathrm{f}} \end{array} \right.

\Rightarrow \left\{ \begin{array}{l} z _ {1 \mathrm{f}} = 0 \\ z _ {2 \mathrm{f}} = 0 \end{array} \right. \tag {5.2.2}
$$

分析平衡点的性质,首先要得到状态矩阵 A 的特征值,令 $\left|A-\lambda I\right|=0$ , 得到

$$
\left| \begin{array}{c c} - \lambda & 1 \\ - \omega_ {n} ^ {2} & - 2 \zeta \omega_ {n} - \lambda \end{array} \right| = \lambda^ {2} + 2 \zeta \omega_ {n} \lambda + \omega_ {n} ^ {2} = 0 \tag {5.2.3a}
$$

求解特征值,得到

$$
\left\{ \begin{array}{l} \lambda_ {1} = - \zeta \omega_ {\mathrm{n}} + \omega_ {\mathrm{n}} \sqrt {\zeta^ {2} - 1} \\ \lambda_ {2} = - \zeta \omega_ {\mathrm{n}} - \omega_ {\mathrm{n}} \sqrt {\zeta^ {2} - 1} \end{array} \right. \tag {5.2.3b}
$$

特征值 $\lambda$ 对应了式(5.1.3)中的传递函数 $G(s)$ 的极点。

下面来分类讨论不同的参数对特征值 $\lambda_{1}$ 和 $\lambda_{2}$ 的影响以及特征值将如何影响系统的表现。

类(1): $\zeta \geqslant 1$ 。

此时

$$
\zeta > \sqrt {\zeta^ {2} - 1} \geqslant 0
\Rightarrow \left\{ \begin{array}{l} \lambda_ {1} = - \zeta \omega_ {\mathrm{n}} + \omega_ {\mathrm{n}} \sqrt {\zeta^ {2} - 1} <   0 \\ \lambda_ {2} = - \zeta \omega_ {\mathrm{n}} - \omega_ {\mathrm{n}} \sqrt {\zeta^ {2} - 1} <   0 \end{array} \right. \tag {5.2.4}
$$

特征值 $\lambda_{1}$ 与 $\lambda_{2}$ 都为实数且都小于0。根据表3.3.1，平衡点 $z_{\mathrm{f}} = [0,0]^{\mathrm{T}}$ 是一个稳定的节点。它的相轨迹如图5.2.1(a)所示。不管初始位置从何处开始，都会随着时间的增加而趋于0。

其中, 当 $\zeta > 1$ 时的系统称为过阻尼系统 (Overdamped System), 当 $\zeta = 1$ 时的系统称为临界阻尼系统 (Critically Damped System)。过阻尼和临界阻尼的区别在于它们的收敛速度不同, 其中临界阻尼的系统收敛更快。本节重点在于定性分析, 这两种系统的细微差别将在 5.3 节定量分析中详细阐释。

类(2): $0 < \zeta < 1$ 。

此时
