$$
\widetilde {u} (\tau) = \left\{ \begin{array}{l l} u ^ {0} (\tau), & t \leqslant \tau \leqslant t _ {1}, \\ 0, & t _ {1} <   \tau <   \infty , \end{array} \right.
\widetilde {x} (\tau) = T (\tau - t) x + \int_ {t} ^ {\tau} T (\tau - s) B \widetilde {u} (s) d s, \quad \forall \tau \geqslant t.
$$

于是根据引理10.6.1，我们得到

$$
\begin{array}{l} m (t, t _ {1}, x) \leqslant m (t, \tau_ {n}, x) \leqslant J (\tilde {u}; t, \tau_ {n}, x) = m (t, t _ {1}, x) + (G \tilde {x} (\tau_ {n}), \tilde {x} (\tau_ {n})) \\ - \left(G \widetilde {x} \left(t _ {1}\right), \widetilde {x} \left(t _ {1}\right)\right) + \int_ {t _ {1}} ^ {\tau_ {n}} \left(Q \widetilde {x} (s), \widetilde {x} (s)\right) d s. \tag {10.6.17} \\ \end{array}
$$

由于 $\widetilde{x} (\cdot)$ 连续，并且当 $n\to \infty$ 时 $\tau_{n}\rightarrow t_{1}$ ，故从式(10.6.17）可知当 $n\to \infty$ 时 $m(s_n,t_1,x)\to m(t,t_1,x)$ .这样我们证明了 $m(t,t_1,x)$ 是 $t\in [t_0,t_1)$ 的连续函数．证毕.

定理 10.6.4 $P(t)$ 在 $[t_{0}, t_{1})$ 是强连续的.

证明 根据引理 10.6.2, $\|P(t)\|\leqslant\mu_{5}$ ，这里常数 $\mu_{5}$ 与 $t\in[t_{0},t_{1})$ 无关。再利用引理 10.6.2，对于每一 $x\in H$ 和 $t,t'\in[t_{0},t_{1}), t\leqslant t'$ ，我们有

$$
\begin{array}{l} \left\| \left(P (t) - P \left(t ^ {\prime}\right)\right) x \right\| ^ {4} = \left(\left(P (t) - P \left(t ^ {\prime}\right)\right) x, \left(P (t) - P \left(t ^ {\prime}\right)\right) x\right) ^ {2} \\ \leqslant \left(P (t) - P \left(t ^ {\prime}\right)\right) x, x) \left(\left(P (t) - P \left(t ^ {\prime}\right)\right) ^ {2} x, \left(P (t) - P \left(t ^ {\prime}\right)\right) x\right) \\ = \left[ m \left(t, t _ {1}, x\right) - m \left(t ^ {\prime}, t _ {1}, x\right) \right] \left(\left(P (t) - P \left(t ^ {\prime}\right)\right) ^ {2} x, \left(P (t) - P \left(t ^ {\prime}\right)\right) x\right) \\ \leqslant 8 \mu_ {5} ^ {3} [ m (t, t _ {1}, x) - m (t ^ {\prime}, t _ {1}, x) ] \| x \| ^ {2}. \\ \end{array}
$$

但从引理10.6.2可知， $m(t,t_1,x)$ 对于 $t\in [t_0,t_1)$ 是连续的，故从上述不等式推出 $P(t)$ 在 $[t_0,t_1)$ 上是连续的．证毕.

定理10.6.5 $P(t)$ 是区间 $[t_0, t_1)$ 上如下内积Riccati方程在 $\mathcal{L}(H)$ 的强连续自伴算子类中的唯一解

$$
\left\{ \begin{array}{l} \frac {\mathrm{d}}{\mathrm{d} t} (P (t) x, y) + (P (t) x, A y) + (A x, P (t) y) + (Q x, y) \\ = (B R ^ {- 1} B ^ {*} P (t) x, P (t) y), \quad \forall t \in (t _ {0}, t _ {1}), \forall x, y \in \mathcal {D} (A), \\ P (t _ {1}) = G. \end{array} \right. \tag {10.6.18}
$$
