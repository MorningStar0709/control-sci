# 10.2.1 系统能控性的直观理解

在设计控制器之前,需要判断一个先决条件,即系统的能控性(Controllability)。思考两个例子,如图10.2.1(a)所示,对一个质量为 $m_{1}$ 的小车施加向右的力 $F(t)$ 。小车的位移为 $x_{1}(t)$ ,根据牛顿第二定律: $m_{1}\frac{\mathrm{d}^{2}x_{1}(t)}{\mathrm{d}t^{2}}=F(t)$ ,选取两个状态变量, $z_{1}(t)=x_{1}(t)$ ,代表位移; $z_{2}(t)=\frac{\mathrm{d}z_{1}(t)}{\mathrm{d}t}$ ,代表速度。令系统的输入 $u(t)=F(t)$ ,代表外力。可以得到状态空间方程,即

$$
\frac {\mathrm{d}}{\mathrm{d} t} \left[ \begin{array}{l} z _ {1} (t) \\ z _ {2} (t) \end{array} \right] = \left[ \begin{array}{l l} 0 & 1 \\ 0 & 0 \end{array} \right] \left[ \begin{array}{l} z _ {1} (t) \\ z _ {2} (t) \end{array} \right] + \left[ \begin{array}{l} 0 \\ 1 \end{array} \right] u (t) \tag {10.2.1}
$$

仅凭常识判断便知,理论上可以通过改变输入 $u(t)$ , 使得状态变量 $z_{1}(t)$ (小车的位移) 和 $z_{2}(t)$ (小车的速度) 达到任意给定值。

下面考虑一个更复杂的情况, 如果将另一辆质量为 $m_{2}$ 的小车用一根弹簧挂在 $m_{1}$ 的后面, 如图 10.2.1(b) 所示, $m_{2}$ 的状态变量 $z_{3}(t)=x_{2}(t)$ , 代表其位移; $z_{4}(t)=\frac{\mathrm{d}z_{3}(t)}{\mathrm{d}t}$ , 代表其速度。现在的问题是, 通过输入 $u(t)$ 是否可以控制所有的状态变量 $z(t)=[z_{1}(t), z_{2}(t), z_{3}(t), z_{4}(t)]^{\mathrm{T}}$ , 使它们同时达到一个任意的给定值? 换言之, 我们能否通过控制作用在第一辆车上的外力同时控制两辆小车的位置和速度? 这一问题需要在设计控制器之前解决。

![](image/c91e6a9bc1ec3db3c011ae155d7286fe80e13d0d47712919640ce7dfa29391c8.jpg)

<details>
<summary>text_image</summary>

z₁(t)=x₁(t)
→ z₂(t)=\frac{dz₁(t)}{dt}
m₁ → u(t)=F(t)
</details>

(a) 单个小车控制

![](image/3fa023b0406c9485d45f4c52286ca27415342b74604ae5d94d38ba0aa03dbd5f.jpg)

<details>
<summary>text_image</summary>

z₃(t)=x₂(t)
z₄(t)=dz₃(t)/dt
m₂
k
m₁
z₁(t)=x₁(t)
z₂(t)=dz₁(t)/dt
u(t)=F(t)
</details>

(b) 两个小车控制  
图10.2.1 能控性举例
