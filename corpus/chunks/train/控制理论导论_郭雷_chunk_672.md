$$\text {(ii)} \sum_ {k = 1} ^ {t} (\phi_ {t} ^ {\mathrm{T}} \tilde {\theta} _ {k}) ^ {2} = o (r _ {t}) \quad \text { a.s. }$$

注意到上述性质 (ii) 说明对 WLS 算法而言，式 (9.2.21) 自动几乎处处成立 (无需关于 $\phi_t$ 的除可测性外的其他条件). 进一步 WLS 算法还具有如下良好性质：

定理 9.2.3 (WLS 的自收敛性 $^{[17]}$ ). 在定理 9.2.2 的条件下, 由式 (9.2.25)\~(9.2.28) 所定义的 WLS 算法具有自收敛性. 即对任何初值 $(P_{0}, \theta_{0})$ 和任何随机回归向量 $\{\phi_{k}, F_{k}\}, \theta_{t}$ 总是几乎处处收敛到某一个向量 $\bar{\theta}$ (不一定与 $\theta$ 相等).

证明 将式 (9.2.1) 代入式 (9.2.25) 并在两边求和得

$$\theta_ {t + 1} = \theta_ {0} + \sum_ {k = 0} ^ {t} a _ {k} P _ {k} \phi_ {k} (\phi_ {k} ^ {\mathrm{T}} \tilde {\theta} _ {k} + w _ {k + 1}). \tag {9.2.32}$$

注意到，在式(9.2.26)两边取迹数 $\operatorname{tr}(\cdot)$ 可得，

$$\sum_ {k = 0} ^ {\infty} a _ {k} \| P _ {k} \phi_ {k} \| ^ {2} = \sum_ {k = 0} ^ {\infty} [ \operatorname{tr} (P _ {k}) - \operatorname{tr} (P _ {k + 1}) ] < \infty .$$

于是利用 Schwarz 不等式和定理 9.2.2(ii) 得

$$\sum_ {k = 1} ^ {t} a _ {k} P _ {k} \phi_ {k} \phi_ {k} ^ {\mathrm{T}} \tilde {\theta} _ {k} \leqslant \left\{\sum_ {k = 1} ^ {t} a _ {k} \| P _ {k} \phi_ {k} \| ^ {2} \sum_ {k = 1} ^ {t} a _ {k} \left(\phi_ {k} ^ {\mathrm{T}} \tilde {\theta} _ {k}\right) ^ {2} \right\} ^ {1 / 2} < \infty . \tag {9.2.33}$$

进一步注意到

$$\sum_ {k = 0} ^ {\infty} E \left[ a _ {k} ^ {2} \| P _ {k} \phi_ {k} w _ {k + 1} \| ^ {2} \mid \mathcal {F} _ {k} \right] \leqslant a _ {0} \sup _ {k} E \left[ w _ {k + 1} ^ {2} \mid \mathcal {F} _ {k} \right] \cdot \sum_ {k = 0} ^ {\infty} a _ {k} \| P _ {k} \phi_ {k} \| ^ {2} < \infty .$$

于是根据鞅收敛定理4.2.11知 $\sum_{k=0}^{\infty} a_k P_k \phi_k w_{k+1}$ 几乎处处收敛. 最后利用式(9.2.33), 从式(9.2.32)知, $\theta_t$ 几乎处处收敛.
