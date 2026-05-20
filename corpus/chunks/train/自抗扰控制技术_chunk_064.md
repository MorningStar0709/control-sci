$$\lim _ {r \rightarrow \infty} \int_ {0} ^ {T} | z _ {1} (r, t) - z _ {1} ^ {\prime} (r, t) | \mathrm{d} t = 0$$

下面看看几个例子.

例1 最速系统(2.3.8)和形如

$$
\left\{ \begin{array}{l} \dot {x} _ {1} = x _ {2} \\ \dot {x} _ {2} = - \operatorname{sign} (x _ {1}) | x _ {1} | ^ {\alpha} - x _ {2} \end{array} , 0 <   \alpha <   1 \right. \tag {2.3.23}
$$

的系统,都满足定理2的条件. 在前面已看到,最速系统(2.3.7)派生的系统(2.3.8)是一个很好的跟踪微分器. 同样,我们将看到,由系统(2.3.23)派生的系统

$$
\left\{ \begin{array}{l} \dot {x} _ {1} = x _ {2} \\ \dot {x} _ {2} = - r ^ {2} \operatorname{sign} (x _ {1} - v (t)) | x _ {1} - v (t) | ^ {\alpha} - r x _ {2} \end{array} \right. \tag {2.3.24}
$$

也是一个不错的跟踪微分器．把这个系统离散化成

$$
\left\{ \begin{array}{l} x _ {1} (k + 1) = x _ {1} (k) + h x _ {2} (k) \\ x _ {2} (k + 1) = x _ {2} (k) - h \left(r ^ {2} \operatorname{sign} \left(x _ {1} (k) - v (k)\right) \mid x _ {1} (k) - v (k) \mid^ {\alpha} + r x _ {2} (k)\right) \end{array} \right. \tag {2.3.26}
$$

输入被噪声污染的正弦信号: $v(t)=\sin(t)+\gamma n(t)$ ，并取步长为h=0.001，噪声强度 $\gamma$ 分别取 $\gamma=0.0,\gamma=0.1$ 时的仿真结果示于图2.3.6.从仿真结果看，无论是跟踪性能还是微分的滤波性能都是不错的.

积分步长的不同取法对滤波效果会有很大差异. h 分别取 h = 0.001, h = 0.0001 时的仿真结果分别示于图 2.3.7. 实际上，在这里滤波效果是与采样步长 h 的开放成正比的.

![](image/afb53e5d1e68c21b4da7423cd90de04acfe472e6948f87938173f94eb4a57337.jpg)  
图 2.3.6

![](image/f04348ad5ac29c4bcdf973813f5a5db887870f45dddb04dfa9d7c88fe2596233.jpg)

<details>
<summary>line</summary>

| x | v(t) | μ(t) |
| --- | --- | --- |
| 0 | 1.0 | 0.0 |
| 5 | -1.0 | 0.0 |
| 10 | 1.0 | 0.0 |
| 15 | -1.0 | 0.0 |
| 20 | 1.0 | 0.0 |
| 25 | -1.0 | 0.0 |
| 30 | 1.0 | 0.0 |
| 35 | -1.0 | 0.0 |
| 40 | 1.0 | 0.0 |
| 45 | -1.0 | 0.0 |
| 50 | 1.0 | 0.0 |
| 55 | -1.0 | 0.0 |
| 60 | 1.0 | 0.0 |
| 65 | -1.0 | 0.0 |
| 70 | 1.0 | 0.0 |
| 75 | -1.0 | 0.0 |
| 80 | 1.0 | 0.0 |
| 85 | -1.0 | 0.0 |
| 90 | 1.0 | 0.0 |
| 95 | -1.0 | 0.0 |
| 100 | 1.0 | 0.0 |
| 105 | -1.0 | 0.0 |
| 110 | 1.0 | 0.0 |
| 115 | -1.0 | 0.0 |
| 120 | 1.0 | 0.0 |
| 125 | -1.0 | 0.0 |
| 130 | 1.0 | 0.0 |
| 135 | -1.0 | 0.0 |
| 140 | 1.0 | 0.0 |
| 145 | -1.0 | 0.0 |
| 150 | 1.0 | 0.0 |
| 155 | -1.0 | 0.0 |
| 160 | 1.0 | 0.0 |
| 165 | -1.0 | 0.0 |
| 170 | 1.0 | 0.0 |
| 175 | -1.0 | 0.0 |
| 180 | 1.0 | 0.0 |
| 185 | -1.0 | 0.0 |
| 190 | 1.0 | 0.0 |
| 195 | -1.0 | 0.0 |
| 200 | 1.0 | 0.0 |
The chart displays two line plots: left plot (v(t)) and right plot (μ(t)). The x-axis ranges from approximately -2 to +2, and the y-axis ranges from -2 to +2 for both plots. The left plot is labeled 'h=0.0' and the right plot is labeled 'α=-α=5, γ=1, γ=2'. The left plot shows a sinusoidal waveform with amplitude ~2π/2, while the right plot shows a sine wave with amplitude ~2π/2 and frequency ~3π/2.
</details>

图 2.3.7
