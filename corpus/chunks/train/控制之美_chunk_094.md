$$
\sqrt {\zeta^ {2} - 1} = \sqrt {1 - \zeta^ {2}} j
\Rightarrow \left\{ \begin{array}{l} \lambda_ {1} = - \zeta \omega_ {\mathrm{n}} + \omega_ {\mathrm{n}} \sqrt {1 - \zeta^ {2}} \mathrm{j} \\ \lambda_ {2} = - \zeta \omega_ {\mathrm{n}} - \omega_ {\mathrm{n}} \sqrt {1 - \zeta^ {2}} \mathrm{j} \end{array} \right. \tag {5.2.5}
$$

特征值 $\lambda_{1}$ 和 $\lambda_{2}$ 是两个复数，而且它们的实部都是 $-\zeta \omega_{\mathrm{n}} < 0$ 。根据表3.3.1，平衡点 $z_{\mathrm{f}} = [0,0]^{\mathrm{T}}$ 是一个稳定的焦点，它的相轨迹如图5.2.1(b)所示。这是一个边振荡边衰减的系统，系统的状态变量将随着时间的增加而趋于平衡点。这也是我们日常生活中最常见的弹簧系统,无论它被压缩或者拉伸,当它从初始位置被释放后,就会不断地振动且振幅逐渐减小并最终停下来。这种系统称为欠阻尼系统(Underdamped System)。

类(3): $\zeta=0$ 。

此时

$$
\left\{ \begin{array}{l} \lambda_ {1} = \omega_ {\mathrm{n}} \mathrm{j} \\ \lambda_ {2} = - \omega_ {\mathrm{n}} \mathrm{j} \end{array} \right. \tag {5.2.6}
$$

状态矩阵的特征值是一对共轭纯虚数。根据表3.3.1,平衡点 $z_{f}=[0,0]^{T}$ 是一个中心点。其相轨迹会围绕着这个中心点做圆周运动,如图5.2.1(c)所示。此时两个状态变量,即质量块的位移与速度会不断地振动,循环往复。从物理意义上来理解它, $\zeta=0$ 代表了式(5.1.1)中b=0,即系统的阻尼为零。没有阻尼的时候系统的总能量就不会消耗,所以一旦对这个系统施加一个初始状态(给予其初始的能量),它就会不断地振动下去。这种系统称为无阻尼系统(Undamped System)。

![](image/3651f3f18dbe00f457691a52fedc2d2bd9678306c0023511a16e2f5ff0ea9cb9.jpg)

<details>
<summary>text_image</summary>

z₂(t)
O
z₁(t)
</details>

(a) $\zeta \geqslant 1$

![](image/2799aa482c3e44ecb7074d23ebfdafe594dac0a6695fe42bb57ab0894bd3e274.jpg)

<details>
<summary>text_image</summary>

z₂(t)
O
z₁(t)
</details>

(b) $0 < \zeta < 1$

![](image/2ba6dab3e34b5cad48879af118e011f6951eafaa7d76f1962dc00d4c76b0793a.jpg)

<details>
<summary>text_image</summary>

z₂(t)
O
z₁(t)
</details>

(c) $\zeta=0$   
图 5.2.1 二阶系统对初始状态响应的相轨迹
