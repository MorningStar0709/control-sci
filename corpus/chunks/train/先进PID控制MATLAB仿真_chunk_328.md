# 6.4.1 非线性 PID 控制算法

传统的 PID 控制形式为误差的现在（P）、过去（I）和将来（变化趋势 D）的线性组合，显然这种线性组合不是最佳的组合形式，可以在非线性范围内寻求更合适、更有效的组合形式 $^{[4]}$ 。

韩京清教授推荐了三种非线性组合形式的 PID 控制器，其中的一种 PD 形式的非线性组合表示为 $^{[2]}$

$$u = \beta_ {1} \operatorname{fal} \left(e _ {1}, \alpha_ {1}, \delta\right) + \beta_ {2} \operatorname{fal} \left(e _ {2}, \alpha_ {2}, \delta\right) \tag {6.7}$$

式中， $0<\alpha_{1}<1<\alpha_{2}$ ; $k_{p}=\beta_{1}$ ; $k_{d}=\beta_{2}$ ; $e_{1}$ 为指令信号与被控对象位置输出之差； $e_{2}$ 为指令信号微分与被控对象速度输出之差。

为了避免高频振荡现象，将幂函数 $\left|e\right|^{\alpha}\operatorname{sgn}(e)$ 改造成原点附近具有线性段的连续的幂次函数，即饱和函数，表示为

$$
\operatorname{fal} (e, \alpha , \delta) = \left\{ \begin{array}{l l} \frac {e}{\delta^ {\alpha - 1}}, | e | \leqslant \delta \\ | e | ^ {\alpha} \operatorname{sgn} (e), | e | > \delta \end{array} \right. \tag {6.8}
$$

式中， $\delta$ 为线性段的区间长度。

![](image/f92bf072848c4b5f6d81b0b62e4eb6ec7467cf707a3fc5cf3475cf42128682a1.jpg)
