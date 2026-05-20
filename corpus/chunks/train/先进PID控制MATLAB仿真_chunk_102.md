# 【仿真之一】采用 M 语言进行仿真

取 M=1，采用积分分离式 PID 控制器进行阶跃响应，对积分分离式 PID 控制算法进行改进，采用分段积分分离方式，即根据误差绝对值的不同，采用不同的积分强度。仿真中指令信号为 $y_{\mathrm{d}}(k)=40$ ，控制器输出限制在 $[-110,110]$ ，其阶跃式跟踪结果如图 1-23 所示。取 M=2，采用普通 PID 控制，其阶跃式跟踪结果如图 1-24 所示。

![](image/64074dae9a9d107740fa020356bc63dd7bf54429359fb9cc7c60200239d92f84.jpg)

<details>
<summary>line</summary>

| time(s) | Ideal position signal | Position tracking |
| --- | --- | --- |
| 0 | 0 | 0 |
| 500 | 38 | 38 |
| 1000 | 39 | 39 |
| 1500 | 39 | 39 |
| 2000 | 38 | 38 |
| 2500 | 36 | 36 |
| 3000 | 32 | 32 |
| 3500 | 28 | 28 |
| 4000 | 24 | 24 |
</details>

图 1-23 积分分离式 PID 阶跃跟踪 (M=1)

![](image/04eb26aea95efabf553b09ea84529307e4fc73c894104267eaf97fa44e46ebb1.jpg)

<details>
<summary>line</summary>

| time(s) | Ideal position signal | Position tracking |
| --- | --- | --- |
| 0 | 0 | 0 |
| 500 | 38 | 30 |
| 1000 | 40 | 38 |
| 1500 | 40 | 40 |
| 2000 | 40 | 40 |
| 2500 | 40 | 40 |
| 3000 | 40 | 40 |
| 3500 | 40 | 40 |
| 4000 | 40 | 40 |
</details>

图 1-24 采用普通 PID 阶跃跟踪（M=2）

〖仿真程序〗 chap1\_13.m

```txt
%Integration Separation PID Controller
clear all;
close all;
```

```matlab
ts=20;
%Delay plant
sys=tf([1],[60,1],'inputdelay',80);
dsys=c2d(sys,ts,'zoh');
[num,den]=tfdata(dsys,'v');

u_1=0;u_2=0;u_3=0;u_4=0;u_5=0;
y_1=0;y_2=0;y_3=0;
error_1=0;error_2=0;
ei=0;
for k=1:1:200
time(k)=k*ts;

%Delay plant
y(k)=-den(2)*y_1+num(2)*u_5;

%I separation
yd(k)=40;
error(k)=yd(k)-y(k);
ei=ei+error(k)*ts;

M=2;
if M==1    %Using integration separation
    if abs(error(k))>=30
    beta=0.0;
    elseif abs(error(k))>=20&abs(error(k))<=30
    beta=0.6;
    elseif abs(error(k))>=10&abs(error(k))<=20
    beta=0.9;
    else
    beta=1.0;
    end
elseif M==2
    beta=1.0;    %Not using integration separation
end

kp=0.80;
ki=0.005;
kd=3.0;
u(k)=kp*error(k)+kd*(error(k)-error_1)/ts+beta*ki*ei;

if u(k)>=110    % Restricting the output of controller
    u(k)=110;
end

if u(k)<=-110
    u(k)=-110;
end

u_5=u_4;u_4=u_3;u_3=u_2;u_2=u_1;u_1=u(k); 
```

```matlab
y_3=y_2;y_2=y_1;y_1=y(k);
error_2=error_1;
error_1=error(k);
end
figure(1);
plot(time,yd,'r',time,y,'k:','linewidth',2);
xlabel('time(s)');ylabel('yd,y');
legend('Ideal position signal','Position tracking');
figure(2);
plot(time,u,'r','linewidth',2);
xlabel('time(s)');ylabel('Control input'); 
```

由仿真结果可以看出，采用积分分离方法控制效果有很大的改善。值得注意的是，为保证引入积分作用后系统的稳定性不变，在输入积分作用时比例系数 $k_{p}$ 可作相应变化。此外， $\beta$ 值应根据具体对象及要求而定，若 $\beta$ 过大，则达不到积分分离的目的；若 $\beta$ 过小，则会导致无法进入积分区。如果只进行PD控制，会使控制出现余差。
