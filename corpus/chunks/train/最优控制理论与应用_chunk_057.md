# 3.4 小结

1. 函数的函数叫做泛函。性能指标 J 是控制作用 $u(t)$ 的函数，故称为性能泛函。和微分类似，可引入泛函的变分 $\delta J$ 。J 取极值的必要条件为 $\delta J = 0$ 。

2. 泛函 $J = \int_{t_0}^{t_f} F[X, \dot{X}, t] \mathrm{d}t(X, \dot{X}$ 为向量）取无约束极值的必要条件为

$$\frac {\partial F}{\partial X} - \frac {\mathrm{d}}{\mathrm{d} t} \bigg (\frac {\partial F}{\partial \dot {X}} \bigg) = 0 \qquad \text {(欧拉-拉格朗日方程)}$$

当 $X(t_0), X(t_f)$ 自由时，还有横截条件

$$\frac {\partial F}{\partial \dot {X}} = 0 \qquad (\text {当} t = t _ {0} \text {和} t = t _ {f} \text {时})$$

3. 求解动态系统的最优控制是一个求取有约束条件的泛函极值问题。系统的状态方程就是状态变量要满足的一个约束方程，即

$$\boldsymbol {f} (\boldsymbol {X}, \boldsymbol {U}, t) - \dot {\boldsymbol {X}} = \mathbf {0}$$

4. 设系统状态方程为 $\dot{\pmb{X}} = \pmb{f}(\pmb{X},\pmb{U},t)$ ，性能指标为 $J = \phi[\pmb{X}(t_{\mathrm{f}}),t_{\mathrm{f}}] + \int_{t_0}^{t_f}F[\pmb {X},\pmb {U},t]\mathrm{d}t$ ，初始状态 $\pmb {X}(t_0)$ 给定，终端状态 $\pmb {X}(t_{\mathrm{f}})$ 满足向量约束方程 $\pmb {G}[\pmb {X}(t_{\mathrm{f}}),t_{\mathrm{f}}] = 0$ （包括 $\pmb {X}(t_{\mathrm{f}})$ 给定的情况）。则由变分法可得下面的结果：

(1) 终端时刻 $t_{f}$ 给定时, J 取极值的必要条件为

$$
\begin{array}{r l r} {\dot {\pmb {\lambda}}} & {= - \frac {\partial H}{\partial \pmb {X}} \quad} & {\mathrm{(协态方程)}} \\ {\dot {\pmb {X}}} & {= \frac {\partial H}{\partial \pmb {\lambda}} \quad} & {\mathrm{(状态方程)}} \end{array} \Bigg \} \text {正则方程}
\frac {\partial H}{\partial \pmb {U}} = \pmb {0} \quad (\text {控制方程})\pmb {\lambda} (t _ {\mathrm{f}}) = \frac {\partial \phi}{\partial \pmb {X} (t _ {\mathrm{f}})} + \frac {\partial \pmb {G} ^ {\mathrm{T}}}{\partial \pmb {X} (t _ {\mathrm{f}})} \pmb {v} \qquad \text {(横截条件)}
$$

其中， $H(X,U,\lambda ,t) = F(X,U,t) + \pmb{\lambda}^{\mathrm{T}}\cdot f(X,U,t)$ 称为哈密顿函数。

正则方程有 2n 个变量, 积分时要 2n 个边界条件, 初始条件 $X(t_{0})$ 给定时提供了 n 个边界条件, 若 $X(t_{f})$ 也完全给定, 则又提供了 n 个边界条件, 这时可不需要横截条件, 见例 3-3。当 $X(t_{f})$ 自由或部分分量自由时, 就要靠横截条件来提供缺少的边界条件, 见例 3-4。

(2) 终端条件 $t_{f}$ 自由, J 取极值的必要条件与 $t_{f}$ 给定时的不同处, 仅在于多一个求最优终端时刻的条件

$$H (t _ {\mathrm{f}}) = - \frac {\partial \phi}{\partial t _ {\mathrm{f}}} - \frac {\partial G ^ {\mathrm{T}}}{\partial t _ {\mathrm{f}}} \boldsymbol {v} \tag {3-57}$$

5. 用经典变分法求解最优控制时, 假定 $u(t)$ 不受限制, $\delta U$ 为任意, 故得出控制方程

$$\frac {\partial H}{\partial \boldsymbol {U}} = \boldsymbol {0}$$

不满足这种情况时,要用极小值原理或动态规划求解。这些内容将在下面的章节中介绍。
