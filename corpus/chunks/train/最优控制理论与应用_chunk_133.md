$$\boldsymbol {Y} _ {j} ^ {K + 1} \left(t _ {0}\right) = \boldsymbol {X} _ {j} \left(t _ {0}\right) = \boldsymbol {X} _ {j 0} j = 1, 2, \dots , n \tag {7-81}\mathbf {Y} _ {j} ^ {K + 1} \left(t _ {\mathrm{f}}\right) = \boldsymbol {\lambda} _ {j} \left(t _ {\mathrm{f}}\right) = \boldsymbol {\lambda} _ {j \mathrm{f}} j = n + 1, n + 2, \dots , 2 n \tag {7-82}$$

式(7-80)可写成下面的线性非齐次方程

$$\dot {\boldsymbol {Y}} ^ {K + 1} = \left(\frac {\partial \boldsymbol {g}}{\partial \boldsymbol {Y}}\right) _ {K} \boldsymbol {Y} ^ {K + 1} + \left[ \boldsymbol {g} \left(\boldsymbol {Y} ^ {K}, t\right) - \left(\frac {\partial \boldsymbol {g}}{\partial \boldsymbol {Y}}\right) _ {K} \boldsymbol {Y} ^ {K} \right] \tag {7-83}$$

或

$$\dot {\mathbf {Y}} ^ {K + 1} = \mathbf {A} _ {K} (t) \mathbf {Y} ^ {K + 1} + \mathbf {v} _ {K} (t) \tag {7-84}$$

其中

$$\boldsymbol {A} _ {K} (t) = \left(\frac {\partial \boldsymbol {g}}{\partial \boldsymbol {Y}}\right) _ {K} \tag {7-85}$$

是 $2n \times 2n$ 的系统矩阵，

$$\boldsymbol {v} _ {K} (t) = \left[ g \left(\mathbf {Y} ^ {K}, t\right) - \left(\frac {\partial g}{\partial \mathbf {Y}}\right) _ {K} \mathbf {Y} ^ {K} \right] \tag {7-86}$$

是 $n \times 1$ 驱动函数向量。式(7-84)是线性微分方程，由给定的 $2n$ 个边界条件可确定其通解的 $2n$ 个未知常数，故解 $\mathbf{Y}^{K+1}(t)$ 可完全被确定。

当满足

$$\left| \mathbf {Y} _ {i} ^ {K + 1} (t) - \mathbf {Y} _ {i} ^ {K} (t) \right| \leqslant \varepsilon_ {i} \quad i = 1, 2, \dots , 2 n \tag {7-87}$$

可停止计算。

例7-4 系统方程为

$$\dot {x} = - x ^ {2} + u \quad x (0) = 1 0 \tag {7-88}$$

性能指标为

$$J = \frac {1}{2} \int_ {0} ^ {1} \left(x ^ {2} + u ^ {2}\right) d t \tag {7-89}$$

用拟线性化法求 $u(t)$ ，使 $J$ 最小。

解 哈密顿函数为

$$H = \frac {1}{2} \left(x ^ {2} + u ^ {2}\right) + \lambda (- x ^ {2} + u) \tag {7-90}\frac {\partial H}{\partial u} = u + \lambda = 0u = - \lambda \tag {7-91}$$

上式代入状态方程后得到

$$\dot {x} = - x ^ {2} - \lambda \quad x (0) = 1 0 \tag {7-92}\dot {\lambda} = - \frac {\partial H}{\partial X} = - x + 2 \lambda x \quad \lambda (1) = \frac {\partial \Phi}{\partial X (1)} = 0 \tag {7-93}$$

或写成

$$
\dot {\boldsymbol {Y}} = \left[ \begin{array}{l} \dot {x} \\ \dot {\lambda} \end{array} \right] = \left[ \begin{array}{c} - x ^ {2} - \lambda \\ - x + 2 \lambda x \end{array} \right] \tag {7-94}
$$

上式与式(7-78)对照可知

$$
g (\boldsymbol {Y}, t) = \left[ \begin{array}{l} g _ {1} \\ g _ {2} \end{array} \right] = \left[ \begin{array}{c} - x ^ {2} - \lambda \\ - x + 2 \lambda x \end{array} \right] \tag {7-95}
$$

根据式 $(7-85)$ 、 $(7-86)$ ，可得
