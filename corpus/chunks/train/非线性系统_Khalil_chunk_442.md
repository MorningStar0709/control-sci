并利用式(14.62)，可得 $\dot{V}_c \leqslant -b \| \eta \|_2^2 + (\xi - \phi) \left[ \delta_\xi - \frac{\partial \phi}{\partial \eta} \delta_\eta \right] - k (\xi - \phi)^2$

通过式(14.60)、式(14.61)和式(14.63)，可证明，对于某个 $a_{6}\geqslant0$ ，有

$$
\begin{array}{l} \dot {V} _ {c} \leqslant - b \| \eta \| _ {2} ^ {2} + 2 a _ {6} \| \eta \| _ {2} | \xi - \phi | - (k - a _ {3}) (\xi - \phi) ^ {2} \\ = - \left[ \begin{array}{c} \| \eta \| _ {2} \\ | \xi - \phi | \end{array} \right] ^ {\mathrm{T}} \left[ \begin{array}{c c} b & - a _ {6} \\ - a _ {6} & (k - a _ {3}) \end{array} \right] \left[ \begin{array}{c} \| \eta \| _ {2} \\ | \xi - \phi | \end{array} \right] \\ \end{array}
$$

选择 $k > a_{3} + \frac{a_{6}^{2}}{b}$

对于某个 $\sigma > 0$ , 得

$$\dot {V} _ {c} \leqslant - \sigma [ \| \eta \| _ {2} ^ {2} + | \xi - \phi | ^ {2} ]$$

至此，已完成了下一引理的证明。

引理 14.3 考虑系统(14.58)～(14.59)，其中不确定项满足不等式(14.60)和不等式(14.61)。设 $\phi(\eta)$ 为式(14.58)的稳定状态反馈控制律，满足式(14.63)， $V(\eta)$ 是满足式(14.62)的李雅普诺夫函数，则对于足够大的 k，状态反馈控制律(14.65)可稳定系统(14.58)～(14.59)的原点。此外，如果所有假设全局成立，且 $V(\eta)$ 为径向无界的，则原点是全局渐近稳定的。

$$
\left. \begin{array}{r c l} \dot {x} _ {i} & = & x _ {i + 1} + \delta_ {i} (x), \quad 1 \leqslant i \leqslant n - 1 \\ \dot {x} _ {n} & = & \gamma (x) [ u - \alpha (x) ] + \delta_ {n} (x) \end{array} \right\} \tag {14.66}
$$

定义在包含原点 x=0 的定义域 $D \subset R^{n}$ 上, $x = [x_{1}, \cdots, x_{n}]^{T}$ 。假设对于所有 $x \in D$ , 有 $\gamma(x) \neq 0$ , 且所有函数都是光滑的。设 $\alpha$ 和 $\gamma$ 已知, $\delta_{i}$ 是不确定项, $1 \leqslant i \leqslant n$ , 标称系统是可反馈线性化的。假设不确定项对于所有 $x \in D$ 满足不等式

$$| \delta_ {i} (x) | \leqslant a _ {i} \sum_ {k = 1} ^ {i} | x _ {k} |, \quad 1 \leqslant i \leqslant n \tag {14.67}$$

其中，非负常数 $a_1$ 到 $a_n$ 已知。当 $1 \leqslant i \leqslant n - 1$ 时，不等式(14.67)限定了不确定项的类型，因为它限定 $\delta_i(x)$ 的上界只取决于 $x_1$ 到 $x_i$ ，即上界以严格反馈的形式出现。但这一限定不如 $1 \leqslant i \leqslant n - 1$ 时的匹配条件 $\delta_i = 0$ 严格。为运用反步迭代设计步骤，从标量系统

$$\dot {x} _ {1} = x _ {2} + \delta_ {1} (x)$$

入手,其中 $x_{2}$ 为控制输入, $\delta_{1}(x)$ 满足不等式 $|\delta_{1}(x)| \leqslant a_{1}|x_{1}|$ 。在该标量系统中不确定项满足匹配条件, 若选择 $k_{1} > 0$ 足够大, 原点 $x_{1} = 0$ 可通过高增益反馈控制 $x_{2} = -k_{1}x_{1}$ 达到鲁棒稳定。特别地, 设 $V_{1}(x_{1}) = x_{1}^{2}/2$ 为备选李雅普诺夫函数, 则有

$$\dot {V} _ {1} = x _ {1} [ - k _ {1} x _ {1} + \delta_ {1} (x) ] \leqslant - (k _ {1} - a _ {1}) x _ {1} ^ {2}$$

且对于所有 $k_{1} > a_{1}$ ，原点是稳定的。基于此，反步法和引理 14.3 可迭代运用于推出稳定状态反馈控制律，下一个例题将说明这一过程。

例 14.13 设计一个状态反馈控制律,稳定二阶系统

$$\dot {x} _ {1} = x _ {2} + \theta_ {1} x _ {1} \sin x _ {2}\dot {x} _ {2} = \theta_ {2} x _ {2} ^ {2} + x _ {1} + u$$
