# (2) 末端自由时的离散极小值原理

如果离散系统末端自由,则离散极小值原理的形式如下,其证明过程类似于定理10-13。读者不妨自行推证。

定理 10-14 设离散系统状态差分方程为

$$
\begin{array}{l} \boldsymbol {x} (k + 1) = \boldsymbol {f} [ \boldsymbol {x} (k), \boldsymbol {u} (k), k ], \quad \boldsymbol {x} (0) = \boldsymbol {x} _ {0} \\ (k = 0, 1, \dots , N - 1) \\ \end{array}
$$

性能指标

$$J = \varphi [ x (N) ] + \sum_ {k = 0} ^ {N - 1} L [ x (k), u (k), k ]$$

式中，N 固定，末端状态 $x(N)$ 自由，其余假设同定理 10-13。

若 $u^{*}(k)$ 是使性能指标为极小的最优控制序列， $x^{*}(k)$ 为相应的最优轨线序列，则必存在 $n$ 维向量序列 $\lambda(k)$ ，使得最优解满足如下必要条件：

1) $x(k)$ 和 $\lambda(k)$ 满足下列差分方程：

$$\pmb {x} (k + 1) = \frac {\partial H (k)}{\partial \pmb {\lambda} (k + 1)}, \qquad \pmb {\lambda} (k) = \frac {\partial H (k)}{\partial \pmb {x} (k)}$$

式中，离散哈密顿函数

$$
\begin{array}{l} H (k) \triangleq H [ x (k), u (k), \lambda (k), k ] \\ = L [ \boldsymbol {x} (k), \boldsymbol {u} (k), k ] + \lambda^ {\mathrm{T}} (k + 1) f [ \boldsymbol {x} (k), \boldsymbol {u} (k), k ] \\ \end{array}
$$

2) 边界条件与横截条件

$$\boldsymbol {x} (0) = \boldsymbol {x} _ {0}, \quad \boldsymbol {\lambda} (N) = \frac {\partial \varphi}{\partial \boldsymbol {x} (N)}$$

3) 离散哈密顿函数对最优控制序列取极小值

$$H ^ {*} (k) = \min _ {u (k) \in \Omega} H (k)$$

若控制变量不受约束，则极值条件为

$$\frac {\partial H (k)}{\partial \boldsymbol {u} (k)} = \mathbf {0}$$

上述定理 10-13 及定理 10-14 表明, 离散系统最优化问题归结为求解一个离散两点边值问题, 且使离散性能指标泛函为极小与使离散哈密顿函数为极小是等价的。

例 10-10 设离散系统状态方程为

$$
\boldsymbol {x} (k + 1) = \left[ \begin{array}{c c} 1 & 0. 1 \\ 0 & 1 \end{array} \right] \boldsymbol {x} (k) + \left[ \begin{array}{c} 0 \\ 0. 1 \end{array} \right] \boldsymbol {u} (k)
$$

已知边界条件

$$
\boldsymbol {x} (0) = \left[ \begin{array}{l} 1 \\ 0 \end{array} \right], \quad \boldsymbol {x} (2) = \left[ \begin{array}{l} 0 \\ 0 \end{array} \right]
$$

试用离散极小值原理求最优控制序列,使性能指标

$$J = 0. 0 5 \sum_ {k = 0} ^ {1} u ^ {2} (k)$$

取极小值，并求出最优轨线序列。

解 本例为控制无约束, N 固定, 末端固定的离散最优控制问题。构造离散哈密顿函数

$$H (k) = 0. 0 5 u ^ {2} (k) + \lambda_ {1} (k + 1) [ x _ {1} (k) + 0. 1 x _ {2} (k) ] + \lambda_ {2} (k + 1) [ x _ {2} (k) + 0. 1 u (k) ]$$

式中， $\lambda_{1}(k + 1)$ 和 $\lambda_{2}(k + 1)$ 为待定拉格朗日乘子序列。

由协态方程，有

$$\lambda_ {1} (k) = \frac {\partial H (k)}{\partial x _ {1} (k)} = \lambda_ {1} (k + 1)\lambda_ {2} (k) = \frac {\partial H (k)}{\partial x _ {2} (k)} = 0. 1 \lambda_ {1} (k + 1) + \lambda_ {2} (k + 1)$$

所以 $\lambda_1(0) = \lambda_1(1),\quad \lambda_2(0) = 0.1\lambda_1(1) + \lambda_2(1)$

$$\lambda_ {1} (1) = \lambda_ {1} (2), \quad \lambda_ {2} (1) = 0. 1 \lambda_ {1} (2) + \lambda_ {2} (2)$$

由极值条件
