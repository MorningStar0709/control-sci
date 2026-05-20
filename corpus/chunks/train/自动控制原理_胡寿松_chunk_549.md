# (1) 描述函数的定义

设非线性环节输入输出描述为

$$y = f (x) \tag {8-50}$$

当非线性环节的输入信号为正弦信号

$$x (t) = A \sin \omega t \tag {8-51}$$

时, 可对非线性环节的稳态输出 $y(t)$ 进行谐波分析。一般情况下, $y(t)$ 为非正弦的周期信号, 可以展开成傅里叶级数:

$$y (t) = A _ {0} + \sum_ {n = 1} ^ {\infty} (A _ {n} \cos n \omega t + B _ {n} \sin n \omega t) = A _ {0} + \sum_ {n = 1} ^ {\infty} Y _ {n} \sin (n \omega t + \varphi_ {n})$$

式中， $A_0$ 为直流分量； $Y_{n}\sin (n\omega t + \varphi_{n})$ 为第 $n$ 次谐波分量，且有

$$Y _ {n} = \sqrt {A _ {n} ^ {2} + B _ {n} ^ {2}}, \quad \varphi_ {n} = \arctan \frac {A _ {n}}{B _ {n}} \tag {8-52}$$

式中， $A_{n}, B_{n}$ 为傅里叶系数，

$$A _ {n} = \frac {1}{\pi} \int_ {0} ^ {2 \pi} y (t) \cos n \omega t d \omega t, \quad B _ {n} = \frac {1}{\pi} \int_ {0} ^ {2 \pi} y (t) \sin n \omega t d \omega t \quad (n = 1, 2, \dots) \tag {8-53}$$

而直流分量

$$A _ {0} = \frac {1}{2 \pi} \int_ {0} ^ {2 \pi} y (t) \mathrm{d} \omega t \tag {8-54}$$

若 $A_0 = 0$ 且当 $n > 1$ 时， $Y_{n}$ 均很小，则可近似认为非线性环节的正弦响应仅有一次谐波分量

$$y (t) \approx A _ {1} \cos \omega t + B _ {1} \sin \omega t = Y _ {1} \sin (\omega t + \varphi_ {1}) \tag {8-55}$$

上式表明,非线性环节可近似认为具有和线性环节相类似的频率响应形式。为此,定义正弦输入信号作用下,非线性环节的稳态输出中一次谐波分量和输入信号的复数比为非线性环节的描述

函数,用 $N(A)$ 表示,即

$$N (A) = \left| N (A) \right| \mathrm{e} ^ {\mathrm{j} \angle N (A)} = \frac {Y _ {1}}{A} \mathrm{e} ^ {\mathrm{j} \varphi_ {1}} = \frac {B _ {1} + \mathrm{j} A _ {1}}{A} \tag {8-56}$$

例8-3 设继电特性为

$$
y (x) = \left\{ \begin{array}{l l} - M, & x <   0 \\ M, & x > 0 \end{array} \right. \tag {8-57}
$$

试计算该非线性特性的描述函数。

解 $x = A\sin \omega t$

$$
y (t) = \left\{ \begin{array}{l l} M, & 0 <   \omega t <   \pi \\ - M, & \pi <   \omega t <   2 \pi \end{array} \right.
A _ {0} = \frac {1}{2 \pi} \int_ {0} ^ {2 \pi} y (t) d \omega t = \frac {M}{2 \pi} \left(\int_ {0} ^ {\pi} d \omega t - \int_ {\pi} ^ {2 \pi} d \omega t\right) = 0A _ {1} = \frac {1}{\pi} \int_ {0} ^ {2 \pi} y (t) \cos \omega t d \omega t = \frac {M}{\pi} \left(\int_ {0} ^ {\pi} \cos \omega t d \omega t - \int_ {\pi} ^ {2 \pi} \cos \omega t d \omega t\right)= \frac {M}{\pi} \left(\sin u \left| _ {0} ^ {\pi} - \sin u \right| _ {\pi} ^ {2 \pi}\right) = 0B _ {1} = \frac {1}{\pi} \int_ {0} ^ {2 \pi} y (t) \sin \omega t d \omega t = \frac {M}{\pi} \left(- \cos u \left| _ {0} ^ {\pi} + \cos u \right| _ {\pi} ^ {2 \pi}\right) = \frac {4 M}{\pi}N (A) = \frac {B _ {1} + \mathrm{j} A _ {1}}{A} = \frac {4 M}{\pi A} \tag {8-58}
$$

一般情况下，描述函数 $N$ 是输入信号幅值 $A$ 和频率 $\omega$ 的函数。当非线性环节中不包含储能元件时，其输出的一次谐波分量的幅值和相位差与 $\omega$ 无关，故描述函数只与输入信号幅值 $A$ 有关。至于直流分量，若非线性环节的正弦响应为关于 $t$ 的奇对称函数，即
