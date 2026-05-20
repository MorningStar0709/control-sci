$$\| x (t) \| \leqslant \beta (\| x (t _ {0}) \|, t - t _ {0}), \forall t _ {0} \leqslant t \leqslant t _ {0} + T \tag {4.42}\| x (t) \| \leqslant \alpha_ {1} ^ {- 1} (\alpha_ {2} (\mu)), \forall t \geqslant t _ {0} + T \tag {4.43}$$

而且,如果 $D = R^{n}$ 且 $\alpha_{1}$ 属于 $K_{\infty}$ 类函数,则式(4.42)和式(4.43)对于任意初始状态 $x(t_{0})$ 都成立,对 $\mu$ 的大小没有任何限制。

证明: 见附录 C.9。

不等式(4.42)和不等式(4.43)说明对于所有 $t \geqslant t_0, x(t)$ 是一致有界的，且是一致毕竟有界的，其最终边界为 $\alpha_1^{-1}(\alpha_2(\mu))$ 。最终边界是 $\mu$ 的 $\kappa$ 类函数，因此， $\mu$ 取值越小，最终边界越小。当 $\mu$ 趋于无穷时，最终边界趋于零。

定理 4.18 的主要应用出现在扰动系统的稳定性研究中 $^{②}$ 。下面的例题说明这一应用的基本思想。

例 4.24 在 1.2.3 节中我们研究了一个具有硬化弹簧、线性黏滞阻尼并施加周期外力的弹簧系统, 可用达芬方程表示为

$$m \ddot {y} + c \dot {y} + k y + k a ^ {2} y ^ {3} = A \cos \omega t$$

取 $x_{1} = y, x_{2} = \dot{y}$ ，并假设对各常数取几个数值。系统的状态方程表示为

$$
\begin{array}{l} \dot {x} _ {1} = x _ {2} \\ \dot {x} _ {2} = - (1 + x _ {1} ^ {2}) x _ {1} - x _ {2} + M \cos \omega t \\ \end{array}
$$

其中 $M \geqslant 0$ ，与周期性外力的幅度成比例。当 M = 0 时，系统在原点有一个平衡点。例 4.6 证明原点是全局渐近稳定的，且取李雅普诺夫函数为①

$$
\begin{array}{l} V (x) = x ^ {\mathrm{T}} \left[ \begin{array}{l l} \frac {1}{2} & \frac {1}{2} \\ \frac {1}{2} & 1 \end{array} \right] x + 2 \int_ {0} ^ {x _ {1}} (y + y ^ {3}) d y = x ^ {\mathrm{T}} \left[ \begin{array}{l l} \frac {1}{2} & \frac {1}{2} \\ \frac {1}{2} & 1 \end{array} \right] x + x _ {1} ^ {2} + \frac {1}{2} x _ {1} ^ {4} \\ = x ^ {\mathrm{T}} \left[ \begin{array}{l l} \frac {3}{2} & \frac {1}{2} \\ \frac {1}{2} & 1 \end{array} \right] x + \frac {1}{2} x _ {1} ^ {4} \stackrel {\text {def}} {=} x ^ {\mathrm{T}} P x + \frac {1}{2} x _ {1} ^ {4} \\ \end{array}
$$

当 $M > 0$ 时，应用定理4.18以 $V(x)$ 作为备选李雅普诺夫函数。函数 $V(x)$ 是正定的，且径向无界，因此，根据引理4.3，存在 $\mathcal{K}_{\infty}$ 类函数 $\alpha_{1}$ 和 $\alpha_{2}$ ，在全局性范围内都满足式(4.39)。 $V$ 沿系统轨线的导数为

$$\dot {V} = - x _ {1} ^ {2} - x _ {1} ^ {4} - x _ {2} ^ {2} + (x _ {1} + 2 x _ {2}) M \cos \omega t \leqslant - \| x \| _ {2} ^ {2} - x _ {1} ^ {4} + M \sqrt {5} \| x \| _ {2}$$

式中把 $(x_{1} + 2x_{2})$ 写为 $y^{\mathrm{T}}x$ ，并用于不等式 $y^{\mathrm{T}}x\leqslant \| x\| _2\| y\| _2$ 。为了满足式(4.40)，对于较大的 $\| x\|$ ，我们想要用 $-\| x\| _2^2$ 控制 $M\sqrt{5}\| x\| _2$ 。因而前述不等式写为

$$\dot {V} \leqslant - (1 - \theta) \| x \| _ {2} ^ {2} - x _ {1} ^ {4} - \theta \| x \| _ {2} ^ {2} + M \sqrt {5} \| x \| _ {2}$$

其中 $0 < \theta < 1$ 。则， $\dot{V} \leqslant -(1 - \theta) \| x \|_2^2 - x_1^4, \forall \| x \|_2 \geqslant \frac{M\sqrt{5}}{\theta}$

上式说明对于 $\mu = M\sqrt{5}/\theta$ ，不等式(4.40)全局满足。从而得出结论：系统的解是全局一致毕竟有界的。假如还想计算最终边界值，此时必须找出函数 $\alpha_{1}$ 和 $\alpha_{2}$ 。由不等式
