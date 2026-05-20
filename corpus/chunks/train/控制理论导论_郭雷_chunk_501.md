$$
\left\{ \begin{array}{l} \dot {\psi} ^ {T} = - \frac {\partial H (x ^ {*} (t) , u ^ {*} (t) , \psi)}{\partial x}, \\ \psi^ {T} (t _ {f}) = - \frac {\partial k (x ^ {*} (t _ {f}))}{\partial x} \end{array} \right. \tag {7.1.37}
$$

的解 (一定存在且唯一), 则 $\Delta J_{1}[u]$ 为

$$
\begin{array}{l} \Delta J _ {1} [ u ] = - \int_ {t _ {0}} ^ {t _ {f}} \frac {\partial (H (x ^ {*} (t) , u ^ {*} (t) + \Delta u (t) , \psi (t)) - H (x ^ {*} (t) , u ^ {*} (t) , \psi (t)))}{\partial x} \Delta x (t) d t \\ - \int_ {t _ {0}} ^ {t _ {f}} \left(H \left(x ^ {*} (t), u ^ {*} (t) + \Delta u (t), \psi (t)\right) - H \left(x ^ {*} (t), u ^ {*} (t), \psi (t)\right)\right) d t \\ + \int_ {t _ {0}} ^ {t _ {f}} o (| \Delta x (t) |) d t + o (| \Delta x (t _ {f}) |). \\ \end{array}
$$

现引入针状变分并考察相应轨线和泛函的改变量．令 $\bar{t} \in \Omega(t_0, t_f; u^*)$ ， $\varepsilon$ 为充分小的实数．任取 $\bar{u} \in \mathbb{U}_r$ ，定义 $u(t)$ 如下：

$$
u (t) = \left\{ \begin{array}{l l} u ^ {*} (t). & t \in [ t _ {0}, \bar {t}), [ \bar {t} + \varepsilon , t _ {f} ]. \\ \bar {u}. & t \in [ \bar {t}, \bar {t} + \varepsilon). \end{array} \right. \tag {7.1.38}
$$

显然，式(7.1.38)中定义的 $u(t)\in \mathcal{U}_{[t_0,t_f]}$ 记 $\Delta_{\varepsilon ,\bar{t}}u(t) = u(t) - u^{*}(t)$ ，于是有

$$
\Delta_ {\varepsilon , \bar {t}} u (t) = \left\{ \begin{array}{l l} 0, & t \in [ t _ {0}, \bar {t}), [ \bar {t} + \varepsilon . t _ {f} ], \\ \bar {u} - u ^ {*} (t), & t \in [ \bar {t}, \bar {t} + \varepsilon). \end{array} \right.
$$

$\Delta_{\varepsilon, \bar{t}} u(t)$ 称为最优控制 $u^{*}(t)$ 的容许改变量，亦称为 $u^{*}(t)$ 的针状变分。最优轨线 $x^{*}(t)$ 和泛函值 $J_{1}[u^{*}]$ 的相应于 $\Delta_{\varepsilon, \bar{t}} u(t)$ 的改变量分别记为 $\Delta_{\varepsilon, \bar{t}} x(t)$ 和 $\Delta_{\varepsilon, \bar{t}} J_{1}[u]$ 。由于 $\Delta_{\varepsilon, \bar{t}} x^{*}(t)$ 满足方程 (7.1.36)，可得

$$
\Delta_ {\varepsilon , \bar {t}} x (t) = 0, \qquad t \in [ t _ {0}, \bar {t}),
\left\{ \begin{array}{l} \frac {\mathrm{d}}{\mathrm{d} t} (\Delta_ {\varepsilon , \bar {t}} x (t)) = f (x ^ {*} (t) + \Delta_ {\varepsilon , \bar {t}} x (t), \bar {u}) - f (x ^ {*} (t), u ^ {*} (t)), \\ \Delta_ {\varepsilon , \bar {t}} x (\bar {t}) = 0, \quad t \in [ \bar {t}, \bar {t} + \varepsilon), \end{array} \right. \tag {7.1.39}

\left\{ \begin{array}{l} \frac {\mathrm{d}}{\mathrm{d} t} (\Delta_ {\varepsilon , \bar {t}} x (t)) = f (x ^ {*} (t) + \Delta_ {\varepsilon , \bar {t}} x (t), u ^ {*} (t)) - f (x ^ {*} (t), u ^ {*} (t)), \\ \Delta_ {\varepsilon , \bar {t}} x (t + \varepsilon), \quad t \in [ t + \varepsilon , t _ {f} ]. \end{array} \right. \tag {7.1.40}
$$

此外，
