$$
\left\{ \begin{array}{l} p _ {j} ^ {c} (z) := p _ {j} (x (z), 0, z), \qquad x _ {1} ^ {i} = \sum_ {r = 2} ^ {h} \psi_ {i} ^ {(r)} (z), \qquad \bar {x} _ {1} ^ {i} = 0, \\ i = 1, \dots , m, \quad j = 1, \dots , s, \\ q _ {k} ^ {c} (z) := q _ {k} (x (z), 0, z), \qquad x _ {1} ^ {i} = \sum_ {r = 2} ^ {h} \psi_ {i} ^ {(r)} (z), \qquad \bar {x} _ {1} ^ {i} = 0, \\ i = 1, \dots , m, \quad k = 1, \dots , t, \\ \tilde {q} _ {k} ^ {c} (z) := q _ {k} (x (z), w (z), z), \qquad x _ {1} ^ {i} = \sum_ {r = 2} ^ {h} \psi_ {i} ^ {(r)} (z) + E _ {1} ^ {i} (z), \qquad (\bar {x} _ {1} ^ {i}) _ {j} = E _ {j} ^ {i} (z), \\ j = 2, \dots , n _ {i}, \quad i = 1, \dots , m, \end{array} \right.
$$

这里 $E_{j}^{i}(z)$ 及 $w(z)$ 是待定函数，将在后面确定。记 $p^{c}(z) = [p_{1}^{c}(z), \cdots, p_{s}^{c}(z)]^{\mathrm{T}}$ ，且同样定义 $q_{k}^{c}(z)$ 及 $\tilde{q}_{k}^{c}(z)$ 。次数为 2 到 h 的多项式将用来做非线性控制设计。下面的定理揭示了设计原理。

定理 8.6.7 设 C = 0，且存在一组多项式 $\psi_{i}^{(r)}(z)$ ， $r = 2, \cdots, h; i = 1, \cdots, m,$ $\deg(\psi_{i}^{(r)}(z)) = r$ ，及一个整数 $e \geqslant 2$ ，使得以下条件 (1)～(4) 成立：

(1) $p^c (z) = O(\| z\|^{e + 1});$

(2) $q^{c}(z) = O(\| z\|^{e})$

(3) 如果 $E_{j}^{i}(z) = O(\| z\|^{e + 1})$ ，及 $w(z) = O(\| z\|^{e + 1})$ ，则

$$\dot {z} = \bar {q} ^ {c} (z) \quad \text {及} \quad \dot {z} = q ^ {c} (z) \tag {8.6.30}$$

有相同的近似系统；

(4) $\dot{z} = q^{c}(z)$ 近似稳定.

那么系统 (8.6.29) 在原点可镇定, 而且, 如果条件 (1)\~(4) 满足, 则镇定系统 (8.6.29) 的一个可行的反馈控制为

$$u _ {i} = - \frac {f _ {i} (\xi)}{g _ {i} (\xi)} + \frac {1}{g _ {i} (\xi)} \left(\sum_ {j = 1} ^ {n _ {i}} a _ {j} ^ {i} x _ {j} ^ {i} - a _ {1} ^ {i} \left(\sum_ {r = 2} ^ {h} \psi_ {i} ^ {(r)} (z)\right)\right), \quad i = 1, \dots , m, \tag {8.6.31}$$

这里 $\lambda^{n_i} - \sum_{j=1}^{n_i} a_j^i \lambda^{j-1}$ 是 Hurwitz 多项式.

证明 选

$$
\Phi (z) = \left\{ \begin{array}{l l} x _ {1} ^ {i} (z) = \sum_ {r = 2} ^ {h} \psi_ {i} ^ {(r)} (z), \\ \overline {{x}} _ {1} ^ {i} (z) = 0, & i = 1, \dots , m, \\ w (z) = 0 \end{array} \right.
$$

来逼近在控制 (8.6.30) 作用下的闭环系统。利用条件 (1), (2) 以及控制 (8.6.31) 可得

$$
\begin{array}{l} M \Phi (z) = \left[ \begin{array}{c} {\left[ \sum_ {r = 2} ^ {h} \frac {\partial \psi_ {i} ^ {(r)} (z)}{\partial z} \right], i = 1, \dots , m} \\ {0} \\ {0} \end{array} \right] q ^ {c} (z) - \left[ \begin{array}{c} {0} \\ {0} \\ {p ^ {c} (z)} \end{array} \right] \\ = O \left(\| z \| ^ {e + 1}\right). \tag {8.6.32} \\ \end{array}
$$

中心流形的动力系统为

$$\dot {z} = q (x (z), w (z), z). \tag {8.6.33}$$

根据逼近定理, 式 (8.6.32) 保证在式 (8.6.33) 中. 函数 $x(z)$ 及 $w(z)$ 具有如下形式:
