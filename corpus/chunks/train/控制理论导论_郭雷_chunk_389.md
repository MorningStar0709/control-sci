定理 5.3.17 设 $T(t)$ 是 Banach 空间 X 上由 A 生成的 $C_{0}$ 半群. 如果 $T'(t)$ 按算子拓扑是一致连续的，则存在函数 $\psi:[0,\infty)\to[0,\infty)$ 使得

$$\rho (A) \supset \left\{\lambda = \sigma + \mathrm{i} \tau \mid | \tau | \geqslant \psi (| \sigma |) \right\}, \tag {5.3.36}$$

并且对于任意 $\sigma \in \mathbb{R}$

$$\| R (\sigma + \mathrm{i} \tau ; A) \| \rightarrow 0 \quad (| \tau | \rightarrow \infty). \tag {5.3.37}$$

证明 不失一般性，我们可以假定 $\rho(A) \subset \{\lambda \mid \operatorname{Re} \lambda > 0\}$ 和 $\|T(t)\| \leqslant M, \forall t \geqslant 0$ 。如果 $\sigma > 0$ ，则根据上述假设， $\lambda = \sigma + i\tau \in \rho(A)$ 。把 $x = R(\lambda; A)y$ 代入式 (5.3.29)，我们得到

$$\mathrm{e} ^ {\lambda t} R (\lambda ; A) y - T (t) R (\lambda ; A) y = B _ {\lambda} (t) y, \quad \forall y \in X,$$

这表明

$$\left(\mathrm{e} ^ {\sigma t} - M\right) \| R (\lambda ; A) \| \leqslant \mathrm{e} ^ {\sigma t} \left\| \int_ {0} ^ {t} \mathrm{e} ^ {- \mathrm{i} \tau t} \mathrm{e} ^ {- \sigma t} T (t) \mathrm{d} s \right\|.$$

于是对于 $t > \sigma^{-1}\log M$ ，我们有

$$\| R (\lambda ; A) \| \leqslant C \left\| \int_ {0} ^ {t} \mathrm{e} ^ {- \mathrm{i} \tau t} \mathrm{e} ^ {- \sigma t} T (t) \mathrm{d} s \right\|,$$

式中 $C$ 为一与 $\tau$ 无关的正常数。根据实变函数论中的Riemann-Lebesgue引理，上式右端当 $|\tau| \to \infty$ 时趋于0。对于 $\sigma \leqslant 0$ ，我们有

$$R (\lambda ; A) = \sum_ {k = 1} ^ {\infty} R (1 + \mathrm{i} \tau ; A) ^ {k + 1} (1 + \mathrm{i} \tau - \lambda) ^ {k}. \tag {5.3.38}$$

令

$$\varphi (| \tau |) = \max _ {| t | \geqslant | \tau |} \| R (1 + \mathrm{i} \tau ; A) \|.$$

依据上面已经证明的结论，当 $|\tau| \to \infty$ 时 $\varphi(|\tau|) \to 0$ 。显然级数 (5.3.38) 当 $|1 - \sigma| \leqslant 1/2\varphi(|\tau|)$ 时按一致算子拓扑收敛，从而式 (5.3.36) 成立。此外，对于任意满足 $|1 - \sigma| \leqslant 1/2\varphi(|\tau|)$ 的 $\sigma$ ，我们有

$$\| R (\sigma + \mathrm{i} \tau ; A) \| \leqslant 2 \| R (1 + \mathrm{i} \tau ; A) \| \leqslant 2 \varphi (| \tau |),$$

从而式 (5.3.37) 成立. 证毕.
