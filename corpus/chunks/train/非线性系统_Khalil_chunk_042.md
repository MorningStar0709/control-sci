当增大输入电压 u 时, 输出 y 将保持在 $(R_{3}/R_{4})E$ , 直到输入电压达到 $R_{3}R_{6}E/R_{4}R_{7}$ 。若超过这个值, 二极管 $D_{1}$ 和 $D_{3}$ 将截止, 而 $D_{2}$ 和 $D_{4}$ 将导通。与上面的情况相似, 因为两个放大器的反相输入端都是虚地的, 所以通过 $R_{5}$ 和 $D_{4}$ 的电流为零, 且 $D_{4}$ 的输入也是虚地的。因此, 输出电压 $y=(R_{2}/R_{1})E$ 。只要流过 $D_{2}$ 的电流为正, 这种状态就保持不变, 即

$$i _ {D 2} = \frac {u}{R _ {6}} + \frac {R _ {2} E}{R _ {1} R _ {7}} > 0 \Leftrightarrow u > - \frac {R _ {2} R _ {6} E}{R _ {1} R _ {7}}$$

这样即可得到图 1.12 所示的输入-输出特性, 其中

$$L _ {-} = - \frac {R _ {3} E}{R _ {4}}, L _ {+} = \frac {R _ {2} E}{R _ {1}}, S _ {-} = - \frac {R _ {2} R _ {6} E}{R _ {1} R _ {7}}, S _ {+} = \frac {R _ {3} R _ {6} E}{R _ {4} R _ {7}}$$

在例 2.1 中将会看到,对于 1.2.2 节的隧道二极管电路,当其输入电压远低于电路的动态特性时,会产生类似的特性。

![](image/54a7b3d8f85abe06ab7ff7ffcf2955c66074da82416388b99123efbcc63c7669.jpg)

<details>
<summary>text_image</summary>

y
L+
S-
S+
u
L-
</details>

图 1.12 迟滞中继

![](image/d6eec1a4e6bd86e7cc70893f11d126cded2e3cc606a985d2d364b352e5d83148.jpg)

<details>
<summary>text_image</summary>

R6
u
-
A1
+
-
R5
D1
D2
-
E
R1
D4
R2
y
A2
+
-
R3
D3
R4
+E
R7
</details>

图 1.13 实现图 1.12 迟滞中继的运算放大器电路

另一类迟滞非线性是间隙特性,如图1.15(b)所示,这在齿轮中是常见的。为说明间隙特性,图1.15(a)的草图给出了一对配套齿轮间的一个小缝隙。假设被驱动的齿轮有较高的摩擦惯性比,使得当驱动齿轮开始减速时,其表面在L处保持接触。图1.15(b)为其输入-输出特性,给出从动轮y与驱动轮u的角度间的关系。从图1.15(a)的位置开始,当驱动轮旋转一个小于a的角度时,从动轮不动。当转动角大于a时,在L 处建立触点,且从动轮按照输入-输出特性的 $A_{o}A$ 段随驱动轮转动。若驱动轮反方向转动,在 U 点建立触点前转动的角度为 2a。在此运动过程中,角度 y 保持不变,得到特性曲线的 AB 段。触点 U 建立后,从动轮随驱动轮转动,得到特性曲线的 BC 段,直到下一个反方向转动得到曲线的 CDA 段。这样,幅度大于 a 的周期输入就产生了图 1.15(b) 的 ABCD 迟滞循环。注意,若输入幅度较大,迟滞循环将是 $A'B'C'D'$ ,这类迟滞特性与图 1.12 所示的中继迟滞特性的重要区别是,后者的迟滞循环与其输入幅度无关。

![](image/35982eca79bcb6af9fc0d0981883c99980c09ac5ebf97822722c001741cdfd94.jpg)

<details>
<summary>text_image</summary>

i
导通
截止
v
</details>

图1.14 理想二极管的 $v - i$ 特性

图 1.16 是典型的磁性材料的迟滞特性,与间隙相似,其迟滞循环也与输入幅度有关 $^{①}$ 。

![](image/7db64c4d44a1d3f623509d44de4eff7225262081572a274c2f9752f1da02b476.jpg)

<details>
<summary>text_image</summary>

a
U
驱动轮
L
a
从动轮
(a)
y
B'
A'
B
A
a
A₀
u
C
D
C'
D'
(b)
</details>

图 1.15 间隙非线性  
![](image/0ee924722ce517bea19fe6e38e9037ca287bbafe46a85a5fc6576a94840d2311.jpg)

<details>
<summary>text_image</summary>

Diagram showing multiple curved trajectories in the u-u-y coordinate system with directional arrows indicating flow or displacement.
</details>

图 1.16 迟滞非线性
