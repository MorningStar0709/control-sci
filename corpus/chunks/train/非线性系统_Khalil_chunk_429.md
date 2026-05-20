$$\dot {z} = (A - B K) z$$

其李雅普诺夫函数可取为 $V(z)=z^{T}Pz$ ，其中 P 是李雅普诺夫方程

$$P (A - B K) + (A - B K) ^ {\mathrm{T}} P = - I$$

的解。当 $u = \psi (x) + v$ 时，不确定项 $\delta (x,u)$ 满足不等式

$$\| \delta (x, \psi (x) + v) \| \leqslant \| \Delta_ {1} (x) + \Delta_ {2} (x) \alpha (x) - \Delta_ {2} (x) \gamma^ {- 1} (x) K z \| + \| \Delta_ {2} (x) \| \| v \|$$

这样,为了满足式(14.35),要求不等式

$$\| \Delta_ {2} (x) \| \leqslant \kappa_ {0} < 1 \tag {14.36}$$

和 $\|\Delta_{1}(x)+\Delta_{2}(x)\alpha(x)-\Delta_{2}(x)\gamma^{-1}(x)KT(x)\|\leqslant\rho(x)$ (14.37)

在包含原点的定义域上成立, $\rho(x)$ 为连续函数。不等式(14.36)是限制性的,因为该式给扰动项 $\Delta_{2}$ 施加了一定的限制,而不等式(14.37)则不是限制性的,因为式中的 $\rho$ 不必很小,主要是选择函数 $\rho$ 估计式(14.37)左边函数的增长性的问题。

现在考虑系统(14.30)，并采用控制律 $u=\psi(t,x)+v$ ，则闭环系统

$$\dot {x} = f (t, x) + G (t, x) \psi (t, x) + G (t, x) [ v + \delta (t, x, \psi (t, x) + v) ] \tag {14.38}$$

是标称闭环系统(14.32)的扰动系统。下面计算 $V(t,x)$ 沿式(14.38)轨线的导数。为方便起见，各函数的自变量不再写出。V 的导数为

$$\dot {V} = \frac {\partial V}{\partial t} + \frac {\partial V}{\partial x} (f + G \psi) + \frac {\partial V}{\partial x} G (v + \delta) \leqslant - \alpha_ {3} (\| x \|) + \frac {\partial V}{\partial x} G (v + \delta)$$

设 $w^{\mathrm{T}} = [\partial V / \partial x]G$ ，上面的不等式可改写为

$$\dot {V} \leqslant - \alpha_ {3} (\| x \|) + w ^ {\mathrm{T}} v + w ^ {\mathrm{T}} \delta$$

式中，右边第一项源于标称闭环系统，右边第二项和第三项分别表示控制 $v$ 和不确定项 $\delta$ 对 $\dot{V}$ 的影响。根据匹配条件，上式右端出现的 $\delta$ 恰好与 $v$ 出现在同一处，因而有可能通过选择 $v$ 消除 $\delta$ 对 $\dot{V}$ 的(不稳定)影响。现在我们寻求两种选择 $v$ 的不同方法，使 $\omega^{\mathrm{T}}v + \omega^{\mathrm{T}}\delta \leqslant 0$ 成立。假设不等式(14.35)满足 $\| \cdot \| _2$ ，即

$$\| \delta (t, x, \psi (t, x) + v) \| _ {2} \leqslant \rho (t, x) + \kappa_ {0} \| v \| _ {2}, \quad 0 \leqslant \kappa_ {0} < 1$$

我们有 $w^{\mathrm{T}}v + w^{\mathrm{T}}\delta \leqslant w^{\mathrm{T}}v + \| w\|_{2}\| \delta \|_{2}\leqslant w^{\mathrm{T}}v + \| w\|_{2}[\rho (t,x) + \kappa_{0}\| v\|_{2}]$

取

$$v = - \eta (t, x) \cdot \frac {w}{\| w \| _ {2}} \tag {14.39}$$

$\eta$ 为非负函数, 得

$$w ^ {T} v + w ^ {T} \delta \leqslant - \eta \| w \| _ {2} + \rho \| w \| _ {2} + \kappa_ {0} \eta \| w \| _ {2} = - \eta (1 - \kappa_ {0}) \| w \| _ {2} + \rho \| w \| _ {2}$$

对于所有 $(t,x)\in [0,\infty)\times D$ ，选择 $\eta (t,x)\geqslant \rho (t,x) / (1 - \kappa_0)$ ，得

$$w ^ {\mathrm{T}} v + w ^ {\mathrm{T}} \delta \leqslant - \rho \| w \| _ {2} + \rho \| w \| _ {2} = 0$$

因此,对于控制律(14.39), $V(t,x)$ 沿闭环系统(14.38)轨线的导数是负定的。

另一种方法是假设式(14.35)满足 $\| \cdot \|_{\infty}$ , 即
