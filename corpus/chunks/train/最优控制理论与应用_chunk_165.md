$$
\left\{ \begin{array}{l} \dot {x} _ {1} = x _ {2} - \operatorname{sgn} \left\{\lambda_ {1} - \lambda_ {2} \right\} \\ \dot {x} _ {2} = \operatorname{sgn} \left\{\lambda_ {1} - \lambda_ {2} \right\} \\ \dot {\lambda} _ {1} = - x _ {1} \\ \dot {\lambda} _ {2} = - \lambda_ {1} \end{array} \right. \tag {9-25}
$$

因为 H 曲线可能依赖于 u，所以可能存在奇异弧，满足

$$\frac {\partial H}{\partial u} = \lambda_ {1} - \lambda_ {2} = 0 \tag {9-26}\frac {\mathrm{d}}{\mathrm{d} t} \left(\frac {\partial H}{\partial u}\right) = \dot {\lambda} _ {1} - \dot {\lambda} _ {2} = - x _ {1} + \lambda_ {1} = 0 \tag {9-27}H = \frac {1}{2} x _ {1} ^ {2} + \lambda_ {1} x _ {2} + \left(\lambda_ {1} - \lambda_ {2}\right) u = C (\text {常数}) \tag {9-28}$$

当 $T$ 是给定的有限时间， $C$ 为某一常数。若 $T$ 自由时，则 $C = 0$ ，由式(9-26)～(9-28)解得

$$\frac {1}{2} x _ {1} ^ {2} + x _ {1} x _ {2} = C \tag {9-29}$$

上式表示一个单参数的双曲线族。如果存在奇异弧，它必是某一特定双曲线的一部分。现在进一步利用条件

$$\frac {\mathrm{d} ^ {2}}{\mathrm{d} t ^ {2}} \left(\frac {\partial H}{\partial u}\right) = - \dot {x} _ {1} + \dot {\lambda} _ {1} = - x _ {2} - u - x _ {1} = 0 \tag {9-30}$$

解得

$$u = - \left(x _ {1} + x _ {2}\right) \tag {9-31}$$

此即奇异弧上的最优控制,它是状态的线性反馈。

现在讨论如下两种情况。

（1）T 为给定的有限值，式(9-29)中的常数 C 是取决于初态的非零值。这时，奇异弧是双曲线，它不通过原点，因此，不是最优轨线的最后一段弧线。典型的最优轨线由三段组成：

第一段控制取其边界值 $\pm1$ ，将系统转移到奇异弧上。

第二段采用状态的线性反馈控制律(9-31)，系统沿着双曲线奇异弧运动。

第三段是再一次应用 $u = \mp 1$ ，使系统沿着为 Bang - Bang 弧转移到坐标原点。

下面讨论一种控制不受约束的特殊情况(见图9-1)。这时,第一段是脉冲控制(控制的幅度为无穷大,持续时间为无穷小)。脉冲控制所对应的轨线可由下式定出

$$
\begin{array}{l} \frac {\mathrm{d} x _ {2}}{\mathrm{d} x _ {1}} = - \frac {u}{x _ {2} + u} \\ \lim _ {u \rightarrow \infty} \frac {\mathrm{d} x _ {2}}{\mathrm{d} x _ {1}} = - 1 \tag {9-32} \\ \end{array}
\lim _ {u \rightarrow - \infty} \frac {\mathrm{d} x _ {2}}{\mathrm{d} x _ {1}} = - 1
$$

![](image/9df501de01186d1bdfef166bd7a751cdd1488424cfed5aeae007ee3fefa15734.jpg)

<details>
<summary>text_image</summary>

x₂
A(t=0)
(t=T)
O
x₁
C(t=T-)
B(t=0+)
奇异弧
</details>

图9-1 最优轨线

在 $x_{1} - x_{2}$ 相平面上，这是一条斜率为-1的直线。正的脉冲控制导致状态向右下方移动，而负的脉冲控制会使状态向左上方转移。因此，假如已知的初态为图中的 $A$ 点，则最优轨线ABCO如图9-1所示。利用脉冲函数的控制，系统的状态沿 $(x_{1} + x_{2})$ 等于常数的直线瞬时地由 $A$ 转移到 $B$ 点。在奇异弧上，使用式(9-31)的控制律，由状态方程解得

$$x _ {1} (t) = x _ {1} \left(0 _ {+}\right) \mathrm{e} ^ {- t} \tag {9-33}$$

$x_{1}$ 的大小随时间按指数规律减小，状态按着箭头所示的方向沿奇异弧变化，当 $t = T$ 时到达直线 $x_{1} + x_{2} = 0$ 。此后，再用一个负脉冲控制，系统瞬

时地转移到原点。
