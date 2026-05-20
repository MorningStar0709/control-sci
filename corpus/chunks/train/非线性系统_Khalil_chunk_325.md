$$\varepsilon \dot {v} _ {1} = \frac {\varepsilon}{C R} (E - v _ {1}) - \frac {\varepsilon}{C} \psi (v _ {1}) - \frac {1}{C} (v _ {1} - v _ {2})\varepsilon \dot {v} _ {2} = \frac {\varepsilon}{C R} (E - v _ {2}) - \frac {\varepsilon}{C} \psi (v _ {2}) - \frac {1}{C} (v _ {2} - v _ {1})$$

若上述模型具有方程(11.1)\~方程(11.2)的形式,则 $v_{1}$ 和 $v_{2}$ 应被看成 z 变量,方程(11.3)应为

$$v _ {1} - v _ {2} = 0$$

然而,这个方程的根不是孤立的,这违反了方程(11.3)的根应孤立的基本假设。因此如果以 $v_{1}$ 和 $v_{2}$ 作为z变量,则模型不是标准形式。现在试选择其他状态变量,取①

$$x = \frac {1}{2} (v _ {1} + v _ {2}); \quad z = \frac {1}{2} (v _ {1} - v _ {2})$$

采用新变量的状态方程为

$$\dot {x} = \frac {1}{C R} (E - x) - \frac {1}{2 C} [ \psi (x + z) + \psi (x - z) ]\varepsilon \dot {z} = - \left(\frac {\varepsilon}{C R} + \frac {2}{C}\right) z - \frac {\varepsilon}{2 C} [ \psi (x + z) - \psi (x - z) ]$$

现在方程(11.3)的唯一根为 z=0，由此得降价模型为

$$\dot {x} = \frac {1}{C R} (E - x) - \frac {1}{C} \psi (x)$$

该模型表示图11.3的简化电路，其中每对相似的并联支路由一个等效的单个支路代替。为了获得无量纲参数 $\varepsilon$ ，对 $x,z$ 和 $\psi$ 进行归一化

$$x _ {r} = \frac {x}{E}; \quad z _ {r} = \frac {z}{E}; \quad \psi_ {r} (v) = \frac {R}{E} \psi (E v)$$

并把时间变量归一化为 $t_r = t / CR$ ，得奇异扰动模型

$$\frac {d x _ {r}}{d t _ {r}} = 1 - x _ {r} - \frac {1}{2} \left[ \psi_ {r} \left(x _ {r} + z _ {r}\right) + \psi_ {r} \left(x _ {r} - z _ {r}\right) \right]\varepsilon \frac {d z _ {r}}{d t _ {r}} = - (\varepsilon + 2) z _ {r} - \frac {\varepsilon}{2} \left[ \psi_ {r} \left(x _ {r} + z _ {r}\right) - \psi_ {r} \left(x _ {r} - z _ {r}\right) \right]$$

其中 $\varepsilon = R_{c}/R$ 是无量纲的。

![](image/b2f856775c37ef51394d028f97d8bbc2eb6ef6bd96ff1662bf054e822c97c333.jpg)

<details>
<summary>text_image</summary>

R/2
E
+
v
-
2C
2ψ(v)
</details>

图11.3 在 $R_{c} = 0$ 时的简化电路

例11.4 汽车悬挂的quarter-car模型如图11.4所示,其中 $m_{s}$ 和 $m_{u}$ 是车体和轮胎的质量, $k_{s}$ 和 $k_{t}$ 是支架和轮胎的弹簧系数, $b_{s}$ 是减震(减震器)常数。 $F$ 是由一个强制驱动装置产生的力,该装置用于主动和半主动悬挂,当 $F = 0$ 时为传统的被动悬挂。 $d_{s}, d_{u}$ 和 $d_{r}$ 分别是车厢、轮胎和公路表面距参考点的高度。根据牛顿定律,作用于 $m_{s}$ 和 $m_{u}$ 的力是平衡的,

从而有方程

$$m _ {s} \ddot {d} _ {s} + b _ {s} (\dot {d} _ {s} - \dot {d} _ {u}) + k _ {s} (d _ {s} - d _ {u}) = Fm _ {u} \ddot {d} _ {u} + b _ {s} (\dot {d} _ {u} - \dot {d} _ {s}) + k _ {s} (d _ {u} - d _ {s}) + k _ {t} (d _ {u} - d _ {r}) = - F$$

典型汽车轮胎的固有频率 $\sqrt{k_{t}/m_{u}}$ 大约是车体和支架固有频率 $\sqrt{k_{s}/m_{s}}$ 的 10 倍。因此，定义参数

$$\varepsilon = \sqrt {\frac {k _ {s} / m _ {s}}{k _ {t} / m _ {u}}} = \sqrt {\frac {k _ {s} m _ {u}}{k _ {t} m _ {s}}}$$
