# 9.1 奇异最优控制问题的提出

在研究时间最短和燃料最少的最优控制问题时就会涉及奇异解问题,在时间最短最优控制问题中,应用庞特里亚金极小值原理可得

$$u _ {j} ^ {*} (t) = - \operatorname{sgn} [ q _ {j} (t) ], \quad j = 1, 2, \dots , r, \quad t \in [ t _ {0}, t _ {\mathrm{f}} ] \tag {9-1}$$

在正常情况下，函数 $q_{j}(t)$ 在控制区间 $[t_0, t_f]$ 中只有有限个零值点。控制变量在其约束的边界上取值，得到的最优控制为Bang-Bang控制。但在奇异情况下，至少有一个函数 $q_{j}(t)$ 在某一区间 $[t_1, t_2] \subset [t_0, t_f]$ 上恒等于零。

在线性二次型性能指标最优控制问题中也有类似的奇异情况。可以将性能指标中的被积函数取为 $X^{\mathrm{T}}QX + U^{\mathrm{T}}RU$ 。其中 $U^{\mathrm{T}}RU$ 项的出现体现了对控制变量的约束，可以使最优控制 $\pmb{U}^{*}$ 的值在合理的范围内。如果直接规定控制变量满足如下不等式约束

$$\left| u _ {j} \right| \leqslant 1, \quad j = 1, 2, \dots , r \tag {9-2}$$

这时就没有必要在性能指标中出现 $U^{T}RU$ 这项了。此类问题与规范调节器的差别在于控制的不等式约束，且 R=0 。哈密顿函数 H 也是控制变量 U 的线性函数。若在控制区间 $[t_{0}, t_{f}]$ 上， $H = B^{T}\lambda$ 只存在有限个零值点，则是 Bang-Bang 控制。如果在某一控制区间 $[t_{1}, t_{2}] \subset [t_{0}, t_{f}]$ 上满足 $H = B^{T}\lambda = 0$ ，那么，控制变量在控制边界内取值总满足极小值原理。但是，由极小值原理同样很难解出最优控制的具体形式。考虑到上述线性二次型问题的最优控制一般情况下是由 Bang-Bang 控制和线性反馈控制两部分组成的，所以，对于一般的 Bolza 问题：

$$
\left\{ \begin{array}{l l} {\dot {X} = f (  X, U, t  )} \\ {J   =   \phi (  X (  t _ {\mathrm{f}})  , t _ {\mathrm{f}}  )   +    \int_ {t _ {0}} ^ {t _ {\mathrm{f}}} F (  X, U, t  )   \mathrm{d} t} \\ {X (  t _ {0}  )   =   X _ {0}} \\ {G (  x (  t _ {\mathrm{f}})  , t _ {\mathrm{f}}  )   =   0} \\ {U = \{  u _ {j} (  \cdot  ): u _ {j} (  t  )   \text {是分段连续函数，且}} \\ {\mid   u _ {j} (  t  )   \mid \leqslant M <   \infty    , \quad t   \in [   t _ {0}  , t _ {\mathrm{f}}   ]  , j = 1, 2, \dots , r   \}} \\ {t _ {0}    \text {给定}, t _ {\mathrm{f}}    \text {可以固定，也可以不固定}} \end{array} \right. \tag {9-3}
$$

其哈密顿函数为

$$H (\boldsymbol {X}, \boldsymbol {U}, \boldsymbol {\lambda}, t) = F (\boldsymbol {X}, \boldsymbol {U}, t) + \boldsymbol {\lambda} ^ {\mathrm{T}} \boldsymbol {f} (\boldsymbol {X}, \boldsymbol {U}, t) \tag {9-4}$$

当控制变量在约束的边界范围内取值时,极值条件应为

$$H _ {u} = 0 \tag {9-5}H _ {u u} \geqslant 0 \tag {9-6}$$

条件(9-6)常称勒让德-克莱勃希条件(Legaudre-lebsch Condition)。若条件(9-6)只取严格的不等式符号,则称强化的勒让德-克莱勃希条件。

如果在某一时间间隔 $[t_1, t_2] \subset [t_0, t_f]$ 上，矩阵 $H_{uu}$ 是奇异的，即

$$\det \left(H _ {u u}\right) = 0 \tag {9-7}$$

或者 $H_{uu}$ 是非负定的，不满足强化的勒让德-克莱勃希条件，则称Bolza问题为奇异的。此时的最优控制为奇异最优控制。与此对应的最优轨线部分称为奇异弧， $[t_1,t_2]$ 则称为奇异区间。
