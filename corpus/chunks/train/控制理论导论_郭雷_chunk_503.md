$$\frac {\mathrm{d}}{\mathrm{d} t} \left| \Delta_ {\varepsilon , \bar {t}} x (t) \right| \leqslant a + b \cdot | \Delta_ {\varepsilon , \bar {t}} x (t) |, \quad t \in [ \bar {t}, \bar {t} + \varepsilon),\frac {\mathrm{d}}{\mathrm{d} t} \left| \Delta_ {\varepsilon , \bar {t}} x (t) \right| \leqslant b \cdot | \Delta_ {\varepsilon , \bar {t}} x (t) |, \quad t \in [ \bar {t} + \varepsilon , t _ {f} ].$$

分别从 $\bar{t}$ 到 $t$ 和从 $\bar{t} + \varepsilon$ 到 $t$ 积分上述第二个不等式，并注意到 $\Delta_{\varepsilon, \bar{t}}x(\bar{t}) = 0$ ，不难得到

$$
\begin{array}{l} \left| \Delta_ {\varepsilon , \bar {t}} x (t) \right| \leqslant a \varepsilon + b \cdot \int_ {\bar {t}} ^ {t} | \Delta_ {\varepsilon , \bar {t}} x (\tau) | \mathrm{d} \tau , \quad t \in [ \bar {t}, \bar {t} + \varepsilon), \\ \left| \Delta_ {\varepsilon , \bar {t}} x (t) \right| \leqslant \left| \Delta_ {\varepsilon , \bar {t}} x (\bar {t} + \varepsilon) \right| + b \int_ {\bar {t} + \varepsilon} ^ {t} \left| \Delta_ {\varepsilon , \bar {t}} x (\tau) \right| d \tau , \quad t \in [ \bar {t} + \varepsilon , t _ {f} ]. \\ \end{array}
$$

由此根据定理2.2.5(Gronwall不等式)得 $\Delta_{\varepsilon ,\bar{t}}x(t)$ 的估计

$$
\begin{array}{l} \left| \Delta_ {\epsilon , \bar {t}} x (t) \right| \leqslant a \varepsilon \cdot \exp (b (t - \bar {t})) \leqslant a \varepsilon \cdot e ^ {\varepsilon} = O (\varepsilon), \quad t \in [ \bar {t}, \bar {t} + \varepsilon), \\ \left| \Delta_ {\varepsilon , \bar {t}} x (t) \right| \leqslant \left| \Delta_ {\varepsilon , \bar {t}} x (\bar {t} + \varepsilon) \right| \cdot \exp (b (t - \bar {t} - \varepsilon)) \leqslant O (\varepsilon), \quad t \in [ \bar {t} + \varepsilon , t _ {f} ]. \\ \end{array}
$$

注意，当 $t \in [t_0, \bar{t}]$ 时 $\Delta_{\varepsilon, \bar{t}} x(t) = 0$ ，所以联合 $\Delta_{\varepsilon, \bar{t}} x(t)$ 在 $[\bar{t}, \bar{t} + \varepsilon)$ 和 $[\bar{t} + \varepsilon, t_f]$ 的估计，得到它在整个 $[t_0, t_f]$ 上的估计

$$\left| \Delta_ {\varepsilon , \bar {t}} x (t) \right| \leqslant O (\varepsilon), \quad t \in [ t _ {0}, t _ {f} ]. \tag {7.1.42}$$

然后将 $|\Delta_{\epsilon, \bar{t}} x(t)|$ 的估计式 (7.1.42) 代入 $\Delta_{\epsilon, \bar{t}} J_1[u]$ 的表示式 (7.1.41), 得到

$$\Delta_ {\varepsilon , \bar {t}} J _ {1} [ u ] = - \int_ {\bar {t}} ^ {\bar {t} + \varepsilon} \left[ H (x ^ {*} (t), \bar {u}, \psi (t)) - H (x ^ {*} (t), u ^ {*} (t), \psi (t)) \right] d t + o (\varepsilon).$$

根据连续性知
