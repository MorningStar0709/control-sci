# 鞅差和估计

我们先证常用的 Kronecker 引理.

引理 4.2.5 设 $b_{k} > 0, b_{k} \uparrow \infty, M_{k}$ 为任一数列．如果级数 $\sum_{k=1}^{\infty} \frac{M_{k}}{b_{k}}$ 收敛，则 $\frac{1}{b_{n}} \sum_{k=1}^{n} M_{k} \xrightarrow[n \to \infty]{\longrightarrow} 0.$

证明 记 $N_0 \stackrel{\mathrm{def}}{=} 0, N_n \stackrel{\mathrm{def}}{=} \sum_{k=1}^{n} \frac{M_k}{b_k}, n \geqslant 1, N \stackrel{\mathrm{def}}{=} \sum_{k=1}^{\infty} \frac{M_k}{b_k}$ . 据条件对任意 $\epsilon > 0$ , 存在 $n_\epsilon$ , 只要 $k > n_\epsilon$ , 必有

$$\left| N _ {k} - N \right| < \epsilon , \quad \forall k \geqslant n _ {\epsilon}.$$

那么我们得到

$$
\begin{array}{l} \left| \frac {1}{b _ {n}} \sum_ {k = 1} ^ {n} M _ {k} \right| = \left| \frac {1}{b _ {n}} \sum_ {k = 1} ^ {n} b _ {k} (N _ {k} - N _ {k - 1}) \right| = \left| N _ {n} + \frac {1}{b _ {n}} \sum_ {k = 2} ^ {n} (b _ {k - 1} - b _ {k}) N _ {k - 1} \right| \\ = \left| N _ {n} - \frac {b _ {n} - b}{b _ {n}} N + \frac {1}{b _ {n}} \sum_ {k = 2} ^ {n} (b _ {k - 1} - b _ {k}) (N _ {k - 1} - N) \right| \\ \leqslant | N _ {n} - N | + \frac {b _ {1}}{b _ {n}} | N | + \frac {1}{b _ {n}} \sum_ {k = 2} ^ {n _ {\epsilon}} (b _ {k - 1} - b _ {k}) | N _ {k - 1} - N | + \epsilon \underset {\begin{array}{c}n \rightarrow \infty\\\epsilon \rightarrow 0\end{array}} {\longrightarrow} 0. \\ \end{array}
$$

定理 4.2.12 (强大数法则) 设 $\{x_{k}, F_{k}\}$ 为鞅差列，对某个 p > 1, $\sup_{k} E|x_{k}|^{p} < \infty$ 或 $\sup_{k} E[|x_{k}|^{p} |F_{k-1}] < \infty$ a.s., 则

$$\frac {1}{n} \sum_ {k = 1} ^ {n} x _ {k} \underset {n \to \infty} {\longrightarrow} 0 \quad \text { a.s. }$$

证明 在推论4.2.5中取 $q = p$ ，便知 $\sum_{k=1}^{\infty} \frac{x_k}{k}$ a.s. 收敛。用引理4.2.5便得定理结论。

注4.2.3 Kolmogorov 强大数法则针对 $\{x_{k}\}$ 相互独立相同分布的随机变量序列，当 $E|x_{1}| < \infty$ 时，断定 $\frac{1}{n} \sum_{k=1}^{n} x_{k} \xrightarrow[n \to \infty]{\longrightarrow} Ex_{1}$ a.s. 和定理4.2.11相比，把鞅差增强到iid,但把 $p (>1)$ 阶矩减弱为1阶矩.

对鞅差列，也成立中心极限定理。设 $\{x_{k},\mathcal{F}_{k}\}$ 为鞅差列。我们沿用上面的符号， $s_n\stackrel {\mathrm{def}}{=}\left(\sum_{j = 1}^{n}Ex_j^2\right)^{\frac{1}{2}}$

若 $\frac{1}{s_n^2}\sum_{k = 1}^{n}E(x_k^2 |\mathcal{F}_{k - 1})\xrightarrow[p]{p}1,$ 并且成立Lindeberg条件，即对任意 $\epsilon >0$

$$\frac {1}{s _ {n} ^ {2}} \sum_ {k = 1} ^ {n} E x _ {k} ^ {2} I _ {\{| x _ {k} | > \epsilon s _ {n} \}} \underset {n \rightarrow \infty} {\longrightarrow} 0, \tag {4.2.10}$$

则
