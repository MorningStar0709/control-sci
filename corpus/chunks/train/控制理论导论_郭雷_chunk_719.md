$$
\begin{array}{l} P \left(f _ {t} \left(\eta_ {t}\right) \geqslant \frac {\delta_ {t}}{2} \mid \mathcal {G} _ {t - 1}\right) = \int_ {x \in D} I \left(f _ {t} (x) \geqslant \frac {\delta_ {t}}{2}\right) \mu (\mathrm{d} x) \\ = \int_ {x \in D _ {t}} \mu (\mathrm{d} x) = \mu (D _ {t}). \tag {9.6.19} \\ \end{array}
$$

下面我们将证明当 $t \to \infty$ 时， $\mu(D_t) \neq 0$ a.s..

注意到 $\{\theta_t\}$ 和 $\{P_t^{\frac{1}{2}}\}$ 都是a.s.收敛的，我们可以定义一个函数 $f(x)$ 为

$$f (x) = \lim _ {t \rightarrow \infty} f _ {t} (x), \quad \text { a.s. } \quad x \in \mathbb {R} ^ {d}. \tag {9.6.20}$$

现设 $\beta^{*}$ 是由 (9.6.10) 所定义的 $\{\beta_{t}^{*}\}$ 的收敛点。于是根据条件 A2) 知 $f(\beta^{*}) = |\det M(\theta)| \neq 0$ 。故有 $f(x) \neq 0$ a.s。这说明 $\max_{x \in D} f(x) \neq 0$ a.s., 因为 $f(x)$ 是一个实多项式的绝对值且 $L(D) > 0$ 。进一步，易见 $f_{t}(x)$ 在 $D$ 上一致收敛于 $f(x)$ 。因此， $\delta_{t} \to \delta_{\infty}$ ，其中 $\delta_{\infty} = \max_{x \in D} f(x) > 0$ a.s.

定义

$$D _ {\infty} = \{x \in D: f (x) \geqslant \lambda \delta_ {\infty} \}, \quad \frac {1}{2} < \lambda < 1,$$

利用 $f(\cdot)$ 的连续性，易见 $L(D_{\infty}) > 0$ 。因此， $[f_t(x), \delta_t]$ 收敛于 $[f(x), \delta_{\infty}]$ ，且对充分大的 $t$ 有 $L(D_t) \geqslant L(D_{\infty})$ 。这说明， $L(D_t) \neq 0$ ，因为 $\mu(D_t) = \frac{L(D_t)}{L(D)}$ 。

因此，根据式(9.6.19)知

$$\sum_ {t = 1} ^ {\infty} P \left(f _ {t} (\eta_ {t}) \geqslant \frac {\delta_ {t}}{2} \mid \mathcal {G} _ {t - 1}\right) = \infty , \quad \text { a.s. }$$

从而根据 Borel-Cantelli-Lévy 引理 (定理 4.2.8) 知

$$\sum_ {t = 1} ^ {\infty} I \left(f _ {t} (\eta_ {t}) \geqslant \frac {\delta_ {t}}{2}\right) = \infty , \quad \text { a.s. }$$

这意味着

$$\lim _ {t \to \infty} \sup f _ {t} (\eta_ {t}) \geqslant \frac {1}{2} \lim _ {t \to \infty} \delta_ {t} = \frac {\delta_ {\infty}}{2} > 0, \quad \text { a.s. }$$

故式 (9.6.18) 成立

第三步：下面我们证明存在正随机变量 $\delta$ 和 $t_0$ 使

$$f (\beta_ {t}) \geqslant \delta , \quad \text { a.s., } \quad \forall t \geqslant t _ {0}, \tag {9.6.21}$$

其中 $f(x)$ 由式(9.6.20)所定义.

利用式 (9.6.17) 及式 (9.6.18) 易见

$$\lim _ {t \to \infty} \sup f _ {t} (\beta_ {t}) \geqslant \frac {\delta_ {\infty}}{1 + \gamma} > 0, \quad \text { a.s. }$$

因此，利用 $f_{t}(x)$ 的一致收敛性，易见存在正随机变量 $\delta > 0$ 及 $t_0 > 0$ ，使

$$f _ {t _ {0}} (\beta_ {t _ {0}}) \geqslant 2 \delta > 0, \tag {9.6.22}$$

且

$$\left| f \left(\beta_ {s}\right) - f _ {t} \left(\beta_ {s}\right) \right| \leqslant \gamma^ {2} \delta , \quad \forall t \geqslant t _ {0}, \forall s \geqslant 0, \tag {9.6.23}$$

其中 $\gamma$ 由式 (9.6.16) 所给出.

我们下面用归纳法来证明式 (9.6.21).
