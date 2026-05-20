# 习题 9.5

9.5.1 考虑系统 (9.5.1) 设控制律由式 (9.5.14)(或式 (9.5.15)) 所定义，但参数估计值 $\theta_{n}$ 由 WLS 算法 (9.2.25)\~(9.2.28) 所给出。证明：在条件 (A1)\~(A3) 下有

$$R _ {n} = o (n), \quad \text { a.s. }$$

其中 $R_{n}$ 由式 (9.5.16) 所定义，而 $\delta > 0$ 由式 (9.2.28) 所定义.

9.5.2 设 $x_{k} \in \mathbb{R}^{d}, (d > 0), k \geqslant 0$ 是一个向量序列，且对任何 $k < 0$ 有 $x_{k} \equiv 0$ . 对任意一个非零多项式 $F(z)$ ，记 $\bar{x}_{k} = F(z)x_{k}$ ，证明：存在常数 $c > 0$ 使对任何 $n \geqslant 0$ 有

$$\lambda_ {\min} \left(\sum_ {k = 0} ^ {n} x _ {k} x _ {k} ^ {\mathrm{T}}\right) \geqslant c \lambda_ {\min} \left(\sum_ {k = 0} ^ {n} \bar {x} _ {k} \bar {x} _ {k} ^ {\mathrm{T}}\right).$$

9.5.3 考虑由式 (9.5.11)\~(9.5.15) 所定义的 LS 自校正调节器。证明：若噪声 $\{w_{n}\}$ 的所有的有穷维分布关于 Lebesgue 测度是绝对连续的，则必有

$$P (b _ {1 n} \neq 0) = 1, \quad \forall n \geqslant 1.$$

(提示：可参考文献 [5] 或文献 [37].)

9.5.4 考虑系统 (9.5.1) 及由式 (9.5.16) 所定义的 $R_{n}$ . 设本节条件 (A1) 和 (A3) 满足且 $B(z)$ 与 $A(z) - 1$ 互质, $|a_{p}| + |b_{p}| \neq 0$ . 进一步, 假设闭环系统是最优的, 即 $R_{n} = o(n)$ , a.s. 证明: 对由式 (9.5.19) 所定义的 $(p + q - 1)$ 维回归 $\phi_{n}$ 必满足下列持续激励条件:

$$\liminf _ {n \to \infty} \lambda_ {\min} \left\{\frac {1}{n} \sum_ {i = 0} ^ {n} \phi_ {i} \phi_ {i} ^ {\mathrm{T}} \right\} > 0, \qquad \text { a.s. }$$

9.5.5 考虑系统 (9.5.1). 设本节条件 (A1)\~(A2) 满足且 $B(z)$ 与 $A(z)-1$ 互质, $\left|a_{p}\right|+\left|b_{q}\right|\neq0$ , $w_{n}^{2}=O(n^{\epsilon})$ , $\forall\epsilon>0$ , a.s. 若 LS 自校正调节器定义为

$$
u _ {n} = \frac {1}{\hat {b} _ {1 n}} \left\{b _ {1 n} u _ {n} - \theta_ {n} ^ {\mathrm{T}} \phi_ {n} \right\},
\hat {b} _ {1 n} = \left\{ \begin{array}{l l} b _ {1 n}, & \text {若} | b _ {1 n} | \geqslant \frac {1}{\sqrt {n \log (n + 1)}}, \\ b _ {1 n} + \frac {\mathrm{sgn} (b _ {1 n})}{\sqrt {n \log (n + 1)}}, & \text {若上式不成立,} \end{array} \right.
$$

其中 $\phi_{n}$ 和 $\theta_{n}$ 分别由式 (9.5.3) 和式 (9.5.11) 所定义，而 $b_{1n}$ 是由 LS 估计 $\theta_{n}$ 给出的对 $b_{1}$ 的估计。证明

$$\sum_ {i = 0} ^ {n} (y _ {i} - w _ {i}) ^ {2} = o (n ^ {\epsilon}), \quad \text { a.s. } \quad \forall \epsilon > 0.$$

(提示：可参考文献 [14].)

9.5.6 对系统 (9.5.1), 设条件 (A1)\~(A3) 满足, 且 $b_{1} > 0$ . 考虑下列投影的 LS 算法

$$\hat {\theta} _ {n + 1} = \pi_ {n} \left\{\hat {\theta} _ {n} + a _ {n} P _ {n} \phi_ {n} \left(y _ {n + 1} - \phi_ {n} ^ {T} \hat {\theta} _ {n}\right) \right\},$$

其中 $a_{n}, \phi_{n}, P_{n}$ 与 LS 算法 (9.5.11)\~(9.5.13) 中定义一样，而投影算法 $\pi_{n}\{\cdot\}$ 定义为

$$\pi_ {n} \{\cdot \} = \underset {y \in D _ {n}} {\operatorname{argmin}} \| P _ {n + 1} ^ {- \frac {1}{2}} (x - y) \|, \quad x \in \mathbb {R} ^ {p + q},$$

而
