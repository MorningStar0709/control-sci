# 【仿真实例】

控制对象为

$$G (s) = \frac {5 2 3 5 0 0}{s ^ {3} + 8 7 . 3 5 s ^ {2} + 1 0 4 7 0 s}$$

采样时间为 1ms，取指令信号 $y_{\mathrm{d}}(k)=30$ ，M=1，采用抗积分饱和算法进行离散系统阶跃响应，仿真结果如图 1-27 所示。取 M=2，采用普通 PID 算法进行离散系统阶跃响应，其阶跃响应结果如图 1-28 所示。由仿真结果可以看出，采用抗积分饱和 PID 方法，可以避免控制量长时间停留在饱和区，防止系统产生超调。

![](image/bb5533498cb3ad1342a060d7b2dc69b72bf2caf384ecbdc1634cedc6a65c746a.jpg)  
图 1-27 抗积分饱和仿真结果（M=1）

![](image/568930b13393592599e33a5a28575e0655cbfdf637d36834b0696e606d668cf7.jpg)

<details>
<summary>line</summary>

| time(s) | Ideal position signal | Position tracking |
| --- | --- | --- |
| 0.0 | 0 | 0 |
| 0.1 | 30 | 20 |
| 0.2 | 45 | 45 |
| 0.3 | 35 | 35 |
| 0.4 | 30 | 30 |
| 0.5 | 30 | 30 |
| 0.6 | 30 | 30 |
| 0.7 | 30 | 30 |
| 0.8 | 30 | 30 |
</details>

![](image/9695d3ff35b142b92d027c74753d3befb92886c2c82d9a571038ed12811bdb1c.jpg)

<details>
<summary>line</summary>

| time(s) | Control input |
| --- | --- |
| 0.0 | 5 |
| 0.1 | 5 |
| 0.2 | -5 |
| 0.3 | 0 |
| 0.4 | 0 |
| 0.5 | 0 |
| 0.6 | 0 |
| 0.7 | 0 |
| 0.8 | 0 |
</details>

![](image/9ab73c2cd4338dea5ccf06e08a3757e59f50bcea4e9a696d38a5f9632b789e2a.jpg)

<details>
<summary>line</summary>

| time(s) | Integration |
| --- | --- |
| 0.0 | 0.0 |
| 0.1 | 1.8 |
| 0.2 | 1.0 |
| 0.3 | 0.3 |
| 0.4 | 0.1 |
| 0.5 | 0.0 |
| 0.6 | 0.0 |
| 0.7 | 0.0 |
| 0.8 | 0.0 |
</details>

图 1-28 普通 PID 算法进行离散系统阶跃响应结果（M=2）

〖仿真程序〗 chap1\_15.m  
```matlab
%PID Controller with intergration sturation
clear all;
close all;

ts=0.001;
sys=tf(5.235e005,[1,87.35,1.047e004,0]);
dsys=c2d(sys,ts,'z');
[num,den]=tfdata(dsys,'v');

u_1=0.0;u_2=0.0;u_3=0.0;
y_1=0;y_2=0;y_3=0;

x=[0,0,0]';
error_1=0;

um=6;
kp=0.85;ki=9.0;kd=0.0;
for k=1:1:800
time(k)=k*ts;

yd(k)=30;    %Step Signal
u(k)=kp*x(1)+kd*x(2)+ki*x(3);    % PID Controller

if u(k)>=um
    u(k)=um;
end

if u(k)<=-um
    u(k)=-um;
end

%Linear model
y(k)=-den(2)*y_1-den(3)*y_2-den(4)*y_3+num(2)*u_1+num(3)*u_2+num(4)*u_3;

error(k)=yd(k)-y(k);

M=2;
if M==1    %Using intergration sturation
if u(k)>=um
    if error(k)>0
    alpha=0;
    else
    alpha=1;
    end
elseif u(k)<=-um 
```

```matlab
if error(k)>0
    alpha=1;
else
    alpha=0;
end
else
    alpha=1;
end

elseif M==2 %Not using intergration sturation
    alpha=1;
end

%Return of PID parameters
u_3=u_2;u_2=u_1;u_1=u(k);
y_3=y_2;y_2=y_1;y_1=y(k);
error_1=error(k);

x(1)=error(k); % Calculating P
x(2)=(error(k)-error_1)/ts; % Calculating D
x(3)=x(3)+alpha*error(k)*ts; % Calculating I

xi(k)=x(3);
end
figure(1);
subplot(311);
plot(time,yd,'r',time,y,'k:',linewidth',2);
xlabel('time(s)');ylabel('yd,y');
legend('Ideal position signal','Position tracking');
subplot(312);
plot(time,u,'r','linewidth',2);
xlabel('time(s)');ylabel('Control input');
subplot(313);
plot(time,xi,'r','linewidth',2);
xlabel('time(s)');ylabel('Integration'); 
```

![](image/cb79fe5ba0de230171a0bc49bb35a1193ead2cce2af79343e0f0656b053e9524.jpg)
