# 例 3.21 用 Matlab 求卫星传递函数

(1) 求例 2.3 中输入 $F_{c}$ 和姿态角 $\theta$ 之间的传递函数；  
（2）在以 t=5s 为起始时刻的 0.1s 内，系统受到 25N 脉冲激励，确定系统响应。设 d=1m 和 $I=5000kg\cdot m^{2}$ 。

解答。

(1) 由例 2.3，得

$$\frac {d}{I} = \frac {1}{5 0 0 0} \frac {\mathrm{m}}{\mathrm{kg} \cdot \mathrm{m} ^ {2}} = 0. 0 0 0 2 \frac {\mathrm{m}}{\mathrm{kg} \cdot \mathrm{m} ^ {2}}$$

这意味着系统传递函数为

$$H (s) = \frac {0 . 0 0 0 2}{s ^ {2}}$$

通过这个特例检验也可以确定该式。我们可以标示传递函数分子多项式的系数为向量 num 和分母多项式的系数为行向量 den。结果为

$$
\mathrm{num} = \left[ \begin{array}{l l l} 0 & 0 & 0. 0 0 0 2 \end{array} \right], \quad \mathrm{den} = \left[ \begin{array}{l l l} 1 & 0 & 0 \end{array} \right]
$$

(2) 下面的 Matlab 语句用来计算系统的脉冲输入为 25N, 0.1s 时的响应:

```matlab
s=tf('s'); % define Laplace variable
sysG=0.0002/s^2; % define system by its transfer function
t=0:0.01:10; % set up time vector with dt = 0.01 sec
% pulse of 25N, at 5 sec, for 0.1 sec duration
u1=[zeros(1,500)
25*ones(1,10)
zeros(1,491)]; % pulse input
[y1]=lsim(sysG,u1,t); % linear simulation
ff=180/pi; % conversion factor from radians to degrees
y1=ff*y1; % output in degrees
plot(t,u1); % plot input signal
plot(t,y1); % plot output response 
```

116

在 t=5s 时系统受到一个短脉冲（脉冲输入）激励，其作用相当于在 t=5s 时给系统加一个非零角 $\theta_{0}$ 。因为系统是无阻尼的，在没有控制，即不受任何约束的情况下，该系统将在 t=5s 时以由脉冲给出的恒定角速度飘移输入的时间响应如图 3.7a 所示，角 $\theta$ 飘移如图 3.7b 所示。

![](image/d8a410046f498f8bbcb4ffc98a4a11d952dbf022c145cfcd67ef86955a5f1504.jpg)

<details>
<summary>bar</summary>

| 时间/s | 推力 Fc/N |
| --- | --- |
| 5 | 25 |
</details>

a）推力输入

![](image/a5d9c1cfb410aad653aabc183d87d4f2563453726176950cf9466c97b0a0b755.jpg)

<details>
<summary>line</summary>

| 时间/s | θ/(°) |
| --- | --- |
| 5 | 0 |
| 10 | 0.145 |
</details>

b）卫星姿态  
图 3.7 卫星暂态响应

在 t=5s 时，我们用相同的正脉冲激励系统，在 t=6.1s 时受到相同幅值和持续时间的负脉冲激励[见图 3.8a 中输入]，那么系统的暂态响应如图 3.8b 所示。这就说明了实际应用中卫星姿态角是如何控制的。相关的其他 Matlab 语句如下。

```matlab
% double pulse input
u2=[zeros(1,500) 25*ones(1,10) zeros(1,100) -25*ones(1,10)
zeros(1,381)];
[y2]=lsim(sysG,u2,t); % linear simulation
plot(t,u2); % plot input signal
ff=180/pi; % conversion factor from radians to degrees
y2=ff*y2; % output in degrees
plot(t,y2); % plot output response 
```

117

![](image/0a1721e5551791f98063986d1a87528f95be320b59636f6f1df72d44536cbc29.jpg)

<details>
<summary>bar</summary>

| 时间/s | 推力 Fc/N |
| --- | --- |
| 5 | 25 |
| 6 | 0 |
| 6 | -25 |
</details>

a）输入

![](image/ab5a691824d569665be4212ed6eddd082a0f723b46dd886d95cca10e16a7cb88.jpg)

<details>
<summary>line</summary>

| 时间/s | θ(°) |
| --- | --- |
| 5 | 0.0000 |
| 6 | 0.0320 |
| 10 | 0.0320 |
</details>

b）卫星姿态  
图 3.8 卫星暂态响应(双脉冲)
