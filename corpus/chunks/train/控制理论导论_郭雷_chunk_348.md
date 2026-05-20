$$
\begin{array}{l} E \left(x _ {t} - \hat {x} _ {t} ^ {G}\right) \left(x _ {t} - \hat {x} _ {t} ^ {G}\right) ^ {\mathrm{T}} \\ = E \left(H _ {t} \hat {x} _ {0} - c _ {t} - G _ {0} (t) y _ {0}\right) \left(H _ {t} \hat {x} _ {0} - c _ {t} - G _ {0} (t) y _ {0}\right) ^ {\mathrm{T}} + P _ {t} \\ + \int_ {0} ^ {t} [ G _ {1} (t) G _ {2} (s) - L _ {s} ^ {\mathrm{T}} \left(D _ {s} F _ {s} ^ {\mathrm{T}} + P _ {s} C _ {s} ^ {\mathrm{T}}\right) \left(F _ {s} F _ {s} ^ {\mathrm{T}}\right) ^ {- 1} ] F _ {s} F _ {s} ^ {\mathrm{T}} \\ \cdot \left[ G _ {1} (t) G _ {2} (t) - L _ {2} ^ {\mathrm{T}} (D _ {s} F _ {s} ^ {\mathrm{T}} + P _ {s} C _ {s} ^ {\mathrm{T}}) (F _ {s} F _ {s} ^ {\mathrm{T}}) ^ {- 1} \right] ^ {\mathrm{T}} \mathrm{d} s. \tag {4.4.65} \\ \end{array}
$$

记

$$K _ {t} \stackrel {\text { def }} {=} (D _ {t} F _ {t} ^ {\mathrm{T}} + P _ {t} C _ {t} ^ {\mathrm{T}}) (F _ {t} F _ {t} ^ {\mathrm{T}}) ^ {- 1}. \tag {4.4.66}$$

由于 $P_{t}$ 不依赖 $G_0(t), G_1(t)$ 及 $G_{2}(t)$ ，所以为使式 (4.4.65) 右端达极小的充分必要条件是

$$H _ {t} \hat {x} _ {0} - c _ {t} - G _ {0} (t) y _ {0} = 0, \tag {4.4.67}G _ {1} (t) G _ {2} (s) = L _ {s} ^ {\mathrm{T}} K _ {s}, \tag {4.4.68}$$

这时， $P_{t}$ 就是估计误差协方差阵.

把式 (4.4.68) 代入式 (4.4.61). 知最优的 $L_{s}$ 应满足方程

$$\frac {\mathrm{d}}{\mathrm{d} s} L _ {s} ^ {\mathbf {T}} = L _ {s} ^ {\mathbf {T}} \left(- A _ {s} + K _ {s} C _ {s}\right), \quad L _ {t} ^ {\mathbf {T}} = I. \tag {4.4.69}$$

设 $\Psi_{t,s}$ 为基本解阵

$$\frac {\mathrm{d}}{\mathrm{d} s} \Psi_ {t, s} = (A _ {t} - K _ {s} C _ {s}) \Psi , \quad \Psi_ {s, s} = I, \tag {4.4.70}$$

从解的唯一性知

$$L _ {s} ^ {\mathrm{T}} = \Psi_ {t, s}. \tag {4.4.71}$$

从式 (4.4.68) 及式 (4.4.71) 看出，最优的 $G_{1}^{0}(t), G_{2}^{0}(t)$ 可取为

$$G _ {1} ^ {0} (t) = \Psi_ {t, 0}, \quad G _ {2} ^ {0} (s) = \Psi_ {0, s} (D _ {s} F _ {s} ^ {\mathrm{T}} + P _ {s} C _ {s} ^ {\mathrm{T}}) (F _ {s} F _ {s} ^ {\mathrm{T}}) ^ {- 1}.$$

由于 $\| \Psi_{0,s}\|$ 及 $\| P_s\|$ 在 $[0,T_f]$ 上有界，所以，

$$\int_ {0} ^ {T _ {f}} \| G _ {2} ^ {0} (s) F _ {s} \| ^ {2} \mathrm{d} s < \infty , \quad \int_ {0} ^ {T _ {f}} \| G _ {2} ^ {0} (s) C _ {s} \| \mathrm{d} s < \infty .$$

这验证了 $G_{t}$ 中要求的可积条件得到满足.

从式 (4.4.60) 及 $G_{2}^{0}(s)$ 的表达式，知 $H_{t} = \Psi_{t,0}$ ，所以为使 (4.4.67) 成立，必须取

$$c _ {t} = c _ {t} ^ {0} \stackrel {\text { def }} {=} \Psi_ {t, 0} (E x _ {0} - R _ {x _ {0} y _ {0}} R _ {y _ {0}} ^ {+} E y _ {0}),G _ {0} (t) = G _ {0} ^ {0} (t) \stackrel {\text { def }} {=} \Psi_ {t, 0} R _ {x _ {0} y _ {0}} R _ {y _ {0}} ^ {+}.$$

由此从式 (4.4.60) 立即看出无偏性

$$E (x _ {t} - \hat {x} _ {0} ^ {G}) = H _ {t} E x _ {0} - c _ {t} ^ {0} - G _ {0} ^ {0} (t) E y _ {0} = 0.$$

把最优加权代入 $\hat{x}_t^G$ 的表达式后，知线性无偏最小方差估计为
