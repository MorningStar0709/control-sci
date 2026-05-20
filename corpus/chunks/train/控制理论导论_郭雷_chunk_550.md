# 线性二次最优调节逆问题

对于线性定常控制系统

$$\dot {x} = A x + B u, \quad x \in \mathbb {R} ^ {n}, u (t) \in \mathbb {R} ^ {r}, \tag {7.3.44}$$

其二次最优调节逆问题是指，给定式(7.3.44)的一个线性定常状态反馈控制规律 $u = -K_{1}x, K_{1}$ 为 $r \times n$ 矩阵，寻找 $n \times n$ 半正定对称矩阵 $Q_{1}$ 和 $r \times r$ 正定对称矩阵 $R_{1}$ ，使得 $u = -K_{1}x$ 正好是在二次性能指标

$$J ^ {1} [ u ] = \frac {1}{2} \int_ {0} ^ {+ \infty} \left[ x ^ {\mathrm{T}} (t) Q _ {1} x (t) + u ^ {\mathrm{T}} (t) R _ {1} u (t) \right] \mathrm{d} t \tag {7.3.45}$$

下的最优控制综合函数。线性定常系统二次最优调节逆问题通常简称为“逆问题”或“反问题”。下面给出与“逆问题”可解性密切相关的正实性与正实引理。为简单起见，令 $R_{1} = I_{r}$ 。

定义7.3.2 设 $Z(s)$ 是有理分式矩阵， $s$ 为复变量。如果 $Z(s)$ 满足

(1) $Z(s)$ 的每个元都在右半复平面： $\operatorname{Re}(s) > 0$ 内解析；  
(2) $\omega \in \mathbb{R}$ , 只要 $j\omega$ 不是 $Z(s)$ 的任何元的极点, 则有 $Z^{\mathrm{H}}(\mathrm{j}\omega) + Z(\mathrm{j}\omega) \geqslant 0$ , 这里“H”表示矩阵的复共轭转置, $\mathrm{j}^{2} = -1$ ;  
(3) 若 $j\omega_0$ 是 $Z(s)$ 的某个元的极点，则它是简单极点，其留数矩阵是半正定的 Hermite 矩阵，则称 $Z(s)$ 为正实的.

考察关于未知矩阵 $P, L$ 的方程

$$
\left\{ \begin{array}{l} P A + A ^ {\mathrm{T}} P = - L L ^ {\mathrm{T}}, \\ P B = K, \end{array} \right. \tag {7.3.46}
$$

其中 $A \in \mathbb{R}^{n \times n}$ , $B \in \mathbb{R}^{n \times r}$ 和 $K \in \mathbb{R}^{n \times r}$ 为已知常矩阵.

引理 7.3.4(正实引理) 设 $(A, B)$ 完全能控， $(A, K^{\mathrm{T}})$ 完全能观测，则 (7.3.46) 有解 $P \in R^{n \times n}, L \in R^{n \times l}$ ，且 P > 0 的充要条件是 $r \times r$ 实有理分式矩阵 $K^{\mathrm{T}}(sI_{n} - A)^{-1}B$ 是正实的，l 为某非负整数.

该引理的证明详见文献 [5].

下面考察线性二次最优调节逆问题的解. 限于篇幅, 这里仅涉及某些基本结果.

定理 7.3.8 对于线性定常系统 (7.3.44)，给定线性反馈控制规律 $u = -K^{T}x$ ，假定 $(A, B)$ 完全能控， $(A, K^{\mathrm{T}})$ 完全能观测，且 $K^{\mathrm{T}}(sI_{n} - A)^{-1}B$ 是正实的，那么存在 $Q_{1} \geqslant 0$ ，使得 $u = -K^{T}x$ 正是式 (7.3.44) 在性能指标

$$J ^ {1} [ u ] = \frac {1}{2} \int_ {0} ^ {+ \infty} \left[ x ^ {\mathrm{T}} (t) Q _ {1} x (t) + u ^ {\mathrm{T}} (t) u (t) \right] \mathrm{d} t \tag {7.3.47}$$

下的最优控制综合函数 (最优调节器).

证明 由于 $K^{\mathrm{T}}(sI_n - A)^{-1}B$ 是正实的，根据引理7.3.4, 存在 $n \times n$ 正定对称矩阵 $P$ 和 $n \times l$ 矩阵 $L$ , 满足

$$P A + A ^ {\mathbf {T}} P = - L L ^ {\mathbf {T}}, \tag {7.3.48}P B = K. \tag {7.3.49}$$

从式 (7.3.48) 和式 (7.3.49) 可得

$$P A + A ^ {\mathrm{T}} P - P B B ^ {\mathrm{T}} P = - \left(L L ^ {\mathrm{T}} + K K ^ {\mathrm{T}}\right). \tag {7.3.50}$$

显然 $LL^{\mathrm{T}} + KK^{\mathrm{T}}\geqslant 0$ ，且是对称的．于是存在 $n\times l$ 矩阵 $C_1,l = \mathrm{rank}C_1$ ，使得 $LL^{\mathrm{T}} + KK^{\mathrm{T}} = C_1C_1^{\mathrm{T}}$ .于是

$$P A + A ^ {\mathrm{T}} P + C _ {1} C _ {1} ^ {\mathrm{T}} - P B B ^ {\mathrm{T}} P = 0. \tag {7.3.51}$$
