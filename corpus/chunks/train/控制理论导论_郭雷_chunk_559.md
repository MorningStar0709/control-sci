$$
\begin{array}{l} \min _ {v \in \mathbf {V} _ {r _ {2}}} \max _ {u \in \mathbf {U} _ {r _ {1}}} H (x ^ {*} (t), u, v, \psi (t), t) \leqslant \max _ {u \in \mathbf {U} _ {r _ {1}}} H (x ^ {*} (t), u, v ^ {*} (t), \psi (t), t), \\ \min _ {v \in \mathbf {V} _ {r _ {2}}} H (x ^ {*} (t), u ^ {*} (t), v, \psi (t), t) \leqslant \max _ {u \in \mathbb {U} _ {r _ {1}}} \min _ {v \in \mathbf {V} _ {r _ {2}}} H (x ^ {*} (t), u, v, \psi (t), t), \\ \end{array}
$$

故

$$
\begin{array}{l} \min _ {v \in \mathbf {V} _ {r _ {2}}} \max _ {u \in \mathbf {U} _ {r _ {1}}} H (x ^ {*} (t), u, v, \psi (t), t) \leqslant H (x ^ {*} (t), u ^ {*} (t), v ^ {*} (t), \psi (t), t) \\ \leqslant \max _ {u \in \mathbf {U} _ {r _ {1}}} \min _ {v \in \mathbf {V} _ {r _ {2}}} H (x ^ {*} (t), u, v, \psi (t), t), \quad \forall t \in \Omega ((u ^ {*}, v ^ {*}); t _ {0}, t _ {f}). \tag {7.4.28} \\ \end{array}
$$

另一方面，将多元函数中关于最大最小的结论“最小中的最大总不大于最大中的最小”用于函数 $H(x^{*}(t), u, v, \psi(t), t)$ ，可知 $\forall t \in \Omega(t_0, t_f; (u^*, v^*))$

$$\max _ {u \in \mathbf {U} _ {r _ {1}}} \min _ {v \in \mathbf {V} _ {r _ {2}}} H (x ^ {*} (t), u, v, \psi (t), t) \leqslant \min _ {v \in \mathbf {V} _ {r _ {2}}} \max _ {u \in \mathbf {U} _ {r _ {1}}} H (x ^ {*} (t), u, v, \psi (t), t). \tag {7.4.29}$$

联合不等式 (7.4.28), (7.4.29) 即知, $\forall t \in \Omega((u^{*}, v^{*}); t_{0}, t_{f})$

$$
\begin{array}{l} H (x ^ {*} (t), u ^ {*} (t), v ^ {*} (t), \psi (t)) = \min _ {v \in \mathbf {V} _ {r _ {2}}} \max _ {u \in \mathbf {U} _ {r _ {1}}} H (x ^ {*} (t), u, v, \psi (t), t) \\ = \max _ {u \in \mathbf {U} _ {r _ {1}}} \min _ {v \in \mathbf {V} _ {r _ {2}}} H (x ^ {*} (t), u, v, \psi (t), t). \\ \end{array}
$$

此外，从式(7.4.22)，(7.4.26)和(7.4.27)直接得到，当 $t_f$ 固定时， $\forall t\in \Omega ((u^{*},v^{*});t_{0},t_{f})$

$$
\begin{array}{l} H (x ^ {*} (t), u ^ {*} (t), v ^ {*} (t), \psi (t)) = H (x ^ {*} (t _ {f}), u ^ {*} (t _ {f}), v ^ {*} (t _ {f}), \psi (t _ {f}), t _ {f}) \\ + \int_ {t} ^ {t _ {f}} \frac {\partial H (x ^ {*} (\tau) , u ^ {*} (\tau) , v ^ {*} (\tau) , \psi (\tau) , \tau)}{\partial t} d \tau . \\ \end{array}
$$

定理 7.4.1(极小极大值原理，亦称双方极值原理) 设 $(u^{*}(t), v^{*}(t)) \in \mathcal{W}_{[t_{0}, t_{f}]}$ 是定量微分对策问题 (7.4.8)\~(7.4.11) 的最优策略 (这里 $t_{f}$ 事先给定)， $x^{*}(t)$ 是相应的最优轨线，则存在向量值函数 $\psi(t)$ 和待定常向量 $\mu$ ，使得 $u^{*}(t), v^{*}(t), x^{*}(t)$ 和 $\psi(t), \mu$ 在 $[t_{0}, t_{f}]$ 上同时满足

(1)
