$$c _ {1} \| \eta \| _ {2} ^ {2} \leqslant V _ {1} (\eta) \leqslant c _ {2} \| \eta \| _ {2} ^ {2}, \quad \frac {\partial V _ {1}}{\partial \eta} f _ {0} (\eta , 0) \leqslant - c _ {3} \| \eta \| _ {2} ^ {2}, \quad \left\| \frac {\partial V _ {1}}{\partial \eta} \right\| _ {2} \leqslant c _ {4} \| \eta \| _ {2}$$

以 $V(z) = bV_{1}(\eta) + \xi^{\mathrm{T}}P\xi ,b > 0$ ，作为系统(13.44）～（13.45）的备选李雅普诺夫函数，得

$$
\begin{array}{l} \dot {V} = b \frac {\partial V _ {1}}{\partial \eta} f _ {0} (\eta , 0) + b \frac {\partial V _ {1}}{\partial \eta} [ f _ {0} (\eta , \xi) - f _ {0} (\eta , 0) ] \\ + \xi^ {T} [ P (A - B K) + (A - B K) ^ {T} P ] \xi + 2 \xi^ {T} P B \delta (z) \\ \leqslant - b c _ {3} \| \eta \| _ {2} ^ {2} + b c _ {4} L \| \eta \| _ {2} \| \xi \| _ {2} - \| \xi \| _ {2} ^ {2} + 2 k \| P B \| _ {2} \| \xi \| _ {2} ^ {2} + 2 k \| P B \| _ {2} \| \xi \| _ {2} \| \eta \| _ {2} \\ = - \left[ \begin{array}{c} \| \eta \| _ {2} \\ \| \xi \| _ {2} \end{array} \right] ^ {\mathrm{T}} \left[ \begin{array}{c c} b c _ {3} & - (k \| P B \| _ {2} + b c _ {4} L / 2) \\ - (k \| P B \| _ {2} + b c _ {4} L / 2) & 1 - 2 k \| P B \| _ {2} \end{array} \right] \left[ \begin{array}{c} \| \eta \| _ {2} \\ \| \xi \| _ {2} \end{array} \right] \\ \stackrel {\text { def }} {=} - \left[ \begin{array}{c} \| \eta \| _ {2} \\ \| \xi \| _ {2} \end{array} \right] ^ {\mathrm{T}} Q \left[ \begin{array}{c} \| \eta \| _ {2} \\ \| \xi \| _ {2} \end{array} \right] \\ \end{array}
$$

这里 L 是 $f_{0}$ 关于 $\xi$ 的利普希茨常数。取 b = k，可以验证对于足够小的 k, Q 是正定的。因此，原点是指数稳定的。

在习题13.22至习题13.24中,提出了引理13.4的几种形式。如果 $\dot{\eta} = f_0(\eta, \xi)$ 不是输入-状态稳定的,但 $\dot{\eta} = f_0(\eta, 0)$ 的原点是渐近稳定的,则可以证明引理第一部分局部成立(见习题13.22)。如果 $f(\eta, \xi)$ 是全局利普希茨的,且 $\dot{\eta} = f_0(\eta, 0)$ 的原点是全局指数稳定的,则可以证明引理第二部分全局成立(见习题13.23)。如果 $\dot{\eta} = f_0(\eta, 0)$ 的原点是渐近稳定而非指数稳定的,则可以通过限制 $\delta$ 与 $\eta$ 的关系,证明闭环系统的原点是渐近稳定的(见习题13.24)。

反馈控制 $u = \alpha (x) - \beta (x)K\xi$ 包含一项线性部分 $u = \alpha (x) + \beta (x)v$ 和一个稳定性部分 $v = -K\xi$ 。前面的李雅普诺夫分析说明，稳定部分对于模型不确定性具有某种程度的鲁棒性①。在第14章中将看到通过利用式(13.45)中的扰动项 $B\delta (z)$ 属于输入矩阵 $B$ 的取值空间的结论，可设计稳定部分，使其具有更高阶鲁棒性，这种扰动被认为满足匹配条件。只要 $\delta$ 的上界已知，第14章的方法就能保证对任何 $\delta (z)$ 都具有鲁棒性。

反馈线性化的基本原理是消去系统的非线性项。除了考虑能否消去非线性项、不确定因素的影响和可实现性问题以外，还应检验该基本原理本身，即取消非线性项是明智之举吗？反馈线性化的思想源于数学上的理论分析。我们希望对系统线性化可使之更容易处理，并可运用相对完善的线性控制理论。然而从性能上看，非线性项有“好”与“坏”之分，决定是否用反馈消去非线性项取决于实际问题。下面通过一对例子说明这一点。

例13.19 考虑标量系统

$$\dot {x} = a x - b x ^ {3} + u$$

其中 a 和 b 是正常数。线性化稳定反馈控制可取为

$$u = - (k + a) x + b x ^ {3}, \quad k > 0$$
