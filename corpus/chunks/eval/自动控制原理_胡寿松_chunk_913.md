# 2）相平面法。

描述该系统的微分方程为

$$
\ddot {c} + \dot {c} = \left\{ \begin{array}{l l} 2, & c <   - 2 \\ - c, & | c | <   2 \\ - 2, & c > 2 \end{array} \right.
$$

在相平面上精确绘制 $c - \dot{c}$ 曲线，需要首先确定上述系统微分方程在一定初始条件下的解，完成

这一求解步骤一般十分困难。但借助于 MATLAB 软件，求解过程可以大大简化。进而通过分析相轨迹的运动形式，可直观地判断非线性系统的稳定性。

MATLAB 程序: example8b. m

$$
\begin{array}{l} t = 0: 0. 0 1: 3 0; \quad \% \text {设定仿真时间为} 3 0 \mathrm{s} \\ \mathrm{c} 0 = [ - 3 0 ] ^ {\prime}; \quad \% \text {给定初始条件} \mathrm{c} (0) = - 3, \dot {c} (0) = 0 \\ [ t, c ] = \text {ode45} (^ {\prime} \text {fun} ^ {\prime}, t, c 0); \quad \% \text {求解初始条件下的系统微分方程} \\ \text { figure } (1) \\ \text {plot} (c (:, 1), c (:, 2)); \text {grid} \% \text {绘制相平面图，其中} c (:, 1) \text {为} c (t) \text {值，} c (:, 2) \text {为} \dot {c} (t) \text {值} \\ \end{array}
$$

![](image/37a036237baf0663bc42ca30e8eca625ff7e90478748de639e9e69758623cf17.jpg)

<details>
<summary>other</summary>

| Real Axis | Imaginary Axis |
| --- | --- |
| -0.75 | 0.9 |
| -0.5 | 0.4 |
| -0.25 | 0.0 |
| 0.0 | 0.0 |
| -0.75 | -1.0 |
| -0.5 | -0.4 |
| -0.25 | -0.8 |
| 0.0 | -1.0 |
</details>

图 B-18 描述函数法分析(MATLAB)

```matlab
figure(2)
plot(t,c(:,1)); grid; %绘制系统时间响应曲线
xlabel('t(s)'); ylabel('c(t)') %添加坐标说明
```

调用函数 fun.m

function dc=fun(t, c) %描述系统的微分方程
dc1=c(2); %c1表示c(t),c(2)表示 $\dot{c}(t)$ ,d表示一阶导数
if (c(1)<-2)
    dc2=2-c(2); %当c<-2时, $\ddot{c}=2-\dot{c}$ elseif (abs(c(1))<2)
    dc2=-c(1)-c(2); %当|c|<2时, $\ddot{c}=-c-\dot{c}$ else dc2=-2-c(2); %否则当c>2时, $\ddot{c}=-2-\dot{c}$ end
dc=[dc1 dc2]';

在 MATLAB 中运行 M 文件 example8b 后, 得系统相轨迹和相应的时间响应曲线分别如图 B-19 和图 B-20 所示。由图可见, 系统振荡收敛。系统的奇点为稳定焦点。

需指出的是,对于带高阶线性环节的非线性系统,借助于 MATLAB,分段求解微分方程可以将高阶系统的运动过程转化为包括位置、速度和加速度等变量的多维空间上的广义相轨迹,从而能直观、准确地反映系统的特性。

![](image/b2bf52ac286aeca8bad7d63c082a00359222c70b2c893eba40fa0776a71163e1.jpg)

<details>
<summary>line</summary>

| c/t | c(t) |
| --- | --- |
| -3.0 | 0.2 |
| -2.5 | 0.8 |
| -2.0 | 1.2 |
| -1.5 | 1.4 |
| -1.0 | 1.4 |
| -0.5 | 1.2 |
| 0.0 | 0.0 |
| 0.5 | -0.2 |
</details>

图B-19 相轨迹

![](image/b2cb19567371eefc04bde3243a82524e5a53442710be5b60f756a9d1882f725c.jpg)

<details>
<summary>line</summary>

| t/s | c(t) |
| --- | --- |
| 0 | -3.0 |
| 5 | 0.4 |
| 10 | 0.0 |
| 15 | 0.0 |
| 20 | 0.0 |
| 25 | 0.0 |
| 30 | 0.0 |
</details>

图 B-20 时间响应曲线
