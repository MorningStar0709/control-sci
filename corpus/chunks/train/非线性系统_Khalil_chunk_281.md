# 9.7 习题

9.1 ([见文献150]) 考虑李雅普诺夫方程 $PA + A^{T}P = -Q$ ，其中 $Q = Q^{T} > 0, A$ 是赫尔维茨矩阵。设 $\mu(Q) = \lambda_{\min}(Q) / \lambda_{\max}(P)$ ，

(a) 证明对于任何正常数 k，有 $\mu(kQ) = \mu(Q)$ 。  
(b) 设 $\hat{Q} = \hat{Q}^{T} >$ 时，有 $\lambda_{\min}(\hat{Q}) = 1$ 。证明 $\mu(I) \geqslant \mu(\hat{Q})$ 。  
(c) 证明 $\mu(I) \geqslant \mu(Q), \forall Q = Q^{T} > 0$ 。

提示: 在(b)中, 设 $P_{1}$ 和 $P_{2}$ 分别是当 Q = I 和 $Q = \hat{Q}$ 时李雅普诺夫方程的解, 证明

$$P _ {1} - P _ {2} = \int_ {0} ^ {\infty} \exp (A ^ {\mathrm{T}} t) (I - \hat {Q}) \exp (A t) d t \leqslant 0$$

9.2 考虑系统 $\dot{x} = Ax + Bu$ ，并设 $u = -Fx$ 是一个稳定状态反馈控制，即矩阵 $(A - BF)$ 是赫尔维茨的。假设由于物理因素限制必须用限幅器把 $u_i$ 的值限制到 $|u_i(t)| \leqslant L$ 。闭环系统可以用 $\dot{x} = Ax - BL \operatorname{sat}(Fx / L)$ 表示，其中 $\operatorname{sat}(v)$ 是一个向量，其第 $i$ 个分量是饱和函数。通过同时加减一项 $BFx$ ，闭环状态方程可重写为 $\dot{x} = (A - BF)x - Bh(Fx)$ ，其中 $h(v) = L\operatorname{sat}(v / L) - v$ 。这样，限幅器的作用就可以看成没有限幅器时标称系统的一个扰动。

(a) 证明 $|h_i(v)| \leqslant \frac{\delta}{(1 + \delta)} |v_i|, \forall |v_i| \leqslant L(1 + \delta)$

其中 $\delta > 0$ 。

(b) 设 $P$ 是 $P(A - BF) + (A - BF)^{\mathrm{T}}P = -I$

的解。证明如果 $\delta / (1 + \delta) < 1 / (2 \| PB \|_2 \| F \|_2)$ ，则 $V(x) = x^{\mathrm{T}}Px$ 沿闭环系统轨线的导数在整个区域 $|F(x)_i| \leqslant L(1 + \alpha), \forall i$ 上是负定的。

(c) 证明原点是渐近稳定的,并讨论如何估计吸引区。

(d) 把(c)得到的结果应用到

$$
A = \left[ \begin{array}{c c} {0} & {1} \\ {0. 5} & {1} \end{array} \right], B = \left[ \begin{array}{l} {0} \\ {1} \end{array} \right], F = \left[ \begin{array}{l l} {1} & {2} \end{array} \right], L = 1
$$

时的情况,并估计吸引区。
