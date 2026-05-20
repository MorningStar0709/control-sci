$$\Psi (a) = \frac {2}{\pi a} \int_ {0} ^ {\pi} \psi (a \sin \theta) \sin \theta d \theta \tag {7.30}$$

该式是将式(7.27)中的积分变量由 t 换成 $\theta = \omega t$ 得到的。

描述函数法说明,如果方程(7.29)有一个解 $(a_{s},\omega_{s})$ ,那么系统“可能”有一个周期解,其振荡频率和振幅(在非线性的输入端)接近 $\omega_{s}$ 和 $a_{s}$ 。相反,如果方程(7.29)没有解,系统“可能”无周期解。当存在一个周期解时,把“可能”换成“一定”及用量化替代“接近 $\omega_{s}$ 和 $a_{s}$ ”一句则需要进行更多的分析,本节后续部分将进行这方面的研究,这里将进一步讨论描述函数的计算和调和平衡方程(7.29)的求解问题。下面三个例题说明奇非线性特性描述函数的计算。

例7.6 考虑正负号函数非线性特性 $\psi(y) = \mathrm{sgn}(y)$ ，其描述函数为

$$\Psi (a) = \frac {2}{\pi a} \int_ {0} ^ {\pi} \psi (a \sin \theta) \sin \theta d \theta = \frac {2}{\pi a} \int_ {0} ^ {\pi} \sin \theta d \theta = \frac {4}{\pi a}$$

△

例7.7 考虑图7.15所示的分段线性函数,如果该非线性正弦输入的振幅 $a \leqslant \delta$ ,那么非线性相当于线性增益,输出是幅度为 $s_{1}a$ 的正弦信号。因此,描述函数是 $\Psi(a) = s_{1}$ ,与a无关。当 $a > \delta$ 时,对式(7.30)右边进行分段积分,每一段对应 $\psi(\cdot)$ 的一个线性部分。然后利用输出波形的奇对称性,可将积分简化为

$$
\begin{array}{l} \Psi (a) = \frac {2}{\pi a} \int_ {0} ^ {\pi} \psi (a \sin \theta) \sin \theta d \theta = \frac {4}{\pi a} \int_ {0} ^ {\pi / 2} \psi (a \sin \theta) \sin \theta d \theta \\ = \frac {4}{\pi a} \int_ {0} ^ {\beta} a s _ {1} \sin^ {2} \theta d \theta \\ + \frac {4}{\pi a} \int_ {\beta} ^ {\pi / 2} [ \delta s _ {1} + s _ {2} (a \sin \theta - \delta) ] \sin \theta d \theta , \quad \beta = \arcsin \left(\frac {\delta}{a}\right) \\ = \frac {2 s _ {1}}{\pi} \left(\beta - \frac {1}{2} \sin 2 \beta\right) + \frac {4 \delta \left(s _ {1} - s _ {2}\right)}{\pi a} \left(\cos \beta - \cos \frac {\pi}{2}\right) \\ + \frac {2 s _ {2}}{\pi} \left(\frac {\pi}{2} - \frac {1}{2} \sin \pi - \beta + \frac {1}{2} \sin 2 \beta\right) \\ = \frac {2 (s _ {1} - s _ {2})}{\pi} \left(\beta + \frac {\delta}{a} \cos \beta\right) + s _ {2} \\ \end{array}
$$

这样， $\Psi (a) = \frac{2(s_1 - s_2)}{\pi}\left[\arcsin \left(\frac{\delta}{a}\right) + \frac{\delta}{a}\sqrt{1 - \left(\frac{\delta}{a}\right)^2}\right] + s_2$

描述函数如图7.16所示。通过选择 $\delta$ 及斜率 $s_1$ 和 $s_2$ 的值，可以得到几个常用非线性特性的描述函数。例如，饱和非线性特性是图7.15所示分段线性函数的特例，即 $\delta = 1, s_1 = 1$ 和 $s_2 = 0$ 时的情况，因此其描述函数为

$$
\Psi (a) = \left\{ \begin{array}{l l} 1, & 0 \leqslant a \leqslant 1 \\ \frac {2}{\pi} \left[ \arcsin \left(\frac {1}{a}\right) + \frac {1}{a} \sqrt {1 - \left(\frac {1}{a}\right) ^ {2}} \right], & a > 1 \end{array} \right.
$$

△

![](image/3ef3b71d418158ad19910cf11a1ea686b540a69b4fea3229c4f00c5992cd5487.jpg)

<details>
<summary>text_image</summary>
