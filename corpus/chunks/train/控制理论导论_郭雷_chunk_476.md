# 6.9 $H_{\infty}$ 控制器的直接设计方法

前面介绍的非线性系统 $H_{\infty}$ 控制器的设计方法, 都是通过求解Hamilton-Jacobi偏微分不等式来得到理想的控制器的. 应该指出, 求解这些Hamilton-Jacobi不等式的解, 并非是一件简单的事情. 到目前为止, 在数学上尚未有求解Hamilton-Jacobi不等式的一般方法. 因此在实际应用时, 我们还要借助于近似求解手段来得到控制器.

另一方面，回顾上述定理的证明过程可知，实际上Hamilton-Jacobi偏微分不等式的解给出了保证系统的 $\gamma-$ 耗散性的能量存储函数。系统的 $L^2$ 增益条件是根据 $\gamma-$ 耗散性间接得到保证的。因此回避求解Hamilton-Jacobi不等式的一个可能的途径就是直接构造能量存储函数。由于 $\gamma-$ 耗散性反映了一种广义的能量耗损概念，因此对于许多实际系统来讲，我们有可能通过描述系统所具有的真正的物理能量的函数来直接构造保证系统 $\gamma-$ 耗散性的存储函数，从而得到满足 $L^2$ 增益要求的控制器。

本节简要介绍这种直接构造存储函数的设计方法。首先我们来观察一个简单的力学系统。

例6.9.1 考察一个在外力 $u$ 作用下，沿 $x$ 方向做直线运动的质点 $m$ (以下用 $m$ 和 $x$ 分别代表其质量和位移). 设该质点的弹性和黏性阻尼系数分别为 $k$ 和 $f$ . 于是该系统的运动方程为

$$m \ddot {x} = u - f \dot {x} - k x, \tag {6.9.1}$$

而该系统在状态 $x(t), \dot{x}(t)$ 所具有的能量为

$$V (x, \dot {x}) = \frac {1}{2} k x ^ {2} (t) + \frac {1}{2} m \dot {x} ^ {2} (t), \tag {6.9.2}$$

其中第一项为势能，第二项为动能.

设该系统的输出为 $y = \dot{x}$ ，则沿该系统的状态轨迹有

$$
\begin{array}{l} \dot {V} = k x \dot {x} + m \dot {x} \ddot {x} \\ = k x \dot {x} + \dot {x} (u - f \dot {x} - k x) \\ = - \frac {1}{2} y ^ {2} + y u - \left(f - \frac {1}{2}\right) y ^ {2} (6.9.3) \\ = \frac {1}{2} \left(\frac {1}{2 f - 1} u ^ {2} - y ^ {2}\right) - \left(\frac {u}{\sqrt {4 f - 2}} - \sqrt {f - \frac {1}{2}} y\right) ^ {2}, (6.9.4) \\ \end{array}
$$

即对于满足 $\gamma^2 \leqslant (2f - 1)^{-1}$ 的 $\gamma > 0$ , 有

$$\dot {V} \leqslant \frac {1}{2} (\gamma^ {2} u ^ {2} - y ^ {2}). \tag {6.9.5}$$

因此该系统由输入 $u$ 到输出 $y$ 具有小于 $\gamma (\leqslant 1 / \sqrt{2f - 1})$ 的 $L^2$ 增益.

上述例子表明，根据描述力学系统能量总和的函数 $V(x, \dot{x})$ ，我们可以判定该系统具有小于 $\gamma$ 的 $L^2$ 增益，而不必判断对应的 Hamilton-Jacobi 不等式或 Riccati 不等式是否有解。因此在实际应用中，如果我们能够找到这样的能量函数的话，就可以直接构造 $H_\infty$ 控制器。

首先我们考虑一个简单的情况，设广义受控对象为

$$
\left\{ \begin{array}{l} \dot {\eta} = f (\eta) + f _ {1} (\eta , y) y, \\ \dot {y} = p (\eta , y) w + u. \\ z = h _ {0} (\eta , y) y. \end{array} \right. \tag {6.9.6}
$$

该系统的状态变量为 $(\eta, y)$ . 如果当 $y = 0$ 时，该系统的 $\eta-$ 子系统

$$\dot {\eta} = f (\eta)$$

在 $\eta = 0$ 是渐近稳定的，那么根据 Lyapunov 逆定理 (参见文献 [10]), 存在正定函数 $W(\eta) \geqslant 0$ ( $W(0) = 0$ ) 满足

$$\frac {\partial W}{\partial \eta} f (\eta) < 0, \quad \forall \eta \neq 0. \tag {6.9.7}$$

如果我们定义正定函数

$$V (\eta , y) = W (\eta) + \frac {1}{2} y ^ {\mathrm{T}} y, \tag {6.9.8}$$

则沿系统状态轨迹有
