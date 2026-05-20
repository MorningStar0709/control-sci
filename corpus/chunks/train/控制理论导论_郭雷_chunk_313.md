$$\sum_ {k = 1} ^ {\infty} \frac {1}{s _ {k} (\alpha) \log^ {\frac {1}{\alpha} + \eta} (s _ {k} ^ {\alpha} (\alpha) + e)} M _ {k} X _ {k + 1} \qquad \text {a.s.} \quad \text {收敛.} \tag {4.2.15}$$

记 $a_{k} = s_{k}(\alpha)\log^{\frac{1}{\alpha} +\eta}(s_{k}^{\alpha}(\alpha) + \mathrm{e}), a_{k}$ 单调非降. 从式 (4.2.15) 知序列 $y_{n} \stackrel{\mathrm{def}}{=} \sum_{k=0}^{n} a_{k}^{-1} M_{k}$ . $X_{k+1}$ 对 $n$ 有界, 即存在可能依赖于 $\omega$ 的 $\zeta < \infty$ 使 $\| y_{n} \| \leqslant \zeta, \forall n$ . 这样我们有

$$
\begin{array}{l} \left\| \sum_ {k = 1} ^ {n} M _ {k} X _ {k + 1} \right\| = \left\| \sum_ {k = 1} ^ {n} a _ {k} \left(y _ {k} - y _ {k - 1}\right) \right\| \\ = \left\| a _ {n} y _ {n} - a _ {0} y _ {0} - \sum_ {k = 1} ^ {n} \left(a _ {k} - a _ {k - 1}\right) y _ {k - 1} \right\| \\ \leqslant O \left(a _ {n}\right) + \sum_ {k = 1} ^ {n} \left(a _ {k} - a _ {k - 1}\right) \| y _ {k - 1} \| \\ = O \left(a _ {n}\right) + O \left(\sum_ {k = 1} ^ {n} \left(a _ {k} - a _ {k - 1}\right)\right) = O \left(a _ {n}\right). \\ \end{array}
$$

注4.2.4 设 $\{X_{n},\mathcal{F}_{n}\}$ 为鞅差列， $\sup_n E[\| X_{n + 1}\|^{\alpha}|\mathcal{F}_k] < \infty$ a.s. 并且 $X_{k}\neq 0$ a.s. 记

$$M _ {k} \stackrel {\text { def }} {=} E [ \| x _ {k + 1} \| ^ {\alpha} | \mathcal {F} _ {k} ] \neq 0 \quad \text { a.s., } \quad X _ {k + 1} ^ {\prime} \stackrel {\text { def }} {=} \frac {X _ {k + 1}}{M _ {k} ^ {\frac {1}{\alpha}}} \quad \forall k.$$

那么 $(X_k', \mathcal{F}_k)$ 仍为鞅差列，并且 $E(\| X_{k+1}'\|^{\alpha}|\mathcal{F}_k) = 1,$

$$X _ {k + 1} = M _ {k} ^ {\frac {1}{\alpha}} X _ {k + 1} ^ {\prime}.$$

所以估计鞅差和 $\sum_{k=1}^{n} X_k$ ，等价于估计 $\sum_{k=1}^{n} M_k^{\frac{1}{\alpha}} X_{k+1}'$ ，而后者适用定理 4.2.13。当 $\alpha = 1$ 时，就有

$$\sum_ {k = 1} ^ {n} X _ {k} = O \left(s _ {n} (2) \log^ {\frac {1}{2} + \eta} \left(s _ {n} ^ {2} (2) + e\right)\right).$$

和式 (4.2.12), (4.2.13) 相比, 这里估计较粗, 但所用条件更为一般.
