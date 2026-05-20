下证 (7.3.10) 的唯一对称解 $P(t)$ 的正定性。任意固定 $x_0 \in \mathbb{R}^n$ ，任取 $u(t) \in \mathcal{U}_{[t_0, t_f]}$ ，式 (7.3.1) 对应于 $u(t)$ 在 $t_0$ 时刻以 $x_0$ 为初态的轨线记为 $x(t)$ 。考察表达式 $\frac{1}{2} \frac{\mathrm{d}}{\mathrm{d}t} [x^{\mathrm{T}}(t) P(t) x(t)]$ 。注意到 $P(t), x(t)$ 分别是方程 (7.3.10) 和式 (7.3.1) 的解。不难得到

$$
\begin{array}{l} \frac {1}{2} \frac {\mathrm{d}}{\mathrm{d} t} [ x (t) ^ {\mathrm{T}} P (t) x (t) ] = [ u (t) + R ^ {- 1} (t) B ^ {\mathrm{T}} (t) P (t) x (t) ] ^ {\mathrm{T}} \\ \times R (t) [ u (t) + R ^ {- 1} (t) B ^ {T} (t) P (t) x (t) ] \\ - \frac {1}{2} \left[ x ^ {\mathrm{T}} (t) Q (t) x (t) + u ^ {\mathrm{T}} (t) R (t) u (t) \right]. \\ \end{array}
$$

从 $t_0$ 到 $t_f$ 积分上式两端得到

$$
\begin{array}{l} \frac {1}{2} x ^ {\mathrm{T}} \left(t _ {f}\right) F x \left(t _ {f}\right) + \frac {1}{2} \int_ {t _ {0}} ^ {t _ {f}} \left[ x ^ {\mathrm{T}} (t) Q (t) x (t) + u ^ {\mathrm{T}} (t) R (t) u (t) \right] \mathrm{d} t \\ = \frac {1}{2} x _ {0} ^ {\mathrm{T}} P (t _ {0}) x _ {0} + \int_ {t _ {0}} ^ {t _ {f}} [ u (t) + R ^ {- 1} (t) B ^ {\mathrm{T}} (t) P (t) x (t) ] ^ {\mathrm{T}} R (t) \\ \times \left[ u (t) + R ^ {- 1} (t) B ^ {T} (t) P (t) x (t) \right] d t, \\ \end{array}
$$

即 $\forall u(t) \in \mathcal{U}_{[t_0, t_f]}$ 有

$$
\begin{array}{l} J [ u ] = \frac {1}{2} x _ {0} ^ {\mathrm{T}} P (t _ {0}) x _ {0} + \int_ {t _ {0}} ^ {t _ {f}} [ u (t) + R ^ {- 1} (t) B ^ {\mathrm{T}} (t) P (t) x (t) ] ^ {\mathrm{T}} R (t) \\ \times \left[ u (t) + R ^ {- 1} (t) B ^ {T} (t) P (t) x (t) \right] d t \\ \end{array}
$$

由此可知，使 $J[u]$ 取极小的充分必要条件是 $(u(t), x(t))$ 满足

$$u (t) = - R ^ {- 1} (t) B ^ {\mathrm{T}} (t) P (t) x (t)$$

依关于 $\mathbf{F}, Q(t), R(t)$ 的假设知最优性能指标值 $J[u] > 0$ ，即

$$J [ u ] = \frac {1}{2} x _ {0} ^ {\mathrm{T}} P (t _ {0}) x _ {0} > 0, \quad \forall x _ {0} \neq 0,$$

所以 $P(t_0) > 0$ . 同理可知对任意固定 $\hat{t} \in (t_0, t_f)$ , 皆有 $P(\hat{t}) > 0$ .

所以 $P(t)$ 为定义在 $[t_0, t_f)$ 上的正定对称矩阵。综上所述可得：

定理 7.3.1 对于线性二次最优控制问题 (7.3.1)\~(7.3.4)，其最优控制 $u^{*}(t)$ 存在唯一，并且有式 (7.3.11) 中的形式，其最优控制综合函数 $u^{*}(x,t)$ 为

$$u ^ {*} (x, t) = - R ^ {- 1} (t) B ^ {T} (t) P (t) x. \tag {7.3.16}$$

式(7.3.11)中 $x^{*}(t)$ 是最优闭环系统

$$
\left\{ \begin{array}{l} \dot {x} (t) = A (t) x (t) + B (t) u ^ {*} (x, t), \\ x \left(t _ {0}\right) = x _ {0} \end{array} \right. \tag {7.3.17}
$$

的轨线， $P(t)$ 是带终端点条件的Riccati矩阵微分方程(7.3.10）的唯一正定对称解矩阵.

关系式 (7.3.16) 中的 $r \times n$ 矩阵 $K^{*}(t) = -R^{-1}(t)B^{\mathrm{T}}(t)P(t)$ 称为系统 (7.3.1) 的“最优反馈增益矩阵”.

定理7.3.1的结论对定常线性二次最优控制问题自然成立的，只是此时的最优控制综合函数为

$$\boldsymbol {u} ^ {*} (\boldsymbol {x}, t) = - R ^ {- 1} B ^ {\mathrm{T}} P (t) \boldsymbol {x}. \tag {7.3.18}$$

从定理7.3.1看到，线性二次(有限时间区间上)最优控制问题归结为求方程(7.3.10)的正定对称解矩阵．甚至在定常情况下，一般也不易求得解析解．因此，通常需要利用计算机求解.
