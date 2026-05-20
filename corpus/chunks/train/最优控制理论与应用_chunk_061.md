# 4.2 连续系统的极小值原理

由于可以利用扩充变量的方法将各类最优控制问题化为定常系统，末值型性能指标情况下的标准形式。这里只就定常系统、末值型性能指标、 $t_{f}$ 固定、末端受约束情况下给出极小值原理的简单证明。

设系统的状态方程为

$$\dot {\boldsymbol {X}} = \boldsymbol {f} (\boldsymbol {X}, \boldsymbol {U}, t) \quad \boldsymbol {X} (t) \in \mathbf {R} ^ {n} \tag {4-1}$$

初始条件为

$$\boldsymbol {X} \left(\boldsymbol {t} _ {0}\right) = \boldsymbol {X} _ {0} \tag {4-2}$$

控制向量 $U(t)\in \mathbf{R}^m$ ，并受下面的约束

$$\boldsymbol {U} \in \Omega \tag {4-3}$$

末值状态必须满足的约束条件为

$$\boldsymbol {G} \left[ \boldsymbol {X} \left(t _ {\mathrm{f}}\right), t _ {\mathrm{f}} \right] = \mathbf {0} \tag {4-4}$$

性能指标函数为

$$J = \phi [ X (t _ {\mathrm{f}}), t _ {\mathrm{f}} ] + \boldsymbol {v} ^ {\mathrm{T}} \boldsymbol {G} [ X (t _ {\mathrm{f}}), t _ {\mathrm{f}} ] \tag {4-5}$$

其中 $\pmb{v} \in \mathbf{R}^n$ 为待定列向量。

在本节中，假设函数 $f_{i}(X,U,t),\frac{\partial f_{i}}{\partial X},\phi [X(t_{\mathrm{f}}),t_{\mathrm{f}}],\frac{\partial\phi}{\partial X(t_{\mathrm{f}})}$ 存在且连续，并假定容许控制 $U(t)$ 是在控制域内取值的任何分段连续函数。这时如果选定了某一容许控制 $U(t)$ ，则容易证明在任意的初始条件下 $X(t_0) = X_0$ 下，方程(4-1)唯一的确定了系统状态的变化规律 $X(t)$ ，且 $X(t)$ 是连续的和分段可微的。在这些条件下，就定常系统、末值型性能指标、 $t_\mathrm{f}$ 固定、末端受约束情况下给出极小值原理的简单证明。

证明 采用扰动法, 即给最优控制一个变分 $\delta U$ , 它将引起最优轨线的变分 $\delta X$ , 并使性能指标有一增量 $\Delta J$ , 当 $J$ 为极小时, 必有 $\Delta J \geqslant 0$ , 由此即可导出最优控制所应满足的必要条件。在变分法中, $\delta U$ 是微量, 即将最优控制和邻近的容许控制相比较, 因而最多只能建立哈密顿函数 $H$ 的相对极小值性质。庞特里亚金极大值原理却将最优控制与控制域内所有可能的值进行比较, 因而得出结论, 在整个控制域内最优控制使哈密顿函数 $H$ 成为绝对极小值。正是这个性质使得庞特里亚金极大值原理成为寻找最优控制的有力工具。但是这样, $U(t)$ 的改变量 $\delta U$ 必须看成有限量, 而不再是微量。如果让改变的时间很短, 则由此引起的最优轨线的改变 $\delta X$ 仍是微量, 性能指标的增量 $\Delta J$ 也是微量, 因而对各关系式的数学处理仍是比较容易的。

设 $U^{*}(t)$ 为最优控制，任选一时刻 $t_1 \in [t_0, t_f]$ 及一微量 $\varepsilon > 0$ ，在时间间隔 $[t_1 - \varepsilon, t_1]$ 中给 $U^{*}(t)$ 一有限大小的改变量 $\delta U$ ，且使得 $U^{*} + \delta U$ $\in \Omega$ 。现在研究由 $\delta U$ 引起的最优轨线 $X^{*}(t)$ 的变化。分为三段考虑：

(1) $0 \leqslant t \leqslant t_{1} - \varepsilon$

在这一段中， $\delta U = 0$ ，因而 $\delta X(t) = 0$ 。

(2) $t_1 - \varepsilon \leqslant t \leqslant t_1$

系统的状态方程(4-1)可在初始条件 $X(t_{1} - \varepsilon) = X^{*}(t_{1} - \varepsilon)$ 下直接积分。

当 $U = U^{*}$ 时，

$$\boldsymbol {X} ^ {*} (t) - \boldsymbol {X} ^ {*} (t _ {1} - \varepsilon) = \int_ {t _ {1} - \varepsilon} ^ {t} \boldsymbol {f} (\boldsymbol {X} ^ {*}, \boldsymbol {U} ^ {*}, t) d t$$

当 $U = U^{*} + \delta U$ 时，
