# 10.3 波音 747 的横向和纵向控制

波音747（见图10.29）是一种大型宽体喷气式运输机。飞机运行时的相关坐标示意图如图10.30所示。波音747的(刚体)运动线性方程组是八阶的，但可将其拆分为2个四阶方程组，即分别代表纵向运动扰动（见图10.30中的 $U, W, \theta$ 和 $q$ )和横向运动扰动 $(\varphi, \beta, r$ 和 $p)$ 。纵向运动由横轴 $(X)$ 、竖轴 $(Z)$ 和俯仰 $(\theta, q)$ 运动构成；而横向运动由滚转 $(\varphi, p)$ 和偏航 $(r, \beta)$ 运动构成。侧偏角 $\beta$ 是飞机前向速度方向与机头方向之间的夹角。升降舵控制面和节流阀影响纵向运动，而副翼和方向舵主要影响横向运动。尽管横向运动和纵向运动会有微弱的耦合，但这点常常被忽略，因此对飞行器控制系统设计或增稳而言，飞行器的运动方程可以分成两个解耦的四阶方程组。

![](image/b4142df7db49bd5a6813964f3167398a597f61e5e8c482a440736dff48516a82.jpg)

<details>
<summary>natural_image</summary>

Black-and-white photo of a large airplane in flight with visible tail number 7457 and fuselage number 1482 (no text or symbols on the aircraft body)
</details>

图 10.29 波音 747

![](image/60851cbe4585f4158b8ff1adcde1fb19438c4b957acf8961c5a733234dcc731c.jpg)

<details>
<summary>text_image</summary>

速度矢量
β
x, u
α
φ, p
θ, q
y, v
方向舵
δr
升降舵 δe
副翼 δa
ψ, r
z, w
x, y, z 为位置坐标
u, y, w 为速度坐标
p 为滚动速率
q 为俯仰速率
r 为偏航速率
φ 为滚动角
θ 为俯仰角
ψ 为偏航角
β 为侧偏角
α 为攻角
</details>

图 10.30 飞行器坐标系的定义

在适当的假设下 $^{②}$ ，可以推导出在自身坐标系下的非线性刚体运动方程布顿森（Bryson，1994年）：

$$m (\dot {U} + q W - r V) = X - m g \sin \theta + \kappa T \cos \thetam (\dot {V} + r U - p W) = Y + m g \cos \theta \sin \varphi \tag {10.16}m (\dot {W} + p V - q U) = Z + m g \cos \theta \cos \varphi - \kappa T \sin \thetaI _ {x} \dot {p} + I _ {x z} \dot {r} + \left(I _ {z} - I _ {y}\right) q r + I _ {x z} q p = LI _ {y} \dot {q} + \left(I _ {x} - I _ {z}\right) p r + I _ {x z} \left(r ^ {2} - p ^ {2}\right) = MI _ {z} \dot {r} + I _ {x z} \dot {p} + \left(I _ {y} - I _ {x}\right) q p - I _ {x z} q r = N \tag {10.17}$$

其中：m 为飞行器的质量； $[U, V, W]$ 为质心速度的机体轴线分矢量；

$$\beta = \operatorname{arc} \tan \left(\frac {V}{U}\right)$$

$[U_0, V_0, W_0]$ 为参考速度； $[p, q, r]$ 为飞行器角速度的机体轴线分矢量； $[X, Y, Z]$ 为关于质心的机体轴线空气动力； $[L, M, N]$ 为关于质心的机体轴线空气动力扭矩； $g_0$ 为单位质量的重力； $I_i$ 为轴体惯量； $(\theta, \varphi)$ 为飞行器机体的欧拉俯仰角和滚转角； $V_{\mathrm{ref}}$ 为参考飞行速度； $T$ 为推进力的合力； $\kappa$ 为推进力与机体 $x$ 轴的夹角。

对上述方程组的线性化可按如下步骤进行：在稳态的垂直、水平以及匀速飞行的条件下， $\dot{U}=\dot{V}=\dot{W}=\dot{p}=\dot{q}=\dot{r}=0$ 。此外，假定在任意的轴向上无转动以便使得 $p_{0}=q_{0}=r_{0}=0$ ，并且当机翼保持水平时， $\varphi=0$ 。然而，为了给机翼提供抵消飞行器重力的升力，系统将存在一个攻角，因此， $\theta_{0}\neq0$ 且 $W_{0}\neq0$ ，其中，

$$U = U _ {0} + uV = V _ {0} + v \tag {10.18}W = W _ {0} + w$$

稳态速度机体轴线分矢量为

$$U _ {0} = V _ {\text { ref }} \cos \theta_ {0}V _ {0} = 0 \left(\beta_ {0} = 0\right) \tag {10.19}W _ {0} = V _ {\text { ref }} \sin \theta_ {0}$$
