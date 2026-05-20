# 7.1.3 仿真实例

取被控对象参数 J=1.0，C=5.0。位置指令信号取 $\frac{\pi}{3}$ 。采用 PD 控制律式（7.3），取 $k_{p}=100, k_{d}=50$ ，仿真结果如图 7-1 和图 7-2 所示。

![](image/3355de226d05c106a68d9a2e74bf24c07f240f6b3c645dfd7b11687044da2f5f.jpg)

<details>
<summary>line</summary>

| time(s) | ideal position signal | position response |
| --- | --- | --- |
| 0 | 1.0 | 0.5 |
| 1 | 1.0 | 1.1 |
| 2 | 1.0 | 1.0 |
| 3 | 1.0 | 1.0 |
| 4 | 1.0 | 1.0 |
| 5 | 1.0 | 1.0 |
| 6 | 1.0 | 1.0 |
| 7 | 1.0 | 1.0 |
| 8 | 1.0 | 1.0 |
| 9 | 1.0 | 1.0 |
| 10 | 1.0 | 1.0 |
</details>

![](image/f2344212a12b0800a1aa98b7806284604c977f7acd6c038c15330ce6f567782b.jpg)

<details>
<summary>line</summary>

| time(s) | Speed response |
| --- | --- |
| 0 | 0.0 |
| 1 | 0.9 |
| 2 | -0.1 |
| 3 | 0.0 |
| 4 | 0.0 |
| 5 | 0.0 |
| 6 | 0.0 |
| 7 | 0.0 |
| 8 | 0.0 |
| 9 | 0.0 |
| 10 | 0.0 |
</details>

图 7-1 位置和速度响应

![](image/b13b7f7948dab65f1297c8ee33bbea74cf82ea084b8d3f8faff6379ed6d52339.jpg)

<details>
<summary>line</summary>

| time(s) | Control input |
| --- | --- |
| 0 | 50 |
| 1 | -12 |
| 2 | 0 |
| 3 | 0 |
| 4 | 0 |
| 5 | 0 |
| 6 | 0 |
| 7 | 0 |
| 8 | 0 |
| 9 | 0 |
| 10 | 0 |
</details>

图 7-2 PD 控制输入
