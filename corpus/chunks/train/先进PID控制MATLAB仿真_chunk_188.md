# 2.8.2 仿真实例

求二阶传递函数的阶跃响应

$$G _ {\mathrm{p}} (s) = \frac {1 3 3}{s ^ {2} + 2 5 s}$$

采用离散 PID 进行仿真，采样时间为 1ms。

针对阶跃进行仿真，阶跃响应如图 2-26 所示，其中 $k_{p}$ 、 $k_{i}$ 、 $k_{d}$ 随偏差的变化曲线如图 2-27 所示， $k_{p}$ 、 $k_{i}$ 、 $k_{d}$ 随时间的变化曲线如图 2-28 所示。从仿真结果可以看出， $k_{p}$ 、 $k_{i}$ 、 $k_{d}$ 的变化规律符合 PID 控制的原理，取得了很好的仿真效果。

![](image/8b4731ef0804e11646d32b8f41c9b01cf4e0c321ec951feb5da8c51aaa84314f.jpg)

<details>
<summary>line</summary>

| time(s) | Ideal position signal | Position tracking |
| --- | --- | --- |
| 0.00 | 1.0 | 1.0 |
| 0.05 | 1.0 | 1.0 |
| 0.10 | 1.0 | 1.0 |
| 0.15 | 1.0 | 1.0 |
| 0.20 | 1.0 | 1.0 |
| 0.25 | 1.0 | 1.0 |
| 0.30 | 1.0 | 1.0 |
| 0.35 | 1.0 | 1.0 |
| 0.40 | 1.0 | 1.0 |
| 0.45 | 1.0 | 1.0 |
| 0.50 | 1.0 | 1.0 |
</details>

图 2-26 阶跃响应

![](image/a3ea9882ac888493d8bba63451e89687471d4c12211f469e808ee997aaf72aba.jpg)

<details>
<summary>line</summary>

| error | kp | kd | ki |
| --- | --- | --- | --- |
| -0.2 | 22.0 | 0.85 | 0.90 |
| 0.0 | 22.0 | 0.83 | 0.90 |
| 0.2 | 22.1 | 0.81 | 0.89 |
| 0.4 | 22.3 | 0.79 | 0.87 |
| 0.6 | 22.6 | 0.77 | 0.84 |
| 0.8 | 23.0 | 0.75 | 0.80 |
| 1.0 | 23.5 | 0.73 | 0.75 |
</details>

图2-27 $k_{\mathrm{p}}$ 、 $k_{\mathrm{i}}$ 、 $k_{\mathrm{d}}$ 随偏差的变化曲线

![](image/bee4bbb13adeca0e5eaf338c977c40cf5452aa8c5bdd953004f9d7ed63e8b64e.jpg)

<details>
<summary>line</summary>

| time(s) | kp |
| --- | --- |
| 0.00 | 24 |
| 0.05 | 22 |
| 0.10 | 22 |
| 0.15 | 22 |
| 0.20 | 22 |
| 0.25 | 22 |
| 0.30 | 22 |
| 0.35 | 22 |
| 0.40 | 22 |
| 0.45 | 22 |
| 0.50 | 22 |
</details>

![](image/ce148ebb75ec8da0ba5e39db333b54dfe685f4a767be3f37e5ac1a5176d51c3c.jpg)

<details>
<summary>line</summary>

| time(s) | kd |
| --- | --- |
| 0.00 | 0.75 |
| 0.05 | 0.83 |
| 0.10 | 0.84 |
| 0.15 | 0.84 |
| 0.20 | 0.84 |
| 0.25 | 0.84 |
| 0.30 | 0.84 |
| 0.35 | 0.84 |
| 0.40 | 0.84 |
| 0.45 | 0.84 |
| 0.50 | 0.84 |
</details>

![](image/49e14788241835dd1feb1b96a4bdece9dd1611af363b11f23c34a7d2988cb974.jpg)

<details>
<summary>line</summary>

| time(s) | ki |
| --- | --- |
| 0.00 | 0.7 |
| 0.05 | 0.9 |
| 0.10 | 0.9 |
| 0.15 | 0.9 |
| 0.20 | 0.9 |
| 0.25 | 0.9 |
| 0.30 | 0.9 |
| 0.35 | 0.9 |
| 0.40 | 0.9 |
| 0.45 | 0.9 |
| 0.50 | 0.9 |
</details>

图2-28 $k_{\mathrm{p}}$ 、 $k_{\mathrm{i}}$ 、 $k_{\mathrm{d}}$ 随时间的变化曲线

〖仿真程序〗 chap2\_10.m  
```matlab
%Nonlinear PID Control for a servo system
clear all;
close all;

ts=0.001;
J=1/133;
q=25/133;
sys=tf(1,[J,q,0]);
dsys=c2d(sys,ts,'z');
[num,den]=tfdata(dsys,'v');

u_1=0;u_2=0;
y_1=0;y_2=0;
error_1=0;
ei=0;
for k=1:1:500
time(k)=k*ts;
