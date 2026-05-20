其中 $\mu(x, y)$ 是一依赖于 $x$ 和 $y$ 的常数。依据有界线性算子的一致有界性原理，存在常数 $M_2$ 使得 $\|T_1(t)\| \leqslant M_2, \forall t \geqslant 1$ 。如果我们令 $M_3 = \sup \left\{\|T_1(t)\| \mid 0 \leqslant t \leqslant 1\right\}$ 和 $M = \max \{M_3, M_2\}$ ，则

$$\| T _ {1} (t) \| \leqslant M, \quad \forall t \geqslant 0.$$

证毕.

定理10.1.5 设 $T(t)$ 是Hilbert空间 $H$ 上闭稠定线性算子 $A$ 生成的 $C_0$ 半群．那么 $T(t)$ 指数稳定当且仅当 $\mathbb{C}^{+}\stackrel {\mathrm{def}}{=}\{\lambda \in \mathbb{C}\mid \operatorname {Re}\lambda \geqslant 0\} \subset \rho (A)$ ，并且

$$\mu \stackrel {\text { def }} {=} \sup \left\{\| R (\lambda ; A) \| \mid \operatorname{Re} \lambda \geqslant 0 \right\} < + \infty .$$

证明 必要性是显然的, 我们只需证明充分性. 设 $\lambda = \sigma + \mathrm{i}\tau$ , 且 $\sigma \in \left[-\frac{2}{3}\mu, 0\right]$ , 则 $\| \sigma R(\mathrm{i}\tau; A) \| \leqslant \frac{2}{3}$ . 于是

$$\lambda = \sigma + \mathrm{i} \tau \in \rho (A), \quad \forall \sigma \in \left[ - \frac {2 \mu}{3}, 0 \right], \forall \tau \in \mathbb {R},$$

并且

$$
\begin{array}{l} \| R (\lambda ; A) \| = \left\| R (\mathrm{i} \tau ; A) [ I + \sigma R (\mathrm{i} \tau ; A) ] ^ {- 1} \right\| \\ \leqslant \left\| R (\mathrm{i} \tau ; A) \right\| \left\| [ I + \sigma R (\mathrm{i} \tau ; A) ] ^ {- 1} \right\| \leqslant 3 \mu . \\ \end{array}
$$

记 $A_{1} = A + \left(\frac{\mu}{2}\right)I$ ，则我们有 $s(A_{1}) < -\frac{\mu}{3}$ ，并且

$$\sup \left\{\| R (\lambda ; A _ {1}) \| \mid \operatorname{Re} \lambda \geqslant - \frac {\mu}{3} \right\} < + \infty .$$

应用证明定理 10.1.4 的方法，可知存在常数 M > 0 使得 $\|T_{1}(t)\| \leqslant M, \forall t \geqslant 1$ ，其中 $T_{1}(t)$ 是由 $A_{1}$ 生成的 $C_{0}$ 半群。因此

$$\| T (t) \| \leqslant M \mathrm{e} ^ {- (\mu / 3) t}, \quad \forall t \geqslant 0,$$

即 $T(t)$ 指数稳定，证毕.

定理10.1.6 设 $T(t)$ 是Hilbert空间 $H$ 上闭稠定线性算子 $A$ 生成的 $C_0$ 半群．那么 $T(t)$ 指数稳定当且仅当

(1) $\{\lambda \in \mathbb{C} \mid \operatorname{Re} \lambda \geqslant 0\} \subset \rho(A)$ ;   
(2) $\sup \left\{\| R(\sigma + i\tau; A) \| \mid \tau \in \mathbb{R}\right\} < \infty, \forall \sigma > 0.$

此外，若 $T(t)$ 是一致有界的，即存在正常数 $M$ 使得 $\| T(t)\| \leqslant M, \forall t\geqslant 0,$ 则条件(2)可用如下更简单的条件(3)代替：

(3) $\sup \left\{\| R(\mathrm{i}\tau; A) \| \mid \tau \in \mathbb{R} \right\} < \infty.$

证明 必要性是显然的. 根据 Hille-Yosida 定理和定理 10.1.5, 为证充分性, 我们只需证明

$$\sup \left\{\| R (\sigma + \mathrm{i} \tau ; A) \| \mid 0 \leqslant \sigma \leqslant a, \tau \in \mathbb {R} \right\} < \infty ,$$
