上述假设仅涉及到系统主算子 $\mathcal{A}$ . 现在我们假设阻尼 (扰动) 算子 $B \in \mathcal{L}(\mathcal{H})$ 满足:

(H1) $\pmb{B}$ 在 $\mathcal{H}$ 上是耗散的，即

$$\operatorname{Re} \langle \mathcal {B} y, y \rangle \leqslant 0, \quad \forall y \in \mathcal {H};$$

(H2) 如果任意序列 $\{y_n \in \mathcal{H} \mid n \geqslant 1\}$ 满足 $\lim_{n \to \infty} \operatorname{Re}\langle \mathcal{B}y_n, y_n \rangle = 0$ , 则

$$\lim _ {n \rightarrow \infty} \mathcal {B} y _ {n} = 0;$$

(H3) 存在 $\delta > 0$ 使得对于 $\mathcal{A}$ 的任意单位本征元 $\psi$ , 有 $\|B\psi\| \geqslant \delta$ .

由此可见，在上述假设下， $A + B$ 是耗散的并且有紧豫解式.此外，依据Lumer-Phillips定理， $A + B$ 生成一 $C_0$ 压缩半群 $S(t)$ .下面的定理10.4.3和后面的几个例子取自文献[7].

定理 10.4.3 假定 A 是 H 中斜自伴算子，并且 B 满足假设 (H1)\~(H3). 那么由 $A_{1}=A+B$ 生成的 $C_{0}$ 半群 $S(t)$ 是指数稳定的.

证明 根据定理 10.1.6, 由于半群 $S(t)$ 是有界的, 我们只需证明 $\{\mathbf{i}\omega \in \mathbb{R}\} \subset \rho(A_1)$ , 并且

$$K _ {1} \stackrel {\text { def }} {=} \sup \left\{\| (\mathrm{i} \omega - \mathcal {A} _ {1}) ^ {- 1} \| \mid \omega \in \mathbb {R} \right\} < \infty . \tag {10.4.11}$$

首先利用假设 (H2) 容易证明 $\{\mathrm{i}\omega \in \mathbb{R}\} \subset \rho(A_1)$ . 现在我们证明式 (10.4.11) 成立. 若不然, 则存在一数列 $\{\nu_n \mid n \geqslant 1\} \subset \mathbb{R}$ 和一单位元序列 $\{z_n \in D(A) \mid n \geqslant 1\}$ 使得

$$\lim _ {n \rightarrow \infty} \left(\mathcal {A} _ {1} z _ {n} - \mathrm{i} \nu_ {n} z _ {n}\right) = 0. \tag {10.4.12}$$

从上式我们得到

$$0 = \lim _ {n \rightarrow \infty} \operatorname{Re} \left\langle \mathcal {A} _ {1} z _ {n} - \mathrm{i} \nu_ {n} z _ {n}, z _ {n} \right\rangle = \lim _ {n \rightarrow \infty} \operatorname{Re} \left\langle \mathcal {B} z _ {n}, z _ {n} \right\rangle .$$

于是根据假设 (H2), 我们有

$$\lim _ {n \rightarrow \infty} \mathcal {B} z _ {n} = 0. \tag {10.4.13}$$

把式 (10.4.13) 代入式 (10.4.12), 我们得到

$$\lim _ {n \rightarrow \infty} (\mathcal {A} - \mathrm{i} \nu_ {n}) z _ {n} = 0. \tag {10.4.14}$$

今将 $z_{n}$ 展开成Fourier级数

$$z _ {n} = \sum_ {m = 1} ^ {\infty} \sum_ {j = 1} ^ {r _ {m}} \left\langle z _ {n}, \varphi_ {m j} \right\rangle \varphi_ {m j}.$$

于是从式 (10.4.14) 得到

$$\lim _ {n \rightarrow \infty} (\mathcal {A} - i \nu_ {n}) z _ {n} = \lim _ {n \rightarrow \infty} \sum_ {m = 1} ^ {\infty} \sum_ {j = 1} ^ {r _ {m}} i (\omega_ {m} - \nu_ {n}) \langle z _ {n}, \varphi_ {m j} \rangle \varphi_ {m j} = 0.$$

因此，对于任意 $\varepsilon > 0$ 。存在正整数 $N_{\varepsilon}$ 使得
