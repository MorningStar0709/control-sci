根据泛函极值的必要条件,令式(10-45)为零,考虑到宗量变分 $\delta x,\delta u$ 和 $\delta x(t_{f})$ 的任意性,及变分预备定理,得如下广义泛函取极值的必要条件:欧拉方程

$$\dot {\lambda} (t) = - \frac {\partial H}{\partial x} \tag {10-46}\frac {\partial H}{\partial \boldsymbol {u}} = \mathbf {0} \tag {10-47}$$

横截条件

$$\boldsymbol {\lambda} \left(t _ {f}\right) = \frac {\partial \varphi}{\partial \boldsymbol {x} \left(t _ {f}\right)} + \frac {\partial \boldsymbol {\psi} ^ {\mathrm{T}}}{\partial \boldsymbol {x} \left(t _ {f}\right)} \boldsymbol {\gamma} \tag {10-48}$$

由于引进哈密顿函数形式(10-43)，使得

$$\dot {\boldsymbol {x}} (t) = \frac {\partial H}{\partial \boldsymbol {\lambda}} = \boldsymbol {f} (\boldsymbol {x}, \boldsymbol {u}, t) \tag {10-49}$$

上式与式(10-46)形成正则形式,其右端都是哈密顿函数的适当偏导数,故将式(10-49)和式(10-46)称为正则方程。因为式(10-49)是众知的状态方程,故称式(10-46)为协态方程,相应的乘子向量 $\lambda(t)$ 称为协态向量。

正则方程(10-49)和方程(10-46)是2n个一阶微分方程组,初始条件 $x(t_{0})=x_{0}$ 和横截条件(10-48)正好为正则方程提供2n个边界条件,根据对 $f(\cdot)$ , $L(\cdot)$ 和 $\varphi(\cdot)$ 的连续性和可微性假设,正则方程可以唯一确定状态向量 $x(t)$ 和协态向量 $\lambda(t)$ 。

对于确定的 $x(t)$ 和 $\lambda(t)$ ，哈密顿函数 $H(\cdot)$ 是控制向量 $u(t)$ 的函数。式(10-47)表明，最优控制 $u^{*}(t)$ 使哈密顿函数 $H(\cdot)$ 取驻值，因此式(10-47)通常称为极值条件或控制方程。由极值条件(10-47)，可以确定最优控制 $u^{*}(t)$ 与最优轨线 $x^{*}(t)$ 和协态向量 $\lambda^{*}(t)$ 之间的关系。

应当指出，正则方程(10-49)、(10-46)与极值条件(10-47)，形成变量间相互耦合的方程组，其边界条件由初始条件、横截条件(10-48)和目标集(10-42)提供，其中目标集条件(10-42)用于联合确定待定的拉格朗日乘子向量 $\gamma$ 。

上述讨论，可以归纳为如下定理。（为便于书写，今后凡不致混淆之处，均省略“\*”号）。

定理 10-6 对于如下最优控制问题：

$$\min _ {\boldsymbol {u} (t)} J = \varphi [ \boldsymbol {x} (t) ] + \int_ {t _ {0}} ^ {t _ {f}} L (\boldsymbol {x}, \boldsymbol {u}, t) d t$$

s. t. ① $\dot{\boldsymbol{x}}(t) = \boldsymbol{f}(\boldsymbol{x},\boldsymbol{u},t),\quad \boldsymbol{x}(t_0) = \boldsymbol{x}_0$

② $\psi [x(t_f)] = 0$

式中， $x\in R^{n}$ ; $u\in R^{m}$ ，无约束且在 $[t_{0},t_{f}]$ 上连续； $\psi\in R^{r}, r\leqslant n$ ；在 $[t_{0},t_{f}]$ 上， $f(\cdot),\psi(\cdot),\varphi(\cdot)$ 和 $L(\cdot)$ 连续且可微； $t_{f}$ 固定。最优解的必要条件为

1) $x(t)$ 和 $\pmb{\lambda}(t)$ 满足正则方程

$$\dot {\boldsymbol {x}} (t) = \frac {\partial H}{\partial \boldsymbol {\lambda}}, \quad \dot {\boldsymbol {\lambda}} (t) = - \frac {\partial H}{\partial \boldsymbol {x}}$$

式中 $H(x,u,\lambda ,t) = L(x,u,t) + \lambda^{\mathrm{T}}(t)f(x,u,t)$

2）边界条件与横截条件
