$$
\begin{array}{l} T (t) = \frac {1}{2 \pi \mathrm{i}} \int_ {t \Gamma_ {\epsilon , \theta}} \mathrm{e} ^ {\mu} R (\mu / t; A) \mathrm{d} \mu / t = \frac {1}{2 \pi \mathrm{i}} \int_ {\Gamma_ {\epsilon , \theta}} \mathrm{e} ^ {\mu} R (\mu / t; A) \mathrm{d} \mu / t \\ = \frac {1}{2 \pi \mathrm{i}} \left[ \int_ {\varepsilon} ^ {\infty} \exp (r \mathrm{e} ^ {\mathrm{i} \theta}) R (r \mathrm{e} ^ {\mathrm{i} \theta} / t; A) \mathrm{e} ^ {\mathrm{i} \theta} \mathrm{d} r / t \right. \\ - \int_ {\epsilon} ^ {\infty} \exp (r e ^ {- i \theta}) R (r e ^ {i \theta} / t; A) e ^ {- i \theta} d r / t \\ \left. + \int_ {- \theta} ^ {\theta} \exp (\varepsilon \mathrm{e} ^ {\mathrm{i} \varphi}) R (\varepsilon \mathrm{e} ^ {\mathrm{i} \varphi} / t; A) i \varepsilon \mathrm{e} ^ {\mathrm{i} \varphi} \mathrm{d} \varphi / t \right]. \\ \end{array}
$$

因此

$$\| T (t) \| \leqslant \frac {M}{2 \pi} \left(2 \int_ {\varepsilon} ^ {\infty} \mathrm{e} ^ {r \cos \theta} \frac {\mathrm{d} r}{r} + \int_ {- \theta} ^ {\theta} \mathrm{e} ^ {\epsilon \cos \varphi} \mathrm{d} \varphi\right).$$

类似地，我们有

$$\left\| T ^ {\prime} (t) \right\| \leqslant \frac {M}{2 \pi t} \left(2 \int_ {\varepsilon} ^ {\infty} \mathrm{e} ^ {r \cos \theta} \mathrm{d} r + \varepsilon \int_ {- \theta} ^ {\theta} \mathrm{e} ^ {\varepsilon \cos \varphi} \mathrm{d} \varphi\right).$$

让 $\varepsilon \to 0$ , 得到式 (5.3.48) 和式 (5.3.49), $M_2 = M / (\pi |\cos \theta |)$ .

(2) 现在我们证明 $T(t)$ 的强连续性. 由于 $\| T'(t) \| \leqslant M_1, \forall t \geqslant 0$ , 只需证明 $\lim_{t \downarrow 0} T(t)x = x, \forall x \in \mathcal{D}(A)$ . 设 $x \in \mathcal{D}(A)$ , 并令 $y = x - Ax$ . 那么 $x = R(1; A)y$ , 并且

$$
\begin{array}{l} T (t) x = T (t) R (1; A) y = \frac {1}{2 \pi \mathrm{i}} \int_ {\Gamma_ {s, \theta}} \mathrm{e} ^ {\lambda t} R (\lambda ; A) R (1; A) y \mathrm{d} \lambda \\ = \frac {1}{2 \pi \mathrm{i}} \int_ {\Gamma_ {\epsilon , \theta}} \mathrm{e} ^ {\lambda t} R (\lambda ; A) y \frac {\mathrm{d} \lambda}{1 - \lambda} - \frac {1}{2 \pi \mathrm{i}} \int_ {\Gamma_ {\epsilon , \theta}} \mathrm{e} ^ {\lambda t} R (1; A) y \frac {\mathrm{d} \lambda}{1 - \lambda} \\ = \frac {1}{2 \pi \mathrm{i}} \int_ {\Gamma_ {\varepsilon , 0}} \mathrm{e} ^ {\lambda t} R (\lambda ; A) y \frac {\mathrm{d} \lambda}{1 - \lambda}. \\ \end{array}
$$

让 $t \to 0$ , 我们得到

$$\lim _ {t \downarrow 0} T (t) x = \frac {1}{2 \pi \mathrm{i}} \int_ {\Gamma_ {\varepsilon , \theta}} R (\lambda ; A) y \frac {\mathrm{d} \lambda}{1 - \lambda} = R (1; A) y = x.$$
