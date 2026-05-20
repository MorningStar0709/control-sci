# 3.3.1 终端时刻 $t_{\mathrm{f}}$ 给定，终端状态 $X(t_{\mathrm{f}})$ 自由

将状态方程(3-13)写成等式约束方程的形式

$$\boldsymbol {f} (\boldsymbol {X}, \boldsymbol {U}, t) - \dot {\boldsymbol {X}} (t) = 0 \tag {3-15}$$

与有约束条件的函数极值情况类似,引入待定的 n 维拉格朗日乘子向量函数

$$\boldsymbol {\lambda} ^ {T} (t) = \left[ \lambda_ {1} (t), \lambda_ {2} (t), \dots , \lambda_ {n} (t) \right] \tag {3-16}$$

与以前不同的是，在动态问题中拉格朗日乘子向量 $\boldsymbol{\lambda}(t)$ 是时间函数。在最优控制中经常将 $\boldsymbol{\lambda}(t)$ 称为伴随变量，协态（协状态向量）或共轭状态。引入 $\boldsymbol{\lambda}(t)$ 后可作出下面的增广泛函

$$J _ {\mathrm{a}} = \phi [ \boldsymbol {X} (t _ {\mathrm{f}}), t _ {\mathrm{f}} ] + \int_ {t _ {0}} ^ {t _ {\mathrm{f}}} \left\{\boldsymbol {F} [ \boldsymbol {X}, \boldsymbol {U}, t ] + \boldsymbol {\lambda} ^ {\mathrm{T}} (t) [ \boldsymbol {f} (\boldsymbol {X}, \boldsymbol {U}, t) - \dot {\boldsymbol {X}} ] \right\} \mathrm{d} t \tag {3-17}$$

于是有约束条件的泛函 J 的极值问题化为无约束条件的增广泛函 $J_{a}$ 的极值问题。

再引入一个标量函数

$$H (\boldsymbol {X}, \boldsymbol {U}, \boldsymbol {\lambda}, t) = F (\boldsymbol {X}, \boldsymbol {U}, t) + \boldsymbol {\lambda} ^ {\mathrm{T}} \boldsymbol {f} (\boldsymbol {X}, \boldsymbol {U}, t) \tag {3-18}$$

它称为哈密顿(Hamilton)函数,在最优控制中起着重要的作用。于是 $J_{a}$ 可写成

$$J _ {\mathrm{a}} = \phi [ \boldsymbol {X} (t _ {\mathrm{f}}), t _ {\mathrm{f}} ] + \int_ {t _ {0}} ^ {t _ {\mathrm{f}}} [ H (\boldsymbol {X}, \boldsymbol {U}, \boldsymbol {\lambda}, t) - \boldsymbol {\lambda} ^ {\mathrm{T}} \dot {\boldsymbol {X}} ] \mathrm{d} t$$

对上式积分号内第二项作分部积分后可得

$$J _ {\mathrm{a}} = \phi [ \boldsymbol {X} (t _ {\mathrm{f}}), t _ {\mathrm{f}} ] - \boldsymbol {\lambda} ^ {\mathrm{T}} (t _ {\mathrm{f}}) \boldsymbol {X} (t _ {\mathrm{f}}) + \boldsymbol {\lambda} ^ {\mathrm{T}} (t _ {0}) \boldsymbol {X} (t _ {0}) +\int_ {t _ {0}} ^ {t _ {f}} \left[ H (\boldsymbol {X}, \boldsymbol {U}, \boldsymbol {\lambda}, t) + \boldsymbol {\lambda} ^ {\mathrm{T}} \boldsymbol {X} \right] \mathrm{d} t \tag {3-19}$$

设 $X(t), U(t)$ 相对于最优值 $X^{*}(t), \dot{U}^{*}(t)$ 的变分分别为 $\delta X(t)$ 和 $\delta U(t)$ ，因为 $X(t_{\mathrm{f}})$ 自由，故还要考虑变分 $\delta X(t_{\mathrm{f}})$ 。下面来计算由这些变分引起的泛函 $J_{\mathrm{a}}$ 的变分 $\delta J_{\mathrm{a}}$
