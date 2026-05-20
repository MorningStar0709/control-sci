$$\boldsymbol {U} (t) = - \boldsymbol {R} ^ {- 1} (t) \boldsymbol {B} ^ {\mathrm{T}} (t) [ \boldsymbol {K} (t) \boldsymbol {X} (t) - \boldsymbol {g} (t) ] \tag {5-103}$$

$U(t)$ 中一项与状态 $X(t)$ 成正比（同状态调节问题），另一项与时间函数 $\pmb{g}(t)$ 成正比，而 $\pmb{g}(t)$ 是与理想输出 $\mathbf{Z}(t)$ 有关的，故它表示了跟踪 $\mathbf{Z}(t)$ 的驱动作用。

值得指出的是:为了求出当时时刻的 $g(t)$ ，需要知道全部未来时刻的 $Z(\tau), t \leqslant \tau \leqslant t_{f}$ 。这是因为积分 (5 - 100) 求 $g(t)$ 是从 $t_{f}$ 逆时间进行的。于是在实现最优控制时，必须预先知道 $Z(t)$ 在 $[t_{0}, t_{f}]$ 中的变化规律。在某些情况下能做到这点，如跟踪卫星时，卫星的运动可事先计算出来。但大部分情况下 $Z(t)$ 的将来值是未知的，如导弹攻击敌机，敌机的运动规律不知道。这时可有两种处理方法：一种是根据对 $Z(t)$ 的测量，预报它的将来值，另一种是将 $Z(t)$ 看成随机的。用后一种处理方法时，当然只能得到统计平均意义下的最优。

例5-6 已知一阶系统

$$\dot {x} (t) = a x (t) + u (t)y (t) = x (t) \tag {5-104}$$

性能指标为

$$J = \frac {1}{2} p e ^ {2} \left(t _ {\mathrm{f}}\right) + \frac {1}{2} \int_ {0} ^ {t _ {\mathrm{f}}} \left[ q e ^ {2} (t) + r u ^ {2} (t) \right] \mathrm{d} t \quad (5 - 1 0 5)$$

其中 $p \geqslant 0, q > 0, r > 0$ 。寻找最优控制 $u(t)$ 使 $J$ 最小。

解 由式(5-104)、(5-105)知 A=a,B=1,C=1,Q=q,R=r,P=p 由式(5-103)得

$$u (t) = \frac {1}{r} [ g (t) - K (t) x (t) ] \tag {5-106}$$

由式(5-99)可得标量函数 $K(t)$ 满足下面的一阶黎卡提方程

$$\dot {K} (t) = - 2 a K (t) + \frac {1}{r} K ^ {2} (t) - q \tag {5-107}$$

由式(5-101)求得边界条件

$$K (t _ {\mathrm{f}}) = p$$

标量函数 $g(t)$ 满足微分方程(5-100)，即

$$\dot {g} (t) = - \left[ a - \frac {1}{r} K (t) \right] g (t) - q Z (t)$$

边界条件由式(5-102)求得为

$$g (t _ {\mathrm{f}}) = p Z (t _ {\mathrm{f}})$$

最优轨线 $x(t) = y(t)$ 由式(5-95)求得

$$\dot {x} (t) = \left[ a - \frac {1}{r} K (t) \right] x (t) + \frac {1}{r} g (t)$$

图5-5（a）表示了当 $a = -1, x(0) = 0, p = 0, q = 1, t_{\mathrm{f}} = 1$ 和理想输出 $Z(t) = 1(t)$ 时，以 $r$ 为参数的最优 $x(t)$ 的一组曲线。由图可见，随着 $r$ 的减小， $x(t)$ 跟踪 $Z(t)$ 的能力增强。此外，在接近 $t_{\mathrm{f}} = 1$ 时，跟踪误差又回升，这时因为 $p = 0, g(t_{\mathrm{f}}) = K(t_{\mathrm{f}}) = 0$ ，使 $u(t_{\mathrm{f}}) = 0$ 的缘故。图5-5（b）表示了最优控制曲线，随着 $r$ 的减小， $u(t)$ 增大，所以提高跟踪能力是以增大控制量为代价的。图5-5（c）是 $g(t)$ 的变化曲线。由图5-5（a）可见当 $r = 0.01$ ，也就是 $q$ 的百分之一时，控制量较大才获得较好的跟踪性能。

![](image/5763ac11dd569a75969882d92a7650e81ee753cd7afd12984775b6f30a622c7f.jpg)

<details>
<summary>line</summary>

| t | x(t) for r=0.01 | x(t) for r=0.1 | x(t) for r=1 |
| --- | --- | --- | --- |
| 0.0 | 0.0 | 0.0 | 0.0 |
| 0.5 | ~0.8 | ~0.6 | ~0.2 |
| 1.0 | ~0.7 | ~0.5 | ~0.3 |
</details>

(a)

![](image/a6518fddc9c015b9d841b86cc8de620b463e54eabe440f056cddec22dc9ce68c.jpg)

<details>
<summary>line</summary>

| t | u(t) for r=0.01 | u(t) for r=0.1 |
| --- | --- | --- |
| 0.0 | 0.0 | 0.0 |
| 0.5 | ~0.1 | ~0.05 |
| 1.0 | 0.0 | 0.0 |
</details>

(b)

![](image/87c9de621d19c00caa5e23bd084539157bb0c84d62341896949318356df3671e.jpg)

<details>
<summary>line</summary>

| t | g(t) for r=1 | g(t) for r=0.1 | g(t) for r=0.01 |
| --- | --- | --- | --- |
| 0.0 | 1 | 1 | 1 |
| 0.5 | ~0.67 | ~0.48 | ~0.32 |
| 1.0 | 0 | 0 | 0 |
</details>

(c)   
图5-5 $x(t), u(t), g(t)$ 以 $r$ 为参数的时间曲线
