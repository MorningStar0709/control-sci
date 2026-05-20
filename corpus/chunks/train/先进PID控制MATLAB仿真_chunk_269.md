# 2. 闭环控制

针对模型式（5.8），取 $d(t) = -5$ 。位置指令为 $\theta_{d} = \sin t$ ，观测器采用式（5.13），控制器采用式（5.14），取 $k_{p} = 10$ ， $k_{d} = 1.0$ ，仿真结果如图 5.6～图 5.8 所示。

![](image/6dfc28f04761f3f12424396faf07335b78cdd90a686326c67c52994a74791688.jpg)

<details>
<summary>line</summary>

| time(s) | ideal angle | x1 |
| --- | --- | --- |
| 0 | 0.0 | 0.0 |
| 2 | 1.0 | 1.0 |
| 4 | -1.0 | -1.0 |
| 6 | 0.0 | 0.0 |
| 8 | 1.0 | 1.0 |
| 10 | -0.5 | -0.5 |
</details>

![](image/a8c897ae43e0d86de8b2f8b911dfdd32364d0a99f52326b5a26bb700b0083e13.jpg)

图 5.6 角度和角速度跟踪  
![](image/d557395a5966b12d88c2fe4ee7a486e2dbee932288a3611952caff37c067af21.jpg)

<details>
<summary>line</summary>

| time(s) | dt | dt estimation |
| --- | --- | --- |
| 0 | -5.0 | -5.0 |
| 1 | -5.0 | -5.0 |
| 2 | -5.0 | -5.0 |
| 3 | -5.0 | -5.0 |
| 4 | -5.0 | -5.0 |
| 5 | -5.0 | -5.0 |
| 6 | -5.0 | -5.0 |
| 7 | -5.0 | -5.0 |
| 8 | -5.0 | -5.0 |
| 9 | -5.0 | -5.0 |
| 10 | -5.0 | -5.0 |
</details>

![](image/e9899857c12b0f32d8b82d6b18067449203b10b70ce3749a4f40fb2df0af8ec1.jpg)

<details>
<summary>line</summary>

| time(s) | error between dt and its estimation |
| --- | --- |
| 0 | 0 |
| 1 | -1 |
| 2 | -2 |
| 3 | -3 |
| 4 | -4 |
| 5 | -5 |
| 6 | -4 |
| 7 | -3 |
| 8 | -2 |
| 9 | -1 |
| 10 | 0 |
</details>

图 5.7 干扰及观测结果

![](image/953dc57516582b3e68b35bb5b1ae3bb0eb28827c3d967e3229a303b7933117aa.jpg)

<details>
<summary>line</summary>

| time(s) | Control input |
| --- | --- |
| 0 | 5.5 |
| 1 | 5.2 |
| 2 | 5.0 |
| 3 | 4.9 |
| 4 | 4.9 |
| 5 | 5.0 |
| 6 | 5.1 |
| 7 | 5.0 |
| 8 | 4.9 |
| 9 | 4.9 |
| 10 | 4.9 |
</details>

图 5.8 控制输入
