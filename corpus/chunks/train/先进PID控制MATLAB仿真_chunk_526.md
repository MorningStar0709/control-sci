# 13.2.4 仿真实例

被控对象模型采用式（13.12）和式（13.13）。仿真时，取 $\varepsilon=0.001$ 。被控对象模型初始状态为 [50] 。采用控制律式（13.20），取 $k_{ps}=10$ ， $k_{pf}=1.0$ ，仿真结果如图 13-6 和图 13-7 所示。

![](image/88a438aabf6109c220804abe88de6ee10ca244f1a32f58bcfcb1a513ecb0902a.jpg)

<details>
<summary>line</summary>

| time(s) | X response |
| --- | --- |
| 0 | 4.5 |
| 0.5 | 0.5 |
| 1 | 0.1 |
| 1.5 | 0.05 |
| 2 | 0.02 |
| 2.5 | 0.01 |
| 3 | 0.005 |
| 3.5 | 0.002 |
| 4 | 0.001 |
| 4.5 | 0.0005 |
| 5 | 0.0001 |
</details>

图13-6 $x$ 的响应

![](image/87e77f3846dba094d93b789d855e551d151b7da91740cc13eaa6bc53d82d95c0.jpg)

<details>
<summary>line</summary>

| time(s) | Control input for slow subsystem | Control input for fast subsystem | Total control input |
| --- | --- | --- | --- |
| 0 | 0 | 0 | 0 |
| 1 | -20 | 0 | 0 |
| 2 | -10 | 0 | 0 |
| 3 | -5 | 0 | 0 |
| 4 | -2 | 0 | 0 |
| 5 | -1 | 0 | 0 |
</details>

图 13-7 控制输入
