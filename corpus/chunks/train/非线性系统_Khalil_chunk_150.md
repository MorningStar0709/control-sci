(b) 试证 $V(x) = \int_{0}^{x_1} h_1(y) dy + x_2^2 / 2 + \int_{0}^{x_3} h_2(y) dy$ 对于所有 $x \in R^3$ 都是正定的。

(c) 试证原点是渐近稳定的。

(d) $h_{1}$ 和 $h_{2}$ 在什么条件下才能证明原点是全局渐近稳定的。

4.16 试证系统 $\dot{x}_1 = x_2, \quad \dot{x}_2 = -x_1^3 - x_2^3$

的原点是全局渐近稳定的。

4.17 (见文献[77]) 李纳(Liénard) 方程

$$\ddot {y} + h (y) \dot {y} + g (y) = 0$$

其中 g 和 h 是连续可微的。

(a) 利用 $x_{1}=y$ 和 $x_{2}=\dot{y}$ ，写出状态方程并找出有关 g 和 h 的条件，以确保原点是孤立的平衡点。

(b) 把 $V(x)=\int_{0}^{x_{1}}g(u)dy+(1/2)x_{2}^{2}$ 当成李雅普诺夫函数, 找出有关 g 和 h 的条件, 以确保原点是渐近稳定的。

(c) 令 $V(x) = (1/2)\left[x_2 + \int_{0}^{x_1} h(y) dy\right]^2 + \int_{0}^{x_1} g(y) dy$ ，重新证明问题(b)。

4.18 利用 $M\ddot{y} = Mg - ky - c_1\dot{y} - c_2\dot{y} |\dot{y}|$

来模拟习题 1.12 中的质量-弹簧系统,试证此系统有全局渐近稳定的平衡点。

4.19 在习题 1.4 中有一个 m 连杆机器人的运动方程。假设 $P(q)$ 是 q 的正定函数，且 $g(q)=0$ 有一个孤立根 q=0。

(a) 令 u=0，用总能量函数 $V(q,\dot{q})=\frac{1}{2}\dot{q}^{\mathrm{T}}M(q)\dot{q}+P(q)$ 作为李雅普诺夫函数，试证原点 $(q=0,\dot{q}=0)$ 是稳定的。

(b) 令 $u = -K_{d} \dot{q}$ ，其中 $K_{d}$ 是正对角矩阵，试证原点是渐近稳定的。

(c) 令 $u = g(q) - K_p(q - q^*) - K_d\dot{q}$ , 其中 $K_p$ 和 $K_d$ 是正对角矩阵, $q^*$ 是 $R^m$ 内所期望的机器人位置, 试证点 $(q = q^*, \dot{q} = 0)$ 是渐近稳定的平衡点。

4.20 假设 LaSalle 定理中的集合 $M$ 由有限个孤立点组成。试证极限 $\lim_{t\to \infty}x(t)$ 存在并等于这些点中的一个。

4.21 （见文献[81]）梯度系统是一个形为 $\dot{x} = -\nabla V(x)$ 的动力学系统，其中 $\nabla V(x) = [\partial V/\partial x]^{\mathrm{T}}$ ， $V: D \subset R^{n} \to R$ 是二阶连续可微的。

(a) 试证对于所有 $x \in D$ 有 $\dot{V}(x) \leqslant 0$ ，并当且仅当 x 是平衡点时有 $\dot{V}(x) = 0$ 。

(b) 取 $D = R^{n}$ ，假设对于每个 $c \in R$ ，区间 $\Omega_{c} = \{x \in R^{n} \mid V(x) \leqslant c\}$ 是封闭的。试证该系统的每个解都定义在 $t \geqslant 0$ 上。

(c) 继续(b)，假设除了有限的点 $p_{1},\cdots,p_{r}$ 外， $\nabla V(x)\neq0$ 。试证对于每个解 $x(t)$ ，极限 $\lim_{t\to\infty}x(t)$ 存在且等于这些点中的某一个。

4.22 设有李雅普诺夫方程 $PA + A^{\mathrm{T}}P = -C^{\mathrm{T}}C$ ，其中 $(A,C)$ 对是可观测的。试证当且仅当存在满足该方程的 $P = P^{\mathrm{T}} > 0, A$ 是赫尔维茨的。而且，证明如果 $A$ 是赫尔维茨的，那么李雅普诺夫方程有唯一解。

提示:运用 LaSalle 定理,并回想对于可得到的矩阵对 $(A,C)$ ,当且仅当 x=0 时有向量 $C\exp(At)x\equiv0\forall t$ 。

4.23 线性系统 $\dot{x} = (A - BR^{-1}B^{\mathrm{T}}P)x$ ，其中 $P = P^{\mathrm{T}} > 0$ ，满足里卡蒂(Riccati)方程

$$P A + A ^ {\mathrm{T}} P + Q - P B R ^ {- 1} B ^ {\mathrm{T}} P = 0$$

$R = R^{T} > 0$ , 并且 $Q = Q^{T} \geqslant 0$ 。用 $V(x) = x^{T}Px$ 作为李雅普诺夫函数, 证明在下列条件下原点是全局渐近稳定的。

(1) Q > 0。  
(2) $Q = C^{T}C, (A, C)$ 对是可观测的；参见习题 4.22 的提示。

4.24 考虑系统① $\dot{x} = f(x) - kG(x)R^{-1}(x)G^{\mathrm{T}}(x)\left(\frac{\partial V}{\partial x}\right)^{\mathrm{T}}$

其中 $V(x)$ 是连续可微且正定的函数，并满足Hamilton-Jacobi-Bellman方程
