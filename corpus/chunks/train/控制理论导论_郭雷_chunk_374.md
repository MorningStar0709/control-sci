(3) 设 $x \in \mathcal{D}(A)$ , $\operatorname{Re} \lambda > \omega$ 并且 $a > 0$ , 则根据 $A$ 的闭性和 $T(t)x \in \mathcal{D}(A), \forall t \geqslant 0$ , 我们有

$$
\begin{array}{l} A \int_ {0} ^ {a} \mathrm{e} ^ {- \lambda t} T (t) x \mathrm{d} t = \int_ {0} ^ {a} \mathrm{e} ^ {- \lambda t} A T (t) x \mathrm{d} t = \int_ {0} ^ {a} \mathrm{e} ^ {- \lambda t} \frac {\mathrm{d}}{\mathrm{d} t} (T (t) x) \mathrm{d} t \\ = \mathrm{e} ^ {- \lambda a} T (a) x - x + \lambda \int_ {0} ^ {a} \mathrm{e} ^ {- \lambda t} T (t) x \mathrm{d} t. \\ \end{array}
$$

但是

$$\lim _ {a \rightarrow \infty} \left[ e ^ {- \lambda a} T (a) x - x + \lambda \int_ {0} ^ {a} e ^ {- \lambda t} T (t) x d t \right] = - x + \lambda \int_ {0} ^ {\infty} e ^ {- \lambda t} T (t) x d t,$$

因此从 $A$ 的闭性和控制收敛定理推出

$$\int_ {0} ^ {\infty} \mathrm{e} ^ {- \lambda t} T (t) x \mathrm{d} t \in \mathcal {D} (A)$$

和

$$A \int_ {0} ^ {\infty} \mathrm{e} ^ {- \lambda t} T (t) x \mathrm{d} t = - x + \lambda \int_ {0} ^ {\infty} \mathrm{e} ^ {- \lambda t} T (t) x \mathrm{d} t.$$

令 $R(\lambda) = \int_{0}^{\infty}\mathrm{e}^{-\lambda t}T(t)\mathrm{d}t.$ 显然当 $\operatorname {Re}\lambda >\omega$ 时， $R(\lambda)$ 是一有界线性算子．于是

$$(\lambda I - A) R (\lambda) x = x, \quad \forall x \in \mathcal {D} (A).$$

从 $A$ 的闭性和 $\mathcal{D}(A)$ 在 $X$ 中的稠密性可以推出，上述公式对于所有 $x \in X$ 成立。另一方面， $\forall x \in \mathcal{D}(A)$ ，

$$
\begin{array}{l} R (\lambda) A x = \int_ {0} ^ {\infty} \mathrm{e} ^ {- \lambda t} T (t) A x \mathrm{d} t = \int_ {0} ^ {\infty} \mathrm{e} ^ {- \lambda t} \frac {\mathrm{d}}{\mathrm{d} t} (T (t) x) \mathrm{d} t \\ = - x + \lambda \int_ {0} ^ {\infty} \mathrm{e} ^ {- \lambda t} T (t) x \mathrm{d} t = - x + \lambda R (\lambda) x, \\ \end{array}
$$

即

$$R (\lambda) (\lambda I - A) x = x, \quad \forall x \in \mathcal {D} (A).$$

于是 $\lambda \in \rho(A)$ , 并且 $R(\lambda; A) = R(\lambda)$ .

(4) 最后证明式 (5.3.8). 注意 $R(\lambda; A)$ 作为 $\lambda$ 的函数在半平面 $\{\operatorname{Re} \lambda > \omega\}$ 中是解析的，于是对于任意自然数 $n$ ，有

$$
\begin{array}{l} R (\lambda ; A) ^ {n} x = \frac {(- 1) ^ {n - 1}}{(n - 1) !} \frac {\mathrm{d} ^ {n - 1}}{\mathrm{d} \lambda^ {n - 1}} R (\lambda ; A) x \\ = \int_ {0} ^ {\infty} \frac {t ^ {n - 1}}{(n - 1) !} \mathrm{e} ^ {- \lambda t} T (t) x \mathrm{d} t, \quad \forall x \in X. \\ \end{array}
$$

因此

$$\| R (\lambda ; A) ^ {n} \| \leqslant \frac {M}{(n - 1) !} \int_ {0} ^ {\infty} t ^ {n - 1} \mathrm{e} ^ {- (\operatorname{Re} \lambda - \omega) t} \mathrm{d} t = \frac {M}{(\operatorname{Re} \lambda - \omega) ^ {n}}.$$

证毕.
