定理 4.4.2 设对系统 (4.4.30), (4.4.31) 成立 A1\~A4, 用 $\hat{x}_{k} \stackrel{\operatorname{def}}{=} E(x_{k}|y^{k}), \hat{x}_{k}^{\prime} \stackrel{\operatorname{def}}{=} E(x_{k}|y^{k-1}), P_{k} \stackrel{\operatorname{def}}{=} E[(x_{k}-\hat{x}_{k})(x_{k}-\hat{x}_{k})^{\mathrm{T}}|y^{k}], P_{k}^{\prime} \stackrel{\operatorname{def}}{=} E[(x_{k}-\hat{x}_{k}^{\prime})(x_{k}-\hat{x}_{k}^{\prime})^{\mathrm{T}}|y^{k-1}]$ 分别表示最小方差滤波，预报及相应的估计误差阵。那么和式 (4.4.15)\~(4.4.19) 类似成立递推公式：

$$
\hat {x} _ {k + 1} = \hat {x} _ {k + 1} ^ {\prime} + K _ {k + 1} (y _ {k + 1} - C _ {k + 1} \hat {x} _ {k + 1} ^ {\prime} - H _ {k + 1} v _ {k}), \tag {4.4.34}\hat {x} _ {k + 1} ^ {\prime} = \Phi_ {k + 1, k} \hat {x} _ {k} + B _ {k} u _ {k}, \tag {4.4.35}
\begin{array}{l} K _ {k + 1} = \left(P _ {k + 1} ^ {\prime} C _ {k + 1} ^ {\mathrm{T}} + D _ {k + 1} F _ {k + 1} ^ {\mathrm{T}}\right) \left(C _ {k + 1} P _ {k + 1} ^ {\prime} C _ {k + 1} ^ {\mathrm{T}} + F _ {k + 1} F _ {k + 1} ^ {\mathrm{T}} \right. \\ + C _ {k + 1} D _ {k + 1} F _ {k + 1} ^ {\mathrm{T}} + F _ {k + 1} D _ {k + 1} ^ {\mathrm{T}} \left. C _ {k + 1} ^ {\mathrm{T}}\right) ^ {+}, \tag {4.4.36} \\ \end{array}
P _ {k + 1} = P _ {k + 1} ^ {\prime} - K _ {k + 1} (C _ {k + 1} P _ {k + 1} ^ {\prime} + F _ {k + 1} D _ {k + 1} ^ {\mathrm{T}}), \tag {4.4.37}P _ {k + 1} ^ {\prime} = \Phi_ {k + 1, k} P _ {k} \Phi_ {k + 1, k} ^ {\mathrm{T}} + D _ {k + 1} D _ {k + 1} ^ {\mathrm{T}}, \tag {4.4.38}\hat {x} _ {0} = E \left(x _ {0} \mid y _ {0}\right), \quad P _ {0} = R _ {x _ {0}} ^ {y _ {0}}.
$$

证明 因为 $y^{k}$ 和 $w_{k + 1}$ 独立, 对式 (4.4.30) 取条件期望 $E(-|y^k)$ , 便得式 (4.4.35), 同时也得到式 (4.4.38).

据引理 4.4.6, 在 $y^{k}$ 条件下, $(x_{k+1}, y_{k+1})$ 为条件正态. 在引理 4.4.5 的 ii) 中, 和 x, y, z 分别对应 $x_{k+1}, y^{k}$ 及 $y_{k+1}$ , 据式 (4.4.27) 知

$$\hat {x} _ {k + 1} = \hat {x} _ {k + 1} ^ {\prime} + R _ {x _ {k + 1} y _ {k + 1}} ^ {y ^ {k}} (R _ {y _ {k + 1}} ^ {y ^ {k}}) ^ {+} (y _ {k + 1} - \hat {y} _ {k + 1} ^ {\prime}). \tag {4.4.39}$$

虽然现在讨论最小方差估计，但由于条件正态性，形式上和上一节的估计相同。这里式(4.4.39)对应于式(4.4.14)或式(4.4.15)。在表达 $K_{k + 1}$ 时，照样可用式(4.4.20)，只是 $R_{y_{k + 1}|y^k}$ 对应这里的 $R_{y_{k + 1}}^{y^k}, R_{x_{k + 1}y_{k + 1}|y^k}$ 对应 $R_{x_{k + 1}y_{k + 1}}^{y^k}$ 。利用条件正态性， $R_{y_{k + 1}}^{y^k} (= P_{k + 1}')$ 照样由式(4.4.21)右端表达。由此得到式(4.4.34)及式(4.4.36)。其余两式类似于定理4.4.1相应公式得到，只是把“取期望”改成相应的“取条件期望”。

例4.4.1 设 $x$ 为 $n$ 维正态向量， $x \in \mathcal{N}(Ex, R)$ ， $x_0$ 和 $y_0$ 独立，量测为

$$y _ {k} = C _ {k} x + F _ {k} w _ {k},$$

$C_k$ 和 $F_{k}$ 及 $\omega_{k}$ 满足定理4.4.2. 设 $R > 0$ , $F_{k}F_{k}^{\mathrm{T}} > 0$ . 那么由 $y^{k}$ 对 $x$ 的最小方差估计 $\hat{x}_k$ 可递推地给出, 并表达为

$$\hat {x} _ {k} = S _ {k} \left[ E x + R _ {k} \sum_ {j = 1} ^ {k} C _ {j} ^ {\mathrm{T}} (F _ {j} F _ {j} ^ {\mathrm{T}}) ^ {- 1} y _ {j} \right],S _ {k} = \left[ I + R \sum_ {j = 1} ^ {k} C _ {j} ^ {\mathrm{T}} (F _ {j} F _ {j} ^ {\mathrm{T}}) ^ {- 1} C _ {j} \right] ^ {- 1}.$$

这只要注意现在的状态方程为 $x_{k} \equiv x$ .
