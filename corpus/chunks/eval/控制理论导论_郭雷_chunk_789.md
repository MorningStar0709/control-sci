$$\dot {E} _ {\varepsilon} (t) \leqslant 0, \quad \forall t > T _ {0}.$$

另一方面，从Cauchy不等式可得

$$| G (t) | \leqslant \frac {1}{2} \int_ {0} ^ {1} (\dot {y} ^ {2} + y ^ {\prime 2}) \mathrm{d} x \leqslant M E (t),$$

其中 $M$ 为某一正常数。于是根据引理10.4.2，系统(10.4.22)，即方程(10.4.21)的能量是指数衰减的。

例10.4.4 (Euler-Bernoulli 梁的耗散边界反馈镇定) 考虑带耗散边界反馈的 Euler-Bernoulli 梁方程

$$
\left\{ \begin{array}{l l} \ddot {y} (x, t) + a ^ {4} y ^ {\prime \prime \prime \prime} (x, t) = 0, & 0 <   x <   1, t > 0, \\ y (0, t) = 0, y ^ {\prime} (0, t) = 0, & \\ a ^ {4} y ^ {\prime \prime} (1, t) = - \alpha \dot {y} ^ {\prime} (1, t), & \alpha \geqslant 0, \\ a ^ {4} y ^ {\prime \prime \prime} (1, t) = \beta \dot {y} (1, t), & \beta > 0, \end{array} \right. \tag {10.4.23}
$$

这里梁的长度取为 $1, a^4 = \frac{EI}{\rho}, \rho$ 和 $EI$ 分别为梁的线密度和弹性刚度系数，梁的一端 $x = 0$ 固定，而在另一端 $x = 1$ 施加力和力矩反馈控制， $\alpha$ 和 $\beta$ 为反馈增益系数。系统 (10.4.21) 的能量是

$$E (t) = \frac {1}{2} \int_ {0} ^ {1} \left(| \dot {y} (x, t) | ^ {2} + a ^ {4} | y ^ {\prime \prime} (x, t) | ^ {2}\right) d x.$$

设系统的状态空间为能量空间 $\mathcal{H} = V_0^2 (0,1)\times L^2 (0,1)$ ，其中

$$V _ {0} ^ {k} (0, 1) = \left\{f \in H ^ {k} (0, 1) \mid f (0) = 0, f ^ {\prime} (0) = 0 \right\}, \quad k \geqslant 2.$$

$\mathcal{H}$ 中内积为

$$\langle [ f _ {1}, g _ {1} ] ^ {\mathrm{T}}, [ f _ {2}, g _ {2} ] ^ {\mathrm{T}} \rangle = \int_ {0} ^ {1} \left(g _ {1} (x) \overline {{g}} _ {2} (x) + a ^ {4} f _ {1} ^ {\prime \prime} (x) \overline {{f}} _ {2} ^ {\prime \prime} (x)\right) \mathrm{d} x.$$

在 $\mathcal{H}$ 中定义线性算子 $\mathcal{A}$

$$\mathcal {A} [ \varphi , \psi ] ^ {\mathrm{T}} = [ \psi . - a ^ {4} \varphi^ {\prime \prime} ] ^ {\mathrm{T}}. \quad \forall [ \varphi , \psi ] ^ {\mathrm{T}} \in \mathcal {D} (\mathcal {A}).\mathcal {D} (\mathcal {A}) = \left\{\left[ \varphi . w \right] ^ {\mathrm{T}} \mid \varphi \in V _ {0} ^ {- 1} (0, 1), w \in V _ {0} ^ {2} (0, 1), \right.a ^ {4} \varphi^ {\prime \prime} (1) = - \alpha \iota^ {\prime} (1), a ^ {4} \varphi^ {\prime \prime \prime} (1) = \beta \psi (1) \}.$$

于是方程 (10.4.23) 可以写成 $\mathcal{H}$ 中线性发展方程

$$\dot {Y} (t) = \mathcal {A} Y (t), \tag {10.4.24}$$

其中 $Y(t)=[y(\cdot,t),\dot{y}(\cdot,t)]^{\mathrm{T}}$ .

同样可以证明， $\mathcal{A}$ 是 $\mathcal{H}$ 中极大耗散算子（留作练习）。从而 $\mathcal{A}$ 生成 $\mathcal{H}$ 中某个 $C_0$ 压缩半群 $T(t)$ 。当初始值 $Y_0 \in \mathcal{H}$ 时 $Y(t) = T(t)Y_0$ 是弱解，而当 $Y_0 \in \mathcal{D}(\mathcal{A})$ 时 $Y(t) = T(t)Y_0$ 是强解。而且系统能量恰好是 $E(t) = \frac{1}{2} \| Y(t) \|_{\mathcal{H}}$ 。我们有
