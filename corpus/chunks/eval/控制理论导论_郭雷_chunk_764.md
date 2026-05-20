(3) 存在非负对称算子 $P \in \mathcal{L}(H)$ 满足 Riccati 方程

$$2 \operatorname{Re} (P A x, x) + (x, x) - \left(P B B ^ {*} P x, x\right) = 0, \quad \forall x \in \mathcal {D} (A); \tag {10.3.9}$$

(4) 对于任意初值 $x_0 \in H$ , 存在 $u \in L^2(0, \infty; U)$ 使得 $u(t)$ 和式 (10.3.1) 的对应于控制 $u$ 和初值 $x_0$ 的温和解 $x(t)$ 当 $t \to \infty$ 时按指数收敛于零.

证明 $(1) \Longrightarrow (2)$ . 由于 $(A, B)$ 指数能稳，存在 $K \in \mathcal{L}(H, U)$ 使得 $S(t) = T^{A - BK}(t)$ 是指数稳定的. 令 $u(t) = KS(t)x_0$ 和 $x(t) = S(t)x_0$ , 则

$$x (t) = T (t) x _ {0} + \int_ {0} ^ {t} T (t - s) B u (s) \mathrm{d} s,$$

即 $x(t)$ 是式 (10.3.1) 的温和解. 由于 $\| S(t)\| \leqslant Me^{-\alpha t}$ , 其中 $M$ 和 $\alpha$ 为正常数, 从而显然式 (10.3.8) 成立.

(2) $\Longrightarrow$ (3). 在条件 (2) 之下，根据引理 10.6.3(其证明与这里的结果是独立的)，存在一非负对称算子 $P \in \mathcal{L}(H)$ 满足 Riccati 方程 (10.3.9).

(3) $\Longrightarrow$ (1). 设非负对称算子 $P \in \mathcal{L}(H)$ 满足方程 (10.3.9). 令 $K = B^{*}P$ , 则

$$2 \operatorname{Re} (P (A - B K) x, x) + (x, x) + (K ^ {*} K x, x) = 0, \quad \forall x \in \mathcal {D} (A).$$

利用引理 10.3.1, $T^{A-BK}(t)$ 是指数稳定的.

最后， $(1)\Longrightarrow (4)$ 和 $(4)\Longrightarrow (2)$ 是直接的．证毕.

当一个无穷维线性系统渐近稳定但不指数稳定的时候，自然会问，我们是否能通过某个紧反馈控制使得相应的闭环系统指数稳定？答案是否定的，因为我们有如下定理。（见文献[14]）

定理10.3.3 设 $T(t)$ 是无穷维Hilbert空间 $H$ 上一强稳定的 $C_0$ 压缩半群，生成算子为 $A$ . 设 $B \in \mathcal{L}(H)$ 是紧算子，并且 $S(t)$ 是 $A + B$ 生成的 $C_0$ 半群。那么如果 $S(t)$ 是指数稳定的，则 $T(t)$ 也必是指数稳定的。

证明 设 $S(t)$ 是指数稳定的，但 $T(t)$ 不是指数稳定的，我们设法导出矛盾。为简单起见，设 $H$ 是可分的，则 $B$ 可以用其在有穷维子空间上的投影按 $\mathcal{L}(H)$ 中度量任意逼近。对于 $H$ 的任意有穷维子空间 $H_{n}$ ，记 $P_{n}$ 是从 $H$ 到 $H_{n}$ 的直交投影， $B_{n} = P_{n}BP_{n}$ ，不妨设 $\lim_{n\to \infty}\| B_n - B\| = 0$ 。我们证明由 $A + B_{n}$ 生成的 $C_0$ 半群 $S_{n}(t)$ 不是指数稳定的。

事实上，我们有

$$S _ {n} (t) x = T (t) x + \int_ {0} ^ {t} S _ {n} (t - s) B _ {n} T (s) x \mathrm{d} s, \qquad \forall x \in H, t \geqslant 0. \tag {10.3.10}$$

假定存在常数 $M > 0$ 使得

$$\| S _ {n} (t) \| \leqslant M, \quad t \geqslant 0,$$

则从式 (10.3.10) 得到

$$\| S _ {n} (t) x \| \geqslant \| T (t) x \| - M t \sup _ {0 \leqslant s \leqslant t} \| B _ {n} T (s) x \|, \quad t \geqslant 0, x \in H. \tag {10.3.11}$$

任取 $t_1 > 0$ ，选择 $\varepsilon$ 使得 $0 < \varepsilon < \min \{1/2, Mt_1 \| B_n\|\}$ ，并令 $\delta = \varepsilon / (2Mt_1 \| B_n\|)$ 。由于 $H_n$ 是有穷维的，并且 $T(t)$ 是强稳定的，故存在 $t_0 > 0$ 使得

$$\sup \left\{\| T (t) x \| \mid x \in H _ {n}, \| x \| = 1 \right\} \leqslant \frac {\delta^ {2}}{4}, \quad \forall t \geqslant t _ {0}.$$

由于 $T(t)$ 是 $C_0$ 压缩半群，并且不是指数稳定的，故存在 $x_1 \in H, \| x_1 \| = 1$ ，使得
