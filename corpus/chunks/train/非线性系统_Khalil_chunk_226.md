并考虑两个非线性特性:饱和非线性和死区非线性。后者是例7.7中分段线性函数的一个特例,即 $\delta=0,s_{1}=1$ 和 $s_{2}=0.5$ 时的情况。传递函数 $G(j\omega)$ 可写为

$$G (j \omega) = \frac {- 0 . 8 \omega^ {2} - j \omega (8 - \omega^ {2})}{0 . 6 4 \omega^ {2} + (8 - \omega^ {2}) ^ {2}}$$

方程(7.32)有唯一正根 $\omega = 2\sqrt{2}$ 。求出 $\omega = 2\sqrt{2}$ 时 $\operatorname{Re}[G(j\omega)]$ 的值，代入方程(7.31)，得 $\Psi(a) = 0.8$ 。对于饱和非线性特性，其描述函数已在例7.7中给出， $\Psi(a) = 0.8$ 有唯一解 $a = 1.455$ 。因此由 $G(s)$ 和饱和非线性特性构成的非线性系统在频率接近 $2\sqrt{2}$ 时振荡，且（非线性输入端）振幅为1.455。对于死区非线性特性，其描述函数对所有 $a$ 都小于0.8，因此当 $\Psi(a) = 0.8$ 时无解，并由此可预见由 $G(s)$ 和死区非线性特性构成的非线性系统没有持续振荡。在这个特殊的例子中，还可以通过系统对于一类扇形区域的非线性绝对稳定的结论确认无振荡的推测，这类非线性特性包括已给出的死区非线性。容易得到

$$\mathrm{Re} [ G (j \omega) ] \geqslant - 1. 2 5, \forall \omega \in R$$

因此根据圆判据(定理7.2)可知,系统在扇形区域 $[0,\beta]$ 内是绝对稳定的,其中 $\beta<0.8$ 。所给死区非线性属于该扇形区域。因此,状态空间的原点是全局渐进稳定的,且系统无持续振荡。

例7.11 考虑Raleigh方程 $\ddot{z} + z = \varepsilon (\dot{z} - \frac{1}{3}\dot{z}^3)$

其中 $\varepsilon$ 是正常数。为研究周期解的存在性，把方程表示为图 7.1 所示的反馈形式。设 $u = -\dot{z}^{3}/3$ ，并将方程改写为

$$
\begin{array}{l} \ddot {z} - \varepsilon \dot {z} + z = \varepsilon u \\ u = - \frac {1}{3} \dot {z} ^ {3} \\ \end{array}
$$

第一个方程定义了一个线性系统。取 $y = \dot{z}$ 为其输出，则传递函数为

$$G (s) = \frac {\varepsilon s}{s ^ {2} - \varepsilon s + 1}$$

第二个方程定义了非线性特性 $\psi(y) = y^3 / 3$ 。这两个方程一起表示出图7.1以反馈形式连接的系统。 $\psi(y) = y^3 / 3$ 的描述函数由下式给出：

$$\Psi (a) = \frac {2}{3 \pi a} \int_ {0} ^ {\pi} (a \sin \theta) ^ {3} \sin \theta d \theta = \frac {1}{4} a ^ {2}$$

函数 $G(j\omega)$ 可写为 $G(j\omega) = \frac{j\varepsilon\omega[(1 - \omega^2) + j\varepsilon\omega]}{(1 - \omega^2)^2 + \varepsilon^2\omega^2}$

方程 $\operatorname{Im}[G(j\omega)] = 0$ 给出了 $\omega(1 - \omega^2) = 0$ ，因此有唯一正解 $\omega = 1$ 。则

$$1 + \Psi (a) \mathrm{Re} [ G (j) ] = 0 \Rightarrow a = 2$$

因此,可以预见,Raleigh方程有一个周期解,其频率接近1 rad/s,且 $\dot{z}$ 的振荡幅度接近2。

对于高阶传递函数,用解析法求解调和平衡方程(7.29)会很复杂,当然总可以采用数值计算法求解方程(7.29)。然而描述函数法的优势不在于应用解析法或数值计算法求解方程(7.29),而正是方程(7.29)的图形解使其颇受欢迎。方程(7.29)可改写为

$$G (j \omega) = - \frac {1}{\Psi (a)} \tag {7.33}$$

或 $\frac{1}{G(j\omega)} = -\Psi (a)$ (7.34)
