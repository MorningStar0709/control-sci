# 2.2 微分方程解的存在和唯一性

本节首先介绍标量微分方程的比较定理，微分和积分不等式。这些内容不仅对研究标量微分方程是必需的，而且对研究向量微分方程也是重要的。然后介绍向量微分方程解的存在和唯一性问题。

比较定理和微分、积分不等式 考察如下两个标量微分方程：

$$\dot {x} = f (t, x), \tag {2.2.1}\dot {x} = g (t, x). \tag {2.2.2}$$

假定 $f(t,x),g(t,x)$ 皆是定义在 $t - x$ 平面的开区域 $\Omega_2$ 上的连续函数．对于 $\Omega_{2}$ 内任一点 $(t_0,x_0)$ ，可以证明下列结果[6]：

(1) 方程 (2.2.1) 和 (2.2.2) 皆存在满足初始条件 $x(t_0) = x_0$ 的解 $x(t) \stackrel{\mathrm{def}}{=} x(t; t_0, x_0)$ 和 $y(t) \stackrel{\mathrm{def}}{=} y(t; t_0, x_0)$ ，它们的最大存在区间为 $(\alpha, \beta)$ 和 $(\bar{\alpha}, \bar{\beta})$ ( $x(t)$ 和 $y(t)$ 也称为过 $(t_0, x_0)$ 的饱和解 [6]);

(2) 方程 (2.2.1) 和 (2.2.2) 分别存在满足初始条件的唯一最大解及最小解 $\bar{x}(t) \stackrel{\mathrm{def}}{=} \bar{x}(t; t_0, x_0)$ , $\underline{x}(t) \stackrel{\mathrm{def}}{=} \underline{x}(t; t_0, x_0)$ 和 $\bar{y}(t) \stackrel{\mathrm{def}}{=} \bar{y}(t; t_0, x_0)$ . $\underline{y}(t) \stackrel{\mathrm{def}}{=} \underline{y}(t; t_0, x_0)$ , 它们的最大存在区间分别为 $(\alpha_1, \beta_1)$ 和 $(\alpha_2, \beta_2)$ (也称为过点 $(t_0, x_0)$ 的最大饱和解及最小饱和解[6]), 并且方程 (2.2.1) 和 (2.2.2) 的通过 $(t_0, x_0)$ 的任意解 $x(t)$ 和 $y(t)$ 分别满足下列不等式:

$$\underline {{{x}}} (t) \leqslant x (t) \leqslant \bar {x} (t), \quad t \in (\alpha_ {1}, \beta_ {1}),\underline {{{y}}} (t) \leqslant y (t) \leqslant \bar {y} (t), \quad t \in (\alpha_ {2}, \beta_ {2}).$$

定理2.2.1(第一比较定理) 设函数 $f(t,x)$ 和 $g(t,x)$ 在 $\Omega_2$ 上连续并满足

$$f (t, x) < g (t, x), \tag {2.2.3}$$

又设 $x(t)$ 和 $y(t)$ 分别是方程 (2.2.1) 和方程 (2.2.2) 过点 $(t_0, x_0)$ 的解。那么在它们的共同存在区间 $(t_0 - \alpha, t_0 + \beta)$ 上有

$$x (t) < y (t), \quad t \in [ t _ {0}, t _ {0} + \beta), \tag {2.2.4}x (t) > y (t), \quad t \in \left(t _ {0} - \alpha , t _ {0} \right]. \tag {2.2.5}$$

证明 记 $z(t) = y(t) - x(t)$ . 依假设, $\dot{Z}(t) > 0, \forall t \in (t_0 - \alpha, t_0 + \beta)$ . 由于 $Z(t_0) = 0$ , 故式 (2.2.4) 和式 (2.2.5) 成立.

推论2.2.1 在定理2.2.1的假设下，如果 $\bar{x}(t),\underline{x} (t)$ 和 $\bar{y} (t),\underline{y} (t)$ 是方程(2.2.1)和(2.2.2)过点 $(t_0,x_0)$ 并在区间 $(t_0 - \alpha ,t_0 + \beta)$ 上存在的最大解、最小解，则

$$\underline {{{x}}} (t) \leqslant \bar {x} (t) < \underline {{{y}}} (t) \leqslant \bar {y} (t), \quad t \in [ t _ {0}, t _ {0} + \beta).$$

定理2.2.2(第二比较定理) 设函数 $f(t,x)$ 和 $g(t,x)$ 在区域 $\Omega_2$ 上连续并满足

$$f (t, x) \leqslant g (t, x), \tag {2.2.6}$$

则有

$$x (t) \leqslant \bar {y} (t), \quad t \in [ t _ {0}, t _ {0} + \beta), \tag {2.2.7}x (t) \geqslant y (t), \quad t \in \left(t _ {0} - \alpha , t _ {0} \right], \tag {2.2.8}$$
