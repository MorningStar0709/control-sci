其中 $\alpha = \min \{\lambda_{\min}(Q_1),\lambda_{\min}(Q_2)\} ,\qquad \beta = \max \{\| P_1\| _2,\| P_2\| _2\}$

因此,选择 $\gamma<\alpha/(2\sqrt{2}\beta)$ ，以保证在 U 内有 $\dot{V}(z)>0$ 。所以，根据定理 4.3，原点是非稳定的。注意，通过定义矩阵

$$
P = T ^ {\mathrm{T}} \left[ \begin{array}{c c} {P _ {1}} & {0} \\ {0} & {- P _ {2}} \end{array} \right] T; Q = T ^ {\mathrm{T}} \left[ \begin{array}{c c} {Q _ {1}} & {0} \\ {0} & {Q _ {2}} \end{array} \right] T
$$

可以把定理4.3运用于原坐标系中。定义的矩阵 $P$ 和 $Q$ 满足方程

$$P A + A ^ {\mathrm{T}} P = Q$$

矩阵 $Q$ 是正定的，且 $V(x) = x^{\mathrm{T}}Px$ 在任意靠近原点 $x = 0$ 点上为正。现在考虑一般情况，即 $A$ 在虚轴上可能有特征值，而且在右半开复平面内也有特征值。运用前面平移坐标轴的简单方法，即可将一般情况转化为特殊情况。假设 $A$ 有 $m$ 个特征值，且满足 $\operatorname{Re} \lambda_i > \delta > 0$ 。那么，矩阵 $[A - (\delta / 2)I]$ 在右半开平面内有 $m$ 个特征值，但在虚轴上没有特征值。根据前面的讨论，存在矩阵 $P = P^{\mathrm{T}}$ 和 $Q = Q^{\mathrm{T}} > 0$ ，使

$$P \left[ A - \frac {\delta}{2} I \right] + \left[ A - \frac {\delta}{2} I \right] ^ {\mathrm{T}} P = Q$$

其中， $V(x)=x^{T}Px$ 对任意靠近原点的点都为正。 $V(x)$ 沿系统轨线的导数为

$$
\begin{array}{l} \dot {V} (x) = x ^ {\mathrm{T}} \left(P A + A ^ {\mathrm{T}} P\right) x + 2 x ^ {\mathrm{T}} P g (x) \\ = x ^ {\mathrm{T}} \left[ P \left(A - \frac {\delta}{2} I\right) + \left(A - \frac {\delta}{2} I\right) ^ {\mathrm{T}} P \right] x + \delta x ^ {\mathrm{T}} P x + 2 x ^ {\mathrm{T}} P g (x) \\ = x ^ {\mathrm{T}} Q x + \delta V (x) + 2 x ^ {\mathrm{T}} P g (x) \\ \end{array}
$$

在集合 $\{x\in R^n\mid \| x\| _2\leqslant r$ 且 $V(x) > 0\}$

内，当 $\| x\| _2 < r$ 时，选择 $r$ 满足 $\| g(x)\| _2\leqslant \gamma \| x\| _2$ ，则 $\dot{V} (x)$ 满足

$$\dot {V} (x) \geqslant \lambda_ {\min} (Q) \| x \| _ {2} ^ {2} - 2 \| P \| _ {2} \| x \| _ {2} \| g (x) \| _ {2} \geqslant (\lambda_ {\min} (Q) - 2 \gamma \| P \| _ {2}) \| x \| _ {2} ^ {2}$$

当 $\gamma < (1/2)\lambda_{\min}(Q) / \|P\|_2$ 时，上式为正。运用定理4.3即可证明。

定理 4.7 提供了确定原点处平衡点稳定性的简单步骤。首先计算雅可比矩阵

$$A = \left. \frac {\partial f}{\partial x} \right| _ {x = 0}$$

并验证其特征值,如果对于所有 i 有 $Re \lambda_{i}<0$ ,或对某些 i 有 $Re \lambda_{i}>0$ ,那么原点就分别是渐近稳定的或非稳定的。该定理的证明还表明，当对于所有 $i$ 有 $\operatorname{Re} \lambda_i < 0$ 时，也可求出系统工作在原点的某个邻域内的李雅普诺夫函数为二次型 $V(x) = x^{\mathrm{T}}Px$ ，其中 $P$ 是对于任意正定对称矩阵 $Q$ ，李雅普诺夫方程(4.12)的解。注意，定理4.7并未涉及到对于所有 $i, \operatorname{Re} \lambda_i \leqslant 0$ ，以及对于某些 $i, \operatorname{Re} \lambda_i = 0$ 的情况。此时，线性化不能确定平衡点的稳定性①。

例4.14 考虑标量系统

$$\dot {x} = a x ^ {3}$$

在原点 x=0 对系统线性化, 得

$$A = \left. \frac {\partial f}{\partial x} \right| _ {x = 0} = \left. 3 a x ^ {2} \right| _ {x = 0} = 0$$
