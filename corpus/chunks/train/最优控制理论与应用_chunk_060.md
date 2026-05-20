# 4.1 经典变分法的局限性

上面用经典变分法解最优控制问题时,得出了最优性的必要条件

$$\frac {\partial H}{\partial \boldsymbol {U}} = \mathbf {0}$$

在得出这个条件时,作了下面的假定:(1) $\delta U$ 是任意的,即U不受限制,它遍及整个向量空间,是一个开集;(2) $\frac{\partial H}{\partial U}$ 是存在的。

在实际工程问题中,控制作用常常是有界的。如飞机舵面的偏角有限制,火箭的推力有限制,生产过程中的生产能力有限制,等等。通常可用下面的不等式来表示

$$\mid u _ {i} (t) \mid \leqslant M _ {i} \quad i = 1, 2, \dots , m$$

这时 $\boldsymbol{U}(t) = [u_{1}(t), u_{2}(t), \cdots, u_{m}(t)]^{\mathrm{T}}$ 属于一个有界的闭集，写成 $\boldsymbol{U}(t) \in \Omega, \Omega$ 为闭集。更一般的情况可用下面的不等式约束来表示。

$$g [ \boldsymbol {U} (t), t ] \geqslant 0$$

当 $U(t)$ 属于有界闭集， $U(t)$ 在边界上取值时， $\delta U$ 就不是任意的了，因为无法向边界外取值，这时 $\frac{\partial H}{\partial U} = 0$ 就不一定是最优解的必要条件。考察由图4-1所表示的几种情况，图中横轴上每一点都表示一个标量控制函数 $u$ ，其容许取值范围为 $\Omega$ 。

对于图 $4 - 1(a)\frac{\partial H}{\partial u} = 0$ 仍对应最优解 $u^{*}$ 。对于图 $4 - 1(b)\frac{\partial H}{\partial u} = 0$ 所对应的解 $u^0$ 不是最优解，最优解 $u^{*}$ 在边界上。对于图 $4 - 1(c)\frac{\partial H}{\partial U} \equiv$ 常数，由这个方程解不出最优控制 $u$ 来（这种情况称为奇异情况），最优解 $u^{*}$ 在边界上。另外， $\frac{\partial H}{\partial U}$ 也不一定是存在的。例如状态方程的右端 $f(X,U,t)$ 对 $U$ 的一阶偏导数可能不连续，或由于有些指标函数，如燃料

![](image/05c99740cfebe318606e701e749b6543c0b35e85e688a8a6253537c80f36df19.jpg)

<details>
<summary>text_image</summary>

H
u*
u
Ω
</details>

(a)

![](image/ecc987381aaf9e0ca286d461da1731f8ddd8539975cde63ed778ca511ff3c416.jpg)

<details>
<summary>text_image</summary>

H
u*
u⁰
u
Ω
</details>

(b)

![](image/06e0abe58078fbd4105f0ad3f187f260d2c17fa8b0367dcc74d65ae263d147e5.jpg)

<details>
<summary>text_image</summary>

H
u*
Ω
u
</details>

(c)   
图4-1 有界闭集内函数的几种形状

最优控制问题中,具有下面的形式:

$$J = \int_ {t _ {0}} ^ {t _ {\mathrm{f}}} F (\boldsymbol {X}, \boldsymbol {U}, t) \mathrm{d} t = \int_ {t _ {0}} ^ {t _ {\mathrm{f}}} | \boldsymbol {U} | \mathrm{d} t$$

这时 $H(X, U, \lambda, t) = F(X, U, t) + \lambda^{\mathrm{T}} f(X, U, t)$ 对 $U$ 的一阶偏导数不连续。

经典变分法无法处理上面的情况,必须另辟新的途径。极小值原理就是解决这类问题的有力工具。用极小值原理求解控制无约束的最优控制问题和古典变分法是完全一样的。1956年前苏联学者庞特里亚金提出这个原理时,把它称为极大值原理,目前较多地采用极小值原理这个名字。下面给出这个原理及其证明,并举例说明其应用。
