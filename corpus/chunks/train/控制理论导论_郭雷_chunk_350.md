$$\mathrm{d} \hat {x} _ {t} = A _ {t} (y) \hat {x} _ {t} \mathrm{d} t + B _ {t} u _ {t} (y) \mathrm{d} t+ \left(D _ {t} (y) F _ {t} ^ {\mathrm{T}} (y) + P _ {t} C _ {t} ^ {\mathrm{T}} (y)\right) \left(F _ {t} (y) F _ {t} ^ {\mathrm{T}} (y)\right) ^ {- 1} \left(\mathrm{d} y _ {t} - c _ {t} \hat {x} _ {t} \mathrm{d} t\right), \tag {4.4.74}\dot {P} _ {t} = P _ {t} A _ {t} ^ {\mathrm{T}} (y) + A _ {t} (y) P _ {t} + D _ {t} (y) D _ {t} ^ {\mathrm{T}} (y) - \left(D _ {t} (y) F _ {t} ^ {\mathrm{T}} (y) \right.+ P _ {t} C _ {t} ^ {\mathrm{T}} (y)) \left(F _ {t} (y) F _ {t} ^ {\mathrm{T}} (y)\right) ^ {- 1} \left(D _ {t} (y) F _ {t} ^ {\mathrm{T}} (y) + P _ {t} C _ {t} ^ {\mathrm{T}} (y)\right) ^ {\mathrm{T}}, \tag {4.4.75}\hat {x} _ {0} = E (x _ {0} | y _ {0}), \quad P _ {0} = R _ {x _ {0} | y _ {0}}.$$

当系数阵 $A_{t}, D_{t}, C_{t}, F_{t}$ 不依赖于量测，而是确定性阵时，

$$\mathrm{d} x _ {t} = A _ {t} x _ {t} \mathrm{d} t + B _ {t} u _ {t} \mathrm{d} t + D _ {t} \mathrm{d} w _ {t}, \tag {4.4.76}\mathrm{d} y _ {t} = C _ {t} x _ {t} \mathrm{d} t + F _ {t} \mathrm{d} w _ {t}, \tag {4.4.77}$$

则式 (4.4.75) 所给出的 $P_{t}$ 是确定性的。这时 Riccati 方程

$$- \dot {S} _ {t} = A _ {t} ^ {\mathrm{T}} S _ {t} + S _ {t} A _ {t} + Q _ {1} (t) - S _ {t} B _ {t} Q _ {2} ^ {- 1} (t) B _ {t} ^ {\mathrm{T}} S _ {t}, \quad S _ {T} = Q _ {0} \tag {4.4.78}$$

对任意对称非负定的 $Q_0, Q_1(t)$ 及正定的 $Q_2(t)$ 有唯一解，其解也是确定性的.

对系统 (4.4.76)\~(4.4.77) 在二次性能指标

$$E J (u) = E \left\{x _ {T _ {f}} ^ {\mathrm{T}} Q _ {0} x _ {T _ {f}} + \int_ {0} ^ {T _ {f}} (x _ {t} ^ {\mathrm{T}} Q _ {1} (t) x _ {t} + u _ {2} ^ {\mathrm{T}} Q _ {2} (t) u _ {2}) \mathrm{d} t \right\}Q _ {0} \geqslant 0, \quad Q _ {1} (t) \geqslant 0, \quad Q _ {2} (t) > 0$$

下的最优随机控制为

$$u _ {t} ^ {0} \stackrel {\text { def }} {=} L _ {t} \hat {x} _ {t}, \quad L _ {t} = - Q _ {2} ^ {- 1} (t) B _ {t} ^ {\mathrm{T}} S _ {t},$$

其中 $\hat{x}_t = E(x_t|\mathcal{F}_t^y)$ 由式(4.4.74)，(4.4.75)给出.

以上结果和离散时间系统是平行的.
