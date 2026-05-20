$$\omega_ {n} = m _ {n} \pi + O (n ^ {- 1}), \tag {10.4.60}\lambda_ {n} = - \alpha^ {- 1} a ^ {- 2} + \mathrm{i} (m _ {n} \pi) ^ {2} \pi + O (n ^ {- 1}), \tag {10.4.61}$$

其中 $m_{n} = n - \frac{1}{4}$ . 设 $\mathcal{A}$ 的对应于本征值 $\lambda_{n}$ 的本征元为 $[f_{n}, \lambda_{n} f_{n}]^{\mathrm{T}}$ , 这里 $f_{n}$ 为式 (10.4.59) 中让 $\omega = \omega_{n}$ 所对应的 $f$ . 若令

$$F _ {n} (x) = 2 \omega_ {n} ^ {- 2} \mathrm{e} ^ {- \omega_ {n}} [ f _ {n} ^ {\prime \prime} (x), \lambda_ {n} f _ {n} (x) ] ^ {\mathrm{T}},$$

则有

$$
F _ {n} (x) = \left[ \begin{array}{c} \mathrm{e} ^ {- m _ {n} \pi x} + \mathrm{e} ^ {- m _ {n} \pi (x - 1)} (\sin m _ {n} \pi + \cos m _ {n} \pi) \\ - (\sin m _ {n} \pi x - \cos m _ {n} \pi x) \\ \mathrm{ie} ^ {- m _ {n} \pi x} + \mathrm{ie} ^ {- m _ {n} \pi (x - 1)} (\sin m _ {n} \pi + \cos m _ {n} \pi) \\ - \mathrm{i} (\sin m _ {n} \pi x - \cos m _ {n} \pi x) \end{array} \right] + O (n ^ {- 1}), \tag {10.4.62}
$$

并且

$$\lim _ {n \rightarrow \infty} \| F _ {n} \| _ {L ^ {2} \times L ^ {2}} ^ {2} = 2.$$

首先注意，对于任意 $y > 0$ 和 $0 \leqslant x \leqslant 1$ ，有

$$
\left\{ \begin{array}{l} \mathrm{e} ^ {- \omega_ {n} y} = \mathrm{e} ^ {- m _ {n} \pi y} + O (n ^ {- 1}), \\ \sin \omega_ {n} x = \sin m _ {n} \pi x + O (n ^ {- 1}), \\ \cos \omega_ {n} x = \cos m _ {n} \pi x + O (n ^ {- 1}), \end{array} \right.
$$

于是我们有

$$
\begin{array}{l} 2 \mathrm{e} ^ {- \omega_ {n}} \omega_ {n} ^ {- 2} f _ {n} ^ {\prime \prime} (x) = \mathrm{e} ^ {- \omega_ {n} x} - \sin \omega_ {n} x + \mathrm{e} ^ {- \omega_ {n} (1 - x)} \sin \omega_ {n} \\ + \cos \omega_ {n} x + e ^ {- \omega_ {n} (1 - x)} \cos \omega_ {n} + O (n ^ {- 1}) \\ = \mathrm{e} ^ {- m _ {n} \pi x} + \mathrm{e} ^ {- m _ {n} \pi (1 - x)} (\sin m _ {n} \pi + \cos m _ {n} \pi) \\ - \left(\sin m _ {n} \pi x - \cos m _ {n} \pi x\right) + O (n ^ {- 1}). \\ \end{array}
$$

类似地可得 $f_{n}$ 本身的估计．从而式(10.4.62)成立．有关 $\| F_n\|_{L^2\times L^2}^2$ 的极限是直接的.

应该指出，这里估计式 (10.4.61) 仅对特定的一列本征值成立，但我们将证明 $\mathcal{A}$ 的广义本征元全体构成 $\mathcal{H}$ 的 Riesz 基，从而实际上式 (10.4.61) 就是 $\mathcal{A}$ 的所有本征值的渐近表达式.

(3) 为了证明 $\mathcal{A}$ 的广义本征元全体构成 $\mathcal{H}$ 的 Riesz 基，依照定理 10.4.4，须要有一个基准 Riesz 基。为此，我们把式 (10.4.57) 中取 $\alpha^{-1} = 0$ 时所对应的斜自伴算子 $\mathcal{A}_0$ 的广义本征元全体作为这一基准 Riesz 基。于是定义

$$\mathcal {A} _ {0} [ f, g ] ^ {\mathrm{T}} = [ f, - a ^ {4} g ] ^ {\mathrm{T}}, \quad \forall [ f, g ] ^ {\mathrm{T}} \in \mathcal {D} (\mathcal {A}),\mathcal {D} (\mathcal {A} _ {0}) = \left\{\left[ f, g \right] ^ {\mathrm{T}} \in V _ {0} ^ {4} (0, 1) \times V _ {0} ^ {2} (0, 1) \mid f ^ {\prime \prime \prime} (1) = 0; g ^ {\prime} (1) = 0 \right\}.$$
