这样，当 $x_{1} < a$ 时， $\dot{V}$ 为正，当 $x_{1} > a$ 时， $\dot{V}$ 为负。现在

$$\delta (p) = V (E) - V (A) = \int_ {A E} \dot {V} (x (t)) d t$$

右边的积分沿由 A 到 E 的弧线进行, 如果 p 较小, 则整个弧线处于 $0 < x_{1} < a$ 的带内, 那么 $\delta(p)$ 为正。随 p 增加, 一部分弧线会出现在带外, 即图 2.24 中的 BCD 段。在这种情况下, 可根据弧线在 $0 < x_{1} < a$ 的带内还是带外, 以不同的方式计算积分。因此把积分分为三部分:

$$\delta (p) = \delta_ {1} (p) + \delta_ {2} (p) + \delta_ {3} (p)$$

其中， $\delta_{1}(p)=\int_{AB}\dot{V}(x(t))dt,\quad\delta_{2}(p)=\int_{BCD}\dot{V}(x(t))dt,\quad\delta_{3}(p)=\int_{DE}\dot{V}(x(t))dt$

考虑第一项 $\delta_1(p) = -\int_{AB}\varepsilon x_1h(x_1)dt = -\int_{AB}\varepsilon x_1h(x_1)\frac{dt}{dx_1} dx_1$

把方程(2.8)中的 $dx_{1} / dt$ 代入上式，得

$$\delta_ {1} (p) = - \int_ {A B} \varepsilon x _ {1} h (x _ {1}) \frac {1}{x _ {2} - \varepsilon h (x _ {1})} d x _ {1}$$

其中，沿弧线 $AB$ 段， $x_{2}$ 是给定的 $x_{1}$ 的函数，显然 $\delta_1(p)$ 为正。注意，对于弧线 $AB$ 段，随 $p$ 增加， $x_{2} - \varepsilon h(x_{1})$ 增加，因此 $\delta_1(p)$ 随 $p$ 趋于无穷而减小。同理可以证明第三项 $\delta_3(p)$ 为正，且随 $p$ 趋于无穷而减小。现在考虑第二项

$$\delta_ {2} (p) = - \int_ {B C D} \varepsilon x _ {1} h (x _ {1}) d t = - \int_ {B C D} \varepsilon x _ {1} h (x _ {1}) \frac {d t}{d x _ {2}} d x _ {2}$$

把方程(2.8)中的 $dx_{2} / dt$ 代入，得

$$\delta_ {2} (p) = \int_ {B C D} \varepsilon h (x _ {1}) d x _ {2}$$

其中，沿弧线BCD段， $x_{1}$ 是给定的 $x_{2}$ 的函数。由于 $h(x_{1}) > 0$ 且 $dx_{2} < 0$ ，右边的积分为负。随 $p$ 增大，弧线ABCDE移到右边， $\delta_2(p)$ 的积分区域增大。随 $p$ 减小， $\delta_2(p)$ 的积分区域减小，显然 $\lim_{p\to \infty}\delta_2(p) = -\infty$ 。简言之，我们已经证明

- 当 $r > 0$ 时, 如果 $p < r$ , 则 $\delta(p) > 0$   
- 当 $p \geqslant r$ 时, 随 $p$ 趋于无穷, $\delta(p)$ 单调减小到负无穷

图2.25为函数 $\delta (p)$ 的图形，显然，通过选择足够大的 $p$ 即可保证 $\delta (p)$ 为负，因此 $\alpha (p) < p$

![](image/2298f68a25eb6338947d14dc77c35974eb26aec95ff0ca34b42a7320a177148b.jpg)

<details>
<summary>text_image</summary>

x₂
x₂ = εh(x₁)
x₁
</details>

图2.23 例2.9的向量场图

![](image/682206439efc2ad94323c87b5da776ce59a868d95f59f0a23f452bb4c1758ea5.jpg)

<details>
<summary>text_image</summary>

x₂
p
A
B
a
C
x₁
-α(p)
E
</details>

图2.24 例2.9的轨道ABCDE

注意到 $h(\cdot)$ 是奇函数, 由对称性可推出, 如果 $(x_{1}(t), x_{2}(t))$ 是方程(2.8)的解, 那么 $(-x_{1}(t), -x_{2}(t))$ 也是方程(2.8)的解。因此, 如果已知存在一个图2.24中的路径ABCDE, 那么该路径对原点的映像就是另一条路径。考虑点 $A$ 为 $(0, p), E$ 为 $(0, -\alpha(p))$ , 其中 $\alpha(p) < p$ , 弧线ABCDE形成一条闭合曲线, 其对原点的映像和与弧线相接的 $x_{2}$ 轴也形成一条闭合曲线(见图2.26)。设 $M$ 是闭合曲线环绕的区域, 当 $t \geqslant 0$ 时, 在 $t = 0$ 时始于 $M$ 内的每条轨线都会保持在 $M$ 内。这是由于在 $x_{2}$ 轴上部分向量场的方向以及解的唯一性使各轨线不相交造成的。现在 $M$ 是有界闭集, 且有唯一的平衡点在原点。在原点的雅可比矩阵为
