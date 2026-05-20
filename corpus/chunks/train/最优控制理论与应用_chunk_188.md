$$
\begin{array}{l} \boldsymbol {c} ^ {\mathrm{T}} \boldsymbol {x} \left(t _ {\mathrm{f}}\right) + \int_ {t _ {0}} ^ {t _ {\mathrm{f}}} \left\{\left[ \boldsymbol {p} ^ {\mathrm{T}} (t) \boldsymbol {x} (t) + L _ {1} (\boldsymbol {u}, t) + L _ {2} \left(\boldsymbol {v} ^ {*}, t\right) \right] - \right. \\ L _ {1} (\boldsymbol {u}, t) - L _ {2} \left(\boldsymbol {v} ^ {*}, t\right) - \boldsymbol {p} ^ {\mathrm{T}} (t) \boldsymbol {x} ^ {*} (t) - \\ \boldsymbol {\lambda} ^ {T} (t) [ \boldsymbol {A} (t) \boldsymbol {x} ^ {*} (t) + f _ {1} (\boldsymbol {u}, t) + f _ {2} (\boldsymbol {v} ^ {*}, t) ] \rbrace d t \\ \end{array}
= \boldsymbol {c} ^ {\mathrm{T}} \boldsymbol {x} ^ {*} (t _ {\mathrm{f}}) + \int_ {t _ {0}} ^ {t _ {\mathrm{f}}} \left\{\left[ \boldsymbol {p} ^ {\mathrm{T}} (t) \boldsymbol {x} ^ {*} (t) + L _ {1} (\boldsymbol {u} ^ {*}, t) + \right. \right.\left. \left. L _ {2} \left(\boldsymbol {v} ^ {*}, t\right) \right] - L _ {1} \left(\boldsymbol {u} ^ {*}, t\right) - L _ {2} \left(\boldsymbol {v} ^ {*}, t\right) - \right.\boldsymbol {\lambda} ^ {T} (t) \left[ \boldsymbol {A} (t) \boldsymbol {x} ^ {*} (t) + f _ {1} \left(\boldsymbol {u} ^ {*}, t\right) + f _ {2} \left(\boldsymbol {v} ^ {*}, t\right) \right] \rbrace d t
$$

将式 $(10-58)$ 与式 $(10-60)$ 代入上式,得

$$J [ \boldsymbol {u}, \boldsymbol {v} ^ {*} ] - \int_ {t _ {0}} ^ {t _ {f}} H (\boldsymbol {x} ^ {*}, \boldsymbol {u}, \boldsymbol {v} ^ {*}, \boldsymbol {\lambda}, t) d t= J \left[ \boldsymbol {u} ^ {*}, \boldsymbol {v} ^ {*} \right] - \int_ {t _ {0}} ^ {t _ {\mathrm{f}}} H \left(\boldsymbol {x} ^ {*}, \boldsymbol {u} ^ {*}, \boldsymbol {v} ^ {*}, \boldsymbol {\lambda}, t\right) \mathrm{d} t$$

注意到式(10-61)，可得

$$J \left[ \boldsymbol {u} ^ {*}, \boldsymbol {v} ^ {*} \right] \leqslant J \left[ \boldsymbol {u}, \boldsymbol {v} ^ {*} \right] \tag {10-64}$$

同理, 若任取 $v \in V$ , 记状态方程相对于 $(u^{*}, v)$ 的解为 $x(t)$ , 则可以推得

$$J \left[ u ^ {*}, v ^ {*} \right] \geqslant J \left[ u ^ {*}, v \right] \tag {10-65}$$

式(10-65)和(10-66)说明鞍点条件式(10-21)成立, $(u^{*},v^{*})$ 确实是最优策略,充分性得证。

例10-3 加速度有限时的追-逃问题

设追逐者的控制量是它的加速度 $a_{p}(t)$ ，它垂直于指向逃逸者的初始视线。逃逸者的控制量为 $a_{e}(t)$ ，它也垂直于初始视线。设 $y(t)$ 是垂直于初始视线的追-逃者之间的相对位置， $v_{y}$ 为其相对速度（见图10-5）。则相对运动的微分方程为

$$
\left\{ \begin{array}{r l} \dot {y} & = v _ {y} \quad y (t _ {0}) = 0 \\ \ddot {y} & = \dot {v} _ {y} = a _ {p} - a _ {e} \quad v _ {y} (t _ {0}) = v _ {0} \end{array} \right. \tag {10-66}
$$
