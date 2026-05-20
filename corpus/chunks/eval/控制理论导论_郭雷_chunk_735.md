$$
\begin{array}{l} \langle T _ {1} (t) x, y \rangle = \frac {1}{2 \pi \mathrm{i}} \lim _ {\tau \rightarrow \infty} \int_ {\sigma_ {1} - \mathrm{i} \tau} ^ {\sigma_ {1} + \mathrm{i} \tau} \mathrm{e} ^ {\lambda t} \langle R (\lambda ; A _ {1}) x, y \rangle \mathrm{d} \lambda \\ = \frac {1}{2 \pi \mathrm{i}} \lim _ {\tau \rightarrow \infty} \left[ \right. \frac {\mathrm{e} ^ {\lambda t}}{t} \langle R (\lambda ; A _ {1}) x, y \rangle \left. \right| _ {\sigma_ {1} - \mathrm{i} \tau} ^ {\sigma_ {1} + \mathrm{i} \tau} \\ \left. + \int_ {\sigma_ {1} - \mathrm{i} \tau} ^ {\sigma_ {1} + \mathrm{i} \tau} \frac {\mathrm{e} ^ {\lambda t}}{t} \langle R (\lambda ; A _ {1}) ^ {2} x, y \rangle \mathrm{d} \lambda \right] \\ = \frac {1}{2 \pi \mathrm{i}} \lim _ {\tau \rightarrow \infty} \int_ {\sigma_ {1} - \mathrm{i} \tau} ^ {\sigma_ {1} + \mathrm{i} \tau} \frac {\mathrm{e} ^ {\lambda t}}{t} \langle R (\lambda ; A _ {1}) ^ {2} x, y \rangle \mathrm{d} \lambda . \\ \end{array}
$$

记 $M_{1} = \sup \left\{\| R(\lambda; A_{1}) \| \mid \operatorname{Re} \lambda \geqslant -\frac{\varepsilon}{2}\right\}$ . 再取 $\sigma_{2} > \sigma_{1}$ . 对任意固定的 $t \geqslant 1$ , $\mathrm{e}^{\lambda t} \langle R(\lambda; A_{1})^{2} x, y \rangle$ 是区域 $\left\{\lambda \in \mathbb{C} \mid -\frac{\varepsilon}{2} < \operatorname{Re} \lambda < \sigma_{2}\right\}$ 中的解析函数，并且依引理 10.1.2，当 $\tau \to \infty$ 时，

$$\sup \left\{\left| \mathrm{e} ^ {(\sigma + \mathrm{i} \tau) t} \langle R (\sigma + \mathrm{i} \tau ; A _ {1}) ^ {2} x, y \rangle \right| \Big | - \frac {\varepsilon}{2} \leqslant \sigma \leqslant \sigma_ {2} \right\}\leqslant M _ {1} \| y \| \mathrm{e} ^ {\sigma_ {2} t} \sup \left\{\| R (\sigma + \mathrm{i} \tau ; A _ {1}) x \| \mid - \frac {\varepsilon}{2} \leqslant \sigma \leqslant \sigma_ {2} \right\}\rightarrow 0.$$

于是从复变函数的回道积分理论得到

$$\langle T _ {1} (t) x, y \rangle = \frac {1}{2 \pi \mathrm{i}} \lim _ {\tau \rightarrow \infty} \int_ {- \mathrm{i} \tau} ^ {+ \mathrm{i} \tau} \frac {\mathrm{e} ^ {\lambda t}}{t} \langle R (\lambda ; A _ {1}) ^ {2} x, y \rangle \mathrm{d} \lambda .$$

由于 $|\langle R(\lambda; A_1)^2 x, y \rangle| \leqslant \|R(\lambda; A_1)x\| \|R(\overline{\lambda}; A_1^*)y\|$ ，我们看到上述积分是绝对收敛的。于是对于 $t \geqslant 1$ ，有

$$\left| \langle T _ {1} (t) x, y \rangle \right| \leqslant \mu (x, y) / t < + \infty , \quad \forall x, y \in H,$$
