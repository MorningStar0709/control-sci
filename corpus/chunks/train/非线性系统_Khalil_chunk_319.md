# 10.7 习题

10.1 如果 $\delta(\varepsilon)=O(\varepsilon)$ ，它是否为 $O(\varepsilon^{1/2})$ 或 $O(\varepsilon^{3/2})$ ?

10.2 如果 $\delta(\varepsilon)=\varepsilon^{1/n}$ ，其中 n>1 为正整数。是否存在一个正整数 N，使得 $\delta(\varepsilon)=O(\varepsilon^{N})$ ?

10.3 设初值问题

$$\dot {x} _ {1} = - (0. 2 + \varepsilon) x _ {1} + \frac {\pi}{4} - \arctan x _ {1} + \varepsilon \arctan x _ {2}, x _ {1} (0) = \eta_ {1}\dot {x} _ {2} = - (0. 2 + \varepsilon) x _ {2} + \frac {\pi}{4} - \arctan x _ {2} + \varepsilon \arctan x _ {1}, x _ {2} (0) = \eta_ {2}$$

(a) 求 $O(\varepsilon)$ 逼近。

(b) 求 $O(\varepsilon^{2})$ 逼近。

(c) 研究在无限时间区间上的逼近是否成立。

(d) 用计算机程序计算在时间区间 $[0,3]$ 上，当 $\varepsilon = 0.1, \eta_1 = 0.5$ 和 $\eta_2 = 1.5$ 时的精确解、 $O(\varepsilon)$ 逼近和 $O(\varepsilon^2)$ 逼近。讨论近似的精度。

提示: 在(a)和(b)中, 给出逼近方程即可, 不必求逼近的解析闭式表达式。

10.4 对于系统 $\dot{x}_{1}=x_{2},\quad\dot{x}_{2}=-x_{1}-x_{2}+\varepsilon x_{1}^{3}$

重复习题 10.3, 在(d)中设 $\varepsilon=0.1,\eta_{1}=1.0,\eta_{2}=0.0$ , 时间区间为 [0,5]。

10.5 对于系统 $\dot{x}_{1} = -x_{1} + x_{2}, \quad \dot{x}_{2} = \varepsilon x_{1} - x_{2} - \frac{1}{3} x_{2}^{3}$

重复习题 10.3, 在(d)中设 $\varepsilon=0.2,\eta_{1}=1.0,\eta_{2}=0.0$ , 且时间区间为 [0,4]。

10.6 （见文献[166]）对于系统

$$\dot {x} _ {1} = x _ {1} - x _ {1} ^ {2} + \varepsilon x _ {1} x _ {2}, \quad \dot {x} _ {2} = 2 x _ {2} - x _ {2} ^ {2} - \varepsilon x _ {1} x _ {2}$$

重复习题 10.3, 在(d)中设 $\varepsilon=0.2,\eta_{1}=0.5,\eta_{2}=1.0$ , 且时间区间为 [0,4]。

10.7 对于系统 $\dot{x}_1 = -x_1 + x_2(1 + x_1) + \varepsilon (1 + x_1)^2,$ $\dot{x}_2 = -x_1(x_1 + 1)$

重复习题 10.3, 在(d)中设 $\varepsilon = -0.1, \eta_{1} = -1, \eta_{2} = 2$ 。当 $\varepsilon = -0.05$ 和 $\varepsilon = -0.2$ 时重新计算, 并讨论逼近精度。

10.8 考虑初值问题 $\dot{x}_1 = -x_1 + \varepsilon x_2, x_1(0) = \eta$

$$\dot {x} _ {2} = - x _ {2} - \varepsilon x _ {1}, \quad x _ {2} (0) = \eta$$

求 $O(\varepsilon)$ 逼近。对于两组不同的初始条件(1) $\eta=1,(2)\eta=10$ ，计算当 $\varepsilon=0.1$ 时的精确解和近似解，讨论逼近精度。解释与定理 10.1 的差异。

10.9 （见文献[70]）运用平均化法研究下列各标量系统：

(1) $\dot{x} = \varepsilon (x - x^{2})\sin^{2}t$

(2) $\dot{x} = \varepsilon (x\cos^2 t - \frac{1}{2} x^2)$

(3) $\dot{x} = \varepsilon(-x + \cos^{2} t)$

(4) $\dot{x} = -\varepsilon x \cos t$

10.10 对于下列各系统,证明对于充分小的 $\varepsilon > 0$ , 原点是指数稳定的:

$$
\begin{array}{l} \dot {x} _ {2} = - \varepsilon (1 + 2 \sin t) x _ {2} - \varepsilon (1 + \cos t) \sin x _ {1} \\ \dot {x} _ {2} = \varepsilon [ (- 1 - 1. 5 \sin t \cos t) x _ {1} + (- 1 + 1. 5 \sin^ {2} t) x _ {2} ] \tag {2} \\ \end{array}
$$

$\dot{x}_{1}=\varepsilon x_{2}$
