# 4.1.1 全程快速微分器

全程快速微分器 $^{[2]}$ :

$$
\begin{array}{l} \dot {x} _ {1} = x _ {2} \\ \dot {x} _ {2} = R ^ {2} \left(- a _ {0} (x _ {1} - v (t)) - a _ {1} (x _ {1} - v (t)) ^ {\frac {m}{n}} - b _ {0} \frac {x _ {2}}{R} - b _ {1} \left(\frac {x _ {2}}{R}\right) ^ {\frac {m}{n}}\right) \tag {4.1} \\ y = x _ {2} (t) \\ \end{array}
$$

式中， $R > 0$ ； $a_0, a_1, b_0, b_1 \geqslant 0$ ；m、n均为大于0的奇数，且 $m < n$ 。系统输出 $y = x_2(t)$ 跟踪信号 $\nu(t)$ 的一阶导数 $\dot{\nu}(t)$ 。当取 $a_1 = b_1 = 0$ 时，线性微分器起主导作用。

$$
\begin{array}{l} \dot {x} _ {1} = x _ {2} \\ \dot {x} _ {2} = R ^ {2} \left(- a _ {0} (x _ {1} - v (t)) - b _ {0} \frac {x _ {2}}{R}\right) \tag {4.2} \\ y = x _ {2} (t) \\ \end{array}
$$

该种形式微分器可直接通过差分或高精度数值迭代方法来离散化，具体设计方法可参考文献[1]。

![](image/253f1bbcca94562e570ab3464f68053a2cc2a8b4f0cef9ba5fcf5b1946507fb4.jpg)
