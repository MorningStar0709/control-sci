随着 $K$ 的增加, $G_{\mathrm{cl}}(s)$ 的根轨迹将离开实轴向无穷移动。当 $K = 2$ 时, $G_{\mathrm{cl}}(s)$ 的两个极点分别为 $s_{\mathrm{cl\_p3},4} = -2 \pm \mathrm{j}$ , 如图8.4.2(b)所示。此时若对其施加一个单位阶跃 $\left(r(t) = 1\right.$ , 即 $R(s) = \frac{1}{s}$ ), 系统的输出为

$$
x (t) = 1 + C _ {3} \mathrm{e} ^ {- 2 t} \sin (\omega t + \varphi) \tag {8.4.3}
$$

$C_{3}$ 和 $\varphi$ 的计算留给读者自己完成(参考第 5 章)。

式(8.4.2)和式(8.4.3)说明输出 $x(t)$ 的收敛速度与闭环传递函数极点的实部相关(这一结论在第4章、第5章和第6章中反复出现过)。根据图8.4.2,无论如何增大 $K$ 值, $G_{\mathrm{cl}}(s)$ 极点的实部最小值 $\sigma_{\min} = -2$ , 这意味着系统最快沿着 $\mathrm{e}^{-2t}$ 这条渐近线收敛。因此, 若要改变系统的响应速度, 就需要改变其根轨迹。这可以通过串联控制器/补偿器来实现。若可以将闭环传递函数的极点置于 $s = \sigma \pm \mathrm{j}\omega = -3 \pm 2\sqrt{3}\mathrm{j}$ 上, 那么系统的响应就会沿着渐近线 $\mathrm{e}^{-3t}$ 收敛。根据规则4, 根轨迹相对于实轴对称, 因此只需要分析 $s = \sigma + \mathrm{j}\omega = -3 + 2\sqrt{3}\mathrm{j}$ 这一个点。在例8.3.2中, 我们利用根轨迹的几何性质证明了 $s = -3 + 2\sqrt{3}\mathrm{j}$ 不在 $G_{\mathrm{cl}}(s)$ 的根轨迹上, 因为

$\angle G(s = -3 + 2\sqrt{3} j) = \left(\sum \text{零点到 } s_1 \text{ 的夹角} - \sum \text{极点到 } s_1 \text{ 的夹角}\right)\bigg|_{s = -3 + 2\sqrt{3} j}$

$$
= - \left(\frac {2 \pi}{3} + \frac {\pi}{2}\right) = - \frac {7}{6} \pi \tag {8.4.4}
$$

不满足式(8.3.7)。若要满足式(8.3.7)，需要在式(8.4.4)中补充 $+\frac{1}{6}\pi$ ，最简单的做法是为开环传递函数 $G(s)$ 增加一个零点，令其到 $s = -3 + 2\sqrt{3}j$ 的夹角为 $\frac{1}{6}\pi$ 。根据几何关系可以求得此零点位置为 $s_{z1} = -9$ ，如图8.4.3所示。此时， $\angle G(s = -3 + 2\sqrt{3}j) = \frac{1}{6}\pi -$ $\left(\frac{2\pi}{3} +\frac{\pi}{2}\right) = -\pi$ ，满足式(8.3.7)。

此新增加的控制器对应的传递函数为 $C(s) = s + 9$ ，它被串联在原控制系统中，如图8.4.4所示。

此时,控制量 $U(s)$ 为

$$
U (s) = E (s) K C (s) = K (s E (s) + 9 E (s)) \tag {8.4.5a}
$$

所对应的时域表达为

$$
u (t) = K \left(\frac {\mathrm{d} e (t)}{\mathrm{d} t} + 9 e (t)\right) \tag {8.4.5b}
$$

![](image/ff163303bacb703871e2bc8ce62c0a8532969020a9c458ebcf0878cbb40c591a.jpg)

<details>
<summary>text_image</summary>

新增零点s_{z1}=-9
-9
-\frac{1}{6}\pi
-\frac{1}{2}\pi
-\frac{2}{3}\pi
-\frac{1}{3}\pi
-\frac{1}{2}\pi
-\frac{1}{3}\pi
-\frac{1}{2}\pi
-\frac{1}{3}\pi
O
σ
jω
</details>

图8.4.3 增加一个零点 $s_{\mathrm{zl}} = -9$ 使得 $s = -3 + 2\sqrt{3}\mathbf{j}$ 在 $G_{\mathrm{el}}(s)$ 的根轨迹上

![](image/7e13c7a10dfc01e06a43dcb38c9c70910a0eecdf131fe718a13964b852731d20.jpg)

<details>
<summary>flowchart</summary>
