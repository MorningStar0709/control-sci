# 5.1.3 仿真实例

对象动态方程为

$$\ddot {\theta} = - b \dot {\theta} + a u - d$$

式中， $a = 5$ ； $b = 0.15$ ； $d$ 为干扰；取 $d = 150\mathrm{sgn}\left(\sin (0.1t)\right)$ 。

开环测试，输入为 $u = \sin t$ ，闭环控制，位置指令为 $\theta_{d} = \sin t$ 。观测器取式（5.2）和式（5.3），取 $k_{1} = 500$ ， $k_{2} = 200$ ，仿真结果如图 5-1 所示。分别采用加补偿和不加补偿的 PD 控制，取 $k_{p} = 100$ ， $k_{d} = 10$ ，位置跟踪效果如图 5-2 和图 5-3 所示。

![](image/5de025483ece9ff9c518f074d6b08c700f027db41a34a1542d6076b5015db52b.jpg)

<details>
<summary>line</summary>

| time(s) | d | Estimate d |
| --- | --- | --- |
| 0 | 150 | 150 |
| 30 | -150 | -150 |
| 65 | -150 | -150 |
| 95 | -150 | -150 |
</details>

图 5-1 干扰及其观测结果

![](image/38abfc230c5ed965344a88de6531bc654d7c29dd733008a30511f78fac79888b.jpg)

<details>
<summary>line</summary>

| time(s) | Ideal position signal | position tracking |
| --- | --- | --- |
| 0 | 1.0 | 1.0 |
| 10 | -1.2 | -1.2 |
| 20 | 1.0 | 1.0 |
| 30 | -1.2 | -1.2 |
| 40 | 1.0 | 1.0 |
| 50 | -1.2 | -1.2 |
| 60 | 1.0 | 1.0 |
| 70 | -1.2 | -1.2 |
| 80 | 1.0 | 1.0 |
| 90 | -1.2 | -1.2 |
| 100 | 1.0 | 1.0 |
</details>

图 5-2 未加补偿时位置跟踪

![](image/a626794b3ebc09ab54658b3c7b5de085324b52a6d8fd3f2a618d3fc0db0ae002.jpg)

<details>
<summary>line</summary>

| time(s) | Ideal position signal | position tracking |
| --- | --- | --- |
| 0 | 1.0 | 1.0 |
| 10 | -1.0 | -1.0 |
| 20 | 1.0 | 1.0 |
| 30 | -1.0 | -1.0 |
| 40 | 1.0 | 1.0 |
| 50 | -1.0 | -1.0 |
| 60 | 1.0 | 1.0 |
| 70 | -1.0 | -1.0 |
| 80 | 1.0 | 1.0 |
| 90 | -1.0 | -1.0 |
| 100 | 1.0 | 1.0 |
</details>

图 5-3 加补偿时位置跟踪
