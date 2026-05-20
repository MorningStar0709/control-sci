$$
\begin{array}{l} \dot {V} (S ^ {*} (t) x) = \frac {1}{2} [ (A ^ {*} S ^ {*} (t) x, S ^ {*} (t) x) + (S ^ {*} (t) x, A ^ {*} S ^ {*} (t) x) \\ \left. - \left(B B ^ {*} S ^ {*} (t), S ^ {*} (t)\right) - \left(S ^ {*} (t), B B ^ {*} S ^ {*} (t)\right) \right] \\ \leqslant - \| B ^ {*} S ^ {*} (t) x \| ^ {2}. \\ \end{array}
$$

对于任意 $y \in H$ , 由于 $\mathcal{D}(F^{*})$ 在 $X$ 中是稠密的, 故存在序列 $\{y_{n}\} \subset \mathcal{D}(A^{*})$ 使得 $\lim_{n \to \infty} y_{n} = y$ . 于是我们有

$$
\begin{array}{l} \dot {V} (y) = \overline {{\lim _ {t \rightarrow 0 ^ {+}}}} \frac {1}{t} [ V (S ^ {*} (t) y) - V (y) ] \\ = \overline {{\lim _ {t \rightarrow 0 ^ {+}}}} \lim _ {n \rightarrow \infty} \frac {1}{t} \left[ V \left(S ^ {*} (t) y _ {n}\right) - V \left(y _ {n}\right)\right] \\ = \overline {{\lim _ {t \rightarrow 0 ^ {+}}}} \lim _ {n \rightarrow \infty} \frac {1}{t} \left[ \int_ {0} ^ {t} \dot {V} (S ^ {*} (s) y _ {n}) d s \right] \\ \leqslant \overline {{\lim _ {t \rightarrow 0 ^ {+}}}} \lim _ {n \rightarrow \infty} \frac {1}{t} \left[ - \int_ {0} ^ {t} \| B ^ {*} S ^ {*} (s) y _ {n}) \| ^ {2} d s \right] \\ \leqslant - \| B ^ {*} y \| ^ {2}. \\ \end{array}
$$

因此根据定义， $V$ 是 $H$ 上一Lyapunov泛函．此外，依据假设(1)，轨线 $\mathcal{O}_S\cdot (y)$ 包含在 $H$ 的一紧集中．于是从定理10.3.4可知，当 $t\to \infty$ 时， $\forall x\in H,S^{*}(t)x\to M,$ 其中 $M$ 是 $E = \{y\in H\mid \dot{V} (y) = 0\}$ 中最大不变集.

剩下证明 $M = \{0\}$ . 事实上, 设 $y \in M$ , 则 $S^{*}(t)y \in M, \forall t \geqslant 0$ . 于是 $0 = \dot{V}(S^{*}(t)y) \leqslant -\|B^{*}S^{*}(t)y\|^2$ , 因此 $B^{*}S^{*}(t)y = 0, \forall t \geqslant 0$ . 但依据定理 10.2.7,

$$B ^ {*} S ^ {*} (t) y = 0, \quad \forall t \geqslant 0 \Longleftrightarrow B ^ {*} T ^ {*} (t) y = 0, \quad \forall t \geqslant 0.$$

于是从 $(A, B)$ 完全近似能控的假设推出 $y = 0$ , 从而 $M = \{0\}$ . 最后, 利用定理10.3.4, 我们得出结论: $S^{*}(t)$ 强稳定, 因此 $S(t)$ 是弱稳定的. 证毕.

定理10.3.6 设 $A$ 是 $H$ 上一 $C_0$ 群 $T(t)$ 的生成算子．如果

(1) 对于任意 $y \in H$ , 轨线 $\mathcal{O}_S(y)$ 包含在 $H$ 的某个 (可能与 $y$ 有关的) 紧集中;

(2) $(A, B)$ 完全近似能控；

(3) $A^{*} = -A,$

那么 $S(t)$ 是强稳定的，从而 $(A, B)$ 是强能稳的.

证明 考虑 $H$ 中泛函 $V(x) = \frac{1}{2} \| x\|^2$ . 由于 $\| T(t)\| \leqslant 1$ , 如前可证 $\dot{V}(S(t)x) \leqslant -\| B^{*}S(t)x\|^2, \forall x \in \mathcal{D}(A)$ . 利用定理 10.3.5 证明中的同样推理, 可得

$$\dot {V} (y) \leqslant - \| B ^ {*} y \| ^ {2}, \quad \forall y \in H.$$

于是从定理 10.3.4 和假设 (1) 得到，当 $t \to \infty$ 时 $S(t)y \to M$ ，其中 $M$ 是 $\Omega = \{y \in H \mid \dot{V}(y) = 0\}$ 中相对群 $S(t)$ 的最大不变集。
