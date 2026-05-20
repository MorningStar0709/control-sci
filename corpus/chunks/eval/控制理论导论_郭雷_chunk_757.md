$$
\operatorname{rank} \left[ \begin{array}{c c c c} \langle b _ {1}, \psi_ {n 1} \rangle & \langle b _ {2}, \psi_ {n 1} \rangle & \dots & \langle b _ {m}, \psi_ {n 1} \rangle \\ \langle b _ {1}, \psi_ {n 2} \rangle & \langle b _ {2}, \psi_ {n 2} \rangle & \dots & \langle b _ {m}, \psi_ {n 2} \rangle \\ \vdots & \vdots & & \vdots \\ \langle b _ {1}, \psi_ {n r _ {n}} \rangle & \langle b _ {2}, \psi_ {n r _ {n}} \rangle & \dots & \langle b _ {m}, \psi_ {n r _ {n}} \rangle \end{array} \right] = r _ {n}. \tag {10.2.37}
$$

与完全近似能控性相类似，我们可以定义完全精确能控性、完全精确零能控性，等等.

定义 10.2.10 (A, B) 叫做完全精确能控的，是指对于任意 $x, y \in X$ ，必存在 t > 0 和 $u \in L^{p}(0, t; U)$ ， $p \geqslant 1$ ，使得

$$y = T (t) x + \int_ {0} ^ {t} T (t - s) B u (s) \mathrm{d} s.$$

(A, B) 叫做完全精确零能控的，是指对于任意 $x \in X$ ，必存在 $t > 0$ 和 $u \in L^{p}(0, t; U)$ ， $p \geqslant 1$ ，使得

$$0 = T (t) x + \int_ {0} ^ {t} T (t - s) B u (s) \mathrm{d} s.$$

(A, B) 叫做完全近似零能控的，是指对于任意 $x \in X$ 和 $\varepsilon > 0$ ，必存在 t > 0 和 $u \in L^{p}(0, t; U)$ ， $p \geqslant 1$ ，使得

$$\left\| T (t) x + \int_ {0} ^ {t} T (t - s) B u (s) \mathrm{d} s \right\| < \varepsilon .$$

定理 10.2.10 设 X, U 为两个自反 Banach 空间，那么 $(A, B)$ 完全精确能控当且仅当存在 $t_{f} > 0$ ，使得 $(A, B)$ 在 $[0, t_{f}]$ 上精确能控。

证明 设 $\| T(t)\| \leqslant Me^{\omega t},\forall t\geqslant 0.$ 于是对于任意给定的 $\varepsilon >0$ ，存在 $\alpha >0$ 使得

$$\mathrm{e} ^ {- \alpha t} \| T (t) \| \leqslant M \mathrm{e} ^ {- \varepsilon t}, \quad \forall t \geqslant 0. \tag {10.2.38}$$

我们只需证明充分性. 于是假定 $(A, B)$ 完全精确能控. 对于固定的 $p > 1$ , 定义线性算子 $G: L^{p}(0, \infty; U) \to X$ 如下:

$$G u = \int_ {0} ^ {\infty} \mathrm{e} ^ {- \alpha t} T (t) B u (t) \mathrm{d} t. \tag {10.2.39}$$

显然，由于 $(A, B)$ 完全精确能控，我们有 $\mathcal{R}(G) = X$ 。从而根据定理10.2.1，存在常数 $\gamma_1 > 0$ 使得

$$\left\| G ^ {*} x ^ {*} \right\| _ {L ^ {q} (0, \infty ; U ^ {*})} \geqslant \gamma_ {1} \| x ^ {*} \|, \quad \forall x ^ {*} \in X ^ {*}, \tag {10.2.40}$$

其中 $q$ 满足 $1 / p + 1 / q = 1$ . 但是

$$(G ^ {*} x ^ {*}) (t) = \mathrm{e} ^ {- \alpha t} B ^ {*} T ^ {*} (t) x ^ {*}, \quad 0 \leqslant t < \infty ,$$

因此

$$\left(\int_ {0} ^ {\infty} \mathrm{e} ^ {- \alpha q t} \| B ^ {*} T ^ {*} (t) x ^ {*} \| _ {U ^ {*}} ^ {q} \mathrm{d} t\right) ^ {\frac {1}{q}} \geqslant \gamma_ {1} \| x ^ {*} \| _ {X ^ {*}}, \quad \forall x ^ {*} \in X ^ {*}. \tag {10.2.41}$$

从式 (10.2.38) 和式 (10.2.41) 可知存在两个正常数 $t_f$ 和 $\gamma, 0 < \gamma < \gamma_1$ 使得

$$\left(\int_ {0} ^ {t _ {f}} \mathrm{e} ^ {- \alpha q t} \| B ^ {*} T ^ {*} (t) x ^ {*} \| _ {U ^ {*}} ^ {q} \mathrm{d} t\right) ^ {\frac {1}{q}} \geqslant \gamma \| x ^ {*} \| _ {X ^ {*}}, \quad \forall x ^ {*} \in X ^ {*}.$$

于是我们得到
