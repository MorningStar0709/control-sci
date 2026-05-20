# 【仿真实例】

采用卡尔曼滤波器的 PID 控制。被控对象为二阶传递函数

$$G _ {\mathrm{p}} (s) = \frac {1 3 3}{s ^ {2} + 2 5 s}$$

离散化结果与“1. 卡尔曼滤波器原理”的仿真实例相同。采样时间为 1ms。控制干扰信号 $w(k)$ 和测量噪声信号 $v(k)$ 幅值均为 0.002 的白噪声信号，输入信号为一阶跃信号。采用卡尔曼滤波器实现信号的滤波，取 Q=1，R=1。仿真时间为 1s。分两种情况进行仿真：M=1 时为未加滤波，M=2 时为加滤波。在 PID 控制器中，取 $k_{p}=8.0$ ， $k_{i}=0.80$ ， $k_{d}=0.20$ 。加入滤波器前后 PID 阶跃响应如图 1-63 和图 1-64 所示，仿真结果表明，通过采用滤波器使控制效果明显改善。

本方法的不足之处是设计卡尔曼滤波器时需要被控对象的精确模型。

![](image/1643b783a0d4f7fba6940a4625e033682213db141609b81cd3cba2bea731b779.jpg)

<details>
<summary>line</summary>

| time(s) | Ideal position signal | Position tracking |
| --- | --- | --- |
| 0.0 | 1.0 | 0.0 |
| 0.1 | 1.0 | 1.15 |
| 0.2 | 1.0 | 0.78 |
| 0.3 | 1.0 | 1.1 |
| 0.4 | 1.0 | 0.95 |
| 0.5 | 1.0 | 0.85 |
| 0.6 | 1.0 | 1.1 |
| 0.7 | 1.0 | 0.95 |
| 0.8 | 1.0 | 1.2 |
| 0.9 | 1.0 | 0.9 |
| 1.0 | 1.0 | 1.05 |
</details>

图 1-63 无滤波器时 PID 控制阶跃响应 (M=1)  
![](image/7b99244f2ca36354e9f930b7a6de3c10d9812dc3c0500f2411d7704c4f5fdcf2.jpg)

<details>
<summary>line</summary>

| time(s) | Ideal position signal | Position tracking |
| --- | --- | --- |
| 0.0 | 0.0 | 0.0 |
| 0.1 | 1.0 | 1.0 |
| 0.2 | 1.0 | 1.0 |
| 0.3 | 1.0 | 1.0 |
| 0.4 | 1.0 | 1.0 |
| 0.5 | 1.0 | 1.0 |
| 0.6 | 1.0 | 1.0 |
| 0.7 | 1.0 | 1.0 |
| 0.8 | 1.0 | 1.0 |
| 0.9 | 1.0 | 1.0 |
| 1.0 | 1.0 | 1.0 |
</details>

图 1-64 加入滤波器后 PID 控制阶跃响应 (M=2)

〖仿真程序〗 chap1\_28.m  
```matlab
%Discrete Kalman filter for PID control
%Reference kalman_2rank.m
%x=Ax+B(u+w(k));
%y=Cx+D+v(k)
clear all;
close all;

ts=0.001;
%Continuous Plant
a=25;b=133;
sys=tf(b,[1,a,0]);
dsys=c2d(sys,ts,'z');
[num,den]=tfdata(dsys,'v');

A1=[0 1;0 -a];
B1=[0;b];
C1=[1 0];
D1=[0];
[A,B,C,D]=c2dm(A1,B1,C1,D1,ts,'z');

Q=1; %Covariances of w
R=1; %Covariances of v

P=B*Q*B'; %Initial error covariance
x=zeros(2,1); %Initial condition on the state

u_1=0;u_2=0;
y_1=0;y_2=0;
ei=0;
error_1=0;
for k=1:1:1000
time(k)=k*ts;

yd(k)=1;
kp=8.0;ki=0.80;kd=0.20;

w(k)=0.002*rands(1); %Process noise on u
v(k)=0.002*rands(1); %Measurement noise on y

y(k)=-den(2)*y_1-den(3)*y_2+num(2)*u_1+num(3)*u_2;
yv(k)=y(k)+v(k);

%Measurement update
Mn=P*C'/(C*P*C'+R);
P=A*P*A'+B*Q*B';
P=(eye(2)-Mn*C)*P; 
```

```matlab
x=A*x+Mn*(yv(k)-C*A*x);
ye(k)=C*x+D; %Filtered value
M=1;
if M==1 %No kalman filter
    yout(k)=yv(k);
elseif M==2 %Using kalman filter
    yout(k)=ye(k);
end
error(k)=yd(k)-yout(k);
ei=ei+error(k)*ts;

u(k)=kp*error(k)+ki*ei+kd*(error(k)-error_1)/ts; %PID
u(k)=u(k)+w(k);

errcov(k)=C*P*C'; %Covariance of estimation error

%Time update
x=A*x+B*u(k);

u_2=u_1;u_1=u(k);
y_2=y_1;y_1=yout(k);
error_1=error(k);
end
figure(1);
plot(time,yd,'r',time,yout,'k:','linewidth',2);
xlabel('time(s)');ylabel('yd,yout');
legend('Ideal position signal','Position tracking'); 
```

![](image/ff66e26c1ea926475a9ccca71c40d431ab37ae78e2352f8f6ea5cb5f93982fbc.jpg)
