# (1) 幅角原理

设 $s$ 为复数变量, $F(s)$ 为 $s$ 的有理分式函数。对于 $s$ 平面上任意一点 $s$ , 通过复变函数 $F(s)$ 的映射关系, 在 $F(s)$ 平面上可以确定关于 $s$ 的象。在 $s$ 平面上任选一条闭合曲线 $\Gamma$ , 且不通过 $F(s)$ 的任一零点和极点, 当 $s$ 从闭合曲线 $\Gamma$ 上任一点 $A$ 起, 顺时针沿 $\Gamma$ 运动一周, 再回到 $A$ 点, 则相应地, $F(s)$ 平面上亦从点 $F(A)$ 起, 到 $F(A)$ 点止亦形成一条闭合曲线 $\Gamma_F$ 。为讨论方便, 取 $F(s)$ 为下述简单形式:

$$F (s) = \frac {(s - z _ {1}) (s - z _ {2})}{(s - p _ {1}) (s - p _ {2})} \tag {5-61}$$

其中 $z_{1}, z_{2}$ 为 $F(s)$ 的零点； $p_{1}, p_{2}$ 为 $F(s)$ 的极点。不失一般性，取 $s$ 平面上 $F(s)$ 的零点和极点以及闭合曲线的位置如图5-29(a)所示， $\Gamma$ 包围 $F(s)$ 的零点 $z_{1}$ 和极点 $p_{1}$ 。

设复变量 $s$ 沿闭合曲线 $\Gamma$ 顺时针运动一周，研究 $F(s)$ 相角的变化情况

$$\delta \underline {{{/ F (s)}}} = \oint_ {\Gamma} \underline {{{/ F (s)}}} d s \tag {5-62}$$

因为

$$\underline {{{F (s)}}} = \underline {{{s - z _ {1}}}} + \underline {{{s - z _ {2}}}} - \underline {{{s - p _ {1}}}} - \underline {{{s - p _ {2}}}} \tag {5-63}$$

![](image/1910c80df3622d81f5990b87f073e7e8feec5eeb823526ec6e35bdbd102150d8.jpg)

<details>
<summary>text_image</summary>

j
s₁
z₁
Γ
s
P₁
z₂
A
s₂
P₂
0
</details>

(a) $s$ 平面

![](image/6c362a5dadb683d9230d892928f31b884632460968a41c3e8763f42d40ee7497.jpg)

<details>
<summary>text_image</summary>

j
Γ_F
F(A)
F(s)
0
</details>

(b) $F(s)$ 平面  
图 5-29 s 和 $F(s)$ 平面的映射关系

因而

$$\delta \underline {{{/ F (s)}}} = \delta \underline {{{/ s - z _ {1}}}} + \delta \underline {{{/ s - z _ {2}}}} - \delta \underline {{{/ s - p _ {1}}}} - \delta \underline {{{/ s - p _ {2}}}} \tag {5-64}$$

由于 $z_{1}$ 和 $p_1$ 被 $\Gamma$ 所包围，故按复平面向量的相角定义，逆时针旋转为正，顺时针旋转为负

$$\delta \left/ s - z _ {1} \left. \right. = \delta \left/ s - p _ {1} \left. \right. = - 2 \pi$$

而对于零点 $z_{2}$ , 由于 $z_{2}$ 未被 $\Gamma$ 所包围, 过 $z_{2}$ 作两条直线与闭合曲线 $\Gamma$ 相切, 设 $s_{1}, s_{2}$ 为切点, 则在 $\Gamma$ 的 $\widehat{s_{1}s_{2}}$ 段, $s - z_{2}$ 的角度减小, 在 $\Gamma$ 的 $\widehat{s_{2}s_{1}}$ 段, 角度增大, 且有

$$
\begin{array}{l} \delta \underline {{{/ s - z _ {2}}}} = \oint_ {\Gamma} \underline {{{/ s - z _ {2}}}} \mathrm{d} s \\ = \int_ {\Gamma_ {s _ {1} s _ {2}}} \underline {{{\left/ s - z _ {2} \left. \right.}}} \mathrm{d} s + \int_ {\Gamma_ {s _ {2} s _ {1}}} \underline {{{\left/ s - z _ {2} \left. \right.}}} \mathrm{d} s = 0 \\ \end{array}
$$

$p_{2}$ 未被 $\Gamma$ 包围，同理可得 $\delta \sqrt{s - p_2} = 0$ 。

上述讨论表明, 当 $s$ 沿 $s$ 平面任意闭合曲线 $\Gamma$ 运动一周时, $F(s)$ 绕 $F(s)$ 平面原点的圈数只和 $F(s)$ 被闭合曲线 $\Gamma$ 所包围的极点和零点的代数和有关。上例中 $\delta / F(s) = 0$ 。因而, 形成如下幅角原理。

幅角原理 设 $s$ 平面闭合曲线 $\Gamma$ 包围 $F(s)$ 的 $Z$ 个零点和 $P$ 个极点，则 $s$ 沿 $\Gamma$ 顺时针运动一周时，在 $F(s)$ 平面上， $F(s)$ 闭合曲线 $\Gamma_F$ 包围原点的圈数

$$R = P - Z \tag {5-65}$$

$R < 0$ 和 $R > 0$ 分别表示 $\Gamma_F$ 顺时针包围和逆时针包围 $F(s)$ 平面的原点， $R = 0$ 表示不包围 $F(s)$ 平面的原点。
