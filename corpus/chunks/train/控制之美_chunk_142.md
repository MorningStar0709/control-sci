从右向左编号
偶
第4
奇
第3
偶
第2
奇
第1
-4 有 -3 无 -2 有 -1 O σ
jω
</details>

(a) 规则3示意图

![](image/ea2f32a664b0325e1759d011009e705ace3836788254545292543721fd952903.jpg)

<details>
<summary>text_image</summary>

jω
-4 -3 -2 -1 O σ
</details>

(b) 根轨迹  
图8.2.2 例8.2.3的说明与根轨迹

规则 4：若复数根存在，则一定是共轭的，所以根轨迹相对于实轴对称。

例 8.2.4 系统开环传递函数 $G(s)=\frac{s^{2}+4}{s^{2}+2s+2}$ ，绘制闭环传递函数 $G_{\mathrm{cl}}(s)$ 的根轨迹。

解： $G(s)$ 有 $n = 2$ 个极点 $s_{\mathrm{p1}} = -1 + \mathrm{j}$ 和 $s_{\mathrm{p2}} = -1 - \mathrm{j}$ 。有 $m = 2$ 个零点 $s_{z1} = 2\mathrm{j}$ 和 $s_{z2} = -2\mathrm{j}$ 。根据规则1、规则2和规则4，根轨迹有 $n = 2$ 条对称于实轴的分支，其运行轨迹从极点指向零点，如图8.2.3所示。

规则 5: 如果 n > m，则有 $(n - m)$ 条分支从极点指向无穷。如果 n < m，则有 $(m - n)$ 条分支从无穷指向零点。

![](image/18831692b4c55bbdc0dae97417ed0b2e245ec54dfbabafbe98946e11c15a16f7.jpg)

<details>
<summary>text_image</summary>

jω
2
-1+j×
O
σ
-1-j×
-2
</details>

图8.2.3 例8.2.4的根轨迹

例 8.2.5a 系统开环传递函数 $G(s)=\frac{s+2}{(s+1)(s+3)}$ ，绘制闭环传递函数 $G_{\mathrm{cl}}(s)$ 的根轨迹。

解： $G(s)$ 有 $n = 2$ 个极点 $s_{\mathrm{p1}} = -1$ 和 $s_{\mathrm{p2}} = -3$ 。有 $m = 1$ 个零点 $s_{\mathrm{z1}} = -2$ 。根据规则1，根轨迹有 $n = 2$ 条分支。根据规则2和规则3，其中的一条分支从极点 $s_{\mathrm{p1}} = -1$ 指向零点 $s_{\mathrm{z1}} = -2$ 。因为 $G(s)$ 的极点数多于零点数，即 $n > m$ ，根据规则5，将会有 $n - m = 1$ 条根轨迹的分支从 $s_{\mathrm{p2}} = -3$ 指向无穷。 $s_{\mathrm{p2}} = -3$ 是从右边数在实轴上的第三个极点/零点（奇数点），根据规则3，根轨迹一定在其左边的实轴上，因此这一条分支将从极点 $s_{\mathrm{p2}} = -3$ 指向负无穷。其根轨迹如图8.2.4(a)所示。

例 8.2.5b 系统开环传递函数 $G(s)=s+2$ ，绘制闭环传递函数 $G_{\mathrm{cl}}(s)$ 的根轨迹。

解： $G(s)$ 没有极点， $n = 0$ 。只有 $m = 1$ 个零点 $s_{z1} = -2$ 。根据规则5，有一条根轨迹从无穷指向零点。根据规则3，根轨迹在零点 $s_{z1}=-2$ 的左边实轴上。综上所述，其根轨迹如图8.2.4(b)所示。

![](image/c94817fec14c52ab8cd24002a978b5705e5cb11711a610ff08b75e713395044d.jpg)

<details>
<summary>text_image</summary>

jω
-3 -2 -1 O σ
</details>

(a) 例8.2.5a的根轨迹

![](image/a310ec65c5170bf4e5361d48eda5358a758f87e64076effb20613b8bb9743df7.jpg)

<details>
<summary>text_image</summary>

jω
-2 O σ
</details>

(b) 例8.2.5b的根轨迹  
图8.2.4 例8.2.5的根轨迹

规则 6：根轨迹沿着渐近线移动，渐近线与实轴的交点为

$$
\sigma_ {\mathrm{a}} = \frac {\sum s _ {\mathrm{pn}} - \sum s _ {\mathrm{zm}}}{n - m} \tag {8.2.3a}
$$

渐近线与实轴的夹角为

$$
\theta = \frac {2 q + 1}{n - m} \pi , \quad q = \left\{ \begin{array}{l l} 0, 1, \dots , n - m - 1 & n > m \\ 0, 1, \dots , m - n - 1 & n <   m \end{array} \right. \tag {8.2.3b}
$$

例 8.2.6 系统开环传递函数 $G(s)=\frac{1}{(s+1)(s+2)}$ ，绘制闭环传递函数 $G_{\mathrm{cl}}(s)$ 的根轨迹。
