$$
\begin{array}{l} b _ {1} \| y \| ^ {2} \leqslant W (t, x, y) \leqslant b _ {2} \| y \| ^ {2} \\ \frac {\partial W}{\partial y} g (t, x, y + h (t, x), 0) \leqslant - b _ {3} \| y \| ^ {2} \\ \left\| \frac {\partial W}{\partial y} \right\| \leqslant b _ {4} \| y \| \\ \left\| \frac {\partial W}{\partial t} \right\| \leqslant b _ {5} \| y \| ^ {2}; \quad \left\| \frac {\partial W}{\partial x} \right\| \leqslant b _ {6} \| y \| ^ {2} \\ \end{array}
$$

其中 $b_{i}$ 是正常数, $i=1,\cdots,6$ , 且 $y\in B_{\rho_{0}},\rho_{0}\leqslant\rho$ 。应用变量代换

$$y = z - h (t, x)$$

将方程(11.47)和方程(11.48)变换为

$$\dot {x} = f (t, x, y + h (t, x), \varepsilon) \tag {11.49}\varepsilon \dot {y} = g (t, x, y + h (t, x), \varepsilon) - \varepsilon \frac {\partial h}{\partial t} \tag {11.50}- \varepsilon \frac {\partial h}{\partial x} f (t, x, y + h (t, x), \varepsilon)$$

下面将用

$$\nu (t, x, y) = V (t, x) + W (t, x, y)$$

作为系统(11.49)\~(11.50)的一个备选李雅普诺夫函数。在上述过程中,注意在原点邻域内的估计:由于对于所有 $\varepsilon\in[0,\varepsilon_{0}]$ , f 和 g 在原点为零,它们对于 $\varepsilon$ 是利普希茨的,对于状态 $(x,y)$ 是线性的。具体地讲,

$$\left\| f (t, x, y + h (t, x), \varepsilon) - f (t, x, y + h (t, x), 0) \right\| \leqslant \varepsilon L _ {1} (\| x \| + \| y \|)\left\| g (t, x, y + h (t, x), \varepsilon) - g (t, x, y + h (t, x), 0) \right\| \leqslant \varepsilon L _ {2} (\| x \| + \| y \|)\left\| f (t, x, y + h (t, x), 0) - f (t, x, h (t, x), 0) \right\| \leqslant L _ {3} \| y \|$$

且

$$\left\| f (t, x, h (t, x), 0) \right\| \leqslant L _ {4} \| x \|\left\| \frac {\partial h}{\partial t} \right\| \leqslant k _ {1} \| x \|; \quad \left\| \frac {\partial h}{\partial x} \right\| \leqslant k _ {2}$$

其中用到对于所有 $t, f(t, x, h(t, x), 0)$ 和 $h(t, x)$ 在 $x = 0$ 时为零。利用这些估计以及函数 $V$ 和 $W$ 的性质，可以验证 $\nu$ 沿方程(11.49)和方程(11.50)的轨线的导数满足不等式

$$\dot {\nu} \leqslant - a _ {1} \| x \| ^ {2} + \varepsilon a _ {2} \| x \| ^ {2} - \frac {a _ {3}}{\varepsilon} \| y \| ^ {2} + a _ {4} \| y \| ^ {2}+ a _ {5} \| x \| \| y \| + a _ {6} \| x \| \| y \| ^ {2} + a _ {7} \| y \| ^ {3}$$

其中， $a_1$ 和 $a_3$ 为正， $a_2$ 及 $a_4$ 到 $a_7$ 非负。对于所有 $\| y\| \leqslant \rho_0$ ，该不等式简化为

$$
\dot {\nu} \leqslant - a _ {1} \| x \| ^ {2} + \varepsilon a _ {2} \| x \| ^ {2} - \frac {a _ {3}}{\varepsilon} \| y \| ^ {2} + a _ {8} \| y \| ^ {2} + 2 a _ {9} \| x \| \| y \|
= - \left[ \begin{array}{c} \| x \| \\ \| y \| \end{array} \right] ^ {T} \left[ \begin{array}{c c} a _ {1} - \varepsilon a _ {2} & - a _ {9} \\ - a _ {9} & (a _ {3} / \varepsilon) - a _ {8} \end{array} \right] \left[ \begin{array}{c} \| x \| \\ \| y \| \end{array} \right]
$$
