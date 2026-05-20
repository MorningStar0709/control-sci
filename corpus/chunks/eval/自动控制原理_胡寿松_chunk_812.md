# (3) 奇异性的充分必要条件

定理 10-15 对于问题 10-1, 设矩阵

$$\boldsymbol {G} _ {j} = \left[ \boldsymbol {b} _ {j} \boldsymbol {A} \boldsymbol {b} _ {j} \dots \boldsymbol {A} ^ {n - 1} \boldsymbol {b} _ {j} \right]; \quad j = 1, 2, \dots , m \tag {10-79}$$

式中， $b_{j}\in R^{n}$ ，为矩阵B的列向量。当且仅当m个 $G_{j}$ 矩阵中至少有一个 $G_{j}$ 是奇异矩阵，问题10-1是奇异的。

证明 构造哈密顿函数

$$H (\boldsymbol {x}, \boldsymbol {u}, \lambda) = 1 + \lambda^ {\mathrm{T}} (t) [ \boldsymbol {A} \boldsymbol {x} (t) + \boldsymbol {B} \boldsymbol {u} (t) ] \tag {10-80}$$

由极小值原理知，应有 $H^{*}(t_{f}^{*}) = 0$ ，所以在式(10-80)中，必有

$$\lambda (t) \neq 0, \quad \forall t \in [ 0, t _ {f} ] \tag {10-81}$$

由协态方程

$$\dot {\boldsymbol {\lambda}} (t) = - \frac {\partial H}{\partial \boldsymbol {x}} = - \boldsymbol {A} ^ {\mathrm{T}} \boldsymbol {\lambda} (t)$$

其解为 $\pmb {\lambda}(t) = \mathrm{e}^{-\pmb{A}^{\mathrm{T}}t}\pmb {\lambda}(0),\qquad \pmb {\lambda}(0)\neq \mathbf{0}$

因而 $g_{j}(t) = \pmb{\lambda}^{\mathrm{T}}(t)\pmb{b}_{j} = \pmb{\lambda}^{\mathrm{T}}(0)\mathrm{e}^{-\mathbf{A}\iota}\pmb{b}_{j}$

设存在奇异区间 $[t_1, t_2] \subset [0, t_f]$ ，使得

$$\boldsymbol {g} _ {j} (t) = \boldsymbol {\lambda} ^ {\mathrm{T}} (0) \mathrm{e} ^ {- A t} \boldsymbol {b} _ {j} = 0, \quad \forall t \in [ t _ {1}, t _ {2} ]$$

对上式求导 n-1 次，并根据矩阵指数性质，有

$$(- 1) ^ {n - 1} g _ {j} ^ {(n - 1)} (t) = \boldsymbol {\lambda} ^ {\mathrm{T}} (0) \mathrm{e} ^ {- A t} \boldsymbol {A} ^ {n - 1} \boldsymbol {b} _ {j} = 0$$

将 $g_{j}(t)$ 各次导数表达式写为矩阵形式，有

$$\boldsymbol {\lambda} ^ {\mathrm{T}} (0) \left[ \mathrm{e} ^ {- A t} \boldsymbol {b} _ {j} \quad \mathrm{e} ^ {- A t} A \boldsymbol {b} _ {j} \quad \dots \quad \mathrm{e} ^ {- A t} A ^ {n - 1} \boldsymbol {b} _ {j} \right] = 0 \tag {10-82}$$

由矩阵论知, 向量 $\lambda(0)$ 有非零解的充分必要条件为系数矩阵奇异, 因此式(10-82) 成立的充分必要条件为

$$
\begin{array}{l} \det \left[ e ^ {- A t} \boldsymbol {b} _ {j} \quad e ^ {- A t} \boldsymbol {A b} _ {j} \quad \dots \quad e ^ {- A t} \boldsymbol {A} ^ {n - 1} \boldsymbol {b} _ {j} \right] \\ = \det ^ {- A t} \det [ \boldsymbol {b} _ {j} \quad \boldsymbol {A b} _ {j} \quad \dots \quad \boldsymbol {A} ^ {n - 1} \boldsymbol {b} _ {j} ] = 0 \tag {10-83} \\ \end{array}
$$

因为 $e^{-At}$ 为状态转移矩阵，是非奇异的，故式(10-83)成立的充分必要条件为

$$
\det \boldsymbol {G} _ {j} = \det \left[ \begin{array}{l l l l} \boldsymbol {b} _ {j} & \boldsymbol {A b} _ {j} & \dots & \boldsymbol {A} ^ {n - 1} \boldsymbol {b} _ {j} \end{array} \right] = 0; \quad \forall j = 1, 2, \dots , m
$$

由上述定理,立即可得问题 10-1 正常的充分必要条件。

定理 10-16 问题 10-1 是正常的, 当且仅当
