# 14.1.2 稳定性

考虑系统

$$\dot {x} = f (x) + B (x) [ G (x) E (x) u + \delta (t, x, u) ] \tag {14.1}$$

其中 $x \in R^n$ 为状态, $u \in R^p$ 为控制输入, $f, B, G$ 和 $E$ 为在包含原点的定义域 $D \subset R^n$ 上的充分光滑函数。函数 $\delta$ 对于 $t$ 是分段连续的, 且对于 $(x, u)$ 是充分光滑的, $(t, x, u) \in [0, \infty) \times D \times R^p$ 。假设 $f, B$ 和 $E$ 已知, $G$ 和 $\delta$ 可能不确定, 进一步假设 $E(x)$ 是非奇异矩阵, $G(x)$ 是对角阵, 其元素为大于零的有界值, 即 $g_i(x) \geqslant g_0 > 0 (x \in D)^{①}$ 。假设 $f(0) = 0$ , 则在没有 $\delta$ 的情况下, 原点为开环平衡点。我们的目标是设计一个状态反馈控制律, 使得对于所有 $G$ 和 $\delta$ 的不确定性, 都能使原点稳定。

设 $T: D \rightarrow R^{n}$ 是微分同胚的, 满足

$$
\frac {\partial T}{\partial x} B (x) = \left[ \begin{array}{l} 0 \\ I \end{array} \right] \tag {14.2}
$$

其中 I 为 $p \times p$ 的单位矩阵 $^{②}$ 。进行变量代换

$$
\left[ \begin{array}{l} \eta \\ \xi \end{array} \right] = T (x), \quad \eta \in R ^ {n - p}, \xi \in R ^ {p} \tag {14.3}
$$

系统变换为 $\dot{\eta} = f_{a}(\eta, \xi)$ (14.4)

$$\dot {\xi} = f _ {b} (\eta , \xi) + G (x) E (x) u + \delta (t, x, u) \tag {14.5}$$

方程(14.4)和方程(14.5)通常称为正则形式。要设计滑模控制,首先从设计滑动流形 s = $\xi - \phi(\eta) = 0$ 开始,使得当把运动限制在流形上时,降阶系统

$$\dot {\eta} = f _ {a} (\eta , \phi (\eta)) \tag {14.6}$$

在原点有一个渐近稳定平衡点, $\phi(\eta)$ 的设计归结为求解系统

$$\dot {\eta} = f _ {a} (\eta , \xi)$$

的稳定性问题,上式中把 $\xi$ 看成控制输入。求解该稳定性问题可运用前两章提出的线性化或反馈线性化技术,或运用本章后面将要介绍的一些非线性设计工具,如反步法或基于无源的控制法。假设可以找到一个可使系统稳定的连续可微函数 $\phi(\eta)$ ,且 $\phi(0)=0$ 。然后设计u,使其在有限时间内把s带到零,并在所有未来时刻保持s不变。为此,写出 $\dot{s}$ 方程

$$\dot {s} = f _ {b} (\eta , \xi) - \frac {\partial \phi}{\partial \eta} f _ {a} (\eta , \xi) + G (x) E (x) u + \delta (t, x, u) \tag {14.7}$$

正如在引例中所见， $u$ 可以设计成纯切换分量，或者它可能包含一个附加的连续分量，消去了方程(14.7)右边的已知项①。如果 $\hat{G}(x)$ 是 $G(x)$ 的标称模型，则 $u$ 的连续分量就是 $-E^{-1}\hat{G}^{-1}[f_b - (\partial \phi/\partial \eta)f_a]$ 。在无不确定量时，即 $\delta = 0, G$ 已知，取 $u = -E^{-1}\hat{G}^{-1}[f_b - (\partial \phi/\partial \eta)f_a]$ 可得 $\dot{s} = 0$ ，这样就可以保证在所有未来时刻 $s = 0$ 。为便于同时分析上述两种情况，把控制 $u$ 表示为

$$u = E ^ {- 1} (x) \left\{- L (x) \left[ f _ {b} (\eta , \xi) - \frac {\partial \phi}{\partial \eta} f _ {a} (\eta , \xi) \right] + v \right\} \tag {14.8}$$

其中 $L(x) = \hat{G}^{-1}(x)$ ，否则如果消去已知项，则 $L = 0$ 。将式(14.8)代入方程(14.7)，得

$$\dot {s} _ {i} = g _ {i} (x) v _ {i} + \Delta_ {i} (t, x, v), \quad 1 \leqslant i \leqslant p \tag {14.9}$$

其中 $\Delta_{i}$ 是
