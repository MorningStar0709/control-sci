其中, $h(t,\varepsilon)$ 的泰勒级数系数是 $x(t,\varepsilon)$ 的泰勒级数系数的函数。由于式(10.6)对于所有足够小的 $\varepsilon$ 都成立,所以一定对 $\varepsilon$ 恒成立,因此 $\varepsilon$ 的同次幂的系数一定相等。如果这些系数匹配,就可以导出 $x_{0},x_{1}$ 等必须满足的方程。在此之前,还必须产生 $h(t,\varepsilon)$ 的泰勒级数的系数。

0 次项 $h_0(t)$ 为 $h_0(t) = f(t, x_0(t), 0)$

因而,若匹配式(10.6)中 $\varepsilon_{0}$ 的系数,可以确定 $x_{0}(t)$ 满足

$$\dot {x} _ {0} = f (t, x _ {0}, 0), \quad x _ {0} (t _ {0}) = \eta_ {0}$$

毫不奇怪,这就是非扰动问题(10.3)。一次项 $h_{1}(t)$ 为

$$
\begin{array}{l} h _ {1} (t) = \left. \frac {\partial}{\partial \varepsilon} f (t, x (t, \varepsilon), \varepsilon) \right| _ {\varepsilon = 0} \\ = \left. \left\{\frac {\partial f}{\partial x} (t, x (t, \varepsilon), \varepsilon) \frac {\partial x}{\partial \varepsilon} (t, \varepsilon) + \frac {\partial f}{\partial \varepsilon} (t, x (t, \varepsilon), \varepsilon) \right\} \right| _ {\varepsilon = 0} \\ = \frac {\partial f}{\partial x} (t, x _ {0} (t), 0) x _ {1} (t) + \frac {\partial f}{\partial \varepsilon} (t, x _ {0} (t), 0) \\ \end{array}
$$

匹配式(10.6)中 $\varepsilon$ 的系数, 可得 $x_{1}(t)$ 满足

$$\dot {x} _ {1} = \frac {\partial f}{\partial x} (t, x _ {0} (t), 0) x _ {1} + \frac {\partial f}{\partial \varepsilon} (t, x _ {0} (t), 0), \quad x _ {1} (t _ {0}) = \eta_ {1}$$

定义 $A(t) = \frac{\partial f}{\partial x} (t,x_0(t),0),\quad g_1(t,x_0(t)) = \frac{\partial f}{\partial\varepsilon} (t,x_0(t),0)$

重写关于 $x_{1}$ 的方程为 $\dot{x}_1 = A(t)x_1 + g_1(t,x_0(t)),\quad x_1(t_0) = \eta_1$

该线性方程在 $\left[t_{0},t_{1}\right]$ 上有唯一解。

继续这一过程可推导出 $x_{2}, x_{3}$ 等满足的方程, 但其中包含了 $f$ 对 $x$ 的高阶微分, 表示起来过于繁琐。其实没有必要写出方程的通式, 只要概念清楚, 就可以对讨论的特殊问题列出方程。不过为了设定这些方程所采用的模式, 我们还是要推导 $x_{2}$ 满足的方程, 也许读者会感到厌烦。 $h(t, \varepsilon)$ 的泰勒级数中二次系数为

$$h _ {2} (t) = \frac {1}{2} \left. \frac {\partial^ {2}}{\partial \varepsilon^ {2}} h (t, \varepsilon) \right| _ {\varepsilon = 0}$$

现在 $\frac{\partial}{\partial\varepsilon} h(t,\varepsilon) = \frac{\partial f}{\partial x}(t,x,\varepsilon)\frac{\partial x}{\partial\varepsilon}(t,\varepsilon) + \frac{\partial f}{\partial\varepsilon}(t,x,\varepsilon)$

$$= \frac {\partial f}{\partial x} (t, x, \varepsilon) \left[ x _ {1} (t) + 2 \varepsilon x _ {2} (t) + \dots \right] + \frac {\partial f}{\partial \varepsilon} (t, x, \varepsilon)$$

为了简化表达式,设 $\psi(t,x,\varepsilon)=\frac{\partial f}{\partial x}(t,x,\varepsilon)x_{1}(t)$

继续计算 h 对 $\varepsilon$ 的二阶导数：
