考察 $x_{1}, x_{2}$ 的有界区域 G 内有限步数的数值积分问题. 不妨假定 $x_{1}^{0} = x_{2}^{0} = 0$ .

系统(4.7.15)的精确积分为

$$
\left\{ \begin{array}{l} x _ {1} (t) = \int_ {0} ^ {t} x _ {2} (\tau) \mathrm{d} \tau \\ x _ {2} (t) = \int_ {0} ^ {t} f (\tau) \mathrm{d} \tau \end{array} \right.

\left\{ \begin{array}{l} x _ {1} (t) = \int_ {0} ^ {t} \int_ {0} ^ {\tau} f (s) \mathrm{d} s \mathrm{d} \tau = \int_ {0} ^ {t} (t - \tau) f (\tau) \mathrm{d} \tau \\ x _ {2} (t) = \int_ {0} ^ {t} f (\tau) \mathrm{d} \tau \end{array} \right.
$$

而欧拉近似积分公式为

$$
\begin{array}{l} \left\{ \begin{array}{l} x _ {1} ((i + 1) h) = x _ {1} (i h) + h x _ {2} (i h) \\ x _ {2} ((i + 1) h) = x _ {2} (i h) + h f (i h) \end{array} \right. \\ \left\{ \begin{array}{l} x _ {1} ((i + 1) h) = x _ {1} (i h) + h x _ {2} ((i - 1) h) + h ^ {2} f ((i - 1) h) \\ x _ {2} (i h) = x _ {2} ((i - 1) h) + h f ((i - 1) h) \end{array} \right. \\ \left\{ \begin{array}{l} x _ {1} (n h) = x _ {1 0} + h \sum_ {0} ^ {n - 1} x _ {2} (i h) + h ^ {2} \sum_ {0} ^ {n - 1} f (i h) \\ x _ {2} (n h) = x _ {2 0} + h \sum_ {0} ^ {n - 1} f (i h) \end{array} \right. \\ \end{array}
$$

由于从速度 $x_{2}$ 向前积分一步的过程中速度值的改变不会超出 $h\max |f(t)|$ ，那么在时间区间 $[0,T]$ 内的积分过程中速度分量 $x_{2}(t)$ 始终不会超出 $T\max |f(t)|$ ，从而步长 $h$ 要对某一常数 $K$ ，满足不等式

$$K \left(\frac {h}{2}\right) ^ {2} \max | f (x _ {1}, x _ {2}) | < eh < 2 \sqrt {\frac {e}{K}} \frac {1}{\sqrt {\max _ {(x _ {1} , x _ {2}) \in G} | f (x _ {1} , x _ {2}) |}}$$

这样，步长 $h$ 是与 $\left|f(x_1,x_2)\right|$ 的最大值的开放成反比，而且这个最大值也可以表示系统在区域 $G$ 范围内运行时动作的“快慢”程度.于是我们定义

$$\rho = \frac {1}{\sqrt {\max _ {(x _ {1} , x _ {2}) \in G} | f (x _ {1} , x _ {2}) |}} \tag {4.7.16}$$

为系统(4.7.9)在G范围内的“时间尺度”.这样,计算步长h应与系统的“时间尺度”成正比,即对某一常数k,有

$$h = k \rho \tag {4.7.17}$$

关于第三问题：“时间尺度” $\rho$ 和步长h的关系，关系式(4.7.14)，(4.7.17)给出了“正比”关系，但这里的比例系数应该取多少？而第四个问题： $\rho=1$ 时的扩张状态观测器参数 $\beta_{01},\beta_{02},\beta_{03}$ 又是什么？这些问题都是相互关联的.

如果记 $M = \max_{(x_1, x_2) \in G} |f(x_1, x_2)|$ ，那么根据式 (4.7.15)，(4.7.16)，有

$$k = h \sqrt {M} \tag {4.7.18}$$

这说明,对给定的步长 h, 只要确定了扩张状态观测器(4.7.4)能够跟踪的系统(4.7.11)的加速度范围 M, 就能确定出比例系数 k.

比例系数 k 和 $\rho = 1$ 时的参数 $\beta_{01}, \beta_{02}, \beta_{03}$ ，我们只能用数字仿真方法来确定.

扩张状态观测器的数值仿真研究表明,参数 $\beta_{01}$ 是与采样步长h成反比,而 $\beta_{02},\beta_{03}$ 分别与 $\frac{1}{h^{2}},\frac{1}{h^{3}}$ 成反比.大量数字仿真研究表明,步长 h 有一个阈值 $h_{0}$ ，使得当 $h > h_{0}$ 时， $\beta_{02}, \beta_{03}$ 都小于 $\beta_{01}$ ，当 $h < h_{0}$ 时， $\beta_{02}, \beta_{03}$ 却大于 $\beta_{01}$ ，而当 $h = h_{0}$ 时， $\beta_{02}, \beta_{03}$ 几乎与 $\beta_{01}$ 相当.
