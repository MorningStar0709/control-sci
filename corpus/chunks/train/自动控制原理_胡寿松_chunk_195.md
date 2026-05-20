| Time/sec | Amplitude |
| --- | --- |
| 0.0 | 0.0 |
| 0.1 | 0.6 |
| 0.2 | 0.9 |
| 0.3 | 1.0 |
| 0.4 | 1.0 |
| 0.5 | 1.0 |
| 0.6 | 1.0 |
| 0.7 | 1.0 |
| 0.8 | 1.0 |
| 0.9 | 1.0 |
| 1.0 | 1.0 |
</details>

(a) 单位阶跃输入响应

![](image/8fc65fcd26a97c82282cc6b3f5f0f6d477921136895cb25b2558027661530b8d.jpg)

<details>
<summary>line</summary>

| Time/sec | Amplitude (×10⁻³) |
| --- | --- |
| 0.0 | 0.0 |
| 0.1 | -1.4 |
| 0.2 | -1.8 |
| 0.3 | -2.0 |
| 0.4 | -2.0 |
| 0.5 | -2.0 |
| 0.6 | -2.0 |
| 0.7 | -2.0 |
| 0.8 | -2.0 |
| 0.9 | -2.0 |
| 1.0 | -2.0 |
</details>

(b) 单位阶跃扰动响应  
图 3-52 带速度反馈的磁盘驱动器系统的响应 (MATLAB)

MATLAB 文本：

$$
\begin{array}{l} \mathrm{Ka} = 1 0 0; \mathrm{K} 1 = 0. 0 5; \\ \mathrm{G} 1 = \mathrm{tf} ([ 5 0 0 0 ], [ 1 1 0 0 0 ]); \quad \% \text {电机线圈模型} \\ \mathrm{G} 2 = \mathrm{zpk} ([ ], [ 0 - 2 0 ], 1); \quad \% \text {负载模型} \\ \mathrm{H} 1 = \operatorname{tf} ([ \mathrm{K} 1 1 ], [ 0 1 ]); \quad \% \text {速度位置反馈} \\ \end{array}
$$

```matlab
G=series(G1,G2);sys=feedback(Ka*G,H1); % 输入端闭环传递函数
Gn=series(Ka*G1,H1);sysn=-feedback(G2,Gn); % 扰动端闭环传递函数
t=0:0.01:1;
figure(1);step(sys,t);grid % 单位阶跃输入响应
figure(2);step(sysn,t);grid % 单位阶跃扰动响应
```

若取误差带 $\Delta=2\%$ , 所设计系统的性能指标如表 3-7 所示。

由表 3-7 可见, 以上设计近似满足性能指标要求。如果需要严格达到调节时间不大于 250ms 的指标要求, 则应重新考虑 $K_{1}$ 的取值。
