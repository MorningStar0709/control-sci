$$
\begin{array}{l} \sigma \% = 100 \left[ 0.16 + 0.4 \left(\frac{1}{\sin\gamma} - 1\right) \right] \% = 42.1\% \\ K _ {0} = 2 + 1. 5 \left(\frac {1}{\sin \gamma} - 1\right) + 2. 5 \left(\frac {1}{\sin \gamma} - 1\right) ^ {2} = 4. 0 4 \\ \end{array}
t _ {s} = \frac {K _ {0} \pi}{\omega_ {c}} = 1 0. 1 \mathrm{ms} (\Delta = 5 \%)
$$

上述估算公式是偏保守的，仅能用于系统的初步设计。实际上，图5-57所示磁头位置控制系统的单位阶跃响应曲线如图5-61所示。由图可得系统的动态性能

$$\sigma \% \approx 31\% , \quad t _ {s} = 9.2 \mathrm{ms} (\Delta = 2 \%)$$

![](image/de61ff848095a55e1f240551b36f40b8249ef2d2fed79077fa59bfb239e6a36b.jpg)

<details>
<summary>line</summary>

| Time/sec | Amplitude |
| --- | --- |
| 0.000 | 0.0 |
| 0.002 | 1.3 |
| 0.004 | 0.9 |
| 0.006 | 1.0 |
| 0.008 | 1.0 |
| 0.010 | 1.0 |
| 0.012 | 1.0 |
| 0.014 | 1.0 |
| 0.016 | 1.0 |
| 0.018 | 1.0 |
| 0.020 | 1.0 |
</details>

图 5-61 磁头位置控制系统的单位阶跃响应(MATLAB)

MATLAB 文本：

$$
\begin{array}{l} \text { num } = 2 0 0 0 * 0. 0 5 * [ 1, 1 ]; \\ \text { den } = [ \text { conv } (\text { conv } ([ 0. 0 0 1, 1 ], [ 1 / 2 0, 1 ]), \text { conv } ([ 1, 0 ], [ (1 / 1 8 8 5 0) ^ {- 2}, 2 * 0. 3 / 1 8 8 5 0, 1 ])) ]; \end{array}
\mathrm{G0} = \mathrm{tf(num,den)}; \mathrm{G} = \text {feedback(G0,1) ;} \quad \% \text {系统的开环和闭环传递函数}\mathrm{t} = 0: 0. 0 0 0 1: 0. 0 2;\text {figure(1);bode(G0);grid}\text {figure(2);bode(G);grid}\text {figure(3);step(G,t);grid} \% \text {系统的单位阶跃响应}
$$
