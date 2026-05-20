# 10.5.5 仿真实例

考虑简单的被控对象

$$I \ddot {\theta} + b \dot {\theta} = \tau + d$$

式中， $I=\frac{1}{133}$ ; $b=\frac{25}{133}$ ; $d=\sin t$ 。

采样时间为 $t_{s}=0.001$ ，采用 Z 变换进行离散化。仿真中，最大允许时间为 $3T_{E}$ ，摆线周期 $T_{E}=1$ ，取摆线周期的一半离散点数为 n=500，则采样时间为 $t_{s}=\frac{T_{E}}{2n}=0.001$ 。

采用样条插值方法，插值点选取4个点，即D=4。通过插值点的优化来初始化路径，具体方法为：插值点横坐标固定取第200、第400、第600和第800个点，纵坐标取初始点和终止点之间的4个随机值，第i个样本 $(i=1,2,\cdots,Size)$ 第j个插值点 $(j=1,2,3,4)$ 的值取为

$$\theta_ {\mathrm{op}} (i, j) = \operatorname{rand} \left(\theta_ {\mathrm{d}} - \theta_ {0}\right) + \theta_ {0}$$

式中，rand 为 0～1 之间的随机值。

采用差分进化算法设计最优轨迹 $\theta_{op}$ ，取权值 $\omega=0.60$ ，样本个数 Size=50，变异因子 F=0.5，交叉因子 CR=0.9，优化次数为 30 次。通过差分进化方法不断优化 4 个插值点的纵坐标值，直到达到满意的优化指标 J 或优化次数为止。

跟踪指令为 $\theta_{d}=0.5$ ，采用 PD 控制律式（10.16），取 $k_{p}=300$ ， $k_{d}=0.30$ ，仿真结果如图 10-12～图 10-15 所示。

![](image/8b6fef820511dde9d5a644b484802ed3ccedadfdb80d60d5d2c45851a7978265.jpg)

<details>
<summary>line</summary>

| Time (s) | Ideal trajectory | Optimal trajectory | Trajectory tracking |
| --- | --- | --- | --- |
| 0.0 | 0.0 | 0.0 | 0.0 |
| 0.5 | 0.4 | 0.35 | 0.38 |
| 1.0 | 0.5 | 0.5 | 0.5 |
| 1.5 | 0.5 | 0.5 | 0.5 |
| 2.0 | 0.5 | 0.5 | 0.5 |
| 2.5 | 0.5 | 0.5 | 0.5 |
| 3.0 | 0.5 | 0.5 | 0.5 |
</details>

图 10-12 理想轨迹、最优轨迹及轨迹跟踪

![](image/910495fb166fc1a2d99c2825a8110b3e57c36c8c1dde977088f6463a79a27457.jpg)

<details>
<summary>line</summary>

| Time (s) | Control input, tol |
| --- | --- |
| 0.0 | 0.3 |
| 0.5 | -0.2 |
| 1.0 | -0.8 |
| 1.5 | -1.0 |
| 2.0 | -0.8 |
| 2.5 | -0.4 |
| 3.0 | 0.0 |
</details>

图 10-13 控制输入信号

![](image/47ecce2f57c7ae5946209ffdb2b5efbe4cb87b7dd212198e9e919eed9ac1d6e1.jpg)

<details>
<summary>line</summary>

| Time (s) | Ideal Path | Interpolation points | Optimized Path |
| --- | --- | --- | --- |
| 0.0 | 0.0 | 0.0 | 0.0 |
| 0.2 | 0.1 | 0.1 | 0.1 |
| 0.4 | 0.3 | 0.3 | 0.3 |
| 0.6 | 0.45 | 0.45 | 0.45 |
| 1.0 | 0.5 | 0.5 | 0.5 |
</details>

图 10-14 最优轨迹的优化效果

![](image/6b6ec7e8697878ef76fe98656de016b61a22902261dab414ebadf13ab290a210.jpg)

<details>
<summary>line</summary>

| Time (s) | Fitness Change |
| --- | --- |
| 0 | 105.5 |
| 5 | 105.5 |
| 7 | 101.0 |
| 9 | 93.0 |
| 11 | 93.0 |
| 13 | 91.5 |
| 15 | 91.5 |
| 17 | 90.5 |
| 20 | 90.5 |
| 25 | 90.5 |
| 27 | 90.0 |
| 30 | 90.0 |
</details>

图 10-15 目标函数的优化过程
