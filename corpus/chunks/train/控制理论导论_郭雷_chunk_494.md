即 $\left.\frac{\partial^2H}{\partial u^2}\right|_*$ 在 $\bar{t}$ 时刻是半负定的.

注意到 $u^{*}(t), x^{*}(t), \psi(t)$ 满足

$$
\left\{ \begin{array}{l l} \dot {x} ^ {*} (t) = \frac {\partial H}{\partial \psi^ {\mathrm{T}}} \Big | _ {*} = f (x ^ {*} (t), u ^ {*} (t)), & x ^ {*} (t _ {0}) = x _ {0}, \\ \dot {\psi} ^ {\mathrm{T}} (t) = - \frac {\partial H}{\partial x} \Big | _ {*}, & \psi^ {\mathrm{T}} (t _ {f}) = - \frac {\partial k}{\partial x} \Big | _ {*}, \end{array} \right.
$$

我们常称下列方程：

$$
\left\{ \begin{array}{l} \dot {x} = \frac {\partial H}{\partial \psi^ {\mathrm{T}}} \\ \dot {\psi} = - \left(\frac {\partial H}{\partial x}\right) ^ {\mathrm{T}} \end{array} \right. \tag {7.1.21}
$$

为最优控制问题 (7.1.1), (7.1.3) 的 Hamilton 正则方程组. (ψ 满足的方程也称为共轭 (伴随) 方程, ψ 也称为共轭变量或协态.) 利用 $u^{*}(t)$ , $x^{*}(t)$ 和 $\psi(t)$ 满足 Hamilton 正则方程组 (7.1.21) 及 $\left.\frac{\partial H}{\partial u}\right|_{*} = 0$ , 直观上可以得到 $H(x^{*}(t), u^{*}(t), \psi(t)) \equiv$ 常数 $(= H(x^{*}(t_{f}), u^{*}(t_{f}), \psi(t_{f}))$ , 其严格证明将在下段中给出.

当系统终端状态受形如式 (7.1.2) 约束时, 通过引入 Lagrange 乘子向量 $\mu \in \mathbb{R}^p$ , 将 $x(t_f)$ 受式 (7.1.2) 约束化为自由端点情况进行处理, 即式 (7.1.1), (7.1.2) 和式 (7.1.3) 的最优控制问题化为求泛函 $J_2[u]$ 的极小问题, 这里泛函 $J_2[u]$ 为

$$J _ {2} [ u ] = k (x (t _ {f})) + \mu^ {\mathrm{T}} g (x (t _ {f})) + \int_ {t _ {0}} ^ {t _ {f}} l (x (t), u (t)) \mathrm{d} t. \tag {7.1.22}$$

类似于上面的讨论能够得到：如果 $u^{*}(t)$ 是式(7.1.1)，(7.1.2)和式(7.1.3)的最优控制， $x^{*}(t)$ 是相应的最优轨线，则

$$H (x ^ {*} (t), u, \psi (t)) \stackrel {\mathrm{def}} {=} - l (x ^ {*} (t), u) + \psi^ {\mathrm{T}} (t) f (x ^ {*} (t), u)$$

作为 $u$ 的函数，在 $u = u^{*}(t)$ 的一切连续时刻满足

$$\frac {\partial H (x ^ {*} (t) , u ^ {*} (t) , \psi (t))}{\partial u} = 0,\frac {\partial^ {2} H \left(x ^ {*} (t) , u ^ {*} (t) , \psi (t)\right)}{\partial u ^ {2}} \leqslant 0,H (x ^ {*} (t), u ^ {*} (t), \psi (t)) = \text {常数}.$$

这里Lagrange乘子向量值函数 $\psi (t)$ 和Lagrange乘子向量 $\mu$ 满足

$$
\left\{ \begin{array}{l} \dot {\psi} ^ {T} (t) = - \frac {\partial H}{\partial x} \Big | _ {*} \\ \psi^ {T} (t _ {f}) = - \frac {\partial k}{\partial x} \Big | _ {*} - \mu^ {T} \frac {\partial g}{\partial x} \Big | _ {*}, \end{array} \right. \tag {7.1.23}
$$

$\psi(t)$ 在 $t_f$ 处满足的条件称为横截条件。常见的横截条件如下：

(1) 当系统终端状态 $x(t_f)$ 是 $\mathbb{R}^n$ 中某固定点时，即 $x(t_f) - x_f$ ，此时 $k(x(t_f)) =$ 常数， $g(x(t_f)) = x(t_f) - x_f = 0$ . 于是有

$$\frac {\partial k (x (t _ {f}))}{\partial x} = 0, \qquad \frac {\partial g (x (t _ {f}))}{\partial x} = I _ {n} (n \times n \text {恒等矩阵}).$$
