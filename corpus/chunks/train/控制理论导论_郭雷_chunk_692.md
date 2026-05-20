其中 $I(\cdot)$ 为示性函数。于是利用式(9.4.25)和式(9.4.26)知

$$
\begin{array}{l} T _ {m + 1} ^ {p} \leqslant T _ {m + 1} ^ {p} \left[ I \left(\operatorname{tr} \left(P _ {m h}\right) \geqslant \mu^ {- 1}\right) + I \left(\operatorname{tr} \left(P _ {m h}\right) <   \mu^ {- 1}\right) \right] \\ \leqslant b _ {m + 1} T _ {m} ^ {p} + [ h (1 - \mu) ^ {- h} ] ^ {p} \cdot \mu^ {- p}. \tag {9.4.27} \\ \end{array}
$$

根据式(9.4.24)中 $a_{m + 1}$ 的定义及不等式 $\operatorname {tr}(P_k^2)\geqslant d^{-1}(\operatorname {tr}P_k)^2$ (其中 $d$ 是矩阵 $P_{k}$ 的行数)易见在 $\{\mathrm{tr}(P_{mh})\geqslant \mu^{-1}\}$ 上有

$$E [ a _ {m + 1} | \mathcal {F} _ {m h} ] \geqslant \frac {\mu (h + 1) \mathrm{tr} (P _ {m h} ^ {2}) \cdot \lambda_ {m}}{h (1 + \mu \mathrm{tr} (P _ {m h})) \mathrm{tr} (P _ {m h})} \geqslant \frac {(h + 1) \lambda_ {m}}{2 h d},$$

从而根据 $b_{m + 1}$ 的定义有

$$E [ b _ {m + 1} | \mathcal {F} _ {m h} ] \leqslant (1 - \mu) ^ {(1 - 2 h) p} \left(1 - \frac {(h + 1) \lambda_ {m}}{4 h d}\right) I (\operatorname{tr} (P _ {m h}) \geqslant \mu^ {- 1}).$$

现令

$$
\alpha_ {m + 1} = \left\{ \begin{array}{l l} b _ {m + 1}, & \text {若} \operatorname{tr} (P _ {m h}) \geqslant \mu^ {- 1}, \\ (1 - \mu) ^ {(1 - 2 h) p} \left(1 - \frac {(1 + h) \lambda_ {m}}{4 h d}\right), & \text {上式不成立}, \end{array} \right.
$$

于是利用式 (9.4.27) 知

$$T _ {m + 1} ^ {p} \leqslant \alpha_ {m + 1} T _ {m} ^ {p} + [ h \mu^ {- 1} (1 - \mu) ^ {- h} ] ^ {p}.$$

由于根据假设条件 9.4.1, $\{\lambda_m\} \in S^0$ ，且 $\lambda_m \leqslant \frac{h}{1 + h}$ ，因此根据命题 9.3.2 知 $\left\{\left(\frac{1 + h}{4hd}\right)\lambda_m\right\} \in S^0$ 。于是根据 $\alpha_{m+1}$ 的定义知当 $\mu$ 充分小时，命题 9.3.3 的条件满足，因此我们有 $\sup_m ET_{m+1}^p < \infty$ 。故有

$$\sup _ {t} \| P _ {t} \| _ {L _ {p}} < \infty .$$

因此，遗忘因子算法的指数稳定性得证.

(iii) 最后，我们来考虑 Kalman 滤波型算法.

利用式 (9.4.11) 及式 (9.4.12) 可见

$$P _ {t} = (I - \mu L _ {t} \phi_ {t} ^ {\mathrm{T}}) P _ {t - 1} (I - \mu L _ {t} \phi_ {t} ^ {\mathrm{T}}) ^ {\mathrm{T}} + Q _ {t}, \tag {9.4.28}$$

其中

$$Q _ {t} = \mu R L _ {t} L _ {t} ^ {\mathrm{T}} + \mu Q. \tag {9.4.29}$$

由此易见

$$P _ {t} \geqslant Q _ {t} \geqslant \mu Q, \quad \forall t \geqslant 0. \tag {9.4.30}$$

我们的目的是利用定理9.3.4来证明所欲的指数稳定性。为此先考虑 $\{P_t\}$ 的 $L_{p}$ 有界性。

对由式 (9.4.12) 所定义的 $\{P_t\}$ , 记

$$T _ {m} = \sum_ {k = (m - 1) h + 1} ^ {m h} \operatorname{tr} \left(P _ {k}\right), \quad T _ {0} = 0, \tag {9.4.31}$$

其中 $h > 0$ 是整数．我们先来证明

$$T _ {m + 1} \leqslant (1 - a _ {m + 1}) T _ {m} + b, \tag {9.4.32}$$

其中 $b = \frac{3}{2} h(h + 1)\mu \mathrm{tr}Q,$ 而
