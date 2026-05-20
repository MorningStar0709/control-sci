# 3) 电动机轴上的转矩平衡方程

$$J _ {m} \frac {\mathrm{d} \omega_ {m} (t)}{\mathrm{d} t} + f _ {m} \omega_ {m} (t) = M _ {m} (t) - M _ {c} (t) \tag {2-4}$$

式中， $f_{m}$ 是电动机和负载折合到电动机轴上的黏性摩擦系数； $J_{m}$ 是电动机和负载折合到电动机轴上的转动惯量。

由式(2-2)～式(2-4)中消去中间变量 $i_{a}(t), E_{a}$ 及 $M_{m}(t)$ ，便可得到以 $\omega_{m}(t)$ 为输出量， $u_{a}(t)$ 为输入量的直流电动机微分方程

$$
\begin{array}{l} L _ {a} J _ {m} \frac {\mathrm{d} ^ {2} \omega_ {m} (t)}{\mathrm{d} t ^ {2}} + (L _ {a} f _ {m} + R _ {a} J _ {m}) \frac {\mathrm{d} \omega_ {m} (t)}{\mathrm{d} t} + (R _ {a} f _ {m} + C _ {m} C _ {e}) \omega_ {m} (t) \\ = C _ {m} u _ {a} (t) - L _ {a} \frac {\mathrm{d} M _ {c} (t)}{\mathrm{d} t} - R _ {a} M _ {c} (t) \tag {2-5} \\ \end{array}
$$

在工程应用中，由于电枢电路电感 $L_{a}$ 较小，通常忽略不计，因而式(2-5)可简化为

$$T _ {m} \frac {\mathrm{d} \omega_ {m} (t)}{\mathrm{d} t} + \omega_ {m} (t) = K _ {m} u _ {a} (t) - K _ {c} M _ {c} (t) \tag {2-6}$$

式中， $T_{m}=R_{a}J_{m}/(R_{a}f_{m}+C_{m}C_{e})$ 是电动机机电时间常数； $K_{m}=C_{m}/(R_{a}f_{m}+C_{m}C_{e})$ ， $K_{c}=R_{a}/(R_{a}f_{m}+C_{m}C_{e})$ 是电动机传递系数。

如果电枢电阻 $R_{a}$ 和电动机的转动惯量 $J_{m}$ 都很小可忽略不计时, 式(2-6)还可进一步简化为

$$C _ {e} \omega_ {m} (t) = u _ {a} (t) \tag {2-7}$$

这时，电动机的转速 $\omega_{m}(t)$ 与电枢电压 $u_{a}(t)$ 成正比，于是，电动机可作为测速发电机使用。

例 2-3 图 2-3 是弹簧-质量-阻尼器机械位移系统。试列写质量 m 在外力 $F(t)$ 作用下（其中重力略去不计），位移 $x(t)$ 的运动方程。

解 设质量 m 相对于初始状态的位移、速度、加速度分别为 $x(t)$ , $\mathrm{d}x(t)/\mathrm{d}t$ , $\mathrm{d}^{2}x(t)/\mathrm{d}t^{2}$ 。由牛顿运动定律有

$$m \frac {\mathrm{d} ^ {2} x (t)}{\mathrm{d} t ^ {2}} = F (t) - F _ {1} (t) - F _ {2} (t) \tag {2-8}$$

式中， $F_{1}(t)=f\cdot dx(t)/dt$ 是阻尼器的阻尼力，其方向与运动方向相反，大小与运动速度成比例； $f$ 是阻尼系数； $F_{2}(t) = Kx(t)$ 是弹簧的弹力，其方向与运动方向相反，其大小与位移成比例， $K$ 是弹性系数。将 $F_{1}(t)$ 和 $F_{2}(t)$ 代入式(2-8)中，经整理后即得该系统的微分方程为

![](image/5b10235e2356fd2c2060c15f8ed6d406f7485de9ffe7e63505c829b15440e7f0.jpg)

<details>
<summary>text_image</summary>

F(t)
K
m
x(t)
f
</details>

图 2-3 弹簧-质量-阻尼器
机械位移系统

$$m \frac {\mathrm{d} ^ {2} x (t)}{\mathrm{d} t ^ {2}} + f \frac {\mathrm{d} x (t)}{\mathrm{d} t} + K x (t) = F (t) \tag {2-9}$$

例2-4 试列写图2-4齿轮系的运动方程。图中齿轮1和齿轮2的转速、齿数和半径分别用 $\omega_{1},Z_{1},r_{1}$ 和 $\omega_{2},Z_{2},r_{2}$ 表示；其黏性摩擦系数及转动惯量分别是 $f_{1},J_{1}$ 和 $f_{2},J_{2}$ ；齿轮1和齿轮2的原动转矩及负载转矩分别是 $M_{m},M_{1}$ 和 $M_2,M_c$ 。

![](image/d25bdfe599a3b0d61864ef753f8c83a33684956ea1eb7b18de45001a0e573815.jpg)

<details>
<summary>text_image</summary>

J₁
f₁
Z₁,M₁
Z₂,M₂
ω₂
J₂
f₂
Mc
</details>

(a)
