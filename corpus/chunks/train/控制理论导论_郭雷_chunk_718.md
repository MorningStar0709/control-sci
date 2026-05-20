这是一个借助于随机搜索法来近似最大化 $f_{t}(x)$ 的简单方法， $\gamma > 0$ 的作用是为了保证 $\{\beta_{t}\}$ 的收敛性。下面定理说明如此定义的 $\{\beta_{t}\}$ 确实满足要求：

定理9.6.1 对由式(9.6.11)定义的 $\hat{\theta}_t$ ，假设 $\beta_t$ 按式(9.6.16)选取，则对任何的反馈输入序列 $\{u_t\}$ 都有

(i) $\{\hat{\theta}_{t}\}$ 几乎处处收敛 (事实上，有限步后 $\beta_{t}$ 是常数);  
(ii) $(A(\hat{\theta}_t), B(\hat{\theta}_t))$ 几乎处处一致能控.

证明 我们将证明分为三步：

第一步：我们证明对任何 $t \geqslant 0, (A(\hat{\theta}_t), b(\hat{\theta}_t))$ 是几乎处处能控的，或 $f_t(\beta_t) \neq 0$ a.s., 其中 $f_t(x)$ 由式 (9.6.14) 所定义.

为此我们仅需证明 $f_{t}(\eta_{t}) \neq 0$ a.s. $\forall t \geqslant 0$ 即可，因为根据式 (9.6.16) 我们总有

$$f _ {t} \left(\beta_ {t}\right) \geqslant \frac {f _ {t} \left(\eta_ {t}\right)}{1 + \gamma}, \quad \forall t \geqslant 0. \tag {9.6.17}$$

利用条件 A2) 及式 (9.6.10), 式 (9.6.13), 易见 $\det M(\theta_{t} + P_{t}^{\frac{1}{2}}x)$ 是 x 的非零实有理多项式. 因此, 对 Lebesgue 测度 $L\{\cdot\}$ 有 (见本节习题)

$$L \{x: f _ {t} (x) = 0 \} = 0, \quad \text { a.s. } \quad \forall t \geqslant 0.$$

这说明，对 $D$ 上的均匀概率测度 $\mu (\cdot)$ 有

$$\mu (x \in D: f _ {t} (x) = 0) = 0, \quad \text { a.s. } \quad \forall t \geqslant 0.$$

进一步，对任何适应的输入序列 $\{u_t\}$ ，易见 $f_{t}(\cdot)$ 是关于 $\sigma$ 代数 $\mathcal{G}_{t-1} \stackrel{\mathrm{def}}{=} \sigma\{w_{i}, \eta_{i-1}, i \leqslant t\}$ 可测的。于是，利用 $\eta_{t}$ 与 $\mathcal{G}_{t-1}$ 的独立性，知

$$
\begin{array}{l} E I \left(f _ {t} \left(\eta_ {t}\right) = 0\right) = E \left\{E ^ {\prime} \left[ I \left(f _ {t} \left(\eta_ {t}\right) = 0\right) \mid \mathcal {G} _ {t - 1} \right] \right\} \\ = E \left\{\int_ {x \in D} I \left(f _ {t} (x) = 0\right) \mu (\mathrm{d} x) \right\} \\ = E \left\{\mu (x \in D): f _ {t} (x) = 0 \right\} = 0. \\ \end{array}
$$

这说明 $P(f_{t}(\eta_{t}) = 0) = 0$ 或 $f_{t}(\eta_{t}) \neq 0$ a.s., $\forall t \geqslant 0$ . 因此 $[A(\bar{\theta}), b(\hat{\theta}_{t})]$ 是 a.s. 能控的.

第二步：我们证明存在一个正随机变量 $\delta_{\infty} > 0$ 使

$$\limsup _ {t \to \infty} f _ {t} (\eta_ {t}) \geqslant \delta_ {\infty}, \quad \text { a.s. } \tag {9.6.18}$$

记

$$\delta_ {t} \stackrel {\text { def }} {=} \max _ {x \in D} f _ {t} (x), \quad D _ {t} \stackrel {\text { def }} {=} \left\{x \in D: f _ {t} (x) \geqslant \frac {\delta_ {t}}{2} \right\}.$$

注意到 $\theta_t, P_t^{\frac{1}{2}}$ 及 $\delta_t$ 都是 $\mathcal{G}_{t-1}$ 可测的，且 $\eta_t$ 与 $\mathcal{G}_{t-1}$ 独立，其中 $\mathcal{G}_{t-1}$ 由上面所定义。于是根据条件期望性质有
