# (3) 单位加速度输入时的稳态误差

当系统输入为单位加速度函数 $r(t) = t^2 / 2$ 时，其 $z$ 变换函数

$$R (z) = \frac {T ^ {2} z (z + 1)}{2 (z - 1) ^ {3}}$$

因而稳态误差为

$$e _ {s} (\infty) = \lim _ {z \rightarrow 1} \frac {T ^ {2} (z + 1)}{2 (z - 1) ^ {2} [ 1 + G (z) ]} = \frac {T ^ {2}}{\lim _ {z \rightarrow 1} (z - 1) ^ {2} G (z)} = \frac {T ^ {2}}{K _ {a}} \tag {7-83}$$

当然，上式也是系统的稳态位置误差，并称为加速度误差。式中

$$K _ {a} = \lim _ {z \rightarrow 1} (z - 1) ^ {2} G (z) \tag {7-84}$$

称为静态加速度误差系数。由于0型及I型系统的 $K_{a}=0$ ，II型系统的 $K_{a}$ 为常值，III型及III型以上系统的 $K_{a}=\infty$ ，因此有如下结论成立：

0型及I型离散系统不能承受单位加速度函数作用，II型离散系统在单位加速度函数作用下存在加速度误差，只有III型及III型以上的离散系统在单位加速度函数作用下，才不存在采样瞬时的稳态位置误差。

不同型别单位反馈离散系统的稳态误差,见表 7-5。

表 7-5 单位反馈离散系统的稳态误差

<table><tr><td>系统型别</td><td>位置误差r(t)=1(t)</td><td>速度误差r(t)=t</td><td>加速度误差r(t)= $\frac{1}{2}t^2$ </td></tr><tr><td>0型</td><td> $\frac{1}{K_p}$ </td><td>∞</td><td>∞</td></tr><tr><td>I型</td><td>0</td><td> $\frac{T}{K_v}$ </td><td>∞</td></tr><tr><td>II型</td><td>0</td><td>0</td><td> $\frac{T^2}{K_a}$ </td></tr><tr><td>III型</td><td>0</td><td>0</td><td>0</td></tr></table>
