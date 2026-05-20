# C. 13 证明引理 7.1

首先写出无限维方程(7.20)的时域表达式,考虑所有基频为 $\omega$ 的半波对称周期信号空间 S, 在有限区间内能量有限。可以看出这个信号在有限区间内是能量有限的,信号 $y \in S$ 可由其傅里叶级数表示为

$$y (t) = \sum_ {k \text { odd }} a _ {k} \exp (j k \omega t), \quad \sum_ {k \text { odd }} | a _ {k} | ^ {2} < \infty$$

定义S上的范数为 $\|y\|^{2}=\frac{\omega}{\pi}\int_{0}^{2\pi/\omega}y^{2}(t)dt=2\sum_{k\mathrm{odd}}|a_{k}|^{2}$

在此范数下，S是Banach空间，定义 $g_{k}(t - \tau)$ 为

$$g _ {k} (t - \tau) = \frac {\omega}{\pi} \left\{G (j k \omega) \exp [ j k \omega (t - \tau) ] + G (- j k \omega) \exp [ - j k \omega (t - \tau) ] \right\}$$

当 $m$ 为奇数且 $k > 0$ 时，有

$$
\int_ {0} ^ {\pi / \omega} g _ {k} (t - \tau) \exp (j m \omega \tau) d \tau = \left\{ \begin{array}{l l} G (j k \omega) \exp (j k \omega t), & m = k \\ G (- j k \omega) \exp (- j k \omega t), & m = - k \\ 0, & | m | \neq k \end{array} \right. \tag {C.44}
$$

定义S上的线性映射 g 和非线性映射 $g \psi$ 为

$$g y = \int_ {0} ^ {\pi / \omega} \sum_ {k \text {odd}; k > 0} g _ {k} (t - \tau) y (\tau) d \taug \psi y = \int_ {0} ^ {\pi / \omega} \sum_ {k \text {odd}; k > 0} g _ {k} (t - \tau) \psi (y (\tau)) d \tau$$

其中 $y(t)=\sum_{k\text{ odd }}a_{k}\exp(jk\omega t),\quad\psi(y(t))=\sum_{k\text{ odd }}c_{k}\exp(jk\omega t)$

由方程(C.44)可看出

$$g y = \sum_ {k \text {odd}} G (j k \omega) a _ {k} \exp (j k \omega t)g \psi y = \sum_ {k \text {odd}} G (j k \omega) c _ {k} \exp (j k \omega t)$$

在这些定义下,半波对称周期振荡存在的条件为

$$y = - g \psi y \tag {C.45}$$

方程(C.45)与方程(7.20)等价。为了消除高次谐波对基波的影响,定义映射 $P_{1}$ 为

$$P _ {1} y = y _ {1} = a _ {1} \exp (j \omega t) + \bar {a} _ {1} \exp (- j \omega t) = 2 \operatorname{Re} \left[ a _ {1} \exp (j \omega t) \right]$$

及映射 $P_{h}$ 为 $P_{h}y = y_{h} = y - y_{1} = \sum_{k\mathrm{odd};|k|\neq 1}a_{k}\exp (jk\omega t)$

为不失一般性,取 $a_{1}=a/2j$ , 使得 $y_{1}(t)=a\sin\omega t$ , 求解方程(C.45)相当于求解方程(C.46)和方程(C.47):

$$y _ {h} = - P _ {h} g \psi \left(y _ {1} + y _ {h}\right) \tag {C.46}y _ {1} = - P _ {1} g \psi \left(y _ {1} + y _ {h}\right) \tag {C.47}$$

计算方程(C.47)的右边可看出,该方程等价于方程(7.35)。按照方程(7.36)定义的误差项 $\delta\Psi$ 满足 $P_{1}g\psi y_{1}-P_{1}g\psi(y_{1}+y_{h})=2\mathrm{Re}[G(j\omega)a_{1}\delta\Psi\exp(j\omega t)]$ (C.48)

这样,为了得到 $\delta\Psi$ 的边界,需要求出 $y_{h}$ 的边界,我们不求解方程(C.46),而是用压缩映射定理。在方程(C.46)的两端同加 $\left[P_{h}g(\beta+\alpha)/2\right]y_{h}$ ,得

$$\left(I + P _ {h} g \frac {\beta + \alpha}{2}\right) y _ {h} = - P _ {h} g \left[ \psi \left(y _ {1} + y _ {h}\right) - \frac {\beta + \alpha}{2} y _ {h} \right] \tag {C.49}$$

考虑出现在上式左边的线性映射 $K=I+P_{h}g(\beta+\alpha)/2$ ，它把S映射到S。给定任意 $z\in S$ ，定义
