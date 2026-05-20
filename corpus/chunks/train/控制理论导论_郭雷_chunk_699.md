9.4.4 设 $C_{nk} \in [0,1]$ , $n \geqslant k \geqslant 0$ 是双下标随机序列，且存在正常数 $N > 0$ 及 $\lambda \in (0,1)$ 使

$$E C _ {n k} \leqslant N \lambda^ {n - k}, \quad \forall n \geqslant k \geqslant 0.$$

如果 $\{\xi_k\}$ 是一非负随机序列，且满足

$$\sigma \stackrel {\text { def }} {=} \sup _ {k \geqslant 0} E [ \xi_ {k} \log^ {\beta} (e + \xi_ {k}) ] < \infty , \quad \beta > 1,$$

证明下述不等式成立：

$$\sum_ {k = 0} ^ {n} E C _ {n k} \xi_ {k} \leqslant C \sigma \log (e + \sigma^ {- 1}), \quad \forall n \geqslant 0,$$

其中 $C$ 是仅依赖于 $\beta, N$ 和 $\lambda$ 的常数.

9.4.5 利用上题和定理 9.4.1 的结论，分别给出本节所述的三类基本算法之跟踪误差的 $L_{p}$ 模（即 $\| \hat{\theta}_{t} - \theta_{t} \|_{L_p}$ ）的上界估计.

9.4.6 设 $\sup_{t} E \| \phi_t \|^2 < \infty$ . 证明若存在某个 $\mu \in (0,1)$ 使由 (9.4.9) 所定义的 $\{P_t\}$ 具有性质 $\sup_{t} E \| P_t \| < \infty$ , 则必存在整数 $h > 0$ , 使

$$\inf _ {t} E \left[ \lambda_ {\min} \left(\sum_ {i = t + 1} ^ {t + h} \phi_ {i} \phi_ {i} ^ {\mathrm{T}}\right) \right] > 0.$$

进一步，举例说明该结论反之一般不成立.

9.4.7 设 $\{z_n, \mathcal{F}_n\}$ 与 $\{u_n, \mathcal{F}_n\}$ 是两个非负适应序列，满足不等式

$$u _ {n + 1} \leqslant \frac {u _ {n}}{(1 - \mu) ^ {h} (1 + \mu u _ {n} z _ {n + 1})}, \quad \forall n \geqslant 0, u _ {0} \neq 0,$$

其中 $\mu \in (0,1), h > 0$ . 证明：如果存在常数 $C > 0$ 及 $\delta > 0$ 使

$$P (z _ {n + 1} \geqslant c | \mathcal {F} _ {n}) \geqslant \delta , \quad \text { a.s. } \quad \forall n \geqslant 0,$$

则对任何 $p \geqslant 1$ 及 $\mu_0 \in (0, 1 - (1 - \delta)^{1 / ph})$ 都有

$$\sup _ {\mu \in [ 0, \mu_ {0} ]} \sup _ {n \geqslant 0} \| u _ {n} \| _ {L _ {p}} < \infty .$$

进一步，令

$$z _ {n + 1} = \lambda_ {\min} \left\{\sum_ {i = n h + 1} ^ {n h + h} \phi_ {i} \phi_ {i} ^ {\mathrm{T}} \right\}.$$

假设 $\{z_n\}$ 满足上述条件，利用上述结论证明由 (9.4.9) 所定义的 $\{P_t\}$ 具有性质

$$\sup _ {\mu \in (0, \mu_ {0} | t \geqslant 0} \sup \| P _ {t} \| _ {L _ {p}} < \infty .$$

(提示：令 $u_{n} = \lambda_{\min}^{-1}(P_{nh}^{-1})$ ，可参见文献 [23].)

9.4.8 考虑由 (9.4.50) 所定义的 Riccati 方程

$$R _ {k} = R _ {k - 1} - \mu R _ {k - 1} S _ {k} R _ {k - 1} + \mu Q R ^ {- 1}, \quad (R _ {0} = P _ {0} R ^ {- 1})$$

以及由 Riccati 方程 (9.4.12) 所 “诱导” 的 “平均值” 方程

$$\overline {{{P}}} _ {k} = [ \overline {{{P}}} _ {k - 1} ^ {- 1} + \mu R ^ {- 1} S _ {k} ] ^ {- 1} + \mu Q, \quad (\overline {{{P}}} _ {0} = P _ {0}).$$

假设 $\{S_k\}$ 是有界的非负定矩阵序列且存在 $h > 0$ 及 $\delta > 0$ 使

$$\sum_ {t = k + 1} ^ {k + h} S _ {t} \geqslant \delta I, \quad \forall k \geqslant 0.$$

证明：当 $\mu$ 适当小时， $\{R_k\}$ 及 $\{\overline{P}_k\}$ 都是有界的且

$$\| R _ {k} - \overline {{P}} _ {k} R ^ {- 1} \| = O (\mu). \quad \forall k.$$

(提示：可参考文献 [21].)
