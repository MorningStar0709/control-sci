$$a _ {1} \sqrt {\left| x _ {1} - x _ {3} \right|} = \frac {U}{2}, a _ {2} \sqrt {\left| x _ {2} - x _ {3} \right|} = \frac {U}{2} (6. 4. 2 4)$$

由这两式解出

$$x _ {1} = x _ {3} + \frac {U ^ {2}}{4 a _ {1} ^ {2}}, x _ {2} = x _ {3} + \frac {U ^ {2}}{4 a _ {2} ^ {2}} \tag {6.4.25}$$

现在我们把这样解出的 $x_{1},x_{2}$ 分别作为实际状态 $x_{1},x_{2}$ 要跟踪的时变轨迹，即

$$x _ {1} ^ {*} = x _ {3} + \frac {U ^ {2}}{4 a _ {1} ^ {2}}, x _ {2} ^ {*} = x _ {3} + \frac {U ^ {2}}{4 a _ {2} ^ {2}} \tag {6.4.26}$$

然后，分别以 $x_{1}^{*}, x_{2}^{*}$ 为设定值，用自抗扰控制器使状态变量 $x_{1}, x_{2}$ 分别达到这些设定值就能解决三水箱的串级控制问题.

整个过程的控制算法为

(1) 先定虚拟控制量

$$U = \frac {0 . 1 7 5}{\gamma} \pi \mathrm{sin} \Big (\frac {\pi}{\gamma} t \Big) \frac {1 - \mathrm{sign} (t - \gamma)}{2} \text {或} U = \beta \mathrm{fal} (x _ {d} - x _ {3}, \alpha , \delta) \tag {6.4.27}$$

和状态变量 $x_{1}, x_{2}$ 要跟踪的设定值分别为

$$x _ {1} ^ {*} = x _ {3} + \frac {U ^ {2}}{4 a _ {1} ^ {2}}, x _ {2} ^ {*} = x _ {3} + \frac {U ^ {2}}{4 a _ {2} ^ {2}} \tag {6.4.28}$$

(2) 决定控制 $x_{1}$ 的自抗扰控制器为

$$
\left\{ \begin{array}{l} e _ {1} = z _ {1 1} - x _ {1}, \mathrm{fe} _ {1} = \operatorname{fal} \left(e _ {1}, 0. 5, h\right) \\ z _ {1 1} = z _ {1 1} + h \left(z _ {1 2} - \beta_ {0 1} e _ {1} + b u _ {1}\right) \\ z _ {1 2} = z _ {1 2} + h \left(- \beta_ {0 2} \mathrm{fe} _ {1}\right) \\ e _ {0 1} = x _ {1} ^ {*} - z _ {2 1} \\ u _ {1} = \beta_ {1} \operatorname{fal} \left(e _ {0 1}, \alpha_ {1}, h\right) - \frac {z _ {1 2}}{b} \end{array} \right. \tag {6.4.29}
$$

(3) 决定控制 $x_{2}$ 的自抗扰控制器为

$$
\left\{ \begin{array}{l} e _ {2} = z _ {2 1} - x _ {2}, \mathrm{fe} _ {2} = \operatorname{fal} \left(e _ {2}, 0. 5, h\right) \\ z _ {2 1} = z _ {2 1} + h \left(z _ {2 2} - \beta_ {0 1} e _ {2} + b u _ {2}\right) \\ z _ {2 2} = z _ {2 2} + h \left(- \beta_ {0 2} \mathrm{fe} _ {2}\right) \\ e _ {0 2} = x _ {2} ^ {*} - z _ {2 1} \\ u _ {2} = \beta_ {1} \operatorname{fal} \left(e _ {0 3}, \alpha_ {2}, h\right) - \frac {z _ {2 2}}{b} \end{array} \right. \tag {6.4.30}
$$

取对象参数为 $a_1 = 0.015, a_2 = a_1, A = 1.12, b = 6.5$ ，对各水箱分别加上如下扰动： $w_1(t) = 0.4\mathrm{sign}(\sin(0.02t)), w_2(t) = 0.4\cos(0.03t), w_3(t) = 0.0$ ，虚拟控制量取成 $U = \beta \mathrm{fal}(x_d - x_3, \alpha, \delta), \beta = 0.04, \alpha = 0.5, \delta = 1.0, \beta_1 = 0.3$ 所作的仿真结果如图6.4.12所示。这个仿真结果表明，1号、2号水箱的扰动作用 $w_1(t), w_2(t)$ 都被抑制的很好。

虚拟控制量取成 $U = \frac{0.35}{\gamma} \pi \sin \left( \frac{\pi}{\gamma} t \right) \frac{1 - \text{sign}(t - \gamma)}{2}$ 时的仿真结果如图 6.4.13 所示.

这说明虚拟控制量的取法是，让 $x_{3}$ 趋近设定值 $x_{d}$ 的前提下可以灵活选取。例如还可以根据信号 $x_{d}$ 和 $x_{3}$ ，用自抗扰控制器来决定 $U(t)$
