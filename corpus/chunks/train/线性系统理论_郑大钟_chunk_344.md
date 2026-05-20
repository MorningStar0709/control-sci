$$
\left[ \begin{array}{c c} {s I - A _ {c}} & {B _ {c}} \\ {- C _ {c}} & {\mathbf {0}} \end{array} \right] \text {为列满秩} \quad \text {或} \left[ \begin{array}{c c} {s I - A _ {c}} \\ {- C _ {c}} \end{array} \right] \text {为列满秩} \tag {9.146}
$$

于是，根据PBH秩判据即知， $(A_{c},C_{c})$ 为能观测。从而，控制器形实现 $(A_{c},B_{c},C_{c})$ 为联合能控和能观测。由此，证明完成。

性质5 设 $\lambda$ 为 $A_{c}$ 的一个特征值， $\pmb{q}$ 为使 $D(\lambda)\pmb{q} = \mathbf{0}$ 的任一非零常数列向量，则 $A_{c}$ 的属于 $\lambda$ 的一个特征向量 $\pmb{p}$ 可按下式来确定：

$$\boldsymbol {p} = \Psi (\lambda) \boldsymbol {q} \tag {9.147}$$

其中 $\Psi(s)$ 如(9.120)所示。

证 由(9.119)可以导出

$$(s I - A _ {c}) \Psi (s) - B _ {c} D (s) = 0 \tag {9.148}$$

或将其表示为

$$
[ s I - A _ {c} - B _ {c} ] \left[ \begin{array}{l} \Psi (s) \\ D (s) \end{array} \right] = 0 \tag {9.149}
$$

再据(9.116)知， $\{\Psi(s), D(s)\}$ 为右互质，也即矩阵 $\begin{bmatrix}\Psi(s)\\ D(s)\end{bmatrix}$ 对复数平面上所有 s 值均为列满秩。由此表明， $\begin{bmatrix}\Psi(s)\\ D(s)\end{bmatrix}$ 的列向量可作为基，它们张成了 $[sI-A_{c},-B_{c}]$ 的零空间。此外，根据特征向量的定义又有 $A_{c}p=\lambda p$ ，也即对 $s=\lambda$ 成立

$$
[ \lambda I - A _ {c} - B _ {c} ] \left[ \begin{array}{l} p \\ 0 \end{array} \right] = 0 \tag {9.150}
$$

表明向量 $\begin{bmatrix} p \\ 0 \end{bmatrix}$ 位于 $[sI - A_{c} - B_{c}]$ 的零空间内，可表为零空间基向量组的一个线性组合，即

$$
\left[ \begin{array}{l} p \\ 0 \end{array} \right] = \left[ \begin{array}{l} \Psi (s) \\ D (s) \end{array} \right] q \quad \forall s = \lambda \tag {9.151}
$$

于是，就证明了当 $\pmb{q}$ 为使 $D(\lambda)\pmb{q} = \pmb{0}$ 的非零常数向量时，必有 $\pmb{p} = \Psi (\lambda)\pmb{q}$ 。至此，证明完成。

左 MFD 的观测器形实现 我们转而来讨论矩阵分式描述的另一种典型的实现。给定严格真的 $q \times p$ 左 MFD $D_{L}^{-1}(s)N_{L}(s)$ ，其中 $D_{L}(s)$ 为行既约，则定义如下的一个状态空间描述

$$\dot {x} = A _ {o} x + B _ {o} u, y = C _ {o} x \tag {9.152}$$

为 $D_{L}^{-1}(s)N_{L}(s)$ 的观测器形实现，如果满足条件：

① $C_{o}(sI - A_{o})^{-1}B_{o} = D_{L}^{-1}(s)N_{L}(s)$ ;   
② $(A_{0}, C_{0})$ 为能观测。

考虑到左 MFD 和右 MFD 以及能控性和能观测性之间具有对偶的关系, 因此可以断言, 观测器形实现 $(A_{o}, B_{o}, C_{o})$ 在形式上必是对偶于控制器形实现 $(A_{c}, B_{c}, C_{c})$ 的。由这一基本结论出发, 将可直接导出观测器形实现的有关结论和推论。设 $D_{L}^{-1}(s)$ $N_{L}(s)$ 为严格真的, $D_{L}(s)$ 为行既约, 表 $l_{i} = \delta_{ri} D_{L}(s)$ 为行次数, 那么对 $D_{L}(s)$ 和 $N_{L}(s)$

可引入如下的行次表达式:

$$D _ {L} (s) = S _ {L} (s) D _ {h r} + \Psi_ {L} (s) D _ {l r} \tag {9.153}N _ {L} (s) = \Psi_ {L} (s) N _ {l r} \tag {9.154}$$

其中

$$
S _ {L} (s) = \left[ \begin{array}{c c c} s ^ {l _ {1}} & & \\ & \ddots & \\ & & s ^ {l _ {q}} \end{array} \right], \sum_ {i = 1} ^ {q} l _ {i} = n;
