得出 $\dot{V} \leqslant -y^{\mathrm{T}}Ly - u^{\mathrm{T}}Mu + u^{\mathrm{T}}Ny$

其中 $L=\left[\begin{array}{cc}(\varepsilon_{2}+\delta_{1})I & 0 \\ 0 & (\varepsilon_{1}+\delta_{2})I\end{array}\right], M=\left[\begin{array}{cc}\varepsilon_{1}I & 0 \\ 0 & \varepsilon_{2}I\end{array}\right], N=\left[\begin{array}{cc}I & 2\varepsilon_{1}I \\ -2\varepsilon_{2}I & I\end{array}\right]$

且 $V(x) = V_{1}(x_{1}) + V_{2}(x_{2})$ 。设 $a = \min \{\varepsilon_2 + \delta_1, \varepsilon_1 + \delta_2\} > 0, b = \| N \|_2 \geqslant 0$ 和 $c = \| M \|_2 \geqslant 0$ ，则

$$
\begin{array}{l} \dot {V} \leqslant - a \| y \| _ {2} ^ {2} + b \| u \| _ {2} \| y \| _ {2} + c \| u \| _ {2} ^ {2} \\ = - \frac {1}{2 a} (b \| u \| _ {2} - a \| y \| _ {2}) ^ {2} + \frac {b ^ {2}}{2 a} \| u \| _ {2} ^ {2} - \frac {a}{2} \| y \| _ {2} ^ {2} + c \| u \| _ {2} ^ {2} \\ \leqslant \frac {k ^ {2}}{2 a} \| u \| _ {2} ^ {2} - \frac {a}{2} \| y \| _ {2} ^ {2} \\ \end{array}
$$

其中 $k^2 = b^2 + 2ac$ 。在 $[0, \tau]$ 范围积分，利用 $V(x) \geqslant 0$ ，并取平方根，得

$$\| y _ {\tau} \| _ {\mathcal {L} _ {2}} \leqslant \frac {k}{a} \| u _ {\tau} \| _ {\mathcal {L} _ {2}} + \sqrt {2 V (x (0)) / a}$$

定理得证。

当 $\varepsilon_{1} = \varepsilon_{2} = 0, \delta_{1} > 0, \delta_{2} > 0$ ，式(6.34)成立时，定理6.2简化为引理6.8。但条件(6.35)在其他几种情况下也是满足的，例如，当 $H_{1}$ 和 $H_{2}$ 都是严格输入无源的，对于某个 $\varepsilon_{i} > 0$ ，满足 $e_{i}^{\mathrm{T}}y_{i} \geqslant \dot{V}_{i} + \varepsilon_{i}u_{i}^{\mathrm{T}}u_{i}$ 时，就是这种情况。当有一个分支（譬如 $H_{1}$ ）是无源的，而另一个分支在 $\varepsilon_{2}$ 和 $\delta_{2}$ 为正时满足式(6.34)时，也会满足式(6.35)。我们更感兴趣的是，即使当某些常数 $\varepsilon_{i}$ 和 $\delta_{i}$ 是负数时，式(6.35)也成立的情况。例如，一个负的 $\varepsilon_{1}$ 可由正的 $\delta_{2}$ 补偿，这种情况即 $H_{1}$ 的欠量无源性（在输入端）由 $H_{2}$ 的过量无源性（在输出端）补偿。同样，负的 $\delta_{2}$ 可以由正的 $\varepsilon_{1}$ 补偿，这种情况是 $H_{2}$ 的欠量无源性（在输出端）由 $H_{1}$ 的过量无源性（在输入端）补偿。

例6.7 考虑 $H_{1}$ ： $\left\{ \begin{array}{ll} \dot{x} & = f(x) + G(x)e_1\\ y_1 & = h(x) \end{array} \right.$ 和 $H_{2}$ ： $y_{2} = ke_{2}$

的反馈连接,其中 $k>0, e_{i}, y_{i} \in R^{p}$ 。假设存在正定有界函数 $V_{1}(x)$ , 使得

$$\frac {\partial V _ {1}}{\partial x} f (x) \leqslant 0, \quad \frac {\partial V _ {1}}{\partial x} G (x) = h ^ {\mathrm{T}} (x), \quad \forall x \in R ^ {n}$$

两个分支都是无源的。而且 $H_{2}$ 满足

$$e _ {2} ^ {\mathrm{T}} y _ {2} = k e _ {2} ^ {\mathrm{T}} e _ {2} = \gamma k e _ {2} ^ {\mathrm{T}} e _ {2} + \frac {(1 - \gamma)}{k} y _ {2} ^ {\mathrm{T}} y _ {2}, \quad 0 < \gamma < 1$$
