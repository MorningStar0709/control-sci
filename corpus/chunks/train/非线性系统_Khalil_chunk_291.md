$$
\begin{array}{l} \frac {\partial^ {2}}{\partial \varepsilon^ {2}} h (t, \varepsilon) = \frac {\partial \psi}{\partial x} (t, x, \varepsilon) \frac {\partial x}{\partial \varepsilon} (t, \varepsilon) + \frac {\partial}{\partial \varepsilon} \frac {\partial f}{\partial x} (t, x, \varepsilon) x _ {1} (t) \\ + 2 \frac {\partial f}{\partial x} (t, x, \varepsilon) x _ {2} (t) + \frac {\partial}{\partial x} \frac {\partial f}{\partial \varepsilon} (t, x, \varepsilon) \frac {\partial x}{\partial \varepsilon} (t, \varepsilon) \\ + \frac {\partial^ {2} f}{\partial \varepsilon^ {2}} (t, x, \varepsilon) + \varepsilon [ \cdot ] \\ \end{array}
$$

这样， $h_2(t) = A(t)x_2(t) + g_2(t,x_0(t),x_1(t))$

其中

$$
\begin{array}{l} g _ {2} (t, x _ {0} (t), x _ {1} (t)) = \frac {1}{2} \frac {\partial \psi}{\partial x} (t, x _ {0} (t), 0) x _ {1} (t) + \frac {\partial}{\partial \varepsilon} \frac {\partial f}{\partial x} (t, x _ {0} (t), 0) x _ {1} (t) \\ + \frac {1}{2} \frac {\partial^ {2} f}{\partial \varepsilon^ {2}} (t, x _ {0} (t), 0) \\ \end{array}
$$

匹配式(10.6)中 $\varepsilon^{2}$ 的系数,得

$$\dot {x} _ {2} = A (t) x _ {2} + g _ {2} \left(t, x _ {0} (t), x _ {1} (t)\right), \quad x _ {2} \left(t _ {0}\right) = \eta_ {2}$$

归纳起来,泰勒级数的系数 $x_{0}, x_{1}, \cdots, x_{N-1}$ 可通过解下列方程获得

$$\dot {x} _ {0} = f (t, x _ {0}, 0), \quad x _ {0} (t _ {0}) = \eta_ {0} \tag {10.7}\dot {x} _ {k} = A (t) x _ {k} + g _ {k} \left(t, x _ {0} (t), \dots , x _ {k - 1} (t)\right), \quad x _ {k} \left(t _ {0}\right) = \eta_ {k} \tag {10.8}$$

其中， $k=1,2,\cdots,N-1,A(t)$ 是雅可比矩阵 $[\partial f/\partial x]$ 在 $x=x_{0}(t)$ 和 $\varepsilon=0$ 的值， $g_{k}(t,x_{0}(t),x_{1}(t),\cdots,x_{k-1}(t))$ 项是关于 $x_{1},\cdots,x_{k-1}$ 的一个多项式，其系数连续依赖于t和 $x_{0}(t)$ 。假设$x_0(t)$ 定义在 $[t_0, t_1]$ 上意味着 $A(t)$ 也定义在同一区间上。因此，线性方程(10.8)在 $[t_0, t_1]$ 上有唯一解。现在用二阶例子说明如何计算泰勒级数系数。

例 10.2 考虑范德波尔(Van der Pol)状态方程

$$\dot {x} _ {1} = x _ {2}, \quad x _ {1} (0) = \eta_ {1} (\varepsilon)\dot {x} _ {2} = - x _ {1} + \varepsilon \left(1 - x _ {1} ^ {2}\right) x _ {2}, \quad x _ {2} (0) = \eta_ {2} (\varepsilon)$$

假设希望构造一个 N=3 的有限项泰勒级数。设

$$x _ {i} = x _ {i 0} + \varepsilon x _ {i 1} + \varepsilon^ {2} x _ {i 2} + \varepsilon^ {3} R _ {x _ {i}}, i = 1, 2$$

和 $\eta_{i} = \eta_{i0} + \varepsilon \eta_{i1} + \varepsilon^{2}\eta_{i2} + \varepsilon^{3}R_{\eta_{i}}, i = 1,2$

将 $x_{1},x_{2}$ 的级数代入状态方程,得
