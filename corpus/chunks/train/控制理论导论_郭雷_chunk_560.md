$$
\begin{array}{l} \dot {x} ^ {*} (t) = \left[ \frac {\partial H (x ^ {*} (t) , u ^ {*} (t) , v ^ {*} (t) , \psi (t) , t)}{\partial \psi} \right] ^ {\mathbf {T}}, \quad x ^ {*} (t _ {0}) = x _ {0}, \\ \dot {\psi} ^ {T} (t) = - \frac {\partial H (x ^ {*} (t) , u ^ {*} (t) , v ^ {*} (t) , \psi (t) , t)}{\partial x}, \\ \psi^ {\mathrm{T}} (t _ {f}) = - \frac {\partial k (x ^ {*} (t _ {f}) , t _ {f})}{\partial x} - \mu^ {\mathrm{T}} \frac {\partial g (x ^ {*} (t _ {f}) , t _ {f})}{\partial x}; \\ \end{array}
$$

(2) $\forall t\in \Omega (t_0,t_f;(u^*,v^*))$

$$
\begin{array}{l} H (x ^ {*} (t), u ^ {*} (t), v ^ {*} (t), \psi (t)) = \min _ {v \in \mathbb {V} _ {r _ {2}}} \max _ {u \in \mathbb {U} _ {r _ {1}}} H (x ^ {*} (t), u, v, \psi (t), t) \\ = \max _ {u \in \mathbf {U} _ {r _ {1}}} \min _ {v \in \mathbf {V} _ {r _ {2}}} H (x ^ {*} (t), u, v, \psi (t), t); \\ \end{array}
$$

(3) $\forall t\in \Omega (t_0,t_f;(u^*,v^*))$

$$
\begin{array}{l} H (x ^ {*} (t), u ^ {*} (t), v ^ {*} (t), \psi (t), t) = H (x ^ {*} (t _ {f}), u ^ {*} (t _ {f}), v ^ {*} (t _ {f}), \psi (t _ {f}), t _ {f}) \\ + \int_ {t _ {f}} ^ {t} \frac {\partial H (x ^ {*} (\tau) , u ^ {*} (\tau) , v ^ {*} (\tau) , \psi (\tau) , \tau)}{\partial t} d \tau . \\ \end{array}
$$

注7.4.1 对于 $x(t_{f})$ 自由， $t_{f}$ 自由以及 $f, g, k$ 和 $l$ 皆不显含时间 $l$ 的情况的定量微分对策问题，皆有相应的双方极值原理。这里不再一一叙述。读者从定理7.4.1的推证过程，并利用7.1中相应情况下的极大值及相应极小值原理，易得此结论。
