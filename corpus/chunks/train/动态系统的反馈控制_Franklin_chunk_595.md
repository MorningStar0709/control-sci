# 例9.10 饱和非线性的描述函数

图 9.25a 所示的为饱和非线性，它也是控制系统中最为常见的非线性。饱和函数定义为

$$
\operatorname{sat} (x) = \left\{ \begin{array}{l l} + 1, & x > 1 \\ x, & | x | \leqslant 1 \\ - 1, & x <   - 1 \end{array} \right.
$$

![](image/f402744d9b69c9aa5b86b68b39145c175a10e19bf9fc21b3c789644bff4a5b2d.jpg)

<details>
<summary>text_image</summary>

u →
-N
-h O
h
u → y
</details>

a）饱和非线性

![](image/f9b7dc9c7161347fdf1b0743bdfd45fc807d210946da15e24c8b98d621b9e1e1.jpg)

<details>
<summary>line</summary>

| t | u |
| --- | --- |
| t₀ | y |
| t₁ | u |
| t₂ | u |
</details>

b）输入和输出信号  
图 9.25

如果线性区域的斜率为 $k$ ，且最终的饱和值为 $\pm N$ ，那么这个函数就是

$$y = N \mathrm{sat} (\frac {k}{N} x)$$

给出这个非线性的描述函数。

解答。考虑图9.25所示的饱和环节的输入、输出信号。对于幅值为 $a \leqslant \frac{N}{k}$ 的输入正弦信号 $u = a \sin (\omega t)$ ，输出使得描述函数恰为单位增益。当 $a \geqslant \frac{N}{k}$ 时，我们需要计算输出所含基波分量的幅值和相位。由于饱和是一个奇函数，式(9.21)中的所有余弦项都是零，并且 $a_1 = 0$ 。根据式(9.27)，有

$$K _ {\mathrm{eq}} (a) = \frac {b _ {1}}{a}$$

使得

$$b _ {1} = \frac {2}{\pi} \int_ {0} ^ {\pi} N \mathrm{sat} \left(\frac {k}{N} a \sin (\omega t)\right) \sin (\omega t) \mathrm{d} (\omega t)$$

由于系数 $b_{1}$ 在区间 $\omega t = [0, \pi]$ 上的积分是在区间 $\omega t = [0, \pi / 2]$ 上积分的2倍。于是

$$b _ {1} = \frac {4 N}{\pi} \int_ {0} ^ {\frac {\pi}{2}} \mathrm{sat} \left(\frac {k}{N} a \sin (\omega t)\right) \sin (\omega t) \mathrm{d} (\omega t)$$

现在，我们能将积分分为线性和饱和两部分。定义饱和时间 $t_{s}$ 为

$$t _ {s} = \frac {1}{\omega} \arcsin \left(\frac {N}{a k}\right) \quad \text {或} \quad \omega t _ {s} = \arcsin \left(\frac {N}{a k}\right) \tag {9.28}$$

那么

$$
\begin{array}{l} b _ {1} = \frac {4 N \omega}{\pi a} \left[ \int_ {0} ^ {\omega t _ {s}} \operatorname{sat} \left(\frac {k}{N} a \sin (\omega t)\right) \sin (\omega t) \mathrm{d} t + \int_ {\omega t _ {s}} ^ {\frac {\pi}{2}} \sin (\omega t) \mathrm{d} t \right] \\ = \frac {4 N \omega}{\pi a} \left[ \int_ {0} ^ {\omega t _ {\mathrm{s}}} \frac {k}{N} a \sin^ {2} (\omega t) \mathrm{d} t + \int_ {\omega t _ {\mathrm{s}}} ^ {\frac {\pi}{2}} \sin (\omega t) \mathrm{d} t \right] \\ = \frac {4 N \omega}{\pi a} \left[ \int_ {0} ^ {\omega t _ {\mathrm{s}}} \frac {k}{2 N} a (1 - \cos (2 \omega t)) \mathrm{d} t + \int_ {\omega t _ {\mathrm{s}}} ^ {\frac {\pi}{2}} \sin (\omega t) \mathrm{d} t \right] \\ = \frac {4 N \omega}{\pi a} \left[ \frac {k}{2 N} a t \Big | _ {0} ^ {t _ {\mathrm{s}}} - \frac {k}{2 N} a \sin (2 \omega t) \Big | _ {0} ^ {t _ {\mathrm{s}}} - \frac {1}{\omega} (\cos \frac {\pi}{2} - \cos t _ {\mathrm{s}}) \right] \\ \end{array}
$$

利用式 $(9.28)$ ，我们得到

$$\sin (\omega t _ {\mathrm{s}}) = \frac {N}{k a}, \cos (\omega t _ {\mathrm{s}}) = \sqrt {1 - \left(\frac {N}{k a}\right) ^ {2}}$$

最终得到

$$
K _ {\mathrm{eq}} (a) = \left\{ \begin{array}{l l} \frac {2}{\pi} \Big [ k \arcsin \Big (\frac {N}{a k} \Big) + \frac {N}{a} \sqrt {1 - \Big (\frac {N}{a k} \Big) ^ {2}} \Big ], & \frac {k a}{N} > 1 \\ k, & \frac {k a}{N} \leqslant 1 \end{array} \right. \tag {9.29}
$$

图 9.26 给出了 $K_{\mathrm{eq}}(a)$ 的图，该图表明了该描述函数是不依赖频率的实值函数，因此不会导致相移。可以看到描述函数开始时为常数，之后作为输入信号幅值 a 的倒数函数衰减。
