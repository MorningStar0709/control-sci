# 例 3.26 振荡的时间响应

讨论下式的极点与系统脉冲响应之间的相互关系，并且求出准确的脉冲响应。

$$H (s) = \frac {2 s + 1}{s ^ {2} + 2 s + 5} \tag {3.67}$$

![](image/80861732d8921bc3d3389a32fac2682ad8e8bd961ec9069538a373c6268d810f.jpg)

<details>
<summary>line</summary>

| 时间/s | e^(-σt) | e^(-σt) |
| --- | --- | --- |
| 0 | 1.0 | -1.0 |
| 5 | -0.4 | -0.2 |
| 10 | 0.2 | 0.0 |
| 15 | 0.0 | 0.0 |
| 20 | 0.0 | 0.0 |
| 25 | 0.0 | 0.0 |
| 30 | 0.0 | 0.0 |
</details>

图 3.21 带有指数包络线的二阶系统响应

解答。从式(3.63)给出的 $H(s)$ 的形式，我们可以看出，

$$\omega_ {\mathrm{n}} ^ {2} = 5 \Rightarrow \omega_ {\mathrm{n}} = \sqrt {5} \mathrm{rad/s} = 2. 2 4 \mathrm{rad/s}$$

并且

$$2 \zeta \omega_ {\mathrm{n}} = 2 \Rightarrow \zeta = \frac {1}{\sqrt {5}} = 0. 4 4 7$$

这表明我们期望的频率大约在 2rad/s 左右，有轻微的振荡现象，为获取准确的响应，我们将 $H(s)$ 的分母转换成式(3.62)的形式，结果为

$$H (s) = \frac {2 s + 1}{s ^ {2} + 2 s + 5} = \frac {2 s + 1}{(s + 1) ^ {2} + 2 ^ {2}}$$

从式中可以看出传递函数的极点是复数，实部为-1，虚部为±2j。表A.2中的第19条和第20条适用于这个分母。上述方程的右半部分需要拆分成两部分，以使他们分子与表中的条目相匹配：

$$
\begin{array}{l} H (s) = \frac {2 s + 1}{(s + 1) ^ {2} + 2 ^ {2}} \\ = 2 \frac {s + 1}{(s + 1) ^ {2} + 2 ^ {2}} - \frac {1}{2} \frac {2}{(s + 1) ^ {2} + 2 ^ {2}} \\ \end{array}
$$

因此，脉冲响应为

$$h (t) = (2 \mathrm{e} ^ {- t} \cos (2 t) - \frac {1}{2} \mathrm{e} ^ {- t} \sin (2 t)) 1 (t)$$

图 3.22 所示的是一个响应图，显示了包络线是如何削弱主导项 $2\cos(2t)$ 的正弦曲线的，以及由 $-\frac{1}{2}\sin(2t)$ 所引起的小相移。

如前面的例子，确定脉冲响应最方便的方法是使用 Matlab 指令。其 Matlab 语句如下。

$$
\begin{array}{l} \begin{array}{l} \text {s = tf('s')}; \\ \text {sysH = (2*s + 1) / (s^2 + 2*s + 5);} \end{array} \\ \begin{array}{l}\% \text{define Laplace variable}\\ \% \text{define system by its numerator}\\ \text{and denominator} \end{array} \\ \begin{array}{l} \text {t = 0:0.1:6;} \\ \text {y = impulse(sysH,t);} \end{array} \\ \begin{array}{l}\% \text{form time vector}\\ \% \text{compute impulse response} \end{array} \\ \operatorname{plot} (t, y); \\ \% \text { plot impulse response } \\ \end{array}
$$

如图 3.22 所示。

![](image/45f0cd20cb3fac9f9ae7308cbc9d84fa794049a790118068849120cb91d49a6e.jpg)

<details>
<summary>line</summary>

| 时间/s | h(t) (实线) | h(t) (虚线) |
| --- | --- | --- |
| 0 | 2.0 | -2.0 |
| 1 | 0.5 | -0.5 |
| 2 | 0.0 | 0.0 |
| 3 | 0.0 | 0.0 |
| 4 | 0.0 | 0.0 |
| 5 | 0.0 | 0.0 |
| 6 | 0.0 | 0.0 |
</details>

图3.22 例3.25的系统响应
