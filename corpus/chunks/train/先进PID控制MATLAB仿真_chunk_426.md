# 9.2.2 仿真实例

设被控对象过程模型为

$$y (k) = 0. 3 6 8 y (k - 1) + 0. 2 6 4 y (k - 2) + u (k - d) + 0. 6 3 2 u (k - d - 1) + \xi (k)$$

应用最优二次型性能指标学习算法进行仿真研究。 $\xi(k)$ 为在 100 个采样时间的外加干扰， $\xi(100)=0.10$ ，输入为阶跃响应信号 $y_{\mathrm{d}}(k)=1.0$ 。启动时采用开环控制，取 u=0.1726，K=0.02，P=2，Q=1，d=6，比例、积分、微分三部分加权系数学习速率分别取 $\eta_{1}=4$ ， $\eta_{p}=120$ ， $\eta_{D}=159$ ， $w_{1}(0)=0.34$ ， $w_{2}(0)=0.32$ ， $w_{3}(0)=0.33$ ，神经元自适应 PID 跟踪及中权值变化结果如图 9-6 和图 9-7 所示。

![](image/fb7f36464e4aab84923204a3ef4d2800c845368f99021b4240f2ed0c82b6b4d1.jpg)

<details>
<summary>line</summary>

| time(s) | ideal position | position tracking |
| --- | --- | --- |
| 0.00 | 1.0 | 0.0 |
| 0.05 | 1.0 | 1.0 |
| 0.10 | 1.0 | 1.1 |
| 0.15 | 1.0 | 1.0 |
| 0.20 | 1.0 | 1.0 |
| 0.25 | 1.0 | 1.0 |
</details>

图 9-6 二次型性能指标学习单神经元自适应 PID 位置跟踪

![](image/4db71d024a751ba4f6471fa2616e75244ecbebbc38308080f96d25cc4c646b05.jpg)

<details>
<summary>line</summary>

| time(s) | wkp | wki | wkd |
| --- | --- | --- | --- |
| 0.00 | 0.34 | 0.32 | 0.35 |
| 0.05 | 0.31 | 0.318 | 0.29 |
| 0.10 | 0.31 | 0.318 | 0.29 |
| 0.15 | 0.31 | 0.318 | 0.29 |
| 0.20 | 0.31 | 0.318 | 0.29 |
| 0.25 | 0.31 | 0.318 | 0.29 |
</details>

图 9-7 单神经元 PID 控制过程中权值变化

〖仿真程序〗 chap9\_2.m  
```matlab
%Single Neural Net PID Controller based on Second Type Learning Algorithm
clear all;
close all;

xc=[0,0,0]';
K=0.02;P=2;Q=1;d=6;
xiteP=120;
xiteI=4;
xiteD=159;

%Initilizing kp,ki and kd
wkp_1=rand;
wiki_1=rand;
wkd_1=rand;

wkp_1=0.34;
wiki_1=0.32;
wkd_1=0.33;

error_1=0;error_2=0;
y_1=0;y_2=0;
u_1=0.1726;u_2=0;u_3=0;u_4=0;u_5=0;u_6=0;u_7=0;

ts=0.001;
for k=1:1:250 
```

```matlab
time(k)=k*ts;
yd(k)=1.0; %Tracing Step Signal

ym(k)=0;
if k==100
    ym(k)=0.10; %Disturbance
end
y(k)=0.368*y_1+0.26*y_2+u_6+0.632*u_7+ym(k);
error(k)=yd(k)-y(k);

wx=[wkp_1,wkd_1,wki_1];
wx=wx*xc;

b0=y(1);
K=0.0175;
wkp(k)=wkp_1+xiteP*K*[P*b0*error(k)*xc(1)-Q*K*wx*xc(1)];
wiki(k)=wiki_1+xiteI*K*[P*b0*error(k)*xc(2)-Q*K*wx*xc(2)];
wkd(k)=wkd_1+xiteD*K*[P*b0*error(k)*xc(3)-Q*K*wx*xc(3rows);
xc(1)=error(k)-error_1; %P
xc(2)=error(k); %I
xc(3)=error(k)-2*error_1+error_2; %D

wadd(k)=abs(wkp(k))+abs(wki(k))+abs(wkd(k));
w11(k)=wkp(k)/wadd(k);
w22(k)=wiki(k)/wadd(k);
w33(k)=wkd(k)/wadd(k);
w=[w11(k),w22(k),w33(k)];
u(k)=u_1+K*w*xc; % Control law

if u(k)>10
    u(k)=10;
end
if u(k)<-10
    u(k)=-10;
end

error_2=error_1;
error_1=error(k);
