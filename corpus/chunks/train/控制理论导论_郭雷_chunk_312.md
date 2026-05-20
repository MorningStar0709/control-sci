$$\lim _ {n \rightarrow \infty} P \left(\frac {1}{s _ {n}} \sum_ {k = 1} ^ {n} E x _ {k} < x\right) = \frac {1}{\sqrt {2 \pi}} \int_ {- \infty} ^ {x} \mathrm{e} ^ {- \frac {t ^ {2}}{2}} \mathrm{d} t. \tag {4.2.11}$$

对鞅差列，还成立重对数律．设 $(x_{k},\mathcal{F}_{k})$ 为鞅差列，且同分布， $Ex_{k}^{2}=\sigma^{2}$ ，那么

$$\limsup _ {n \to \infty} (2 \sigma^ {2} n \log \log n) ^ {- \frac {1}{2}} \sum_ {k = 1} ^ {n} x _ {k} = + 1 \quad \text { a.s. } \tag {4.2.12}\liminf _ {n \to \infty} (2 \sigma^ {2} n \log \log n) ^ {- \frac {1}{2}} \sum_ {k = 1} ^ {n} x _ {k} = - 1 \quad \text { a.s. } \tag {4.2.13}$$

当“同分布”换成“一致有界性”后，在 $[r_n \to \infty]$ 上仍成立上述重对数律，只是应把 $n\sigma^2$ 换成 $r_n^2 \stackrel{\mathrm{def}}{=} \sum_{k=1}^{n} E(x_k^2 | \mathcal{F}_{k-1})$ .

在牵涉到随机量的分析时，下述加权鞅差和估计很有用.

定理 4.2.13 设 $\{X_{k}, F_{k}\}$ 为鞅差列， $X_{k}$ 可以是一个阵。设 $(M_{k}, F_{k})$ 为适应过程， $M_{k}$ 也可以是阵， $\|M_{k}\| < \infty$ a.s. $\forall k$ 。设对某 $\alpha \in (0, 2]$

$$\sup _ {n} E [ \| X _ {n + 1} \| ^ {\alpha} | \mathcal {F} _ {n} ] < \infty \quad \text { a.s. },$$

那么若记 $s_n(\alpha) = \left(\sum_{k=0}^{n} \|M_k\|^{\alpha}\right)^{\frac{1}{\alpha}}$ ，当 $n \to \infty$ 时，有

$$\sum_ {k = 0} ^ {n} M _ {k} X _ {k + 1} = O (s _ {n} (\alpha) \log^ {\frac {1}{\alpha} + \eta} (s _ {n} ^ {\alpha} (\alpha) + e)) \quad \text { a.s. } \quad \forall \eta > 0. \tag {4.2.14}$$

证明 不失一般性可认为 $M_0 \neq 0$ . 记

$$\sigma = \sup _ {n \geqslant 0} E [ \| X _ {n + 1} \| ^ {\alpha} | \mathcal {F} _ {n} ].$$

由于 $s_k(\alpha)$ 及 $M_{k}$ 对 $\mathcal{F}_k$ 可测，所以用定理条件知

$$
\begin{array}{l} \sum_ {k = 1} ^ {\infty} E \left[ \left\| \left(s _ {n} (\alpha) \log^ {\frac {1}{\alpha} + \eta} \left(s _ {k} ^ {\alpha} (\alpha) + e\right)\right) ^ {- 1} M _ {k} X _ {k + 1} \right\| ^ {\alpha} \mid \mathcal {F} _ {k} \right] \\ \leqslant \sigma \sum_ {k = 1} ^ {\infty} \left(s _ {k} ^ {\alpha} (\alpha) \log^ {1 + \eta \alpha} \left(s _ {k} ^ {\alpha} (\alpha) + c\right)\right) ^ {- 1} \| M _ {k} \| ^ {\alpha} \\ = \sigma \sum_ {k = 1} ^ {\infty} \left(s _ {k} ^ {\alpha} (\alpha) \log^ {1 + \eta \alpha} \left(s _ {k} ^ {\alpha} (\alpha) + e\right)\right) ^ {- 1} \int_ {s _ {k - 1} ^ {\alpha} (\alpha)} ^ {s _ {k} ^ {\alpha} (\alpha)} d x \\ \leqslant \sigma \sum_ {k = 1} ^ {\infty} \int_ {s _ {k - 1} ^ {a} (\alpha)} ^ {s _ {k} ^ {a} (\alpha)} \frac {\mathrm{d} x}{x \log^ {1 + \eta \alpha} (x + e)} \leqslant \sigma \int_ {s _ {0} ^ {a} (\alpha)} ^ {\infty} \frac {\mathrm{d} x}{x \log^ {1 + \eta \alpha} (x + e)} <   \infty . \\ \end{array}
$$

由定理4.2.11知
