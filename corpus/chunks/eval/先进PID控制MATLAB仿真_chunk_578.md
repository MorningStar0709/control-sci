# 14.4.5 仿真实例

被控对象为式（14.18），取位姿指令 $\left[x_{d}\quad y_{d}\right]$ 为 $x_{d}=t,\quad y_{d}=\sin(0.5x)+0.5x+1$ 。

取位姿初始值为 $[0\quad 0\quad 0]$ ，采用控制律式（14.26）和式（14.27），取 $k_{\mathrm{p1}} = 10$ ， $k_{\mathrm{d1}} = 10$ ， $k_{\mathrm{p3}} = 100$ ，微分器参数取 $R = 100$ ，仿真结果如图14-16～图14-19所示。

![](image/04dc9daaaa33a7f07280c1c08d825bbf75711192ce647e8773ee2843ce3000f6.jpg)

<details>
<summary>line</summary>

| x | ideal trajectory | position tracking |
| --- | --- | --- |
| 0 | 1.0 | 0.5 |
| 5 | 4.0 | 3.5 |
| 10 | 6.0 | 5.5 |
| 15 | 10.0 | 9.5 |
| 20 | 10.5 | 10.0 |
| 25 | 14.0 | 13.5 |
| 30 | 17.0 | 16.5 |
</details>

图 14-16 圆轨迹的跟踪

![](image/91279784a8afeee1378c1e51ddd024e6abd3fef3228c119e078f8359c058a543.jpg)

<details>
<summary>line</summary>

| time(s) | ideal x | x tracking | ideal y | y tracking | θ_d | θ_d tracking |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 0 | 0 | 0 | 0 | 1 | 1 |
| 5 | ~5 | ~5 | ~2 | ~2 | ~0 | ~0 |
| 10 | ~10 | ~10 | ~4 | ~4 | ~-2 | ~-2 |
| 15 | ~15 | ~15 | ~6 | ~6 | ~-4 | ~-4 |
| 20 | ~20 | ~20 | ~8 | ~8 | ~-6 | ~-6 |
| 25 | ~25 | ~25 | ~10 | ~10 | ~-8 | ~-8 |
| 30 | ~30 | ~30 | ~12 | ~12 | ~-10 | ~-10 |
</details>

图 14-17 位置和角度的跟踪

![](image/8a463c64cfa102ec673a625506dee414fa08bb814e44301701e55caea9bca7f0.jpg)

<details>
<summary>line</summary>

| time(s) | θ_d | dθ_d |
| --- | --- | --- |
| 0 | 1.0 | 0.0 |
| 5 | 0.0 | -0.5 |
| 10 | 1.0 | 0.0 |
| 15 | 0.0 | -0.5 |
| 20 | 1.0 | 0.0 |
| 25 | 0.0 | -0.5 |
| 30 | 1.0 | 0.0 |
</details>

图 14-18 微分器的输入与输出

![](image/8fc7a86239eb31a54cb2fff0ea118408afdbc3d7ea6473efcf3dc661fbce0eb4.jpg)

<details>
<summary>line</summary>

| time(s) | Control input v |
| --- | --- |
| 0 | 1.6 |
| 5 | 1.0 |
| 10 | 1.4 |
| 15 | 1.0 |
| 20 | 1.0 |
| 25 | 1.4 |
| 30 | 1.0 |
</details>

![](image/fb543cde909129c9574e1f6f4a72af1682c5f52ff334985ac57a6959cf50f43d.jpg)

<details>
<summary>line</summary>

| time(s) | Control input w |
| --- | --- |
| 0 | 5.0 |
| 5 | 0.0 |
| 10 | 0.0 |
| 15 | 0.0 |
| 20 | 0.0 |
| 25 | 0.0 |
| 30 | 0.0 |
</details>

图 14-19 控制输入信号 $\omega$ 和 v

由仿真可见， $\theta_{d}$ 的最大值为 0.9526 弧度，属于区间 $(-π/2, π/2)$ ，满足式（14.25）的要求。
