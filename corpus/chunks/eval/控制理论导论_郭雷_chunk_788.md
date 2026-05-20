例 10.4.3 (弦振动耗散边界反馈镇定) 考虑弦振动方程

$$
\left\{ \begin{array}{l l} \ddot {y} (x, t) - c ^ {2} y ^ {\prime \prime} (x, t) = 0, & 0 <   x <   1, t > 0. \\ y (0, t) = 0, & c ^ {2} y ^ {\prime} (1, t) = - \alpha \dot {y} (1, t), \end{array} \right. \tag {10.4.21}
$$

其中为简单起见，弦的长度取为 $1, c^2 = K / \rho, \rho$ 和 $K$ 分别为弦的线密度和张力系数，弦的一端 $x = 0$ 固定，而在另一端 $x = 1$ 施加反馈控制， $\alpha > 0$ 为反馈增益系数。系统 (10.4.21) 的能量是

$$E (t) = \frac {1}{2} \int_ {0} ^ {1} \left(| \dot {y} (x, t) | ^ {2} + c ^ {2} | y ^ {\prime} (x, t) | ^ {2}\right) d x.$$

设系统的状态空间为能量空间 $\mathcal{H} = V_0^1 (0,1)\times L^2 (0,1)$ ，其中

$$V _ {0} ^ {k} (0, 1) = \left\{f \in H ^ {k} (0, 1) \mid f (0) = 0 \right\}, \quad k = 1, 2.$$

$\mathcal{H}$ 中内积为

$$\left\langle \left[ f _ {1}, g _ {1} \right] ^ {\mathrm{T}}, \left[ f _ {2}, g _ {2} \right] ^ {\mathrm{T}} \right\rangle = \int_ {0} ^ {1} \left(g _ {1} (x) \overline {{{g}}} _ {2} (x) + c ^ {2} f _ {1} ^ {\prime} (x) \overline {{{f}}} _ {2} ^ {\prime} (x)\right) \mathrm{d} x.$$

在 $\mathcal{H}$ 中定义线性算子 $\pmb{A}$

$$\mathcal {A} [ \varphi , \psi ] ^ {\mathrm{T}} = [ \psi , c ^ {2} \varphi^ {\prime \prime} ] ^ {\mathrm{T}}, \quad \forall [ \varphi , \psi ] ^ {\mathrm{T}} \in \mathcal {D} (\mathcal {A}).\mathcal {D} (\mathcal {A}) = \left\{\left[ \varphi , \psi \right] ^ {\mathrm{T}} \mid \varphi \in V _ {0} ^ {2} (0, 1), \psi \in V _ {0} ^ {1} (0, 1), c ^ {2} \varphi^ {\prime} (1) = - \alpha \psi (1) \right\}.$$

于是方程 (10.4.21) 可以写成 $\mathcal{H}$ 中线性发展方程

$$\dot {Y} (t) = \mathcal {A} Y (t), \tag {10.4.22}$$

其中 $Y(t) = [y(\cdot ,t),\dot{y} (\cdot ,t)]^{\mathrm{T}}$

可以证明， $\mathcal{A}$ 是 $\mathcal{H}$ 中极大耗散算子（留作练习）。从而 $\mathcal{A}$ 生成 $\mathcal{H}$ 中某个 $C_0$ 压缩半群 $T(t)$ 。当初始值 $Y_0 \in \mathcal{H}$ 时 $Y(t) = T(t)Y_0$ 是弱解，而当 $Y_0 \in \mathcal{D}(\mathcal{A})$ 时 $Y(t) = T(t)Y_0$ 是强解。而且系统能量恰好是 $E(t) = \frac{1}{2} \| Y(t) \|_{\mathcal{H}}$ 。我们有

$$\dot {E} (t) = - \alpha | \dot {y} (1, t) | ^ {2},$$

这表明能量是耗散的。下面我们利用乘子法证明系统能量 $E(t)$ 是指数衰减的，即由 $\mathcal{A}$ 生成的半群 $T(t)$ 是指数稳定的。

我们取能量摄动泛函

$$E _ {\varepsilon} (t) = (1 - \varepsilon) t E (t) + G (t),$$

其中 $0 < \varepsilon < 1$ ，而

$$G (t) = \frac {1}{2} \int_ {0} ^ {1} x (\dot {y} \overline {{{y}}} ^ {\prime} + \overline {{{\dot {y}}}} y ^ {\prime}) \mathrm{d} x.$$

我们有

$$\dot {E} _ {\varepsilon} (t) = - \varepsilon E (t) - \alpha (1 - \varepsilon) t | \dot {y} (1, t) | ^ {2} + \frac {1}{2} \left(\frac {\alpha^ {2}}{c ^ {2}} + 1\right) | \dot {y} (1, t) | ^ {2}.$$

由此可见，若令 $T_0 = \frac{\alpha^2 + c^2}{(1 - \varepsilon)c^2\alpha}, 0 < \varepsilon < 1$ ，则
