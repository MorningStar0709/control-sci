# 6.1 无记忆函数

本节主要定义无记忆函数 $y = h(t, u)$ 的无源性, 这里 $h: [0, \infty) \times R^P \to R^P$ 。下面用电路来阐述该定义。图6.1(a)所示是电压为 $u$ , 电流为 $y$ 的单端口电阻元件, 我们把该元件看成以电压 $u$ 为输入, 以电流 $y$ 为输出的系统。如果输入功率始终非负, 即如果在 $u - y$ 特性上的每一点 $(u, y)$ 都满足 $uy \geqslant 0$ , 则该电阻元件是无源的。从几何意义上讲, 如图6.1(b)所示, 就意味着 $u - y$ 特性曲线一定位于一、三象限。这种电阻最简单的是服从欧姆定律 $u = Ry$ 或 $y = Gu$ 的线性电阻, 这里 $R$ 是电阻值, $G = 1/R$ 为其电导。阻值为正时, $u - y$ 特性是斜率为 $G$ 的直线, 且乘积 $uy = Gu^2$ 始终非负。事实上, 除了原点 $(0, 0)$ 以外, 该乘积总为正。图6.2(a)和图6.2(b)所示为几个关于非线性无源电阻元件的非线性 $u - y$ 特性曲线位于一、三象限的例子。注意图6.2(b)所示的隧道二级管特性, 即使 $u - y$ 曲线在某区域斜率为负, 仍是无源的。作为非线性无源元件的一个例子, 图6.2(c)所示为一个负电阻的 $u - y$ 特性, 该电阻在1.2.4节用于组成负阻振荡器。这一特性只有通过有源器件加以理解, 如图1.7所示的双隧道二极管电路。对于一个多端口网络, $u$ 和 $y$ 是向量, 流入网络的功率是内积 $u^{\mathrm{T}}y = \sum_{i=1}^{p} u_i y_i = \sum_{i=1}^{p} u_i h_i(u)$ 。如果对于所有 $u$ 都有 $u^{\mathrm{T}}y \geqslant 0$ , 则该网络是无源的。现在把这一无源性的概念推广到任何函数 $y = h(t, u)$ , 不考虑其物理原点。将 $u^{\mathrm{T}}y$ 作为系统的输入功率, 如果对于所有 $u, u^{\mathrm{T}}y \geqslant 0$ , 则认为系统是无源的。在标量情况下, 输入-输出关系曲线必须位于一、三象限, 或者说曲线属于扇形区域 $[0, \infty]$ , 这里0和无穷是一、三象限边界的斜率。即使 $h$ 是时变的, 这种图形表示也有效。在这种情况下, $u - y$ 曲线将随时间变化而变化, 但始终属于扇形区域 $[0, \infty]$ 。对于向量函数,能给出特殊情况下的图形表示,即 $h_{i}(t,u)$ 仅取决于 $u_{i},h(t,u)$ 可以分解的情况,即

$$
h (t, u) = \left[ \begin{array}{c} h _ {1} (t, u _ {1}) \\ h _ {2} (t, u _ {2}) \\ \vdots \\ h _ {p} (t, u _ {p}) \end{array} \right] \tag {6.1}
$$

在这种情况下，曲线的每部分都属于扇形区域 $[0, \infty]$ 。一般来讲，这种图形表示是不可能的，但如果对于所有 $(t, u)$ 都有 $u^{\mathrm{T}}h(t, u) \geqslant 0$ ，则将继续用名词“扇形区域”，称 $h$ 属于扇形区域 $[0, \infty]$ 。

![](image/8e737f7399c5d126a5e339392aaa512f20622e730bebc0b0f5d99e36b96b5c53.jpg)

<details>
<summary>text_image</summary>

+
u
-
y
</details>

(a)

![](image/5bc120c63a1143e947c392ef31bc83e0a4f16ee22b70a29ec74b526068f48b9b.jpg)

<details>
<summary>text_image</summary>

y
u
</details>

(b)

图 6.1 (a) 无源电阻；(b) 位于一、三象限的 u-y 特性  
![](image/63f3288ef970dca51582b68ab07090f9d23930ac8443a99f9397151502325a87.jpg)

<details>
<summary>text_image</summary>

y
u
</details>

(a)

![](image/81d3ac461ecef75c6ba9e86e0212b0e3edb116d06a27df0d4d98ecda94c7e80e.jpg)

<details>
<summary>text_image</summary>

y
u
</details>

(b)

![](image/c14b5eae2c2fbc3b57f301cbf05aa58513c89997bd52e49b4f8af7f76c216e79.jpg)

<details>
<summary>text_image</summary>

y
u
</details>

(c)   
图 6.2 (a) 和 (b) 非线性无源电阻特性曲线; (c) 非无源电阻特性曲线
