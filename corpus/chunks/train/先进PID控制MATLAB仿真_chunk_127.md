# 【仿真实例】

被控对象为

$$G (s) = \frac {1 3 3}{s ^ {2} + 2 5 s}$$

输入信号为 $y_{\mathrm{d}}(k)=0.5\sin(6\pi t)$ ，采样时间为 1ms。

$$u _ {\mathrm{f}} (t) = \frac {2 5}{1 3 3} \dot {y} _ {\mathrm{d}} (t) + \frac {1}{1 3 3} \ddot {y} _ {\mathrm{d}} (t)$$

只采用 PID 正弦跟踪控制方法的结果如图 1-49 所示。采用前馈 PID 控制方法的跟踪结果如图 1-50 所示。可见通过前馈补偿可大大提高系统的跟踪性能。

本方法的不足之处是需要被控对象的精确模型。

![](image/ec5be339d7e95a1268304febc29d516c2625eb4f2ce3c271666f3e254db0e980.jpg)  
图 1-49 PID 正弦跟踪及跟踪误差（M=1）

![](image/289e38b18913f79a3e33462f3630e7b9fe90c827a35c2eb98e3336b47d5ae0c8.jpg)

<details>
<summary>line</summary>

| time(s) | Ideal position signal | Position tracking |
| --- | --- | --- |
| 0.0 | 0.0 | 0.0 |
| 0.1 | 0.5 | 0.5 |
| 0.2 | 0.0 | 0.0 |
| 0.3 | -0.5 | -0.5 |
| 0.4 | 0.5 | 0.5 |
| 0.5 | 0.0 | 0.0 |
| 0.6 | -0.5 | -0.5 |
| 0.7 | 0.5 | 0.5 |
| 0.8 | 0.0 | 0.0 |
| 0.9 | -0.5 | -0.5 |
| 1.0 | 0.0 | 0.0 |
</details>

![](image/44c694f17700db0b57f19d63d24de63345750a057ece045392aff84d3760319c.jpg)

<details>
<summary>line</summary>

| time(s) | error |
| --- | --- |
| 0.0 | 0.045 |
| 0.1 | 0.005 |
| 0.2 | 0.001 |
| 0.3 | 0.0005 |
| 0.4 | 0.0002 |
| 0.5 | 0.0001 |
| 0.6 | 0.0001 |
| 0.7 | 0.0001 |
| 0.8 | 0.0001 |
| 0.9 | 0.0001 |
| 1.0 | 0.0001 |
</details>

图 1-50 PID+前馈补偿正弦跟踪及跟踪误差（M=2）

〖仿真程序〗 chap1\_23.m  
```matlab
%PID Feedforward Controller
clear all;
close all;

ts=0.001;
sys=tf(133,[1,25,0]);
dsys=c2d(sys,ts,'z');
[num,den]=tfdata(dsys,'v');

u_1=0;u_2=0;
y_1=0;y_2=0;

error_1=0;ei=0;
for k=1:1:1000
time(k)=k*ts;

A=0.5;F=3.0;
yd(k)=A*sin(F*2*pi*k*ts);
dyd(k)=A*F*2*pi*cos(F*2*pi*k*ts);
ddyd(k)=-A*F*2*pi*F*2*pi*sin(F*2*pi*k*ts);

%Linear model
y(k)=-den(2)*y_1-den(3)*y_2+num(2)*u_1+num(3)*u_2;

error(k)=yd(k)-y(k);

ei=ei+error(k)*ts;

up(k)=80*error(k)+20*ei+2.0*(error(k)-error_1)/ts; 
```

```matlab
uf(k)=25/133*dyd(k)+1/133*ddyd(k);

M=2;
if M==1 %Only using PID
    u(k)=up(k);
elseif M==2 %PID+Feedforward
    u(k)=up(k)+uf(k);
end

if u(k)>=10
    u(k)=10;
end

if u(k)<=-10
    u(k)=-10;
end

u_2=u_1;u_1=u(k);
y_2=y_1;y_1=y(k);
error_1=error(k);
end

figure(1);
subplot(211);
plot(time,yd,'r',time,y,'k:',linewidth',2);
xlabel('time(s)');ylabel('yd,y');
legend('Ideal position signal','Position tracking');
subplot(212);
plot(time,error,'r','linewidth',2);
xlabel('time(s)');ylabel('error');
figure(2);
plot(time,up,'k',time,uf,'b',time,u,'r','linewidth',2);
xlabel('time(s)');ylabel('up,uf,u'); 
```

![](image/9056107da28cf3a5d1e1c0b55b011046dc7c61082dcfa21c4f99427c1a6f5e93.jpg)
