不难看出 $\mathcal{A}$ 是 $\mathcal{H}$ 中具有紧豫解式的斜自伴算子，满足定理10.4.3的假设。 $\pmb{\beta}$ 显然是耗散的。注意 $\mathcal{A}$ 的本征值序列为

$$\mathrm{i} \omega_ {n} = \frac {\mathrm{i} n ^ {2} \pi^ {2}}{\ell^ {2}}, \quad n = \pm 1, \pm 2, \dots .$$

注意到

$$\left| \mathrm{i} \frac {n ^ {2} \pi^ {2}}{\ell^ {2}} - \mathrm{i} \frac {(n + 1) ^ {2} \pi^ {2}}{\ell^ {2}} \right| = \frac {| (2 n + 1) \pi^ {2} |}{\ell^ {2}},$$

可知有关 A 的谱间隙条件满足.

$\pmb{A}$ 的相应的规范本征元为

$$
y _ {n} = \frac {\ell^ {\frac {3}{2}}}{n ^ {2} \pi^ {2}} \left[ \begin{array}{c} \sin \left(\frac {n \pi x}{\ell}\right) \\ \mathrm{i} \frac {n ^ {2} \pi^ {2}}{\ell^ {2}} \sin \left(\frac {n \pi x}{\ell}\right) \end{array} \right], \qquad n = \pm 1, \pm 2, \dots .
$$

容易验证有关 B 的假设 (H1) 和 (H2) 成立. 仿照上例, 存在常数 $\delta > 0$ 使得

$$
\begin{array}{l} \left\| \mathcal {B} y _ {n} \right\| ^ {2} \geqslant \int_ {c} ^ {d} b ^ {2} (x) \ell^ {- 1} \sin^ {2} \left(\frac {n \pi x}{\ell}\right) d x \\ \geqslant \frac {b _ {0} ^ {2}}{\ell} \int_ {c} ^ {d} \sin^ {2} \left(\frac {n \pi x}{\ell}\right) d x \geqslant \delta^ {2}, \quad \forall n = \pm 1, \pm 2, \dots . \\ \end{array}
$$

从而 (H3) 满足. 因此依据定理 10.4.3. 一维梁振动系统 (10.4.18) 指数稳定, 而相应的局部分布控制系统

$$
\left\{ \begin{array}{l} \ddot {y} (x, t) + y ^ {\prime \prime \prime \prime} (x, t) + b (x) u (x, t) = 0, \\ y (0, t) = 0 = y (\ell , t), \quad y ^ {\prime \prime} (0, t) = 0 = y ^ {\prime \prime} (\ell , t), \end{array} \right.
$$

则是精确能控的.
