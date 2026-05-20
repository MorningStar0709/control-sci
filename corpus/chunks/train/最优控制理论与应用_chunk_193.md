# 10.5 线性二次微分对策

考虑追逐、逃逸双方各自的线性状态方程为

$$\dot {\boldsymbol {x}} _ {\mathrm{e}} = \boldsymbol {A} _ {\mathrm{e}} (t) \boldsymbol {x} _ {\mathrm{e}} + \boldsymbol {B} _ {\mathrm{e}} (t) \boldsymbol {v}, \boldsymbol {x} _ {\mathrm{e}} \left(t _ {0}\right) = \boldsymbol {x} _ {\mathrm{e} 0} \tag {10-88}\dot {\boldsymbol {x}} _ {\mathrm{p}} = \boldsymbol {A} _ {\mathrm{p}} (t) \boldsymbol {x} _ {\mathrm{p}} + \boldsymbol {B} _ {\mathrm{p}} (t) \boldsymbol {u}, \boldsymbol {x} _ {\mathrm{p}} \left(t _ {0}\right) = \boldsymbol {x} _ {\mathrm{p} 0} \tag {10-89}$$

式中，下标 p、e 代表追逐者(pursuer)和逃逸者(evader)。追逐者利用控制 $\boldsymbol{u}(t)$ 力图捕获逃逸者，而逃逸者利用控制 $\boldsymbol{v}(t)$ 力图避免被捕获。这就是说，追逐者要使终端脱靶量最小，而逃逸者则要使它最大。脱靶量用加权二次型给出为

$$\left[ \boldsymbol {x} _ {\mathrm{p}} \left(t _ {\mathrm{f}}\right) - \boldsymbol {x} _ {\mathrm{e}} \left(t _ {\mathrm{f}}\right) \right] ^ {\mathrm{T}} \boldsymbol {F} ^ {\mathrm{T}} \boldsymbol {F} \left[ \boldsymbol {x} _ {\mathrm{p}} \left(t _ {\mathrm{f}}\right) - \boldsymbol {x} _ {\mathrm{e}} \left(t _ {\mathrm{f}}\right) \right] \tag {10-90}$$

另一方面，设控制变量服从下面的积分二次约束

$$\int_ {t _ {0}} ^ {t _ {\mathrm{f}}} \boldsymbol {u} ^ {\mathrm{T}} \boldsymbol {R} _ {\mathrm{p}} \boldsymbol {u} \mathrm{d} t \leqslant E _ {\mathrm{p}} \tag {10-91}\int_ {t _ {0}} ^ {t _ {\mathrm{f}}} \boldsymbol {v} ^ {\mathrm{T}} \boldsymbol {R} _ {\mathrm{e}} \boldsymbol {v} \mathrm{d} t \leqslant E _ {\mathrm{e}} \tag {10-92}$$

在追逐一逃逸过程中,双方都要使用他们能用的一切控制量,因此约束式(10-91)、(10-92)应取等式。将式(10-90)、(10-91)、(10-92)组合起来可得下面的性能指标

$$J (\boldsymbol {u}, \boldsymbol {v}) = \frac {1}{2} \left[ \boldsymbol {x} _ {\mathrm{p}} \left(t _ {\mathrm{f}}\right) - \boldsymbol {x} _ {\mathrm{e}} \left(t _ {\mathrm{f}}\right) \right] ^ {\mathrm{T}} \boldsymbol {F} ^ {\mathrm{T}} \boldsymbol {F} \left[ \boldsymbol {x} _ {\mathrm{p}} \left(t _ {\mathrm{f}}\right) - \boldsymbol {x} _ {\mathrm{e}} \left(t _ {\mathrm{f}}\right) \right] +\frac {1}{2} \int_ {t _ {0}} ^ {t _ {\mathrm{f}}} \left[ \boldsymbol {u} ^ {\mathrm{T}} (t) \boldsymbol {R} _ {\mathrm{p}} (t) \boldsymbol {u} (t) - \boldsymbol {v} ^ {\mathrm{T}} (t) \boldsymbol {R} _ {\mathrm{e}} (t) \boldsymbol {v} (t) \right] \mathrm{d} t \tag {10-93}$$

其中 F 阵非奇异, $R_{\mathrm{p}}(t) > 0$ , $R_{\mathrm{e}}(t) > 0$ 。
