设 $y \in M$ , 由于 $T(t)$ 是群, 与前相类似, 我们有 $B^{*}S(t)y = 0, \forall t \in \mathbb{R}$ . 从定理10.2.7可知 $B^{*}T(t)y = 0, \forall t \in \mathbb{R}$ . 由于 $T(t)$ 是一酉群, 故 $T(t) = T^{*}(-t)$ , 从而 $B^{*}T^{*}(t)y = 0, \forall t \geqslant 0$ . 因此假设(2)蕴含 $y = 0$ , 从而 $M = \{0\}$ . 证毕.

在上述两个定理中，我们对 $C_0$ 半群 $S(t)$ 和 $S^{*}(t)$ 的轨线作了紧性假设，以便应用定理10.3.4. 当 $T(t)$ 对于所有 $t > 0$ 为紧算子时，我们知道 $S(t)$ 和 $S^{*}(t)$ 对于所有 $t > 0$ 都是紧的。因此对于任意固定的 $y \in H, S(t)y$ 和 $S^{*}(t)y$ 对于任意 $t \geqslant 0$ 属于 $H$ 中某个（可能与 $y$ 有关的）紧集。事实上，设 $\{t_k\}$ 是一正数列使得当 $k \to \infty$ 时 $t_k \uparrow \infty$ 。记 $y_k = S(t_k - t_1)y$ ，则 $\| y_k \| \leqslant \| y\|$ ， $\forall k \geqslant 1$ ，并且从 $S(t_1)$ 的紧性可知， $\{S(t_k)y\} = \{S(t_1)y_k\}$ 包含一收敛子列。一般说来，上述情形出现在线性抛物型方程中。但是，对于线性双曲型方程， $S(t)$ 对于任意 $t > 0$ 决不会是紧的。我们有如下结果。

定理10.3.7 设 $A$ 是 $H$ 上 $C_0$ 压缩半群 $T(t)$ 的生成算子，并假设 $A$ 有紧豫解式，则对于任意固定的 $y \in H, S(t)y$ 和 $S^*(t)y$ 对于所有 $t \geqslant 0$ 属于 $H$ 同一个紧集.

证明 首先注意 $A - BB^{*}$ 和 $A^{*} - BB^{*}$ 均有紧豫解式. 利用 $S(t)$ 的压缩半群性质, 我们有

$$\| (A - B B ^ {*}) S (t) y \| \leqslant \| (A - B B ^ {*}) y \|, \quad \forall y \in \mathcal {D} (A), \forall t \geqslant 0.$$

今任取 $\lambda \in \rho(A)$ , 从上述不等式得到

$$\left\| (A - B B ^ {*} - \lambda I) S (t) y \right\| \leqslant \left\| (A - B B ^ {*}) y \right\| + | \lambda | \| y \|, \quad \forall t \geqslant 0,$$

由此可见，对于任意固定的 $y \in \mathcal{D}(A)$ , $S(t)y$ 对于所有 $t \geqslant 0$ 属于 $H$ 某个紧集，这是因为 $(A - BB^{*} - \lambda I)^{-1}$ 是一紧算子。但 $\mathcal{D}(A)$ 在 $H$ 中是稠密的，故我们得出结论：对于任意固定的 $y \in H$ , $S(t)y$ 对于所有 $t \geqslant 0$ 属于 $H$ 的某一个紧集。事实上，对于任意 $y \in H$ ，存在序列 $\{y_{n}\} \subset \mathcal{D}(A)$ 使得当 $n \to \infty$ 时 $y_{n} \to y$ 。对于任意给定的 $\varepsilon > 0$ ，由于 $S(t)$ 是压缩的，故存在自然数 $n$ 使得

$$\| S (t) y _ {n} - S (t) y \| \leqslant \| y _ {n} - y \| < \varepsilon , \quad \forall t \geqslant 0.$$

这意味着对于每一 $\varepsilon > 0$ , 存在 $\{S(t)y \mid t \geqslant 0\}$ 的一相对紧的 $\varepsilon$ -网 $\{S(t)y_n \mid t \geqslant 0\}$ . 因此 $\{S(t)y \mid t \geqslant 0\}$ 是相对紧的.

有关 $S^{*}(t)$ 的相应结论的证明是完全类似的．证毕.

综合定理 10.3.5, 10.3.6 和定理 10.3.7 便得到如下结果:

推论 10.3.2 设 A 是 H 上的 $C_{0}$ 压缩半群 $T(t)$ ，而 $B \in \mathcal{L}(U, H)$ 。假定 (1) A 有紧豫解式；(2) $(A, B)$ 是完全近似能控的，那么 $(A, B)$ 是强能稳的，更确切地说，由 $A - BB^{*}$ 生成的 $C_{0}$ 半群 $S(t)$ 是强稳定的。

证明 注意 $A$ 有紧豫解式等价于 $A^{*}$ 有紧豫解式，故在假设 (1) 之下，从定理 10.3.5 和 10.3.7 可知， $S(t)$ 是弱稳定的。由于 $A - BB^{*}$ 有紧豫解式，根据定理 10.1.2，由 $A - BB^{*}$ 生成的 $C_{0}$ 半群 $S(t)$ 是强稳定的。证毕。
