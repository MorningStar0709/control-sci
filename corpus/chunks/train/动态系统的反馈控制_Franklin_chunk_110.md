# 例3.2 时不变性

考虑系统

$$\dot {y} _ {1} (t) + k (t) y _ {1} (t) = u _ {1} (t) \tag {3.2}$$

并且

$$\dot {y} _ {2} (t) + k (t) y _ {2} (t) = u _ {1} (t - \tau)$$

其中： $\tau$ 是常数。假设 $y_{2}(t) = y_{1}(t - \tau)$ 那么

$$\frac {\mathrm{d} y _ {1} (t - \tau)}{\mathrm{d} t} + k (t) y _ {1} (t - \tau) = u _ {1} (t - \tau)$$

作变量代换 $t - \tau = \eta$ ，那么

$$\frac {\mathrm{d} y _ {1} (\eta)}{\mathrm{d} \eta} + k (\eta + \tau) y _ {1} (\eta) = u _ {1} (\eta) \tag {3.3}$$

仅当 $\tau = 0$ 或者 $k(\eta +\tau) = k =$ 常数时，式(3.3)满足式(3.2)，在这种情况下，有

$$\frac {\mathrm{d} y _ {1} (\eta)}{\mathrm{d} \eta} + k y _ {1} (\eta) = u (\eta)$$

这就是例 3.1 中的第 1 个式子。所以，我们得到以下结论：如果系统是时不变的， $y(t-\tau)$ 将是输入为 $u(t-\tau)$ 时的系统响应；也就是说，如果输入延迟 $\tau$ ，那么输出也会延迟 $\tau$ 。

给定一个一般信号，只需通过叠加将给定的信号简单地分解为若干基本信号的和的形式，我们就能够求解线性系统的响应，总结得出：系统对一般信号的响应就是对基本信号响应的和。为了处理以上问题，基本信号需要有广泛的代表性，并且一定能很容易地得到它们的响应。用于线性系统的最常见的基本信号为脉冲信号和指数信号。

假设一个线性时不变系统的输入信号是一个短脉冲 $u_{1}(t) = p(t)$ ，并且相应的输出信号为 $y_{1}(t) = h(t)$ 。如图3.1a所示，如果这个输入按比例缩小到 $u_{1}(t) = u(0)p(t)$ ，那么依据叠加原理的扩展性质，输出响应将是 $y_{1}(t) = u(0)h(t)$ 。已证明：一个线性时不变系统遵循时不变特性。如果我们把这个小脉冲信号延迟时间 $\tau$ ，那么输入是 $u_{2}(t) = p(t - \tau)$ ，并且输出响应也将以同样的时刻延迟至 $y_{2}(t) = h(t - \tau)$ 。如图3.1b所示，在图3.1c中，依据叠加原理，两个短脉冲的响应可以表示成各自输出响应之和的形式。如果把4个脉冲信号作为输入，那么输出响应将是这4个单独响应之和，如图3.1d所示，对于任何输入信号 $u(t)$ 都可以被近似成若干脉冲信号的叠加，如图3.2所示，定义一个短脉冲 $p_{\Delta}(t)$ 作为一个具有单位面积的矩形脉冲如

$$
p _ {\Delta} (t) = \left\{ \begin{array}{l l} \frac {1}{\Delta}, & 0 \leqslant t \leqslant \Delta \\ 0, & \text {其他} \end{array} \right. \tag {3.4}
$$

输入信号  
![](image/d0d523ac927e5a97e95f84151dcf01b137f5447c613e7f37b23c9ae56548233e.jpg)

<details>
<summary>line</summary>

| t (s) | p(t) |
| --- | --- |
| 0 | 1/Δ |
| Δ | 1/Δ |
</details>

系统输出  
![](image/4400fc6483306ea163084aae7a81beaec52c8d8ee1132066b16d723bd6f6ede1.jpg)

<details>
<summary>line</summary>

| t/s | h(t) |
| --- | --- |
| 0 | 1 |
</details>

a)

![](image/686009e75a5565a33fb355f81fcad5d02903603c12bcba33d1be2ab49a3cffb0.jpg)

<details>
<summary>bar</summary>

| Time (s) | Probability p(t-τ) |
| --- | --- |
| 0 | 1/Δ |
| τ | 1/Δ |
| τ+Δ | 1/Δ |
</details>

![](image/bcddc8bff137c00b3a9e56a5086c9c72e0397b8819712f23342d8fb6a6286394.jpg)

<details>
<summary>line</summary>

| t/s | h(t-τ) |
| --- | --- |
| 0 | 0 |
| τ/4 | 1 |
| >τ/4 | Decreasing from peak to baseline |
</details>

b)

![](image/99205946a74a70dcb20e6b108227e1198000128a4353ac3bcdb1a71e00fda787.jpg)
