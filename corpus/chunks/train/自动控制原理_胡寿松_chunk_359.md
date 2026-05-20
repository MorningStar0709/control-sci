![](image/4f0ee5a2106c4e55ac90ded02229d547367c9a14491aa773b020abbe03220fff.jpg)

<details>
<summary>line</summary>

| Time/sec | Amplitude |
| --- | --- |
| 0.0 | 0.0 |
| 0.5 | 0.6 |
| 1.0 | 1.0 |
| 1.5 | 1.2 |
| 2.0 | 1.1 |
| 2.5 | 1.0 |
| 3.0 | 1.0 |
| 3.5 | 1.0 |
| 4.0 | 1.0 |
| 4.5 | 1.0 |
| 5.0 | 1.0 |
</details>

图 6-28 无前置滤波器时系统的时间响应(MATLAB)

![](image/82c8b1f4bda6dc22298b3d9d535d69a46e6dc19d56c0e089d9e329f1f332c396.jpg)

<details>
<summary>line</summary>

| Time/sec | Amplitude |
| --- | --- |
| 0.0 | 0.0 |
| 0.5 | 0.1 |
| 1.0 | 0.4 |
| 1.5 | 0.8 |
| 2.0 | 1.0 |
| 2.5 | 1.0 |
| 3.0 | 1.0 |
| 3.5 | 1.0 |
| 4.0 | 1.0 |
</details>

图 6-29 有前置滤波器时系统的时间响应(MATLAB)

MATLAB 文本如下：

$$
\begin{array}{l} \mathrm{K} = 6. 1 4; \mathrm{z} = 1. 3 4; \mathrm{p} = 2. 8 4; \\ \mathrm{G0} = \operatorname{tf} (\mathrm{K}, [ 1, 1, 0 ]); \quad \% \text {被控对象的传递函数} \\ \mathrm{Gc} = \mathrm{tf} ([ 1, z ], [ 1, p ]); \quad \% \text {超前校正网络的传递函数} \\ \mathrm{Gp} = \mathrm{tf} (z, [ 1, z ]); \quad \% \text {前置滤波的传递函数} \\ \mathrm{G} = \text { series } (\mathrm{G0}, \mathrm{Gc}); \\ \mathrm{sys0} = \text {feedback(G,1) ;} \quad \% \text {无前置滤波器时系统的闭环传递函数} \\ \mathrm{sys} = \text {series(Gp,sys0)}; \quad \% \text {有前置滤波器时系统的闭环传递函数} \\ \text { figure } (1); \text { step } (\text { sys0 }); \text { grid } \\ \text { figure } (2); \text { step(sys) }; \text { grid } \\ \end{array}
$$
