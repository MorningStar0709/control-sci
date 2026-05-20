# 6.3 稳定性与状态空间方程

6.2节讨论了经典控制理论中使用传递函数的极点来判断系统稳定性的方法。本节将分析稳定性与状态空间方程的关系。使用状态空间方程描述线性时不变系统的一般表达式为

$$\frac {\mathrm{d} \boldsymbol {z} (t)}{\mathrm{d} t} = \boldsymbol {A} \boldsymbol {z} (t) + \boldsymbol {B} \boldsymbol {u} (t) \tag {6.3.1a}\mathbf {y} (t) = \mathbf {C z} (t) + \mathbf {D u} (t) \tag {6.3.1b}$$

其中， $z(t)$ 是状态变量， $y(t)$ 是系统的输出， $u(t)$ 是系统的输入，矩阵 A 是状态矩阵，矩阵 B

是输入矩阵,矩阵 C 是输出矩阵,矩阵 D 是直接传递矩阵。

如式(6.3.1b)所示,系统的输出 $y(t)$ 是状态变量 $z(t)$ 与输入 $u(t)$ 的线性组合,如果系统的状态变量和输入都有界,那么系统的输出也是有界的(符合李雅普诺夫意义下的稳定性)。所以在讨论稳定性的时候,可以直接分析式(6.3.1a)。

首先考虑0输入状态，即 $u(t) = 0$ 。在3.3节中详细分析了状态矩阵 $\mathbf{A}$ 的特征值与平衡点类型之间的关系，这一结论可以直接和系统的稳定性结合起来。回顾3.3.3节二维系统相轨迹并对照6.1.2节中稳定性的定义，如果 $\mathbf{A}$ 是一个二维矩阵，那么其特征值与稳定性的关系见表6.3.1。

表 6.3.1 状态矩阵 $A$ 的特征值与稳定性

<table><tr><td> $\lambda_{1,2}=\sigma\pm\omega j$ </td><td colspan="2">特征值  $\lambda_1,\lambda_2$  分类与说明</td><td>平衡点类型</td><td>稳定性分析</td></tr><tr><td rowspan="3">特征值为实数(ω=0)</td><td> $\lambda_1\lambda_2>0$  且  $\lambda_1+\lambda_2<0$ </td><td> $\lambda_1$  和  $\lambda_2$  都为负数</td><td>稳定节点</td><td>渐近稳定</td></tr><tr><td> $\lambda_1\lambda_2<0$ </td><td> $\lambda_1$  和  $\lambda_2$  一正一负</td><td>鞍点</td><td>不稳定</td></tr><tr><td> $\lambda_1\lambda_2>0$  且  $\lambda_1+\lambda_2>0$ </td><td> $\lambda_1$  和  $\lambda_2$  都为正数</td><td>不稳定节点</td><td>不稳定</td></tr><tr><td rowspan="3">特征值为复数(ω≠0)</td><td> $\lambda_{1,2}=\pm\omega j$ </td><td>特征值为纯虚数</td><td>中心点</td><td>李雅普诺夫意义下的稳定</td></tr><tr><td> $\lambda_{1,2}=\sigma\pm\omega j(\sigma>0)$ </td><td>实部大于0</td><td>不稳定焦点</td><td>不稳定</td></tr><tr><td> $\lambda_{1,2}=\sigma\pm\omega j(\sigma<0)$ </td><td>实部小于0</td><td>稳定焦点</td><td>渐近稳定</td></tr></table>

上述分析方法可以推广到更高维度的状态矩阵中。对于 $n$ 维向量 $\mathbf{z}(t)$ ，首先令 $\mathbf{z}(t) = \mathbf{P}\overline{\mathbf{z}}(t)$ ，其中， $\mathbf{P}$ 是过渡矩阵，由矩阵 $\mathbf{A}$ 的特征向量组成。可得

$$
\frac {\mathrm{d} \overline {{{z}}} (t)}{\mathrm{d} t} = \left[ \begin{array}{c c c} \lambda_ {1} & \dots & 0 \\ \vdots & \ddots & \vdots \\ 0 & \dots & \lambda_ {n} \end{array} \right] \overline {{{z}}} (t) \tag {6.3.2}
$$

其中， $\lambda_{i}$ 代表 $\mathbf{A}$ 的特征值，由式(6.3.2)可得
