$$\dot {x} = \frac {\partial H}{\partial \lambda} = u \quad \dot {\lambda} = - \frac {\partial H}{\partial x} = 0$$

控制方程是

$$\frac {\partial H}{\partial u} = u + \lambda = 0 \quad u = - \lambda$$

因边界条件全部给定,故不用横截条件。确定最优终端时刻的条件式(3-57)为

$$H (t _ {\mathrm{f}}) = - \frac {\partial \theta}{\partial t _ {\mathrm{f}}} = - \frac {\partial \phi}{\partial t _ {\mathrm{f}}} = - \frac {\partial t _ {\mathrm{f}}}{\partial t _ {\mathrm{f}}} = - 1\frac {1}{2} u ^ {2} \left(t _ {\mathrm{f}}\right) + \lambda \left(t _ {\mathrm{f}}\right) u \left(t _ {\mathrm{f}}\right) = - 1$$

将 $u(t) = -\lambda (t)$ 代入，可得

$$\frac {1}{2} \lambda^ {2} (t _ {f}) - \lambda^ {2} (t _ {f}) + 1 = 0$$

由上式求得 $\lambda(t_{\mathrm{f}})=\sqrt{2}$ 。因为由正则方程 $\dot{\lambda}=0$ ，所以 $\lambda(t)=\lambda(t_{\mathrm{f}})=\sqrt{2}$ 于是最优控制

$$u ^ {*} (t) = - \sqrt {2}$$

再由正则方程 $\dot{x} = u = -\lambda$ ，可得

$$x (t) = - \sqrt {2} t + c$$

由初始条件 $x(0) = 1$ ，求得 $c = 1$ ，故最优轨迹为

$$x ^ {*} (t) = - \sqrt {2} t + 1$$

以终端条件 $x^{*}(t_{\mathrm{f}}^{*}) = 0$ 代入上式，即求得最优终端时刻 $t_\mathrm{f}^* = \frac{\sqrt{2}}{2}$ 。

例3-6 火箭发射最优程序问题。设火箭在垂直平面内运动，加速度 $a(t)$ 与水平面夹角为 $\theta(t), \theta(t)$ 是控制作用，见图3-4。令

$$x _ {1} = V _ {L} (t) \quad (\text { 水 平 速 度 })x _ {2} = V _ {h} (t) \quad (\text { 垂直速度 })x _ {3} = L (t) \quad (\text { 水 平 距 离 })x _ {4} = h (t) \quad (\text {垂直高度})$$

忽略重力和空气阻力时,系统的状态方程和初始条件为

$$\dot {x} _ {1} = a \cos \theta \quad x _ {1} (0) = 0$$

![](image/8b147709631021aa2b2e2f6faeab0c641bcfc18f6e391858a61539cbab7f510c.jpg)

<details>
<summary>text_image</summary>

h=x₄
a
V
θ
Vₕ-λ
Vₗ-x
h
L-x
</details>

图3-4 火箭发射示意图

$$
\begin{array}{l} \dot {x} _ {2} = a \sin \theta \quad x _ {2} (0) = 0 \\ \dot {x} _ {3} = x _ {1} \quad x _ {3} (0) = 0 \\ \dot {x} _ {4} = x _ {2} \quad x _ {4} (0) = 0 \tag {3-58} \\ \end{array}
$$

终端状态为

$$x _ {1} (t _ {\mathrm{f}}) = U \quad x _ {2} (t _ {\mathrm{f}}) = 0 \quad x _ {3} (t _ {\mathrm{f}}) \text {自由} x _ {4} (t _ {\mathrm{f}}) = h _ {\mathrm{f}}$$

要求选择最优控制程序 $u(t)=\theta(t)$ ，使性能指标

$$J = \int_ {0} ^ {t _ {\mathrm{f}}} \mathrm{d} t = t _ {\mathrm{f}}$$

为最小。

解 因为要求 $t_{f}$ 最小, 故是 $t_{f}$ 自由问题。由给定的终端状态可得三个约束方程为

$$
\begin{array}{l} G _ {1} = x _ {1} \left(t _ {\mathrm{f}}\right) - U = 0 \\ G _ {2} = x _ {2} \left(t _ {\mathrm{f}}\right) = 0 \\ G _ {3} = x _ {4} \left(t _ {\mathrm{f}}\right) - h _ {\mathrm{f}} = 0 \tag {3-59} \\ \end{array}
$$

作哈密顿函数

$$H = F + \lambda^ {T} f = 1 + \lambda_ {1} a \cos \theta + \lambda_ {2} a \sin \theta + \lambda_ {3} x _ {1} + \lambda_ {4} x _ {2}$$

协态方程为
