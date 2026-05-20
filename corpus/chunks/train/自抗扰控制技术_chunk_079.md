# 2.6.5 频率估计

我们测得了被噪声污染的正弦信号 $x(t) = a \sin(\omega t) + \gamma n(t)$ ，如何估计出此信号所含的频率 $\omega$ ，是下面要讨论的问题。

先看无噪声的情形．取 $x(t)$ 的微分，得

$$\dot {x} (t) = a \omega \cos (\omega t) \tag {2.6.17}$$

于是可得

$$\frac {\int_ {0} ^ {t} (\dot {x} (\tau)) ^ {2} \mathrm{d} \tau}{\int_ {0} ^ {t} (x (\tau)) ^ {2} \mathrm{d} \tau} = \frac {a ^ {2} \omega^ {2} \int_ {0} ^ {t} \cos^ {2} (\omega \tau) \mathrm{d} \tau}{a ^ {2} \int_ {0} ^ {t} \sin^ {2} (\omega \tau) \mathrm{d} \tau} = \omega^ {2} \frac {\int_ {0} ^ {t} \cos^ {2} (\omega \tau) \mathrm{d} \tau}{\int_ {0} ^ {t} \sin^ {2} (\omega \tau) \mathrm{d} \tau} \tag {2.6.18}$$

但是由于

$$\lim _ {t \rightarrow \infty} \int_ {0} ^ {t} \cos^ {2} (\omega \tau) d \tau / \int_ {0} ^ {t} \sin^ {2} (\omega \tau) d \tau = 1$$

因此就有

$$\omega^ {2} \approx \lim _ {t \rightarrow \infty} \int_ {0} ^ {t} (\dot {x} (\tau)) ^ {2} \mathrm{d} \tau / \int_ {0} ^ {t} (x (\tau)) ^ {2} \mathrm{d} \tau \tag {2.6.19}$$

这个公式对被噪声污染的信号也是有效的．这里的信号微分是用TD来获取.

例 设输入信号为 $y = a \sin (\omega t) + \gamma n(t)$ ，取 $a = 1, \gamma = 0.1$ ， $n(t)$ 为 $[-1, 1]$ 之间均匀分布的随机噪声。取步长 $h = 0.0001$ ，TD 的速度因子 $r = 2000$ ，滤波因子 $h_0 = 100h$ ，TD 的初值： $x_1(0) = 0.1, x_2(0) = 0.0$ 所做的仿真结果示于图 2.6.9。从仿真看出对频率 $\omega$ 的估计都是很好的。

![](image/9ff9b5a7ae8a08878807a81f41b33ffb2f9010b4b53e584129142fc43f594ef5.jpg)

<details>
<summary>line</summary>

| x | y = sin(α) + n(t) (α=20) | y = sin(α) + n(t) (α=40) | y = sin(α) + n(t) (α=60) |
| --- | --- | --- | --- |
| 0 | 90 | 90 | 90 |
| 10 | 85 | 85 | 85 |
| 20 | 80 | 80 | 80 |
| 30 | 75 | 75 | 75 |
| 40 | 70 | 70 | 70 |
| 50 | 65 | 65 | 65 |
| 60 | 60 | 60 | 60 |
| 70 | 55 | 55 | 55 |
| 80 | 50 | 50 | 50 |
| 90 | 45 | 45 | 45 |
| 100 | 40 | 40 | 40 |
| 110 | 35 | 35 | 35 |
| 120 | 30 | 30 | 30 |
| 130 | 25 | 25 | 25 |
| 140 | 20 | 20 | 20 |
| 150 | 15 | 15 | 15 |
| 160 | 10 | 10 | 10 |
| 170 | 5 | 5 | 5 |
| 180 | 0 | 0 | 0 |
The chart displays a step function of the sine function y = sin(α) + n(t). The x-axis ranges from 'h=0.001' to 'h=0.01', and the y-axis ranges from 'a' to 'b'. The data is presented in a grid format with three distinct step functions labeled by 'α'.
</details>

图2.6.9
