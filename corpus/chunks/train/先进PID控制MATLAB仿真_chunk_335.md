# (2) 离散系统仿真

取采样时间为 h=0.01 。用于安排过渡过程的微分器参数取 $\delta=10$ 。扩张观测器中，取 $\beta_{1}=100,\quad\beta_{2}=300,\quad\beta_{3}=1000,\quad\delta=0.0025,\quad\alpha_{1}=0.5,\quad\alpha_{2}=0.25$ 。非线性 PID 控制器中，取 $\alpha_{1}=\frac{3}{4},\quad\alpha_{2}=\frac{3}{2},\quad\delta=2h,\quad\beta_{1}=3.0,\quad\beta_{2}=0.3$ 。采用自抗扰控制方法的方波跟踪及扩张观测器仿真结果如图 6-19 和图 6-20 所示。如果采用线性 PD 控制， $k_{p}$ 和 $k_{d}$ 不变，仿真结果如图 6-21 所示。

![](image/a30be92d92c5ad1009a66e425f54600b8a4e5ba742848e676c492ff2d2f25f79.jpg)

<details>
<summary>line</summary>

| time(s) | ideal position signal | transient position signal | position tracking signal |
| --- | --- | --- | --- |
| 0 | 1.0 | 1.0 | 1.0 |
| 2 | 1.0 | 1.0 | 1.0 |
| 4 | -1.0 | -1.0 | -1.0 |
| 6 | -1.0 | -1.0 | -1.0 |
| 8 | 1.0 | 1.0 | 1.0 |
| 10 | -1.0 | -1.0 | -1.0 |
| 12 | -1.0 | -1.0 | -1.0 |
| 14 | 1.0 | 1.0 | 1.0 |
| 16 | -1.0 | -1.0 | -1.0 |
| 18 | -1.0 | -1.0 | -1.0 |
| 20 | 1.5 | 1.5 | 1.5 |
</details>

图 6-19 基于自抗扰控制的方波响应（M=1）

![](image/f030e31019f538ff356aa4436cc4eaa1f076e056c1930bf23202fec01af0f256.jpg)

<details>
<summary>line</summary>

| time(s) | z1_y (practical position signal) | z1_y (position signal estimation) | z2dy (practical speed signal) | z2dy (speed signal estimation) | z3,x3 (practical uncertain part) | z3,x3 (uncertain part estimation) |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | ~0.5 | ~0.5 | ~0 | ~0 | ~0 | ~0 |
| 2 | ~1.0 | ~1.0 | ~-5 | ~-5 | ~-5 | ~-5 |
| 4 | ~-1.0 | ~-1.0 | ~-10 | ~-10 | ~-10 | ~-10 |
| 6 | ~-1.0 | ~-1.0 | ~0 | ~0 | ~0 | ~0 |
| 8 | ~1.0 | ~1.0 | ~7 | ~7 | ~7 | ~7 |
| 10 | ~-1.0 | ~-1.0 | ~-10 | ~-10 | ~-10 | ~-10 |
| 12 | ~-1.0 | ~-1.0 | ~0 | ~0 | ~0 | ~0 |
| 14 | ~-1.0 | ~-1.0 | ~-5 | ~-5 | ~-5 | ~-5 |
| 16 | ~-1.0 | ~-1.0 | ~-10 | ~-10 | ~-10 | ~-10 |
| 18 | ~-1.0 | ~-1.0 | ~0 | ~0 | ~0 | ~0 |
| 20 | ~1.5 | ~1.5 | ~9 | ~9 | ~9 | ~9 |
</details>

图 6-20 扩张观测器的观测结果（M=1）

![](image/ae00727e8d7b64785fc30860d31a41019a21edf86e9c215e4fee988d11f7b6ca.jpg)

<details>
<summary>line</summary>

| time(s) | ideal position signal | position tracking |
| --- | --- | --- |
| 0 | 1.0 | 1.0 |
| 2 | 1.0 | 1.0 |
| 4 | -1.0 | -1.0 |
| 6 | -1.0 | -1.0 |
| 8 | 1.0 | 1.0 |
| 10 | -1.0 | -1.0 |
| 12 | -1.0 | -1.0 |
| 14 | 1.0 | 1.0 |
| 16 | -1.0 | -1.0 |
| 18 | -1.0 | -1.0 |
| 20 | 1.0 | 1.0 |
</details>

图 6-21 传统线性 PID 下的方波响应 (M=2)
