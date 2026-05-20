(2) 假定 $A$ 生成一 $C_0$ 等距群. 任取 $\lambda_0 \in \sigma(T(1))$ , 由于 $T(1)$ 等距并且有界, 故根据引理5.3.13, 对于任意 $\delta_0, 0 < \delta_0 < 1$ , 存在一相对 $T(1)$ 超不变的子空间 $X_0$ , 使得

$$\sigma (T _ {0}) \subset \mathbb {C} _ {1} \cap \left\{\lambda \in \mathbb {C} \mid | \lambda - \lambda_ {0} | \leqslant \delta \right\}, \quad \delta_ {0} < \delta < 1,$$

其中 $T_{0} = T(1)|_{X_{0}}$

令 $\Gamma = \{\lambda \in \mathbb{C} | |\lambda - \lambda_0| = \delta\}$ , 并定义

$$B _ {0} = \frac {1}{2 \pi \mathrm{i}} \int_ {\Gamma} (\log \lambda) R (\lambda ; T _ {0}) \mathrm{d} \lambda ,$$

其中 $\Gamma$ 按顺时针方向定向，并且 $\log \lambda$ 取为任一单值分支。那么 $B_0$ 是 $X_0$ 中的有界线性算子，并且根据 $B_0$ 的定义和乘积公式 (5.3.65)，我们得到

$$
\begin{array}{l} \mathrm{e} ^ {B _ {0}} = \sum_ {n = 0} ^ {\infty} \frac {B _ {0} ^ {n}}{n !} = \frac {1}{2 \pi \mathrm{i}} \sum_ {n = 0} ^ {\infty} \frac {1}{n !} \int_ {\Gamma} (\log \lambda) ^ {n} R (\lambda ; T _ {0}) \mathrm{d} \lambda \\ = \frac {1}{2 \pi \mathrm{i}} \int_ {\Gamma} \mathrm{e} ^ {\log \lambda} R (\lambda ; T _ {0}) \mathrm{d} \lambda = \frac {1}{2 \pi \mathrm{i}} \int_ {\Gamma} \lambda R (\lambda ; T _ {0}) \mathrm{d} \lambda \\ = T _ {0} = T (1) | _ {X _ {0}} = T ^ {A _ {0}} (1), \tag {5.3.66} \\ \end{array}
$$

其中 $A_0$ 是 $A$ 在 $X_0$ 上的限制。由于 $B_0$ 与 $A_0$ 可交换，故从式 (5.3.66) 可得

$$T ^ {A _ {0} - B _ {0}} (1) = I | _ {X _ {0}} \stackrel {\text { def }} {=} I _ {0}.$$

于是 $T^{A_0 - B_0}(t)$ 是周期为1的周期函数.

对于任意自然数 $n$ , 定义线性算子

$$P _ {n} x = \int_ {0} ^ {1} \mathrm{e} ^ {- 2 n \pi \mathrm{i} t} T ^ {A _ {0} - B _ {0}} (t) x \mathrm{d} t, \quad \forall x \in X _ {0},$$

由于 $T^{A_0 - B_0}(t)$ 是周期为1的周期函数，容易验证 $P_{n}$ 是 $X_0$ 上的投影，即 $P_{n}$ 有界并且 $P_{n}^{2} = P_{n}$ . 于是

$$
\begin{array}{l} (A _ {0} - B _ {0}) P _ {n} = \int_ {0} ^ {1} \mathrm{e} ^ {- 2 n \pi i t} T ^ {A _ {0} - B _ {0}} (t) (A _ {0} - B _ {0}) x \mathrm{d} t \\ = 2 n \pi \mathrm{i} \int_ {0} ^ {1} \mathrm{e} ^ {- 2 n \pi \mathrm{i} t} T ^ {A _ {0} - B _ {0}} (t) x \mathrm{d} t \\ = 2 n \pi \mathrm{i} P _ {n}, \quad \forall x \in X _ {0} \cap \mathcal {D} (A). \tag {5.3.67} \\ \end{array}
$$

现在我们证明存在一自然数 $k$ 使得 $P_{k} \neq 0$ . 事实上, 若不然, 则

$$\int_ {0} ^ {1} \mathrm{e} ^ {- 2 n \pi \mathrm{i} t} T ^ {A _ {0} - B _ {0}} (t) x \mathrm{d} t = 0, \quad \forall x \in X _ {0}, \forall n \geqslant 1,$$

由此得到

$$\int_ {0} ^ {1} f (t) T ^ {A _ {0} - B _ {0}} (t) x \mathrm{d} t = 0, \quad \forall x \in X _ {0}, \forall f \in L ^ {2} (0, \ell).$$

于是 $T^{A_0 - B_0}(t)x = 0, \forall x \in X_0, \forall t \geqslant 0,$ 矛盾.

因此对于某个 $k, X_{k0} \stackrel{\mathrm{def}}{=} P_k X_0$ 为非零子空间。从式 (5.3.67) 推出，在 $X_{k0}$ 上 $A$ 可以表示成

$$A | _ {X _ {k 0}} = B _ {k 0} + 2 k \pi \mathrm{i} I _ {k 0},$$

其中 $B_{k0} = B_0|_{X_{k0}}, I_{k0}$ 是 $X_{k0}$ 上的恒等算子.

由于 $A|_{X_{k0}}$ 是有界且强守恒的，故 $\sigma(A|_{X_{k0}}) \neq \emptyset, \sigma(A|_{X_{k0}}) \subset \mathbb{R}$ . 因此 $\sigma(A|_{X_{k0}})$ 由其边界点组成，从而 $\sigma(A|_{X_{k0}}) = \sigma_a(A|_{X_{k0}})$ . 但容易验证 $\sigma_a(A|_{X_{k0}}) \subset \sigma(A)$ ，从而 $\sigma(A|_{X_{k0}}) \subset \sigma(A)$ . 由此即得所需论断. 证毕.

推论5.3.3 设 $A$ 是Banach空间 $X$ 上某 $C_0$ 等距群 $T(t)$ 的生成算子，那么存在一相对 $A$ 不变的非平凡子空间 $X_0 \subset X$ 使得 $A|_{X_0}: X_0 \to X_0$ 是有界的.
