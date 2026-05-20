# 2.7.2 仿真实例

设被控对象为

$$G _ {\mathrm{p}} (s) = \frac {1}{6 0 s + 1} \mathrm{e} ^ {- 8 0 s}$$

临界比例度法整定分成两步：

（1）采样周期取为 $T_{s}=20$ ，将被控对象和PID控制器离散化，首先采用纯比例控制（程序中取M=1），取 $\delta_{r}=0.575$ ，使系统对阶跃输入的响应达到临界振荡状态，如图2-22所示，这是一个反复测试的过程；

![](image/9d7a90ea1e32a84b7bce92deaefe6202d54c293432bce31c83a6fb0d3751bc65.jpg)

<details>
<summary>line</summary>

| time(s) | Ideal position signal | position tracking |
| --- | --- | --- |
| 0 | 0.0 | 0.0 |
| 500 | 1.4 | 1.4 |
| 1000 | 0.0 | 0.0 |
| 1500 | 1.4 | 1.4 |
| 2000 | 0.0 | 0.0 |
| 2500 | 1.4 | 1.4 |
| 3000 | 0.0 | 0.0 |
| 3500 | 1.4 | 1.4 |
| 4000 | 0.0 | 0.0 |
| 4500 | 1.4 | 1.4 |
| 5000 | 0.0 | 0.0 |
| 5500 | 1.4 | 1.4 |
| 6000 | 0.0 | 0.0 |
</details>

图 2-22 等幅振荡曲线（M=1）

（2）然后按照临界比例度法，根据图 2-22 可得到 $T_{r}=500-200=300$ ；

（3）根据表 2-2，采用 PI 控制算法，可计算得到 $K_{p}$ 、 $T_{I}$ 的值，程序中取 M=3，仿真结果如图 2-23 所示。

![](image/99e858c0ae3e78ab84104d142676d00895fd71ad091a716312d77661a8c4aafc.jpg)

<details>
<summary>line</summary>

| time(s) | Ideal position signal | position tracking |
| --- | --- | --- |
| 0 | 0.0 | 0.0 |
| 500 | 0.9 | 0.7 |
| 1000 | 0.95 | 0.9 |
| 2000 | 0.98 | 0.95 |
| 3000 | 0.99 | 0.98 |
| 4000 | 0.995 | 0.99 |
| 5000 | 0.998 | 0.995 |
| 6000 | 1.0 | 1.0 |
</details>

图 2-23 闭环 PID 控制单位阶跃响应曲线（M=3）

〖仿真程序〗 chap2\_9.m  
```matlab
clear all;
close all;
Ts=20;

%Delay plant
deltar=0.575;
Tr=1000/4; %From 4000 to 5000

kp=1;
Tp=60;
tol=80;
sys=tf([kp],[Tp,1],'inputdelay',tol);
dsys=c2d(sys,Ts,'zoh');
[num,den]=tfdata(dsys,'v');

u_1=0.0;u_2=0.0;u_3=0.0;u_4=0.0;u_5=0.0;
e_1=0;
ei=0;
y_1=0.0;
for k=1:1:300
    time(k)=k*Ts;

yd(k)=1.0; %Tracing Step Signal

y(k)=-den(2)*y_1+num(2)*u_5;

e(k)=yd(k)-y(k);
de(k)=(e(k)-e_1)/Ts; 
```

```matlab
ei=ei+Ts*e(k);

u(k)=1/deltar*e(k);

M=1;
if M==1 %Critical testing
    delta=deltar;
    u(k)=1/delta*e(k);
elseif M==2 %P
    delta1=2*deltar;
    u(k)=1/delta1*e(k);
elseif M==3 %PI
    delta2=2.2*deltar;
    TI2=0.85*Tr;
    u(k)=1/delta2*(e(k)+1/TI2*ei);
elseif M==4 %PID
    delta3=1.7*deltar;
    TI3=0.5*Tr;
    TD3=0.13*Tr;
    u(k)=1/delta3*(e(k)+1/TI3*ei+TD3*de(k));
end

e_1=e(k);
u_5=u_4;u_4=u_3;u_3=u_2;u_2=u_1;u_1=u(k);
y_1=y(k);
end

plot(time,yd,'r',time,y,'k:','linewidth',2);
xlabel('time(s)');ylabel('Position tracking');
legend('Ideal position signal','position tracking','location','NorthEast'); 
```

![](image/3c703ae1334e563c54f16a696d1739260cd57def901e18fae734530047f43cee.jpg)
