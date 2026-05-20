![](image/c7b88ea5b1899545d30be63c6f7310057da2628bda94fd984f9423468c0795ed.jpg)

<details>
<summary>text_image</summary>

U_r
\overline{U}_r^*
u^*(t)
</details>

图7.1.1

用类似方法可得在 $[t_0, t_f]$ 上 $H(x^*(t), u^*(t), \psi(t))$ 为常数的结论.

对于 $x(t_{f})$ 受有形如式(7.1.2)约束的情况，通过引入Lagrange乘子向量 $\mu$ 可化为如上面 $x(t_{f})$ 自由情况进行处理。其结论中，除Lagrange乘子向量值函数 $\psi (t)$ 满足端点条件

$$\psi^ {\mathrm{T}} (t _ {f}) = - \frac {\partial k (x ^ {*} (t _ {f}))}{\partial x} - \mu^ {\mathrm{T}} \frac {\partial g (x (t _ {f}))}{\partial x}$$

外，其余皆与 $x(t_{f})$ 自由情况相同.

对于当 $t_f$ 自由时， $x(t_f)$ 自由和 $x(t_f)$ 受形如式 (7.1.2) 约束的情况，亦可用与上面相同的方法进行讨论，这里仅列出结果，不再细述。

定理 7.1.3(Pontryagin 极大值原理) 设 $u^{*}(t)$ 是定义在 $[t_{0}, t_{f}]$ 上定常系统 (7.1.1) 和性能指标 (7.1.3) 的最优控制， $x^{*}(t)$ 是相应最优轨线，则必定存在向量值函数 $\psi(t)$ ，使 $u^{*}(t)$ ， $x^{*}(t)$ 和 $\psi(t)$ 在 $[t_{0}, t_{f}]$ 上同时满足

(1)

$$
\left\{ \begin{array}{l l} {\dot {x} ^ {*} (t) = \left[ \frac {\partial H (x ^ {*} (t) , u ^ {*} (t) , \psi (t))}{\partial \psi} \right] ^ {\mathrm{T}},} & {x ^ {*} (t _ {0}) = x _ {0},} \\ {\dot {\psi} ^ {\mathrm{T}} (t) = - \frac {\partial H (x ^ {*} (t) , u ^ {*} (t) , \psi (t))}{\partial x},} \\ {\psi^ {\mathrm{T}} (t _ {f}) = \left\{ \begin{array}{l l} {- \frac {\partial k (x ^ {*} (t _ {f}))}{\partial x},} & {x (t _ {f}) \text {自由},} \\ {- \frac {\partial k (x ^ {*} (t _ {f}))}{\partial x} - \mu^ {\mathrm{T}} \frac {\partial g (x ^ {*} (t _ {f}))}{\partial x},} & {x (t _ {f}) \text {受约束} g (x (t _ {f})) = 0,} \end{array} \right.} \end{array} \right.
$$

其中 $\mu$ 为待定常向量；

(2) $H(x^{*}(t),u^{*}(t),\psi (t)) = \max_{u\in \mathbf{U}_{r}}H(x^{*}(t),u,\psi (t)),\forall t\in \Omega (t_{0},t_{f};u^{*});$   
(3) $H(x^{*}(t),u^{*}(t),\psi (t)) =$ 常数， $t_0\leqslant t\leqslant t_f.$

当 $t_f$ 固定时，该常数可能不为零，而当 $t_f$ 自由时，该常数一定为零。这里 $H(x, u, \psi) \stackrel{\mathrm{def}}{=} -l(x, u) + \psi^{\mathrm{T}} f(x, u)$ 为 (7.1.1)，(7.1.3) 的 Hamilton 函数。

“极大值原理”名称源于定理7.1.3的条件(2). 对于 $f, g, k, l$ 显含时间 $t$ 的情况，通过将 $t = x_{n+1}$ 视为新的状态变量，直接能从上述定理得到最优控制问题的

极大值原理：

定理 7.1.4(时变系统 Pontryagin 极大值原理) 设 $u^{*}(t)$ 是时变系统 (7.1.1) 和性能指标 (7.1.3) 在 $[t_{0}, t_{f}]$ 上的最优控制， $x^{*}(t)$ 是相应最优轨线，则必定存在向量值函数 $\psi(t)$ ，使 $u^{*}(t)$ ， $x^{*}(t)$ 和 $\psi(t)$ 在 $[t_{0}, t_{f}]$ 上同时满足
