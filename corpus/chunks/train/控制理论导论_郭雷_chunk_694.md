$$E \prod_ {k = m} ^ {n} (1 - a _ {k + 1}) \leqslant M \lambda^ {n - m + 1}, \quad \forall n \geqslant m \geqslant 0. \tag {9.4.37}$$

对任何 $\varepsilon > 0$ , 根据式 (9.4.32) 得

$$\exp (\varepsilon T _ {m + 1}) \leqslant \exp \left\{\left(1 - a _ {m + 1}\right) \cdot \varepsilon T _ {m} \right\} \cdot \exp (b \varepsilon).$$

但据不等式

$$\exp (\alpha x) \leqslant \alpha \exp (x) + 1, \quad \forall x > 0, 0 < \alpha < 1$$

又知

$$\exp (\varepsilon T _ {m + 1}) \leqslant e ^ {b \epsilon} \cdot \{(1 - a _ {m + 1}) \cdot \exp (\varepsilon T _ {m}) + 1 \}.$$

因此，若取 $\varepsilon$ 充分小使 $e^{b\varepsilon}\cdot \lambda < 1$ ，则根据式(9.4.37)易知

$$\sup _ {k} E \exp (\varepsilon \| P _ {k} \|) < \infty . \tag {9.4.38}$$

此式的一个直接推论是对任何 $p \geqslant 1, \{P_k\}$ 都是 $L_p$ 有界的。因此我们验证了定理9.3.4的条件(ii)，这是因为 $\| P_m^{-1} \| \leqslant \| (\mu Q)^{-1} \| < \infty$ 是自然成立的。

为了验证定理9.3.4中的条件(i)，我们令

$$x _ {k} = h + \mu^ {- 1} \| Q ^ {- 1} \| T _ {k},$$

其中 $T_{k}$ 如式 (9.4.31) 所定义。于是利用式 (9.4.32) 知

$$x _ {k + 1} \leqslant (1 - a _ {k + 1}) x _ {k} + h + \mu^ {- 1} \| Q ^ {- 1} \| b.$$

注意到式 (9.4.36), 利用命题 9.3.3 知 $\{1 / x_{k}\} \in S^{0}$ . 但是, 注意到

$$x _ {k} = \sum_ {i = (k - 1) h + 1} ^ {k h} (1 + \mu^ {- 1} \| Q ^ {- 1} \| \operatorname{tr} (P _ {i})),$$

故据命题9.3.4知

$$\left\{\frac {1}{1 + \mu^ {- 1} \| Q ^ {- 1} \| \operatorname{tr} (P _ {k})} \right\} \in S ^ {0}.$$

从而注意到 $Q_{k} \geqslant \mu Q$ 知

$$\left\{\frac {1}{1 + \left\| Q _ {k} ^ {- 1} P _ {k + 1} \right\|} \right\} \in S ^ {0}.$$

因此利用定理9.3.4知，对Kalman滤波型算法也有 $\{\mu F_k\} \in S_p$ .定理证毕.

定理 9.4.1 在一个统一的一般性激励条件下，建立了三类基本算法的跟踪误差方程 (9.4.5) 之齐次部分的指数稳定性。据此，就可以估计出误差 $\tilde{\theta}_{t}$ 的 $L_{p}$ 模的上界，从而说明这一误差是如何被观测噪声 $\{w_{t}\}$ 和参数变差 $\{\Delta_{t}\}$ 所控制的（见本节习题）。

然而，仅仅知道估计误差方差的上界，还不足以对跟踪算法的性能作精确的评估或优化。这就需要，比如说，给出估计误差方差 $E[\widetilde{\theta}_t\widetilde{\theta}_t^{\mathrm{T}}]$ 的具体表达式。但是，由于算法对数据本质上的非线性性，使得这一任务极其复杂。一个可行的办法是寻找近似表达式。我们先看一个最简单的例子。

例 9.4.1 考虑模型 (9.4.1)～模型 (9.4.2). 假设:

a) $\phi_t$ 和 $\theta_t$ 是标量随机序列；

b) $\{\phi_t\}, \{w_t\}$ 及 $\{\Delta_t\}$ 是相互独立的三个独立随机序列，都具有零均值，分别具有方差 $R_{\phi}, R_{w}$ 及 $\gamma^2 Q_{\Delta}$ ;

c) $\phi_t$ 的四阶矩记为 $R_4$ .

进一步假设估计值 $\hat{\theta}_{k}$ 由简单的 LMS 算法给出，即

$$\hat {\theta} _ {k + 1} = \hat {\theta} _ {k} + \mu \phi_ {k} (y _ {k + 1} - \phi_ {k} \hat {\theta} _ {k}). \tag {9.4.39}$$

在上述理想假设下，我们来计算 $\Pi_k^0 \stackrel{\mathrm{def}}{=} E[\tilde{\theta}_k \tilde{\theta}_k^T]$ . 这时误差方程 (9.4.5) 变为
