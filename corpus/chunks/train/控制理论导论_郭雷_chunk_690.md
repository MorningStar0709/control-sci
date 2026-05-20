其中 $P_0 \geqslant 0, R > 0, Q > 0$ 及 $\hat{\theta}_0$ 可任取为确定性值 (一般来讲， $R$ 和 $Q$ 可以为 $w_t$ 和 $\left(\frac{\Delta t}{\mu}\right)$ 的方差的先验估计).

熟知，根据 Kalman 滤波理论 (见 4.4)，若 $\phi_t$ 是 $\mathcal{F}_t \stackrel{\mathrm{def}}{=} \sigma\{y_i, i \leqslant t\}$ 可测的， $\{\Delta t, w_{t+1}\}$ 是正态白噪声序列，且

$$Q = E \left[ \Delta_ {t} \Delta_ {t} ^ {\mathrm{T}} \right] / \mu^ {2}, \quad R = E w _ {t + 1} ^ {2},\hat {\theta} _ {0} = E \theta_ {0}, \quad P _ {0} = E [ \bar {\theta} _ {0} \bar {\theta} _ {0} ^ {\mathrm{T}} ],$$

则由式(9.4.3)与式(9.4.11)\~(9.4.12)给出的估计是 $\theta_{t}$ 的最小方差估计，且 $P_{t}$ 是估计的协方差阵，换言之

$$\hat {\theta} _ {t} = E [ \theta_ {t} | \mathcal {F} _ {t} ], \quad P _ {t} = E [ \tilde {\theta} _ {t} \tilde {\theta} _ {t} ^ {\mathrm{T}} | \mathcal {F} _ {t} ]. \tag {9.4.13}$$

为了统一研究上述三类算法的稳定性，我们需要下述很一般的激励条件 (excitation condition).

条件 9.4.1(激励条件) 回归向量 $\{\phi_{t}, F_{t}\}$ 是适应的随机序列 (即 $\phi_{t}$ 是 $F_{t}$ 可测的，其中 $F_{t}$ 是非降的子 $\sigma-$ 代数)，且存在正整数 h > 0 使得 $\{\lambda_{k}\} \in S^{0}$ ，其中 $S^{0}$ 由上节定义 9.3.3 所定义，而

$$\lambda_ {k} \stackrel {\text { def }} {=} \lambda_ {\min} \left\{E \left[ \frac {1}{1 + h} \sum_ {i = k h + 1} ^ {(k + 1) h} \frac {\phi_ {i} \phi_ {i} ^ {\mathrm{T}}}{1 + \| \phi_ {i} \| ^ {2}} \mid \mathcal {F} _ {k h} \right] \right\}. \tag {9.4.14}$$

利用上节推论9.3.3, 立即可得下述结论:

命题9.4.1 设 $\{\phi_t\}$ 是 $\phi-$ 混合序列，那么条件9.4.1成立的充分必要条件是存在某正整数 $h > 0$ 使

$$\inf _ {k \geqslant 0} \lambda_ {\min} \left\{\sum_ {i = k h + 1} ^ {(k + 1) h} E \left[ \frac {\phi_ {i} \phi_ {i} ^ {\mathrm{T}}}{1 + \| \phi_ {i} \| ^ {2}} \right] \right\} > 0. \tag {9.4.15}$$

上述激励条件9.4.1还可包括 $\phi$ 混合序列之外的许多重要情形，例如，当回归向量分别由状态空间方程所产生和由时变自回归模型所产生时，均可证明条件9.4.1成立(见本节习题).

本节提到的三类基本的跟踪算法的稳定性，可在统一的激励条件9.4.1下被建立.

定理 9.4.1 $^{[15]}$ 设 $\{\phi_{t}\}$ 满足激励条件 9.4.1, 且在跟踪算法 (9.4.3) 中增益 $L_{t}$ 取为下列三种情形之一:

(i) $L_{t}$ 按LMS或NLMS算法选取(在LMS情形下,需假设 $0 < \mu < (\sup_t \| \phi_t\|^2)^{-1}$ );   
(ii) $L_{t}$ 按遗忘因子FFLS算法选取(此时假定 $\mu$ 充分小且 $\phi_t\in L_{2q},q > 1)$ ;  
(iii) $L_{t}$ 按Kalman滤波型算法选取.

则对上述任一情形，跟踪误差方程(9.4.5)的齐次部分

$$x _ {t + 1} = (I - \mu F _ {t}) x _ {t}, \quad t \geqslant 0, \tag {9.4.16}$$

都是 $L_{p}$ 指数稳定的 (或 $\{\mu F_t\} \in S_p$ ), 其中 $p \geqslant 1$ 为任意正数 (在 FFLS 情形下, $p < q$ ).

证明 (i) 首先考虑 LMS 或 NLMS 情形. 此时, 根据假设知 $\mu F_{t} = \mu L_{t}\phi_{t}^{\mathrm{T}}$ 总满足 $0 \leqslant \mu F_{t} \leqslant I$ . 因此, 根据条件 9.4.1, 命题 9.3.2 及定理 9.3.5 可知 $\{\mu F_{t}\} \in S_{p}, \forall p \geqslant 1$ ;

(ii) 其次考虑 FFLS 情形.

利用式 (9.4.8) 和式 (9.4.9) 经简单计算，不难看出
