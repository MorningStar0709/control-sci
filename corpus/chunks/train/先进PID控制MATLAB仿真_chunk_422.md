# 9.1.4 仿真实例

被控对象为

$$y (k) = 0. 3 6 8 y (k - 1) + 0. 2 6 y (k - 2) + 0. 1 0 u (k - 1) + 0. 6 3 2 u (k - 2)$$

输入指令为一方波信号： $y_{\mathrm{d}}(k) = 0.5 \mathrm{sgn}\left(\sin (4\pi t)\right)$ ，采样时间为 $1 \mathrm{~ms}$ ，分别采用四种控制律进行单神经元 PID 控制，即无监督的 Hebb 学习规则、有监督的 Delta 学习规则、有监督的 Hebb 学习规则、改进的 Hebb 学习规则，跟踪结果如图 9-2～图 9-5 所示。

![](image/8f6f30c87512cd353a8a2a1d4563b964ee123098779654c5fb883c438e20b0da.jpg)

<details>
<summary>line</summary>

| time(s) | ideal position | position tracking |
| --- | --- | --- |
| 0.0 | 0.0 | 0.0 |
| 0.1 | 0.5 | 0.5 |
| 0.2 | 0.5 | 0.5 |
| 0.3 | -0.5 | -0.5 |
| 0.4 | -0.5 | -0.5 |
| 0.5 | 0.5 | 0.5 |
| 0.6 | 0.5 | 0.5 |
| 0.7 | -0.5 | -0.5 |
| 0.8 | -0.5 | -0.5 |
| 0.9 | -0.5 | -0.5 |
| 1.0 | -0.5 | -0.5 |
</details>

图 9-2 基于无监督 Hebb 学习规则的位置跟踪 (M = 1)

![](image/639cba1356ba994919a92c15b7f7427846cd2c38a9159ddf8e84ff7b8a6864a8.jpg)

<details>
<summary>line</summary>

| time(s) | ideal position | position tracking |
| --- | --- | --- |
| 0.0 | 0.5 | 0.5 |
| 0.1 | 0.5 | 0.5 |
| 0.2 | 0.5 | 0.5 |
| 0.3 | 0.5 | -0.5 |
| 0.4 | 0.5 | -0.5 |
| 0.5 | 0.5 | -0.5 |
| 0.6 | 0.5 | -0.5 |
| 0.7 | 0.5 | -0.5 |
| 0.8 | 0.5 | -0.5 |
| 0.9 | 0.5 | -0.5 |
| 1.0 | 0.5 | -0.5 |
</details>

图 9-3 基于有监督的 Delta 学习规则的位置跟踪 (M = 2)

![](image/c337c0788839dd4a8f92edcc11f5fadcbfd5de561c78d7ddcb965bf8b4375697.jpg)

<details>
<summary>line</summary>

| time(s) | ideal position | position tracking |
| --- | --- | --- |
| 0.0 | 0.5 | 0.5 |
| 0.25 | 0.5 | 0.5 |
| 0.3 | -0.5 | -0.5 |
| 0.5 | -0.5 | -0.5 |
| 0.75 | -0.5 | -0.5 |
| 1.0 | -0.5 | -0.5 |
</details>

图 9-4 基于有监督 Hebb 学习规则的位置跟踪 (M = 3)

![](image/b6094fcf6021386498eb972e2b24bdc2ad8f2b6097ccdcd20ee6d287af027e62.jpg)

<details>
<summary>line</summary>

| time(s) | ideal position | position tracking |
| --- | --- | --- |
| 0.0 | 0.5 | 0.5 |
| 0.25 | 0.5 | 0.5 |
| 0.3 | -0.5 | -0.5 |
| 0.5 | -0.5 | -0.5 |
| 0.75 | -0.5 | -0.5 |
| 1.0 | -0.5 | -0.5 |
</details>

图 9-5 基于改进学习规则的位置跟踪 (M = 4)

〖仿真程序〗 chap9\_1.m  
```matlab
%Single Neural Adaptive PID Controller
clear all;
close all;

x=[0,0,0]';
xiteP=0.40;
xiteI=0.35; 
```

```matlab
xiteD=0.40;
%Initilizing kp,ki and kd
wkp_1=0.10;
wiki_1=0.10;
wkd_1=0.10;
%wkp_1=rand;
%wiki_1=rand;
%wkd_1=rand;

error_1=0;
error_2=0;
y_1=0;y_2=0;y_3=0;
u_1=0;u_2=0;u_3=0;

ts=0.001;
for k=1:1:1000
    time(k)=k*ts;
    yd(k)=0.5*sign(sin(2*2*pi*k*ts));
    y(k)=0.368*y_1+0.26*y_2+0.1*u_1+0.632*u_2;
    error(k)=yd(k)-y(k);
