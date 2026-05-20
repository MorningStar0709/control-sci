# 【仿真方法一】

采用 M 语言进行数字化仿真。按 Smith 算法设计控制器。取位置指令为方波信号，取 $y_{d}=r$ ，M 代表三种情况下的仿真：M=1 为模型不精确，M=2 为模型精确，M=3 为采用 PI 控制。取 S=2，针对 M=1，M=2，M=3 三种情况进行仿真。在 PI 控制中， $k_{p}=0.50$ ， $k_{i}=0.010$ 。其响应结果如图 3-20～图 3-22 所示。

![](image/dde399c6af312df7028c034237124d36d2aa5422f2742f335c3f50ff6caa8fa1.jpg)

<details>
<summary>line</summary>

| time(s) | ideal position signal | position tracking |
| --- | --- | --- |
| 0 | 1.0 | 0.0 |
| 2000 | 1.0 | 1.0 |
| 4000 | 1.0 | -1.0 |
| 6000 | 1.0 | 1.0 |
| 8000 | 1.0 | -1.0 |
| 10000 | 1.0 | 1.0 |
| 12000 | 1.0 | 1.0 |
</details>

图 3-20 模型不精确时方波响应（M=1）

![](image/390af0f9e02a7f59816e0c7f812bcc9efb41f87840173939144fa76908fd1188.jpg)

<details>
<summary>line</summary>

| time(s) | ideal position signal | position tracking |
| --- | --- | --- |
| 0 | 0.0 | 0.0 |
| 2500 | 1.0 | 1.0 |
| 3000 | -1.0 | -1.0 |
| 5000 | 1.0 | 1.0 |
| 7500 | -1.0 | -1.0 |
| 10000 | 1.0 | 1.0 |
| 12000 | 1.0 | 1.0 |
</details>

图 3-21 模型精确时方波响应（M=2）

![](image/c05698be65ee7cf263906efe0f9f4b304d6255d6893b28760ec1d588310b06fe.jpg)

<details>
<summary>line</summary>

| time(s) | ideal position signal | position tracking |
| --- | --- | --- |
| 0 | 1.0 | 0.0 |
| 2000 | 1.0 | 1.4 |
| 3000 | -1.0 | -1.8 |
| 5000 | 1.0 | 1.8 |
| 6000 | 1.0 | 0.7 |
| 8000 | -1.0 | -1.8 |
| 10000 | 1.0 | 1.4 |
| 12000 | 1.0 | 1.0 |
</details>

图 3-22 PI 控制时方波响应 (M=3)

〖仿真程序〗 chap3\_6.m  
```matlab
%Big Delay PID Control with Smith Algorithm
clear all;close all;
Ts=20;

%Delay plant
kp=1;
Tp=60;
tol=80;
sysP=tf([kp],[Tp,1],'inputdelay',tol); %Plant
dsysP=c2d(sysP,Ts,'zoh'); 
```

```matlab
[numP,denP]=tfdata(dsysP,'v');
M=1;
%Prediction model
if M==1 %No Precise Model: PI+Smith
    kp1=kp*1.10;
    Tp1=Tp*1.10;
    tol1=tol*1.0;
elseif M==2|M==3 %Precise Model: PI+Smith
    kp1=kp;
    Tp1=Tp;
    tol1=tol;
end

sysHO=tf([kp1],[Tp1,1]); %Model without delay
dsysHO=c2d(sysHO,Ts,'zoh');
[numHO,denHO]=tfdata(dsysHO,'v');

sysHP=tf([kp1],[Tp1,1],'inputdelay',tol1); %Model with delay
dsysHP=c2d(sysHP,Ts,'zoh');
[numHP,denHP]=tfdata(dsysHP,'v');

u_1=0.0;u_2=0.0;u_3=0.0;u_4=0.0;u_5=0.0;
e1_1=0;
e2=0.0;
e2_1=0.0;
ei=0;

xm_1=0.0;
ym_1=0.0;
y_1=0.0;

for k=1:1:600
    time(k)=k*Ts;

yd(k)=sign(sin(0.0002*2*pi*k*Ts)); %Tracing Square Wave Signal
y(k)=-denP(2)*y_1+numP(2)*u_5; %GP(z):Practical Plant

%Prediction model
xm(k)=-denHO(2)*xm_1+numHO(2)*u_1; %GHO(z):Without Delay
ym(k)=-denHP(2)*ym_1+numHP(2)*u_5; %GHP(z):With Delay
