# 线性系统二次最优控制形式，存在及唯一性

线性二次最优控制中，其状态方程、初始条件、控制值域、目标集和性能指标分别为

$$\dot {x} = A (t) x + B (t) u, \quad x (t _ {0}) = x _ {0}, \tag {7.3.1}\mathbb {U} _ {r} = \mathbb {R} ^ {n}, \tag {7.3.2}\mathcal {S} = \mathbb {R} ^ {n} (\text { 即终端状态不受约束 }), \tag {7.3.3}J [ u ] = \frac {1}{2} x ^ {\mathrm{T}} (t _ {f}) F x (t _ {f}) + \frac {1}{2} \int_ {t _ {0}} ^ {t _ {f}} \left[ x ^ {\mathrm{T}} (t) Q (t) x (t) + u ^ {\mathrm{T}} (t) R (t) u (t) \right] \mathrm{d} t, \tag {7.3.4}$$

其中 $x(t) \in \mathbb{R}^n, u(t) \in \mathbb{U}_r$ ； $A(t) \in \mathbb{R}^{n \times n}, B(t) \in \mathbb{R}^{n \times r}, Q(t) \in \mathbb{R}^{n \times n}, R(t) \in \mathbb{R}^{r \times r}$ ，其元皆是定义在 $[t_0, t_f]$ 上的连续（或分段连续）函数， $Q(t)$ 和 $R(t)$ 分别是半正定和正定对称矩阵 $\forall t \in [t_0, t_f]$ ，简记为 $Q(t) \geqslant 0$ 和 $R(t) > 0, F$ 为 $n \times n$ 半正定常值阵， $t_0 < t_f, t_f$ 固定。

最优控制问题 (7.3.1)\~(7.3.4) 简称线性二次最优控制问题.

现在我们利用7.1节中控制不受约束的极大值原理来寻求二次最优控制问题解的形式。式(7.3.1)和式(7.3.4)的Hamilton函数 $H(x,u,\psi ,t)$ 为

$$H (x, u, \psi , t) = - \frac {1}{2} \left[ x ^ {\mathrm{T}} Q (t) x + u ^ {\mathrm{T}} R (t) u \right] + \psi^ {\mathrm{T}} A (t) x + \psi^ {\mathrm{T}} B (t) u. \tag {7.3.5}$$

根据极大值原理，从 $\frac{\partial H}{\partial u} = -u^{\mathrm{T}}R(t) + \dot{\psi}^{\mathrm{T}}B(t)u = 0$ 得到

$$u = R ^ {- 1} (t) B ^ {\mathrm{T}} (t) \psi , \tag {7.3.6}$$

且有

$$\frac {\partial^ {2} H}{\partial u ^ {2}} = - R (t) < 0, \quad \forall t \in [ t _ {0}, t _ {f} ]. \tag {7.3.7}$$

将式 (7.3.6) 代入式 (7.3.1) 中，得到

$$
\left\{ \begin{array}{l} \dot {x} = A (t) x + B (t) R ^ {- 1} (t) B ^ {\mathrm{T}} (t) \psi , \\ \dot {\psi} = Q (t) x - A ^ {\mathrm{T}} (t) \psi , \\ x \left(t _ {0}\right) = x _ {0}, \quad \psi \left(t _ {f}\right) = - F \cdot x \left(t _ {f}\right). \end{array} \right. \tag {7.3.8}
$$

从方程 (7.3.8) 易得

$$\psi (t) = - P (t) x (t), \quad \forall t \in [ t _ {0}, t _ {f} ], \tag {7.3.9}$$

其中 $P(t)$ 为待定 $n \times n$ 矩阵函数.

对式 $(7.3.9)$ 两端求导，并利用式 $(7.3.8)$ 容易得到

$$\left[ \dot {P} (t) + P (t) A (t) + A ^ {\mathrm{T}} (t) P (t) + Q (t) - P (t) B (t) R ^ {- 1} (t) B ^ {\mathrm{T}} (t) P (t) \right] x (t) = 0.$$

由于上式对任意 $x(t)$ 皆成立，从而 $P(t)$ 满足带终端条件的Riccati矩阵微分方程

$$
\left\{ \begin{array}{l} - \dot {P} (t) = P (t) A (t) + A ^ {\mathrm{T}} (t) P (t) + Q (t) - P (t) B (t) R ^ {- 1} (t) B ^ {\mathrm{T}} (t) P (t), \\ P \left(t _ {f}\right) = F. \end{array} \right. \tag {7.3.10}
$$

在 $A(t), B(t), Q(t), R(t)$ 和 $F$ 的假设下，易知，方程 (7.3.10) 在区间 $[t_0, t_f]$ 上存在唯一对称解矩阵 $P(t)$ . 于是，如果式 (7.3.1) 和式 (7.3.4) 的最优解 $(u^*(t), x^*(t))$ 在 $[t_0, t_f]$ 上存在，则 $u^*(t)$ 能表示为

$$u ^ {*} (t) = - R ^ {- 1} (t) B ^ {\mathbf {T}} (t) P (t) x ^ {*} (t). \tag {7.3.11}$$
