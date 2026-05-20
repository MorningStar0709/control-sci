设 $S=\left[\begin{array}{ccc}x_{3}&x_{5}&x_{7}\\ x_{4}&x_{6}&x_{8}\end{array}\right]=\left[\begin{array}{ccc}\frac{\partial x_{1}}{\partial a}&\frac{\partial x_{1}}{\partial b}&\frac{\partial x_{1}}{\partial c}\\ \frac{\partial x_{2}}{\partial a}&\frac{\partial x_{2}}{\partial b}&\frac{\partial x_{2}}{\partial c}\end{array}\right]\bigg|_{\text{标称}}$

可给出方程(3.7) $\dot{x}_1 = x_2, x_1(0) = x_{10}$ $\dot{x}_2 = -\sin x_1 - x_2, x_2(0) = x_{20}$ $\dot{x}_3 = x_4, x_3(0) = 0$ $\dot{x}_4 = -x_3\cos x_1 - x_4 - x_2, x_4(0) = 0$ $\dot{x}_5 = x_6, x_5(0) = 0$ $\dot{x}_6 = -x_5\cos x_1 - x_6 - x_2\cos x_1, x_6(0) = 0$ $\dot{x}_7 = x_8, x_7(0) = 0$ $\dot{x}_8 = -x_7\cos x_1 - x_8 - \sin x_1, x_8(0) = 0$

该方程的解是当初始状态为 $x_{10} = x_{20} = 1$ 时计算的。图3.2(a)所示的 $x_{3}, x_{5}$ 和 $x_{7}$ 分别是 $x_{1}$ 对 $a, b$ 和 $c$ 的灵敏度。图3.2(b)所示的是 $x_{2}$ 相应的曲线。从这些图上可以看出，解对参数 $c$ 变化时的灵敏度比对参数 $a$ 和 $b$ 变化时的灵敏度高，这与解其他初始状态方程是一致的。

![](image/5b6a7b3be9d7652bbe26ca63b8fe836b89749ca1f1ae2364ff58f43b337a5354.jpg)

<details>
<summary>line</summary>

| x | x3 | x5 | x7 |
| --- | --- | --- | --- |
| 0 | 0.0 | 0.0 | 0.0 |
| 5 | 0.5 | 0.3 | -0.8 |
| 10 | 0.0 | 0.0 | 0.0 |
</details>

(a)

![](image/4054c5767a3244c1b49990432ec8f6bb9aa358f667a57059217e8620b35d5782.jpg)

<details>
<summary>line</summary>

| x | x4 | x6 | x8 |
| --- | --- | --- | --- |
| 0 | 0.0 | 0.0 | 0.0 |
| 1 | -0.2 | -0.1 | -0.3 |
| 2 | -0.4 | -0.3 | -0.5 |
| 3 | -0.6 | -0.5 | -0.7 |
| 4 | -0.4 | -0.3 | -0.5 |
| 5 | -0.2 | -0.1 | -0.3 |
| 6 | 0.0 | 0.1 | -0.1 |
| 7 | 0.2 | 0.3 | 0.1 |
| 8 | 0.4 | 0.5 | 0.3 |
| 9 | 0.6 | 0.7 | 0.5 |
| 10 | 0.4 | 0.5 | 0.3 |
</details>

(b)   
图3.2 例3.7的灵敏度函数
