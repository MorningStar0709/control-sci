现在我们假定 $N_{\mu}(A)$ 是 $\mathcal{R}(A_{-1})$ 的一个真子空间。定义 $T \stackrel{\mathrm{def}}{=} \mu I - A, \mathcal{D}(T) = \mathcal{R}(A_{-1})$ 。根据定理5.2.2, $T$ 在 $\mathcal{R}(A_{-1})$ 是有界的，其谱为单点集 $\{0\}$ 。依据式(5.2.7)， $\lim_{n \to \infty} \| T^n \|^{1/n} = 0$ 。此外，注意到 $\mu$ 有有穷指标，并且 $N_{\mu}(A)$ 作为有穷维子空间是闭的，我们有 $T(N_{\mu}(A)) \subset N_{\mu}(A)$ 。设 $X_1 = \mathcal{R}(A_{-1}) / N_{\mu}(A)$ 是Banach商空间，并设 $\hat{T}$ 是如下定义在 $X_1$ 上的线性算子

$$\widehat {T} [ x ] = [ T x ], \quad \forall x \in \mathcal {R} (A _ {- 1}).$$

注意对所有的 $x \in \mathcal{R}(A_{-1})$ ，有 $\widehat{T}^k[x] = [T^k x]$ ，从而

$$
\begin{array}{l} \left\| \widehat {T} ^ {k} [ x ] \right\| = \left\| \left[ T ^ {k} x \right] \right\| \\ = \inf \left\{\| T ^ {k} x - z \| \mid z \in N _ {\mu} (A) \right\} \\ \leqslant \| T ^ {k} \| \| x \|, \quad \forall x \in \mathcal {R} (A _ {- 1}), \\ \end{array}
$$

这表明 $\| \widehat{T}^k\| \leqslant \| T^k\|$ . 于是 $\lim \| \widehat{T}^k\|^{1 / k} = 0$ . 我们断定 $\mathcal{R}(\widehat{T})$ 是 $X_{1}$ 的一闭子空间. 事实上, $\mathcal{R}(\widehat{T})$ 正好是商空间 $(\mathcal{R}(T) + N_{\mu}(A)) / N_{\mu}(A)$ , 而 $\mathcal{R}(T)$ 根据假设是闭的, 并且 $N_{\mu}(A)$ 是有穷维的, 所以 $\mathcal{R}(T) + N_{\mu}(A)$ 是闭的. 因此 $X_{1}$ 作为商空间是闭的. 此外, $\widehat{T}[x] = [0]$ 隐含 $Tx\in N_{\mu}(A)$ . 由此 $0 = (\mu I - A)^m Tx = (\mu I - A)^{m + 1}x = (\mu I - A)^m x$ , 从而 $x\in N_{\mu}(A)$ . 这样我们证明了 $\mathcal{N}(\widehat{T}) = 0$ . 于是 $\widehat{T}$ 是 $X_{1}$ 到 $X_{1}$ 的闭商空间 $\mathcal{R}(\widehat{T})$ 上的一对一映射. 根据假设 $X_{1}$ 为非零子空间, 故依据开映象定理5.1.6, 存在一常数 $c > 0$ 使得 $\| \widehat{T}[x]\| \geqslant c\| [x]\|, \forall [x]\in X_1$ . 由此

$$\| \widehat {T} ^ {k} [ x ] \| \geqslant c ^ {k} \| [ x ] \|, \quad \forall [ x ] \in X _ {1}, k \geqslant 1,$$

$\| \widehat{T}^k\|^{1 / k}\geqslant c,$ 这不可能．从而得证 $N_{\mu}(A) = \mathcal{R}(A_{-1})$

在文献 [2] 中，F. Browder 证明了，若 $A$ 是 Banach 空间 $X$ 中的线性算子， $\mu$ 是 $\sigma(A)$ 中的一孤立点， $N_{\mu}(A)$ 是有穷维的，并且 $\mu$ 是 $R(\lambda; A)$ 的极点，那么 $\mu \in \sigma(A) \backslash \sigma_e(A)$ .

设 $X, Y, Z$ 为 Banach 空间。算子 $A \in \mathcal{L}(X, Y)$ 称为紧的，是指 $A$ 把 $X$ 中任意有界集映成 $Y$ 中相对紧集。 $X$ 到 $Y$ 的所有紧线性算子全体记作 $\mathcal{K}(X, Y)$ ，这是 $\mathcal{L}(X, Y)$ 的一闭线性子空间。如果 $A \in \mathcal{L}(X, Y)$ 和 $B \in \mathcal{K}(Y, Z)$ ，则 $BA \in \mathcal{K}(X, Z)$ 。类似地，如果 $A \in \mathcal{K}(X, Y)$ 和 $B \in \mathcal{L}(X, Y)$ ，则 $BA \in \mathcal{K}(X, Y)$ 。此外，紧线性算子的伴随仍然是紧的。

定理5.2.4 设 $X$ 是Banach空间， $A \in \mathcal{K}(X) \stackrel{\mathrm{def}}{=} \mathcal{K}(X, X)$ . 那么
