$$\Pi_ {1} (x) = \frac {\partial V}{\partial x} f (x) + \frac {1}{2} \frac {\partial V}{\partial x} \left\{\frac {1}{\gamma^ {2}} g _ {1} (x) g _ {1} ^ {\mathrm{T}} (x) - g _ {2} (x) g _ {2} ^ {\mathrm{T}} (x) \right\} \frac {\partial^ {\mathrm{T}} V}{\partial x} + \frac {1}{2} h _ {1} ^ {\mathrm{T}} (x) h _ {1} (x), \tag {6.8.27}\Pi_ {2} (x, \xi) = \frac {\partial W}{\partial x _ {e}} f _ {e} (x _ {e}) + \frac {1}{2 \gamma^ {2}} \frac {\partial W}{\partial x _ {e}} E (x _ {e}) E ^ {\mathrm{T}} (x _ {e}) \frac {\partial^ {\mathrm{T}} W}{\partial x _ {e}} + \frac {1}{2} h _ {e} ^ {\mathrm{T}} (x _ {e}) h _ {e} (x _ {e}). \tag {6.8.28}$$

将 $U(x_{e})$ 代入式(6.8.25)并经整理，可以得到

$$
\begin{array}{l} \frac {\partial U}{\partial x _ {e}} F \left(x _ {e}\right) + \frac {1}{2 \gamma^ {2}} \frac {\partial U}{\partial x _ {e}} E \left(x _ {e}\right) E ^ {\mathrm{T}} \left(x _ {e}\right) \frac {\partial^ {\mathrm{T}} U}{\partial x _ {e}} \\ + \frac {1}{2} H ^ {\mathrm{T}} (x _ {e}) H (x _ {e}) = \Pi_ {1} (x) + \Pi_ {2} (x, \xi). \tag {6.8.29} \\ \end{array}
$$

由此可见，从不等式(6.8.20)，(6.8.21)得出 $U$ 满足Hamilton-Jacobi不等式(6.8.25).

以下我们证明闭环系统 (6.8.24) 的稳定性. 根据 $\gamma$ -耗散性与 Hamilton-Jacobi 不等式的关系 (见定理 6.7.1), 满足不等式 (6.8.10) 的 $U(x_{e})$ 一定满足耗散不等式

$$\dot {U} \leqslant \frac {1}{2} (\gamma^ {2} \| w \| ^ {2} - \| z \| ^ {2}).$$

因此当 $w = 0$ 时，沿闭环系统

$$\dot {x} _ {e} = F (x _ {e}) \tag {6.8.30}$$

的状态轨迹有

$$\dot {U} \leqslant - \frac {1}{2} \| z \| ^ {2} \leqslant 0,$$

从而 $\dot{U} = 0$ 仅当 $z = 0$ ，即

$$h _ {1} (x) = 0, \quad \alpha (\xi) = 0. \tag {6.8.31}$$

此时的状态轨迹满足

$$
\left\{ \begin{array}{l} \dot {x} = f (x), \\ \dot {\xi} = f (\xi) + \frac {1}{\gamma^ {2}} g _ {1} (\xi) \beta (\xi) - G h _ {2} (\xi). \end{array} \right. \tag {6.8.32}
$$

根据 $(f(x), h_1(x))$ 的零状态能检测性假设，以及自由系统(6.8.22)在零点是渐近稳定的假设，满足上述动态方程的 $x(t)$ 和 $\xi(t)$ 将趋近于零。于是由LaSalle不变原理(第2章)，闭环系统(6.8.24)在原点 $x = 0, \xi = 0$ 是渐近稳定的。

注6.8.1 与状态反馈的情况一样, 当广义受控对象具有线性结构时, 定理6.8.3给出的输出反馈 $H_{\infty}$ 控制器与定理6.6.1给出的控制器是等价的。可以证明, 在线性的情况下, 由Hamilton-Jacobi不等式描述的条件实际上等价于定理6.6.1的Riccati方程所描述的条件。感兴趣的读者可参阅文献[15].

注6.8.2 比较本节给出的状态反馈与输出反馈控制器可知，反馈律 $\alpha (\cdot)$ 与推论6.8.1给出的状态反馈控制器是等价的．因此，从控制器的结构上看，定理6.8.3的输出反馈控制器实际上是基于状态观测器

$$\dot {\xi} = f (\xi) + g _ {2} (\xi) u + \frac {1}{\gamma^ {2}} g _ {1} (\xi) \beta (\xi) + G (y - h _ {2} (\xi))$$

实现的 $H_{\infty}$ 状态反馈控制器，即 $\xi$ 是广义受控对象的状态 $x$ 的一个估计，而且与线性系统的情况一样，上述观测器中的 $\frac{1}{\gamma^2}\beta (\xi)$ 正是最劣干扰输入的一个估计.
