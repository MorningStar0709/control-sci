在证明本法则之前,需要介绍一下关于分离点的特性。因为根轨迹是对称的,所以根轨迹的分离点或位于实轴上,或以共轭形式成对出现在复平面中。一般情况下,常见的根轨迹分离点是位于实轴上的两条根轨迹分支的分离点。如果根轨迹位于实轴上两个相邻的开环极点之间,其中一个可以是无限极点,则在这两个极点之间至少存在一个分离点;同样,如果根轨迹位于实轴上两个相邻的开环零点之间,其中一个可以是无限零点,则在这两个零点之间也至少有一个分离点。参见图 4-7。

证明 由根轨迹方程,有

$$1 + \frac {K ^ {*} \prod_ {j = 1} ^ {m} (s - z _ {j})}{\prod_ {i = 1} ^ {n} (s - p _ {i})} = 0$$

所以闭环特征方程

$$D (s) = \prod_ {i = 1} ^ {n} (s - p _ {i}) + K ^ {*} \prod_ {j = 1} ^ {m} (s - z _ {j}) = 0$$

根轨迹在 $s$ 平面上相遇，说明闭环特征方程有重根出现。设重根为 $d$ ，根据代数中重根条件，有

![](image/a532cce9e2bf6535f73db4ec448fdb169b247a42cf89de94f4bfbf427b2adf6c.jpg)

<details>
<summary>text_image</summary>

d₂
分离点
d₁
-4
-3
-2
-1
0
j
</details>

图 4-7 实轴上根轨迹的分离点

$$D (s) = \prod_ {i = 1} ^ {n} (s - p _ {i}) + K ^ {*} \prod_ {j = 1} ^ {m} (s - z _ {j}) = 0\dot {D} (s) = \frac {\mathrm{d}}{\mathrm{d} s} \left[ \prod_ {i = 1} ^ {n} \left(s - p _ {i}\right) + K ^ {*} \prod_ {j = 1} ^ {m} \left(s - z _ {j}\right) \right] = 0$$

或

$$\prod_ {i = 1} ^ {n} (s - p _ {i}) = - K ^ {*} \prod_ {j = 1} ^ {m} (s - z _ {j}) \tag {4-21}\frac {\mathrm{d}}{\mathrm{d} s} \prod_ {i = 1} ^ {n} (s - p _ {i}) = - K ^ {*} \frac {\mathrm{d}}{\mathrm{d} s} \prod_ {j = 1} ^ {m} (s - z _ {j}) \tag {4-22}$$

将式(4-21)除式(4-22)，得

$$\frac {\frac {d}{d s} \prod_ {i = 1} ^ {n} (s - p _ {i})}{\prod_ {i = 1} ^ {n} (s - p _ {i})} = \frac {\frac {d}{d s} \prod_ {j = 1} ^ {m} (s - z _ {j})}{\prod_ {j = 1} ^ {m} (s - z _ {j})}, \quad \frac {d \ln \prod_ {i = 1} ^ {n} (s - p _ {i})}{d s} = \frac {d \ln \prod_ {i = 1} ^ {n} (s - z _ {j})}{d s}$$

代入 $\ln \prod_{i=1}^{n}(s - p_i) = \sum_{i=1}^{n}\ln (s - p_i),\quad \ln \prod_{j=1}^{m}(s - z_j) = \sum_{j=1}^{m}\ln (s - z_j)$

得 $\sum_{i=1}^{n} \frac{\mathrm{d}\ln(s-p_i)}{\mathrm{d}s} = \sum_{j=1}^{m} \frac{\mathrm{d}\ln(s-z_j)}{\mathrm{d}s}, \quad \sum_{i=1}^{n} \frac{1}{s-p_i} = \sum_{j=1}^{m} \frac{1}{s-z_j}$

从上式中解出 s，即为分离点 d。

这里不加证明地指出：当 l 条根轨迹分支进入并立即离开分离点时，分离角可由 $(2k+1)\pi/l$ 决定，其中 $k=0,1,\cdots,l-1$ 。需要说明的是，分离角定义为根轨迹进入分离点的切线方向与离开分离点的切线方向之间的夹角。显然，当 l=2 时，分离角必为直角。

例 4-1 设系统结构图与开环零、极点分布如图 4-8 所示，试绘制其概略根轨迹。

解 由法则4, 实轴上区域 $[0, -1]$ 和 $[-2, -3]$ 是根轨迹, 在图4-8中以粗实线表示。

由法则 2, 该系统有三条根轨迹分支, 且对称于实轴。

由法则1,一条根轨迹分支起于开环极点(0),终于开环有限零点(-1),另外两条根轨迹分支起于开环极点(-2)和(-3),终于无穷远处(无限零点)。

由法则 3, 两条终于无穷的根轨迹的渐近线与实轴交角为 $90^{\circ}$ 和 $270^{\circ}$ , 交点坐标为

![](image/912429449f3d6d401a6310a169a2bc74743b50249c6ab5b57be9cedd173283da.jpg)

<details>
<summary>flowchart</summary>
