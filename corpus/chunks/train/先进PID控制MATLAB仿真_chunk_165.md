# 2.3.4 仿真实例

设被控对象为

$$G (s) = \frac {1}{1 0 s ^ {2} + 2 s}$$

采样周期为 T=0.25s。

采用零阶保持器将对象离散化，使用 rlocus 及 rlocfind 命令作出 $G(z)$ 的根轨迹图，可求得振荡增益 $K_{m}=11.2604$ 和振荡频率 $\omega_{m}=1.0546rad/s$ 。采用 Ziegler-Nichols 公式（2.6）可求得离散 PID 参数：

$$K _ {\mathrm{p}} = 6. 7 5 6 2, K _ {\mathrm{d}} = 5. 0 3 1 8, K _ {\mathrm{i}} = 2. 2 6 7 9$$

运行整定程序 chap2\_5tuning.m，可得图 2-10 和图 2-11。图 2-10 所示为系统未补偿的根轨迹图与 z 平面单位圆的比较，在根轨迹图上选定与 z 平面单位圆上的交点（共有两个点，任选其一），则求得所对应的增益 $K_{m}$ 和该点对应的 $\omega_{m}$ 。整定程序中，dsysc 为校正后的离散闭环系统。图 2-11 所示为 PID 整定后闭环系统的根轨迹。

运行控制程序 chap2\_5.m，通过开关切换进行两种方法的仿真，可得图 2-12 和图 2-13。图 2-12 所示为系统采用 PID 校正后的正弦跟踪，图 2-13 所示为系统未校正的正弦跟踪。

![](image/7ec18928a58753745136d65fd9cd30a8225acda872a5eacb30b7c4de82328d95.jpg)

图 2-10 未整定时开环系统的根轨迹图与单位圆比较  
![](image/0648c6d5a6645c6756ecd200a8c92df9932507544b08da83c06e22980f52d14f.jpg)

<details>
<summary>radar</summary>

| Real Axis | Imaginary Axis |
| --- | --- |
| -1.0 | 0.0 |
| -0.5 | 0.2 |
| 0.0 | 0.4 |
| 0.5 | 0.6 |
| 1.0 | 0.8 |
| 1.5 | 1.0 |
</details>

图 2-11 整定后闭环系统的根轨迹图与单位圆比较

![](image/b50d6e68ce82965e676bd18b6a8b2965b1f3d8100d425e344180d8dd208dba1a.jpg)

<details>
<summary>line</summary>

| time(s) | ideal position signal | position tracking |
| --- | --- | --- |
| 0 | 0.0 | 0.0 |
| 25 | 0.5 | 0.5 |
| 50 | -0.5 | -0.5 |
| 75 | 0.5 | 0.5 |
| 100 | -0.5 | -0.5 |
| 125 | 0.5 | 0.5 |
| 150 | -0.5 | -0.5 |
| 175 | 0.5 | 0.5 |
| 200 | -0.5 | -0.5 |
| 225 | 0.5 | 0.5 |
| 250 | -0.5 | -0.5 |
</details>

图 2-12 整定后的正弦跟踪

![](image/f0025cf01e1f50e34b8b743d485a63157f7e9f99ddb1ef90915068f3050ad5a4.jpg)

<details>
<summary>line</summary>

| time(s) | ideal position signal | position tracking |
| --- | --- | --- |
| 0 | 0.0 | 0.0 |
| 50 | 0.6 | 0.6 |
| 100 | 0.0 | 0.0 |
| 150 | -0.6 | -0.6 |
| 200 | 0.6 | 0.6 |
| 250 | 0.0 | 0.0 |
</details>

图 2-13 整定前的正弦跟踪（M=2）

〖仿真程序〗分为PID整定程序和PID控制程序两部分。

(1) PID 整定程序: chap2\_5tuning.m

```matlab
%PID Controller Based on Ziegler-Nichols
clear all;
close all;

ts=0.25;
sys=tf(1,[10,2,0]);
dsys=c2d(sys,ts,'zoh');
[num,den]=tfdata(dsys,'v');

axis('normal'),zgrid('new');

figure(1);
rlocus(dsys);
[km,pole]=rlocfind(dsys)

wm=angle(pole(1))/ts;
kp=0.6*km
kd=kp*pi/(4*wm)
ki=kp*wm/pi

sysc=tf([kd,kp,ki],[10,2,0,0]);
dsysc=c2d(sysc,ts,'zoh');
figure(2);
rlocus(dsysc);
axis('normal'),zgrid; 
```

(2) PID 控制程序: chap2\_5.m

```txt
close all; 
```

```matlab
ts=0.25;
sys=tf(1,[10,2,0]);
dsys=c2d(sys,ts,'z');
[num,den]=tfdata(dsys,'v');
