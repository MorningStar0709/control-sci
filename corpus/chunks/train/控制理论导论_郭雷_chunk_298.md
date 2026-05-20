证明 必要性直接从上面的讨论中得出．现证充分性．设 $\xi$ 的分布函数为 $F(x_{1},\cdots,x_{k}),\xi_{k}$ 的分布函数为 $F_{k}(x_{k}), k=1,\cdots,n.$ 记 $G(x_{1},\cdots,x_{n})\stackrel{\mathrm{def}}{=}F_{1}(x_{1})\cdots F_{n}(x_{n}),\lambda^{\mathrm{T}}\stackrel{\mathrm{def}}{=}[\lambda_{1},\cdots,\lambda_{n}], x^{\mathrm{T}}=[x_{1},\cdots,x_{n}]$ ，那么

$$
\begin{array}{l} \int_ {\mathbb {R} ^ {n}} \mathrm{e} ^ {\mathrm{i} \lambda^ {\mathrm{T}} x} \mathrm{d} G (x _ {1}, \dots , x _ {n}) = \prod_ {k = 1} ^ {n} \int_ {\mathbb {R}} \mathrm{e} ^ {\mathrm{i} \lambda_ {k} x _ {k}} \mathrm{d} F _ {k} (x _ {k}) = \prod_ {k = 1} ^ {n} E \mathrm{e} ^ {\mathrm{i} \lambda_ {k} \xi_ {k}} \\ = E \mathrm{e} ^ {\mathrm{i} (\lambda_ {1} \xi_ {1} + \dots + \lambda_ {n} \xi_ {n})} = \int_ {\mathbb {R} ^ {n}} \mathrm{e} ^ {\mathrm{i} (\lambda_ {1} x _ {1} + \dots + \lambda_ {n} x _ {n})} \mathrm{d} F (x _ {1}, \dots , x _ {n}). \\ \end{array}
$$

由于分布函数由特征函数唯一地确定，所以

$$F (x _ {1}, \dots , x _ {n}) = F _ {1} (x _ {1}) \dots F _ {n} (x _ {n}),$$

也就是说 $\xi_{1},\cdots,\xi_{n}$ 相互独立.

设 $X_{1}, X_{2}, \cdots, X_{n}$ 为相互独立的随机变量，记 $S_{n} = \sum_{j=1}^{n} X_{j}$ . 据式 (4.1.11)，求 $S_{n}$ 的分布函数，等同于求 $S_{n}$ 的特征函数

$$E \mathrm{e} ^ {\mathrm{i} \lambda S _ {n}} = E \mathrm{e} ^ {\mathrm{i} \lambda \sum_ {j = 1} ^ {n} X _ {j}}.$$

根据独立性，便知

$$E \mathrm{e} ^ {\mathrm{i} \lambda S _ {n}} = E \prod_ {j = 1} ^ {n} \mathrm{e} ^ {\mathrm{i} \lambda X _ {j}} = \prod_ {j = 1} ^ {n} E \mathrm{e} ^ {\mathrm{i} \lambda X _ {j}} = \prod_ {j = 1} ^ {n} f _ {j} (\lambda),$$

这里 $f_{j}(\lambda)$ 表示 $X_{j}$ 的特征函数.

所以为求独立变量和的分布函数，只要求它们的特征函数的乘积，这就是推导下面的极限定理的主要方法.

收敛到正态分布的极限定理，称为中心极限定理。下面定理4.2.2的第2部分就是一个中心极限定理。

定理 4.2.2 设 $\{X_{i}\}, i=1,2,\cdots$ ，为相互独立的随机变量.

(1) 设对某一 $\delta \in (0,1]$ , $\frac{1}{n^{1 + \delta}} \sum_{j=1}^{n} E|X_j - EX_j|^{1 + \delta} \to 0$ , 那么下列弱大数定律成立:

$$\frac {1}{n} \sum_ {j = 1} ^ {n} (X _ {j} - E X _ {j}) \xrightarrow [ n \to \infty ]{w} 0;$$

(2) 记 $s_n = \left(\sum_{j=1}^{n} E(X_j - EX_j)^2\right)^{\frac{1}{2}}$ . 设对某 $\delta \in (0, 1]$ , $\frac{1}{s_n^{2+\delta}} \sum_{j=1}^{n} E|X_j - EX_j|^{2+\delta} \to 0$ , 那么,

$$P \left(s _ {n} ^ {- 1} \sum_ {j = 1} ^ {n} (X _ {j} - E X _ {j}) < x\right) \underset {n \rightarrow \infty} {\longrightarrow} \frac {1}{\sqrt {2 \pi}} \int_ {- \infty} ^ {x} e ^ {- \frac {t ^ {2}}{2}} d t,$$

也就是左边的分布函数收敛到正态分布 $\mathcal{N}(0,1)$ .
