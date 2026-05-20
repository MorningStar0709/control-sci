![](image/8263ae3e4d45fdabee59ce7bd00119782cbc74b9b19c42ee8fecf1e5290dece9.jpg)

<details>
<summary>text_image</summary>

V
θ
mg
y
H
</details>

图1.24 习题1.15的倒摆

1.16 图1.25是一个带有旋转制动装置的平移振荡器系统[205]示意图。该系统是一个用线性弹簧连接到固定参考框架上的物体 $M$ 的平台，弹簧系数为 $k$ ，平台只可以在平行于弹簧轴线的水平面运动，在平台上有一个由直流电机驱动的检测质量，其质量为 $m$ ，对其质心的转动惯量为 $I$ ，质心到转轴的距离为 $L$ ，加于检测质量的控制力矩用 $\pmb{u}$ 表示。旋转的检测质量产生一个可控制的力，使平台的平衡运动衰减。忽略摩擦力，可推导出该系统的模型。图1.25所示为检测质量受到的力 $F_{x}, F_{y}$ 及力矩 $\pmb{u}$ 。写出质心的牛顿运动定律方程及其质心的力矩方程，有

$$m \frac {d ^ {2}}{d t ^ {2}} (x _ {c} + L \sin \theta) = F _ {x}, m \frac {d ^ {2}}{d t ^ {2}} (L \cos \theta) = F _ {y}, I \ddot {\theta} = u + F _ {y} L \sin \theta - F _ {x} L \cos \theta$$

其中, $\theta$ 为检测质量转角位置(逆时针测量),平台在反方向及在弹簧恢复力方向的受力为 $F_{x}$ 和 $F_{y}$ ,写出平台的牛顿定律方程为

$$M \ddot {x} _ {c} = - F _ {x} - k x _ {c}$$

$x_{c}$ 是平台的平衡位置。

(a) 运用给定的微分法消去 $F_{x}$ 和 $F_{y}$ ，证明运动方程可简化为

$$
D (\theta) \left[ \begin{array}{c} {\ddot {\theta}} \\ {\ddot {x} _ {c}} \end{array} \right] = \left[ \begin{array}{c} {u} \\ {m L \dot {\theta} ^ {2} \sin \theta - k x _ {c}} \end{array} \right], \text {其中} D (\theta) = \left[ \begin{array}{c c} {I + m L ^ {2}} & {m L \cos \theta} \\ {m L \cos \theta} & {M + m} \end{array} \right]
$$

(b) 对于 $\ddot{\theta}$ 和 $\ddot{x}_{c}$ 解上面的方程, 证明

$$
\left[ \begin{array}{l} \ddot {\theta} \\ \ddot {x} _ {c} \end{array} \right] = \frac {1}{\Delta (\theta)} \left[ \begin{array}{l l l} m + M & & - m L \cos \theta \\ - m L \cos \theta & & I + m L ^ {2} \end{array} \right] \left[ \begin{array}{l} u \\ m L \dot {\theta} ^ {2} \sin \theta - k x _ {c} \end{array} \right]
$$

其中， $\Delta (\theta) = (I + mL^2)(m + M) - m^2 L^2\cos^2\theta \geqslant (I + mL^2)M + mI > 0$

（c）用 $x_{1}=\theta, x_{2}=\dot{\theta}, x_{3}=x_{c}$ 和 $x_{4}=\dot{x}_{c}$ 作为状态变量，u 作为控制输入，写出状态方程。
(d) 求系统的所有平衡点。

![](image/719d1e7f90d8432be9fc4f877f7dda1ebbc5d5d84b6bbdb171db182adee6f330.jpg)

<details>
<summary>text_image</summary>

M
k
x_c u F_c
L
θ
F_y m
</details>

图 1.25 带有旋转制动装置的平移振荡器系统

1.17 直流电机的动力学方程 $^{[178]}$ 为

$$v _ {f} = R _ {f} i _ {f} + L _ {f} \frac {d i _ {f}}{d t}v _ {a} = c _ {1} i _ {f} \omega + L _ {a} \frac {d i _ {a}}{d t} + R _ {a} i _ {a}J \frac {d \omega}{d t} = c _ {2} i _ {f} i _ {a} - c _ {3} \omega$$

第一个是励磁回路的方程, $v_{f},i_{f},R_{f}$ 和 $L_{f}$ 分别表示电压、电流、电阻和电感。电枢回路由第二个方程描述,相应的变量为 $v_{a},i_{a},R_{a}$ 和 $L_{a}$ 。第三个方程是轴的力矩方程,J 是电机的惯量, $c_{3}$ 是阻尼系数, $c_{1}i_{f}\omega$ 一项是电枢回路产生的反电动势, $c_{2}i_{f}i_{a}$ 是电枢电流与励磁电路磁通的相互作用产生的力矩。
