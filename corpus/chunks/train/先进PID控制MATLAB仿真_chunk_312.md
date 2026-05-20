# 6.2.2 仿真实例

输入信号为方波信号，采样周期为 h=0.01， $\delta=50$ 。

位置指令为方波，被控对象为 $G(s)=\frac{523500}{s^{3}+87.35s^{2}+10470s}$ 。采用 6.1 节介绍的离散跟踪微分器来获得指令信号的位置和速度，运行安排过渡过程程序 chap6\_3.m，经过微分器处理过的方波信号及其导数如图 6-5 所示。

![](image/c534b05e3ba7877ce32bbab65d3d6347b2afae731f55f3e78cedf0e6f645e9d9.jpg)

<details>
<summary>line</summary>

| time(s) | Ideal position signal | Transient position signal |
| --- | --- | --- |
| 0 | 1 | 0 |
| 3 | -1 | 1 |
| 6 | -1 | -1 |
| 9 | -1 | -1 |
| 10 | -1 | -1 |
</details>

![](image/5ef7a02f13926eda76bf311702b93fc2d13a832e7c53009e00598295e6e36e75.jpg)

<details>
<summary>line</summary>

| time(s) | Transient speed signal |
| --- | --- |
| 0 | 7 |
| 3 | -10 |
| 6 | 5 |
| 9 | -10 |
</details>

图 6-5 方波信号及其过渡过程

在离散方式下，将微分器处理过的方波信号及其导数作为位置和速度指令，采用 PD 控制律，取 $k_{p}=1.0$ ， $k_{d}=0.02$ ，图 6-6 和图 6-7 所示分别为采用和不采用微分器的正弦位置跟踪。可见，采用微分器实现方波的过渡过程，可实现对象的平稳跟踪。还可以采用连续系统仿真实现安排过渡过程，图 6-8 所示为基于 Levant 微分器的方波过渡过程，其中 Levant 微分器算法见 4.2 节，参数取 $\alpha=1$ ， $\lambda=5$ 。

![](image/acfb351b4e9b1bc84727dc07615d52de8f24944b7b9e73bf6f26378c489fd3b0.jpg)

<details>
<summary>line</summary>

| time(s) | Transient position signal | Position signal tracking |
| --- | --- | --- |
| 0 | 0 | 0 |
| 1 | 1 | 1 |
| 2 | 1 | 1 |
| 3 | 1 | 1 |
| 4 | -1 | -1 |
| 5 | -1 | -1 |
| 6 | -1 | -1 |
| 7 | 1 | 1 |
| 8 | 1 | 1 |
| 9 | 1 | 1 |
| 10 | -1 | -1 |
</details>

图 6-6 基于安排过渡过程的方波跟踪（S=2）

![](image/6c10e4ecc46493ffb9513181e6b4b841ec9257f92529e9dd15130fce279f557e.jpg)

<details>
<summary>line</summary>

| time(s) | Ideal position signal | Position signal tracking |
| --- | --- | --- |
| 0 | 1.0 | 1.0 |
| 3 | -1.0 | -1.0 |
| 6 | -1.0 | -1.0 |
| 9 | 1.0 | 1.0 |
| 10 | -1.0 | -1.0 |
</details>

图 6-7 不采用过渡过程的方波跟踪（S=1）

![](image/fb35f31f2fd44e3c26a9ddb6d08b4e114fa80f33bd95be30bc70bd27161e7a9a.jpg)

<details>
<summary>line</summary>

| time(s) | ideal position signal | transient position signal | transient speed signal |
| --- | --- | --- | --- |
| 0 | 1.0 | 1.0 | 0.0 |
| 2 | 1.0 | 1.0 | 0.3 |
| 4 | -1.0 | -1.0 | -0.5 |
| 6 | -1.0 | -1.0 | 0.5 |
| 8 | 1.0 | 1.0 | 0.0 |
| 10 | -1.0 | -1.0 | -0.5 |
| 12 | -1.0 | -1.0 | 0.5 |
| 14 | 1.0 | 1.0 | 0.0 |
</details>

图 6-8 基于 Levant 微分器的方波过渡过程
