# 三级数准则及鞅差局部收敛（续）

引理4.2.4 设 $(x_{k},\mathcal{F}_{k})$ 为适应序列， $\{b_k\}$ 为正实数序列，记

$$A \stackrel {\mathrm{def}} {=} \left\{\sum_ {k = 1} ^ {\infty} P (| x _ {k} | > b _ {k}) | \mathcal {F} _ {k - 1}) < \infty \right\}.$$

在 $A$ 上 $\sum_{k=1}^{\infty} x_k$ 收敛等价于 $\sum_{k=1}^{\infty} x_k I_{[|x_k| \leqslant b_k]}$ 收敛.

证明 记 $B_{k} \stackrel{\mathrm{def}}{=} \{|x_{k}| > b_{k}\}$ . 用定理4.3.3知

$$A = \left\{\sum_ {k = 1} ^ {\infty} I _ {B _ {k}} < \infty \right\}.$$

这说明 $A$ 表示 $B_{k}$ 只出现有穷次的集合，也就是说，固定 $\omega$ ，只要 $k$ 充分大，必有 $I_{[|x_k|\leqslant b_k]} = 1$ ，所以在 $A$ 上定理结论中两级数的收敛性等价.

定理4.2.10（三级数准则）设 $(x_{k},\mathcal{F}_{k})$ 为适应序列．用 $S$ 表示下面三个级数同时收敛的 $\omega$ 集：

$$\sum_ {k = 1} ^ {\infty} P (| x _ {k} | \geqslant c | \mathcal {F} _ {k - 1}), \quad \sum_ {k = 1} ^ {\infty} E (x _ {k} I _ {[ | x _ {k} | \leqslant c ]} | \mathcal {F} _ {k - 1}),\sum_ {k = 1} ^ {\infty} \left\{E (x _ {k} ^ {2} I _ {\{| x _ {k} | \leqslant c \}} | \mathcal {F} _ {k - 1}) - \left(E (x _ {k} I _ {\{| x _ {k} | \leqslant c \}} | \mathcal {F} _ {k - 1})\right) ^ {2} \right\},$$

其中 $c$ 为正常数，那么

$$\xi_ {n} \stackrel {\mathrm{def}} {=} \sum_ {k = 1} ^ {n} x _ {k} \text {在} S \text {上收敛.}$$

证明 记

$$A \stackrel {\mathrm{def}} {=} \left\{\sum_ {k = 1} ^ {\infty} P (| x _ {k} | \geqslant c | \mathcal {F} _ {k - 1}) < \infty \right\}.$$

据引理 4.2.4, 在 A 上 $\sum_{k=1}^{\infty}x_{k}$ 收敛等价于 $\sum_{k=1}^{\infty}x_{k}I_{\left[\left|x_{k}\right|\leqslant c\right]}$ 收敛. 由于 $S \subset A$ , 所以在 S 上 $\sum_{k=1}^{\infty}x_{k}$ 收敛等价于 $\sum_{k=1}^{\infty}x_{k}I_{\left[\left|x_{k}\right|\leqslant c\right]}$ 收敛. 记

$$y _ {k} = x _ {k} I _ {\{| x _ {k} | \leqslant c \}} - E [ x _ {k} I _ {\{| x _ {k} | \leqslant c \}} | \mathcal {F} _ {k - 1} ].$$

据 $S$ 的定义，在 $S$ 上 $\sum_{k=1}^{\infty} E[x_k I_{\{|x_k| \leqslant c\}} | \mathcal{F}_{k-1}]$ 收敛，所以在 $S$ 上 $\sum_{k=1}^{\infty} x_k I_{\{|x_k| \leqslant c\}}$ 收敛等价于 $\sum_{k=1}^{\infty} y_k$ 收敛，因此在 $S$ 上 $\sum_{k=1}^{\infty} x_k$ 收敛等价于 $\sum_{k=1}^{\infty} y_k$ 收敛。但 $(y_k, \mathcal{F}_k)$ 是鞅差列，并且

$$E (y _ {k} ^ {2} | \mathcal {F} _ {k - 1}) = E (x _ {k} ^ {2} I _ {\{| x _ {k} | \leqslant c \}} | \mathcal {F} _ {k - 1}) - (E (x _ {k} I _ {\{| x _ {k} | \leqslant c \}} | \mathcal {F} _ {k - 1})) ^ {2}.$$

据 $S$ 的定义， $S \subset \left\{\sum_{k=1}^{\infty} E(y_k^2 | \mathcal{F}_{k-1}) < \infty \right\}$ .

用定理4.2.6知 $\sum_{k=1}^{\infty} y_k$ 在 $S$ 上收敛，但在 $S$ 上 $\sum_{k=1}^{\infty} x_k$ 收敛等价于 $\sum_{k=1}^{\infty} y_k$ 收敛，所以在 $S$ 上 $\xi_n$ 收敛.
