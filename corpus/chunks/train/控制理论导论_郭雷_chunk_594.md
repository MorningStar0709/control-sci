# 8.1.3 考虑时变线性系统

$$
\left\{ \begin{array}{l} \dot {x} = A (t) x + \sum_ {i = 1} ^ {m} b _ {i} (t) u _ {i} := A (t) x + B (t) u, \\ y = C (t) x. \end{array} \right. \tag {8.1.29}
$$

将 $t$ 作为一个变量，则系统 (8.1.29) 可表示为

$$
\left\{ \begin{array}{l} \dot {t} = 1, \\ \dot {x} = A (t) x + B (t) u := f (t, x) + \sum_ {i = 1} ^ {m} g _ {i} (t) u _ {i}, \\ y = C (t) x. \end{array} \right. \tag {8.1.30}
$$

(i) 证明对系统 (8.1.30)

$$
[ f, g _ {i} ] - \left[ \begin{array}{c} 0 \\ \frac {\partial}{\partial t} b _ {i} (t) - A (t) b _ {i} (t) \end{array} \right], \quad 1 \leqslant i \leqslant m,
$$

且

$$\left[ g _ {i}, g _ {j} \right] = 0, \quad 1 \leqslant i, j \leqslant m;$$

(ii) 定义

$$\Delta_ {c} ^ {k} B (t) = \left(\frac {\partial}{\partial t} - A (t)\right) \Delta_ {c} ^ {k - 1} B (t), \quad k = 1, 2, \dots$$

这里 $\Delta_c^0 B(t) := B(t)$ . 证明其能控性 Lie 代数为

$$\mathcal {F} = \operatorname{span} \left\{B _ {c} ^ {i} (t) \mid i = 0, 1, 2, \dots \right\}. \tag {8.1.31}$$
