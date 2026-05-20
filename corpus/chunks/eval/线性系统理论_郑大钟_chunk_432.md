# 11.8 线性二次型调节器问题的频域综合

线性二次型调节器问题简称为LQ问题，是相对于一个线性受控系统（L）和相对于其状态及控制的一个二次型性能指标（Q)，来确定使性能指标取极小值的最优控制律的一类综合问题。在第5章中，我们采用状态空间法讨论过这类问题，给出了最优控制律的状态空间表达式及其基本特性。这一节中，我们将从复频率域方法的角度来研究LQ问题，给出其最优控制律的频域综合方法。并且，作为进一步讨论的基础，首先要对LQ问题的提法和状态空间法的分析结果作一简要的回顾。

LQ 问题的提法和状态空间法的分析结果 给定受控系统的状态方程和二次型性能指标:

$$\dot {\boldsymbol {x}} = A \boldsymbol {x} + B \boldsymbol {u}, \boldsymbol {x} (0) = \boldsymbol {x} _ {0} \tag {11.251}J = \int_ {0} ^ {\infty} [ \boldsymbol {x} ^ {T} Q \boldsymbol {x} + \boldsymbol {u} ^ {T} R \boldsymbol {u} ] d t \tag {11.252}$$

其中， $\pmb{x}$ 和 $\pmb{u}$ 分别为 $n$ 维状态向量和 $p$ 维控制向量， $A$ 和 $B$ 是相应维数的常数矩阵， $R = R^T > 0$ （正定）， $Q = Q^T \geqslant 0$ （正半定）。LQ 问题的综合目标是要寻求一个控制律 $\pmb{u}^*$ 和其作用下的相应状态轨线 $\pmb{x}^*$ ，使得相对于 $\{\pmb{x}^*, \pmb{u}^*\}$ 成立：

$$
\begin{array}{l} J ^ {*} = \int_ {0} ^ {\infty} \left[ x ^ {* T} Q x ^ {*} + u ^ {* T} R u ^ {*} \right] d t \\ = \min _ {u} \int_ {0} ^ {\infty} [ \boldsymbol {x} ^ {T} Q \boldsymbol {x} + \boldsymbol {u} ^ {T} R \boldsymbol {u} ] d t \tag {11.253} \\ \end{array}
$$

并且，称 $u^{*}$ 为最优控制， $x^{*}$ 为最优轨线。

采用状态空间法的分析表明,对给定的 LQ 问题,如果 $(A,B)$ 为能控, $(A,C)$ 为能观测 $(Q=C^{T}C,C\in\mathcal{R}^{q\times n})$ ,则最优控制 $u^{*}$ 存在且唯一具有如下的形式

$$\boldsymbol {u} ^ {*} = - K ^ {*} \boldsymbol {x} ^ {*} (t), K ^ {*} = R ^ {- 1} B ^ {T} P \tag {11.254}$$

而最优性能值为

$$J ^ {*} = \boldsymbol {x} _ {o} ^ {T} P \boldsymbol {x} _ {o} \tag {11.255}$$

其中 $P$ 为下述黎卡提（Riccati）代数方程的正定解阵：

$$P A + A ^ {T} P + Q - P B R ^ {- 1} B ^ {T} P = 0 \tag {11.256}$$

状态空间域 LQ 问题的频域求解 现在,我们采用复频率域方法来求解由(11.251)和(11.252)所描述的状态空间域 LQ 问题。对此,有如下的一些结论。

结论 1 给定由(11.251)和(11.252)所描述的 LQ 问题,定义如下的增广矩阵

$$
M \triangleq \left[ \begin{array}{c c} A & - B R ^ {- 1} B ^ {T} \\ - C ^ {T} C & - A ^ {T} \end{array} \right] \in \mathcal {R} ^ {2 n} \tag {11.257}
$$

则在实现最优时系统的最优特征值即为代数方程

$$\det (s I - M) = 0 \tag {11.258}$$

的位于左半开复平面上的 n 个根。

证 对给定 LQ 问题(11.251)和(11.252)，可采用欧拉-拉格朗日（Euler-Lagrange）方法来推导其最优控制。为此，先构成如下的哈密顿（Hamilton）函数：

$$
\begin{array}{l} H (\boldsymbol {x}, \boldsymbol {u}, \lambda) = 1 / 2 \left(\boldsymbol {x} ^ {T} Q \boldsymbol {x} + \boldsymbol {u} ^ {T} R \boldsymbol {u}\right) + \lambda^ {T} (A \boldsymbol {x} + B \boldsymbol {u}) \\ = 1 / 2 \left(x ^ {T} C ^ {T} C x + u ^ {T} R u\right) + \lambda^ {T} (A x + B u) \tag {11.259} \\ \end{array}
$$

其中， $\lambda^{T}$ 为 n 维行向量，称为拉格朗日乘子向量或协状态。进而，有
