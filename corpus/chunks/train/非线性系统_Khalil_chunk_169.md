# 5.3 $\mathcal{L}_2$ 增益

$\mathcal{L}_2$ 稳定性在系统分析中起着特殊的作用。很自然我们选择的信号是平方可积信号，它是一种有限能量信号①。在许多控制问题中②，把系统表示为一种输入-输出映射，即从一个干扰输入 $u$ 到受控输出 $y$ 的映射，要求 $y$ 足够小。对于 $\mathcal{L}_2$ 输入信号，控制系统要设计为使输入-输出映射为有限增益 $\mathcal{L}_2$ 稳定的，并使 $\mathcal{L}_2$ 增益最小。在这类问题中，重要的是不仅能求出系统为有限增益 $\mathcal{L}_2$ 稳定的，而且要计算 $\mathcal{L}_2$ 增益或其上界。在本节中，我们将说明如何计算一类特殊时不变系统的 $\mathcal{L}_2$ 增益。下面先从线性系统开始分析。

定理 5.4 考虑线性时不变系统

$$\dot {x} = A x + B u \tag {5.24}y = C x + D u \tag {5.25}$$

其中 $A$ 为赫尔维茨矩阵。设 $G(s) = C(sI - A)^{-1}B + D$ ，则系统的 $\mathcal{L}_2$ 增益为 $\sup_{\omega \in R}\| G(j\omega)\| _2^{③}$ 。

证明:由于是线性系统,故设定 $x(0)=0$ 。由傅里叶变换理论可知①,对于因果信号 $y\in L_{2}$ ,傅里叶变换 $Y(j\omega)$ 为

$$Y (j \omega) = \int_ {0} ^ {\infty} y (t) e ^ {- j \omega t} d t$$

且

$$Y (j \omega) = G (j \omega) U (j \omega)$$

由帕塞瓦尔定理 $^{②}$ 可写出：

$$
\begin{array}{l} \| y \| _ {\mathcal {L} _ {2}} ^ {2} = \int_ {0} ^ {\infty} y ^ {T} (t) y (t) d t = \frac {1}{2 \pi} \int_ {- \infty} ^ {\infty} Y ^ {*} (j \omega) Y (j \omega) d \omega \\ = \frac {1}{2 \pi} \int_ {- \infty} ^ {\infty} U ^ {*} (j \omega) G ^ {T} (- j \omega) G (j \omega) U (j \omega) d \omega \\ \leqslant \left(\sup _ {\omega \in R} \| G (j \omega) \| _ {2}\right) ^ {2} \frac {1}{2 \pi} \int_ {- \infty} ^ {\infty} U ^ {*} (j \omega) U (j \omega) d \omega \\ = \left(\sup _ {\omega \in R} \| G (j \omega) \| _ {2}\right) ^ {2} \| u \| _ {\mathcal {L} _ {2}} ^ {2} \\ \end{array}
$$

这说明, $L_{2}$ 增益小于或等于 $\sup_{\omega\in R}\|G(j\omega)\|_{2}$ 。附录C.10用反证法证明了 $L_{2}$ 增益等于 $\sup_{\omega\in R}\|G(j\omega)\|_{2}$ 。

因为线性时不变系统是个特例,所以可以得到确定的 $L_{2}$ 增益。对于一般情况,例如下面的定理,只能得到 $L_{2}$ 增益的上界。

定理5.5 考虑非线性时不变系统

$$\dot {x} = f (x) + G (x) u, \quad x (0) = x _ {0} \tag {5.26}y = h (x) \tag {5.27}$$

其中 $f(x)$ 和 $G(x)$ 是局部利普希茨的， $h(x)$ 在 $R^n$ 上连续。 $G$ 为 $n \times m$ 矩阵， $h: R^n \to R^q$ 。函数 $f$ 和 $h$ 在原点为零，即 $f(0) = 0, h(0) = 0$ 。设 $\gamma$ 为正数，并假设对于所有 $x \in R^n$ ，存在一个连续可微的半正定函数 $V(x)$ ，满足不等式

$$\mathcal {H} (V, f, G, h, \gamma) \stackrel {\text {def}} {=} \frac {\partial V}{\partial x} f (x) + \frac {1}{2 \gamma^ {2}} \frac {\partial V}{\partial x} G (x) G ^ {\mathrm{T}} (x) \left(\frac {\partial V}{\partial x}\right) ^ {\mathrm{T}} + \frac {1}{2} h ^ {T} (x) h (x) \leqslant 0 \tag {5.28}$$

则对于每个 $x_0 \in R^n$ ，系统(5.26)～(5.27)为有限增益 $\mathcal{L}_2$ 稳定的，且其 $\mathcal{L}_2$ 增益小于或等于 $\gamma$ 。

证明:通过配平方,有
