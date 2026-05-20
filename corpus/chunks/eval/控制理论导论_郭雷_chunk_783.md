$$\sum_ {m = 1} ^ {\infty} \sum_ {j = 1} ^ {r _ {m}} | \omega_ {m} - \nu_ {n} | ^ {2} | \langle z _ {n}, \varphi_ {m j} \rangle | ^ {2} \leqslant \varepsilon , \quad \forall n \geqslant N _ {\varepsilon}. \tag {10.4.15}$$

由于 $z_{n}$ 是单位元，故

$$\sum_ {m = 1} ^ {\infty} \sum_ {j = 1} ^ {r _ {m}} | \langle z _ {n}, \varphi_ {m j} \rangle | ^ {2} = 1.$$

根据 $\mathcal{A}$ 的本征值的间隙条件假设，对于每一 $n$ ，存在某自然数 $p(n)$ 使得

$$\left| \omega_ {k} - \nu_ {n} \right| ^ {2} \geqslant \left(\frac {\gamma}{2}\right) ^ {2}, \quad \forall k \geqslant 1, k \neq p (n).$$

这样从式 (10.4.15), 我们有

$$
\frac {\gamma^ {2}}{4} \sum_ {\substack {k = 1 \\ k \neq p (n)}} ^ {\infty} \sum_ {j = 1} ^ {r _ {k}} | \langle z _ {n}, \varphi_ {k j} \rangle | ^ {2} + | \omega_ {p (n)} - \nu_ {n} | ^ {2} \sum_ {j = 1} ^ {r _ {p (n)}} | \langle z _ {n}, \varphi_ {p (n) j} \rangle | ^ {2} \leqslant \varepsilon .
$$

因此

$$
\sum_ {\substack {m = 1 \\ m \neq p (n)}} ^ {\infty} \sum_ {j = 1} ^ {r _ {m}} | \langle z _ {n}, \varphi_ {m j} \rangle | ^ {2} \leqslant \frac {4 \varepsilon}{\gamma^ {2}}.
$$

但 $z_{n}$ 是单位元，故

$$\sum_ {j = 1} ^ {r _ {p (n)}} | \langle z _ {n}, \varphi_ {p (n) j} \rangle | ^ {2} \geqslant 1 - \frac {4 \varepsilon}{\gamma^ {2}}.$$

定义

$$\psi_ {n} = \sum_ {j = 1} ^ {r _ {p (n)}} \left\langle z _ {n}, \varphi_ {p (n) j} \right\rangle \varphi_ {p (n) j}. \quad \left(\| \psi_ {n} \| ^ {2} \geqslant 1 - \frac {4 \varepsilon}{\gamma^ {2}}\right),$$

并令 $\hat{\psi}_n \stackrel{\mathrm{def}}{=} \psi_n / \| \psi_n \|$ . 于是 $\hat{\psi}_n$ 是 $A$ 的单位本征元.

利用式 (10.4.13), 当 $\varepsilon$ 充分小时, 我们有

$$
\begin{array}{l} 0 = \lim _ {n \rightarrow \infty} \| \mathcal {B} z _ {n} \| = \lim _ {n \rightarrow \infty} \| \mathcal {B} \psi_ {n} + \mathcal {B} (z _ {n} - \psi_ {n}) \| \\ \geqslant \lim _ {n \rightarrow \infty} [ \| \mathcal {B} \psi_ {n} \| - \| \mathcal {B} z _ {n} - \mathcal {B} \psi_ {n} \| ] \\ = \lim _ {n \rightarrow \infty} [ \| \psi_ {n} \| \| \widehat {\mathcal {B} \psi_ {n}} \| - \| \mathcal {B} z _ {n} - \mathcal {B} \psi_ {n} \| ] \\ \geqslant \lim _ {n \rightarrow \infty} \left[\left(1 - \frac {4 \varepsilon}{\gamma^ {2}}\right) ^ {\frac {1}{2}} \delta - \| \mathcal {B} \| \| z _ {n} - \psi_ {n} \| \right] \\ \geqslant \left[ \left(1 - \frac {4 \varepsilon}{\gamma^ {2}}\right) ^ {\frac {1}{2}} \delta - \| \mathcal {B} \| \left(\frac {4 \varepsilon}{\gamma^ {2}}\right) ^ {\frac {1}{2}} \right] \\ > 0. \\ \end{array}
$$

由此导出矛盾．证毕.

注 在许多应用中，B实际上满足更强的条件
