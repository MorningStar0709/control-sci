# 3.3.2 终端时刻 $t_{f}$ 自由, 终端状态 $X(t_{f})$ 受约束

设终端状态 $X(t_{t})$ 满足下面约束方程

$$\boldsymbol {G} \left[ \boldsymbol {X} (t _ {\mathrm{f}}), t _ {\mathrm{f}} \right] = 0 \tag {3-44}$$

其中

$$
\boldsymbol {G} = \left[ \begin{array}{c} G _ {1} \left[ \boldsymbol {X} \left(t _ {\mathrm{f}}\right), t _ {\mathrm{f}} \right] \\ G _ {2} \left[ \boldsymbol {X} \left(t _ {\mathrm{f}}\right), t _ {\mathrm{f}} \right] \\ \dots \dots \\ G _ {q} \left[ \boldsymbol {X} \left(t _ {\mathrm{f}}\right), t _ {\mathrm{f}} \right] \end{array} \right] \tag {3-45}
$$

性能指标为

$$J = \phi [ X (t _ {f}), t _ {f} ] + \int_ {t _ {0}} ^ {t _ {f}} F [ X (t), U (t), t ] \mathrm{d} t \tag {3-46}$$

引入 n 维拉格朗日乘子向量函数 $\boldsymbol{\lambda}(t)$ 和 q 维拉格朗日乘子向量 v，作出增广性能泛函

$$J _ {\mathrm{a}} = \phi [ \boldsymbol {X} (t _ {\mathrm{f}}), t _ {\mathrm{f}} ] + \boldsymbol {v} ^ {\mathrm{T}} \boldsymbol {G} [ \boldsymbol {X} (t _ {\mathrm{f}}), t _ {\mathrm{f}} ] +\int_ {t _ {0}} ^ {t _ {\mathrm{f}}} \left\{F (\boldsymbol {X}, \boldsymbol {U}, t) + \boldsymbol {\lambda} ^ {\mathrm{T}} (t) [ \boldsymbol {f} (\boldsymbol {X}, \boldsymbol {U}, t) - \dot {\boldsymbol {X}} ] \right\} \mathrm{d} t \quad (3 - 4 7)$$

引入哈密顿函数

$$H (\boldsymbol {X}, \boldsymbol {U}, \boldsymbol {\lambda}, t) = F [ \boldsymbol {X}, \boldsymbol {U}, t ] + \boldsymbol {\lambda} ^ {\mathrm{T}} \boldsymbol {f} (\boldsymbol {X}, \boldsymbol {U}, t) \tag {3-48}$$

将 $H$ 代入式(3-47)，可得

$$J _ {\mathrm{a}} = \phi [ \boldsymbol {X} (t _ {\mathrm{f}}), t _ {\mathrm{f}} ] + \boldsymbol {v} ^ {\mathrm{T}} \boldsymbol {G} [ \boldsymbol {X} (t _ {\mathrm{f}}), t _ {\mathrm{f}} ] + \int_ {t _ {0}} ^ {t _ {\mathrm{f}}} [ \dot {H} (\boldsymbol {X}, \boldsymbol {U}, \boldsymbol {\lambda}, t) - \boldsymbol {\lambda} ^ {\mathrm{T}} \dot {\boldsymbol {X}} ] \mathrm{d} t \tag {3-49}$$

令

$$\theta \left[ X (t _ {\mathrm{f}}), t _ {\mathrm{f}} \right] = \phi \left[ X (t _ {\mathrm{f}}), t _ {\mathrm{f}} \right] + \boldsymbol {v} ^ {\mathrm{T}} \boldsymbol {G} \left[ X (t _ {\mathrm{f}}), t _ {\mathrm{f}} \right] \tag {3-50}$$

则

$$J _ {\mathrm{a}} = \theta [ \boldsymbol {X} (t _ {\mathrm{f}}), t _ {\mathrm{f}} ] + \int_ {t _ {0}} ^ {t _ {\mathrm{f}}} [ H (\boldsymbol {X}, \boldsymbol {U}, \boldsymbol {\lambda}, t) - \boldsymbol {\lambda} ^ {\mathrm{T}} \dot {\boldsymbol {X}} ] \mathrm{d} t \tag {3-51}$$
