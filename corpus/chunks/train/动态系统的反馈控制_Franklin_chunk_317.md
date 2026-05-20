对控制系统工程师而言，理解伯德图技术很重要，有几个原因：这些知识使工程师不仅可以处理简单问题，而且可以在计算机结果上对更多复杂情况进行合理性检验。通常近似值能被用于快速描绘频率响应与推断稳定性，也可用于确定所需的动态补偿的形式。最后，对于绘图方法的理解可用于解释由实验方法获得的频率响应数据。

第 5 章中，我们写过开环传递函数的形式为

$$K G (s) = K \frac {(s - z _ {1}) (s - z _ {2}) \cdots}{(s - p _ {1}) (s - p _ {2}) \cdots} \tag {6.15}$$

因为它曾是由关于增益 K 的根轨迹来确定稳定程度的最方便的形式。在讨论频率响应时，我们仅对于沿 $j\omega$ 轴计算 $G(s)$ 感兴趣，所以为了更加方便起见，以 $j\omega$ 代替 s，且将传递函数写成伯德形式，即

$$K G (\mathrm{j} \omega) = K _ {\circ} (\mathrm{j} \omega) ^ {n} \frac {(\mathrm{j} \omega \tau_ {1} + 1) (\mathrm{j} \omega \tau_ {2} + 1) \cdots}{(\mathrm{j} \omega \tau_ {\mathrm{a}} + 1) (\mathrm{j} \omega \tau_ {\mathrm{b}} + 1) \cdots} \tag {6.16}$$

这种形式导致增益 $K_{0}$ 与在很低频率处的传递函数的幅值直接相关。事实上，对于 n=0 的系统， $K_{0}$ 就是式(6.16)中在 $\omega=0$ 处的增益，也等于系统的直流增益。尽管直接的计算将会把式(6.15)形式的传递函数转化为一个等价的式(6.16)形式的传递函数，但请注意，在这两个表达式中 K 和 $K_{0}$ 通常并不会取到相同的值。

传递函数还可以根据式(6.10)和式(6.11)写出。例如，令

$$K G (\mathrm{j} \omega) = K _ {\circ} \frac {\mathrm{j} \omega \tau_ {1} + 1}{(\mathrm{j} \omega) ^ {2} (\mathrm{j} \omega \tau_ {\mathrm{a}} + 1)}. \tag {6.17}$$

那么

$$\angle K G (\mathrm{j} \omega) = \angle K _ {\mathrm{o}} + \angle (\mathrm{j} \omega \tau_ {1} + 1) - \angle (\mathrm{j} \omega) ^ {2} - \angle (\mathrm{j} \omega \tau_ {\mathrm{a}} + 1) \tag {6.18}$$

且

$$
\begin{array}{l} \lg | K G (\mathrm{j} \omega) | = \lg | K _ {\mathrm{o}} | + \lg | \mathrm{j} \omega \tau_ {1} + 1 | - \lg | (\mathrm{j} \omega) ^ {2} | \\ - \lg | j \omega \tau_ {\mathrm{a}} + 1 | \tag {6.19} \\ \end{array}
$$

在分贝单位下，式(6.19)变成

$$
\begin{array}{l} \left| K G (\mathrm{j} \omega) \right| _ {\mathrm{dB}} = 2 0 \lg \left| K _ {\mathrm{o}} \right| + 2 0 \lg \left| \mathrm{j} \omega \tau_ {1} + 1 \right| - 2 0 \lg \left| (\mathrm{j} \omega) ^ {2} \right| \\ - 2 0 \lg | j \omega \tau_ {a} + 1 | \tag {6.20} \\ \end{array}
$$

目前为止，我们所讨论过的各种系统的所有传递函数都可由下面三类的项组合而成：

(1) $K_{0}(j\omega)^{n}$ ;   
(2) $(j\omega\tau+1)^{\pm1}$ ;   
(3) $\left[\left(\frac{\mathrm{j}\omega}{\omega_{\mathrm{n}}}\right)^{2}+2\zeta\frac{\mathrm{j}\omega}{\omega_{\mathrm{n}}}+1\right]^{\pm1}$

首先我们将讨论每个单独项的绘图以及这些项对于包含所有上述项的复合图的影响；然后我们将介绍如何绘制复合曲线。

(1) 对于 $K_{0}(j\omega)^{n}$ ，因为

$$\lg K _ {o} \mid (\mathrm{j} \omega) ^ {n} \mid = \lg K _ {o} + n \lg | \mathrm{j} \omega |$$
