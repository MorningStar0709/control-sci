$$
\begin{array}{l} \frac {\partial V}{\partial x} f (x) + \frac {\partial V}{\partial x} G (x) u = - \frac {1}{2} \gamma^ {2} \left\| u - \frac {1}{\gamma^ {2}} G ^ {\mathrm{T}} (x) \left(\frac {\partial V}{\partial x}\right) ^ {\mathrm{T}} \right\| _ {2} ^ {2} + \frac {\partial V}{\partial x} f (x) \\ + \frac {1}{2 \gamma^ {2}} \frac {\partial V}{\partial x} G (x) G ^ {T} (x) \left(\frac {\partial V}{\partial x}\right) ^ {T} + \frac {1}{2} \gamma^ {2} \| u \| _ {2} ^ {2} \\ \end{array}
\int_ {0} ^ {\infty} y ^ {T} (t) y (t) d t = \frac {1}{2 \pi} \int_ {- \infty} ^ {\infty} Y \in (j \omega) Y (j \omega) d \omega
$$

代入式(5.28)有

$$\frac {\partial V}{\partial x} f (x) + \frac {\partial V}{\partial x} G (x) u \leqslant \frac {1}{2} \gamma^ {2} \| u \| _ {2} ^ {2} - \frac {1}{2} \| y \| _ {2} ^ {2} - \frac {1}{2} \gamma^ {2} \left\| u - \frac {1}{\gamma^ {2}} G ^ {\mathrm{T}} (x) \left(\frac {\partial V}{\partial x}\right) ^ {\mathrm{T}} \right\| _ {2} ^ {2}$$

因此， $\frac{\partial V}{\partial x} f(x) + \frac{\partial V}{\partial x} G(x)u\leqslant \frac{1}{2}\gamma^{2}\| u\|_{2}^{2} - \frac{1}{2}\| y\|_{2}^{2}$ (5.29)

注意,式(5.29)左边是 V 沿系统(5.26)轨线的导数。对于式(5.29)积分有

$$V (x (\tau)) - V (x _ {0}) \leqslant \frac {1}{2} \gamma^ {2} \int_ {0} ^ {\tau} \| u (t) \| _ {2} ^ {2} d t - \frac {1}{2} \int_ {0} ^ {\tau} \| y (t) \| _ {2} ^ {2} d t$$

其中，对于每个给定的 $u \in \mathcal{L}_{2e}, x(t)$ 为方程(5.26)的解。由 $V(x) \geqslant 0$ ，得

$$\int_ {0} ^ {\tau} \| y (t) \| _ {2} ^ {2} d t \leqslant \gamma^ {2} \int_ {0} ^ {\tau} \| u (t) \| _ {2} ^ {2} d t + 2 V (x _ {0})$$

取平方根,并对于非负数 a 和 b 应用不等式 $\sqrt{a^{2}+b^{2}}\leqslant a+b$ , 可得

$$\left\| y _ {\tau} \right\| _ {\mathcal {L} _ {2}} \leqslant \gamma \left\| u _ {\tau} \right\| _ {\mathcal {L} _ {2}} + \sqrt {2 V \left(x _ {0}\right)} \tag {5.30}$$

证毕。

□

不等式(5.28)称为Hamilton-Jacobi不等式,当该式取“=”时,称为Hamilton-Jacobi等式。要找到满足不等式(5.28)的函数 $V(x)$ ，至少需要求解偏微分方程，而这是十分困难的。如果找到了 $V(x)$ ，就得到了一个有限增益 $L_{2}$ 稳定性的结果，不像定理5.1，它不要求无激励系统的原点为指数稳定的。下例将说明这一点。

例5.8 考虑单输入-单输出系统

$$
\begin{array}{l} \dot {x} _ {1} = x _ {2} \\ \dot {x} _ {2} = - a x _ {1} ^ {3} - k x _ {2} + u \\ y = x _ {2} \\ \end{array}
$$

其中 $a$ 和 $k$ 为正常数。该无激励系统是例4.9中所研究的一类系统的特例。在例4.9中，用类能量李雅普诺夫函数 $V(x) = ax_{1}^{4} / 4 + x_{2}^{2} / 2$ 证明了原点是全局渐近稳定的。用 $V(x) = \alpha (ax_1^4 /4 + x_2^2 /2)(\alpha >0)$ 作为Hamilton-Jacobi不等式(5.28)的备选解，可以证明

$$\mathcal {H} (V, f, G, h, \gamma) = \left(- \alpha k + \frac {\alpha^ {2}}{2 \gamma^ {2}} + \frac {1}{2}\right) x _ {2} ^ {2}$$
