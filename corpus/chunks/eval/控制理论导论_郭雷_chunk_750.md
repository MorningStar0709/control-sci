$$\| \mathcal {B} ^ {*} T ^ {*} (\cdot) w \| _ {L ^ {2} (0, t _ {f}; H)} ^ {2} = \sum_ {n = 1} ^ {\infty} \left[ \alpha_ {n} \lambda_ {n} (y, \varphi_ {n}) ^ {2} + \beta_ {n} (z, \varphi_ {n}) ^ {2} + \gamma_ {n} (y, \varphi_ {n}) (z, \varphi_ {n}) \right],$$

其中 $w = [y,z]^{\mathrm{T}}$ ，并且

$$\alpha_ {n} = \frac {t _ {f}}{2} - \frac {\sin 2 \sqrt {\lambda_ {n}} t _ {f}}{4 \sqrt {\lambda_ {n}}}, \beta_ {n} = \frac {t _ {f}}{2} + \frac {\sin 2 \sqrt {\lambda_ {n}} t _ {f}}{4 \sqrt {\lambda_ {n}}}, \gamma_ {n} = \frac {1}{2} (1 - \cos 2 \sqrt {\lambda_ {n}} t _ {f}).$$

但对于每一固定的 $n \geqslant 1$ ，由于

$$t _ {f} > \left| \frac {\sin \sqrt {\lambda_ {n}} t _ {f}}{\sqrt {\lambda_ {n}}} \right|,$$

二次型 $\alpha_{n}\xi^{2} + \beta_{n}\eta^{2} + \frac{\gamma_{n}}{\sqrt{\lambda_{n}}}\xi \eta$ 是正定的，并且相应的系数矩阵的最小本征值是 $\frac{t_f}{2} -\left|\frac{\sin\sqrt{\lambda_n}t_f}{2\sqrt{\lambda_n}}\right|$ ，从而

$$
\begin{array}{l} \alpha_ {n} \lambda_ {n} | (y, \varphi_ {n}) | ^ {2} + \beta_ {n} | (z, \varphi_ {n}) | ^ {2} + \gamma_ {n} (y, \varphi_ {n}) (z, \varphi_ {n}) \\ \geqslant \left(\frac {t _ {f}}{2} - \left| \frac {\sin \sqrt {\lambda_ {n}} t _ {f}}{2 \sqrt {\lambda_ {n}}} \right|\right) \left(\lambda_ {n} | (y, \varphi_ {n}) | ^ {2} + | (z, \varphi_ {n}) | ^ {2}\right). \\ \end{array}
$$

如果我们令

$$\delta = \inf _ {n \geqslant 1} \left(\frac {t _ {f}}{2} - \left| \frac {\sin \sqrt {\lambda_ {n}} t _ {f}}{2 \sqrt {\lambda_ {n}}} \right|\right),$$

则显然 $\delta > 0$ 并且

$$\left\| \mathcal {B} ^ {*} T ^ {*} (\cdot) w \right\| _ {L ^ {2} (0, t _ {f}; H)} ^ {2} \geqslant \delta \sum_ {n = 1} ^ {\infty} \left(\lambda_ {n} | (y, \varphi_ {n}) | ^ {2} + | (z, \varphi_ {n}) | ^ {2}\right).$$

然而

$$\sum_ {n = 1} ^ {\infty} \left(\lambda_ {n} | (y, \varphi_ {n}) | ^ {2} + | (z, \varphi_ {n}) | ^ {2}\right) = \| w \| ^ {2},$$

于是依据定理 10.2.1, 系统 (10.2.13) 在任意有穷区间 $[0, t_f]$ 上精确能控.

例 10.2.2 考虑如下线性控制系统:

$$\frac {\mathrm{d} x}{\mathrm{d} t} = - A x (t) + u (t), \tag {10.2.14}$$

其中 $A$ 与上例中的相同. $-A$ 生成的 $H$ 中的 $C_0$ 半群为

$$T (t) x = \sum_ {n = 1} ^ {\infty} \mathrm{e} ^ {- \lambda_ {n} t} (x, \varphi_ {n}) _ {H} \varphi_ {n}, \quad \forall x \in H.$$

这里 $U = H, B = I$ 并且 $B^{*} = I$ , 因此

$$\| B ^ {*} T ^ {*} (\cdot) x \| _ {L ^ {2} (0, t _ {f}; H)} ^ {2} = \sum_ {n = 1} ^ {\infty} \frac {1 - e ^ {- 2 \lambda_ {n} t _ {f}}}{2 \lambda_ {n}} | (x, \varphi_ {n}) | ^ {2}, \quad \forall x \in H.$$

由于

$$\frac {1 - \mathrm{e} ^ {- 2 \lambda_ {n} t _ {f}}}{2 \lambda_ {n} t _ {f}} \geqslant \mathrm{e} ^ {- 2 \lambda_ {n} t _ {f}},$$

我们有
