引理8.1.2 $R(x_0,T)$ 在 $M$ 中有非空内点集，当且仅当 $\hat{R} ((0,x_0))$ 在 $\mathbb{R}\times M$ 中有非空内点集.

证明 $(\Longrightarrow)$ 设 $V \subset R(x_0, T)$ 为一非空开集。任选 $X \in F$ 构造一个映射 $P: \mathbb{R} \times V \to \mathbb{R} \times M$ 如下：

$$P (t, v) = \left(T + t, \phi_ {t} ^ {X} (v)\right). \tag {8.1.18}$$

那么 $P$ 的Jacobi矩阵可表示为

$$
J _ {P} = \left[ \begin{array}{c c} 1 & 0 \\ * & J _ {e} \end{array} \right],
$$

这里 $J_{e}$ 是微分同胚 $x \mapsto \phi_{t}^{X}(x)$ 的 Jacobi 矩阵，故非奇异。于是 $J_{P}$ 也非奇异，因此映射 $P$ 是一个开映射。

由 $P$ 的结构可知

$$P ((0, \infty) \times V) \subset \hat {R} ((0, x _ {0})).$$

而且因为 $P$ 是一个开映射，故 $P((0, \infty) \times V)$ 为 $\hat{R}((0, x_0))$ 的一个开子集.

$(\Leftarrow)$ 因为 $\hat{R} ((0, x_0))$ 有一个非空开子集，故根据定理8.1.2，对每一点 $t \in (0, T)$ ，

$$\bigcup_ {0 \leqslant s \leqslant t} \hat {R} ((0, x _ {0}), s)$$

包含一个非空开子集. 设 $W$ 为 $\mathbb{R}$ 的一个非空开子集, 且 $V$ 为 $M$ 的一个非空开子集使得

$$W \times V \subset \bigcup_ {0 \leqslant s \leqslant t} \hat {R} ((0, x _ {0}), s).$$

那么对任一 $t_0 \in W$ 有

$$\{t _ {0} \} \times V \subset \bigcup_ {0 \leqslant s \leqslant t} \hat {R} ((0, x _ {0}), s),$$

这表明

$$V \subset R (x _ {0}, t _ {0}).$$

选择任一 $X \in F$ 构造映射 $G: y \mapsto \phi_{T - t_0}^X(y)$ . 由于 $G$ 为一微分同胚, 故 $G(V)$ 为一非空开集, 且

$$G (V) \subset R (x _ {0}, T).$$

由以上引理可知，如果存在一个 $T > 0$ 使得 $R(x_0, T)$ 具有非空内点，那么对任一 $t > 0$ , $R(x_0, t)$ 具有非空内点，因为它的等价条件是 $\hat{R}((0, x_0))$ 具有非空内点，而这条件与时间 $t$ 无关.

现在我们可给出强能接近的条件.

定理8.1.3 考虑系统(8.1.1). (1) 如果它在 $x_0 \in M$ 满足强能控秩条件

$$\operatorname{rank} \mathcal {F} _ {0} (x _ {0}) = n, \tag {8.1.19}$$

那么它在 $x_0$ 点强能接近；

(2) 如果它是解析系统且在 $x_0$ 点强能接近，则它在 $x_0$ 点满足强能控秩条件；  
(3) 如果它在 $x_0$ 点强能接近或者在 $x_0$ 点满足强能控秩条件, 那么对任一 $T > 0$ 内点集 $\operatorname{Int}(R(x_0, T))$ 在 $R(x_0, T)$ 中稠.

证明 由引理8.1.2，系统(8.1.1)在 $x_0$ 点强能接近等价于系统(8.1.17)在 $(0, x_0)$ 点能接近.

根据定理 8.1.2, 系统 (8.1.17) 的能接近性由以下秩条件保证:

$$\operatorname{rank} (\mathcal {F} _ {0} (0, x _ {0})) = n + 1. \tag {8.1.20}$$

在解析的情况下，它等价于式(8.1.20). 因此，要证明定理的(1)和(2)我们只要证明式(8.1.20)等价于式(8.1.19)即可.

假设有式 (8.1.20). 选择任意向量场 $V \in T_{x_0}$ , 于是

$$
\left[ \begin{array}{c} 0 \\ V \end{array} \right] \in \hat {\mathcal {F}} (x _ {0}).
$$

回忆 $\hat{\mathcal{F}}$ 的表达式 (8.1.16), 我们有

$$V = \left(\sum_ {i = 1} ^ {s} \lambda_ {i} X _ {i} + Y\right) (x _ {0}), \tag {8.1.21}$$

这里 $X_{i} \in F, Y \in \mathcal{F}'$ ，且

$$0 = \sum_ {i = 1} ^ {s} \lambda_ {i} \frac {\partial}{\partial t}. \tag {8.1.22}$$
