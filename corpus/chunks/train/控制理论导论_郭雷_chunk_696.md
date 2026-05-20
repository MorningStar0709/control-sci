$$E [ w _ {k + 1} | \mathcal {F} _ {k} ] = 0, \quad E [ \Delta_ {k + 1} | \mathcal {F} _ {k} ] = E [ \Delta_ {k + 1} w _ {k + 1} | \mathcal {F} _ {k} ] = 0,E [ w _ {k + 1} ^ {2} | \mathcal {F} _ {k} ] = R _ {w} (k), \quad E [ \Delta_ {k} \Delta_ {k} ^ {\mathrm{T}} ] = \gamma^ {2} Q _ {\Delta} (k),$$

且存在常数 $r > 2$ 及 $M > 0$ 使

$$\sup _ {k} \left\{E \left[ \left| w _ {k + 1} \right| ^ {r} \mid \mathcal {F} _ {k} \right] + E \left\| w _ {k} \right\| ^ {r} \right\} \leqslant M.$$

下面，我们再给出 $E[\tilde{\theta}_k\tilde{\theta}_k^{\mathrm{T}}]$ 的逼近值 $\Pi_k$ 的计算公式，它是由下列线性确定性差分方程所定义的：

$$
\begin{array}{l} \Pi_ {k + 1} = (I - \mu R _ {k} S _ {k}) \Pi_ {k} (I - \mu R _ {k} S _ {k}) ^ {\mathrm{T}} \\ + \mu^ {2} R _ {w} (k + 1) R _ {k} S _ {k} R _ {k} + \gamma^ {2} Q _ {\Delta} (k + 1), \tag {9.4.47} \\ \end{array}
$$

其中 $S_{k} = E[\phi_{k}\phi_{k}^{\mathrm{T}}]$ ，而 $R_{k}$ 分别如下定义：

a) LMS 情形

$$R _ {k} = I, \tag {9.4.48}$$

b) FFLS 情形

$$R _ {k} = R _ {k - 1} - \mu R _ {k - 1} S _ {k} R _ {k - 1} + \mu R _ {k - 1}, \quad (R _ {0} = P _ {0}), \tag {9.4.49}$$

c) KF 情形

$$R _ {k} = R _ {k - 1} - \mu R _ {k - 1} S _ {k} R _ {k - 1} + \mu Q / R, \quad (R _ {0} = P _ {0} / R). \tag {9.4.50}$$

于是，我们有下列基本结果，其证明见文献 [21].

定理 9.4.2 假设条件 C1\~C3 成立，则对本节所述的三类基本算法中的任意一个，都存在 $\mu^{*}\in(0,1)$ 使对所有 $\mu\in(0,\mu^{*})$ 及所有 $k\geqslant1$ ，下式成立：

$$\left\| E \left[ \tilde {\theta} _ {k} \tilde {\theta} _ {k} ^ {\mathrm{T}} \right] - \Pi_ {k} \right\| \leqslant C \sigma (\mu) \left[ \mu + \frac {\gamma^ {2}}{\mu} + (1 - \alpha \mu) ^ {k} \right], \tag {9.4.51}$$

其中 $\Pi_k$ 由式 (9.4.47) 所定义，而 $\sigma(\mu) \xrightarrow[\mu \to 0]{\longrightarrow} 0$ ，它由下式定义：

$$\sigma (\mu) \stackrel {\text { def }} {=} \min _ {m \geqslant 1} \{\sqrt {\mu} m + \phi (m) \}, \tag {9.4.52}$$

其中 $\phi(m)$ 由条件 C2 给出， $\alpha \in (0,1), C > 0$ 是常数.

注9.4.1 定理9.4.2中所用的条件C1和C2还可以进一步减弱，特别是 $\{\phi_k\}$ 的有界性假设可以大大减弱(详见文献[21])。另一方面，当 $\{\phi_k\}$ 无界时，我们还可以考虑等价的正则化模型

$$\bar {y} _ {k + 1} = \theta_ {k} ^ {\mathrm{T}} \bar {\phi} _ {k} + \overline {{{w}}} _ {k + 1},$$

其中

$$\left(\bar {y} _ {k + 1}, \bar {\phi} _ {k}, \bar {w} _ {k + 1}\right) \stackrel {{\text { def }}} {{=}} \frac {1}{\sqrt {1 + \| \phi_ {k} \| ^ {2}}} (y _ {k + 1}, \phi_ {k}, w _ {k + 1}).$$

显然此处 $\bar{\phi}_k$ 是有界的．最后值得指出，C1中的激励条件

$$\sum_ {t = k + 1} ^ {k + h} S _ {t} \geqslant \delta I$$

在一定意义下是算法稳定的必要条件.

注9.4.2 定理9.4.2的实际用途在于，通过一个非常简单的线性确定性差分方程(9.4.47)就可以描述算法的跟踪性能。这一差分方程便于分析与计算。例如，在弱平稳情形下，即

$$S _ {k} \equiv S, \quad R _ {w} (k) \equiv R _ {w}, \quad Q _ {\Delta} (k) \equiv Q _ {\Delta}, \quad \forall k.$$
