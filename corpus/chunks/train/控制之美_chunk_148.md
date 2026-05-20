$$
\angle K G (s) = - (2 q + 1) \pi , \quad q = \pm 0, \pm 1, \pm 2, \dots \tag {8.3.6b}
$$

因为增益 $K$ 是一个常数，因此不会改变复数 $KG(s)$ 的复角，因此式(8.3.6b)可以写成

$$
\angle G (s) = - (2 q + 1) \pi , \quad q = \pm 0, \pm 1, \pm 2, \dots \tag {8.3.7}
$$

式(8.3.7)将被用来判断给定值 $s=\sigma+j\omega$ 是否在 $G_{\mathrm{cl}}(s)$ 的轨迹上，请看下面的例子。

例 8.3.2 系统开环传递函数 $G(s)=\frac{1}{(s+1)(s+3)}$ ，利用根轨迹的几何性质判断 $s_{1}=-2-j$ 和 $s_{2}=-3+2\sqrt{3}j$ 是否在闭环传递函数 $G_{\mathrm{cl}}(s)$ 的根轨迹上。

解：首先将 $G(s)$ 的极点 $s_{\mathrm{p1}} = -1, s_{\mathrm{p2}} = -3$ 以及给定点 $s_1 = -2 - \mathrm{j}$ 和 $s_2 = -3 + 2\sqrt{3} \mathrm{j}$ 标记在图8.3.4中，之后将极点与给定点连接起来。

![](image/624b50233bb8dc1508ea7b469d795f0eecbb31da3e85362512c7c1b00ea37f20.jpg)

<details>
<summary>text_image</summary>

s₂=-3+2√3j
φ₄
-3
φ₁
-2
-1
φ₃
φ₂
s₁=-2-j
O
σ
jω
</details>

图 8.3.4 例 8.3.2 图示

如图 8.3.4 所示, 根据几何性质可得 $\varphi_{1} = -\frac{\pi}{4}, \varphi_{2} = -\frac{3\pi}{4}, \varphi_{3} = \frac{2\pi}{3}, \varphi_{4} = \frac{\pi}{2}$ 。

判断 $s_{1}=-2-j$ 点，代入式(8.3.4b)，得到

$\angle G(s_1 = -2 - j) = \left(\sum \text{零点到 } s_1 \text{ 的夹角} - \sum \text{极点到 } s_1 \text{ 的夹角}\right)\bigg|_{s_1 = -2 - j}$

$$
= 0 - (\varphi_ {1} + \varphi_ {2}) = \frac {\pi}{4} + \frac {3 \pi}{4} = \pi \tag {8.3.8}
$$

满足式(8.3.7)，因此 $s_{1}=-2-j$ 在 $G_{\mathrm{cl}}(s)$ 的根轨迹上。

判断 $s_{2}=-3+2\sqrt{3}$ j 点，代入式(8.3.4b)，得到

$\angle G(s_{2} = -3 + 2\sqrt{3}\mathrm{j}) = \left(\sum \text{零点到} s_{2}\text{的夹角} - \sum \text{极点到} s_{2}\text{的夹角}\right)\bigg|_{s_{2} = -3 + 2\sqrt{3}\mathrm{j}}$

$$
= 0 - (\varphi_ {3} + \varphi_ {4}) = - \left(\frac {2 \pi}{3} + \frac {\pi}{2}\right) = - \frac {7}{6} \pi \tag {8.3.9}
$$

不满足式(8.3.7)，因此 $s_{2}=-3+2\sqrt{3}\mathrm{j}$ 不在 $G_{\mathrm{cl}}(s)$ 的根轨迹上。这意味着无论增益K如何调节， $G_{\mathrm{cl}}(s)$ 的极点都无法位于 $s_{2}$ 上。但我们可以设计控制器改变 $G_{\mathrm{cl}}(s)$ 的根轨迹，使它包含给定的 $s_{2}$ ，请看8.4节分析。
