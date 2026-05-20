$$
\begin{array}{l} \dot {\mathcal {V}} = - \mathcal {Y} ^ {\mathrm{T}} \mathcal {Y} + 2 \mathcal {Y} ^ {\mathrm{T}} P _ {m s} \left[ g (\mathcal {Y} + \mathcal {X} _ {\mathrm{ss}} (\rho), \rho) - A _ {m s} (\rho) \mathcal {Y} + N (\rho) \mathcal {Z} - \frac {\partial \mathcal {X} _ {\mathrm{ss}}}{\partial \rho} \dot {\rho} \right] \\ + \mathcal {Y} ^ {\mathrm{T}} \left[ \frac {d}{d t} P _ {m s} (\rho) \right] \mathcal {Y} \\ - \frac {1}{\varepsilon} \mathcal {Z} ^ {\mathrm{T}} \mathcal {Z} - \mathcal {Z} ^ {\mathrm{T}} \left\{\frac {\partial \phi}{\partial \mathcal {X}} [ g (\mathcal {Y} + \mathcal {X} _ {\mathrm{ss}} (\rho), \rho) + N (\rho) \mathcal {Z} ] + \frac {\partial \phi}{\partial \rho} \dot {\rho} \right\} \\ \leqslant - \| \mathcal {Y} \| _ {2} ^ {2} - \frac {1}{\varepsilon} \| \mathcal {Z} \| _ {2} ^ {2} + c _ {1} \| \mathcal {Y} \| _ {2} ^ {3} + c _ {2} \| \mathcal {Y} \| _ {2} \| \mathcal {Z} \| _ {2} + c _ {3} \| \mathcal {Y} \| _ {2} \| \dot {\rho} \| _ {2} \\ + c _ {4} \| \mathcal {Y} \| _ {2} ^ {2} \| \dot {\rho} \| _ {2} + c _ {5} \| \mathcal {Z} \| _ {2} ^ {2} + c _ {6} \| \mathcal {Z} \| _ {2} \| \dot {\rho} \| _ {2} \\ \end{array}
$$

其中 $c_{i}$ 是正常数。把分析限制在邻域 $\| \mathcal{Y}\| _2\leqslant c_7\leqslant 1 / (4c_1)$ 内，可得不等式

$$
\begin{array}{l} \dot {\mathcal {V}} \leqslant - \frac {1}{2} \| \mathcal {Y} \| _ {2} ^ {2} - \frac {1}{2 \varepsilon} \| \mathcal {Z} \| _ {2} ^ {2} + \left(c _ {3} \| \mathcal {Y} \| _ {2} + c _ {4} c _ {7} \| \mathcal {Y} \| _ {2} + c _ {6} \| \mathcal {Z} \| _ {2}\right) \| \dot {\rho} \| _ {2} \\ - \left[ \begin{array}{c} \| \mathcal {Y} \| _ {2} \\ \| \mathcal {Z} \| _ {2} \end{array} \right] ^ {\mathrm{T}} \left[ \begin{array}{c c} 1 / 4 & - c _ {2} / 2 \\ - c _ {2} / 2 & 1 / (2 \varepsilon) - c _ {5} \end{array} \right] \left[ \begin{array}{c} \| \mathcal {Y} \| _ {2} \\ \| \mathcal {Z} \| _ {2} \end{array} \right] \\ \end{array}
$$

选择 $\varepsilon^{*}$ 足够小，使得对于所有 $0 < \varepsilon < \varepsilon^{*}, 2 \times 2$ 矩阵都是正定的。这样，对于某个正常数 $\alpha$ 和 $\beta$ ，有

$$\dot {\mathcal {V}} \leqslant - 2 \alpha \mathcal {V} + 2 \beta \sqrt {\mathcal {V}} \| \dot {\rho} \| _ {2}$$

因此, $W=\sqrt{V}$ 满足不等式

$$D ^ {+} W \leqslant - \alpha W + \beta \| \dot {\rho} \| _ {2}$$

应用比较引理即可得定理 12.2。

□
