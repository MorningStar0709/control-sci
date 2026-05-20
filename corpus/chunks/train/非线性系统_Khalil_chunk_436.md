# 14.3 反步设计法

我们首先讨论积分器反步(integrator backstepping)的特例,考虑系统

$$\dot {\eta} = f (\eta) + g (\eta) \xi \tag {14.49}\dot {\xi} = u \tag {14.50}$$

其中 $[\eta^{\mathrm{T}},\xi]^{\mathrm{T}}\in R^{n + 1}$ 是状态， $u\in R$ 是控制输入，函数 $f:D\to R^n$ 和 $g:D\to R^n$ 在包含原点 $\eta = 0$ 和 $f(0) = 0$ 的定义域 $D\subset R^n$ 上是光滑的①。我们要设计一个状态反馈控制律，以稳定原点 $(\eta = 0,\xi = 0)$ 。假设 $f$ 和 $g$ 都已知，系统可看成两部分的级联，如图14.15(a)所示。第一部分是方程(14.49)， $\xi$ 为输入；第二部分是积分器方程(14.50)。假设方程(14.49)可通过一个光滑的状态反馈控制律 $\xi = \phi (\eta),\phi (0) = 0$ 稳定，即

$$\dot {\eta} = f (\eta) + g (\eta) \phi (\eta)$$

的原点是渐近稳定的。进一步假设已知李雅普诺夫函数 $V(\eta)$ （光滑，正定）满足不等式

$$\frac {\partial V}{\partial \eta} [ f (\eta) + g (\eta) \phi (\eta) ] \leqslant - W (\eta), \quad \forall \eta \in D \tag {14.51}$$

其中 $W(\eta)$ 是正定的。在方程(14.49)的右边同时加减一项 $g(\eta)\phi (\eta)$ ，可得到等价的表达式

$$
\begin{array}{l} \dot {\eta} = [ f (\eta) + g (\eta) \phi (\eta) ] + g (\eta) [ \xi - \phi (\eta) ] \\ \dot {\xi} = u \\ \end{array}
$$

如图 14.15(b) 所示。应用变量代换

$$z = \xi - \phi (\eta)$$

得到系统 $\begin{array}{rcl}\dot{\eta} & = & [f(\eta) + g(\eta)\phi (\eta)] + g(\eta)z\\ \dot{z} & = & u - \dot{\phi} \end{array}$

如图 14.15(c) 所示。从图 14.15(b) 到图 14.15(c) 可认为是通过积分器的“反步” $-\phi(\eta)$ 。由于 f, g 和 $\phi$ 已知，导数 $\dot{\phi}$ 可用下式计算：

$$\dot {\phi} = \frac {\partial \phi}{\partial \eta} [ f (\eta) + g (\eta) \xi ]$$

取 $v = u - \dot{\phi}$ ，系统简化为级联形式

$$
\begin{array}{l} \dot {\eta} = [ f (\eta) + g (\eta) \phi (\eta) ] + g (\eta) z \\ \dot {z} = v \\ \end{array}
$$

该式与本节开始提出的系统非常相似,所不同的是现在的系统当输入为零时,第一部分具有渐近稳定的原点,这一特点将用于 v 的设计中,以稳定整个系统。用

$$V _ {c} (\eta , \xi) = V (\eta) + \frac {1}{2} z ^ {2}$$

作为备选李雅普诺夫函数,可得

$$
\begin{array}{l} \dot {V} _ {c} = \frac {\partial V}{\partial \eta} [ f (\eta) + g (\eta) \phi (\eta) ] + \frac {\partial V}{\partial \eta} g (\eta) z + z v \\ \leqslant - W (\eta) + \frac {\partial V}{\partial \eta} g (\eta) z + z v \\ \end{array}
$$

选择 $v = -\frac{\partial V}{\partial \eta} g(\eta) - kz, k > 0$

得 $\dot{V}_c\leqslant -W(\eta) - kz^2$

该式表明原点 $(\eta=0,z=0)$ 是渐近稳定的。由 $\phi(0)=0$ 可知，原点 $(\eta=0,\xi=0)$ 是渐近稳定的，将v,z, $\dot{\phi}$ 代入，得状态反馈控制律为

$$u = \frac {\partial \phi}{\partial \eta} [ f (\eta) + g (\eta) \xi ] - \frac {\partial V}{\partial \eta} g (\eta) - k [ \xi - \phi (\eta) ] \tag {14.52}$$

如果假设全局成立,且 $V(\eta)$ 是径向无界的,则原点是全局渐近稳定的。下一引理是上述结论的总结。

![](image/6c7fa327c3f8de124c4701cf8897398252ca224d8ebd61ade2038e56db1ba022.jpg)

<details>
<summary>flowchart</summary>
