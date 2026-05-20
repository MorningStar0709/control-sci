(i) 利用 $V = (1 / 2)(e_d^2 + e_q^2)$ 和比较引理，证明 $\| e\| = \sqrt{e_d^2 + e_q^2}$ 满足边界

$$\| e (t) \| \leqslant k _ {1} e ^ {- \gamma t} + k _ {2} \left| \frac {\hat {R} _ {r} - R _ {r}}{R _ {r}} \right| M I _ {q}$$

其中 $\gamma, k_{1}$ 和 $k_{2}$ 为正常数。

(j) 求在什么条件下, (f) 中设计的带有积分作用的滑模控制器, 仍能实现零稳态误差。

14.52 一个 $m$ 连杆机器人的非线性动力学方程为

$$M (q) \ddot {q} + C (q, \dot {q}) \dot {q} + D \dot {q} + g (q) = u \tag {14.120}$$

所有变量定义都与习题1.4中相同。假设 $M, C$ 和 $g$ 都是其自变量的连续函数，且对于正常数 $\lambda_{m}$ 和 $\lambda_{M}$ ，有

$$0 < \lambda_ {m} y ^ {\mathrm{T}} y \leqslant y ^ {\mathrm{T}} M (q) y \leqslant \lambda_ {M} y ^ {\mathrm{T}} y, \quad \forall q, y \in R ^ {m}, y \neq 0$$

我们想要设计一个状态反馈控制律,使 $q(t)$ 渐近跟踪参考轨线 $q_{r}(t)$ , 其中 $q_{r}(t)$ , $\dot{q}_{r}(t)$ 和 $\ddot{q}_{r}(t)$ 都是连续且有界的。本题要求设计一个滑模控制器, 取滑动曲面为

$s = \Lambda e + \dot{e} = 0$ , 其中 $\Lambda$ 为正对角阵, 并设

$$u = \hat {M} (q) v + L [ \hat {C} (q, \dot {q}) \dot {q} + \hat {g} (q) + \hat {M} (q) \ddot {q} _ {r} - \hat {M} (q) \Lambda \dot {e} ]$$

其中 $\hat{M},\hat{C}$ 和 $\hat{g}$ 分别是 M,C 和 g 的标称模型,L 或为 0 或为单位阵,分别对应两种不同的控制律。

(a) 证明 s 满足形如 $\dot{s}=v+\Delta(q,\dot{q},q_{r},\dot{q}_{r},\ddot{q}_{r},v)$

的方程,并给出当 L=0 和 L=I 时, $\Delta$ 的表达式。

(b) 假设 $\|M^{-1}(q)\hat{M}(q)-I\|_{\infty}\leqslant\kappa_{0}<1,\quad\forall q\in R^{m}$ (14.121)

证明 $\Delta_{i}$ 满足不等式 $|\Delta_{i}| \leqslant \rho(\cdot) + \kappa_{0}\|v\|_{\infty}, \quad 1 \leqslant i \leqslant m$

其中 $\rho$ 可能与 $(q, \dot{q}, q_{r}, \dot{q}_{r}, \ddot{q}_{r})$ 有关。

(c) 设 $v_{i} = -\beta(\cdot) \operatorname{sat}(s_{i}/\varepsilon), \quad \varepsilon > 0, \quad 1 \leqslant i \leqslant m$

其中 $\beta$ 可能与 $(q, \dot{q}, q_{r}, \dot{q}_{r}, \ddot{q}_{r})$ 有关。说明应如何选择 $\beta$ 才能保证误差 e 全局一致毕竟有界，并估计最终边界值与 $\varepsilon$ 的关系。

(d) 当 $\beta$ 取常数时, 证明滑模控制器具有哪些性质?

14.53 考虑上题中的 m 连杆机器人。在本题中推导出一个不同的滑模控制器 [180]，该滑模控制器用到 M-2C 的斜对称性，并免去条件 (14.121)。

(a) 取 s 与上题相同, 取 $W = (1/2)s^{\mathrm{T}}M(q)s$ 为 s 方程的备选李雅普诺夫函数。证明

$$\dot {W} = s ^ {\mathrm{T}} \left[ M \Lambda \dot {e} + C (\Lambda e - \dot {q} _ {r}) - D \dot {q} - g - M \ddot {q} _ {r} + u \right]$$

(b) 设 $u = v + L[-\hat{M}(q)\Lambda \dot{e} - \hat{C}(q,\dot{q})(\Lambda e - \dot{q}_r) + \hat{g}(q) + \hat{M}(q)\ddot{q}_r]$

其中 L=0 或 L=I，分别对应两种不同的控制律。证明

$$\dot {W} = s ^ {\mathrm{T}} [ v + \Delta (q, \dot {q}, q _ {r}, \dot {q} _ {r}, \ddot {q} _ {r}) ]$$

并给出当 L=0 和 L=I 时, $\Delta$ 的表达式。

(c) 设
