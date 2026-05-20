$$\dot {x} = f _ {0} (x) + g _ {0} (x) z _ {1}\dot {z} _ {1} = f _ {1} (x, z _ {1}) + g _ {1} (x, z _ {1}) z _ {2}\dot {z} _ {2} = f _ {2} \left(x, z _ {1}, z _ {2}\right) + g _ {2} \left(x, z _ {1}, z _ {2}\right) z _ {3}$$

•
•
•

$$\dot {z} _ {k - 1} = f _ {k - 1} \left(x, z _ {1}, \dots , z _ {k - 1}\right) + g _ {k - 1} \left(x, z _ {1}, \dots , z _ {k - 1}\right) z _ {k}\dot {z} _ {k} = f _ {k} \left(x, z _ {1}, \dots , z _ {k}\right) + g _ {k} \left(x, z _ {1}, \dots , z _ {k}\right) u$$

的严格反馈系统,其中 $x \in R^{n}, z_{1}$ 到 $z_{k}$ 是标量, $f_{0}$ 到 $f_{k}$ 在原点为零。之所以称该系统为“严格反馈系统”是因为 $\dot{z}_{i}$ 方程 $(i = 1, \cdots, k)$ 中的非线性函数 $f_{i}$ 和 $g_{i}$ 仅与 $x, z_{1}, \cdots, z_{i}$ 有关, 即“回馈”的状态变量。假设在所讨论的区域内,有

$$g _ {i} \left(x, z _ {1}, \dots , z _ {i}\right) \neq 0, \quad 1 \leqslant i \leqslant k$$

从系统 $\dot{x} = f_{0}(x) + g_{0}(x)z_{1}$

开始迭代,其中将 $z_{1}$ 看成控制输入。假设能够确定一个稳定状态反馈控制律 $z_{1} = \phi_{0}(x)$ , $\phi_{0}(0) = 0$ 和一个李雅普诺夫函数 $V_{0}(x)$ , 使得在讨论的区域内对某一正定函数 $W(x)$ , 有

$$\frac {\partial V _ {0}}{\partial x} [ f _ {0} (x) + g _ {0} (x) \phi_ {0} (x) ] \leqslant - W (x)$$

在许多反步法应用中, 变量 x 是标量, 从而使稳定性问题得以简化。下面给出当 $\phi_{0}(x)$ 和 $V_{0}(x)$ 已知时, 系统地运用反步法的步骤。首先把系统

$$\dot {x} = f _ {0} (x) + g _ {0} (x) z _ {1}\dot {z} _ {1} = f _ {1} \left(x, z _ {1}\right) + g _ {1} \left(x, z _ {1}\right) z _ {2}$$

作为系统(14.53)\~(14.54)的特例考虑,其中

$$\eta = x, \quad \xi = z _ {1}, \quad u = z _ {2}, \quad f = f _ {0}, \quad g = g _ {0}, \quad f _ {a} = f _ {1}, \quad g _ {a} = g _ {1}$$

利用式(14.56)及式(14.57)可得稳定状态反馈控制律及李雅普诺夫函数分别为

$$\phi_ {1} (x, z _ {1}) = \frac {1}{g _ {1}} \left[ \frac {\partial \phi_ {0}}{\partial x} \left(f _ {0} + g _ {0} z _ {1}\right) - \frac {\partial V _ {0}}{\partial x} g _ {0} - k _ {1} \left(z _ {1} - \phi_ {0}\right) - f _ {1} \right], \quad k _ {1} > 0V _ {1} (x, z _ {1}) = V _ {0} (x) + \frac {1}{2} [ z _ {1} - \phi_ {0} (x) ] ^ {2}$$

然后把系统 $\dot{x} = f_{0}(x) + g_{0}(x)z_{1}$

$$\dot {z} _ {1} = f _ {1} \left(x, z _ {1}\right) + g _ {1} \left(x, z _ {1}\right) z _ {2}\dot {z} _ {2} = f _ {2} \left(x, z _ {1}, z _ {2}\right) + g _ {2} \left(x, z _ {1}, z _ {2}\right) z _ {3}$$

作为系统(14.53)\~(14.54)的特例考虑,其中

$$
\eta = \left[ \begin{array}{c} x \\ z _ {1} \end{array} \right], \xi = z _ {2}, u = z _ {3}, f = \left[ \begin{array}{c} f _ {0} + g _ {0} z _ {1} \\ f _ {1} \end{array} \right], g = \left[ \begin{array}{c} 0 \\ g _ {1} \end{array} \right], f _ {a} = f _ {2}, g _ {a} = g _ {2}
$$

利用式(14.56)和式(14.57)可得稳定状态反馈控制律
