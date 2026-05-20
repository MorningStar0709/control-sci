其中 $\kappa_0\geqslant \left|\frac{c - \hat{c}}{\hat{c}}\right|,\quad \rho_1 = \frac{k}{\hat{c}},\quad k\geqslant \left|\frac{\hat{a}c - a\hat{c}}{\hat{c}}\right| + \left|\frac{c - \hat{c}}{\hat{c}}\right|\sqrt{k_1^2 + k_2^2}$

假设 $\kappa_0 < 1$ ，并按照上一例题选取 $v$ ，我们会发现控制律 $u = \psi(x) + v$ 使原点达到全局指数稳定。例13.18已经分析了在控制律 $u = \psi(x)$ 下的同一个系统，对两例结果的比较明确说明了附加控制分量 $v$ 的贡献。例13.18能够证明当把 $k$ 限制为满足

$$k < \frac {1}{2 \sqrt {p _ {1 2} ^ {2} + p _ {2 2} ^ {2}}}$$

时,控制律 $u=\psi(x)$ 可以稳定系统。现在这一限制已经完全不需要了,只要知道 k 即可。△例 14.6 再次考虑上例中的单摆方程,这次假设单摆的悬挂点是时变、有界且水平加速的。为了简化问题,忽略摩擦 $(b=0)$ ,则状态方程为

$$
\begin{array}{l} \dot {x} _ {1} = x _ {2} \\ \dot {x} _ {2} = a \sin x _ {1} + c u + h (t) \cos x _ {1} \\ \end{array}
$$

其中 $h(t)$ 是悬挂点的(归一化)水平加速度，对于所有 $t \geqslant 0$ ，有 $|h(t)| \leqslant H$ 。标称模型和标称稳定控制律可按上例选取 $(b = 0)$ ，不确定项 $\delta$ 满足

$$| \delta | \leqslant \rho_ {1} \| x \| _ {2} + \kappa_ {0} | v | + H / \hat {c}$$

其中 $\rho_{1}$ 和 $\kappa_0$ 与上例相同，而 $\rho (x) = \rho_{1}\parallel x\parallel_{2} + H / \hat{c}$ ，当 $x = 0$ 时不为零。在控制律(14.41）中 $\eta$ 的选择必须满足 $\eta \geqslant (\rho_1\parallel x\parallel_2 + H / \hat{c}) / (1 - \kappa_0)$ ，取 $\eta (x) = \eta_0 + \rho_1\parallel x\parallel_2 / (1 - \kappa_0)$

$\eta_{0}\geqslant H/\hat{c}(1-\kappa_{0})$ 。但在前例中，我们任意设置了 $\eta(0)=1$ ，这是为适应非零扰动项 $h(t)\cos x_{1}$ 所做的唯一修正。因为 $\rho(0)\neq0$ ，推论14.1不适用，只能由定理14.3得出结论，即闭环系统的解是一致毕竟有界的，其最终边界正比于 $\sqrt{\varepsilon}$ 。
