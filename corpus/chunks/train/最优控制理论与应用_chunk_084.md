# 5.3.2 矩阵黎卡提微分方程的求解及 $K(t)$ 的性质

1. 矩阵黎卡提微分方程是非线性的,一般不能求得闭合形式的解。在数字机上求解时,可用一阶差分代替微分

$$\frac {\mathrm{d} \boldsymbol {K} (t)}{\mathrm{d} t} = \lim _ {\Delta t \rightarrow 0} \frac {\boldsymbol {K} (t + \Delta t) - \boldsymbol {K} (t)}{\Delta t}$$

于是可用下面的差分方程来近似黎卡提微分方程

$$\boldsymbol {K} (t + \Delta t) \approx \boldsymbol {K} (t) + \Delta t \{- \boldsymbol {K} (t) \boldsymbol {A} (t) - \boldsymbol {A} ^ {\mathrm{T}} (t) \boldsymbol {K} (t) +\boldsymbol {K} (t) \boldsymbol {B} (t) \boldsymbol {R} ^ {- 1} (t) \boldsymbol {B} ^ {\mathrm{T}} (t) \boldsymbol {K} (t) - \boldsymbol {Q} (t) \} \tag {5-17}$$

求解上式时，以 $K(t_{\mathrm{f}})=P$ 为初始条件， $\Delta t$ 取为负的小量，从 $t_{f}$ 到 $t_{0}$ 逆时间递推计算，即可求出 $K(t)$ 。

2. $K(t)$ 是对称矩阵, 即 $K(t) = K^{\mathrm{T}}(t)$ 。这可证明如下: 因为 P、 $Q(t)$ 、 $R(t)$ 都是对称的, 将式 (5-14) 转置一下, 可得

$$[ \dot {\boldsymbol {K}} (t) ] ^ {\mathrm{T}} = \dot {\boldsymbol {K}} ^ {\mathrm{T}} (t) = - \boldsymbol {K} ^ {\mathrm{T}} (t) \boldsymbol {A} (t) - \boldsymbol {A} ^ {\mathrm{T}} (t) \boldsymbol {K} ^ {\mathrm{T}} (t) +\boldsymbol {K} ^ {\mathrm{T}} (t) \boldsymbol {B} (t) \boldsymbol {R} ^ {- 1} (t) \boldsymbol {B} ^ {\mathrm{T}} (t) \boldsymbol {K} ^ {\mathrm{T}} (t) - \boldsymbol {Q} (t)$$

因此 $\pmb{K}^{\mathrm{T}}(t)$ 和 $\pmb{K}(t)$ 一样满足同一黎卡提方程，并且边界条件一样，即

$K^{\mathrm{T}}(t_{\mathrm{f}}) = P = K(t_{\mathrm{f}})$ 。于是，由微分方程解的唯一性可知

$$\boldsymbol {K} ^ {\mathrm{T}} (t) = \boldsymbol {K} (t)$$

利用这个对称性, 求 $n \times n$ 维 $K(t)$ 的元时, 只需积分 $\frac{n(n+1)}{2}$ 个方程即可。

3. 即使系统是定常的, 即系统矩阵 A, 输入矩阵 B 为常数阵, 加权阵 Q 和 R 也是常数阵, 但 $K(t)$ 仍为时变阵。这从 $K(t)$ 是黎卡提微分方程的解可看出。 $K(t)$ 时变时, 反馈控制增益也时变, 在实现时总是不太方便。下一段将看到, 对线性定常系统, 若终端时间 $t_{f} \to \infty$ , 且系统满足一些附加条件时, $K(t)$ 将变为常数阵 K。

例5-1 设系统状态方程为

$$\dot {x} _ {1} = x _ {2} \quad x _ {1} (0) = 1 \tag {5-18}\dot {x} _ {2} = u \quad x _ {2} (0) = 0$$

寻找最优控制 $u(t)$ 使下面的性能指标

$$J = \frac {1}{2} \int_ {0} ^ {t _ {\mathrm{f}}} \left[ x _ {1} ^ {2} (t) + u ^ {2} (t) \right] \mathrm{d} t \tag {5-19}$$

为最小。

解 把状态方程式(5-18)和(5-5)相比较,把性能指标式(5-19)和(5-6)相比较,可得

$$
\boldsymbol {A} = \left[ \begin{array}{l l} 0 & 1 \\ 0 & 0 \end{array} \right], \quad \boldsymbol {B} = \left[ \begin{array}{l} 0 \\ 1 \end{array} \right], \quad \boldsymbol {P} = 0, \quad \boldsymbol {Q} = \left[ \begin{array}{l l} 1 & 0 \\ 0 & 0 \end{array} \right], \quad \boldsymbol {R} = 1 \tag {5-20}
$$

考虑到 $K(t)$ 是对称阵, 设
