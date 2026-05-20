$$(I + X) ^ {\alpha} \stackrel {\text { def }} {=} I + \alpha X; \frac {\alpha (\alpha - 1)}{2 !} X ^ {2} + \frac {\alpha (\alpha - 1) (\alpha - 2)}{3 !} X ^ {3} + \dots$$

当 $\pmb{X}$ 的所有特征值的模都小于1时收敛．特别取 $\alpha = -1, X = -A$ 时，

$$(I - A) ^ {- 1} \stackrel {\mathrm{def}} {=} I + A + A ^ {2} + \dots$$

线性矩阵方程 现在我们讨论以实变量 $x$ 的函数为元素的矩阵

$$
\boldsymbol {A} (x) = \left[ \begin{array}{c c c c} a _ {1 1} (x) & a _ {1 2} (x) & \dots & a _ {1 n} (x) \\ a _ {2 1} (x) & a _ {2 2} (x) & \dots & a _ {2 n} (x) \\ \vdots & \vdots & & \vdots \\ a _ {m 1} (x) & a _ {m 2} (x) & \dots & a _ {m n} (x) \end{array} \right],
$$

式中设 $a_{ij}$ 是 $x$ 的实函数(或复变函数), 即对于任意 $x \in \mathbb{R}, A(x) \in \mathbb{R}^{m \times n}$ (或 $A(x) \in \mathbb{C}^{m \times n}$ ). 当 $a_{ij} (i = 1, 2, \cdots, m, j = 1, 2, \cdots, n)$ 可微分时, 称为矩阵 $A$ 可微, $A$ 的各元素对 $x$ 微商后, 定义为 $A$ 对 $x$ 的微商

$$\frac {\mathrm{d} A (x)}{\mathrm{d} x} \stackrel {{\text { def }}} {{=}} \left[ \frac {\mathrm{d} a _ {i j}}{\mathrm{d} x} \right].$$

$\pmb{A}$ 的各元素对 $x$ 的积分，定义为 $\pmb{A}$ 对 $x$ 的积分

$$\int_ {x _ {1}} ^ {x _ {2}} A (x) \mathrm{d} x \stackrel {\text { def }} {=} \left[ \int_ {x _ {1}} ^ {x _ {2}} a _ {i j} (x) \mathrm{d} x \right].$$

考虑线性矩阵微分方程

$$\dot {\pmb {X}} = \pmb {X} D (t) + E (t) \pmb {X} + F (t), \quad \pmb {X} (t _ {0}) = \pmb {X} _ {0}, \tag {1.1.9}$$

其中 $X \in \mathbb{R}^{m \times n}$ 为未知矩阵， $D(\cdot), E(\cdot), F(\cdot)$ 分别为适当阶数的矩阵，其元是 $t$ 的分段连续函数.

定理1.1.1 对于任意的 $t \in \mathbb{R}$ , 方程 (1.1.9) 有唯一解 $X(t; t_0, X_0)$ , 并且

$$\boldsymbol {X} (t; t _ {0}, \boldsymbol {X} _ {0}) = \Phi_ {1} (t, t _ {0}) \boldsymbol {X} _ {0} \Phi_ {2} (t, t _ {0}) + \int_ {t _ {0}} ^ {t} \Phi_ {1} (t, \tau) F (\tau) \Phi_ {2} (t, \tau) \mathrm{d} \tau ,$$

其中矩阵 $\Phi_1(t,\tau)$ 和 $\Phi_2(t,\tau)$ 满足

$$
\begin{array}{l} \frac {\partial \Phi_ {1}}{\partial t} = E (t) \Phi_ {1}, \qquad \Phi_ {1} (\tau , \tau) = I _ {m}; \\ \frac {\partial \Phi_ {2}}{\partial t} = \Phi_ {2} D (t), \quad \Phi_ {2} (\tau , \tau) = I _ {n}. \\ \end{array}
$$

在定理1.1.1中，若 $n = m, D(t) = A$ (常数矩阵)， $E(t) = A^{\mathrm{T}}, F(t) = Q$ (常数矩阵)，则可得下列推论.

推论1.1.1 对于任意 $t \in \mathbb{R}$ , 线性定常矩阵微分方程

$$\dot {\boldsymbol {X}} = \boldsymbol {X} \boldsymbol {A} + \boldsymbol {A} ^ {\mathrm{T}} \boldsymbol {X} + \boldsymbol {Q}, \quad \boldsymbol {X} (t _ {0}) = \boldsymbol {X} _ {0} \tag {1.1.10}$$

有唯一解
