式(3.3.21)是一个以原点为中心的椭圆方程,这说明 $z_{1}(t)$ 和 $z_{2}(t)$ 在相平面中沿着一个椭圆的轨迹运行,如图3.3.10所示。在这种情况下,平衡点 $z_{\mathrm{f}}$ 称为中心点 (Center),相轨迹会围绕着这个中心点做圆周运动。判断相轨迹的运动方向,可以以一个在横轴的点进行分析,例如选择状态在横轴 $\begin{bmatrix} z_1(0) \\ z_2(0) \end{bmatrix} = \begin{bmatrix} z_1(0) \\ 0 \end{bmatrix}$ (如图3.3.10所示,选择 $z_{1}(0) > 0$ ) 的点进行分析。此时根据状态空间方程 $\frac{\mathrm{d}z(t)}{\mathrm{d}t} = \begin{bmatrix} 0 & 4 \\ -1 & 0 \end{bmatrix} z(t)$ , 可得 $\begin{bmatrix} \frac{\mathrm{d}z_1(t)}{\mathrm{d}t} \\ \frac{\mathrm{d}z_2(t)}{\mathrm{d}t} \end{bmatrix} = \begin{bmatrix} 0 \\ -z_1(0) \end{bmatrix}$ 。在这一时刻, $\frac{\mathrm{d}z_1(t)}{\mathrm{d}t} \Big|_{t=0} = 0$ , 所以 $z_{1}(t)$ 不会随时间改变。而 $\frac{\mathrm{d}z_2(t)}{\mathrm{d}t} \Big|_{t=0} = -z_{1}(0) < 0$ , 所以 $z_{2}(t)$ 会随着时间的增加而减小。在相轨迹中, $z_{2}(t)$ 在 $t=0$ 时的移动趋势指向下方,所以相轨迹在图中按照顺时针移动。图3.3.10(b)显示了 $z_{1}(t)$ 和 $z_{2}(t)$ 随时间的变化。可以发现, $z_{1}(t)$ 和 $z_{2}(t)$ 此消彼长, 循环往复。如果从能量的角度来分析, 它们的总能量取决于初始状态 $z(0)$ , 不会随着时间发生改变。所以这个系统在稳定与不稳定之间, $z(t)$ 始终有界但始终不为0。

例 3.3.6 分析二阶系统 $\frac{\mathrm{d}z(t)}{\mathrm{d}t} = Az(t)$ 的相轨迹, 其中 $A = \begin{bmatrix} 1 & -2 \\ 2 & 1 \end{bmatrix}$ 。

解：首先求解矩阵 A 的特征值，可得

![](image/40bd011292cb799ccbfe5919205429fe9dc4466005e66ba7ea929221a38e1628.jpg)

<details>
<summary>text_image</summary>

z₂(t)
O
(z₁(0),0)
z₁(t)
</details>

(a) 相轨迹

![](image/b86353592325a724a21af405e61f2c6160f6813376007401c08e1f35ed1c934a.jpg)

<details>
<summary>line</summary>

| t | z₁(t) | z₂(t) |
| --- | --- | --- |
| 0 | 0 | 0 |
| t₁ | z₁(t) | z₂(t) |
| t₂ | 0 | 0 |
</details>

(b) $z(t)$ 随时间的变化  
图3.3.10 例3.3.5的相轨迹分析

$$
\left\{ \begin{array}{l} \lambda_ {1} = 1 + 2 \mathrm{j} \\ \lambda_ {2} = 1 - 2 \mathrm{j} \end{array} \right. \tag {3.3.22}
$$

矩阵 $\mathbf{A}$ 的特征值是共轭的复数，但与例3.3.5不同，它包含了实部部分。分析它的解，令 $\pmb {z}(t) = \pmb {P}\overline{\pmb{z}} (t)$ ，其中 $P = [v_1,v_2]$ ，可得

$$
\frac {\mathrm{d}}{\mathrm{d} t} \left[ \begin{array}{c} \overline {{z}} _ {1} (t) \\ \overline {{z}} _ {2} (t) \end{array} \right] = \left[ \begin{array}{c c} 1 + 2 \mathrm{j} & 0 \\ 0 & 1 - 2 \mathrm{j} \end{array} \right] \overline {{z}} (t) \tag {3.3.23}
$$

式 $(3.3.23)$ 的解为
