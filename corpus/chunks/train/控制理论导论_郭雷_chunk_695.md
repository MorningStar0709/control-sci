$$\tilde {\theta} _ {k + 1} = (1 - \mu \phi_ {k} ^ {2}) \tilde {\theta} _ {k} - \mu \phi_ {k} w _ {k + 1} + \Delta_ {k + 1}, \tag {9.4.40}$$

两边平方并取期望得

$$\Pi_ {k + 1} ^ {0} = (1 - 2 \mu R _ {\phi} + \mu^ {2} R _ {4}) \Pi_ {k} ^ {0} + \mu^ {2} R _ {\phi} R _ {w} + \gamma^ {2} Q _ {\Delta}, \tag {9.4.41}$$

这是一个线性差分方程，其解可以具体写出来。特别地，若

$$\left| 1 - 2 \mu R _ {\phi} + \mu^ {2} R _ {4} \right| < 1,$$

则式 (9.4.41) 的解 $\Pi_k^0$ 将收敛到 $\Pi^*$ , 其中

$$\Pi^ {*} = \frac {1}{1 - \mu R _ {4} / (2 R _ {\phi})} \Pi , \tag {9.4.42}\Pi = \frac {1}{2 R _ {\phi}} \left[ \mu R _ {\phi} R _ {w} + \frac {\gamma^ {2}}{\mu} Q _ {\Delta} \right]. \tag {9.4.43}$$

经简单计算可得

$$\left| \Pi^ {*} - \Pi \right| \leqslant \sigma (\mu) \Pi , \quad \sigma (\mu) = \left[ \frac {R _ {4} / (2 R _ {\phi})}{1 - \mu R _ {4} / (2 R _ {\phi})} \right] \mu . \tag {9.4.44}$$

由于当 $\mu \to 0$ 时 $\sigma(\mu) \to 0$ , 这说明对小的 $\mu, \Pi^{*}$ 可以被 $\Pi$ 很好地逼近.

这个例子之所以特别容易，是因为对 $\{\phi_k, w_k, \Delta_k\}$ 假定了很强的独立性，这使得 $\widetilde{\theta}_k$ 与 $\phi_k$ 独立，从而使计算 $\Pi_k^0$ 成为可能.

一般情形下，我们需要处理 $\{\phi_k\}$ 的相依性，这是这个问题的本质困难。直观上讲，如果 $\{\phi_k\}$ 的相依性是“衰减的”，且 $\hat{\theta}_k$ 以较小的幅度依赖于“最近的” $\phi_k$ （这相当于要求适应速率 $\mu$ 较小，且误差方程的齐次部分指数稳定），则 $\hat{\theta}_k$ 与 $\phi_k$ 也应有“弱相依性”，从而类似于式(9.4.44)的逼近公式也应存在。

事实上，我们下面将说明在很一般的条件下，对本节给出的三类基本算法，当 $\mu$ 较小时在本质上都有逼近公式

$$\| E [ \widetilde {\theta} _ {k} \widetilde {\theta} _ {k} ^ {\mathrm{T}} ] - \Pi_ {k} \| \leqslant \sigma (\mu) \| \Pi_ {k} \|, \tag {9.4.45}$$

其中当 $\mu \to 0$ 时 $\sigma(\mu) \to 0$ , $\Pi_k$ 由一个简单的线性确定性差分方程所定义 (其形式与 (9.4.41) 类似但没有高阶项 $\mu^2 R_4$ ).

为此，我们先引进所用的几个条件.

C1(可辨识性). 存在整数 $h > 0$ 及常数 $\delta > 0$ 使 $S_{t} \stackrel{\mathrm{def}}{=} E[\phi_{t} \phi_{t}^{\mathrm{T}}]$ 满足

$$\sum_ {t = k + 1} ^ {k + h} S _ {t} \geqslant \delta I, \quad \forall k \geqslant 0.$$

进一步，存在常数 $C_{\phi}$ 使 $\| \phi_k\| \leqslant C_\phi, \forall k \geqslant 0.$

C2(弱相依性). 回归向量序列 $\{\phi_k\}$ 在下列意义下是弱相依 ( $\phi$ 混合) 的

$$\sup _ {A \in \mathcal {G} _ {k + m}, B \in \mathcal {F} _ {k}} | P (A | B) - P (A) | \leqslant \phi (m), \quad \forall k, \forall m, \tag {9.4.46}$$

其中函数 $\phi(m) \geqslant 0$ 满足 $\phi(m) \xrightarrow[m]{\text{def}} 0$ , 而 $\mathcal{G}_k \stackrel{\text{def}}{=} \sigma\{\phi_k\}, \mathcal{F}_k \stackrel{\text{def}}{=} \sigma\{\phi_i, w_i, \Delta_i, i \leqslant k\}$ .

C3(噪声条件). 对 C2 中定义的 $F_{k}$ ，有
