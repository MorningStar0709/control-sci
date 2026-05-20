它在复平面上的表达如图8.3.2(a)所示，其模为

$$
M = | G (s) | = \sqrt {\left(- \frac {1}{2}\right) ^ {2} + \left(- \frac {\sqrt {3}}{6}\right) ^ {2}} = \frac {\sqrt {3}}{3} \tag {8.3.3b}
$$

复角为

$$
\varphi = \arctan \frac {\left(\frac {\sqrt {3}}{6}\right)}{\left(\frac {1}{2}\right)} - \pi = - \frac {5}{6} \pi \tag {8.3.3c}
$$

将其写成指数形式为

$$
G (s = - 1 + \sqrt {3} \mathrm{j}) = M \mathrm{e} ^ {\mathrm{j} \varphi} = \frac {\sqrt {3}}{3} \mathrm{e} ^ {- \frac {5}{6} \pi \mathrm{j}} \tag {8.3.3d}
$$

![](image/858a8ba870c66e13dee2ff56dfff569b9a18a03bfea5e8a9a39a7acc0e6ab265.jpg)

<details>
<summary>text_image</summary>

-1/2
jω
O
φ=-5/6 π
σ
M=√3/3
-√3/6
</details>

(a) $G(s) = -\frac{1}{2} - \frac{\sqrt{3}}{6}\mathrm{j}$ 的复平面表达

![](image/9912ed119b70da6316dffacd3831408150ad80eed49ef70c535af0fd8ddd85d2.jpg)

<details>
<summary>text_image</summary>

s=-1+\u221a3j
l₁
l₂
l₃
φ₁
φ₂
φ₃
-2
-1
O
σ
jω
</details>

(b) 几何方法求解  
图8.3.2 例8.3.1图示

方法二：使用几何方法和式(8.3.2)，首先将 $G(s)=\frac{s+2}{s(s+1)}$ 的极点 $s_{p1}=0,s_{p2}=-1$ 和零点 $s_{z1}=-2$ 及 $s=-1+\sqrt{3}j$ 标记在图8.3.2(b)中，之后将极点/零点与 $s=-1+\sqrt{3}j$ 连接起来。根据几何关系，可得 $l_{1}=2,l_{2}=\sqrt{3},l_{3}=2,\varphi_{1}=\frac{\pi}{3},\varphi_{2}=\frac{\pi}{2},\varphi_{3}=\frac{2\pi}{3}$ 。代入式(8.3.2)，可得

$$
M = \mid G (s = - 1 + \sqrt {3} \mathrm{j}) \mid = \frac {\prod \text {零点到} s \text {的距离}}{\prod \text {极点到} s \text {的距离}} \Bigg | _ {s = - 1 + \sqrt {3} \mathrm{j}} = \frac {l _ {1}}{l _ {2} l _ {3}} = \frac {2}{\sqrt {3} \times 2} = \frac {\sqrt {3}}{3} \tag {8.3.4a}
$$

$\varphi = \angle G(s = -1 + \sqrt{3} j) = \left(\sum \text{零点到 } s \text{ 的夹角} - \sum \text{极点到 } s \text{ 的夹角}\right)\bigg|_{s = \sigma +j\omega}$

$$
= \varphi_ {1} - \varphi_ {2} - \varphi_ {3} = \frac {\pi}{3} - \frac {\pi}{2} - \frac {2 \pi}{3} = - \frac {5}{6} \pi \tag {8.3.4b}
$$

将其写成指数形式,与式(8.3.3d)所得结果一致。

以上性质可以用来判断给定值 $s = \sigma + \mathrm{j}\omega$ 是否为 $G_{\mathrm{cl}}(s)$ 的根（极点），这对增益调节及控制器的设计非常重要。令闭环传递函数 $G_{\mathrm{cl}}(s) = \frac{KG(s)}{1 + KG(s)}$ 的分母等于0，可以得到它的特征方程的根（极点），即

$$
1 + K G (s) = 0
$$

$$
\Rightarrow K G (s) = - 1 \tag {8.3.5}
$$

![](image/dc5b41d6c7732130b61e4eafe3dd950589084b3c3ea1f2c3b9bfa4058b5cebfb.jpg)

<details>
<summary>text_image</summary>

jω
KG(s)
∠KG(s)
-1 |KG(s)| O σ
</details>

图 8.3.3 KG(s) = -1 复平面表达

$KG(s)$ 在复平面上的表达如图 8.3.3 所示。根据图示的几何关系, 可得

$$
\mid K G (s) \mid = 1 \tag {8.3.6a}
$$
