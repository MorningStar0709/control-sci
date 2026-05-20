现在证明 $T(t)$ 的半群性质．设 $t, s > 0$ ，并取 $\theta' = \pi / 2 + \delta'$ ， $0 < \delta' < \delta$ ，则我们有

$$
\begin{array}{l} T (t) T (s) = - \frac {1}{4 \pi^ {2}} \int_ {\Gamma_ {e, \theta}} \mathrm{e} ^ {\lambda t} R (\lambda ; A) \mathrm{d} \lambda \int_ {\Gamma_ {2 e, \theta^ {\prime}}} \mathrm{e} ^ {\mu s} R (\mu ; A) \mathrm{d} \mu \\ = - \frac {1}{4 \pi^ {2}} \int_ {\Gamma_ {\varepsilon , \theta}} \int_ {\Gamma_ {2 \varepsilon , \theta^ {\prime}}} \mathrm{e} ^ {\lambda t + \mu s} [ R (\lambda ; A) - R (\mu ; A) ] \frac {\mathrm{d} \lambda \mathrm{d} \mu}{\mu - \lambda} \\ = - \frac {1}{4 \pi^ {2}} \int_ {\Gamma_ {\epsilon , \theta}} e ^ {\lambda t} R (\lambda ; A) d \lambda \int_ {\Gamma_ {2 \epsilon , \theta^ {\prime}}} \frac {e ^ {\mu s} d \mu}{\mu - \lambda} \\ + \frac {1}{4 \pi^ {2}} \int_ {\Gamma_ {\varepsilon , 2 \theta^ {\prime}}} \mathrm{e} ^ {\mu s} R (\mu ; A) \mathrm{d} \mu \int_ {\Gamma_ {\varepsilon , \theta}} \frac {\mathrm{e} ^ {\lambda t} \mathrm{d} \lambda}{\mu - \lambda} = T (t + s), \\ \end{array}
$$

这里我们已经使用了如下事实：

$$\frac {1}{2 \pi \mathrm{i}} \int_ {\Gamma_ {2 \varepsilon , \theta^ {\prime}}} \frac {\mathrm{e} ^ {\mu s} \mathrm{d} \mu}{\mu - \lambda} = \mathrm{e} ^ {\lambda s} \quad \text {和} \quad \frac {1}{2 \pi \mathrm{i}} \int_ {\Gamma_ {\varepsilon , \theta}} \frac {\mathrm{e} ^ {\lambda t} \mathrm{d} \lambda}{\mu - \lambda} = 0.$$

设 $B$ 是 $T(t)$ 的生成算子. 由于 $\| T(t) \| \leqslant M_1$ , 我们有 $\mathbb{C}_+ \subset \rho(A)$ , 其中 $\mathbb{C}_+ = \{\mu \in \mathbb{C} \mid \operatorname{Re} \mu > 0\}$ . 对于任意 $\mu \in \mathbb{C}_+$ , 取 $\varepsilon$ 使得 $0 < \varepsilon < \operatorname{Re} \mu$ , 则我们有

$$
\begin{array}{l} R (\mu ; B) = \int_ {0} ^ {\infty} \mathrm{e} ^ {- \mu t} T (t) \mathrm{d} t \\ = \frac {1}{2 \pi \mathrm{i}} \int_ {0} ^ {\infty} \mathrm{e} ^ {- \mu t} \mathrm{d} t \int_ {\Gamma_ {\epsilon , \theta}} \mathrm{e} ^ {\lambda t} R (\lambda ; A) \mathrm{d} \lambda \\ = \frac {1}{2 \pi \mathrm{i}} \int_ {\Gamma_ {t, \theta}} R (\lambda ; A) \mathrm{d} \lambda \int_ {0} ^ {\infty} \mathrm{e} ^ {(\lambda - \mu) t} \mathrm{d} t \\ = \frac {1}{2 \pi \mathrm{i}} \int_ {\Gamma_ {\epsilon , \theta}} R (\lambda ; A) \frac {\mathrm{d} \lambda}{\mu - \lambda} = R (\mu ; A), \\ \end{array}
$$

由此得到 A = B.

(3) 最后一个结论的证明是直接的，只需注意当 $z \in \Sigma_{\delta}$ 时， $\mathrm{e}^{\lambda z} R(\lambda; A)$ 沿着 $\Gamma_{\varepsilon, \theta}^{1}$ 和 $\Gamma_{\varepsilon, \theta}^{3}$ 的积分是收敛的.
