# 13.1.3 输入成型器基本原理

在输入成型技术中，输入信号被一系列脉冲调制，其目标是通过调制脉冲幅度和时间来消除振动。输入成型是一种非常实用的消除余振的方法。输入成型在挠性振动的控制中取得很好的效果。采用输入成型和滑模变结构控制相结合，可以有效地抑制挠性系统的挠性振动。

输入成型是指由脉冲系列（称为输入成型器，Input Shaper）与一定的期望输入指令相卷积，所形成的新指令作为系统的输入指令。其中，脉冲系列根据振动的频率和阻尼得到，用于抑制振动，脉冲系列中各脉冲的幅值和作用时间通过求解一定的约束方程组得到,约束方程包括对残余振动幅值的约束、对鲁棒性的约束、对成型器时间长度的约束等。

输入成型器的基本约束：所有脉冲的幅度大小之和等于1，且每一个脉冲都是正脉冲，即

$$\sum_ {i = 1} ^ {m} A _ {i} = 1, A _ {i} > 0 \tag {13.6}$$

如果所有的脉冲幅度之和等于 1，则经过成型后的输入信号的最后输出和没经过成型的输入信号的最后输出完全一样，即该约束使加入输入成型器后不改变系统的最后输出。

对于给定的振动系统，其受m个脉冲力作用的余振方程可表示为

$$V (\omega , \zeta) = \mathrm{e} ^ {- \xi \omega T _ {m}} \left[ \left(\sum_ {i = 1} ^ {m} A _ {i} \mathrm{e} ^ {\xi \omega T _ {i}} \cos \left(\omega_ {\mathrm{d}} T _ {i}\right)\right) ^ {2} + \left(\sum_ {i = 1} ^ {m} A _ {i} \mathrm{e} ^ {\xi \omega T _ {i}} \sin \left(\omega_ {\mathrm{d}} T _ {i}\right)\right) ^ {2} \right] ^ {1 / 2} \tag {13.7}$$

式中， $A_{i}$ 和 $T_{i}$ 分别为第 i 个脉冲力的幅值和作用时间，为使系统的响应时间尽可能的短，一般取 $T_{1}=0$ （即第一个脉冲时间为 0 时刻）； $T_{m}$ 为最后一个脉冲的作用时间，也是成型器的总长度。

采用输入成型算法设计跟踪期望信号 $r(t)$ ，设计具有单模态 2 阶鲁棒性的 4 脉冲零振动零微分 ZVDD 输入成型器。

具有 m=4 脉冲的 ZVDD 成型器，约束条件如下：

$$
\left\{ \begin{array}{l} V (\omega , \zeta) = 0 \\ \frac {\partial V (\omega , \zeta)}{\partial \omega} = 0 \\ \frac {\partial^ {2} V (\omega , \zeta)}{\partial \omega^ {2}} = 0 \\ T _ {1} = 0 \end{array} \right. \tag {13.8}
$$

式（13.8）中前三个式子每个可构成两个子方程，则由式（13.6）和式（13.8）可得8个方程构成的方程组。以 $V(\omega,\zeta)=0$ 为例，可得如下两个方程：

$$
\left\{ \begin{array}{l} \sum_ {i = 1} ^ {m} A _ {i} \mathrm{e} ^ {\xi \omega T _ {i}} \cos (\omega_ {d} T _ {i}) = 0 \\ \sum_ {i = 1} ^ {m} A _ {i} \mathrm{e} ^ {\xi \omega T _ {i}} \sin (\omega_ {d} T _ {i}) = 0 \end{array} \right.
$$

解 8 个方程构成的方程组得幅值和作用时间为

$$
\left\{ \begin{array}{l} A _ {i} = \frac {\binom {i - 1} {3} \bar {K} ^ {i - 1}}{\sum_ {i = 1} ^ {4} \binom {i - 1} {3} \bar {K} ^ {i - 1}} \\ T _ {i} = \frac {(i - 1) \pi}{\omega \sqrt {1 - \zeta^ {2}}} \end{array} \right. \tag {13.9}
$$

式中， $i = 1,2,3,4$ ； $\overline{K} = \mathrm{e}^{-(\zeta \pi /\sqrt{1 - \zeta^2})}$ ； $\zeta$ 振动模态的阻尼系数； $\omega$ 为振动模态的振动频率； $\binom{n}{m} = \frac{m!}{n!(m - n)!}$ ，即 $\binom{i - 1}{3} = \frac{3!}{(i - 1)!(4 - i)!}$ 。

最后可得脉冲序列为

$$A _ {\mathrm{mult}} = A _ {1} \delta (t - T _ {1}) + A _ {2} \delta (t - T _ {2}) + A _ {3} \delta (t - T _ {3}) + A _ {4} \delta (t - T _ {4}) \tag {13.10}$$

式中， $\delta$ 为脉冲信号。

输入成型器成型输出 $u_{r}$ 为

$$u _ {\mathrm{r}} = r (t) * A _ {\mathrm{mult}} \tag {13.11}$$

式中， $r(t)$ 为期望信号。

![](image/0983b6b1aff5566d289e6d67c26dc09b21364f285f55df4068fc287963846712.jpg)
