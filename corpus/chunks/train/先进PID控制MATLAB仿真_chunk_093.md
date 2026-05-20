# 【仿真之一】指令为阶跃信号、正弦信号和方波信号

设计离散 PID 控制器。其中，S 为信号选择变量，S=1 时为阶跃跟踪，S=2 时为方波跟踪，S=3 时为正弦跟踪。PID 阶跃跟踪结果如图 1-13～图 1-15 所示。

![](image/70b1c4d995f3d838fa5de5a148f08932f3d81a651e97bb3119b72f6ad7afe307.jpg)

<details>
<summary>line</summary>

| time(s) | Ideal position signal | Position tracking |
| --- | --- | --- |
| 0.00 | 0.0 | 0.0 |
| 0.05 | 0.8 | 0.8 |
| 0.10 | 0.95 | 0.95 |
| 0.15 | 1.0 | 1.0 |
| 0.20 | 1.0 | 1.0 |
| 0.25 | 1.0 | 1.0 |
| 0.30 | 1.0 | 1.0 |
| 0.35 | 1.0 | 1.0 |
| 0.40 | 1.0 | 1.0 |
| 0.45 | 1.0 | 1.0 |
| 0.50 | 1.0 | 1.0 |
</details>

图 1-13 PID 阶跃跟踪 (S=1)

![](image/8184cffcb2df2a437dbae940cccfcce55650d17f5d30159feda5dcf2aa5dd3a5.jpg)

<details>
<summary>line</summary>

| time(s) | Ideal position signal | Position tracking |
| --- | --- | --- |
| 0.00 | 0.0 | 0.0 |
| 0.05 | 0.8 | 0.8 |
| 0.10 | 0.9 | 0.9 |
| 0.15 | 0.95 | 0.95 |
| 0.20 | 0.98 | 0.98 |
| 0.25 | 1.0 | 1.0 |
| 0.30 | -1.0 | -0.8 |
| 0.35 | -1.0 | -0.9 |
| 0.40 | -1.0 | -1.0 |
| 0.45 | -1.0 | -1.0 |
| 0.50 | -1.0 | -1.0 |
</details>

图 1-14 PID 方波跟踪 (S=2)

![](image/bbb855793b01669a2f7d79ce34bf42da8f8a78938d96302d91bfabceabcec0a8.jpg)

<details>
<summary>line</summary>

| time(s) | Ideal position signal | Position tracking |
| --- | --- | --- |
| 0.00 | 0.00 | 0.00 |
| 0.05 | 0.30 | 0.28 |
| 0.10 | 0.48 | 0.47 |
| 0.15 | 0.50 | 0.49 |
| 0.20 | 0.40 | 0.38 |
| 0.25 | 0.20 | 0.18 |
| 0.30 | -0.10 | -0.12 |
| 0.35 | -0.45 | -0.47 |
| 0.40 | -0.50 | -0.52 |
| 0.45 | -0.30 | -0.32 |
| 0.50 | 0.00 | 0.00 |
</details>

图 1-15 PID 正弦跟踪 (S=3)

〖仿真程序〗 chap1\_9.m  
```matlab
%PID Controller
clear all;
close all;

ts=0.001;
sys=tf(5.235e005,[1,87.35,1.047e004,0]);
dsys=c2d(sys,ts,'z');
[num,den]=tfdata(dsys,'v');

u_1=0.0;u_2=0.0;u_3=0.0;
y_1=0.0;y_2=0.0;y_3=0.0;
x=[0,0,0]';
error_1=0;
for k=1:1:500 
```

```matlab
time(k)=k*ts;
S=3;
if S==1
    kp=0.50;ki=0.001;kd=0.001;
    yd(k)=1; %Step Signal
elseif S==2
    kp=0.50;ki=0.001;kd=0.001;
    yd(k)=sign(sin(2*2*pi*k*ts)); %Square Wave Signal
elseif S==3
    kp=1.5;ki=1.0;kd=0.01; %Sine Signal
    yd(k)=0.5*sin(2*2*pi*k*ts);
end

u(k)=kp*x(1)+kd*x(2)+ki*x(3); %PID Controller
%Restricting the output of controller
if u(k)>=10
    u(k)=10;
end
if u(k)<=-10
    u(k)=-10;
end
%Linear model
y(k)=-den(2)*y_1-den(3)*y_2-den(4)*y_3+num(2)*u_1+num(3)*u_2+num(4)*u_3;
error(k)=yd(k)-y(k);

%Return of parameters
u_3=u_2;u_2=u_1;u_1=u(k);
y_3=y_2;y_2=y_1;y_1=y(k);

x(1)=error(k); %Calculating P
x(2)=(error(k)-error_1)/ts; %Calculating D
x(3)=x(3)+error(k)*ts; %Calculating I

error_1=error(k);
end

figure(1);
plot(time,yd,'r',time,y,'k:',linewidth',2);
xlabel('time(s)');ylabel('yd,y');
legend('Ideal position signal','Position tracking'); 
```
