# 6.5 混沌系统的自抗扰控制

我们在第四章已讨论过混沌系统的观测问题．用同一个状态观测器跟踪不同混沌系统状态是很好的．既然能够很好地跟踪混沌系统的状态，用自抗扰控制器来控制混沌系统，让它来实现已给

的某种动态行为是完全可以的.

考察如下两个常见混沌系统的控制问题,对 Lorenz 系统

$$
\left\{ \begin{array}{l} \dot {x} _ {1} = \sigma (x _ {2} - x _ {1}) \\ \dot {x} _ {2} = \rho x _ {1} - x _ {2} - x _ {1} x _ {3} \\ \dot {x} _ {3} = - b x _ {3} + x _ {1} x _ {2} \\ y = x _ {1} \end{array} \right. \tag {6.5.1}
$$

其中， $\sigma = 10, \rho = 28, b = \frac{8}{3}, x_{1}(0) = -4.47, x_{2}(0) = -0.505,$ $x_{3}(0)=28.02.$

控制力加在不同通道上的两种情形进行仿真研究(图6.5.1)

(1) $\left\{ \begin{array}{l} \dot{x}_1 = \sigma (x_2 - x_1) + u \\ \dot{x}_2 = \rho x_1 - x_2 - x_1x_3 \\ \dot{x}_3 = -bx_3 + x_1x_2 \\ y = x_1 \end{array} \right.$

(2) $\left\{ \begin{array}{l} \dot{x}_1 = \sigma (x_2 - x_1) \\ \dot{x}_2 = \rho x_1 - x_2 - x_1x_3 + u \\ \dot{x}_3 = -bx_3 + x_1x_2 \\ y = x_1 \end{array} \right.$ (6.5.2)

控制器的具体算法如下：

$$
\left\{ \begin{array}{l} \mathrm{fs} = - r ^ {2} (v _ {1} - v) + 2 r v _ {2} \\ v _ {1} = v _ {1} + h v _ {2} \\ v _ {2} = v _ {2} + h \mathrm{fs} \end{array} \right.
$$

安排过渡过程 (6.5.3)

$$
\left\{ \begin{array}{l} e = z _ {1} - y \\ \mathrm{fe} _ {1} = \operatorname{fal} (e, 0. 5, h) \\ \mathrm{fe} _ {2} = \operatorname{fal} (e, 0. 2 5, h) \\ z _ {1} = z _ {1} + h \left(z _ {2} - \beta_ {0 1} e\right) \\ z _ {2} = z _ {2} + h \left(z _ {3} - \beta_ {0 2} \mathrm{fe} _ {1} + u\right) \\ z _ {3} = z _ {3} + h \left(- \beta_ {0 3} \mathrm{fe} _ {2}\right) \end{array} \right.
$$

估计对象状态和总和扰动

(6.5.4)

$$
\left\{ \begin{array}{l l} e _ {1} = v _ {1} - z _ {1} \\ e _ {2} = v _ {2} - z _ {2} \\ u = \beta_ {1} e _ {1} + \beta_ {2} e _ {2} - z _ {3} \end{array} \right. \quad \text { 控制量 } \tag {6.5.5}
$$

我们取采样步长 $h = 0.001$ ，扩张状态观测器参数为 $\beta_{01} = 1000$ $\beta_{02} = 6000, \beta_{03} = 30000.$ 而反馈增益取成 $\beta_{1} = 300, \beta_{2} = 1.0.$ 设定值取成 $v(t) = 1.0$ 时，安排过渡过程的参数取成 $r = 1.0.$

![](image/2006870a6f6585487bfeff1bee3481be72baaf4e1d4f2181c2777f1b1547176f.jpg)  
图6.5.1

设定值取成 $v(t) = \sin (t) + \cos (t)$ 时，安排过渡过程的参数取成 $r = 50$ . 用式(6.5.3)，式(6.5.4)，式(6.5.5)决定的自抗扰控制器对(1)，(2)两种情形仿真的结果如图6.5.2所示.

![](image/f42fcb8f30df1b2e8390ba7f6bb4086d2a82652b0dd05374f224e2e101c6e4d5.jpg)  
图6.5.2

对 Chua 电路系统

$$
\left\{ \begin{array}{l} \dot {x} _ {1} = a \left[ x _ {2} - \phi \left(x _ {1}\right) \right] \\ \dot {x} _ {2} = x _ {1} - x _ {2} + x _ {3} \\ \dot {x} _ {3} = b x _ {2} \\ y = x _ {1} \end{array} \right. \tag {6.5.6}
$$

其中， $\phi (x) = m_1x + \frac{1}{2} (m_0 - m_1)(|x + c| - |x - c|),a = 9,$
