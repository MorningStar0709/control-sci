# 例2.14 直流电动机模型

根据如图 2.33a 所示的等效电路图，列写直流电动机方程。假设转子的惯量为 $J_{m}$ ，黏性摩擦因数为 b。

解答。转子的受力图如图 2.33b 所示，定义正方向，用 T 和 $b\dot{\theta}_{m}$ 表示产生的转矩。根据牛顿定律可得

$$J _ {\mathrm{m}} \ddot {\theta} _ {\mathrm{m}} + b \dot {\theta} _ {\mathrm{m}} = K _ {\mathrm{t}} i _ {\mathrm{a}} \tag {2.62}$$

![](image/55a00edd61ac3751f08bec963650b79bdc60736a0e53c1a016ca099b07e01fc3.jpg)

<details>
<summary>text_image</summary>

Rₐ
Lₐ
iₐ
+
-
vₐ
e = Kₑ θ̇ₘ
+ -
</details>

a）电枢电路

![](image/faf64497b8292021d13597002f81a49c06c856ad2e8a114bebc7fc60c9388a5d.jpg)

<details>
<summary>text_image</summary>

T
θm
Jm
bθm
</details>

b）转子受力图  
图 2.33 直流电动机

分析包含反电动势电压的电路，可得电路方程为

$$L _ {\mathrm{a}} \frac {\mathrm{d} i _ {\mathrm{a}}}{\mathrm{d} t} + R _ {\mathrm{a}} i _ {\mathrm{a}} = v _ {\mathrm{a}} - K _ {\mathrm{e}} \dot {\theta} _ {\mathrm{m}} \tag {2.63}$$

在式(2.62)和式(2.63)中用 s 代替 d/dt，很容易得到电动机的传递函数为

$$\frac {\Theta_ {\mathrm{m}} (s)}{V _ {\mathrm{a}} (s)} = \frac {K _ {\mathrm{t}}}{s [ (J _ {\mathrm{m}} s + b) (L _ {\mathrm{a}} s + R _ {\mathrm{a}}) + K _ {\mathrm{t}} K _ {\mathrm{e}} ]} \tag {2.64}$$

一般地，与机械运动相比，电感的相对效应可忽略不计，方程(2.63)中可忽略电感的相对效应。在这种情况下，将式(2.62)和式(2.63)合并成一个方程，可得

$$J _ {\mathrm{m}} \ddot {\theta} _ {\mathrm{m}} + \left(b + \frac {K _ {\mathrm{t}} K _ {\mathrm{e}}}{R _ {\mathrm{a}}}\right) \dot {\theta} _ {\mathrm{m}} = \frac {K _ {\mathrm{t}}}{R _ {\mathrm{a}}} v _ {\mathrm{a}} \tag {2.65}$$

从式(2.65)可清楚地看到，此时反电动势的影响和摩擦的影响是不可区分的，传递函数为

$$\frac {\Theta_ {\mathrm{m}} (s)}{V _ {\mathrm{a}} (s)} = \frac {\frac {K _ {\mathrm{t}}}{R _ {\mathrm{a}}}}{J _ {\mathrm{m}} s ^ {2} + \left(b + \frac {K _ {\mathrm{t}} K _ {\mathrm{e}}}{R _ {\mathrm{a}}}\right) s} \tag {2.66}= \frac {K}{s (\tau s + 1)} \tag {2.67}$$

其中：

$$K = \frac {K _ {\mathrm{t}}}{b R _ {\mathrm{a}} + K _ {\mathrm{t}} K _ {\mathrm{e}}} \tag {2.68}\tau = \frac {R _ {\mathrm{a}} J _ {\mathrm{m}}}{b R _ {\mathrm{a}} + K _ {\mathrm{t}} K _ {\mathrm{e}}} \tag {2.69}$$

多数情况下，需要建立电动机输入电压和输出速度 $\left(\omega=\dot{\theta}_{m}\right)$ 之间的传递函数。此时，传递函数变形为

$$\frac {\Omega (s)}{V _ {\mathrm{a}} (s)} = s \frac {\Theta_ {\mathrm{m}} (s)}{V _ {\mathrm{a}} (s)} = \frac {K}{\tau s + 1} \tag {2.70}$$

机电能量转换的另一种装置是由 N. Tesla 发明的交流(AC)感应电动机。分析交流电动机远比分析直流电动机复杂。图 2.34 给出了当外加频率不变、幅值变化的(正弦)电压时，转速对转矩的典型实验曲线族。虽然图中数据是基于恒定的发电机转速得到的，但可以利用它们得到电动机常数，从而获得电动机动态模型。为了分析如图 2.34 所描述的交流电动机的控制问题，当转速接近零时，在中间电压处对曲线进行线性近似，可得
