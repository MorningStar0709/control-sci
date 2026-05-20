# 3.3.2 二维相平面与相轨迹——简化形式

考虑一个二维系统,在没有输入的情况下,它的状态空间方程为

$$
\frac {\mathrm{d}}{\mathrm{d} t} \left[ \begin{array}{l} z _ {1} (t) \\ z _ {2} (t) \end{array} \right] = A \left[ \begin{array}{l} z _ {1} (t) \\ z _ {2} (t) \end{array} \right] = \left[ \begin{array}{l l} a _ {1 1} & a _ {1 2} \\ a _ {2 1} & a _ {2 2} \end{array} \right] \left[ \begin{array}{l} z _ {1} (t) \\ z _ {2} (t) \end{array} \right] \tag {3.3.5}
$$

求式(3.3.5)的平衡点,可令 $\frac{d}{dt}\begin{bmatrix}z_{1}(t)\\ z_{2}(t)\end{bmatrix}=0$ ,得到

$$
\left\{ \begin{array}{l} 0 = a _ {1 1} z _ {1} (t) + a _ {1 2} z _ {2} (t) \\ 0 = a _ {2 1} z _ {1} (t) + a _ {2 2} z _ {2} (t) \end{array} \right.

\Rightarrow \left\{ \begin{array}{l} z _ {1 \mathrm{f}} = 0 \\ z _ {2 \mathrm{f}} = 0 \end{array} \right. \tag {3.3.6}
$$

首先分析简化矩阵，假设 $a_{12} = a_{21} = 0$ 。此时式(3.3.5)可以化简为

$$
\frac {\mathrm{d}}{\mathrm{d} t} \left[ \begin{array}{l} z _ {1} (t) \\ z _ {2} (t) \end{array} \right] = \left[ \begin{array}{c c} a _ {1 1} & 0 \\ 0 & a _ {2 2} \end{array} \right] \left[ \begin{array}{l} z _ {1} (t) \\ z _ {2} (t) \end{array} \right] \tag {3.3.7}
$$

即

$$
\left\{ \begin{array}{l} \frac {\mathrm{d} z _ {1} (t)}{\mathrm{d} t} = a _ {1 1} z _ {1} (t) \\ \frac {\mathrm{d} z _ {2} (t)}{\mathrm{d} t} = a _ {2 2} z _ {2} (t) \end{array} \right. \tag {3.3.8}
$$

下面根据 $a_{11}$ 和 $a_{22}$ 的符号来进行分类讨论。

类(1): $a_{11}>0$ 且 $a_{22}>0$ 。

首先分析 $a_{11} = a_{22} > 0$ 的情况：从坐标轴上的点入手，假设 $\mathbf{z}(t)$ 在 $t = 0$ 时位于坐标横轴上，即 $z(0) = [z_1(0), z_2(0)]^{\mathrm{T}} = [z_1(0), 0]^{\mathrm{T}}$ ，此时 $z_2(0) = 0 = z_{2\mathrm{f}}$ 在平衡点上，所以 $z_2(t)$ 不会随时间改变。如图3.3.4(a)所示，当初始状态 $z_1(0) = z_{1\mathrm{r}} > 0$ 时，根据式(3.3.8)， $\frac{\mathrm{d}z_1(t)}{\mathrm{d}t}\Bigg|_{z_1(0) = z_{1\mathrm{r}}} = a_{11}z_{1\mathrm{r}} > 0$ ，因此 $z_1(t)$ 会随着时间增加而不断地增加，向右移动并远离平衡点。同理，如果初始状态处于平衡点左边，即 $z_1(0) = z_{1\mathrm{l}} < 0$ ，那么随着时间的增加， $z_1(t)$ 会不断地减小（向左移动）。读者可以用同样的方法去分析在纵轴上 $(z_1(0) = z_{1\mathrm{f}} = 0)$ 的情况，如图3.3.4(a)所示，在纵轴上 $z_2(t)$ 的变化也将是沿着远离平衡点的轨迹移动。

![](image/e26abd9eda75467ee396adde08c0320dcb684ef209028194cbbb7e1638580dca.jpg)

<details>
<summary>text_image</summary>

z₂(t)
z₁₁ O z₁ᵣ
z₁(t)
</details>

(a) 坐标轴上的相轨迹

![](image/45002a3184b938befcd90ad741b68d2253948253d32886e2f6fa6b507735aef0.jpg)

<details>
<summary>text_image</summary>

z₂(t)
z(0)
O
z₁(t)
</details>

(b) 平面上的相轨迹  
图 3.3.4 $a_{11}=a_{22}>0$ 时的相平面分析
