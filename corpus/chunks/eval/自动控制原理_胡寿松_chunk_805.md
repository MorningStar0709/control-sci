# (1) 末端约束时的离散极小值原理

定理 10-13 设离散系统状态差分方程为

$$\boldsymbol {x} (k + 1) = f [ \boldsymbol {x} (k), \boldsymbol {u} (k), k ], \quad \boldsymbol {x} (0) = \boldsymbol {x} _ {0} \tag {10-64}(k = 0, 1, \dots , N - 1)$$

性能指标

$$J = \varphi [ \boldsymbol {x} (N) ] + \sum_ {k = 0} ^ {N - 1} L [ \boldsymbol {x} (k), \boldsymbol {u} (k), k ] \tag {10-65}$$

式中， $N$ 固定； $f(\cdot),\varphi (\cdot)$ 和 $L(\cdot)$ 都是其自变量的连续可微函数； $\pmb {x}(k)\in \mathbf{R}^n;\pmb {u}(k)\in \mathbf{R}^m$ ，其约束 $\pmb {u}(k)\in \Omega ,\Omega$ 为容许控制域。末端状态受下列目标集约束：

$$\psi [ \boldsymbol {x} (N) ] = \mathbf {0} \tag {10-66}$$

式中， $\psi(\cdot) \in \mathbb{R}^r$ 且连续可微， $r \leqslant n$ 。

若 $u^{*}(k)$ 是使性能指标(10-65)为最小的最优控制序列, $x^{*}(k)$ 是相应的最优轨线序列, 则必存在 r 维非零常向量 $\gamma$ 和 n 维向量序列 $\lambda(k)$ , 使得最优解满足如下必要条件:

1) $x(k)$ 和 $\lambda (k)$ 满足差分方程

$$\boldsymbol {x} (k + 1) = \frac {\partial H (k)}{\partial \lambda (k + 1)} \tag {10-67}\boldsymbol {\lambda} (k) = \frac {\partial H (k)}{\partial \boldsymbol {x} (k)} \tag {10-68}$$

式中，离散哈密顿函数

$$
\begin{array}{l} H (k) \triangleq H [ x (k), u (k), \lambda (k), k ] \\ = L [ \boldsymbol {x} (k), \boldsymbol {u} (k), k ] + \lambda^ {\mathrm{T}} (k + 1) f [ \boldsymbol {x} (k), \boldsymbol {u} (k), k ] \tag {10-69} \\ \end{array}
$$

2）边界条件与横截条件

$$\boldsymbol {x} (0) = \boldsymbol {x} _ {0}, \quad \psi [ \boldsymbol {x} (N) ] = \boldsymbol {0}\boldsymbol {\lambda} (N) = \frac {\partial \varphi}{\partial \boldsymbol {x} (N)} + \frac {\partial \boldsymbol {\psi} ^ {\mathrm{T}}}{\partial \boldsymbol {x} (N)} \boldsymbol {\gamma} \tag {10-70}$$

3）离散哈密顿函数对最优控制序列取极小值

$$H ^ {*} (k) = \min _ {u (k) \in \Omega} H (k) \tag {10-71}$$

若 $u(k)$ 无约束，则极值条件为

$$\frac {\partial H (k)}{\partial \boldsymbol {u} (k)} = \mathbf {0} \tag {10-72}$$

证明 引入拉格朗日乘子 $\lambda(k)$ 和 $\gamma$ ，构造离散广义泛函

$$
\begin{array}{l} J _ {a} = \varphi [ x (N) ] + \boldsymbol {\gamma} ^ {T} \psi [ x (N) ] + \sum_ {k = 0} ^ {N - 1} \{L [ x (k), u (k), k ] \\ \left. + \boldsymbol {\lambda} ^ {T} (k + 1) [ f (\boldsymbol {x} (k), \boldsymbol {u} (k), k) - \boldsymbol {x} (k + 1) ] \right\} \tag {10-73} \\ \end{array}
$$

令离散哈密顿函数

$$H (k) = L [ \boldsymbol {x} (k), \boldsymbol {u} (k), k ] + \lambda^ {\mathrm{T}} (k + 1) f [ \boldsymbol {x} (k), \boldsymbol {u} (k), k ]$$

则式(10-73)可表示为
