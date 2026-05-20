$$u = K (v _ {r} - v) \tag {2.108}$$

其中：

$$v _ {\mathrm{r}} = \text { 参 考 速 度 } \tag {2.109}K = \text { 常数 } \tag {2.110}$$

这是“比例”控制规律，把 $v_{r}$ 与实际速度之差作为信号来加快或减慢发动机速度。以 $v_{r}$ 为输入，v为输出，将运动方程改写为传递函数形式。假定 $m=1500kg,\ b=70N\cdot s/m$ ，使用Matlab研究 $v_{r}$ 为单位阶跃时的响应。利用试错法，选择K值，使控制系统中实际速度能尽可能快地收敛到参考速度，达到满意的效果。

2.10 确定图 2.45 所示机器人横向运动的动力学方程。如图 2.46 的几何图所示，假定它有三个轮子，其中一个单一的、可操纵的车轮在前面，控制器 $U_{steer}$ 直接控制转向角的变化速率。假定机器人沿着一条直线运动，且偏离角非常小。也假定机器人以恒定速度 $V_{o}$ 运动。在控制器 $U_{steer}$ 处于理想情况下，列写有关机器人中心横向速度的动态方程。

![](image/93a7cb90977f6007a00dd8be727105acd55904fbc5823beb849314de0e89c267.jpg)

<details>
<summary>natural_image</summary>

Exterior view of a modern office building (no signage)
</details>

图 2.45 医疗设备用于交付的机器人

![](image/8bdbe3fa9b94bed8cb72101a97f53543a1633a397b6bbd0eda8f9b07f2960eca.jpg)

<details>
<summary>text_image</summary>

L
2
θs
L
</details>

图 2.46 机器人运动模型
