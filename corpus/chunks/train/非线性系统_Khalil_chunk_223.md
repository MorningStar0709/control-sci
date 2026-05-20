注意方程(7.22)和方程(7.23)用两个实未知量 $\omega$ 和 $\hat{a}_{0}$ 以及一个复未知量 $\hat{a}_{1}$ 定义了一个实数方程(7.22)和一个复数方程(7.23)。当用实数表示时，这些方程是以四个未知数定义了三个方程。这是符合要求的，因为自治系统的时间原点是任意的，所以如果 $(\hat{a}_{0},\hat{a}_{1})$ 满足方程，则 $(\hat{a}_{0},\hat{a}_{1}e^{i\theta})$ 是另一个解， $\theta$ 为任意实数。为了解决不唯一性，取 $y(t)$ 的一次谐波为 $a\sin\omega t$ ，其中 $a\geqslant0$ ，即选择时间原点，使一次谐波的相位为零。利用

$$a \sin \omega t = \frac {a}{2 j} [ \exp (j \omega t) - \exp (- j \omega t) ] \Rightarrow \hat {a} _ {1} = \frac {a}{2 j}$$

方程(7.22)和方程(7.23)可重写为

$$G (0) \hat {c} _ {0} \left(\hat {a} _ {0}, \frac {a}{2 j}\right) + \hat {a} _ {0} = 0 \tag {7.24}G (j \omega) \hat {c} _ {1} \left(\hat {a} _ {0}, \frac {a}{2 j}\right) + \frac {a}{2 j} = 0 \tag {7.25}$$

因为方程(7.24)与 $\omega$ 无关, 所以当 $a$ 为 $\hat{a}_0$ 的函数时方程可解。注意, 如果 $\psi(\cdot)$ 是奇函数, 即

$$\psi (- y) = - \psi (y)$$

那么 $\hat{a}_0 = \hat{c}_0 = 0$ 就是方程(7.24)的一个解，因为

$$\hat {c} _ {0} = \frac {\omega}{2 \pi} \int_ {0} ^ {2 \pi / \omega} \psi (\hat {a} _ {0} + a \sin \omega t) d t$$

为方便起见, 只研究奇对称特性的非线性, 并取 $\hat{a}_{0} = \hat{c}_{0} = 0$ , 那么方程 (7.25) 可重写为

$$G (j \omega) \hat {c} _ {1} \left(0, \frac {a}{2 j}\right) + \frac {a}{2 j} = 0 \tag {7.26}$$

系数 $\hat{c}_1(0, a/2j)$ 是当非线性输入为正弦信号 $a \sin \omega t$ 时，其输出一次谐波的复傅里叶系数：

$$
\begin{array}{l} \hat {c} _ {1} (0, a / 2 j) = \frac {\omega}{2 \pi} \int_ {0} ^ {2 \pi / \omega} \psi (a \sin \omega t) \exp (- j \omega t) d t \\ = \frac {\omega}{2 \pi} \int_ {0} ^ {2 \pi / \omega} [ \psi (a \sin \omega t) \cos \omega t - j \psi (a \sin \omega t) \sin \omega t ] d t \\ \end{array}
$$

积分号内的第一项为奇函数,而第二项为偶函数。因此,在一个周期内第一项积分为零,由此积分化简为

$$\hat {c} _ {1} (0, a / 2 j) = - j \frac {\omega}{\pi} \int_ {0} ^ {\pi / \omega} \psi (a \sin \omega t) \sin \omega t d t$$

定义函数 $\Psi(a)$ 为

$$\Psi (a) = \frac {\hat {c} _ {1} (0 , a / 2 j)}{a / 2 j} = \frac {2 \omega}{\pi a} \int_ {0} ^ {\pi / \omega} \psi (a \sin \omega t) \sin \omega t d t \tag {7.27}$$

因此方程(7.26)可重写为

$$[ G (j \omega) \Psi (a) + 1 ] a = 0 \tag {7.28}$$

由于不考虑 $a = 0$ 时的解，因此可以通过求下列方程的所有解，得到方程(7.28)的全解：

$$G (j \omega) \Psi (a) + 1 = 0 \tag {7.29}$$

方程(7.29)称为一阶调和平衡方程,或简称为调和平衡方程。由式(7.27)定义的函数 $\Psi(a)$ 称为非线性特性 $\psi$ 的描述函数,通过在非线性特性的输入端加一正弦信号 $a \sin \omega t$ ,然后计算输出端一次谐波的傅里叶系数与 $a$ 的比值,即可求得 $\Psi(a)$ ,可被认为是输入为 $a \sin \omega t$ ,响应为 $\Psi(a)a \sin \omega t$ 的线性时不变单元的等效增益。这种等效增益的概念(有时也称等效线性化)也可应用到一般的时变非线性特性或有记忆的非线性特性中,比如迟滞和回差特性①。一般在这样的背景下,描述函数可能是复变函数,且与 $a$ 和 $\omega$ 都有关。我们只考虑奇对称、时不变、无记忆非线性特性的描述函数,其 $\Psi(a)$ 是实函数,且仅与 $a$ 有关,由下面的表达式给出:
