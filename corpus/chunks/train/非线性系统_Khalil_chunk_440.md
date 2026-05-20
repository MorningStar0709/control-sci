$$\phi_ {2} (x, z _ {1}, z _ {2}) = \frac {1}{g _ {2}} \left[ \frac {\partial \phi_ {1}}{\partial x} (f _ {0} + g _ {0} z _ {1}) + \frac {\partial \phi_ {1}}{\partial z _ {1}} (f _ {1} + g _ {1} z _ {2}) - \frac {\partial V _ {1}}{\partial z _ {1}} g _ {1} - k _ {2} (z _ {2} - \phi_ {1}) - f _ {2} \right]$$

对于 $k_{2} > 0$ ，及李雅普诺夫函数

$$V _ {2} (x, z _ {1}, z _ {2}) = V _ {1} (x, z _ {1}) + \frac {1}{2} [ z _ {2} - \phi_ {1} (x, z _ {1}) ] ^ {2}$$

该步骤重复 k 次, 即可得到总的稳定状态反馈控制律 $u = \phi_{k}(x, z_{1}, \cdots, z_{k})$ 及李雅普诺夫函数 $V_{k}(x, z_{1}, \cdots, z_{k})$ 。

例 14.10 考虑特殊归一化形式的单输入-单输出系统

$$
\begin{array}{l} \dot {x} = f _ {0} (x) + g _ {0} (x) z _ {1} \\ \dot {z} _ {1} = z _ {2} \\ \dot {z} _ {r - 1} = z _ {r} \\ \dot {z} _ {r} = \gamma (x, z) [ u - \alpha (x, z) ] \\ y = z _ {1} \\ \end{array}
$$

•
•
•

其中，对于所有 $(x,z), x \in R^{n - r}, z_1$ 到 $z_r$ 是标量， $\gamma(x,z) \neq 0$ 。由于 $\dot{x}$ 方程取 $f_0(x) + g_0(x)z_1$ 的形式，而不是一般形式 $f_0(x,z)$ ，因此上面的方程是标准形(13.16)～(13.18)的特例，且为严格反馈形式。如果对于某个正定函数 $W(x)$ ，能找到一个光滑函数 $\phi_0(x)$ 和一个光滑且径向无界的李雅普诺夫函数 $V_0(x)$ ，满足

$$\frac {\partial V _ {0}}{\partial x} [ f _ {0} (x) + g _ {0} (x) \phi_ {0} (x) ] \leqslant - W (x), \quad \forall x \in R ^ {n}$$

则通过迭代反步法使原点达到全局稳定。如果是最小相位系统， $\dot{x}=f_{0}(x)$ 的原点是全局渐近稳定的，且已知对于某个正定函数 $W(x)$ ，李雅普诺夫函数 $V_{0}(x)$ 满足

$$\frac {\partial V _ {0}}{\partial x} f _ {0} (x) \leqslant - W (x), \quad \forall x \in R ^ {n}$$

则可以简单地取 $\phi_{0}(x)=0$ ，否则必须寻找 $\phi_{0}(x)$ 及 $V_{0}(x)$ 。这表明只要零动态稳定问题可解，反步法就能够稳定最小相位系统。

例14.11 在例13.16中已证明二阶系统

$$
\begin{array}{l} \dot {\eta} = - \eta + \eta^ {2} \xi \\ \dot {\xi} = u \\ \end{array}
$$

对于足够大的 $k(k > 0)$ ，控制律 $u = -k\xi$ 可使系统达到半全局稳定。本例将证明反步法可使系统达到全局稳定。首先考虑系统

$$\dot {\eta} = - \eta + \eta^ {2} \xi$$

显然，取 $\xi = 0$ 及 $V_{0}(\eta) = \eta^{2} / 2$ 时，有

$$\frac {\partial V _ {0}}{\partial \eta} (- \eta) = - \eta^ {2}, \quad \forall \eta \in R$$

利用 $V = V_{0} + \xi^{2} / 2 = (\eta^{2} + \xi^{2}) / 2$ ，可得

$$\dot {V} = \eta (- \eta + \eta^ {2} \xi) + \xi u = - \eta^ {2} + \xi (\eta^ {3} + u)$$

这样 $u = -\eta^3 - k\xi, \quad k > 0$

使原点全局稳定。

例 14.12 作为前一个例子的变形,考虑系统 $^{①}$

$$
\begin{array}{l} \dot {\eta} = \eta^ {2} - \eta \xi \\ \dot {\xi} = u \\ \end{array}
$$

这次取 $\xi = 0$ ，此时 $\dot{\eta} = \eta^2 -\eta \xi$ 不会使系统稳定。但很容易看出，取 $\xi = \eta +\eta^2$ 和 $V_{0}(\eta) =$ $\eta^2 /2$ 时，得

$$\frac {\partial V _ {0}}{\partial \eta} [ \eta^ {2} - \eta (\eta + \eta^ {2}) ] = - \eta^ {4}, \quad \forall \eta \in R$$

利用 $V = V_{0} + (\xi -\eta -\eta^{2})^{2} / 2$ ，可得
