$$
\overline {{{z}}} (t) = \left[ \begin{array}{l} \overline {{{z}}} _ {1} (t) \\ \overline {{{z}}} _ {2} (t) \end{array} \right] = \left[ \begin{array}{l} C _ {1} \mathrm{e} ^ {(1 + \mathrm{j} 2) t} \\ C _ {2} \mathrm{e} ^ {(1 - \mathrm{j} 2) t} \end{array} \right] = \mathrm{e} ^ {t} \left[ \begin{array}{l} C _ {1} \mathrm{e} ^ {\mathrm{j} 2 t} \\ C _ {2} \mathrm{e} ^ {- \mathrm{j} 2 t} \end{array} \right] \tag {3.3.24}
$$

可以发现,它和式(3.3.15)的差别在于一个系数 $e^{t}$ , 而 $e^{t}$ 是随着时间的增加而不断增大的。因此其相轨迹如图 3.3.11(a) 所示, 它与图 3.3.10(a) 类似, 以原点为中心做圆周运动, 但是直径在不断地扩大, 形成了一个向外的螺旋线(本例中, 螺旋线的方向是逆时针的, 如例 3.3.5 所分析, 可以通过坐标轴上一点进行判断, 故不赘述)。 $z(t)$ 随时间变化的示意图如图 3.3.11(b) 所示, 会持续地振荡且振幅不断地加强。在这种情况下, 平衡点 $z_{f}$ 称为不稳定焦点 (Unstable Spiral)。

![](image/544413b9529bf0cf7f58f89fe28ec182ec6a1b62b200a706b3dce9c53d07fae8.jpg)

<details>
<summary>text_image</summary>

z₂(t)
O
z₁(t)
</details>

(a) 相轨迹

![](image/2382f3727f5787b013ab24f3eae5a971a6ff4a885d9bd06ea0f16dca51dd77c7.jpg)

<details>
<summary>line</summary>

| t | z(t) |
| --- | --- |
| 0 | 0 |
| Peak | High |
| Low | Low |
</details>

(b) $z(t)$ 随时间的变化  
图3.3.11 例3.3.6的相轨迹分析

例3.3.7 分析二阶系统 $\frac{\mathrm{d}z(t)}{\mathrm{d}t} = Az(t)$ 的相轨迹，其中 $A = \begin{bmatrix} -4 & 2 \\ -5 & -2 \end{bmatrix}$ 。

解：求解矩阵 A 的特征值，可得

$$
\left\{ \begin{array}{l} \lambda_ {1} = - 3 + 3 j \\ \lambda_ {2} = - 3 - 3 j \end{array} \right. \tag {3.3.25}
$$

与例 3.3.6 类似, 可以判断出它的平衡点是一个稳定焦点(Stable Spiral)。相轨迹将沿螺旋线指向原点。其所对应的时间函数将振荡衰减, 直至为 0 。它的相轨迹和时间函数如图 3.3.12 所示。

![](image/50561409f629be8aa1331fefd776633516bfea5a24cceb95c82ba84283c0df62.jpg)

<details>
<summary>text_image</summary>

z₂(t)
O
z₁(t)
</details>

(a) 相轨迹

![](image/880604b151413e9625c54d67c0c9418b7f8bb37ce32f2b6e778f07cc5385b578.jpg)

<details>
<summary>line</summary>

| t | z(t) |
| --- | --- |
| 0 | 0 |
| e^(-3t) | (estimated from curve) |
| t | (estimated from curve) |
</details>

(b) 时间函数  
图3.3.12 例3.3.7的相轨迹分析

上述例子说明,状态矩阵 A 的特征值将决定平衡点的类型及系统的表现。表 3.3.1 总结了特征值与平衡点类型的关系。通过上述分析和表 3.3.1 可知,状态矩阵 A 的特征值实部部分决定了平衡点的稳定性,而特征值的虚部部分决定了系统是否会有振动。

表 3.3.1 状态矩阵 $A$ 的特征值与平衡点类型
