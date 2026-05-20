为了得到镇定控制，我们首选 $a_1, a_2, a_3$ 使其镇定线性能控变量 $x_1, x_2, x_3$ ，然后选 $b$ 镇定中心流形变量 $z$ 。为确定 $b$ 的值，设

$$
\varphi (z) = \left[ \begin{array}{l} \varphi_ {1} (z) \\ \varphi_ {2} (z) \\ \varphi_ {3} (z) \end{array} \right] = O (\| z \| ^ {2})
$$

为中心流形的一个近似. 对系统 (8.6.1), 定义算子 $M$ 如下 [6]:

$$M (\varphi (z)) = \frac {\partial \varphi (z)}{\partial z} (C z + q (\varphi (z), z)) - A \varphi (z) - p (\varphi (z), z).$$

于是对系统 (8.6.10) 我们有

$$
\begin{array}{l} M \varphi (z) = D \varphi (z) \left(q (z) \varphi_ {1} (z)\right) - \left[ \begin{array}{c} \varphi_ {2} (z) \\ \varphi_ {3} (z) \\ a _ {1} \varphi_ {1} (z) + a _ {2} \varphi_ {2} (z) + a _ {3} \varphi_ {3} (z) + b z ^ {2} \end{array} \right] \\ = O (\| z \| ^ {4}) - \left[ \begin{array}{c} \varphi_ {2} (z) \\ \varphi_ {3} (z) \\ a _ {1} \varphi_ {1} (z) + a _ {2} \varphi_ {2} (z) + a _ {3} \varphi_ {3} (z) + b z ^ {2} \end{array} \right]. \\ \end{array}
$$

取

$$
\left\{ \begin{array}{l} \varphi_ {1} = - \frac {b}{a _ {1}} z ^ {2}, \\ \varphi_ {i} = 0, \quad i = 2, 3. \end{array} \right.
$$

那么 $M\varphi (z) = O(\| z\|^4)$ . 由逼近定理，中心流形可表示为

$$
\left\{ \begin{array}{l} x _ {1} = h _ {1} (z) = - \frac {b}{a _ {1}} z ^ {2} + O (\| z \| ^ {4}), \\ x _ {i} = h _ {i} (z) = O (\| z \| ^ {4}), \quad i = 2, 3. \end{array} \right. \tag {8.6.13}
$$

中心流形上的动力系统为

$$\dot {z} = \left(1 - \frac {b}{a}\right) z ^ {3} + O (\| z \| ^ {4}). \tag {8.6.14}$$

取 $\{a_1, a_2, a_3, b\}$ 使反馈系统的线性部分是 Hurwitz 的，且

$$1 - \frac {b}{a _ {1}} < 0,$$

比如取 $a_1 = -1, a_2 = a_3 = -3, b = -2$ ，就满足上述要求。反馈控制为

$$u = - \frac {f (x , z)}{g (x , z)} + \frac {1}{g (x , z)} (- x _ {1} - 3 x _ {2} - 3 x _ {3} - 2 z ^ {2}).$$

于是系统 (8.6.13) 在原点是渐近稳定的。由等价定理知，闭环系统是渐近稳定的。

由上述例子可以得到以下几点启示：

(1) 高阶状态反馈不影响线性能控状态的稳定性，但它可通过改变中心流形结构影响中心部分的变量；  
(2) 高阶反馈可由每个积分列的第一个变量 $x_{1}$ 注入系统。 $x_{1}$ 不影响中心流形的逼近阶。线性部分的这个分量可用来改变非线性动态；

(3) 由于中心流形方程难以解出，一般只能得到一定阶数的逼近，因此中心流形上的动力学系统必须有相应阶数的鲁棒稳定性。因为一般只能得到中心流形的一个近似，因此需要一套工具检验如何通过中心流形的动力系统的近似系统的稳定性来判断动力系统自身的稳定性。为此本节介绍一个新概念：“齐次导数 Lyapunov 函数”。

考虑动力系统

$$\dot {x} = f (x), \qquad x \in \mathbb {R} ^ {n}, \tag {8.6.15}$$

这里 $f(0) = 0$

记 $Z_{+}$ 为非负整数集. 对一个 n 重指标 $S = [s_{1}, \cdots, s_{n}] \in Z_{+}^{n}$ 及 $x = [x_{1}, \cdots, x_{n}] \in R^{n}$ ，我们记

$$| S | = \sum_ {i = 1} ^ {n} s _ {i}, \quad x ^ {S} = \prod_ {i = 1} ^ {n} (x _ {i}) ^ {s _ {i}}, \quad S! = \prod_ {i = 1} ^ {n} s _ {i}!.$$

这里我们约定 $0! = 1$ ，故 $S! \neq 0$ 。对一个光滑函数 $F(x)$ ，记
