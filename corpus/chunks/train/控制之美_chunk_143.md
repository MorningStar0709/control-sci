解: $G(s)$ 有 $n=2$ 个极点 $s_{p1}=-1$ 和 $s_{p2}=-2, m=0$ 个零点。根据规则 5, 将有 $n=m-2$ 条根轨迹分支从 $G(s)$ 的两个极点分别指向无穷。根据规则 3, 根轨迹在实轴上存在于这两个极点之间。这意味着两条根轨迹分支将分别从两个极点出发, 沿着实轴相向而行, 汇聚后沿着一定的渐近线向无穷移动, 通过规则 6, 可以得到渐近线的信息, 渐近线与实轴的交点为

$$
\sigma_ {\mathrm{a}} = \frac {\sum s _ {\mathrm{pn}} - \sum s _ {\mathrm{zm}}}{n - m} = \frac {- 1 - 2 - 0}{2 - 0} = - 1. 5 \tag {8.2.4a}
$$

渐近线与实轴的夹角为

$$
\begin{array}{l} \theta = \frac {2 q + 1}{2 - 0} \pi , \quad q = 0, 1 \\ \Rightarrow \left\{ \begin{array}{l} \theta_ {1} = \frac {1}{2} \pi \\ \theta_ {2} = \frac {3}{2} \pi = - \frac {1}{2} \pi \end{array} \right. \tag {8.2.4b} \\ \end{array}
$$

根据式(8.2.4a)和式(8.2.4b)，得到渐近线的位置与方向，如图8.2.5所示。其根轨迹将沿着渐近线指向无穷。

最后,使用上述6个规则分析一个综合的例子。

例 8.2.7 系统开环传递函数 $G(s)=\frac{s+1}{s(s+2)(s+3)(s+4)}$ ，绘制闭环传递函数 $G_{\mathrm{cl}}(s)$ 的根轨迹。

解： $G(s)$ 有 $n = 4$ 个极点 $s_{\mathrm{p1}} = 0,s_{\mathrm{p2}} = -2,s_{\mathrm{p3}} = -3$ 和 $s_{\mathrm{p4}} = -4$ 。有 $m = 1$ 个零点

$s_{z1}=-1$ 。根据规则1，根轨迹一共有n=4条分支。

首先将所有极点/零点标注在复平面上并从右向左编号,如图 8.2.6 所示。根据规则 2 和规则 3, $s_{p1}=0$ 与 $s_{z1}=-1$ 之间有一条根轨迹,并且由极点 $s_{p1}=0$ 指向 $s_{z1}=-1$ 。 $s_{p2}=-2$ 与 $s_{p3}=-3$ 之间的实轴上也存在根轨迹。另外,在 $s_{p4}=-4$ 的左边实轴上也存在一条根轨迹。

![](image/ba2cfc693034d183aa4afeb007084c7d3a23df6a074b332e7e2b930a3696a5cd.jpg)

<details>
<summary>text_image</summary>

渐近线
jω
-2
-1.5
-1
O
σ
</details>

图8.2.5 例8.2.6的根轨迹

![](image/47dd4c419ffc514bac6d184fa7a164debfd7ad57f3ffe944925d6ba508de3d48.jpg)

<details>
<summary>text_image</summary>

从右向左编号
奇
第5
偶
第4
奇
第3
偶
第2
jω
奇
第1
有 -4 无 -3 有 -2 无 -1 有 O σ
</details>

图 8.2.6 例 8.2.7 的极点/零点分布与根轨迹分布

根据规则 5, 将有 $n - m = 3$ 条根轨迹指向无穷。利用规则 6 计算其渐近线, 可得渐近线与实轴的交点为

$$
\sigma_ {\mathrm{a}} = \frac {\sum s _ {\mathrm{pm}} - \sum s _ {z m}}{n - m} = \frac {0 - 2 - 3 - 4 - (- 1)}{4 - 1} = - \frac {8}{3} \tag {8.2.5a}
$$

渐近线与实轴的夹角为

$$
\begin{array}{l} \theta = \frac {2 q + 1}{4 - 1} \pi , \quad q = 0, 1, 2 \\ \Rightarrow \left\{ \begin{array}{l} \theta_ {1} = \frac {1}{3} \pi \\ \theta_ {2} = \pi \\ \theta_ {3} = \frac {5}{3} \pi = - \frac {1}{3} \pi \end{array} \right. \tag {8.2.5b} \\ \end{array}
$$

其中，与实轴夹角为 $\theta_{2} = \pi$ 的渐近线是从 $s_{\mathrm{p4}} = -4$ 沿着实轴指向负无穷的根轨迹分支。而另外两条渐近线与实轴的交点在 $\sigma_{\mathrm{a}} = -\frac{8}{3}$ ，夹角 $\theta_{1,3} = \pm \frac{1}{3}\pi$ 。这意味着将有两条根轨迹分支从 $s_{\mathrm{p2}} = -2$ 和 $s_{\mathrm{p3}} = -3$ 出发，沿着实轴相向而行，汇聚后再沿着渐近线移动，指向无穷。其根轨迹及渐近线如图8.2.7所示。
