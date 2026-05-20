$$3 x _ {1} + \frac {1}{4} x _ {2} = 0$$

因此，由直线 $x_{1} = -x_{2} / 12$ 与李雅普诺夫曲面的交点可得 $x_{2}$ 的极值。通过简单的计算可知，在李雅普诺夫曲面上 $x_{2}^{2}$ 的最大值为 $96c / 29$ 。这样，在 $\Omega_c$ 内的所有点满足边界

$$| x _ {2} | \leqslant k _ {2}, \text {其中} k _ {2} ^ {2} = \frac {9 6 c}{2 9}$$

因此如果 $\beta < \frac{29}{3.026 \times 96c} \approx \frac{0.1}{c}$

则 $\dot{V}(x)$ 在 $\Omega_c$ 内是负定的，并且可得以 $\Omega_c$ 作为吸引区的估计值，原点 $x = 0$ 是指数稳定的。不等式 $\beta < 0.1 / c$ 表明在吸引区估计值和 $\beta$ 的上界估计值之间可进行调整， $\beta$ 的上界越小，吸引区的估计值就越大。这个折中不是人为的，在本例中实际存在。应用变量代换

$$
\begin{array}{l} z _ {1} = \sqrt {\frac {3 \beta}{2}} x _ {2} \\ \begin{array}{r c l} z _ {2} & = & \sqrt {\frac {3 \beta}{8}} (4 x _ {1} + 2 x _ {2} - \beta x _ {2} ^ {3}) = - \sqrt {\frac {3 \beta}{8}} \dot {x} _ {2} \\ \tau & = & 2 t \end{array} \\ \end{array}
$$

状态方程变换为 $\frac{dz_1}{d\tau} = -z_2$

$${\frac {d z _ {2}}{d \tau}} = {z _ {1} + (z _ {1} ^ {2} - 1) z _ {2}}$$

例8.5已证明该方程有一个有界吸引区，被一个不稳定极限环包围。当变换到 $x$ 坐标系时，吸引区会随 $\beta$ 的减小而扩大，随 $\beta$ 的增加而缩小。最后，用这个例子说明式(9.7)的边界的保守性。利用此边界可得不等式 $\beta < 1 / 3.026k_2^2$ ，这就是说扰动项 $g(t,x)$ 可以是任何满足 $\| g(t,x)\| _2\leqslant \beta k_2^2\| x\| _2$ 的二阶向量。这类扰动比特殊情况下的扰动更具有一般性。如果 $g$ 的第一项总为零，就是结构扰动。但我们的分析也涉及到非结构扰动，即向量 $g$ 可以在各个方向变化。一般来讲，忽略扰动的结构会导致有裕量的边界。假设考虑到扰动结构重新进行分析，不用式(9.7)的一般边界，而是计算 $V(t,x)$ 沿扰动系统轨线的导数，得到

$$
\begin{array}{l} \dot {V} (x) = - \| x \| _ {2} ^ {2} + 2 x ^ {\mathrm{T}} P g (x) \\ = - \| x \| _ {2} ^ {2} + 2 \beta x _ {2} ^ {2} \left(\frac {1}{8} x _ {1} x _ {2} + \frac {5}{1 6} x _ {2} ^ {2}\right) \\ \leqslant - \| x \| _ {2} ^ {2} + 2 \beta x _ {2} ^ {2} \left(\frac {1}{1 6} \| x \| _ {2} ^ {2} + \frac {5}{1 6} \| x \| _ {2} ^ {2}\right) \\ \leqslant - \| x \| _ {2} ^ {2} + \frac {3}{4} \beta k _ {2} ^ {2} \| x \| _ {2} ^ {2} \\ \end{array}
$$

因此，当 $\beta < 4 / 3k_2^2$ 时， $\dot{V}(x)$ 是负定的。再次利用对于所有 $x \in \Omega_c, |x_2|^2 \leqslant k_2^2 = 96c / 29$ ，可以得到边界 $\beta < 0.4 / c$ ，它是采用式(9.7)所得到边界的4倍。

当标称系统(9.2)的原点一致渐近稳定,而不是指数稳定时,扰动系统的稳定性分析就更为复杂。假设对于所有 $(t,x)\in[0,\infty)\times D$ ,标称系统有一个正定递减的李雅普诺夫函数 $V(x)$ ,满足

$$\frac {\partial V}{\partial t} + \frac {\partial V}{\partial x} f (t, x) \leqslant - W _ {3} (x)$$

其中， $W_{3}(x)$ 是正定且连续的。 $V$ 沿系统(9.1)轨线的导数为

$$\dot {V} (t, x) = \frac {\partial V}{\partial t} + \frac {\partial V}{\partial x} f (t, x) + \frac {\partial V}{\partial x} g (t, x)\leqslant - W _ {3} (x) + \left\| \frac {\partial V}{\partial x} g (t, x) \right\|$$

现在的任务是要证明,对于所有的 $(t,x)\in[0,\infty)\times D$ ,有

$$\left\| \frac {\partial V}{\partial x} g (t, x) \right\| < W _ {3} (x)$$
