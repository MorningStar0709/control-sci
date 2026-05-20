不难验证 $\mathcal{A}_0$ 在 $\mathcal{H}$ 中是斜自伴的，并且具有紧豫解式。我们知道 $\mathcal{A}_0$ 的本征值 $\mu$ 对称地位于虚轴上，从而可记 $\mu = \pm i\nu^2, \nu$ 为正数。类似于算子 $\mathcal{A}, \nu$ 满足特征方程

$$\sinh \nu \cos \nu + \cosh \nu \sin \nu = 0, \tag {10.4.63}$$

而 $\mathcal{A}_0$ 的相应于本征值 $\mu = \mathrm{i}\nu^2$ 的本征元是

$$
\begin{array}{l} \varphi (x) = \cosh \nu (1 - x) - \cos \nu (1 - x) + \sinh \nu \sin \nu x \\ + \sin \nu \sinh \nu x - \cosh \nu \cos \nu x + \cos \nu \cosh \nu x. \tag {10.4.64} \\ \end{array}
$$

类似于前面的分析，可知式(10.4.63)的正解 $\nu_{n}$ 有渐近表达式

$$\nu_ {n} = m _ {n} \pi + O (n ^ {- 1}). \tag {10.4.65}$$

所有 $\mathcal{A}_0$ 的本征值 $\mu_n = \pi \mathrm{i}\nu_n^2$ 都是代数单的。记相应于 $\mu_n = \mathrm{i}\nu_n^2$ 的本征元为 $[\varphi_n, \mu_n\varphi_n]^{\mathrm{T}}$ ，并且

$$G _ {n} (x) \stackrel {\text { def }} {=} 2 \nu_ {n} ^ {- 2} \mathrm{e} ^ {- \nu_ {n}} [ \varphi_ {n} ^ {\prime \prime} (x), \mu_ {n} \varphi_ {n} (x) ] ^ {\mathrm{T}},$$

其中 $\varphi_{n}$ 为式 (10.4.64) 则有中让 $\nu = \nu_{n}$ 取代后的 $\varphi$ . 于是

$$
G _ {n} (x) = \left[ \begin{array}{c} \mathrm{e} ^ {- m _ {n} \pi x} + \mathrm{e} ^ {- m _ {n} \pi (x - 1)} (\sin m _ {n} \pi + \cos m _ {n} \pi) \\ - (\sin m _ {n} \pi x - \cos m _ {n} \pi x) \\ \mathrm{i} \mathrm{e} ^ {- m _ {n} \pi x} + \mathrm{i} \mathrm{e} ^ {- m _ {n} \pi (x - 1)} (\sin m _ {n} \pi + \cos m _ {n} \pi) \\ - \mathrm{i} (\sin m _ {n} \pi x - \cos m _ {n} \pi x) \end{array} \right] + O (n ^ {- 1}), \tag {10.4.66}
$$

这里我们可以假定 $\{[\varphi_n, \mu_n \varphi_n]^T | n \geqslant 1\} \cup \{[\overline{\varphi}_n, \overline{\mu}_n \overline{\varphi}_n]^T | n \geqslant 1\}$ 为 $A_0$ 的所有本征元，构成 $\mathcal{H}$ 的 Riesz 基 (实际上是直交基). 从式 (10.4.62) 和式 (10.4.66) 可知存在自然数 $N$ 使得

$$
\begin{array}{l} \sum_ {n = N + 1} ^ {\infty} \left\| 2 \omega_ {n} ^ {- 2} \mathrm{e} ^ {- \omega_ {n}} \left[ f _ {n}, \lambda_ {n} f _ {n} \right] ^ {\mathrm{T}} - 2 \nu_ {n} ^ {- 2} \mathrm{e} ^ {- \nu_ {n}} \left[ \varphi_ {n}, \mu_ {n} \varphi_ {n} \right] ^ {\mathrm{T}} \right\| _ {\mathcal {H}} ^ {2} \\ = \sum_ {n = N + 1} ^ {\infty} \| F _ {n} - G _ {n} \| _ {L ^ {2} \times L ^ {2}} ^ {2} = \sum_ {n = N + 1} ^ {\infty} O (n ^ {- 2}) <   \infty . \tag {10.4.67} \\ \end{array}
$$

同样的不等式对于共轭本征元也成立。因此，根据定理10.4.4, $\pmb{A}$ 的广义本征元全体构成状态空间 $\pmb{\mathcal{H}}$ 的Riesz基。

(4) 系统 (10.4.57) 是指数稳定的。事实上，我们只需证明

$$\sup \left\{\operatorname{Re} \lambda \mid \lambda \in \sigma (\mathcal {A}) \right\} < \infty . \tag {10.4.68}$$

从式 (10.4.61) 可知 $\xi = -\alpha^{-1}a^{-2}$ 是 $\sigma(A)$ 的渐近线，并且容易验证 $\operatorname{Re}\lambda < 0$ ， $\forall \lambda \in \sigma(A)$ . 另一方面，由于 $A$ 具有紧豫解式，故它在复平面的任意有界区域内至多有有穷个本征值。综上所述，式 (10.4.68) 成立。
