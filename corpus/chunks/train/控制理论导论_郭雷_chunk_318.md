$$\int_ {- \infty} ^ {\infty} f (t) \mathrm{d} \eta_ {t} \stackrel {\text { def }} {=} \zeta \left(= \underset {n \to \infty} {\text { l.i.m. }} \int_ {- \infty} ^ {\infty} f _ {n} (t) \mathrm{d} \eta_ {t}\right),$$

“l.i.m.”表示均方极限.

可以证明对 $f, g \in L_2(\mathrm{d}F)$

$$E \int_ {- \infty} ^ {\infty} f (t) \mathrm{d} \eta_ {t} \left(\int_ {- \infty} ^ {\infty} g (t) \mathrm{d} \eta_ {t}\right) ^ {*} = \int_ {- \infty} ^ {\infty} f (t) g ^ {*} (t) \mathrm{d} F (t).$$

宽平稳过程有谱表示，对任意 $p$ 维宽平稳过程 $\xi_t$ ，存在 $p$ 维直交增量过程 $\eta_t$ ，使

$$\xi_ {t} = \int_ {- \infty} ^ {\infty} \mathrm{e} ^ {\mathrm{i} t \lambda} \mathrm{d} \eta_ {\lambda}, \quad - \infty < t < \infty .$$

对离散时间的宽平稳过程 $\{\xi_k\}$ , 有

$$\xi_ {k} = \int_ {- \pi} ^ {\pi} \mathrm{e} ^ {\mathrm{i} k \lambda} \mathrm{d} \eta_ {\lambda}, \tag {4.3.2}E \xi_ {k} \xi_ {j} ^ {*} = \int_ {- \pi} ^ {\pi} \mathrm{e} ^ {\mathrm{i} \lambda (k - j)} \mathrm{d} F (\lambda).$$

由此看出，相关函数 $R(\tau)$ 是谱函数的Fourier-Stieltjes变换，

$$R (\tau) = \int_ {- \pi} ^ {\pi} \mathrm{e} ^ {\mathrm{i} \lambda \tau} \mathrm{d} F (\lambda). \tag {4.3.3}$$

当 $\tau = 0$ 时， $R(0) = \int_{-\pi}^{\pi} \mathrm{d}F(\lambda)$ ，也就是说，谱函数的全变差等于 $\{\xi_k\}$ 的二阶矩。

可以证明 $\xi_{k}$ 的时间平均均方收敛到随机变量 $\xi \stackrel{\mathrm{def}}{=} (\eta_{0^{+}} - \eta_{0^{-}})$ ，即

$$E \left\| \frac {1}{N} \sum_ {k = 1} ^ {N} \xi_ {k} - \xi \right\| ^ {2} \underset {N \rightarrow \infty} {\longrightarrow} 0.$$

当 $N$ 趋于无穷时，若时间平均 $\frac{1}{N} \sum_{k=1}^{N} \xi_k$ ，趋于 $E\xi_k$ 时，则称 $\{\xi_k\}$ 具有遍历性，或对 $\{\xi_k\}$ 成立遍历定理.

$f(\lambda) \stackrel{\mathrm{def}}{=} \frac{\mathrm{d}F(\lambda)}{\mathrm{d}\lambda}$ 称为谱密度，这时式 (4.3.2) 成为

$$R (\tau) = \int_ {- \pi} ^ {\pi} \mathrm{e} ^ {\mathrm{i} \lambda \tau} f (\lambda) \mathrm{d} \lambda .$$

对平稳过程的预报、内插、滤波在20世纪40年代到60年代做过详细研究，并有许多重要应用。根据对 $\xi_{j}, 0 \leqslant j \leqslant k$ 的观测，要对 $\xi_{k + \tau}, \tau > 0$ 做线性估计，使估计误差在均方意义下达到最小，叫预报。当观测带有噪声时，要去伪存真，这就是滤波。也可能 $k$ 以前观测值中丢了一些数据，则就要内插。

这类问题的解决主要基于已知相应过程的谱函数或谱密度上，当谱密度为有理函数时，可用密度因式分解的办法，求出最优预报或最优滤波的传递函数。对一般的过程，则要求 $\int_{-\pi}^{\pi}\log f(\lambda)\mathrm{d}\lambda > -\infty$ ，也可得到最优预报等有关结果。

设对任意足标 $k_{1}, \cdots, k_{n}$ 及任意 j.

$$(\xi_ {k _ {1}}, \dots , \xi_ {k _ {n}}) \quad \text {和} \quad (\xi_ {k _ {1} + j}, \dots , \xi_ {k _ {n} + j})$$

的分布函数相同，则 $\{\xi_k\}$ 称为狭义平稳过程.

显然，当 $E\| \xi_k\|^2 < \infty$ 时，狭义平稳过程一定也宽平稳.
