$$\left\| x _ {k + r} - x _ {k} \right\| \leqslant \left\| x _ {k + r} - x _ {k + r - 1} \right\| + \left\| x _ {k + r - 1} - x _ {k + r - 2} \right\| + \dots + \left\| x _ {k + 1} - x _ {k} \right\|\leqslant \rho^ {k - 1} \sum_ {i = 0} ^ {\infty} \rho^ {i} \| x _ {2} - x _ {1} \| = \frac {\rho^ {k - 1}}{1 - \rho} \| x _ {2} - x _ {1} \|$$

在 $k$ 趋于无穷时，上式右边趋于零，因此，该序列是Cauchy序列。由于 $\mathcal{X}$ 是Banach空间，故有

$$x _ {k} \to x ^ {*} \in \mathcal {X} \quad {\text {当}} k \to \infty$$

进一步,由于 S 是闭集,故有 $x^{*} \in S$ 。现在要证明 $x^{*} = T(x^{*})$ 。对于任意 $x_{k} = T(x_{k-1})$ ,我们有

$$\| x ^ {*} - T (x ^ {*}) \| \leqslant \| x ^ {*} - x _ {k} \| + \| x _ {k} - T (x ^ {*}) \| \leqslant \| x ^ {*} - x _ {k} \| + \rho \| x _ {k - 1} - x ^ {*} \|$$

选择足够大的 $k$ ，可使上面不等式的右边为任意小，因此 $\| x^{*} - T(x^{*})\| = 0$ ，即 $x^{*} = T(x^{*})$ 。最后要证明的是 $x^{*}$ 是 $S$ 上映射 $T$ 的唯一不动点，设 $x^{*}$ 和 $y^{*}$ 都是不动点，那么

$$\| x ^ {*} - y ^ {*} \| = \| T (x ^ {*}) - T (y ^ {*}) \| \leqslant \rho \| x ^ {*} - y ^ {*} \|$$

由于 $\rho < 1$ ，因此有 $x^{*} = y^{*}$ 。证毕。

□
