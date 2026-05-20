# 【仿真实例】

采用第一种不完全微分算法，被控对象为一时滞系统传递函数

$$G (s) = \frac {\mathrm{e} ^ {- 8 0 s}}{6 0 s + 1}$$

在对象的输出端加幅值为 0.01 的随机信号 $n(k)$ 。采样时间为 20ms。

低通滤波器为

$$Q (s) = \frac {1}{1 8 0 s + 1}$$

取 M=1，采用具有不完全微分 PID 方法，其控制阶跃响应结果如图 1-40 所示。取 M=2，采用普通 PID 方法，阶跃响应结果如图 1-41 所示。由仿真结果可以看出，引入不完全微分后，能有效地克服普通 PID 的不足。尽管不完全微分 PID 控制算法比普通 PID 控制算法要复杂些，但由于其良好的控制特性，近年来越来越得到广泛的应用。

![](image/e00193e969558650b79fca4d1833ce9cd5f531d6c73a4bf5801c10a2fc2f63c4.jpg)

<details>
<summary>line</summary>

| time(s) | Ideal position signal | Position tracking |
| --- | --- | --- |
| 0 | 1.0 | 0.0 |
| 200 | 1.0 | 0.8 |
| 400 | 1.0 | 0.9 |
| 600 | 1.0 | 1.0 |
| 800 | 1.0 | 1.0 |
| 1000 | 1.0 | 1.0 |
| 1200 | 1.0 | 1.0 |
| 1400 | 1.0 | 1.0 |
| 1600 | 1.0 | 1.0 |
| 1800 | 1.0 | 1.0 |
| 2000 | 1.0 | 1.0 |
</details>

图 1-40 不完全微分控制阶跃响应（M=1）

![](image/faaaa8a6295f1947fc8b5085908430e98c5bc71d514b67563ec781576b55e084.jpg)

<details>
<summary>line</summary>

| time(s) | Ideal position signal | Position tracking |
| --- | --- | --- |
| 0 | 1.0 | 0.0 |
| 100 | 1.0 | 0.7 |
| 200 | 1.0 | 0.3 |
| 300 | 1.0 | 0.9 |
| 400 | 1.0 | 0.7 |
| 500 | 1.0 | 1.1 |
| 600 | 1.0 | 0.9 |
| 700 | 1.0 | 1.1 |
| 800 | 1.0 | 1.0 |
| 900 | 1.0 | 1.0 |
| 1000 | 1.0 | 1.0 |
| 1100 | 1.0 | 1.0 |
| 1200 | 1.0 | 1.0 |
| 1300 | 1.0 | 1.0 |
| 1400 | 1.0 | 1.0 |
| 1500 | 1.0 | 1.0 |
| 1600 | 1.0 | 1.0 |
| 1700 | 1.0 | 1.0 |
| 1800 | 1.0 | 1.0 |
| 1900 | 1.0 | 1.0 |
| 2000 | 1.0 | 1.0 |
</details>

图 1-41 普通 PID 控制阶跃响应（M=2）

〖仿真程序〗 chap1\_20.m

```txt
%PID Controller with Partial differential clear all;
close all; 
```

```matlab
ts=20;
sys=tf([1],[60,1],'inputdelay',80);
dsys=c2d(sys,ts,'zoh');
[num,den]=tfdata(dsys,'v');

u_1=0;u_2=0;u_3=0;u_4=0;u_5=0;
ud_1=0;
y_1=0;y_2=0;y_3=0;
error_1=0;
ei=0;

for k=1:1:100
time(k)=k*ts;

yd(k)=1.0;

%Linear model
y(k)=-den(2)*y_1+num(2)*u_5;

n(k)=0.01*rands(1);
y(k)=y(k)+n(k);

error(k)=yd(k)-y(k);

%PID Controller with partly differential
ei=ei+error(k)*ts;
kc=0.30;
ki=0.0055;
TD=140;

kd=kc*TD/ts;

Tf=180;
Q=tf([1],[Tf,1]); %Low Freq Signal Filter

M=2;
if M==1 %Using PID with Partial differential
    alfa=Tf/(ts+Tf);
    ud(k)=kd*(1-alfa)*(error(k)-error_1)+alfa*ud_1;
    u(k)=kc*error(k)+ud(k)+ki*ei;
    ud_1=ud(k);
elseif M==2 %Using Simple PID
    u(k)=kc*error(k)+kd*(error(k)-error_1)+ki*ei;
end

%Restricting the output of controller
if u(k)>=10
    u(k)=10; 
```

```matlab
end
if u(k)<=-10
    u(k)=-10;
end

u_5=u_4;u_4=u_3;u_3=u_2;u_2=u_1;u_1=u(k);
y_3=y_2;y_2=y_1;y_1=y(k);
error_1=error(k);
end
figure(1);
plot(time,yd,'r',time,y,'k:',linewidth',2);
xlabel('time(s)');ylabel('yd,y');
legend('Ideal position signal','Position tracking');
figure(2);
plot(time,u,'r','linewidth',2);
xlabel('time(s)');ylabel('u');
figure(3);
bode(Q,'r');
dcgain(Q); 
```

![](image/ecdb49084a74145f7d5d0f16adae5fa712c15ada265a9c2cc8ba414917a9db31.jpg)
