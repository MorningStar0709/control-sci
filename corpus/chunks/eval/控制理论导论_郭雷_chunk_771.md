(1) $\Longrightarrow$ (6). 设 $(A, B)$ 是完全近似能控的. 如果 $x \in \mathcal{N}(B^{*}) \cap \mathcal{N}(\mathrm{i}\omega - A)$ , 即 $Ax = \mathrm{i}\omega x$ 和 $B^{*}x = 0$ , 则 $B^{*}T^{A^{*}}(t)x = \mathrm{e}^{-\mathrm{i}\omega t}B^{*}x = 0, \forall t \geqslant 0$ . 但 $(A, B)$ 是完全近似能控的, 故 $x = 0$ , 这表明 (6) 成立.

(5) $\Longrightarrow$ (4). 在假设 (5) 之下, $A - BB^{*}$ 是耗散的, 因此我们有

$$\sigma (A - B B ^ {*}) \subset \mathbb {C} ^ {\sim} = \{\lambda \in \mathbb {C} | \operatorname{Re} \lambda < 0 \}.$$

于是 $(5) \Longrightarrow (4)$ 直接从定理10.1.11推出.

(2) $\Longrightarrow$ (6). 设 $K \in \mathcal{L}(H, U)$ 使得 $T^{A + BK}(t)$ 是强稳定的. 由于 $A + BK$ 具有紧豫解式, 故 $\sigma(A + BK) \subset \mathbb{C}^{-}$ . 于是

$$\sigma ((A + B K) ^ {*}) \sigma (- A S + K ^ {*} B ^ {*}) = \overline {{{{\sigma (A + B K)}}}} \subset \mathbb {C} ^ {-},$$

这里 $\overline{\sigma(A + BK)}$ 表示复数集 $\sigma(A + BK)$ 的复共轭。如果存在 $\omega \in \mathbb{R}$ 和 $x \in H$ 使得

$$0 \neq x \in \mathcal {N} (B ^ {*}) \cap \mathcal {N} (\mathrm{i} \omega I - A),$$

即 $B^{*}x = 0$ 并且 $Ax = \mathrm{i}\omega x$ ，则 $(-A + K^{*}B^{*})x = -\mathrm{i}\omega x,$ 也即 $-\mathrm{i}\omega \in \sigma (-A + K^{*}B^{*}),$ 这与 $\sigma (-A + K^{*}B^{*})\subset \mathbb{C}^{-}$ 相矛盾.

(6) $\Longrightarrow$ (5). 设 (6) 成立. 假定对于某个 $\omega \in \mathbb{R}$ 有 $\mathrm{i}\omega \in \sigma(A - BB^{*})$ , 即存在 $x \in H, x \neq 0$ , 使得 $(A - BB^{*})x = \mathrm{i}\omega x$ . 于是

$$(A x, x) - \| B ^ {*} x \| ^ {2} = \mathrm{i} \omega \| x \| ^ {2}.$$

但 $\operatorname{Re}(Ax, x) = 0$ ，从而 $B^{*}x = 0, Ax = \mathrm{i}\omega x$ 。这与 (6) 矛盾。因此 (5) 成立。

(6) $\Longrightarrow$ (1). 设 (6) 成立, 并设 $\{\mathrm{i}\omega_n \mid n \geqslant 1\}$ 是 $A$ 的本征值序列, $\mathrm{i}\omega_n$ 的重数为 $r_n$ . 设 $\{\varphi_{nj} \mid 1 \leqslant j \leqslant r_n, 1 \leqslant n\}$ 是 $A$ 的相应的规范本征元序列. 那么 $\{\varphi_{nj} \mid 1 \leqslant j \leqslant r_n, 1 \leqslant n\}$ 形成 $H$ 的直交规范基. 从 (6) 可知 $B^*\varphi_{n1}, \cdots, B^*\varphi_{nr_n}$ 对于所有 $n \geqslant 1$ 是线性无关的. 假定对某个 $x \in H$ , 有

$$B ^ {*} R (\lambda ; - A) x = 0, \quad \forall \lambda \neq - \mathrm{i} \omega_ {n}, n \geqslant 1. \tag {10.3.15}$$

把 $x$ 在基 $\{\varphi_{nj}\}$ 上展开

$$x = \sum_ {n = 1} ^ {\infty} \sum_ {j = 1} ^ {r _ {n}} c _ {n j} \varphi_ {n j},$$

代入式 (10.3.15) 得到

$$\sum_ {n = 1} ^ {\infty} \frac {1}{\lambda + \mathrm{i} \omega_ {n}} \sum_ {j = 1} ^ {r _ {n}} c _ {n j} B ^ {*} \varphi_ {n j} = 0, \quad \forall \lambda \neq - \mathrm{i} \omega_ {n}, n \geqslant 1.$$

于是

$$\sum_ {j = 1} ^ {r _ {n}} c _ {n j} B ^ {*} \varphi_ {n j} = 0, \quad \forall n \geqslant 1.$$

但 $B^{*}\varphi_{n1},\dots ,B^{*}\varphi_{nr_{n}}$ 是线性无关的，因此

$$c _ {n j} = 0, \quad n \geqslant 1, 1 \leqslant j \leqslant r _ {n},$$

这意味着 $x = 0$ ，从而 $(A,B)$ 完全近似能控.

(4) $\Longrightarrow$ (3). 设 (4) 成立, 则从上面已经证明的结论可知 (1) $\Longleftrightarrow$ (4), 于是 $(A, B)$ 完全近似能控. 任取一正定对称算子 $K \in \mathcal{L}(U)$ , 显然 $(A, BK^{\frac{1}{2}})$ 也是完全近似能控的. 再利用上面已经证明 (1) 和 (4) 的等价性, 我们得出结论: $T^{A - BK^{\frac{1}{2}}(BK^{\frac{1}{2}})^*}(t) = T^{A - BKB^*}(t)$ 是强稳定的.

最后 $(3) \Longrightarrow (2)$ 是显然的. 证毕.
