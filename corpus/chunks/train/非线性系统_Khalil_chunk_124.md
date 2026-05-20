# 4.5 非自治系统

考虑非自治系统

$$\dot {x} = f (t, x) \tag {4.15}$$

其中 $f: [0, \infty) \times D \to R^n$ 在 $[0, \infty) \times D$ 上是 $t$ 的分段连续函数，且对于 $x$ 是局部利普希茨的， $D \subset R^n$ 是包含原点的定义域。如果

$$f (t, 0) = 0, \forall t \geqslant 0$$

则原点是 t=0 时方程(4.15)的平衡点。原点的平衡点可能是某个非零平衡点的平移,或者说是系统某个非零解的平移。为理解后者,假设 $\bar{y}(\tau)$ 是系统

$$\frac {d y}{d \tau} = g (\tau , y)$$

的一个解,系统在所有 $\tau\geqslant a$ 上都有定义。通过变量代换,

$$x = y - \bar {y} (\tau); t = \tau - a$$

系统转换为 $\dot{x} = g(\tau, y) - \dot{\bar{y}}(\tau) = g(t + a, x + \bar{y}(t + a)) - \dot{\bar{y}}(t + a) \stackrel{\mathrm{def}}{=} f(t, x)$

由于 $\dot{\bar{y}} (t + a) = g(t + a,\bar{y} (t + a)),\forall t\geqslant 0$

所以原点 $x = 0$ 是转换后的系统在 $t = 0$ 时的一个平衡点。因此，通过检验转换后系统的平衡点，即原点的稳定性性质，可确定原系统的解 $\bar{y} (\tau)$ 的稳定性性质。注意，如果 $\bar{y} (\tau)$ 不是常数，即使原系统是自治系统，即 $g(\tau ,y) = g(y)$ ，转换后的系统也为非自治系统。这就是为什么只有在研究非自治系统平衡点的稳定性性质中，要用李雅普诺夫法研究解的稳定性性质。

非自治系统平衡点的稳定性和渐近稳定性的概念与定义4.1引入的自治系统的概念基本一样。不同的是自治系统的解仅与 $(t - t_0)$ 有关，而非自治系统的解不仅取决于 $t$ ，也与 $t_0$ 有关。因此，一般来说，平衡点的稳定性都取决于 $t_0$ 。如果对于每个 $\varepsilon >0$ ，且对于任意 $t_0\geqslant 0$ ，存在 $\delta = \delta (\varepsilon ,t_0) > 0$ ，使

$$\| x (t _ {0}) \| < \delta \Rightarrow \| x (t) \| < \varepsilon , \forall t \geqslant t _ {0}$$

原点就是方程(4.15)的稳定平衡点。常数 $\delta$ 一般取决于初始时刻 $t_0$ 。对于每个 $t_0$ 存在常数 $\delta$ ，不一定能保证一个常数 $\delta$ 在任意时刻 $t_0$ 都仅取决于 $\varepsilon$ ，如下例所示。

例4.17 一阶线性系统

$$\dot {x} = (6 t \sin t - 2 t) x$$

的解为

$$
\begin{array}{l} x (t) = x \left(t _ {0}\right) \exp \left[ \int_ {t _ {0}} ^ {t} (6 \tau \sin \tau - 2 \tau) d \tau \right] \\ = x \left(t _ {0}\right) \exp \left[ 6 \sin t - 6 t \cos t - t ^ {2} - 6 \sin t _ {0} + 6 t _ {0} \cos t _ {0} + t _ {0} ^ {2} \right] \\ \end{array}
$$

上式中,对于任意 $t_{0},-t^{2}$ 项将起决定作用,即 $t\geqslant t_{0}$ 时指数项有界,是由 $t_{0}$ 决定的常数 $c(t_{0})$ 。因此 $|x(t)|<|x(t_{0})|c(t_{0}),\forall t\geqslant t_{0}$

对于任意 $\varepsilon > 0$ ，选择 $\delta = \varepsilon / c(t_{0})$ ，则原点是稳定的。现在，假设 $t_{0}$ 取系列值 $t_{0} = 2n\pi, n = 0, 1, 2, \cdots$ ，且 $x(t)$ 在每 $\pi$ 秒后取值，则

$$x (t _ {0} + \pi) = x (t _ {0}) \exp [ (4 n + 1) (6 - \pi) \pi ]$$

上式表示对 $x(t_0)\neq 0$ ，有

$$\frac {x (t _ {0} + \pi)}{x (t _ {0})} \to \infty , \text {当} n \to \infty$$

因此，给定 $\varepsilon > 0$ ，不存在独立于 $t_0$ 的 $\delta$ ，满足稳定性对 $t_0$ 一致的要求。

![](image/235d3b3947ef3c5b0b2f0024b4cce0cba82d5bfeac1a58dbf0c52d844d7d0dd7.jpg)

对 $t_0$ 的不一致性也出现在研究原点的渐近稳定性中，如下例所示。

例4.18 一阶线性系统

$$\dot {x} = - \frac {x}{1 + t}$$

的解为
