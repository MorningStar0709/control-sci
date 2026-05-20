# 10.5 波方程控制

本节介绍波动方程的控制问题，这一领域的结果相当丰富。我们仅对常系数情形的分布反馈镇定和边界反馈镇定作一简单的叙述，这里仍然采用乘子法。

例10.5.1（波方程的分布反馈镇定） 考虑带分布反馈的波方程

$$
\left\{ \begin{array}{l l} \ddot {y} (x, t) + b (x) \dot {y} (x, t) - \Delta y (x, t) = 0, & x \in \Omega , t > 0, \\ y (s, t) | _ {\partial \Omega} = 0, \quad t > 0, \\ y (x, 0) = y _ {0} (x), \quad \dot {y} (x, 0) = y _ {1} (x), & x \in \Omega , \end{array} \right. \tag {10.5.1}
$$

这里 $\Omega \in \mathbb{R}^n$ 为有界开区域，满足Dirichlet边条件， $b$ 为 $\Omega$ 上充分光滑函数，满足 $0 < b_{1} \leqslant b(x) \leqslant b_{2}, \forall x \in \Omega,$ 其中 $b_{1}$ 和 $b_{2}$ 为两个正常数.

设状态空间取 $\mathcal{H} = H_0^1 (\Omega)\times L^2 (\Omega)$ ，其中内积为

$$\left(\left[ f _ {1}, g _ {1} \right] ^ {\mathrm{T}}, \left[ f _ {2}, g _ {2} \right] ^ {\mathrm{T}}\right) = \int_ {\Omega} \left(\langle \nabla f _ {1}, \nabla f _ {2} \rangle + g _ {1} g _ {2}\right) \mathrm{d} x,$$

这里及今后， $\langle \cdot, \cdot \rangle$ 表示 $\mathbb{R}^N$ 上的欧氏内积，而 $|\cdot|$ 则表示 $\mathbb{R}^N$ 中向量的欧氏范数，有时也表示一数的绝对值。在 $\mathcal{H}$ 中定义线性算子 $\mathcal{A}$

$$\mathcal {A} [ \varphi , \psi ] ^ {\mathrm{T}} = [ \psi , \Delta \varphi - b \psi ] ^ {\mathrm{T}}, \quad \forall [ \varphi , \psi ] ^ {\mathrm{T}} \in \mathcal {D} (\mathcal {A}),\mathcal {D} (\mathcal {A}) = \left\{\left[ \varphi , \psi \right] ^ {\mathrm{T}} \mid \varphi \in H ^ {2} (\Omega) \cap H _ {0} ^ {1} (\Omega), \psi \in H _ {0} ^ {1} (\Omega) \right\}.$$

于是方程 (10.5.1) 可以写成 $\mathcal{H}$ 中线性发展方程

$$\dot {Y} (t) = \mathcal {A} Y (t), \tag {10.5.2}$$

其中 $Y(t)=[y(\cdot,t),\dot{y}(\cdot,t)]^{T}.$

同样可以证明， $\mathcal{A}$ 是 $\mathcal{H}$ 中极大耗散算子（留作练习）。从而 $\mathcal{A}$ 生成 $\mathcal{H}$ 中某个 $C_0$ 压缩半群 $T(t)$ 。当初始值 $Y_0 \in \mathcal{H}$ 时 $Y(t) = T(t)Y_0$ 是弱解，而当 $Y_0 \in \mathcal{D}(\mathcal{A})$ 时 $Y(t) = T(t)Y_0$ 是强解。系统能量是

$$E (t) = \frac {1}{2} \| Y (t) \| _ {\mathcal {H}} = \frac {1}{2} \int_ {\Omega} \left(| \nabla y | ^ {2} + | \dot {y} | ^ {2}\right) \mathrm{d} x.$$

我们有

$$\dot {E} (t) = - \int_ {\Omega} b (x) | \dot {y} (x, t) | ^ {2} \mathrm{d} x,$$

从而系统能量是耗散的。下面我们利用乘子法证明系统能量 $E(t)$ 是指数衰减的，即由 $\mathcal{A}$ 生成的半群 $T(t)$ 是指数稳定的。

取

$$E _ {\lambda} (t) = \frac {1}{2} \int_ {\Omega} \left(| \nabla y | ^ {2} + | \dot {y} | ^ {2}\right) d x + \lambda \int_ {\Omega} \left(2 \dot {y} y + b | y | ^ {2}\right) d x.$$

于是
