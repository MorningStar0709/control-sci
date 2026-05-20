# 【仿真实例】

设被控对象为一延迟对象

$$G (s) = \frac {e ^ {- 8 0 s}}{6 0 s + 1}$$

采样时间为 20s，延迟时间为 4 个采样时间，即 80s，取 $k_{p}=0.45$ ， $k_{d}=12$ ， $k_{i}=0.0048$ ，A=0.4，B=0.6。取 M=1，采用变速积分 PID 控制算法进行阶跃响应，其结果如图 1-29 和图 1-30 所示。取 M=2，采用普通 PID 控制，其结果如图 1-31 所示。由仿真结果可以看出，变速积分与积分分离两种控制方法很类似，但调节方式不同，前者对积分项采用的是缓慢变化，而后者则采用所谓“开关”控制。变速积分调节质量更高。

![](image/6ee40db1f27c783359a2d486dac923afba8c21ac318c7ac94e606cb6dffded3a.jpg)

<details>
<summary>line</summary>

| time(s) | Ideal position signal | Position tracking |
| --- | --- | --- |
| 0 | 1.0 | 0.0 |
| 500 | 1.0 | 1.0 |
| 1000 | 1.0 | 1.0 |
| 1500 | 1.0 | 1.0 |
| 2000 | 1.0 | 1.0 |
| 2500 | 1.0 | 1.0 |
| 3000 | 1.0 | 1.0 |
| 3500 | 1.0 | 1.0 |
| 4000 | 1.0 | 1.0 |
</details>

图 1-29 变速积分阶跃响应（M=1）  
![](image/b421c6a18433d2cd834bd248f7dcc9fe3032b1e9b3baac8a2bb673241083ef27.jpg)

<details>
<summary>line</summary>

| time(s) | Integration rate f |
| --- | --- |
| 0 | 1.0 |
| 500 | 1.0 |
| 1000 | 1.0 |
| 1500 | 1.0 |
| 2000 | 1.0 |
| 2500 | 0.8 |
| 3000 | 0.6 |
| 3500 | 0.5 |
| 4000 | 0.4 |
</details>

图 1-30 变速积分参数的变化  
![](image/c418c32aa4c485cb57df28ab5c94f3eebca80a87b686079a3872ad7313e22c3c.jpg)

<details>
<summary>line</summary>

| time(s) | Ideal position signal | Position tracking |
| --- | --- | --- |
| 0 | 0.0 | 0.0 |
| 500 | 0.95 | 0.95 |
| 1000 | 1.0 | 1.0 |
| 1500 | 1.0 | 1.0 |
| 2000 | 1.0 | 1.0 |
| 2500 | 1.0 | 1.0 |
| 3000 | 1.0 | 1.0 |
| 3500 | 1.0 | 1.0 |
| 4000 | 1.0 | 1.0 |
</details>

图 1-31 普通 PID 控制阶跃响应 (M=2)

〖仿真程序〗 chap1\_16.m

```matlab
clear all;
close all;
%Big time delay Plant
ts=20;
sys=tf([1],[60,1],'inputdelay',80);
dsys=c2d(sys,ts,'zoh');
[num,den]=tfdata(dsys,'v');

u_1=0;u_2=0;u_3=0;u_4=0;u_5=0;
y_1=0;y_2=0;y_3=0;
error_1=0;error_2=0;
ei=0;

for k=1:1:200
time(k)=k*ts;

yd(k)=1.0; %Step Signal

%Linear model
y(k)=-den(2)*y_1+num(2)*u_5;
error(k)=yd(k)-y(k);

kp=0.45;kd=12;ki=0.0048;
A=0.4;B=0.6;

%T type integration
ei=ei+(error(k)+error_1)/2*ts;

M=1;
if M==1 %Changing integration rate
if abs(error(k))<=B
    f(k)=1;
elseif abs(error(k))>B&abs(error(k))<=A+B
    f(k)=(A-abs(error(k))+B)/A;
else
    f(k)=0;
end
elseif M==2 %Not changing integration rate
    f(k)=1;
end

u(k)=kp*error(k)+kd*(error(k)-error_1)/ts+ki*f(k)*ei;

if u(k)>=10
    u(k)=10;
end
if u(k)<=-10
    u(k)=-10;
end 
```

```matlab
%Return of PID parameters
u_5=u_4;u_4=u_3;u_3=u_2;u_2=u_1;u_1=u(k);
y_3=y_2;y_2=y_1;y_1=y(k);
error_2=error_1;
error_1=error(k);
end
figure(1);
plot(time,yd,'r',time,y,'k:','linewidth',2);
xlabel('time(s)');ylabel('yd,y');
legend('Ideal position signal','Position tracking');
figure(2);
plot(time,f,'r','linewidth',2);
xlabel('time(s)');ylabel('Integration rate f'); 
```

![](image/04d18ee395d0789b569079c7d26bbe34e5d854cb5468bd268f4ccb1ee9866d7d.jpg)
