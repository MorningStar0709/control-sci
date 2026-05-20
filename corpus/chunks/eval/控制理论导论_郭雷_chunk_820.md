# 无穷时间区间上的调节问题

现在我们考虑如下无穷区间上的二次性能泛函：

$$J (u, x _ {0}) = \int_ {0} ^ {\infty} \left[ (Q x (t), x (t)) + (R u (t), u (t)) \right] d t, \tag {10.6.21}$$

这里 $x(t)$ 是如下线性系统的温和解：

$$\frac {\mathrm{d} x}{\mathrm{d} t} = A x (t) + B u (t), \tag {10.6.22}$$

而 $u \in L^2(\mathbb{R}^+; U), \mathbb{R}^+ = [0, \infty), A, B, Q, R$ 如前所述.

下面设 $\{t_n\}$ 是一单调递增的正数列，使得当 $n \to \infty$ 时 $t_n \to \infty$ 。设 $P_n(t)$ 表示内积 Riccati 方程 (10.6.18) 在 $[0, t_n]$ 上满足 $P_n(t_n) = 0$ 的唯一解。

假设 $A$ : 对于每一 $x \in H$ , 存在 $u \in L^{2}(\mathbb{R}^{+}; U)$ 使得 $J(u, x) < \infty$ .

引理10.6.3 在假设 $A$ 之下，对于任意 $t \in \mathbb{R}^+$ ，算子序列 $\{P_n(t)\}$ 强收敛于一对称算子 $P \in \mathcal{L}(H)$ ，并且 $\| P_n(t) \| \leqslant \| P \|, \forall n \geqslant 1, \forall t \geqslant 0$ ；此外， $P$ 满足如下内积 Riccati 代数方程：

$$(P A x, y) + (x, P A y) + (Q x, y) = \left(B R ^ {1} B ^ {*} P x, P y\right), \quad \forall x, y \in \mathcal {D} (A). \tag {10.6.23}$$

证明 设 $x, y \in H$ . 根据假设 $A$

$$\sup _ {n \geqslant 1} | (P _ {n} (t) x, x) | < \infty , \quad \forall t \geqslant 0.$$

于是利用 Schwarz 不等式，我们有

$$(P _ {n} (t) x, y) ^ {2} \leqslant (P _ {n} (t) x, x) (P _ {n} (t) y, y) \leqslant C (t, x, y),$$

其中 $C(t,x,y)$ 与 $\pmb{n}$ 无关．这样，依据一致有界性原理，上式意味着

$$\sup _ {n \geqslant 1} \| P _ {n} (t) \| < \infty , \quad \forall t \geqslant 0.$$

由于当 $n \geqslant m$ 时 $P_{n}(t) \geqslant P_{m}(t)$ , 故存在一对称算子 $P(t) \in \mathcal{L}(H)$ 使得当 $n \to \infty$ 时 $P_{n}(t)$ 强收敛于 $P(t)$ . 然而, 从引理10.6.1和方程(10.6.16)可知对于任意 $t, t' \in \mathbb{R}^{+}$ , 有

$$(P (t) x, x) = \lim _ {n \rightarrow \infty} (P _ {n} (t) x, x) = \lim _ {n \rightarrow \infty} (P _ {n} (t ^ {\prime}) x, x) = (P (t ^ {\prime}) x, x), \quad \forall x \in H.$$

这表明 $P(t)$ 与 $t$ 无关. 记 $P = P(t)$ . 由于 $P - P_{n}(t) \geqslant 0$ , 我们有 $\|P_{n}(t)\| \leqslant \|P\|$ , $\forall n \geqslant 1, \forall t \geqslant 0$ .

另一方面，从定理10.6.5知 $P_{n}(t)$ 满足如下内积微分方程：

$$
\left\{ \begin{array}{l} \frac {d}{\mathrm{d} t} (P _ {n} (t) x, y) + (P _ {n} (t) x, A y) + (A x, P _ {n} (t) y) + (Q x, y) \\ = (B R ^ {- 1} B ^ {*} P _ {n} (t) x, P _ {n} (t) y), \qquad \forall t \in (0, t _ {n}), \forall x, y \in \mathcal {D} (A), \\ P _ {n} (t _ {n}) = 0. \end{array} \right.
$$

对于任意固定的 $t \geqslant 0$ , 在上述方程中让 $n \to \infty$ 取极限即得式 (10.6.23). 证毕.

定理 10.6.6 设假设 A 成立，P 是引理 10.6.3 中建立的对称算子.

(1) 用 $S(t)$ 表示由 $A - BR^{-1}B^{*}P$ 生成的 $C_0$ 半群，那么

$$S (t) x = T (t) x - \int_ {0} ^ {t} T (t - s) B R ^ {- 1} B ^ {*} P S (s) x \mathrm{d} s, \quad \forall x \in H; \tag {10.6.24}$$

(2) 如果记 $x(t, x_0) = S(t)x_0$ ，并设 $x_n(t, x_0)$ 是如下积分方程的温和解：
