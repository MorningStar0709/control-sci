$$
\begin{array}{l} e ^ {\lambda_ {i} T} - 1 = e ^ {\alpha T} \cos \beta T + j e ^ {\alpha T} \sin \beta T - 1 \\ \neq e ^ {\alpha T} \cos l \pi + j e ^ {\alpha T} \sin l \pi - 1 = 0 \tag {3.144} \\ \end{array}
$$

其中 $\alpha$ 和 $\beta$ 分别表示 $\lambda_{i}$ 的实部和虚部。这表明，在结论条件下，必有

$$\det \left[ \int_ {0} ^ {T} e ^ {A t} d t \right] \neq 0 \tag {3.145}$$

也即 $\int_0^T e^{At}dt$ 为非奇异。此外， $e^{AT}$ 和 $\int_0^T e^{At}dt$ 为可交换的。由此，就可导出

$$
\begin{array}{l} [ H | G H | \dots | G ^ {n - 1} H ] = \left[ \int_ {0} ^ {T} e ^ {A t} d t B \mid e ^ {A T} \int_ {0} ^ {T} e ^ {A t} d t B \right| \\ \dots \left| (e ^ {A T}) ^ {n - 1} \int_ {0} ^ {T} e ^ {A t} d t B \right] = \int_ {0} ^ {T} e ^ {A t} d t \cdot [ B; e ^ {A T} B; \\ \dots \left| \left(e ^ {A T}\right) ^ {n - 1} B \right] \tag {3.146} \\ \end{array}
$$

并且，在(3.138)和(3.139)下， $\Sigma_{T}$ 能控当且仅当

$$\operatorname{rank} [ B \mid e ^ {A T} B \mid \dots \mid (e ^ {A T}) ^ {n - 1} B ] = n \tag {3.147}$$

再利用凯莱-哈密顿定理可知， $e^{AkT}(k=n,n+1,\cdots)$ 均可表为 $I,e^{AT},\cdots,e^{A(n-1)T}$ 的线性组合。因此，式(3.147)又等价于 $e^{AkT}B$ 的行线性无关。从而，证得在结论条件下 $\Sigma_{T}$ 能控归结为 $e^{AkT}B$ 行线无关。

进而来证明：在条件（3.138）和（3.139）下， $\Sigma$ 能控必有 $e^{AkT}B$ 行线性无关。

采用反证法。反设 $e^{AkT}B$ 行线性相关，则必存在非零常向量 $\alpha$ 使成立

$$\boldsymbol {a} ^ {T} e ^ {\boldsymbol {A} k T} \boldsymbol {B} = 0, \quad \forall k \tag {3.148}$$

进而，由约当规范形（3.140）可知， $e^{AkT}$ 的元为 $e^{\lambda_{i}kT}$ 和 $(kT)$ 的多项式的乘积；所以，由

此可把上式改写成为

$$\boldsymbol {a} ^ {T} e ^ {\lambda k T} B = P _ {1} (k T) e ^ {\lambda_ {1} k T} + \dots + P _ {\mu} (k T) e ^ {\lambda_ {\mu} k T} = 0 \tag {3.149}$$

其中 $P_{i}(kT)$ 为 $1 \times p$ 的矩阵。而由 $\Sigma$ 为完全能控知 $e^{At}B$ 行线性无关，因此对上述非零常向量 $\alpha$ 应成立

$$\boldsymbol {a} ^ {T} e ^ {A t} B \neq 0, \quad \forall t \tag {3.150}$$

或表为

$$\boldsymbol {a} ^ {T} e ^ {A t} B = P _ {1} (t) e ^ {\lambda_ {1} t} + \dots + P _ {\mu} (t) e ^ {\lambda_ {\mu} t} \neq 0 \tag {3.151}$$

进一步,取 t = kT，那么(3.151)可表为

$$\alpha^ {T} e ^ {A k T} B = P _ {1} (k T) e ^ {\lambda_ {1} k T} + \dots + P _ {\mu} (k T) e ^ {\lambda_ {\mu} k T} \tag {3.152}$$

不失一般性，假定特征值 $\lambda_{1}, \lambda_{2}, \cdots, \lambda_{\mu}$ 中前 r 个具有相同的实部， $r < \mu$ ，且

$$\operatorname{Re} \left[ \lambda_ {1} \right] > \operatorname{Re} \left[ \lambda_ {m} \right], \quad r < m \leqslant \mu \tag {3.153}$$

再设 $P_{i}(t)$ 的元多项式中 t 的最高幂次为 $v, i = 1, 2, \cdots, \mu$ ，用 $d_{i0}^{\eta}$ 表示 $P_{i}(t)$ 的元多项式 $p_{i\eta}(t)(\eta = 1, 2, \cdots, p)$ 中 $t^{p}$ 的系数，且不妨认为

$$d _ {i 0} ^ {\eta} \neq 0, \quad i = 1, 2, \dots , \zeta , \zeta < r \tag {3.154}$$

这样，将(3.152)的第 $\pmb{\eta}$ 个元乘以
