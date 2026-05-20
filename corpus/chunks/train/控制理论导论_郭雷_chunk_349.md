$$
\begin{array}{l} \hat {x} _ {t} = \Psi_ {t, 0} \left(E x _ {0} - R _ {x _ {0} y _ {0}} R _ {y _ {0}} ^ {+} E y _ {0} + R _ {x _ {0} y _ {0}} R _ {y _ {0}} ^ {+} y _ {0}\right) \\ + \Psi_ {t, 0} \int_ {0} ^ {t} \Psi_ {0, s} \left(D _ {s} F _ {s} ^ {\mathrm{T}} + P _ {s} C _ {s} ^ {\mathrm{T}}\right) \left(F _ {s} F _ {s} ^ {\mathrm{T}}\right) ^ {- 1} \mathrm{d} y _ {s} \\ = - \psi_ {t, 0} \hat {x} _ {0} + \Psi_ {t, 0} \int_ {0} ^ {t} \Psi_ {0, s} \left(D _ {s} F _ {s} ^ {\mathrm{T}} + P _ {s} C _ {s} ^ {\mathrm{T}}\right) \left(F _ {s} F _ {s} ^ {\mathrm{T}}\right) ^ {- 1} \mathrm{d} y _ {s}. \\ \end{array}
$$

取随机微分后得

$$\mathrm{d} \hat {x} _ {t} = (A _ {t} - K _ {t} C _ {t}) \hat {x} _ {t} \mathrm{d} t + K _ {t} \mathrm{d} y _ {t}.$$

注4.4.3 由于对高斯系统，线性无偏最小方差估计也是最小方差估计，即 $\hat{x} = E[x_t|y_s,0\leqslant s\leqslant t]$ 也满足定理4.4.5给出的随机微分方程.

注4.4.4 记

$$\bar {w} _ {t} = \int_ {0} ^ {t} (F _ {s} F _ {s} ^ {\mathrm{T}}) ^ {- 1} (\mathrm{d} y _ {s} - C _ {s} \hat {x} _ {s} \mathrm{d} s), \qquad \mathcal {F} _ {t} ^ {y} = \sigma \{y _ {s}, 0 \leqslant s \leqslant t \}.$$

那么 $(\bar{w}_t, \mathcal{F}_t^y)$ 是 Wiener 过程，并且 $\mathcal{F}_t^{\bar{w}} = \mathcal{F}_t^y$ 。 $\bar{w}_t$ 叫新息过程。

注 4.4.5 Kalman-Bucy 滤波 (定理 4.4.5) 对条件正态过程也成立。这时取代式 (4.4.54), (4.4.55) 的是更一般的系统，它的系数可非线地依赖过去的量测量：

$$\mathrm{d} x _ {t} = A _ {t} (y) x _ {t} \mathrm{d} t + B _ {t} u _ {t} (y) \mathrm{d} t + D _ {t} (y) \mathrm{d} w _ {t}, \tag {4.4.72}\mathrm{d} y _ {t} = C _ {t} (y) x _ {t} \mathrm{d} t + F _ {t} (y) \mathrm{d} w _ {t}. \tag {4.4.73}$$

这里 $A_{t}(\xi), u_{t}(\xi), D_{t}(\xi), F_{t}(\xi)$ 为 $\mathcal{B}_{t}$ 可测， $\xi \in C_{T}, G$ 表示 $[0, T]$ 上的连续函数集， $\mathcal{B}_{t}$ 表示在 $C_{T}$ 中由 $\{\xi_{s}, 0 \leqslant s \leqslant t\}$ 所产生的 $\sigma$ -代数.

当系统的系数满足一些可积性条件时，可以证明在 $\mathcal{F}_t^y$ 条件下， $x_t$ 是条件正态过程。这时 $\hat{x}_t \stackrel{\mathrm{def}}{=} E(x_t|\mathcal{F}_t^y)$ 满足随机微分方程
