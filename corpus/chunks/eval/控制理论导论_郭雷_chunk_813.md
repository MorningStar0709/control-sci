于是根据 Gronwall 不等式，我们得到 $f(t) \equiv 0$ ，从而 (2) 成立.

从式 (10.6.4) 中级数在 $0 \leqslant s \leqslant t \leqslant t_1$ 上收敛直接可得性质 (3). 最后积分方程 (10.6.1) 解的唯一性则直接由 Gronwall 不等式推出 (见文献 [5]). 证毕.

定理10.6.2 在定理10.6.1的假设下，设 $S(t,s)$ 是式(10.6.4)定义的温和发展算子．那么当 $\pmb {x}\in \mathcal{D}(A)$ 时我们有

$$\int_ {s} ^ {t} S (t, \xi) (A + B (\xi)) x \mathrm{d} \xi = S (t, s) x - x, \tag {10.6.5}\frac {\partial}{\partial s} S (t, s) x = - S (t, s) (A + B (s)) x, \quad \text { a.e. } \quad 0 \leqslant s \leqslant t < \infty . \tag {10.6.6}$$

证明 考虑另一个迭代程序：对于 $0 \leqslant s \leqslant t < \infty$ 和 $x \in X$

$$\widetilde {S} _ {0} (t, s) \boldsymbol {x} = T (t - s) \boldsymbol {x},\widetilde {S} _ {n} (t, s) x = \int_ {s} ^ {t} \widetilde {S} _ {n - 1} (t, \xi) B (\xi) T (\xi - s) x d \xi , \quad n \geqslant 1.$$

如同在定理10.6.1中那样，我们可以证明

$$\widetilde {S} (t, s) = \sum_ {n = 0} ^ {\infty} \widetilde {S} _ {n} (t, s)$$

是如下积分方程：

$$\widetilde {S} (t, s) x = T (t - s) x + \int_ {s} ^ {t} \widetilde {S} (t, \xi) B (\xi) T (\xi - s) x \mathrm{d} \xi , \quad 0 \leqslant s \leqslant t < \infty \tag {10.6.7}$$

的唯一解. 通过归纳法容易证明 $\widetilde{S}_n(t, s) = S_n(t, s), \forall n \geqslant 0$ . 于是

$$\widetilde {S} (t, s) = S (t, s).$$

因此我们有

$$S (t, \xi) A x = T (t - \xi) A x + \int_ {\xi} ^ {t} S (t, \eta) B (\eta) T (\eta - \xi) A x \mathrm{d} \eta , \quad \forall x \in \mathcal {D} (A). \tag {10.6.8}$$

对式 (10.6.8) 两端相对 $\xi$ 从 $s$ 到 $t$ 积分，并利用Fubini定理，可得

$$
\begin{array}{l} \int_ {s} ^ {t} S (t, \xi) A x \mathrm{d} \xi = \int_ {s} ^ {t} T (t - \xi) A x \mathrm{d} \xi + \int_ {s} ^ {t} \mathrm{d} \xi \int_ {\xi} ^ {t} S (t, \eta) B (\eta) T (\eta - \xi) A x \mathrm{d} \eta \\ = \int_ {s} ^ {t} T (t - \xi) A x \mathrm{d} \xi + \int_ {s} ^ {t} \mathrm{d} \eta \int_ {s} ^ {\eta} S (t, \eta) B (\eta) T ^ {\prime} (\eta - \xi) A x \mathrm{d} \xi \\ = T (t - s) x - x + \int_ {s} ^ {t} S (t, \eta) B (\eta) (T (\eta - s) - I) x d \eta . \\ \end{array}
$$

于是式 (10.6.5) 从式 (10.6.8) 推出。最后由式 (10.6.5) 相对 $t$ 作微商直接可得式 (10.6.6). 证毕。
