$$
\begin{array}{l} \operatorname{rank} \mathbf {S} _ {1} ^ {\prime} = \operatorname{rank} \left[ \mathbf {G} ^ {n} \mathbf {S} _ {1} ^ {\prime} \right] \\ = \operatorname{rank} [ G ^ {n - 1} h \dots G h h ] = n \tag {9-143} \\ \end{array}
$$

交换矩阵的列，且记为 $S_{1}$ ，其秩也不变，故有

$$\operatorname{rank} S _ {1} = \operatorname{rank} [ h \quad G h \quad \dots \quad G ^ {n - 1} h ] = n \tag {9-144}$$

由于式(9-144)避免了矩阵求逆，在判断系统的可控性时，使用式(9-144)比较方便。

式(9-141)～式(9-144)都称为可控性判据， $S_{1}^{\prime}$ 和 $S_{1}$ 都称为单输入离散系统的可控性矩阵。状态可控性取决于 G 和 h。

当 $\operatorname{rank} S_1 < n$ 时，系统不可控，表示不存在使任意 $x(0)$ 转移至 $x(n) = 0$ 的控制。

以上研究了终态为 $x(n) = 0$ 的情况，若令终态为任意给定状态 $x(n)$ ，则式(9-138)变为

$$\pmb {G} ^ {n} \pmb {x} (0) - \pmb {x} (n) = - \sum_ {i = 0} ^ {n - 1} \pmb {G} ^ {n - 1 - i} \pmb {h u} (i)$$

将上式两端左乘 $G^{-n}$ ，有

$$
\boldsymbol {x} (0) - \boldsymbol {G} ^ {- n} \boldsymbol {x} (n) = - \left[ \begin{array}{l l l l} \boldsymbol {G} ^ {- 1} \boldsymbol {h} & \boldsymbol {G} ^ {- 2} \boldsymbol {h} & \dots & \boldsymbol {G} ^ {- n} \boldsymbol {h} \end{array} \right] \left[ \begin{array}{c} u (0) \\ u (1) \\ \vdots \\ u (n - 1) \end{array} \right]
$$

当 $\pmb{G}$ 满秩时，该式左端只不过是任一给定的另一初态，其状态可控性条件可用以上推导方法得出完全相同的结论。若令 $x(0) = 0$ ，上述结论同样成立。可见，当 $\pmb{G}$ 为非奇异阵时，系统的可控性和可达性是等价的。

上述研究单输入离散系统可控性的方法可推广到多输入系统。设系统的状态方程为

$$\boldsymbol {x} (k + 1) = \boldsymbol {G x} (k) + \boldsymbol {H u} (k) \tag {9-145}$$

所谓可控性问题即是能否求出无约束控制向量序列 $u(0), u(1), \cdots, u(n-1)$ ，使系统能从任意初态 $x(0)$ 转移至 $x(n) = 0$ 。式(9-145) 的解为

$$\boldsymbol {x} (k) = \boldsymbol {G} ^ {k} \boldsymbol {x} (0) + \sum_ {i = 0} ^ {k - 1} \boldsymbol {G} ^ {k - 1 - i} \boldsymbol {H} \dot {\boldsymbol {u}} (i) \tag {9-146}$$

令 $k = n, x(n) = 0$ ，且式(9-146)两端左乘 $\pmb{G}^{-n}$ ，有

$$
\begin{array}{l} \pmb {x} (0) = - \sum_ {i = 0} ^ {n - 1} \pmb {G} ^ {- 1 - i} \pmb {H u} (i) = - [ \pmb {G} ^ {- 1} \pmb {H u} (0) + \pmb {G} ^ {- 2} \pmb {H u} (1) + \dots + \pmb {G} ^ {- n} \pmb {H u} (n - 1) ] \\ = - \left[ \begin{array}{l l l l} \mathbf {G} ^ {- 1} \mathbf {H} & \mathbf {G} ^ {- 2} \mathbf {H} & \dots & \mathbf {G} ^ {- n} \mathbf {H} \end{array} \right] \left[ \begin{array}{c} \boldsymbol {u} (0) \\ \boldsymbol {u} (1) \\ \vdots \\ \boldsymbol {u} (n - 1) \end{array} \right] \tag {9-147} \\ \end{array}
$$

记 $S_{2}^{\prime}=\left[G^{-1}H\quad G^{-2}H\quad\cdots\quad G^{-n}H\right]$ (9-148)
