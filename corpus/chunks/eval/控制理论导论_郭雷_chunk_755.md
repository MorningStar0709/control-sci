$$\langle x, B ^ {*} R (\lambda ; A) ^ {*} x ^ {*} \rangle = \int_ {0} ^ {\infty} \mathrm{e} ^ {- \lambda t} \langle x, B ^ {*} T ^ {*} (t) x ^ {*} \rangle \mathrm{d} t,\forall x \in X, x ^ {*} \in X ^ {*}, \operatorname{Re} \lambda > \omega .$$

任取 $\gamma >\omega$ ，则依据Laplace反演公式，有

$$\langle x, B ^ {*} T ^ {*} (t) x ^ {*} \rangle = \frac {1}{2 \pi \mathrm{i}} \int_ {\gamma - \mathrm{i} \infty} ^ {\gamma + \mathrm{i} \infty} \mathrm{e} ^ {\lambda t} \langle x, B ^ {*} R (\lambda ; A) ^ {*} x ^ {*} \rangle \mathrm{d} \lambda . \tag {10.2.29}$$

由此可见

$$B ^ {*} R (\lambda ; A) ^ {*} x ^ {*} = 0, \forall \operatorname{Re} \lambda > \omega \Longrightarrow B ^ {*} T ^ {*} (t) x ^ {*} = 0, \forall t \geqslant 0,$$

从而由式 (10.2.23) 推出 $x^{*} = 0$ ，即式 (10.2.27) 成立。证毕。

推论10.2.1 在定理10.2.8的假设之下，如果 $\rho(A)$ 是 $\mathbb{C}$ 的一连通区域（例如，当 $A$ 是 $X$ 中的离散算子，即 $A$ 有紧豫解式时就是这种情形），则 $(A, B)$ 完全近似能控当且仅当

$$x ^ {*} \in X ^ {*}, \quad B ^ {*} R (\overline {{{\lambda}}}; A ^ {*}) x ^ {*} = 0, \forall \lambda \in \rho (A) \Longrightarrow x ^ {*} = 0. \tag {10.2.30}$$

设 $A$ 是 $X$ 中的离散算子，即 $A$ 具有紧豫解式，从而 $A$ 具有纯点谱。记 $\sigma(A) = \{\lambda_k | k \geqslant 1\}$ 。对于 $\lambda_k \in \sigma(A)$ ，定义投影算子

$$P _ {k} = \frac {1}{2 \pi \mathrm{i}} \int_ {\Gamma_ {k}} R (\lambda ; A) \mathrm{d} \lambda , \tag {10.2.31}$$

其中 $\Gamma_{k}$ 表示中心在 $\lambda_{k}$ 的小圆，使得 $\Gamma_{k} \subset \rho(A)$ 并且在 $\Gamma_{k}$ 所包围的内部区域中除了 $\lambda_{k}$ 外没有 $A$ 的其余谱点.

实际中存在一类重要的算子，即所谓的标量型离散谱算子类(有关离散型谱算子的概念，参阅文献[13]). 当 $A$ 是离散型谱算子时， $I = \sum_{k=1}^{\infty} P_k$ ，并且 $A$ 有谱分解

$$A = \sum_ {k = 1} ^ {\infty} \lambda_ {k} P _ {k}. \tag {10.2.32}$$

定理10.2.9 设 $X$ 和 $U$ 为两个自反的Banach空间，假定 $A$ 是标量型离散谱算子，具有谱分解(10.2.32)，并且是 $X$ 上 $C_0$ 半群 $T(t)$ 的生成算子．那么 $(A,B)$ 完全近似能控当且仅当

$$x ^ {*} \in X ^ {*}, \quad B ^ {*} P _ {k} ^ {*} x ^ {*} = 0, \forall k \geqslant 1 \Longrightarrow x ^ {*} = 0. \tag {10.2.33}$$

证明 根据推论 10.2.1, 只要证明式 (10.2.33) 和式 (10.2.30) 等价. 使用 A 的谱分解表达式, 容易看出

$$R (\lambda ; A) = \sum_ {k = 1} ^ {\infty} \frac {1}{\lambda - \lambda_ {k}} P _ {k}, \quad \forall \lambda \in \rho (A). \tag {10.2.34}$$

注意由于 $X$ 自反， $A^{*}$ 也是离散谱算子（见文献[13])，并且

$$R (\overline {{{\lambda}}}; A ^ {*}) x ^ {*} = \sum_ {k = 1} ^ {\infty} \frac {1}{\overline {{{\lambda}}} - \overline {{{\lambda}}} _ {k}} P _ {k} ^ {*} x ^ {*}, \quad \forall \lambda \in \rho (A), x ^ {*} \in X ^ {*}. \tag {10.2.35}$$

设式 (10.2.30) 成立. 如果 $B^{*}P_{k}^{*}x^{*} = 0, \forall k \geqslant 1$ , 则依式 (10.2.35), 我们有
