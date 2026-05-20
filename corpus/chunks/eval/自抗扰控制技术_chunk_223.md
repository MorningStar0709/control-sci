$$h = 0. 0 1, \beta_ {0 1} = 1 0 0. 0, \beta_ {0 2} = 3 0 0. 0, r _ {0} = 1. 0,\alpha_ {1} = 0. 5, \alpha_ {2} = 1. 0, \beta_ {1} = 1. 0, \beta_ {2} = 5 0. 0$$

时的仿真结果如图6.4.4所示．在这里第1式中的不确定因素的影响和第2式中的不确定因素的影响都很好的被抑制掉了．

![](image/d16daf591ad0c1c7f05e93dea80fdc28719c898b300de6527b03335a92896524.jpg)

<details>
<summary>line</summary>

| x | v₁₀ | x₂₀ |
| --- | --- | --- |
| 2 | 0 | -10 |
| 4 | -5 | -15 |
| 6 | -10 | -20 |
| 8 | -15 | -25 |
| 10 | -20 | -30 |
| 12 | -25 | -35 |
| 14 | -30 | -40 |
| 16 | -35 | -45 |
| 18 | -40 | -50 |
| 20 | -45 | -55 |
</details>

图6.4.4

例 3 设有三阶被控对象

$$
\left\{ \begin{array}{l} \dot {x} _ {1} = w _ {1} (t) + x _ {2} \\ \dot {x} _ {2} = w _ {2} (t) + x _ {3} \\ \dot {x} _ {3} = w _ {3} (t) + u \\ y = x _ {1} \end{array} \right. \tag {6.4.9}
$$

假定变量 $x_{1}, x_{2}, x_{3}$ 都能量测，控制目标是让变量 $x_{1}$ 快速无超调地跟踪设定值 $v = 1.0$ 。扰动 $w_{1}(t), w_{2}(t), w_{3}(t)$ 是不确定因素，假定为

$$w _ {1} (t) = 1 0 \text { sign } (\sin (0. 6 t)), w _ {2} (t) = 1 0 \text { sign } (\sin (0. 7 t)),w _ {3} (t) = 1 0 \text { sign } (\sin (0. 8 t))$$

按上述思想设计如下控制算法: 把 $x_{2}$ 作为虚拟控制量, 让 $x_{1}$ 跟踪设定值 v = 1.0 的控制算法为

$$
\left\{ \begin{array}{l l} v _ {1} = v _ {1} - h r _ {0} \mathrm{fal} (v _ {1} - v, 0. 5, h) & \text {安排过渡过程} \\ e = z _ {1 1}, \mathrm{fe} = \mathrm{fal} (e, 0. 5, h) \\ z _ {1 1} = z _ {1 1} + h \left(z _ {1 2} - \beta_ {0} e + u _ {1}\right) \\ z _ {1 2} = z _ {1 2} + h \left(- \beta_ {0} \mathrm{fe}\right) & \text {关于} x _ {1} \text {的扩张状态观测器} \\ e _ {1} = v _ {1} - z _ {1 2} & \text {生成误差} \\ u _ {1} = \beta_ {1} \mathrm{fal} \left(e _ {1}, 0. 5, 1. 0\right) - z _ {1 2} & \text {反馈控制与扰动补偿} \end{array} \right. \tag {6.4.10}
$$

以 $x_{3}$ 作为虚拟控制量，让 $x_{2}$ 跟踪上面算出的虚拟控制量 $u_{1}$ 的控制算法为

$$
\left\{ \begin{array}{l l} e = z _ {2 1} - x _ {2}, \mathrm{fe} = \operatorname{fal} (e, 0. 5, h) \\ z _ {2 1} = z _ {2 1} + h \left(z _ {2 2} - \beta_ {0 1} e + u _ {2}\right) \\ z _ {2 2} = z _ {2 2} + h \left(- \beta_ {0 2} \mathrm{fe}\right) & \text {关于} x _ {2} \text {的扩张状态观测器} \\ e _ {2} = u _ {1} - z _ {2 1} & \text {生成误差} \\ u _ {2} = \beta_ {2} \operatorname{fal} \left(e _ {2}, 0. 5, 1. 0\right) - z _ {2 2} & \text {误差反馈和扰动补偿} \end{array} \right. \tag {6.4.11}
$$

然后用实际控制量 u 来控制变量 $x_{3}$ ，让它跟踪上面算出的虚拟控制量 $u_{2}$ 的控制算法为
