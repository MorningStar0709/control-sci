$$\Gamma_ {1}: \operatorname{Re} \lambda = 2 a - b \log (- \operatorname{Im} \lambda), \quad - \infty < \operatorname{Im} \lambda \leqslant - L;\Gamma_ {2}: \operatorname{Re} \lambda = \zeta , - L \leqslant \operatorname{Im} \lambda \leqslant L;\Gamma_ {3}: \operatorname{Re} \lambda = 2 a - b \log (\operatorname{Im} \lambda), \quad L \leqslant \operatorname{Im} \lambda < \infty ,$$

而 $L = \mathrm{e}^{(2a - \zeta) / b}$ . $\Gamma$ 的定向使得 $\operatorname{Im} \lambda$ 沿着 $\Gamma$ 的正向是增加的. 从式 (10.1.9) 和式 (10.1.10) 可以得到

$$\| T (t) \| \leqslant c _ {1} \mathrm{e} ^ {\zeta t} + c _ {2} \mathrm{e} ^ {2 a t} \int_ {L} ^ {\infty} | \tau | ^ {1 - b t} \mathrm{d} \tau , \quad t > \frac {3}{b}, \tag {10.1.11}$$

其中 $c_{1}$ 是一依赖于 $\Gamma_{2}$ 的常数， $c_{2}$ 是依赖于 $\Gamma_{1}$ 和 $\Gamma_{3}$ 的常数。注意当 $t > \frac{3}{b}$ 时有 $bt - 2 \geqslant 1$ ，故从式 (10.1.11) 可知存在常数 $c_{3} > 0$ 使得

$$\| T (t) \| \leqslant c _ {3} \mathrm{e} ^ {\zeta t}, \quad t > \frac {3}{b}.$$

这样我们证明了存在常数 $c(\zeta)$ , 使得 $\|T(t)\| \leqslant c(\zeta)e^{\zeta t}, t \geqslant 0$ , 从而依据 $\omega(A)$ 的定义, 我们有 $\zeta \geqslant \omega(A)$ , 矛盾. 证毕.

推论10.1.1 设 $T(t)$ 是Banach空间 $X$ 上闭稠定线性算子 $A$ 生成的 $C_0$ 半群，如果 $A$ 有界或 $T(t)$ 解析，则谱确定增长假设成立.

在 Hilbert 空间中谱确定增长假设可以得到很好的刻划，见文献 [21], [22] 等. 我们先证明如下两个引理：

引理10.1.2 设 $T(t)$ 是Hilbert空间 $H$ 上闭稠定线性算子 $A$ 生成的 $C_0$ 半群．那么对于任意 $x \in H$ 和 $\sigma > \omega(A)$ ，有

$$\| R (\sigma + \mathrm{i} \cdot ; A) x \| \in L ^ {2} (\mathbb {R}), \quad \| R (\sigma - \mathrm{i} \cdot ; A ^ {*}) x \| \in L ^ {2} (\mathbb {R}),\lim _ {\tau \rightarrow \infty} \| R (\sigma + i \tau ; A) x \| = \lim _ {\tau \rightarrow \infty} \| R (\sigma - i \tau ; A ^ {*}) x \| = 0.$$

证明 由于对称性, 我们只需证明与 $\|R(\sigma + i\tau; A)x\|$ 有关的结论. 对于 $x \in H$ , 当 $\sigma > s(A)$ 时, 有
