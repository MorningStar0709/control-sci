$$t _ {r} = \frac {0 . 7 5}{\omega_ {n}} = 0. 0 7 \mathrm{s} \quad (z / \zeta_ {d} \omega_ {n} = 1, \quad \omega_ {n} t _ {r} = 0. 7 5)t _ {p} = \frac {\beta_ {d} - \Psi}{\omega_ {n} \sqrt {1 - \zeta_ {d} ^ {2}}} = 0. \dot {2} \mathrm{s}\sigma \% = r \sqrt {1 - \zeta_ {d} ^ {2}} \mathrm{e} ^ {- \zeta_ {d} \omega_ {n} t _ {p}} \times 100 \% = 20.0 \%t _ {s} = \frac {4 + \ln r}{\zeta_ {d} \omega_ {n}} = 0.54 \mathrm{s} \quad (\Delta = 2 \%)$$

显然，由于新增零点的影响，超调量无法满足设计指标要求。

考虑采用前置滤波器 $G_{p}(s)$ 来对消闭环传递函数 $\Phi (s)$ 中的零点，并同时保持系统原有的直流增益即 $\Phi (0)$ 不变，为此取

$$G _ {p} (s) = \frac {8}{s + 8}$$

因而闭环传递函数变成

$$\Phi (s) = \frac {1 2 8}{s ^ {2} + 1 6 s + 1 2 8}$$

此时，系统属无零点的二阶系统。由于

$$\beta = \arccos \zeta = \frac {\pi}{4}, \quad \omega_ {d} = \omega_ {n} \sqrt {1 - \zeta^ {2}} = 8$$

根据式(3-19)、式(3-20)、式(3-21)，可以算出系统的动态性能指标为

$$t _ {r} = \frac {\pi - \beta}{\omega_ {d}} = 0. 2 9 \mathrm{s}t _ {p} = \frac {\pi}{\omega_ {d}} = 0. 3 9 \mathrm{s}\sigma \% = 100 \mathrm{e} ^ {- \pi \zeta \sqrt {1 - \zeta^ {2}}} \% = 4.3\%t _ {s} = \frac {4 . 4}{\zeta \omega_ {n}} = 0. 5 5 \mathrm{s} (\Delta = 2 \%)$$

结果表明:系统设计指标要求全部满足。

MATLAB 验证：

无前置滤波器时， $\Phi(s) = \frac{16(s + 8)}{s^2 + 16s + 128}$ ，单位阶跃响应如图6-25所示，测得

$$\sigma \% = 21 \%, \quad t _ {p} = 0.2 \mathrm{s}, \quad t _ {s} = 0.44 \mathrm{s} \quad (\Delta = 2 \%)$$

有前置滤波器时， $\Phi(s) = \frac{128}{s^2 + 16s + 128}$ ，单位阶跃响应如图6-26所示，测得

$$\sigma \% = 4 \%, \quad t _ {p} = 0. 4 \mathrm{s}, \quad t _ {s} = 0. 5 2 \mathrm{s} \quad (\Delta = 2 \%)$$

![](image/2d2e52f959236c1c93d9b8e5dfce56fe75bce4a0008d83e3c8083535281114dc.jpg)

<details>
<summary>line</summary>

| Time/sec | Amplitude |
| --- | --- |
| 0.0 | 0.0 |
| 0.1 | 1.0 |
| 0.2 | 1.2 |
| 0.3 | 1.1 |
| 0.4 | 1.0 |
| 0.5 | 1.0 |
| 0.6 | 1.0 |
| 0.7 | 1.0 |
</details>

图 6-25 无前置滤波器时的单位阶跃响应(MATLAB)

![](image/0d8f0d5abe9e9e49ff204aaeb2f626134f0034811e5b7e7bc72f35d50f984c79.jpg)

<details>
<summary>line</summary>

| Time/sec | Amplitude |
| --- | --- |
| 0.0 | 0.0 |
| 0.1 | 0.4 |
| 0.2 | 0.8 |
| 0.3 | 1.0 |
| 0.4 | 1.05 |
| 0.5 | 1.02 |
| 0.6 | 1.01 |
| 0.7 | 1.0 |
</details>

图 6-26 有前置滤波器时的单位阶跃响应(MATLAB)

MATLAB 文本如下：

```matlab
K1=16; K2=128; Gc=tf([K1 K2], [1 0]);
G0=tf([1], [1 0]); Gp=tf([8], [1 8]);
G=series(Gc, G0);
sys0=feedback(G, 1); %无前置滤波器时的闭环传递函数
sys=series(sys0, Gp); %有前置滤波器时的闭环传递函数
figure(1); step(sys0); grid
figure(2); step(sys); grid 
```
