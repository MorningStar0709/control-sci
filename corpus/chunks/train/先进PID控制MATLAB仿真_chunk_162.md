# 2.3.2 仿真实例

设被控对象为

$$G (s) = \frac {4 0 0}{s (s ^ {2} + 3 0 s + 2 0 0)}$$

运行整定程序 chap2\_4tuning.m，可得图 2-5～图 2-7。图 2-5 为系统未补偿的根轨迹图，在该图上可选定穿越 jω 轴时的点（共有两个点，任选其一），从而获得增益 $K_{m}$ 和该点的 ω 值即 $\omega_{m}$ 。

![](image/d10e92d2f39dfeec1fc501b4e2b44932ed7331d674233611b905c0921bbb2faf.jpg)

<details>
<summary>line</summary>

| Real Axis | Imaginary Axis |
| --- | --- |
| -20 | 0 |
| -10 | 0 |
| 0 | 0 |
| 15 | -40 |
</details>

图 2-5 未整定时开环系统的根轨迹图  
![](image/f3e397d978e87c38246ac17fd450f05d4a31a3a3383e94d6834912b2fd4e567d.jpg)

<details>
<summary>line</summary>

| Frequency (rad/sec) | Magnitude(dB) | Phase(deg) |
| --- | --- | --- |
| 0.1 | 80 | -90 |
| 1 | 40 | -135 |
| 10 | 0 | -180 |
| 100 | -60 | -225 |
| 1000 | -140 | -270 |
</details>

图 2-6 整定前后系统的伯特图（实线为整定前，虚线为整定后）

![](image/7a37a0bd9240452435c745b584987f90890dbce8bd02336d47ce446ae40fd711.jpg)

<details>
<summary>line</summary>

| Real Axis | Imaginary Axis |
| --- | --- |
| -10 | 0 |
| -6 | 50 |
| 0 | 0 |
</details>

图 2-7 整定后闭环系统的根轨迹

使用 rlocus 及 rlocfind 命令可求得穿越增益 $K_{m}=14$ 和穿越频率 $\omega_{m}=14rad/s$ 。采用 Ziegler-Nichols 整定方法（2.5）可求得 PID 参数：

$$K _ {\mathrm{p}} = 8. 8 3 7 1, K _ {\mathrm{d}} = 0. 4 9 4 5, K _ {\mathrm{i}} = 3 9. 4 8 4 7$$

整定程序中，sys\_pid 和 sysc 分别为控制器和闭环系统的传递函数。图 2-6 为整定前后系统的伯特图，可见，该系统整定后，频带拓宽，相移超前。图 2-7 所示为整定后系统的根轨迹，所有极点位于负半面，达到完全稳定状态。

运行 Simulink 控制程序 chap2\_4.mdl，通过开关切换进行两种方法的仿真，可得图 2-8 和图 2-9，图 2-8 所示为系统未补偿的正弦跟踪，图 2-9 所示为系统采用 PID 补偿后的正弦跟踪。

![](image/72a05ea8e52204402aaa94b530399609e07101abea347ae5ffadabccc119515b.jpg)

<details>
<summary>line</summary>

| time(s) | ideal position signal | position tracking |
| --- | --- | --- |
| 0 | 0.0 | 0.0 |
| 1 | 0.4 | 0.35 |
| 2 | 0.5 | 0.45 |
| 3 | 0.3 | 0.25 |
| 4 | -0.2 | -0.15 |
| 5 | -0.5 | -0.45 |
| 6 | -0.3 | -0.25 |
| 7 | 0.2 | 0.15 |
| 8 | 0.4 | 0.35 |
| 9 | 0.3 | 0.25 |
| 10 | -0.3 | -0.2 |
</details>

图 2-8 整定前的正弦跟踪

![](image/7278f75370fddbe7fc4fcd3b6a7ccfc75f518fecba55047b477772588ca56bbe.jpg)

<details>
<summary>line</summary>

| time(s) | ideal position signal | position tracking |
| --- | --- | --- |
| 0 | 0.0 | 0.0 |
| 1 | 0.45 | 0.45 |
| 2 | 0.5 | 0.5 |
| 3 | 0.3 | 0.3 |
| 4 | -0.2 | -0.2 |
| 5 | -0.5 | -0.5 |
| 6 | -0.2 | -0.2 |
| 7 | 0.4 | 0.4 |
| 8 | 0.5 | 0.5 |
| 9 | 0.3 | 0.3 |
| 10 | -0.3 | -0.3 |
</details>

图 2-9 整定后的正弦跟踪

〖仿真程序〗分为PID整定程序、Simulink主程序和作图程序三个部分。

(1) 整定程序: chap2\_4tuning.m

```matlab
%PID Controller Based on Ziegler-Nichols
clear all;
close all;

sys=tf(400,[1,30,200,0]);

figure(1);
rlocus(sys);
[km,pole]=rlocfind(sys)
