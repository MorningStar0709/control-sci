# 连续时间系统

我们先来看连续时间系统的线性最小方差滤波，为简单起见，先不考虑控制

项. 设系统由下述线性随机微分方程描述:

$$\mathrm{d} x _ {t} = A _ {t} x _ {t} \mathrm{d} t + D _ {i} \mathrm{d} w _ {t}, \tag {4.4.54}\mathrm{d} y _ {t} = C _ {t} x _ {t} \mathrm{d} t + F _ {t} \mathrm{d} w _ {t}, \quad F _ {t} F _ {t} ^ {\mathbf {T}} > 0. \tag {4.4.55}$$

$A_{t}, D_{t}, D_{t}$ 和 $F_{t}$ 为确定性阵， $w_{t}$ 为 Wiener 过程。设成立可积性条件

$$\int_ {0} ^ {T _ {f}} \left[ \| A _ {s} \| + \| C _ {s} ^ {\mathrm{T}} (F _ {s} F _ {s} ^ {\mathrm{T}}) ^ {- 1} C _ {s} \| + \| C _ {s} \| ^ {2} + \| D _ {s} \| ^ {2} + \| F _ {s} \| ^ {2} \right] \mathrm{d} s < \infty , \quad T _ {f} < \infty , \tag {4.4.56}$$

设初始估计为

$$
\hat {x} _ {0} = E x _ {0} + R _ {x _ {0} y _ {0}} R _ {y _ {0}} ^ {+} (y _ {0} - E y _ {0}), \tag {4.4.57}R _ {0} = R _ {x _ {0}} - R _ {x _ {0} y _ {0}} R _ {y _ {0}} ^ {+} R _ {y _ {0} x _ {0}}, \tag {4.4.58}
E w _ {t} \left[ \begin{array}{c} x _ {0} \\ y _ {0} \end{array} \right] = 0, \quad \forall t \in [ 0, T _ {f} ],
$$

记 $G_{t} = \left\{\hat{x}_{t}^{G} = c_{t} + G_{0}(t)y_{0} + G_{1}(t)\int_{0}^{t}G_{2}(s)\mathrm{d}y_{s}:c_{t},G_{0}(t)\text{和} G_{1}(t)\right.$ 为确定性，且 $\int_0^t [\| G_2(s)C_s\| +\| G_2(s)F_s\|^2 ]\mathrm{d}s <   \infty \Bigg\} .$

如果 $E\hat{x}_t = Ex_t$ ，且

$$E (x _ {t} - \hat {x} _ {t}) (x _ {t} - \hat {x} _ {t}) ^ {\mathrm{T}} = \min _ {x \in G _ {t}} E (x _ {t} - x) (x _ {t} - x) ^ {\mathrm{T}},$$

那么称 $\hat{x}_t$ 为用 $(y_s, 0 \leqslant s \leqslant t)$ 对 $x_t$ 的线性无偏最小方差估计。而 $\hat{x}_t$ 所满足的随机微分方程为 Kalman-Bucy 滤波。

首先，在条件(4.4.56)下，确定性的Riccati微分方程

$$\dot {P} _ {t} = P _ {t} A _ {t} ^ {\mathrm{T}} + A _ {t} P _ {t} + D _ {t} D _ {t} ^ {\mathrm{T}} - \left(D _ {t} F _ {t} ^ {\mathrm{T}} + P _ {t} C _ {t} ^ {\mathrm{T}}\right) \left(F _ {t} F _ {t} ^ {\mathrm{T}}\right) ^ {- 1}\cdot \left(D _ {t} F _ {t} ^ {\mathrm{T}} + P _ {t} C _ {t} ^ {\mathrm{T}}\right) ^ {\mathrm{T}}, \quad P _ {0} = R _ {0} \tag {4.4.59}$$

有唯一对称非负定解.

定理 4.4.5 (Kalman-Bucy 滤波) 设条件 (4.4.56) 成立，那么满足初值 $\hat{x}_{0} = E(x_{0}|y_{0})$ ， $P_{0} = R_{x_{0}}^{y_{0}}$ 的线性无偏最小方差估计 $\hat{x}_{t}$ 满足线性随机微分方程

$$\mathrm{d} \hat {x} _ {t} = A _ {t} \hat {x} _ {t} \mathrm{d} t + (D _ {t} F _ {t} ^ {\mathrm{T}} + P _ {t} C _ {t} ^ {\mathrm{T}}) (F _ {t} F _ {t} ^ {\mathrm{T}}) ^ {- 1} (\mathrm{d} y _ {t} - C _ {t} \hat {x} _ {t} \mathrm{d} t),$$

其中 $P_{t} \stackrel{\mathrm{def}}{=} E(x_{t} - \hat{x})(x_{t} - \hat{x}_{t})^{\mathrm{T}}$ 满足方程 (4.4.59).

证明 设 $\Phi_{t,s}$ 为基本解阵

$$\frac {\mathrm{d}}{\mathrm{d} t} \Phi_ {t, s} = A _ {t} \Phi_ {t, s}, \quad \Phi_ {s, s} = I.$$

据式 (4.3.24)
