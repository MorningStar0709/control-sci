# 例2.11 积分器

列出图 2.29 所示的电路的传递函数。

解答。本例中的方程是微分方程，式(2.46)和式(2.47)要求

$$i _ {\mathrm{in}} + i _ {\mathrm{out}} = 0 \tag {2.49}$$

因此，

$$\frac {v _ {\mathrm{in}}}{R _ {\mathrm{in}}} + C \frac {\mathrm{d} v _ {\mathrm{out}}}{\mathrm{d} t} = 0 \tag {2.50}$$

将式 $(2.50)$ 表示成积分形式为

$$v _ {\mathrm{out}} = - \frac {1}{R _ {\mathrm{in}} C} \int_ {0} ^ {t} v _ {\mathrm{in}} (\tau) \mathrm{d} \tau + v _ {\mathrm{out}} (0) \tag {2.51}$$

![](image/1ed98480e4e35c37f7e21095816667cc8655e55db45b8a5b4b8482727bda6f6e.jpg)

<details>
<summary>text_image</summary>

C
i_out
v_in ○─R_in─●─○─●─○ v_out
</details>

图 2.29 积分运算放大器

式(2.50)中，利用运算符 $d/dt=s$ ，则传递函数（假定初始条件为零）为

$$V _ {\mathrm{out}} (s) = - \frac {1}{s} \frac {V _ {\mathrm{in}} (s)}{R _ {\mathrm{in}} C} \tag {2.52}$$

因为在该电路中，理想运算放大器实现了积分运算，所以此电路称为积分器。
