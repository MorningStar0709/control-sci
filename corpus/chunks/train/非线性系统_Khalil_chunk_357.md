# 12.3 积分控制

例 12.2 讨论了把单摆的摆角 $\theta$ 调节为常数 $\delta$ 的问题, 通过把期望的平衡点平移到原点, 使问题简化为一个稳定问题。这种方法在系统参数已知时是有效的, 而在有参数扰动时不可取。控制律

$$T = \frac {a \sin \delta}{c} - k _ {1} (\theta - \delta) - k _ {2} \dot {\theta}$$

包含稳态分量 $T_{\mathrm{ss}} = (a/c) \sin \delta$ 和反馈分量 -Kx，前者将 $\theta$ 的平衡值 $\theta_{ss}$ 指定到期望的角度 $\delta$ ，后者使 A - BK 为赫尔维茨矩阵。当两个分量的计算都依赖于系统参数时，可以把反馈部分设计为对较大范围参数扰动的鲁棒设计，特别是当已知 a/c 的上界，即 $a/c \leqslant \rho$ 时，可以选择 $k_{1}$ 和 $k_{2}$ ，使其满足 $k_{1} > \rho, \quad k_{2} > 0$

以保证 A-BK 为赫尔维茨矩阵。另一方面， $T_{ss}$ 的计算对参数扰动是敏感的。假设分别用 a 和 c 的标称值 $a_{0}$ 和 $c_{0}$ 计算 $T_{ss}$ ，则闭环系统的平衡点为

$$a \sin \theta_ {\mathrm{ss}} = c \left[ \frac {a _ {0}}{c _ {0}} \sin \delta - k _ {1} (\theta_ {\mathrm{ss}} - \delta) \right]$$

如果 $\delta=0$ 或 $\delta=\pi$ (即单摆在开环平衡点之一是稳定的) 时 $T_{ss}=0$ ，则由前面的方程可得 $\theta_{ss}=\delta$ 。在这种情况下，用于例 12.2 的方法对于参数扰动是鲁棒的。对于其他 $\delta$ 值，稳态角度的误差是不可接受的。例如，如果 $\delta=45^{\circ}, c=c_{0}/2$ (质量加倍)， $a=a_{0}, k_{1}=3a_{0}/c_{0}$ ，则有 $\theta_{ss}\approx36^{\circ}$ 。

本节将给出一种积分控制方法,这种方法能保证在所有参数扰动下实现渐近调节,只要参数扰动不至于破坏闭环系统的稳定性。积分控制的应用既不局限于线性,也不局限于运用线性化设计反馈控制器。本节提出对一般非线性系统的积分控制方法,下一节将说明如何把线性化用于设计反馈控制器。

考虑系统

$$\dot {x} = f (x, u, w) \tag {12.13}y = h (x, w) \tag {12.14}y _ {m} = h _ {m} (x, w) \tag {12.15}$$

其中 $x \in R^n$ 是状态变量, $u \in R^p$ 是控制输入, $y \in R^p$ 是受控输出, $y_m \in R^m$ 是测得的输出, $w \in R^l$ 是由未知恒定参数以及扰动组成的向量, 函数 $f, h$ 和 $h_m$ 在定义域 $D_x \times D_u \times D_w \subset R^n \times R^p \times R^l$ 上对 $(x, u)$ 连续可微, 且对 $w$ 是连续的。设 $r \in D_r \subset R^p$ 是恒定参考值并可在线测得, 设定

$$
v = \left[ \begin{array}{l} r \\ w \end{array} \right] \in D _ {v} \stackrel {\mathrm{def}} {=} D _ {r} \times D _ {w}
$$

希望设计的反馈控制器能够使 $y(t)\to r$ 当 $t\to \infty$

假设 $y$ 可测，即 $y$ 是 $y_{m}$ 的子集，通过在平衡点 $y = r$ 处稳定系统来实现调节。为此，假设对于每个 $v \in D_v$ ，存在一个连续地取决于 $v$ 的唯一对 $(x_{\mathrm{ss}}, u_{\mathrm{ss}})$ ，满足方程

$$0 = f (x _ {\mathrm{ss}}, u _ {\mathrm{ss}}, w) \tag {12.16}r = h \left(x _ {\mathrm{ss}}, w\right) \tag {12.17}$$

使得 $x_{\mathrm{ss}}$ 为期望的平衡点， $u_{\mathrm{ss}}$ 为稳态控制，以保持系统在点 $x_{\mathrm{ss}}$ 平衡。为引入积分作用，我们对调节误差 $e = \gamma -r$ 进行积分 $\dot{\sigma} = e$

然后把积分器和状态方程(12.13)一起讨论,即

$$\dot {x} = f (x, u, w) \tag {12.18}\dot {\sigma} = h (x, w) - r \tag {12.19}$$
