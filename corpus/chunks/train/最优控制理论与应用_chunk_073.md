# 4.5 离散系统的极小值原理

在现实世界中有些系统本身是离散的,要用离散的状态方程来加以描述。有些系统本身虽是连续的,但采用计算机控制,控制量只在离散的时刻算出来,设计这类系统时,连续对象的状态方程要进行离散化。下面就来讨论离散系统的极小值原理。问题的提法如下：

系统的状态方程为

$$\boldsymbol {X} (k + 1) = \boldsymbol {f} [ \boldsymbol {X} (k), \boldsymbol {U} (k), k ] \quad k = 0, 1, \dots , N - 1 \tag {4-86}$$

$X(k)$ 为 $n$ 维向量， $U(k)$ 为 $m$ 维向量。上式右端在一般情况下是 $X(k)$ 和 $U(k)$ 的非线性函数。

初始条件为

$$\boldsymbol {X} (0) = \boldsymbol {X} _ {0} \tag {4-87}$$

终端约束为

$$\boldsymbol {G} [ \boldsymbol {X} (N), N ] = \mathbf {0} \tag {4-88}$$

G 是 q 维向量方程。

性能指标为

$$J = \phi [ X (N), N ] + \sum_ {k = 0} ^ {N - 1} F [ X (k), U (k), k ] \tag {4-89}$$

要求确定控制序列 $U(k), k=0,1,\cdots,N-1$ ，使 J 最小。下面按控制向量 $U(k)$ 受约束和不受约束两种情况来讨论。

(1) 控制向量无约束。这时可用古典变分法求解。作增广性能指标

$$
\begin{array}{l} J _ {\mathrm{s}} = \phi [ X (N), N ] + \sum_ {k = 0} ^ {N - 1} F [ X (k), U (k), k ] + \\ \boldsymbol {\lambda} ^ {T} (k + 1) \left\{\boldsymbol {f} [ \boldsymbol {X} (k), \boldsymbol {U} (k), k ] - \boldsymbol {X} (k + 1) \right\} + \\ \boldsymbol {v} ^ {\mathrm{T}} \boldsymbol {G} [ \boldsymbol {X} (N), N ] \tag {4-90} \\ \end{array}
$$

式中， $\boldsymbol{\lambda}(k+1)$ 是协态向量(n维)，v是拉格朗日乘子向量(q维)。

引入下面的哈密顿函数

$$
\begin{array}{l} H (X, U, \lambda , k) = F [ X (k), U (k), k ] + \\ \boldsymbol {\lambda} ^ {\mathrm{T}} (k + 1) \boldsymbol {f} [ \boldsymbol {X} (k), \boldsymbol {U} (k), k ] \tag {4-91} \\ \end{array}
$$

并令

$$\theta [ \boldsymbol {X} (N), N ] = \phi [ \boldsymbol {X} (N), N ] + \boldsymbol {v} ^ {\mathrm{T}} \boldsymbol {G} [ \boldsymbol {X} (N), N ] \tag {4-92}$$

则

$$
\begin{array}{l} J _ {\mathrm{a}} = \theta [ \boldsymbol {X} (N), N ] + \sum_ {k = 0} ^ {N - 1} [ H (\boldsymbol {X}, \boldsymbol {U}, \boldsymbol {\lambda}, k) - \boldsymbol {\lambda} ^ {\mathrm{T}} (k + 1) \boldsymbol {X} (k + 1) ] \\ = \theta [ \boldsymbol {X} (N), N ] - \boldsymbol {\lambda} ^ {T} (N) \boldsymbol {X} (N) + \boldsymbol {\lambda} ^ {T} (0) \boldsymbol {X} (0) + \\ \sum_ {k = 0} ^ {N - 1} \left[ H (\boldsymbol {X}, \boldsymbol {U}, \boldsymbol {\lambda}, k) - \boldsymbol {\lambda} ^ {\mathrm{T}} (k) \boldsymbol {X} (k) \right] \tag {4-93} \\ \end{array}
$$

$J_{a}$ 的一次变分可写成
