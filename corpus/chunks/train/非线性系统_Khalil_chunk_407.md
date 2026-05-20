# 14.1.1 引例

考虑二阶系统

$$
\begin{array}{l} \dot {x} _ {1} = x _ {2} \\ \dot {x} _ {2} = h (x) + g (x) u \\ \end{array}
$$

其中 h 和 g 为未知非线性函数,且对于任意 x,有 $g(x) \geqslant g_{0} > 0$ 。我们想要设计一个状态反馈控制律以稳定原点。假设可设计一个控制律,使系统的运动限制在流形(或曲面) $s = a_{1}x_{1} + x_{2} = 0$ 上,在此流形上系统的运动受 $\dot{x}_{1} = -a_{1}x_{1}$ 的控制。选择 $a_{1} > 0$ ,以保证当 t 趋于无穷时, $x(t)$ 趋于零,且其收敛速度可通过 $a_{1}$ 的选择控制,在流形 s = 0 上的运动与 h 和 g 无关。设计问题就是如何把轨线切换并保持在流形 s = 0 上。变量 s 满足方程

$$\dot {s} = a _ {1} \dot {x} _ {1} + \dot {x} _ {2} = a _ {1} x _ {2} + h (x) + g (x) u$$

假设对于某个已知函数 $\varrho(x), h$ 和 $g$ 满足不等式

$$\left| \frac {a _ {1} x _ {2} + h (x)}{g (x)} \right| \leqslant \varrho (x), \quad \forall x \in R ^ {2}$$

将 $V = (1 / 2)s^2$ 作为方程 $\dot{s} = a_{1}x_{2} + h(x) + g(x)u$ 的备选李雅普诺夫函数，有

$$\dot {V} = s \dot {s} = s [ a _ {1} x _ {2} + h (x) ] + g (x) s u \leqslant g (x) | s | \varrho (x) + g (x) s u$$

取① $u = -\beta (x)\operatorname {sgn}(s)$

其中 $\beta (x)\geqslant \varrho (x) + \beta_0,\beta_0 > 0$ ，且

$$
\operatorname{sgn} (s) = \left\{ \begin{array}{c c} 1, & s > 0 \\ 0, & s = 0 \\ - 1, & s <   0 \end{array} \right.
$$

则

$$\dot {V} \leqslant g (x) | s | \varrho (x) - g (x) [ \varrho (x) + \beta_ {0} ] s \operatorname{sgn} (s) = - g (x) \beta_ {0} | s | \leqslant - g _ {0} \beta_ {0} | s |$$

故 $W = \sqrt{2V} = |s|$ 满足微分不等式

$$D ^ {+} W \leqslant - g _ {0} \beta_ {0}$$

由比较引理可知

$$W (s (t)) \leqslant W (s (0)) - g _ {0} \beta_ {0} t$$

因此，轨线在有限的时间内可到达流形 $s = 0$ ，且由不等式 $\dot{V}\leqslant -g_0\beta_0|s|$ 可看出，轨线一旦到达流形就不再离开。总之，系统运动包括到达阶段和滑动阶段两个过程。在前一个阶段，轨线向流形 $s = 0$ 运动并在有限的时间内到达流形。在后一个阶段，系统的运动保持在流形 $s = 0$ 上，此时系统的动态可由降阶模型 $\dot{x}_1 = -a_1x_1$ 表示。图14.1所示为其相图。流形 $s = 0$ 称为滑动流形，控制律 $u = -\beta (x)\mathrm{sgn}(s)$ 称为滑模控制。滑模控制的显著特点

![](image/df08aa549aea3de8c5d15b2f06cc35a51f422c8e397856ab2bfce65b391a9cf4.jpg)

<details>
<summary>text_image</summary>

s=0
</details>

图 14.1 滑模控制下的典型相图

是其对 g 和 h 的鲁棒性, 我们只需要知道上界 $\varrho(x)$ , 而且在滑动阶段, 系统运动完全与 h 和 g 无关。

如果在某一感兴趣的区域, h 和 g 对于某个已知的非负常数 $k_{1}$ 满足不等式

$$\left| \frac {a _ {1} x _ {2} + h (x)}{g (x)} \right| \leqslant k _ {1}$$

则可简化滑模控制器。此时可取

$$u = - k \operatorname{sgn} (s), \quad k > k _ {1}$$

为简单继电器的形式。但该形式通常得到一个有限的吸引区，可用下面的方法进行估计：在集合 $\{|s|\leqslant c\}$ 内，条件 $s\dot{s}\leqslant0$ 使集合为正不变集。由方程

$$\dot {x} _ {1} = x _ {2} = - a _ {1} x _ {1} + s$$

及函数 $V_{1} = (1 / 2)x_{1}^{2}$ ，有

$$\dot {V} _ {1} = x _ {1} \dot {x} _ {1} = - a _ {1} x _ {1} ^ {2} + x _ {1} s \leqslant - a _ {1} x _ {1} ^ {2} + | x _ {1} | c \leqslant 0, \quad \forall | x _ {1} | \geqslant \frac {c}{a _ {1}}$$
