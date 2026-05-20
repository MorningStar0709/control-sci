$$
\begin{array}{l} \frac {1}{2} x ^ {\mathrm{T}} P (t; t _ {f}, 0) x = \frac {1}{2} \int_ {t} ^ {t _ {f}} [ x ^ {*} (\tau) Q (\tau) x ^ {*} (\tau) + u ^ {*} (\tau) R (\tau) u ^ {*} (\tau) ] \mathrm{d} \tau \stackrel {\text { def }} {=} J ^ {*} (t, x; t _ {f}) \\ \leqslant J [ \bar {u} (\cdot); t, x, t _ {f} ] \leqslant J [ \bar {u} (\cdot); t, x, + \infty ] \\ = J [ \bar {u} (\cdot); t, x, t _ {2} ], \\ \end{array}
$$

其中 $u^{*}(\tau), x^{*}(\tau)$ 是相应的最优控制和最优轨线。从上式可知 $P(t; t_{f}, 0)$ 的每个元 $P_{ij}(t; t_{f}, 0)$ 都有上界。

设 $\bar{t}_f > t_f$ ，并令 $(\bar{u}^*(\tau), \bar{x}^*(\tau))$ 表示在 $t$ 时刻以 $x$ 为初态的 $[t, \bar{t}_f]$ 上的最优解。于是有

$$
\begin{array}{l} \frac {1}{2} x ^ {\mathrm{T}} P (t; t _ {f}, 0) x = \frac {1}{2} \int_ {t} ^ {t _ {f}} \left[ x ^ {* ^ {\mathrm{T}}} (s) Q (s) x ^ {*} (s) + u ^ {* ^ {\mathrm{T}}} (s) R (s) u ^ {*} (s) \right] \mathrm{d} s \\ \leqslant \frac {1}{2} \int_ {t} ^ {t _ {f}} \left[ \bar {x} ^ {* ^ {\mathrm{T}}} (s) Q (s) \bar {x} ^ {*} (s) + \bar {u} ^ {* ^ {\mathrm{T}}} (s) R (s) \bar {u} ^ {*} (s) \right] d s \\ \leqslant \frac {1}{2} \int_ {t} ^ {\bar {t} _ {f}} \left[ \bar {x} ^ {* ^ {\mathrm{T}}} (s) Q (s) \bar {x} ^ {*} (s) + \bar {u} ^ {* ^ {\mathrm{T}}} (s) R (s) \bar {u} ^ {*} (s) \right] \mathrm{d} s \\ = \frac {1}{2} x ^ {\mathrm{T}} P (t; \bar {t} _ {f}, 0) x, \quad \forall x \in \mathbb {R}. \\ \end{array}
$$

从上式可得， $\forall 1\leqslant i,j\leqslant n,i <   j,$

$$p _ {i i} (t; t _ {f}, 0) \leqslant p _ {i i} (t; \ddot {t} _ {f}, 0),p _ {i i} (t; t _ {f}, 0) + 2 p _ {i j} (t; t _ {f}, 0) + p _ {j j} (t; t _ {f}) \leqslant p _ {i i} (t; \bar {t} _ {f}, 0) + 2 p _ {i j} (t; \bar {t} _ {f}, 0) + p _ {j j} (t; \bar {t} _ {f}, 0).$$

由此可推出存在 $\bar{p}_{ij}(t)$ 使得

$$\bar {p} _ {i j} (t) = \lim _ {t _ {f} \rightarrow \infty} P _ {i j} (t; t _ {f}, 0), \quad 1 \leqslant i, j \leqslant n.$$

于是若记 $\bar{P}(t) = [\bar{p}_{ij}(t)]$ ，则

$$\bar {P} (t) = \lim _ {t _ {f} \rightarrow \infty} P (t; t _ {f}, 0).$$

再证 $\bar{P}(t)$ 满足方程 (7.3.10) 中矩阵微分方程。对任意 $t \leqslant \bar{t}_f < t_f$ ，由常微分方程终值问题解的唯一性得

$$P (t; t _ {f}, 0) = P (t: \bar {t} _ {f}, P (\bar {t} _ {f}; t _ {f}, 0))$$

(图 7.3.1).

![](image/49e352ff4dc7679dbf14e0efbc713ea3f3676438ad7adc97e51d7605b7d42293.jpg)

<details>
<summary>line</summary>

| t | P(t; t_f, 0) | P(t̄_f; t_f, 0) |
| --- | --- | --- |
| t | p | p |
| t̄_f | p | p |
| t_f | p | p |
</details>

图7.3.1

固定 $\bar{t}_f$ ，由 $P(t; t_f, P(\bar{t}_f; t_f, 0))$ 连续依赖于 $(t_f, 0)$ 的性质得到
