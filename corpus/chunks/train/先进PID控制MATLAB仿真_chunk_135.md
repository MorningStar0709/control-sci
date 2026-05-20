# 【仿真之一】采用 M 语言进行仿真

控制干扰信号 $w(k)$ 和测量噪声信号 $v(k)$ 幅值均为 0.10 的白噪声信号，输入信号幅值为 1.0、频率为 1.5Hz 的正弦信号。采用卡尔曼滤波器实现信号的滤波，取 Q=1, R=1。仿真时间为 3s，原始信号及带有噪声的原始信号、原始信号及滤波后的信号和误差协方差的变化分别如图 1-57～1-59 所示。仿真结果表明，该滤波器对控制干扰和测量噪声具有很好的滤波作用。

![](image/1504f0799672e6945bb1e3e1fec26046b07dd36943f99f1973239125e63806b4.jpg)

<details>
<summary>line</summary>

| time(s) | ideal signal | signal with noise |
| --- | --- | --- |
| 0.0 | 0.0 | 0.0 |
| 0.5 | 1.2 | 1.1 |
| 1.0 | 0.0 | 0.0 |
| 1.5 | 1.2 | 1.1 |
| 2.0 | 0.0 | 0.0 |
| 2.5 | 1.2 | 1.1 |
| 3.0 | 0.0 | 0.0 |
</details>

图 1-57 原始信号及带有噪声的原始信号

![](image/70270a5c5258f4c5105b674bb2dc5bef2428bda3e14e4b14580e23afb0c5c39c.jpg)

<details>
<summary>line</summary>

| time(s) | ideal signal | filtered signal |
| --- | --- | --- |
| 0.0 | 0.0 | 0.0 |
| 0.5 | 1.1 | 1.1 |
| 1.0 | 0.0 | 1.1 |
| 1.5 | 1.1 | 1.1 |
| 2.0 | 0.0 | 1.1 |
| 2.5 | 1.1 | 1.1 |
| 3.0 | 0.0 | 1.1 |
</details>

图 1-58 原始信号及滤波后的信号  
![](image/5fc6540651e2cf0073025cbd71ccd231e97c7b88699472d695ca5ac9ae7be42a.jpg)

<details>
<summary>line</summary>

| time(s) | Covariance of estimation error (×10⁻³) |
| --- | --- |
| 0.0 | 0.0 |
| 0.5 | 4.8 |
| 1.0 | 4.9 |
| 1.5 | 4.95 |
| 2.0 | 4.97 |
| 2.5 | 4.98 |
| 3.0 | 4.99 |
</details>

图 1-59 误差协方差的变化

〖仿真程序〗 chap1\_26.m  
```matlab
%Kalman filter
%x=Ax+B(u+w(k));
%y=Cx+D+v(k)
clear all;
close all;

ts=0.001;
M=3000;

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

ye=zeros(M,1);
ycov=zeros(M,1);

u_1=0;u_2=0;
y_1=0;y_2=0;

for k=1:1:M
time(k)=k*ts;

w(k)=0.10*rands(1); %Process noise on u
v(k)=0.10*rands(1); %Measurement noise on y

u(k)=1.0*sin(2*pi*1.5*k*ts);
u(k)=u(k)+w(k);

y(k)=-den(2)*y_1-den(3)*y_2+num(2)*u_1+num(3)*u_2;
yv(k)=y(k)+v(k);

%Measurement update 
```

```matlab
Mn=P*C'/(C*P*C'+R);
P=A*P*A'+B*Q*B';
P=(eye(2)-Mn*C)*P;

x=A*x+Mn*(yv(k)-C*A*x);
ye(k)=C*x+D; %Filtered value

errcov(k)=C*P*C'; %Covariance of estimation error

%Time update
x=A*x+B*u(k);

u_2=u_1;u_1=u(k);
y_2=y_1;y_1=ye(k);

end

figure(1);

plot(time,y,'r',time,yv,'k:','linewidth',2);
xlabel('time(s)');ylabel('y,yv')

legend('ideal signal','signal with noise');
figure(2);

plot(time,y,'r',time,ye,'k:','linewidth',2);
xlabel('time(s)');ylabel('y,ye')

legend('ideal signal','filtered signal');
figure(3);

plot(time,errcov,'k','linewidth',2);
xlabel('time(s)');ylabel('Covariance of estimation error'); 
```
