# (2) 复变函数 $F(s)$ 的选择

控制系统的稳定性判定是利用已知开环传递函数来判定闭环系统的稳定性。为应用幅角原理,选择复变函数

$$F (s) = 1 + G (s) H (s) = 1 + \frac {B (s)}{A (s)} = \frac {A (s) + B (s)}{A (s)} \tag {5-66}$$

由式(5-66)可知， $F(s)$ 具有以下特点：

1) $F(s)$ 的零点为闭环传递函数的极点， $F(s)$ 的极点为开环传递函数的极点。  
2) 因为开环传递函数分母多项式的阶次一般大于或等于分子多项式的阶次, 故 $F(s)$ 的零点和极点数相同。

3) $s$ 沿闭合曲线 $\Gamma$ 运动一周所产生的两条闭合曲线 $\Gamma_F$ 和 $\Gamma_{GH}$ 只相差常数1，即闭合曲线 $\Gamma_F$ 可由 $\Gamma_{GH}$ 沿实轴正方向平移一个单位长度获得。闭合曲线 $\Gamma_F$ 包

围 $F(s)$ 平面原点的圈数等于闭合曲线 $\Gamma_{GH}$ 包围 $F(s)$ 平面 $(-1, j0)$ 点的圈数，其几何关系如图5-30所示。

由 $F(s)$ 的特点可以看出， $F(s)$ 取上述特定形式具有两个优点：其一是建立了系统的开环极点和闭环极点与 $F(s)$ 的零极点之间的直接联系；其二是建立了闭合曲线 $\Gamma_F$ 和闭合曲线 $\Gamma_{GH}$ 之间的转换关系。在已知开环传递函数 $G(s)H(s)$ 的条件下，上述优点为幅角原理的应用创造了条件。

![](image/64a69ab324472f29045065bab00fca509c561b3670397638cb5d13462d946979.jpg)

<details>
<summary>text_image</summary>

ΓGH
ΓF
-1
0
1
j
</details>

图 5-30 $\Gamma_{F}$ 与 $\Gamma_{GH}$ 的几何关系

(3) s 平面闭合曲线 $\Gamma$ 的选择

系统的闭环稳定性取决于系统闭环传递函数极点即 $F(s)$ 的零点的位置，因此当选择 $s$ 平面闭合曲线 $\Gamma$ 包围 $s$ 平面的右半平面时，若 $F(s)$ 在 $s$ 右半平面的零点数 $Z = 0$ ，则闭环系统稳定。考虑到前述闭合曲线 $\Gamma$ 应不通过 $F(s)$ 的零极点的要求， $\Gamma$ 可取图5-31所示的两种形式。

![](image/cb630bcc8b4b2f710763fce763bb7cf6b86d1c1a584b2a324f114ef1124018d2.jpg)

<details>
<summary>text_image</summary>

(a) G(s)H(s)无虚轴上的极点
</details>

![](image/7a3820343b8842830406161bae29a86586aa2d14ac2f2cb92f59dd1264b34401.jpg)

<details>
<summary>text_image</summary>

(b) G(s)H(s)有虚轴上的极点
</details>

图 5-31 s 平面的闭合曲线 $\Gamma$

当 $G(s)H(s)$ 无虚轴上的极点时，如图5-31(a)所示， $s$ 平面闭合曲线 $\Gamma$ 由两部分组成：

1) $s = \infty \mathrm{e}^{\mathrm{j}\theta}, \theta \in [0^{\circ}, -90^{\circ}]$ , 即圆心为原点、第IV象限中半径为无穷大的 $\frac{1}{4}$ 圆; $s = \mathrm{j}\omega$ , $\omega \in (-\infty, 0]$ , 即负虚轴。  
2） $s=j\omega,\omega\in[0,+\infty)$ ，即正虚轴； $s=\infty e^{j\theta},\theta\in[0^{\circ},+90^{\circ}]$ ，即圆心为原点、第I象限中半径为无穷大的 $\frac{1}{4}$ 圆。

当 $G(s)H(s)$ 在虚轴上有极点时，为避开开环虚极点，在图5-31(a)所选闭合曲线 $\Gamma$ 的基础上加以扩展，构成图5-31(b)所示的闭合曲线 $\Gamma$ 。

1）开环系统含有积分环节时，在原点附近，取 $s = \varepsilon e^{j\theta}(\varepsilon$ 为正无穷小量， $\theta \in [-90^{\circ}, + 90^{\circ}])$ 即圆心为原点、半径为无穷小的半圆。  
2) 开环系统含有等幅振荡环节时，在 $\pm \mathrm{j}\omega_{n}$ 附近，取 $s = \pm \mathrm{j}\omega_{n} + \varepsilon \mathrm{e}^{\mathrm{j}\theta}$ （ $\varepsilon$ 为正无穷小量， $\theta \in [-90^{\circ}, +90^{\circ}]$ ），即圆心为 $\pm \mathrm{j}\omega_{n}$ 、半径为无穷小的半圆。

按上述 $\Gamma$ 曲线，函数 $F(s)$ 位于 $s$ 右半平面的极点数即开环传递函数 $G(s)H(s)$ 位于 $s$ 右半平面的极点数 $P$ 应不包括 $G(s)H(s)$ 位于 $s$ 平面虚轴上的极点数。
