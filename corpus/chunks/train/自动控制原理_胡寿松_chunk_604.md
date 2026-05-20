当 $b_{n} = 0$ 时，可以令上述公式中的 $h_0 = 0$ 得到所需要的结果，也可按如下规则选择另一组状态变量。设

$$
\left. \begin{array}{l} x _ {n} = y \\ x _ {i} = \dot {x} _ {i + 1} + a _ {i} y - b _ {i} u; \quad i = 1, 2, \dots , n - 1 \end{array} \right\} \tag {9-12}
$$

其展开式为

$$x _ {n - 1} = \dot {x} _ {n} + a _ {n - 1} y - b _ {n - 1} u = \dot {y} + a _ {n - 1} y - b _ {n - 1} ux _ {n - 2} = \dot {x} _ {n - 1} + a _ {n - 2} y - b _ {n - 2} u = \ddot {y} + a _ {n - 1} \dot {y} - b _ {n - 1} \dot {u} + a _ {n - 2} y - b _ {n - 2} u$$

•
•
•

$$x _ {2} = \dot {x} _ {3} + a _ {2} y - b _ {2} u = y ^ {(n - 2)} + a _ {n - 1} y ^ {(n - 3)} - b _ {n - 1} u ^ {(n - 3)} + a _ {n - 2} y ^ {(n - 4)}- b _ {n - 2} u ^ {(n - 4)} + \dots + a _ {2} y - b _ {2} ux _ {1} = \dot {x} _ {2} + a _ {1} y - b _ {1} u = y ^ {(n - 1)} + a _ {n - 1} y ^ {(n - 2)} - b _ {n - 1} u ^ {(n - 2)} + a _ {n - 2} y ^ {(n - 3)}- b _ {n - 2} u ^ {(n - 3)} + \dots + a _ {1} y - b _ {1} u$$

故有 $n - 1$ 个状态方程

$$\dot {x} _ {n} = x _ {n - 1} - a _ {n - 1} x _ {n} + b _ {n - 1} u\dot {x} _ {n - 1} = x _ {n - 2} - a _ {n - 2} x _ {n} + b _ {n - 2} u$$

•
•
•

$$\dot {x} _ {2} = x _ {1} - a _ {1} x _ {n} + b _ {1} u$$

对 $x_{1}$ 求导数且考虑式(9-8)，经整理有

$$\dot {x} _ {1} = - a _ {0} x _ {n} + b _ {0} u$$

则式(9-8) $b_{n}=0$ 时的动态方程为

$$\dot {\boldsymbol {x}} = \boldsymbol {A} \boldsymbol {x} + \boldsymbol {b} \boldsymbol {u}, \quad \boldsymbol {y} = \boldsymbol {c x} \tag {9-13}$$

式中

$$
\mathbf {A} = \left[ \begin{array}{c c c c c} 0 & 0 & \dots & 0 & - a _ {0} \\ 1 & 0 & \dots & 0 & - a _ {1} \\ 0 & 1 & \dots & 0 & - a _ {2} \\ \vdots & \vdots & & \vdots & \vdots \\ 0 & 0 & \dots & 1 & - a _ {n - 1} \end{array} \right], \quad \mathbf {b} = \left[ \begin{array}{c} b _ {0} \\ b _ {1} \\ b _ {2} \\ \vdots \\ b _ {n - 1} \end{array} \right], \quad \mathbf {c} = [ 0 0 \dots 1 ]
$$

例 9-2 设二阶系统微分方程为

$$\ddot {y} + 2 \zeta \omega \dot {y} + \omega^ {2} y = T \dot {u} + u$$

试求系统状态空间表达式。

解 设状态变量 $x_{1} = y - h_{0}u, x_{2} = \dot{x}_{1} - h_{1}u = \dot{y} - h_{0}\dot{u} - h_{1}u$ ，故有

$$y = x _ {1} + h _ {0} u, \quad \dot {x} _ {1} = x _ {2} + h _ {1} u$$

对 $x_{2}$ 求导数且考虑 $x_{1}, x_{2}$ 及系统微分方程，有

$$
\begin{array}{l} \dot {x} _ {2} = \ddot {y} - h _ {0} \ddot {u} - h _ {1} \dot {u} = (- \omega^ {2} y - 2 \zeta \omega \dot {y} + T \dot {u} + u) - h _ {0} \ddot {u} - h _ {1} \dot {u} \\ = - \omega^ {2} x _ {1} - 2 \zeta \omega x _ {2} - h _ {0} \ddot {u} + (T - 2 \zeta \omega h _ {0} - h _ {1}) \dot {u} + (1 - \omega^ {2} h _ {0} - 2 \zeta \omega h _ {1}) u \\ \end{array}
$$

令 $\ddot{u},\dot{u}$ 项的系数为零可得

$$h _ {0} = 0, \quad h _ {1} = T$$

故 $\dot{x}_2 = -\omega^2 x_1 - 2\zeta \omega x_2 + (1 - 2\zeta \omega T)u$

系统的状态空间表达式为
