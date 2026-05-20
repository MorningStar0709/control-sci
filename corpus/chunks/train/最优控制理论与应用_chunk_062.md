$$\boldsymbol {X} (t) - \boldsymbol {X} ^ {*} (t _ {1} - \varepsilon) = \int_ {t _ {1} - \varepsilon} ^ {t} \boldsymbol {f} (\boldsymbol {X}, \boldsymbol {U} ^ {*} + \delta \boldsymbol {U}, t) d t$$

两式相减,可得这一段的 $\delta X(t)$

$$\delta \boldsymbol {X} (t) = \int_ {t _ {1} - \varepsilon} ^ {t} [ \boldsymbol {f} (\boldsymbol {X}, \boldsymbol {U} ^ {*} + \delta \boldsymbol {U}, t) - \boldsymbol {f} (\boldsymbol {X} ^ {*}, \boldsymbol {U} ^ {*}, t) ] d t \tag {4-6}$$

可以对 $\delta X(t)$ 的大小作估计

$$\left| \delta X (t) \right| \leqslant \max _ {t _ {1} - \varepsilon \leqslant t \leqslant t _ {1}} \left| f (X, U ^ {*} + \delta U, t) - f (X ^ {*}, U ^ {*}, t) \right| (t - t _ {1} + \varepsilon)$$

由于 $\varepsilon$ 是微量, 所以 $\delta X(t)$ 也是微量, 因而在精确到一阶微量的情况下, 下式成立

$$\boldsymbol {f} (\boldsymbol {X}, \boldsymbol {U} ^ {*} + \delta \boldsymbol {U}) = \boldsymbol {f} (\boldsymbol {X} ^ {*}, \boldsymbol {U} ^ {*} + \delta \boldsymbol {U}) + \frac {\partial \boldsymbol {f}}{\partial \boldsymbol {X}} \Bigg | _ {\boldsymbol {X} = \boldsymbol {X} ^ {*}} \delta \boldsymbol {X} \tag {4-7}$$

将式(4-7)代入式(4-6)，并注意到微量 $\delta X$ 在微小时间间隔上的积分是高阶微量，即得

$$\delta \boldsymbol {X} (t) = \int_ {t _ {1} - \varepsilon} ^ {t} [ \boldsymbol {f} (\boldsymbol {X} ^ {*}, \boldsymbol {U} ^ {*} + \delta \boldsymbol {U}, t) - \boldsymbol {f} (\boldsymbol {X} ^ {*}, \boldsymbol {U} ^ {*}, t) ] d t$$

在第二段时间间隔得终点 $t = t_{1}$ ，则有

$$\delta \boldsymbol {X} (t _ {1}) = \int_ {t _ {1} - \varepsilon} ^ {t _ {1}} [ \boldsymbol {f} (\boldsymbol {X} ^ {*}, \boldsymbol {U} ^ {*} + \delta \boldsymbol {U}, t) - \boldsymbol {f} (\boldsymbol {X} ^ {*}, \boldsymbol {U} ^ {*}, t) ] d t$$

或

$$\delta \boldsymbol {X} (t _ {1}) = [ \boldsymbol {f} (\boldsymbol {X} ^ {*}, \boldsymbol {U} ^ {*} + \delta \boldsymbol {U}, t) - \boldsymbol {f} (\boldsymbol {X} ^ {*}, \boldsymbol {U} ^ {*}, t) ] | _ {t = t _ {1}} \varepsilon + o (\varepsilon) \tag {4-8}$$

其中 $o(\varepsilon)$ 表示二阶以上的微量。

(3) $t_1 \leqslant t \leqslant t_f$

这时又有 $U = U^{*}$ ，系统的状态方程为

$$\dot {\boldsymbol {X}} = \boldsymbol {f} (\boldsymbol {X}, \boldsymbol {U} ^ {*}, t)$$

而状态变量的变分 $\delta X(t)$ 满足方程

$$\delta \dot {\boldsymbol {X}} = \frac {\partial \boldsymbol {f}}{\partial \boldsymbol {X}} \Bigg | _ {\boldsymbol {U} = \boldsymbol {U} ^ {*}} \delta \boldsymbol {X} \tag {4-9}$$

引入变量 $\lambda^{*}(t)$ 及哈密顿函数 H
