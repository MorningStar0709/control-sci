# 3.3.2 仿真实例

设被控对象为

$$G _ {\mathrm{p}} (s) = \frac {\mathrm{e} ^ {- 0 . 7 6 s}}{0 . 4 s + 1}$$

采样时间为 0.5s，期望的闭环响应设计为

$$\phi (s) = \frac {Y (s)}{R (s)} = \frac {\mathrm{e} ^ {- 0 . 7 6 s}}{0 . 1 5 s + 1}$$

位置指令为 $y_{d}=1.0$ ，M=1 时为采用大林控制算法，M=2 时为采用普通 PID 控制算法。可见，采用大林算法可取得很好的控制效果，其阶跃响应结果如图 3-9 和图 3-10 所示。

![](image/cbf05114cacd01c3a1849ad6eb6b984574b80a4bea6eccc3d098a0c3702d2fe1.jpg)

<details>
<summary>line</summary>

| time(s) | ideal position signal | position tracking |
| --- | --- | --- |
| 0 | 0.0 | 0.0 |
| 1 | 1.0 | 1.0 |
| 2 | 1.0 | 1.0 |
| 3 | 1.0 | 1.0 |
| 4 | 1.0 | 1.0 |
| 5 | 1.0 | 1.0 |
| 6 | 1.0 | 1.0 |
| 7 | 1.0 | 1.0 |
| 8 | 1.0 | 1.0 |
| 9 | 1.0 | 1.0 |
| 10 | 1.0 | 1.0 |
| 11 | 1.0 | 1.0 |
| 12 | 1.0 | 1.0 |
| 13 | 1.0 | 1.0 |
| 14 | 1.0 | 1.0 |
| 15 | 1.0 | 1.0 |
| 16 | 1.0 | 1.0 |
| 17 | 1.0 | 1.0 |
| 18 | 1.0 | 1.0 |
| 19 | 1.0 | 1.0 |
| 20 | 1.0 | 1.0 |
| 21 | 1.0 | 1.0 |
| 22 | 1.0 | 1.0 |
| 23 | 1.0 | 1.0 |
| 24 | 1.0 | 1.0 |
| 25 | 1.0 | 1.0 |
</details>

图 3-9 大林算法阶跃响应（M=1）

![](image/d228fb18211e07262803c113d2e29a2a021aa79b01af0b4e888280fddc3416e7.jpg)

<details>
<summary>line</summary>

| time(s) | ideal position signal | position tracking |
| --- | --- | --- |
| 0 | 1.0 | 0.0 |
| 1 | 1.0 | 1.25 |
| 2 | 1.0 | 0.4 |
| 3 | 1.0 | 1.15 |
| 4 | 1.0 | 0.65 |
| 5 | 1.0 | 1.15 |
| 6 | 1.0 | 0.8 |
| 7 | 1.0 | 1.1 |
| 8 | 1.0 | 0.85 |
| 9 | 1.0 | 1.05 |
| 10 | 1.0 | 0.9 |
| 11 | 1.0 | 1.0 |
| 12 | 1.0 | 0.95 |
| 13 | 1.0 | 1.0 |
| 14 | 1.0 | 1.0 |
| 15 | 1.0 | 1.0 |
| 16 | 1.0 | 1.0 |
| 17 | 1.0 | 1.0 |
| 18 | 1.0 | 1.0 |
| 19 | 1.0 | 1.0 |
| 20 | 1.0 | 1.0 |
| 21 | 1.0 | 1.0 |
| 22 | 1.0 | 1.0 |
| 23 | 1.0 | 1.0 |
| 24 | 1.0 | 1.0 |
| 25 | 1.0 | 1.0 |
</details>

图 3-10 普通 PID 算法阶跃响应 (M=2)

〖仿真程序〗 chap3\_3.m  
```matlab
%Delay Control with Dalin Algorithm
clear all;
close all;
ts=0.5;

%Plant
sys1=tf([1],[0.4,1],'inputdelay',0.76);
dsys1=c2d(sys1,ts,'zoh');
[num1,den1]=tfdata(dsys1,'v');

%Ideal closed loop
sys2=tf([1],[0.15,1],'inputdelay',0.76);
dsys2=c2d(sys2,ts,'zoh'); 
```

```matlab
%Design Dalin controller
dsys=1/dsys1*dsys2/(1-dsys2);
[num,den]=tfdata(dsys,'v');

u_1=0.0;u_2=0.0;u_3=0.0;u_4=0.0;u_5=0.0;
y_1=0.0;

error_1=0.0;error_2=0.0;error_3=0.0;
ei=0;
for k=1:1:50
time(k)=k*ts;

yd(k)=1.0; %Tracing Step Signal

y(k)=-den1(2)*y_1+num1(2)*u_2+num1(3)*u_3;
error(k)=yd(k)-y(k);
