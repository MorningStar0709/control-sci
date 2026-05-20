$$M \stackrel {\mathrm{def}} {=} \sup \left\{\| R (\lambda ; A) \| \mid \operatorname{Re} \lambda \geqslant s _ {1} \right\} < + \infty ,$$

则对于所有 $x \in H$ , 当 $t \to \infty$ 时,

$$\| R (\sigma + \mathrm{i} \tau ; A) x \| \rightarrow 0, \quad \forall \sigma \geqslant s _ {1},$$

并且对任意 $s_2 > s_1$ ，上述收敛对于 $\sigma \in [s_1, s_2]$ 是一致的。

证明 取 $s_3 > \max \{s_2, \omega_0\}$ , 其中 $\omega_0 = \omega(A)$ . 于是依引理 10.1.2, 当 $\tau \to \infty$ 时, $\|R(s_3 + i\tau; A)x\| \to 0$ . 对于 $\sigma \in [s_1, s_2]$ , 应用豫解恒等式 (5.2.1), 有

$$\left\| R (\sigma + \mathrm{i} \tau ; A) x \right\| = \left\| R \left(s _ {3} + \mathrm{i} \tau ; A\right) x + \left(s _ {3} - \sigma\right) R \left(s _ {3} + \mathrm{i} \tau ; A\right) R (\sigma + \mathrm{i} \tau ; A) x \right\|\leqslant (1 + | s _ {3} - \sigma | M) \| R (s _ {3} + \mathrm{i} \tau ; A) x \|,$$

由此推出

$$\lim _ {\tau \rightarrow \infty} \| R (\sigma + \mathrm{i} \tau ; A) x \| = 0,$$

并且上述收敛对于 $\sigma \in [s_1, s_2]$ 是一致的。证毕。

定理10.1.4 设 $T(t)$ 是Hilbert空间 $H$ 上闭稠定线性算子 $A$ 生成的 $C_0$ 半群．那么 $s(A) = \omega (A)$ （即谱确定增长假设成立）当且仅当对任意 $\sigma > s(A)$

$$\sup \left\{\| R (\lambda ; A) \| \mid \operatorname{Re} \lambda \geqslant \sigma \right\} < + \infty . \tag {10.1.12}$$

证明 我们只需证明充分性. 为此我们又只需证明在假设 (10.1.12) 之下, 对于任意 $\sigma > s(A)$ , 必存在 $M_{\sigma} \geqslant 1$ 使得

$$\| T (t) \| \leqslant M _ {\sigma} \mathrm{e} ^ {\sigma t}, \quad \forall t \geqslant 0.$$

令 $A_{1} = A - \sigma I$ ，容易看出 $T_{1}(t)\stackrel {\mathrm{def}}{=}\mathrm{e}^{-\sigma t}T(t)$ 的生成算子正好是 $A_{1}$ ，并且 $s(A_{1}) = s(A) - \sigma$ ；此外从假设(10.1.12)，并取 $\varepsilon$ 满足 $\sigma -s(A) > \varepsilon >0,$ 则得

$$\sup \left\{\| R (\lambda ; A _ {1}) \| \mid \operatorname{Re} \lambda \geqslant - \varepsilon \right\} < + \infty .$$

我们要证明存在 $M \geqslant 1$ 使得

$$\| T _ {1} (t) \| \leqslant M, \quad \forall t \geqslant 0.$$

由 $C_0$ 半群的Laplace变换公式，有

$$\langle R (\lambda ; A _ {1}) x, y \rangle = \int_ {0} ^ {\infty} \mathrm{e} ^ {- \lambda t} \langle T _ {1} (t) x, y \rangle \mathrm{d} t, \quad \forall \operatorname{Re} \lambda > \omega (A _ {1}).$$

取 $\sigma_{1} > \max \{0, \omega(A_{1})\}$ , 根据 Laplace 变换的反演公式, 对于任意 $x, y \in H$ 和 $t > 0$ , 我们有
