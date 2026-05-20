# 第二种情况 特征值为复数, $\lambda_{1,2}=\alpha\pm j\beta$

经坐标变换 $z = M^{-1}x$ ，系统(2.3)的形式转换为

$$\dot {z} _ {1} = \alpha z _ {1} - \beta z _ {2}, \qquad \dot {z} _ {2} = \beta z _ {1} + \alpha z _ {2}$$

方程的解是振荡的,用极坐标

$$r = \sqrt {z _ {1} ^ {2} + z _ {2} ^ {2}}, \quad \theta = \arctan \left(\frac {z _ {2}}{z _ {1}}\right)$$

表示可更方便,得到两个去耦的一阶微分方程

$$\dot {r} = \alpha r, \qquad \dot {\theta} = \beta$$

对于给定的初始状态 $(r_{0},\theta_{0})$ ，其解由下式给出：

$$r (t) = r _ {0} e ^ {\alpha t}, \qquad \theta (t) = \theta_ {0} + \beta t$$

这是 $z_{1} - z_{2}$ 平面的对数螺旋曲线。对于不同的 $\alpha$ 值，轨线取图2.6所示的三种形式之一。当 $\alpha < 0$ 时，螺线收敛于原点；当 $\alpha >0$ 时，螺线由原点向外发散；当 $\alpha = 0$ 时，轨线为半径为 $r_0$ 的圆。图2.7所示为在 $x_{1} - x_{2}$ 平面内的轨线，如果 $\alpha < 0$ ，平衡点 $x = 0$ 称为稳定焦点；如果 $\alpha >0$ 平衡点称为非稳定焦点；如果 $\alpha = 0$ ，平衡点称为中心。

![](image/85e63d36c4b3050b2ac827c62af15d7d7efca31d3f271e6bee36f7b646bc0941.jpg)

<details>
<summary>text_image</summary>

z₂
(a)
z₁
</details>

![](image/91677e9389dfc8368a916b5d7458d6fac45f3976c905aa2105417e15180fdc9c.jpg)

<details>
<summary>text_image</summary>

x₂
v₂
v₁
x₁
(b)
</details>

图 2.5 鞍点的相图。(a) 在模型坐标中；(b) 在原坐标中  
![](image/81fc2cfbf24a226d06e4c1635913313503e2b9c3a02fd42ce5ffcbf2289b10af.jpg)

<details>
<summary>text_image</summary>

z₂
(a)
z₁
</details>

![](image/56fd7d52993760dcb70d906c9c025b7e0864f64ca9bfcfd46767c245d329af3b.jpg)

<details>
<summary>text_image</summary>

z₂
(b)
z₁
</details>

![](image/4fd5884f8a149bce6360861900833f51fdc34d2364e41b758e4159a564c40458.jpg)

<details>
<summary>text_image</summary>

z₂
(c)
z₁
</details>

图 2.6 特征值为复数时的典型轨线。(a) $\alpha<0$ ; (b) $\alpha>0$ ; (c) $\alpha=0$

![](image/afd36d1371cabb90200db995f2c94b2aeebfdb08de5b243ddf6eec45d9a57580.jpg)

<details>
<summary>text_image</summary>

(a)
x₂
x₁
</details>

![](image/2451ea22d859324596bddf94750d43d3dca57c18369f42da1903e6a1a41a0812.jpg)

<details>
<summary>text_image</summary>

(b)
x₂
x₁
</details>

![](image/e2abbbb594fdca4d756538586f6999aef639baf3b2eaf5f992237c6cbf620885.jpg)

<details>
<summary>text_image</summary>

(c)
x₂
x₁
</details>

图 2.7 相图。(a) 稳定焦点；(b) 非稳定焦点；(c) 中心
