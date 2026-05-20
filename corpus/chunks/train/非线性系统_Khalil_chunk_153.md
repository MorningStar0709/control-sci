$$V (t, x) = \frac {1}{2} \left(a \sin x _ {1} + x _ {2}\right) ^ {2} + [ 1 + a g (t) - a ^ {2} ] \left(1 - \cos x _ {1}\right)$$

(a) 证明 $V(t,x)$ 是正定且递减的。

(b) 证明 $\dot{V} \leqslant -(\alpha - a)x_2^2 - a(2 - \gamma)(1 - \cos x_1) + O(\|x\|^3)$ , 其中 $O(\|x\|^3)$ 是原点邻域内边界为 $k\|x\|^3$ 的项。

(c) 证明原点是一致渐近稳定的。

4.40 (Floquet 定理) 考虑线性系统 $\dot{x}=A(t)x$ ，其中 $A(t)=A(t+T)^{①}$ 。设 $\Phi(\cdot,\cdot)$ 是状态转移矩阵。由方程 $\exp(BT)=\Phi(T,0)$ 定义一个常数矩阵 B，并设 $P(t)=\exp(Bt)\Phi(0,t)$ 。试证：

(a) $P(t + T) = P(t)$ 。

(b) $\Phi(t,\tau)=P^{-1}(t)\exp[(t-\tau)B]P(\tau)$

(c) 当且仅当 B 是赫尔维茨矩阵时, 系统 $\dot{x} = A(t)x$ 的原点是指数稳定的。

4.41 考虑系统 $\dot{x}_{1}=x_{2},\quad\dot{x}_{2}=2x_{1}x_{2}+3t+2-3x_{1}-2(t+1)x_{2}$

(a) 验证 $x_{1}(t)=t, x_{2}(t)=1$ 是系统的一个解。

(b) 证明如果 $x(0)$ 离 $\begin{bmatrix} 0 \\ 1 \end{bmatrix}$ 足够近, 那么 $x(t)$ 随 $t$ 趋于无穷而接近 $\begin{bmatrix} t \\ 1 \end{bmatrix}$ 。

4.42 考虑系统 $\dot{x} = -a[I_n + S(x) + xx^{\mathrm{T}}]x$

其中 a 是正常数, $I_{n}$ 是 $n \times n$ 单位矩阵, $S(x)$ 是依赖于 x 的斜对称矩阵。证明原点是全局指数稳定的。

4.43 考虑系统 $\dot{x}=f(x)+G(x)u$ 。假设存在正定对称矩阵 P，半正定函数 $W(x)$ ，正常数 $\gamma$ 和 $\sigma$ ，满足：

$$2 x ^ {\mathrm{T}} P f (x) + \gamma x ^ {\mathrm{T}} P x + W (x) - 2 \sigma x ^ {\mathrm{T}} P G (x) G ^ {\mathrm{T}} (x) P x \leqslant 0, \quad \forall x \in R ^ {n}$$

证明当 $u = -\sigma G^{T}(x)Px$ 时,该闭循环系统在原点有一个全局指数稳定的平衡点。

4.44 考虑系统 $\dot{x}_1 = -x_1 + x_2 + (x_1^2 + x_2^2)\sin t,$ $\dot{x}_2 = -x_1 - x_2 + (x_1^2 + x_2^2)\cos t$ 试证原点是指数稳定的，并估计吸引区。

4.45 考虑系统 $\dot{x}_{1}=h(t)x_{2}-g(t)x_{1}^{3},\quad\dot{x}_{2}=-h(t)x_{1}-g(t)x_{2}^{3}$

其中对于所有 $t \geqslant 0, h(t)$ 和 $g(t)$ 是有界连续可微函数，且 $g(t) \geqslant k > 0$ 。

(a) 平衡点 x=0 是一致渐近稳定的吗?

(b) 平衡点 x=0 是指数稳定的吗?

(c) 平衡点 x=0 是全局一致渐近稳定的吗?

(d) 平衡点 x=0 是全局指数稳定的吗?

4.46 证明系统 $\dot{x}_1 = -x_2 - x_1(1 - x_1^2 - x_2^2), \quad \dot{x}_2 = x_1 - x_2(1 - x_1^2 - x_2^2)$

的原点是渐近稳定的,它是指数稳定的吗?

4.47 考虑系统 $\dot{x}_1 = -\phi(t)x_1 + a\phi(t)x_2,\quad \dot{x}_2 = b\phi(t)x_1 - ab\phi(t)x_2 - c\psi(t)x_2^3$

其中 a, b 和 c 是正常数, $\phi(t)$ 和 $\psi(t)$ 是非负的连续有界函数, 且满足

$$\phi (t) \geqslant \phi_ {0} > 0, \quad \psi (t) \geqslant \psi_ {0} > 0, \forall t \geqslant 0$$

证明原点是全局一致渐近稳定的,它是指数稳定的吗?

4.48 两个系统的表示式分别为 $\dot{x} = f(x)$ 和 $\dot{x} = h(x)f(x)$ ，其中 $f: R^n \to R^n$ 和 $h: R^n \to R$ 都是连续可微的， $f(0) = 0, h(0) > 0$ 。证明当且仅当第二个系统的原点指数稳定时，第一个系统的原点也是指数稳定的。

4.49 试证系统 $\dot{x}_1 = -ax_1 + b,$ $\dot{x}_2 = -cx_2 + x_1(\alpha -\beta x_1x_2)$

有一个全局渐近稳定的平衡点,方程中所有系数均为正。
