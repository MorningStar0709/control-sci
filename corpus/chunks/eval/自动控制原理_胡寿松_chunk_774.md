$$
\begin{array}{l} \Delta J = \int_ {t _ {0}} ^ {t _ {f} + \delta t _ {f}} L \left(\boldsymbol {x} ^ {*} + \delta \boldsymbol {x}, \dot {\boldsymbol {x}} ^ {*} + \delta \dot {\boldsymbol {x}}, t\right) d t - \int_ {t _ {0}} ^ {t _ {f}} L \left(\boldsymbol {x} ^ {*}, \dot {\boldsymbol {x}} ^ {*}, t\right) d t \\ = \int_ {t _ {f}} ^ {t _ {f} + \delta t _ {f}} L \left(\boldsymbol {x} ^ {*} + \delta \boldsymbol {x}, \dot {\boldsymbol {x}} ^ {*} + \delta \dot {\boldsymbol {x}}, t\right) d t \\ + \int_ {t _ {0}} ^ {t _ {f}} \left[ L \left(\boldsymbol {x} ^ {*} + \delta \boldsymbol {x}, \dot {\boldsymbol {x}} ^ {*} + \delta \dot {\boldsymbol {x}}, t\right) - L \left(\boldsymbol {x} ^ {*}, \dot {\boldsymbol {x}} ^ {*}, t\right) \right] d t \tag {10-30} \\ \end{array}
$$

对于式(10-30)右端第一项,根据积分中值定理可得

$$\int_ {t _ {f}} ^ {t _ {f} + \delta t _ {f}} L \left(\boldsymbol {x} ^ {*} + \delta \boldsymbol {x}, \dot {\boldsymbol {x}} ^ {*} + \delta \dot {\boldsymbol {x}}, t\right) d t = L \left(\boldsymbol {x} ^ {*} + \delta \boldsymbol {x}, \dot {\boldsymbol {x}} ^ {*} + \delta \dot {\boldsymbol {x}}, t\right) | _ {t = t _ {f} + \theta \otimes t _ {f}} \delta t _ {f}$$

式中， $0 < \theta < 1$ 。由于函数 $L(\cdot)$ 是连续的，因而

$$L \left(\boldsymbol {x} ^ {*} + \delta \boldsymbol {x}, \dot {\boldsymbol {x}} ^ {*} + \delta \dot {\boldsymbol {x}}, t\right) \mid_ {t = t _ {f} + \theta \otimes t _ {f}} = L \left(\boldsymbol {x} ^ {*}, \dot {\boldsymbol {x}} ^ {*}, t\right) \mid_ {t _ {f}} + \varepsilon_ {1}$$

式中 $\varepsilon_{1}\rightarrow 0$ ，故有

$$\int_ {t _ {f}} ^ {t _ {f} + \delta t _ {f}} L \left(\boldsymbol {x} ^ {*} + \delta \boldsymbol {x}, \dot {\boldsymbol {x}} ^ {*} + \delta \dot {\boldsymbol {x}}, t\right) d t = L \left(\boldsymbol {x} ^ {*}, \dot {\boldsymbol {x}} ^ {*}, t\right) \mid_ {t _ {f}} \delta t _ {f} + \varepsilon_ {1} \delta t _ {f} \tag {10-31}$$

对于式(10-30)右端第二项,将被积函数在极值轨线处展成泰勒级数,有

$$
\begin{array}{l} \int_ {t _ {0}} ^ {t _ {f}} \left[ L \left(\boldsymbol {x} ^ {*} + \delta \boldsymbol {x}, \dot {\boldsymbol {x}} ^ {*} + \delta \dot {\boldsymbol {x}}, t\right) - L \left(\boldsymbol {x} ^ {*}, \dot {\boldsymbol {x}} ^ {*}, t\right) \right] d t \\ = \int_ {t _ {0}} ^ {t _ {f}} \left[ \left(\frac {\partial L}{\partial \boldsymbol {x}}\right) ^ {T} \delta \boldsymbol {x} + \left(\frac {\partial L}{\partial \dot {\boldsymbol {x}}}\right) ^ {T} \delta \dot {\boldsymbol {x}} + H O T \right] d t \tag {10-32} \\ \end{array}
$$

取上式右端中第二项进行分部积分,得
