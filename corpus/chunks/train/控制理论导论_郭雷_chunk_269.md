$$\gamma_ {i j} ^ {k} = \gamma_ {j i} ^ {k}, \quad \forall i, j, k. \tag {3.11.15}$$

实际上我们有如下定理：

定理3.11.3 设在流形 $N$ 上存在一个联络，它有对称Christoffel矩阵，那么式(3.11.13)成立.

证明 显见如果 Christoffel 矩阵 $\pmb{\Gamma}$ 对称，则

$$\Gamma \ltimes f \ltimes g = \Gamma \ltimes g \ltimes f, \quad \forall f, g \in V (N).$$

由式 (3.11.8) 可得

$$\nabla_ {f} g - \nabla_ {g} f = D g f - D f g = [ f, g ].$$

由式(3.11.12)可知, 对于 Riemann 流形, Christoffel 矩阵对称. 因此式(3.11.13)成立. 定理 3.11.3 说明, 只要 Christoffel 矩阵对称即可.

一个相关的问题是测地线．测地线方程 $^{[1]}$ 也可以表示成矩阵形式．一条曲线 $r(t)$ 称为M上的测地线，当且仅当

$$\ddot {r} = \Gamma \ltimes \dot {r} ^ {2}. \tag {3.11.16}$$

当 $r(t)$ 在局部坐标下表示为 $r(t) = [x_{1}(t), \cdots, x_{n}(t)]^{\mathrm{T}}$ ，那么方程 (3.11.16) 可表示为以下矩阵形式：

$$
\left[ \begin{array}{c} \ddot {x} _ {1} \\ \vdots \\ \ddot {x} _ {n} \end{array} \right] = \Gamma \left[ \begin{array}{c} \dot {x} _ {1} \\ \vdots \\ \dot {x} _ {n} \end{array} \right] ^ {2}.
$$
