根据图 5-54, 可以认为系统的主导极点为共轭复极点。于是, 由图 5-55 给出的关系曲线, 并由 $M_{r}=1.78$ 估计出系统的阻尼比 $\zeta=0.28$ , 然后进一步得到标准化谐振频率 $\omega_{r}/\omega_{n}=0.92$ 。

因为已求出 $\omega_{r}=0.8$ ，故无阻尼自然频率

$$\omega_ {n} = \frac {0 . 8}{0 . 9 2} = 0. 8 7$$

于是，雕刻机控制系统的二阶近似模型应为

$$\Phi (s) = \frac {\omega_ {n} ^ {2}}{s ^ {2} + 2 \zeta \omega_ {n} s + \omega_ {n} ^ {2}} = \frac {0 . 7 6}{s ^ {2} + 0 . 4 9 s + 0 . 7 6}$$

![](image/630acff22be508f845bc85b4ebfd1ffc1d23cabfce947ecad2433fb933b8f32f.jpg)

<details>
<summary>line</summary>

| ζ | Mr | ωr/ωn |
| --- | --- | --- |
| 0.20 | 3.25 | 0.90 |
| 0.30 | 3.00 | 0.80 |
| 0.40 | 2.75 | 0.70 |
| 0.50 | 2.50 | 0.60 |
| 0.60 | 2.25 | 0.50 |
| 0.70 | 2.00 | 0.40 |
| 0.70 | 1.75 | 0.30 |
| 0.70 | 1.50 | 0.20 |
| 0.70 | 1.25 | 0.10 |
</details>

图 5-55 在共轭复极点项的频率响应中，谐振峰值 $M_{r}$ 、谐振频率 $\omega_{r}$ 与阻尼比 $\zeta$ 的关系曲线

根据近似模型,可以估算出系统的超调量为

$$\sigma \% = \mathrm{e} ^ {- \pi \zeta / \sqrt {1 - \zeta^ {2}}} \times 100 \% = 40 \%$$

调节时间( $\Delta=2\%$ )为

$$t _ {s} = \frac {4 . 4}{\zeta \omega_ {n}} = 1 7. 9 6 \mathrm{s}$$

最后，按实际三阶系统进行仿真，其单位阶跃响应如图5-56所示，得到 $\sigma \% = 39\% ,t_p = 4s,$ $t_s = 16s$ 。结果表明，二阶近似模型是合理的，可以用来调节系统的参数。在本例中，如果要求更小的超调量，应取 $K_{1} < 2$ ，然后重复以上设计过程。

![](image/990fdfcc00af024c6ca801c99392603dda3dfa8889d8de6d2cfd40e46445d623.jpg)

<details>
<summary>line</summary>

| Time/sec | Amplitude |
| --- | --- |
| 0 | 0.0 |
| 5 | 1.4 |
| 10 | 1.0 |
| 15 | 0.98 |
| 20 | 1.0 |
| 25 | 1.0 |
</details>

图 5-56 雕刻机控制系统的阶跃响应(MATLAB)

MATLAB 文本：

$$\mathrm{K1} = 2; \mathrm{G0} = \mathrm{zkp} ([ ], [ 0 - 1 - 2 ], \mathrm{K1}); \quad \% \text {系统开环传递函数}\mathrm{G} = \text {feedback(G0,1)} \quad \% \text {系统的闭环传递函数}$$

<table><tr><td>figure(1);bode(G0);grid</td><td>%绘制系统的开环频率特性曲线</td></tr><tr><td>figure(2);bode(G);grid</td><td>%绘制系统的闭环频率特性曲线</td></tr><tr><td>figure(3);step(G);grid</td><td>%系统的单位阶跃响应</td></tr></table>
