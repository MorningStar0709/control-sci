$$R (\lambda ; A) = R \left(\sigma_ {0} + i \tau ; A\right) \left[ I - \left(\sigma_ {0} - \sigma\right) R \left(\sigma_ {0} + i \tau ; A\right) \right] ^ {- 1},$$

从而

$$\| R (\lambda ; A) \| \leqslant M ^ {p} q / (q - 1), \quad \forall 0 \leqslant \operatorname{Re} \lambda < \sigma_ {0}. \tag {10.1.17}$$

于是我们证明了 $\lambda \in \rho(A), \forall \lambda \in \mathbb{C}_{+}$ , 以及

$$\sup \left\{\| R (\lambda ; A) \| \mid \operatorname{Re} \lambda \geqslant 0 \right\} \leqslant \max \left\{M ^ {p}, M ^ {p} q / (q - 1) \right\}.$$

根据定理 10.1.5, $T(t)$ 指数稳定.

当 $p = 1$ 时，取 $\sigma = (2M)^{-1}$ ，我们有

$$R (\mathrm{i} \tau ; A) = R (\sigma + \mathrm{i} \tau ; A) [ I - \sigma R (\sigma + \mathrm{i} \tau ; A) ] ^ {- 1}, \quad \forall \tau \in \mathbb {R},$$

这意味着 $i\tau \in \rho(A), \forall \tau \in \mathbb{R}$ , 并且

$$\left\| R (\mathrm{i} \tau ; A) \right\| \leqslant 2 M.$$

于是从式 (10.1.17) 得到

$$\| R (\lambda ; A) \| \leqslant 2 M, \quad \forall \lambda \geqslant 0.$$

最后，再次利用定理10.1.5，得知 $T(t)$ 是指数稳定的．证毕.

在有穷维空间 $X = \mathbb{R}^n$ 中，本节开始提到的前3种稳定性都是等价的。特别是通过选择适当的Lyapunov函数，可以得到如下结果：(见第2章)

设 $\pmb{A}$ 是 $n\times n$ 矩阵，则为了 $T(t) = \mathrm{e}^{At}$ 指数稳定，一个充分必要条件是存在一正定矩阵 $\pmb{P}$ 使得

$$\boldsymbol {P} \boldsymbol {A} + \boldsymbol {A} ^ {*} \boldsymbol {P} = - \boldsymbol {I}, \tag {10.1.18}$$

其中 I 表示 $n \times n$ 单位矩阵，而 $A^{*}$ 表示 A 的伴随矩阵。于是 $V(x) = (Px, x)$ 是相应的 Lyapunov 函数，即对于方程

$$\frac {\mathrm{d} x (t)}{\mathrm{d} t} = A x (t) \tag {10.1.19}$$

的任意解 $x(t)$ ，我们有

$$\frac {\mathrm{d}}{\mathrm{d} t} (P x (t), x (t)) < 0, \quad t \geqslant 0. \tag {10.1.20}$$

现在我们的目的是把上述有关式 (10.1.18) 的结论推广到无穷维情形。为此我们先证明几个引理。

设 $H$ 是一复 Hilbert 空间. $H$ 中有界对称线性算子 $P$ 称为非负的，写成 $P \geqslant 0$ , 是指 $(Px, x) \geqslant 0, \forall x \in H$ .

定理10.1.9 设 $T(t)$ 是Hilbert空间 $H$ 上一 $C_0$ 半群， $A$ 为其生成算子。那么 $T(t)$ 指数稳定当且仅当存在 $H$ 中一有界对称算子 $P \geqslant 0$ 使得

$$(A x, P x) + (P x, A x) = - \| x \| ^ {2}, \quad \forall x \in \mathcal {D} (A). \tag {10.1.21}$$

证明 先证充分性. 设 $H$ 中有界线性算子 $P \geqslant 0$ 满足式 (10.1.21). 令

$$V (x, t) \stackrel {\mathrm{def}} {=} (P T (t) x, T (t) x), \quad x \in H, t \geqslant 0. \tag {10.1.22}$$

从 $P$ 的非负性得到

$$V (x, t) \geqslant 0, \quad \forall x \in H, t \geqslant 0.$$

设 $x \in \mathcal{D}(A)$ , 则 $V(x, t)$ 相对 $t$ 是可微的, 并且

$$\frac {\mathrm{d}}{\mathrm{d} t} V (x, t) = (P A T (t) x, T (t) x) + (T (t) x, P A T (t) x) = - \| T (t) x \| ^ {2}.$$

对上式两端从0到 $t$ 积分得到

$$V (x, 0) \geqslant \int_ {0} ^ {t} \| T (s) x \| ^ {2} \mathrm{d} s, \quad \forall t \geqslant 0. \tag {10.1.23}$$
