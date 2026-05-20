# 1.2.7 一般非线性问题

在前面的例子中,我们看到的是物理系统建模中的一些典型非线性问题,如非线性电阻、非线性摩擦力和 S 状非线性等,本节将讨论其他一些典型非线性问题。图 1.10 所示为四个典型的无记忆非线性问题。之所以称为无记忆、零记忆或静态,是因为非线性系统在任一时刻的输出仅由该时刻的输入决定,而与历史输入无关。

图1.10(a)所示的是由符号函数

$$
\operatorname{sgn} (u) = \left\{ \begin{array}{c c} 1, & u > 0 \\ 0, & u = 0 \\ - 1, & u <   0 \end{array} \right. \tag {1.28}
$$

描述的理想中继器,其非线性特性可由机电中继器、晶闸管电路和其他开关器件实现。

图 1.10(b) 所示的是一个理想的饱和非线性问题。饱和特性在实际放大器(如电放大器、磁放大器、气动放大器或液压放大器)、电动机及其他设备中是很普遍的,也常用做限幅器限定变量的范围。定义饱和函数

$$
\operatorname{sat} (u) = \left\{ \begin{array}{c c} u, & | u | \leqslant 1 \\ \operatorname{sgn} (u), & | u | > 1 \end{array} \right. \tag {1.29}
$$

表示归一化的饱和非线性特性,并按照 k sat(u/δ) 得到图 1.10(b)。

图 1.10(c) 所示为理想的死区非线性特性, 这是典型的电子管和其他一些放大器在输入信号较小时的特性。用于图1.10(b)和图1.10(c)中表示饱和特性和死区特性的分段线性函数是实际中平滑函数的近似,如图1.11所示。

![](image/b66dcd45f2f18bb87b9195a8bcc6dc0c215d5675ecd8bc852af8f8b7575be38b.jpg)

<details>
<summary>text_image</summary>

y
1
u
-1
</details>

(a) 中继器

![](image/ced8c0d41edc350ec7d1b868c71f8b047d6a1e746c44b0f5a27ea4a76c95cfc0.jpg)

<details>
<summary>text_image</summary>

y
k
δ u
</details>

(b) 饱和

![](image/7864972be65b2125d88891d35ddc2575123a6b9dec9e31d22839235f51d08657.jpg)

<details>
<summary>text_image</summary>

y
δ u
</details>

(c) 死区

![](image/feb43ca476e69ea5d387a749def1178ce1ba9fa47bef95de8f286304959fa127.jpg)

<details>
<summary>line</summary>
